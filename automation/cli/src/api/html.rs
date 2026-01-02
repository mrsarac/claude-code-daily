//! HTML newsletter generation - CLI style template

use crate::api::Tip;

/// Category icons for display
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

/// Generate CLI-style HTML newsletter
pub fn generate_newsletter_html(tips: &[Tip], issue_number: u32) -> String {
    let date_str = chrono::Local::now().format("%Y-%m-%d").to_string();

    let mut cases_html = String::new();

    for (i, tip) in tips.iter().enumerate() {
        let icon = category_icon(&tip.category);
        let source = if tip.source.is_empty() {
            "Community".to_string()
        } else {
            tip.source.clone()
        };

        // Clean content for HTML
        let content = tip
            .content
            .replace("**Source:**", "// source:")
            .replace("**Why it works:**", "<br><br><strong style=\"color:#06b6d4;\">Why it works:</strong>")
            .replace("**", "")
            .replace("\n\n", "</p><p style=\"margin: 8px 0; color: #a1a1aa;\">")
            .replace('\n', "<br>")
            .replace("```bash", "<pre style=\"background: #000; padding: 12px; border-radius: 4px; overflow-x: auto; margin: 12px 0; color: #22c55e;\">")
            .replace("```markdown", "<pre style=\"background: #000; padding: 12px; border-radius: 4px; overflow-x: auto; margin: 12px 0; color: #a1a1aa;\">")
            .replace("```json", "<pre style=\"background: #000; padding: 12px; border-radius: 4px; overflow-x: auto; margin: 12px 0; color: #fbbf24;\">")
            .replace("```", "</pre>");

        cases_html.push_str(&format!(
            r#"
    <div style="margin-bottom: 24px; font-family: 'SF Mono', 'Fira Code', ui-monospace, monospace;">
      <div style="background: #18181b; padding: 12px 16px; border-radius: 8px 8px 0 0; border-bottom: 1px solid #27272a;">
        <span style="color: #22c55e;">❯</span>
        <span style="color: #06b6d4;"> claude</span>
        <span style="color: #a1a1aa;"> --use-case {}</span>
      </div>
      <div style="background: #0a0a0a; padding: 16px; border-radius: 0 0 8px 8px;">
        <div style="color: #fafafa; font-size: 14px; font-weight: 600; margin-bottom: 8px;">
          {} {}
        </div>
        <div style="color: #71717a; font-size: 11px; margin-bottom: 12px;">
          // source: {}
        </div>
        <div style="color: #a1a1aa; font-size: 13px; line-height: 1.6;">
          {}
        </div>
      </div>
    </div>
"#,
            i + 1,
            icon,
            tip.title,
            source,
            content
        ));
    }

    format!(
        r#"<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Claude Code Daily #{}</title>
</head>
<body style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; margin: 0; padding: 0; background: #09090b;">
  <div style="max-width: 640px; margin: 0 auto; padding: 32px 16px;">

    <!-- Terminal Header -->
    <div style="background: #18181b; border-radius: 8px; padding: 16px; margin-bottom: 24px; border: 1px solid #27272a;">
      <div style="display: flex; align-items: center; margin-bottom: 12px;">
        <span style="width: 12px; height: 12px; border-radius: 50%; background: #ef4444; margin-right: 8px;"></span>
        <span style="width: 12px; height: 12px; border-radius: 50%; background: #eab308; margin-right: 8px;"></span>
        <span style="width: 12px; height: 12px; border-radius: 50%; background: #22c55e;"></span>
        <span style="color: #71717a; font-size: 12px; margin-left: auto; font-family: ui-monospace, monospace;">claude-code-daily</span>
      </div>
      <div style="color: #06b6d4; font-size: 20px; font-weight: 600;">
        Claude Code Daily
      </div>
      <div style="color: #52525b; font-size: 12px; margin-top: 4px; font-family: ui-monospace, monospace;">
        Issue #{} • {} • {} real use cases
      </div>
    </div>

    <!-- Intro as command -->
    <div style="margin-bottom: 24px; padding: 12px 16px; background: #0a0a0a; border-radius: 8px; font-family: ui-monospace, monospace;">
      <span style="color: #22c55e;">❯</span>
      <span style="color: #a1a1aa;"> cat intro.md</span>
      <p style="color: #d4d4d8; margin: 12px 0 0; font-size: 13px; line-height: 1.6;">
        This week's collection: <span style="color: #06b6d4;">{} real use cases</span> from developers
        who've cracked the code on Claude Code workflows. Each one tested in production.
      </p>
    </div>

    <!-- Use Cases -->
    {}

    <!-- Footer -->
    <div style="margin-top: 32px; padding: 16px; background: #18181b; border-radius: 8px; text-align: center; font-family: ui-monospace, monospace;">
      <div style="color: #52525b; font-size: 11px;">
        <span style="color: #22c55e;">❯</span> curated from reddit & claude code community
      </div>
      <div style="color: #3f3f46; font-size: 10px; margin-top: 8px;">
        <a href="{{{{unsubscribe_url}}}}" style="color: #3f3f46;">unsubscribe</a> •
        <a href="https://mustafasarac.com" style="color: #3f3f46;">mustafasarac.com</a>
      </div>
    </div>

  </div>
</body>
</html>"#,
        issue_number,
        issue_number,
        date_str,
        tips.len(),
        tips.len(),
        cases_html
    )
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_generate_html() {
        let tips = vec![Tip {
            category: "workflow".to_string(),
            icon: "⚡".to_string(),
            title: "Test Tip".to_string(),
            source: "Test Source".to_string(),
            content: "Test content here.".to_string(),
        }];

        let html = generate_newsletter_html(&tips, 1);
        assert!(html.contains("Claude Code Daily"));
        assert!(html.contains("Test Tip"));
        assert!(html.contains("Test Source"));
    }
}
