//! Configuration management

use anyhow::Result;
use serde::{Deserialize, Serialize};
use std::path::PathBuf;

/// Application configuration
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct Config {
    /// API base URL
    #[serde(default = "default_api_url")]
    pub api_url: String,

    /// Project ID for the API
    #[serde(default = "default_project_id")]
    pub project_id: String,

    /// Number of tips per newsletter issue
    #[serde(default = "default_tips_per_issue")]
    pub tips_per_issue: usize,

    /// Default subject template
    #[serde(default = "default_subject_template")]
    pub subject_template: String,
}

fn default_api_url() -> String {
    "https://waitlist.neurabytelabs.com".to_string()
}

fn default_project_id() -> String {
    "claudecodedaily".to_string()
}

fn default_tips_per_issue() -> usize {
    8 // Our lucky number!
}

fn default_subject_template() -> String {
    "Claude Code Daily #{issue}: {count} Real Use Cases".to_string()
}

impl Default for Config {
    fn default() -> Self {
        Self {
            api_url: default_api_url(),
            project_id: default_project_id(),
            tips_per_issue: default_tips_per_issue(),
            subject_template: default_subject_template(),
        }
    }
}

impl Config {
    /// Get the config file path
    pub fn path() -> Result<PathBuf> {
        let config_dir = directories::ProjectDirs::from("com", "neurabytelabs", "ccd-cli")
            .map(|dirs| dirs.config_dir().to_path_buf())
            .unwrap_or_else(|| {
                dirs::home_dir()
                    .unwrap_or_default()
                    .join(".config/ccd-cli")
            });

        Ok(config_dir.join("config.toml"))
    }

    /// Load config from file or create default
    pub fn load() -> Result<Self> {
        let path = Self::path()?;

        if path.exists() {
            let content = std::fs::read_to_string(&path)?;
            Ok(toml::from_str(&content)?)
        } else {
            Ok(Self::default())
        }
    }

    /// Save config to file (reserved for settings UI)
    #[allow(dead_code)]
    pub fn save(&self) -> Result<()> {
        let path = Self::path()?;

        if let Some(parent) = path.parent() {
            std::fs::create_dir_all(parent)?;
        }

        let content = toml::to_string_pretty(self)?;
        std::fs::write(&path, content)?;
        Ok(())
    }

    /// Get full API endpoint (helper for future endpoints)
    #[allow(dead_code)]
    pub fn api_endpoint(&self, path: &str) -> String {
        format!("{}/api/{}{}", self.api_url, self.project_id, path)
    }
}
