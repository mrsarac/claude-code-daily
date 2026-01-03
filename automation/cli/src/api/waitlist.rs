//! Waitlist API client

use anyhow::Result;
use serde::{Deserialize, Serialize};

use crate::config::Config;

/// Newsletter statistics (matches API response format)
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct Stats {
    pub total_subscribers: u32,
    pub confirmed_subscribers: u32,
    pub pending_subscribers: u32,
    pub total_issues: u32,
}

/// Waitlist API client
pub struct WaitlistClient {
    client: reqwest::Client,
    base_url: String,
    project_id: String,
}

impl WaitlistClient {
    /// Create a new client
    pub fn new(config: &Config) -> Self {
        Self {
            client: reqwest::Client::new(),
            base_url: config.api_url.clone(),
            project_id: config.project_id.clone(),
        }
    }

    /// Build endpoint URL
    fn endpoint(&self, path: &str) -> String {
        format!("{}/api/{}{}", self.base_url, self.project_id, path)
    }

    /// Get newsletter stats
    pub async fn get_stats(&self) -> Result<Stats> {
        let url = self.endpoint("/newsletter/stats");
        let stats: Stats = self.client.get(&url).send().await?.json().await?;
        Ok(stats)
    }

    /// Create a newsletter issue (draft)
    pub async fn create_issue(&self, subject: &str, html_content: &str) -> Result<String> {
        let url = self.endpoint("/newsletter/issues");
        let response: serde_json::Value = self
            .client
            .post(&url)
            .json(&serde_json::json!({
                "subject": subject,
                "title": subject,
                "content_html": html_content,
                "content_text": "View in browser for best experience."
            }))
            .send()
            .await?
            .json()
            .await?;

        if response["success"].as_bool().unwrap_or(false) {
            // API returns { success: true, data: { id: "..." } }
            let issue_id = response["data"]["id"]
                .as_str()
                .or_else(|| response["issue"]["id"].as_str())
                .or_else(|| response["id"].as_str())
                .ok_or_else(|| anyhow::anyhow!("No issue ID in response"))?;
            Ok(issue_id.to_string())
        } else {
            Err(anyhow::anyhow!(
                response["error"]
                    .as_str()
                    .unwrap_or("Unknown error")
                    .to_string()
            ))
        }
    }

    /// Send a newsletter issue
    pub async fn send_issue(&self, issue_id: &str) -> Result<u32> {
        let url = self.endpoint(&format!("/newsletter/issues/{}/send", issue_id));
        let response: serde_json::Value = self.client.post(&url).send().await?.json().await?;

        if response["success"].as_bool().unwrap_or(false) {
            // API returns { success: true, data: { sent: N, errors: N, total: N } }
            let count = response["data"]["sent"]
                .as_u64()
                .or_else(|| response["recipientCount"].as_u64())
                .unwrap_or(0) as u32;
            Ok(count)
        } else {
            Err(anyhow::anyhow!(
                response["error"]
                    .as_str()
                    .unwrap_or("Unknown error")
                    .to_string()
            ))
        }
    }
}
