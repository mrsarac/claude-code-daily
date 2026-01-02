//! Claude Code Daily Newsletter CLI
//!
//! A terminal-based dashboard for managing the Claude Code Daily newsletter.
//! Built with Ratatui for a modern TUI experience.

mod app;
mod config;
mod api;
mod ui;

use std::io;
use anyhow::Result;
use crossterm::{
    event::{self, DisableMouseCapture, EnableMouseCapture, Event, KeyCode, KeyEventKind},
    execute,
    terminal::{disable_raw_mode, enable_raw_mode, EnterAlternateScreen, LeaveAlternateScreen},
};
use ratatui::{
    backend::CrosstermBackend,
    Terminal,
};

use app::{App, Tab};
use ui::draw;

#[tokio::main]
async fn main() -> Result<()> {
    // Setup terminal
    enable_raw_mode()?;
    let mut stdout = io::stdout();
    execute!(stdout, EnterAlternateScreen, EnableMouseCapture)?;
    let backend = CrosstermBackend::new(stdout);
    let mut terminal = Terminal::new(backend)?;

    // Create app state
    let mut app = App::new().await?;

    // Run the app
    let result = run_app(&mut terminal, &mut app).await;

    // Restore terminal
    disable_raw_mode()?;
    execute!(
        terminal.backend_mut(),
        LeaveAlternateScreen,
        DisableMouseCapture
    )?;
    terminal.show_cursor()?;

    if let Err(err) = result {
        eprintln!("Error: {err:?}");
    }

    Ok(())
}

async fn run_app<B: ratatui::backend::Backend>(
    terminal: &mut Terminal<B>,
    app: &mut App,
) -> Result<()> {
    loop {
        terminal.draw(|f| draw(f, app))?;

        if let Event::Key(key) = event::read()? {
            if key.kind == KeyEventKind::Press {
                match key.code {
                    // Quit
                    KeyCode::Char('q') => {
                        if app.confirm_quit {
                            return Ok(());
                        }
                        app.confirm_quit = true;
                    }

                    // Tab switching
                    KeyCode::Char('1') => app.current_tab = Tab::Tips,
                    KeyCode::Char('2') => app.current_tab = Tab::Draft,
                    KeyCode::Char('3') => app.current_tab = Tab::Preview,
                    KeyCode::Char('4') => app.current_tab = Tab::Stats,
                    KeyCode::Tab => app.next_tab(),
                    KeyCode::BackTab => app.prev_tab(),

                    // Navigation
                    KeyCode::Char('j') | KeyCode::Down => app.next_item(),
                    KeyCode::Char('k') | KeyCode::Up => app.prev_item(),
                    KeyCode::Char('g') => {
                        // Wait for second 'g' for gg
                        if app.pending_g {
                            app.go_to_top();
                            app.pending_g = false;
                        } else {
                            app.pending_g = true;
                        }
                    }
                    KeyCode::Char('G') => app.go_to_bottom(),

                    // Selection
                    KeyCode::Char(' ') => app.toggle_selection(),
                    KeyCode::Enter => app.confirm_action().await?,

                    // Actions
                    KeyCode::Char('s') => app.save_draft()?,
                    KeyCode::Char('S') => app.send_newsletter().await?,
                    KeyCode::Char('r') => app.refresh().await?,
                    KeyCode::Char('?') => app.show_help = !app.show_help,

                    // Cancel quit confirmation
                    _ => {
                        app.confirm_quit = false;
                        app.pending_g = false;
                    }
                }
            }
        }
    }
}
