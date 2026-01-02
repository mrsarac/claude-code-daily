//! Tips loader from markdown files

use anyhow::Result;
use serde::{Deserialize, Serialize};
use std::path::Path;

/// A tip from the repository
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct Tip {
    /// Category (orchestration, context-management, etc.)
    pub category: String,

    /// Category icon
    pub icon: String,

    /// Tip title
    pub title: String,

    /// Source attribution
    pub source: String,

    /// Full content
    pub content: String,
}

/// Category to icon mapping (emoji icons)
fn category_icon(category: &str) -> &'static str {
    match category {
        "orchestration" => "🎭",
        "context-management" => "📝",
        "workflow" => "⚡",
        "subagents" => "🤖",
        "tooling" => "🔧",
        _ => "💡",
    }
}

/// Load all tips from markdown files in the repository
pub fn load_tips_from_files(repo_root: &Path) -> Result<Vec<Tip>> {
    let categories_dir = repo_root.join("tips/categories");

    if !categories_dir.exists() {
        return Ok(Vec::new());
    }

    let mut tips = Vec::new();

    for entry in std::fs::read_dir(&categories_dir)? {
        let entry = entry?;
        let path = entry.path();

        if path.extension().map_or(false, |ext| ext == "md") {
            let category = path
                .file_stem()
                .and_then(|s| s.to_str())
                .unwrap_or("unknown")
                .to_string();

            let content = std::fs::read_to_string(&path)?;
            let icon = category_icon(&category).to_string();

            // Parse markdown content
            let mut current_tip: Option<Tip> = None;

            for line in content.lines() {
                if line.starts_with("## ") {
                    // Save previous tip
                    if let Some(tip) = current_tip.take() {
                        tips.push(tip);
                    }

                    // Start new tip - remove number prefix like "1. " or "11. "
                    let raw_title = line[3..].trim();
                    let title = if raw_title.contains(". ") {
                        // Remove number prefix (e.g., "1. Title" -> "Title")
                        raw_title
                            .split_once(". ")
                            .map(|(_, t)| t.to_string())
                            .unwrap_or_else(|| raw_title.to_string())
                    } else {
                        raw_title.to_string()
                    };

                    current_tip = Some(Tip {
                        category: category.clone(),
                        icon: icon.clone(),
                        title,
                        source: String::new(),
                        content: String::new(),
                    });
                } else if let Some(ref mut tip) = current_tip {
                    // Extract source if present
                    if line.starts_with("**Source:**") {
                        tip.source = line
                            .replace("**Source:**", "")
                            .trim()
                            .to_string();
                    }
                    tip.content.push_str(line);
                    tip.content.push('\n');
                }
            }

            // Don't forget the last tip
            if let Some(tip) = current_tip {
                tips.push(tip);
            }
        }
    }

    Ok(tips)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_category_icon() {
        assert_eq!(category_icon("orchestration"), "O");
        assert_eq!(category_icon("workflow"), "W");
        assert_eq!(category_icon("unknown"), "*");
    }
}
