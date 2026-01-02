//! Application state management

use anyhow::Result;
use std::path::PathBuf;

use crate::api::{Tip, Stats, WaitlistClient};
use crate::config::Config;

/// The current active tab
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum Tab {
    Tips,
    Draft,
    Preview,
    Stats,
}

impl Tab {
    pub fn title(&self) -> &'static str {
        match self {
            Tab::Tips => "Tips",
            Tab::Draft => "Draft",
            Tab::Preview => "Preview",
            Tab::Stats => "Stats",
        }
    }

    pub fn all() -> &'static [Tab] {
        &[Tab::Tips, Tab::Draft, Tab::Preview, Tab::Stats]
    }
}

/// Category filter for tips
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum Category {
    All,
    Orchestration,
    ContextManagement,
    Workflow,
    Subagents,
    Tooling,
}

impl Category {
    pub fn as_str(&self) -> &'static str {
        match self {
            Category::All => "All",
            Category::Orchestration => "orchestration",
            Category::ContextManagement => "context-management",
            Category::Workflow => "workflow",
            Category::Subagents => "subagents",
            Category::Tooling => "tooling",
        }
    }

    pub fn icon(&self) -> &'static str {
        match self {
            Category::All => "*",
            Category::Orchestration => "O",
            Category::ContextManagement => "C",
            Category::Workflow => "W",
            Category::Subagents => "S",
            Category::Tooling => "T",
        }
    }
}

/// Main application state
pub struct App {
    /// Current active tab
    pub current_tab: Tab,

    /// All loaded tips
    pub tips: Vec<Tip>,

    /// Currently selected tips (indices)
    pub selected_tips: Vec<usize>,

    /// Current list index for navigation
    pub list_index: usize,

    /// Category filter
    pub category_filter: Category,

    /// Draft subject line
    pub draft_subject: String,

    /// Newsletter stats from API
    pub stats: Option<Stats>,

    /// API client
    pub client: WaitlistClient,

    /// Config
    pub config: Config,

    /// UI state flags
    pub confirm_quit: bool,
    pub pending_g: bool,
    pub show_help: bool,
    pub is_loading: bool,
    pub status_message: Option<String>,

    /// Repo root path
    pub repo_root: PathBuf,
}

impl App {
    /// Create a new App instance
    pub async fn new() -> Result<Self> {
        let config = Config::load()?;
        let client = WaitlistClient::new(&config);

        // Find repo root (assume we're in automation/cli/)
        let repo_root = std::env::current_dir()?
            .ancestors()
            .find(|p| p.join("tips").exists())
            .map(|p| p.to_path_buf())
            .unwrap_or_else(|| {
                // Fallback to home directory path
                dirs::home_dir()
                    .unwrap_or_default()
                    .join("Documents/GitHub/claude-code-daily")
            });

        let mut app = Self {
            current_tab: Tab::Tips,
            tips: Vec::new(),
            selected_tips: Vec::new(),
            list_index: 0,
            category_filter: Category::All,
            draft_subject: String::new(),
            stats: None,
            client,
            config,
            confirm_quit: false,
            pending_g: false,
            show_help: false,
            is_loading: false,
            status_message: None,
            repo_root,
        };

        // Load initial data
        app.load_tips()?;
        app.refresh().await?;

        Ok(app)
    }

    /// Load tips from markdown files
    pub fn load_tips(&mut self) -> Result<()> {
        self.tips = crate::api::load_tips_from_files(&self.repo_root)?;
        self.status_message = Some(format!("Loaded {} tips", self.tips.len()));
        Ok(())
    }

    /// Get filtered tips based on category
    pub fn filtered_tips(&self) -> Vec<(usize, &Tip)> {
        self.tips
            .iter()
            .enumerate()
            .filter(|(_, tip)| {
                self.category_filter == Category::All
                    || tip.category == self.category_filter.as_str()
            })
            .collect()
    }

    /// Navigate to next tab
    pub fn next_tab(&mut self) {
        let tabs = Tab::all();
        let current_idx = tabs.iter().position(|&t| t == self.current_tab).unwrap_or(0);
        self.current_tab = tabs[(current_idx + 1) % tabs.len()];
        self.list_index = 0;
    }

    /// Navigate to previous tab
    pub fn prev_tab(&mut self) {
        let tabs = Tab::all();
        let current_idx = tabs.iter().position(|&t| t == self.current_tab).unwrap_or(0);
        self.current_tab = tabs[(current_idx + tabs.len() - 1) % tabs.len()];
        self.list_index = 0;
    }

    /// Navigate to next item in list
    pub fn next_item(&mut self) {
        let max = self.current_list_len();
        if max > 0 {
            self.list_index = (self.list_index + 1).min(max - 1);
        }
    }

    /// Navigate to previous item in list
    pub fn prev_item(&mut self) {
        if self.list_index > 0 {
            self.list_index -= 1;
        }
    }

    /// Go to top of list
    pub fn go_to_top(&mut self) {
        self.list_index = 0;
    }

    /// Go to bottom of list
    pub fn go_to_bottom(&mut self) {
        let max = self.current_list_len();
        if max > 0 {
            self.list_index = max - 1;
        }
    }

    /// Get current list length based on tab
    fn current_list_len(&self) -> usize {
        match self.current_tab {
            Tab::Tips => self.filtered_tips().len(),
            Tab::Draft => self.selected_tips.len(),
            _ => 0,
        }
    }

