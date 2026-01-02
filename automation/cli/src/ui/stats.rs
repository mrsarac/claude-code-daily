//! Stats dashboard view

use ratatui::{
    layout::{Constraint, Direction, Layout, Rect},
    style::{Color, Modifier, Style},
    text::{Line, Span},
    widgets::{Block, Borders, Paragraph},
    Frame,
};

use crate::app::App;

pub fn draw(f: &mut Frame, app: &App, area: Rect) {
    let chunks = Layout::default()
        .direction(Direction::Horizontal)
        .constraints([
            Constraint::Percentage(50), // Subscriber stats
            Constraint::Percentage(50), // Issue stats
        ])
        .split(area);

    draw_subscriber_stats(f, app, chunks[0]);
    draw_issue_stats(f, app, chunks[1]);
}

fn draw_subscriber_stats(f: &mut Frame, app: &App, area: Rect) {
    let content = if let Some(ref stats) = app.stats {
        vec![
            Line::from(""),
            Line::from(vec![
                Span::styled("  Total Subscribers: ", Style::default().fg(Color::DarkGray)),
                Span::styled(
                    format!("{}", stats.total_subscribers),
                    Style::default()
                        .fg(Color::Cyan)
                        .add_modifier(Modifier::BOLD),
                ),
            ]),
            Line::from(""),
            Line::from(vec![
                Span::styled("  ", Style::default()),
                Span::styled("", Style::default().fg(Color::Green)),
                Span::styled(
                    format!(" Confirmed: {}", stats.confirmed_subscribers),
                    Style::default().fg(Color::Green),
                ),
            ]),
            Line::from(vec![
                Span::styled("  ", Style::default()),
                Span::styled("", Style::default().fg(Color::Yellow)),
                Span::styled(
                    format!(" Pending:   {}", stats.pending_subscribers),
                    Style::default().fg(Color::Yellow),
                ),
            ]),
            Line::from(""),
            Line::from(""),
            Line::from(vec![Span::styled(
                "  Press [r] to refresh",
                Style::default().fg(Color::DarkGray),
            )]),
        ]
    } else {
        vec![
            Line::from(""),
            Line::from(vec![Span::styled(
                "  Loading...",
                Style::default().fg(Color::DarkGray),
            )]),
            Line::from(""),
            Line::from(vec![Span::styled(
                "  Press [r] to refresh",
                Style::default().fg(Color::DarkGray),
            )]),
        ]
    };

    let widget = Paragraph::new(content).block(
        Block::default()
            .borders(Borders::ALL)
            .title(" Subscribers ")
            .border_style(Style::default().fg(Color::DarkGray)),
    );

    f.render_widget(widget, area);
}

fn draw_issue_stats(f: &mut Frame, app: &App, area: Rect) {
    let content = if let Some(ref stats) = app.stats {
        vec![
            Line::from(""),
            Line::from(vec![
                Span::styled("  Total Issues Sent: ", Style::default().fg(Color::DarkGray)),
                Span::styled(
                    format!("{}", stats.total_issues),
                    Style::default()
                        .fg(Color::Cyan)
                        .add_modifier(Modifier::BOLD),
                ),
            ]),
            Line::from(""),
            Line::from(vec![
                Span::styled("  ", Style::default()),
                Span::styled(
                    format!("Next Issue: #{}", stats.total_issues + 1),
                    Style::default().fg(Color::Green),
                ),
            ]),
            Line::from(""),
            Line::from(""),
            Line::from(vec![Span::styled(
                "  Tip: 8 is our lucky number!",
                Style::default().fg(Color::DarkGray),
            )]),
        ]
    } else {
        vec![
            Line::from(""),
            Line::from(vec![Span::styled(
                "  Loading...",
                Style::default().fg(Color::DarkGray),
            )]),
        ]
    };

    let widget = Paragraph::new(content).block(
        Block::default()
            .borders(Borders::ALL)
            .title(" Newsletter Issues ")
            .border_style(Style::default().fg(Color::DarkGray)),
    );

    f.render_widget(widget, area);
}
