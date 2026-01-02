# Claude Code Daily Newsletter CLI

A terminal-based dashboard for managing the Claude Code Daily newsletter.

```
┌─────────────────────────────────────────────────────────────────────┐
│ Claude Code Daily Newsletter CLI                    [Stats: 4 subs] │
├─────────────────────────────────────────────────────────────────────┤
│ [1] Tips  [2] Draft  [3] Preview  [4] Stats                         │
├─────────────────────────────────────────────────────────────────────┤
│  [x] 🎭 Git Worktree Orchestration              orchestration       │
│  [ ] 📝 Markdown Bridge Documents          context-management       │
│  [x] ⚡ The Full Automation Loop                     workflow       │
└─────────────────────────────────────────────────────────────────────┘
```

## Installation

### From Source

```bash
cd automation/cli
cargo build --release
```

The binary will be at `target/release/ccd`.

### Add to PATH (Optional)

```bash
# Add to ~/.zshrc or ~/.bashrc
export PATH="$HOME/Documents/GitHub/claude-code-daily/automation/cli/target/release:$PATH"
```

## Usage

```bash
# Run from repo root
./automation/cli/target/release/ccd

# Or if added to PATH
ccd
```

## Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `1-4` | Switch tabs |
| `Tab` | Next tab |
| `j/k` | Move down/up |
| `gg/G` | Go to top/bottom |
| `Space` | Toggle selection |
| `Enter` | Confirm action |
| `s` | Save draft |
| `S` | Send newsletter |
| `r` | Refresh data |
| `?` | Toggle help |
| `q` | Quit |

## Tabs

### 1. Tips Browser
- Browse all tips from `tips/categories/*.md`
- Filter by category (orchestration, context-management, workflow, subagents, tooling)
- Select tips with Space (max 8)

### 2. Draft Editor
- View selected tips
- Reorder with K/J
- Save draft to `draft.json`

### 3. Preview
- CLI-style newsletter preview
- See how it will look in emails

### 4. Stats
- Subscriber counts (total, confirmed, pending)
- Newsletter issue history

## Configuration

Config file: `~/.config/ccd-cli/config.toml`

```toml
[api]
api_url = "https://waitlist.neurabytelabs.com"
project_id = "claudecodedaily"

[newsletter]
tips_per_issue = 8
subject_template = "Claude Code Daily #{issue}: {count} Real Use Cases"
```

## API Integration

Connects to the Waitlist API at `waitlist.neurabytelabs.com`:

- `GET /newsletter/stats` - Subscriber and issue counts
- `POST /newsletter/issues` - Create draft issue
- `POST /newsletter/issues/:id/send` - Send issue

## Tech Stack

- **Rust** - Systems programming language
- **Ratatui** - Modern TUI framework
- **Crossterm** - Terminal manipulation
- **Tokio** - Async runtime
- **Reqwest** - HTTP client

## Development

```bash
# Run in development mode
cargo run

# Run with logging
RUST_LOG=debug cargo run

# Check for errors
cargo check

# Run tests
cargo test
```

## License

MIT