    /// Toggle selection of current item
    pub fn toggle_selection(&mut self) {
        if self.current_tab != Tab::Tips {
            return;
        }

        let filtered = self.filtered_tips();
        if let Some((original_idx, _)) = filtered.get(self.list_index) {
            if let Some(pos) = self.selected_tips.iter().position(|&i| i == *original_idx) {
                self.selected_tips.remove(pos);
            } else if self.selected_tips.len() < self.config.tips_per_issue {
                self.selected_tips.push(*original_idx);
            }
        }
    }

    /// Cycle through category filters
    pub fn cycle_category(&mut self) {
        if self.current_tab != Tab::Tips {
            return;
        }

        self.category_filter = match self.category_filter {
            Category::All => Category::Orchestration,
            Category::Orchestration => Category::ContextManagement,
            Category::ContextManagement => Category::Workflow,
            Category::Workflow => Category::Subagents,
            Category::Subagents => Category::Tooling,
            Category::Tooling => Category::All,
        };
        self.list_index = 0;
        self.status_message = Some(format!("Filter: {}", self.category_filter.as_str()));
    }

    /// Select all visible tips (up to limit)
    pub fn select_all(&mut self) {
        if self.current_tab != Tab::Tips {
            return;
        }

        let max = self.config.tips_per_issue;

        // Collect just the indices first, dropping references to self
        let indices: Vec<usize> = self
            .filtered_tips()
            .into_iter()
            .take(max)
            .map(|(idx, _)| idx)
            .collect();

        self.selected_tips = indices;
        self.status_message = Some(format!("Selected {} tips", self.selected_tips.len()));
    }

    /// Remove current item from draft
    pub fn remove_from_draft(&mut self) {
        if self.current_tab != Tab::Draft {
            return;
        }

        if self.list_index < self.selected_tips.len() {
            self.selected_tips.remove(self.list_index);
            if self.list_index > 0 && self.list_index >= self.selected_tips.len() {
                self.list_index = self.selected_tips.len().saturating_sub(1);
            }
            self.status_message = Some("Tip removed from draft".to_string());
        }
    }

    /// Confirm action (Enter key)
    pub async fn confirm_action(&mut self) -> Result<()> {
        match self.current_tab {
            Tab::Tips => {
                // Move selection to draft
                if !self.selected_tips.is_empty() {
                    self.current_tab = Tab::Draft;
                    self.list_index = 0;
                    self.status_message = Some(format!(
                        "{} tips added to draft",
                        self.selected_tips.len()
                    ));
                }
            }
            Tab::Draft => {
                // Preview the draft
                self.current_tab = Tab::Preview;
            }
            Tab::Preview => {
                // Confirm send?
                self.status_message = Some("Press 'S' to send newsletter".to_string());
            }
            Tab::Stats => {}
        }
        Ok(())
    }

    /// Save draft to file
    pub fn save_draft(&mut self) -> Result<()> {
        let draft_path = self.repo_root.join("automation/draft.json");
        let tips: Vec<_> = self
            .selected_tips
            .iter()
            .filter_map(|&i| self.tips.get(i).cloned())
            .collect();

        let issue_number = self
            .stats
            .as_ref()
            .map(|s| s.total_issues + 1)
            .unwrap_or(1);

        let draft = serde_json::json!({
            "issue_number": issue_number,
            "subject": format!("Claude Code Daily #{}: {} Real Use Cases", issue_number, tips.len()),
            "created_at": chrono::Utc::now().to_rfc3339(),
            "tips": tips
        });

        std::fs::write(&draft_path, serde_json::to_string_pretty(&draft)?)?;
        self.status_message = Some(format!("Draft saved to {}", draft_path.display()));
        Ok(())
    }

    /// Send newsletter via API
    pub async fn send_newsletter(&mut self) -> Result<()> {
        if self.selected_tips.is_empty() {
            self.status_message = Some("No tips selected!".to_string());
            return Ok(());
        }

        self.is_loading = true;
        self.status_message = Some("Generating newsletter...".to_string());

        // Get selected tips
        let tips: Vec<_> = self
            .selected_tips
            .iter()
            .filter_map(|&i| self.tips.get(i).cloned())
            .collect();

        let issue_number = self
            .stats
            .as_ref()
            .map(|s| s.total_issues + 1)
            .unwrap_or(1);

        // Generate HTML
        let html = crate::api::generate_newsletter_html(&tips, issue_number);
        let subject = format!("Claude Code Daily #{}: {} Real Use Cases", issue_number, tips.len());

        self.status_message = Some("Creating newsletter issue...".to_string());

        // Create issue via API
        match self.client.create_issue(&subject, &html).await {
            Ok(issue_id) => {
                self.status_message = Some(format!("Sending to subscribers... (issue: {})", issue_id));

                // Send the issue
                match self.client.send_issue(&issue_id).await {
                    Ok(count) => {
                        self.status_message = Some(format!(
                            "Newsletter sent to {} subscribers!",
                            count
                        ));
                        // Clear selection after successful send
                        self.selected_tips.clear();
                        // Refresh stats
                        let _ = self.refresh().await;
                    }
                    Err(e) => {
                        self.status_message = Some(format!("Send failed: {}", e));
                    }
                }
            }
            Err(e) => {
                self.status_message = Some(format!("Create issue failed: {}", e));
            }
        }

        self.is_loading = false;
        Ok(())
    }

    /// Refresh data from API
    pub async fn refresh(&mut self) -> Result<()> {
        self.is_loading = true;
        self.status_message = Some("Refreshing...".to_string());

        match self.client.get_stats().await {
            Ok(stats) => {
                self.stats = Some(stats);
                self.status_message = Some("Stats refreshed".to_string());
            }
            Err(e) => {
                self.status_message = Some(format!("Error: {}", e));
            }
        }

        self.is_loading = false;
        Ok(())
    }
}
