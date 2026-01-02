//! UI rendering module

mod tips;
mod draft;
mod preview;
mod stats;

use ratatui::{
    layout::{Constraint, Direction, Layout, Rect},
    style::{Color, Modifier, Style},
    text::{Line, Span},
    widgets::{Block, Borders, Paragraph, Tabs},
    Frame,
};

use crate::app::{App, Tab};

/// Main draw function
pub fn draw(f: &mut Frame, app: &App) {
    let chunks = Layout::default()
        .direction(Direction::Vertical)
        .constraints([
            Constraint::Length(3), // Header
            Constraint::Length(3), // Tabs
            Constraint::Min(0),    // Content
            Constraint::Length(2), // Status bar
        ])
        .split(f.area());

    draw_header(f, app, chunks[0]);
    draw_tabs(f, app, chunks[1]);
    draw_content(f, app, chunks[2]);
    draw_status_bar(f, app, chunks[3]);

    // Draw help overlay if active
    if app.show_help {
        draw_help_overlay(f, app);
    }

    // Draw quit confirmation if active
    if app.confirm_quit {
        draw_quit_confirmation(f);
    }
}

fn draw_header(f: &mut Frame, app: &App, area: Rect) {
    let stats_text = if let Some(ref stats) = app.stats {
        format!("[{} subs]", stats.total_subscribers)
    } else {
        "[loading...]".to_string()
    };

    let header = Paragraph::new(Line::from(vec![
        Span::styled(
            " Claude Code Daily Newsletter CLI ",
            Style::default()
                .fg(Color::Cyan)
                .add_modifier(Modifier::BOLD),
        ),
        Span::raw("  "),
        Span::styled(stats_text, Style::default().fg(Color::DarkGray)),
    ]))
    .block(
        Block::default()
            .borders(Borders::ALL)
            .border_style(Style::default().fg(Color::DarkGray)),
    );

    f.render_widget(header, area);
}

fn draw_tabs(f: &mut Frame, app: &App, area: Rect) {
    let titles: Vec<Line> = Tab::all()
        .iter()
        .enumerate()
        .map(|(i, tab)| {
            Line::from(format!("[{}] {}", i + 1, tab.title()))
        })
        .collect();

    let current_idx = Tab::all()
        .iter()
        .position(|&t| t == app.current_tab)
        .unwrap_or(0);

    let tabs = Tabs::new(titles)
        .select(current_idx)
        .style(Style::default().fg(Color::DarkGray))
        .highlight_style(
            Style::default()
                .fg(Color::Cyan)
                .add_modifier(Modifier::BOLD),
        )
        .block(Block::default().borders(Borders::ALL).title("Navigation"));

    f.render_widget(tabs, area);
}

fn draw_content(f: &mut Frame, app: &App, area: Rect) {
    match app.current_tab {
        Tab::Tips => tips::draw(f, app, area),
        Tab::Draft => draft::draw(f, app, area),
        Tab::Preview => preview::draw(f, app, area),
        Tab::Stats => stats::draw(f, app, area),
    }
}

fn draw_status_bar(f: &mut Frame, app: &App, area: Rect) {
    let status = app
        .status_message
        .as_deref()
        .unwrap_or("Press ? for help | q to quit");

    let loading_indicator = if app.is_loading { " " } else { "" };

    let status_bar = Paragraph::new(format!("{}{}", loading_indicator, status))
        .style(Style::default().fg(Color::DarkGray));

    f.render_widget(status_bar, area);
}

fn draw_help_overlay(f: &mut Frame, _app: &App) {
    let area = centered_rect(60, 70, f.area());

    let help_text = vec![
        "",
        " NAVIGATION",
        " ──────────────────────────────────",
        " 1-4      Switch to tab 1-4",
        " Tab      Next tab",
        " j/k      Move down/up",
        " gg/G     Go to top/bottom",
        "",
        " SELECTION (Tips tab)",
        " ──────────────────────────────────",
        " Space    Toggle selection",
        " Enter    Add selected to draft",
        "",
        " ACTIONS",
        " ──────────────────────────────────",
        " s        Save draft",
        " S        Send newsletter",
        " r        Refresh data",
        " ?        Toggle this help",
        " q        Quit",
        "",
    ];

    let help = Paragraph::new(help_text.join("\n"))
        .style(Style::default().fg(Color::White))
        .block(
            Block::default()
                .title(" Help ")
                .borders(Borders::ALL)
                .border_style(Style::default().fg(Color::Cyan))
                .style(Style::default().bg(Color::Black)),
        );

    f.render_widget(ratatui::widgets::Clear, area);
    f.render_widget(help, area);
}

fn draw_quit_confirmation(f: &mut Frame) {
    let area = centered_rect(40, 20, f.area());

    let confirm = Paragraph::new("\n  Press 'q' again to quit\n  Any other key to cancel")
        .style(Style::default().fg(Color::Yellow))
        .block(
            Block::default()
                .title(" Quit? ")
                .borders(Borders::ALL)
                .border_style(Style::default().fg(Color::Yellow))
                .style(Style::default().bg(Color::Black)),
        );

    f.render_widget(ratatui::widgets::Clear, area);
    f.render_widget(confirm, area);
}

/// Helper to create a centered rect
fn centered_rect(percent_x: u16, percent_y: u16, area: Rect) -> Rect {
    let popup_layout = Layout::default()
        .direction(Direction::Vertical)
        .constraints([
            Constraint::Percentage((100 - percent_y) / 2),
            Constraint::Percentage(percent_y),
            Constraint::Percentage((100 - percent_y) / 2),
        ])
        .split(area);

    Layout::default()
        .direction(Direction::Horizontal)
        .constraints([
            Constraint::Percentage((100 - percent_x) / 2),
            Constraint::Percentage(percent_x),
            Constraint::Percentage((100 - percent_x) / 2),
        ])
        .split(popup_layout[1])[1]
}
