//! Preview view (newsletter preview)

use ratatui::{
    layout::{Constraint, Direction, Layout, Rect},
    style::{Color, Modifier, Style},
    text::{Line, Span},
    widgets::{Block, Borders, Paragraph, Wrap},
    Frame,
};

use crate::app::App;

pub fn draw(f: &mut Frame, app: &App, area: Rect) {
    let chunks = Layout::default()
        .direction(Direction::Vertical)
        .constraints([
            Constraint::Length(7),  // Header preview
            Constraint::Min(0),     // Content preview
            Constraint::Length(3),  // Send actions
        ])
        .split(area);

    draw_header_preview(f, app, chunks[0]);
    draw_content_preview(f, app, chunks[1]);
    draw_send_actions(f, app, chunks[2]);
}

fn draw_header_preview(f: &mut Frame, app: &App, area: Rect) {
    let issue_number = app.stats.as_ref().map(|s| s.total_issues + 1).unwrap_or(1);
    let subscriber_count = app
        .stats
        .as_ref()
        .map(|s| s.confirmed_subscribers)
        .unwrap_or(0);

    let header = Paragraph::new(vec![
        Line::from(""),
        Line::from(vec![
            Span::styled("  ", Style::default()),
            Span::styled("", Style::default().fg(Color::Red)),
            Span::styled(" ", Style::default()),
            Span::styled("", Style::default().fg(Color::Yellow)),
            Span::styled(" ", Style::default()),
            Span::styled("", Style::default().fg(Color::Green)),
            Span::styled("  claude-code-daily", Style::default().fg(Color::DarkGray)),
        ]),
        Line::from(vec![
            Span::styled(
                "   Claude Code Daily",
                Style::default()
                    .fg(Color::Cyan)
                    .add_modifier(Modifier::BOLD),
            ),
        ]),
        Line::from(vec![Span::styled(
            format!(
                "   Issue #{} | {} tips | {} subscribers",
                issue_number,
                app.selected_tips.len(),
                subscriber_count
            ),
            Style::default().fg(Color::DarkGray),
        )]),
    ])
    .block(
        Block::default()
            .borders(Borders::ALL)
            .title(" Newsletter Header ")
            .border_style(Style::default().fg(Color::DarkGray)),
    );

    f.render_widget(header, area);
}

fn draw_content_preview(f: &mut Frame, app: &App, area: Rect) {
    if app.selected_tips.is_empty() {
        let empty = Paragraph::new("\n\n  No content to preview.\n  Select tips first!")
            .style(Style::default().fg(Color::DarkGray))
            .block(Block::default().borders(Borders::ALL).title(" Content "));
        f.render_widget(empty, area);
        return;
    }

    let mut lines = vec![Line::from("")];

    for (i, &tip_idx) in app.selected_tips.iter().enumerate() {
        if let Some(tip) = app.tips.get(tip_idx) {
            // Command prompt style header
            lines.push(Line::from(vec![
                Span::styled("  > ", Style::default().fg(Color::Green)),
                Span::styled("claude", Style::default().fg(Color::Cyan)),
                Span::styled(format!(" --use-case {}", i + 1), Style::default().fg(Color::DarkGray)),
            ]));

            // Title
            lines.push(Line::from(vec![
                Span::raw("    "),
                Span::styled(
                    format!("{} {}", tip.icon, tip.title),
                    Style::default().add_modifier(Modifier::BOLD),
                ),
            ]));

            // Source
            if !tip.source.is_empty() {
                lines.push(Line::from(vec![
                    Span::raw("    "),
                    Span::styled(
                        format!("// source: {}", tip.source),
                        Style::default().fg(Color::DarkGray),
                    ),
                ]));
            }

            lines.push(Line::from(""));
        }
    }

    let content = Paragraph::new(lines)
        .wrap(Wrap { trim: false })
        .block(
            Block::default()
                .borders(Borders::ALL)
                .title(" Content Preview (CLI-style) "),
        );

    f.render_widget(content, area);
}

fn draw_send_actions(f: &mut Frame, app: &App, area: Rect) {
    let can_send = !app.selected_tips.is_empty();
    let subscriber_count = app
        .stats
        .as_ref()
        .map(|s| s.confirmed_subscribers)
        .unwrap_or(0);

    let actions = if can_send {
        format!(
            " [S] SEND to {} subscribers | [s] Save draft | [2] Back to Draft",
            subscriber_count
        )
    } else {
        " No content to send. Select tips first!".to_string()
    };

    let style = if can_send {
        Style::default().fg(Color::Green)
    } else {
        Style::default().fg(Color::DarkGray)
    };

    let actions_widget = Paragraph::new(actions)
        .style(style)
        .block(Block::default().borders(Borders::TOP));

    f.render_widget(actions_widget, area);
}
