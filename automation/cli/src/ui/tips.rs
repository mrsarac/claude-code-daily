//! Tips browser view

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
            Constraint::Length(3), // Category filter
            Constraint::Min(0),    // Tips list
            Constraint::Length(2), // Selection info
        ])
        .split(area);

    draw_category_filter(f, app, chunks[0]);
    draw_tips_list(f, app, chunks[1]);
    draw_selection_info(f, app, chunks[2]);
}

fn draw_category_filter(f: &mut Frame, app: &App, area: Rect) {
    let categories = vec![
        ("All", "*"),
        ("orchestration", "O"),
        ("context-management", "C"),
        ("workflow", "W"),
        ("subagents", "S"),
        ("tooling", "T"),
    ];

    let spans: Vec<Span> = categories
        .iter()
        .map(|(name, icon)| {
            let is_selected = app.category_filter.as_str() == *name
                || (app.category_filter.as_str() == "All" && *name == "All");

            if is_selected {
                Span::styled(
                    format!(" [{}] {} ", icon, name),
                    Style::default()
                        .fg(Color::Cyan)
                        .add_modifier(Modifier::BOLD),
                )
            } else {
                Span::styled(
                    format!(" [{}] {} ", icon, name),
                    Style::default().fg(Color::DarkGray),
                )
            }
        })
        .collect();

    let filter = Paragraph::new(Line::from(spans)).block(
        Block::default()
            .borders(Borders::ALL)
            .title(" Category Filter "),
    );

    f.render_widget(filter, area);
}

fn draw_tips_list(f: &mut Frame, app: &App, area: Rect) {
    let filtered = app.filtered_tips();

    let items: Vec<ListItem> = filtered
        .iter()
        .enumerate()
        .map(|(display_idx, (original_idx, tip))| {
            let is_selected = app.selected_tips.contains(original_idx);
            let is_current = display_idx == app.list_index;

            let checkbox = if is_selected { "[x]" } else { "[ ]" };

            let style = if is_current {
                Style::default()
                    .bg(Color::DarkGray)
                    .add_modifier(Modifier::BOLD)
            } else if is_selected {
                Style::default().fg(Color::Green)
            } else {
                Style::default()
            };

            let content = format!(
                " {} {} {} ",
                checkbox,
                tip.icon,
                truncate(&tip.title, 60)
            );

            ListItem::new(Line::from(vec![
                Span::styled(content, style),
                Span::styled(
                    format!(" {} ", tip.category),
                    Style::default().fg(Color::DarkGray),
                ),
            ]))
        })
        .collect();

    let list = List::new(items).block(
        Block::default()
            .borders(Borders::ALL)
            .title(format!(" Tips ({}) ", filtered.len())),
    );

    f.render_widget(list, area);
}

fn draw_selection_info(f: &mut Frame, app: &App, area: Rect) {
    let max = app.config.tips_per_issue;
    let selected = app.selected_tips.len();

    let info = Paragraph::new(format!(
        " Selected: {}/{} | [Space] Toggle | [a] All | [c] Filter | [Enter] Draft | [?] Help",
        selected, max
    ))
    .style(Style::default().fg(Color::DarkGray));

    f.render_widget(info, area);
}

fn truncate(s: &str, max_len: usize) -> String {
    if s.len() <= max_len {
        s.to_string()
    } else {
        format!("{}...", &s[..max_len - 3])
    }
}
