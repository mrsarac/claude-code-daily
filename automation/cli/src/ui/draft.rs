//! Draft editor view

use ratatui::{
    layout::{Constraint, Direction, Layout, Rect},
    style::{Color, Modifier, Style},
    text::{Line, Span},
    widgets::{Block, Borders, List, ListItem, Paragraph},
    Frame,
};

use crate::app::App;

pub fn draw(f: &mut Frame, app: &App, area: Rect) {
    let chunks = Layout::default()
        .direction(Direction::Vertical)
        .constraints([
            Constraint::Length(5), // Subject line
            Constraint::Min(0),    // Selected tips
            Constraint::Length(2), // Actions
        ])
        .split(area);

    draw_subject(f, app, chunks[0]);
    draw_selected_tips(f, app, chunks[1]);
    draw_actions(f, app, chunks[2]);
}

fn draw_subject(f: &mut Frame, app: &App, area: Rect) {
    let issue_number = app.stats.as_ref().map(|s| s.total_issues + 1).unwrap_or(1);
    let subject = format!(
        "Claude Code Daily #{}: {} Real Use Cases",
        issue_number,
        app.selected_tips.len()
    );

    let subject_widget = Paragraph::new(vec![
        Line::from(""),
        Line::from(vec![
            Span::styled(" Subject: ", Style::default().fg(Color::DarkGray)),
            Span::styled(
                subject,
                Style::default()
                    .fg(Color::Cyan)
                    .add_modifier(Modifier::BOLD),
            ),
        ]),
    ])
    .block(
        Block::default()
            .borders(Borders::ALL)
            .title(" Newsletter Subject "),
    );

    f.render_widget(subject_widget, area);
}

fn draw_selected_tips(f: &mut Frame, app: &App, area: Rect) {
    if app.selected_tips.is_empty() {
        let empty = Paragraph::new("\n\n  No tips selected yet.\n\n  Go to Tips tab and select some tips!")
            .style(Style::default().fg(Color::DarkGray))
            .block(
                Block::default()
                    .borders(Borders::ALL)
                    .title(" Draft (0 tips) "),
            );
        f.render_widget(empty, area);
        return;
    }

    let items: Vec<ListItem> = app
        .selected_tips
        .iter()
        .enumerate()
        .filter_map(|(i, &tip_idx)| {
            app.tips.get(tip_idx).map(|tip| {
                let is_current = i == app.list_index;

                let style = if is_current {
                    Style::default()
                        .bg(Color::DarkGray)
                        .add_modifier(Modifier::BOLD)
                } else {
                    Style::default()
                };

                let content = format!(
                    " {}. {} {} ",
                    i + 1,
                    tip.icon,
                    truncate(&tip.title, 55)
                );

                ListItem::new(Line::from(vec![
                    Span::styled(content, style),
                    Span::styled(
                        format!(" {} ", tip.category),
                        Style::default().fg(Color::DarkGray),
                    ),
                ]))
            })
        })
        .collect();

    let list = List::new(items).block(
        Block::default()
            .borders(Borders::ALL)
            .title(format!(" Draft ({} tips) ", app.selected_tips.len())),
    );

    f.render_widget(list, area);
}

fn draw_actions(f: &mut Frame, app: &App, area: Rect) {
    let can_preview = !app.selected_tips.is_empty();

    let actions = if can_preview {
        " [s] Save draft | [Enter] Preview | [d] Remove | [j/k] Navigate"
    } else {
        " Select tips first to create a draft (go to Tips tab with [1])"
    };

    let style = if can_preview {
        Style::default().fg(Color::DarkGray)
    } else {
        Style::default().fg(Color::Yellow)
    };

    let actions_widget = Paragraph::new(actions).style(style);
    f.render_widget(actions_widget, area);
}

fn truncate(s: &str, max_len: usize) -> String {
    if s.len() <= max_len {
        s.to_string()
    } else {
        format!("{}...", &s[..max_len - 3])
    }
}
