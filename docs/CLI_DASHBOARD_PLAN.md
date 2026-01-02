# Claude Code Daily - CLI Dashboard Plan

> **Planning Meeting Date:** 2026-01-02
> **Status:** APPROVED
> **Branch:** `feature/cli-dashboard`

---

## 1. Overview

Rust + Ratatui tabanlı bir TUI (Terminal User Interface) uygulaması. Newsletter yönetimini terminal üzerinden yapabilmeyi sağlar.

### Tech Stack
- **Language:** Rust
- **TUI Framework:** Ratatui (modern, active community)
- **HTTP Client:** reqwest (async)
- **JSON:** serde + serde_json
- **Async Runtime:** tokio
- **Config:** toml veya directories crate

### Location
```
claude-code-daily/
└── automation/
    └── cli/
        ├── Cargo.toml
        ├── src/
        │   ├── main.rs
        │   ├── app.rs           # App state
        │   ├── ui/
        │   │   ├── mod.rs
        │   │   ├── tips.rs      # Tip browser view
        │   │   ├── draft.rs     # Draft editor view
        │   │   ├── preview.rs   # Preview view
        │   │   └── stats.rs     # Stats dashboard view
        │   ├── api/
        │   │   ├── mod.rs
        │   │   ├── waitlist.rs  # Waitlist API client
        │   │   └── tips.rs      # Tips loader
        │   └── config.rs
        └── README.md
```

---

## 2. Features

### 2.1 Tip Browser + Selection
- `tips/categories/*.md` dosyalarından tip'leri yükle
- Kategori bazlı filtreleme (orchestration, context-management, workflow, subagents, tooling)
- Vim-style navigation (j/k, gg/G)
- Space ile tip seç/deselect
- Seçili tip'leri draft'a ekle

### 2.2 Draft Editor
- Seçilen tip'leri listele
- Sıralama değiştir (K/J ile yukarı/aşağı)
- Tip çıkar (d)
- Subject line düzenleme
- draft.json'a kaydet

### 2.3 Preview + Send
- HTML preview (terminal'de rendered veya temp file + browser)
- Dry-run modu (gerçekten göndermeden test)
- Send confirmation (y/N)
- API response gösterimi
- Progress bar for sending

### 2.4 Subscriber Stats
- Total subscribers
- Confirmed vs Pending
- Recent signups (last 7 days)
- Issue history (sent newsletters)
- Open rates (if available)

---

## 3. UI Layout

```
┌─────────────────────────────────────────────────────────────────────┐
│ Claude Code Daily Newsletter CLI                    [Stats: 4 subs] │
├─────────────────────────────────────────────────────────────────────┤
│ [1] Tips  [2] Draft  [3] Preview  [4] Stats         Tab: Tips       │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  Category: [All] orchestration context workflow subagents tooling   │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │ [x] 🎭 Git Worktree Orchestration              orchestration │   │
│  │ [ ] 🎭 Skill-Based Agent Delegation            orchestration │   │
│  │ [x] 📝 Markdown Bridge Documents          context-management │   │
│  │ [ ] 📝 Date Check Discipline              context-management │   │
│  │ [x] ⚡ The Full Automation Loop                     workflow │   │
│  │ [ ] ⚡ The Golden Rule                              workflow │   │
│  │ [x] 🤖 Manual Subagent Management                 subagents │   │
│  │ [ ] 🤖 The Sensei Pattern                         subagents │   │
│  │ [x] 🔧 Context7 MCP Server                          tooling │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                                                                     │
│  Selected: 5/8    [Space] Toggle  [Enter] Add to Draft  [q] Quit   │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 4. Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `1-4` | Switch tabs |
| `Tab` | Next tab |
| `j/k` | Navigate down/up |
| `gg/G` | Go to top/bottom |
| `Space` | Toggle selection |
| `Enter` | Confirm action |
| `e` | Edit (in Draft tab) |
| `s` | Save draft |
| `p` | Preview |
| `S` | Send newsletter |
| `r` | Refresh data |
| `q` | Quit |
| `?` | Help |

---

## 5. API Integration

### Waitlist API Base
```
https://waitlist.neurabytelabs.com/api/claudecodedaily
```

### Endpoints Used
| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/newsletter/stats` | GET | Subscriber counts, issue counts |
| `/newsletter/subscribers` | GET | List all subscribers |
| `/newsletter/issues` | POST | Create draft issue |
| `/newsletter/issues/:id/send` | POST | Send issue |

### Config File (~/.config/ccd-cli/config.toml)
```toml
[api]
base_url = "https://waitlist.neurabytelabs.com"
project_id = "claudecodedaily"

[newsletter]
tips_per_issue = 8
default_subject = "Claude Code Daily #{issue}: {count} Real Use Cases"

[ui]
theme = "dark"  # dark | light
```

---

## 6. Development Phases

### Phase 1: Foundation (MVP)
- [ ] Rust project setup (Cargo.toml, dependencies)
- [ ] Basic Ratatui app structure
- [ ] Tab navigation
- [ ] Tips loader from markdown files

### Phase 2: Core Features
- [ ] Tip browser with selection
- [ ] Draft management
- [ ] Save/load draft.json
- [ ] API client (reqwest)

### Phase 3: Newsletter Flow
- [ ] HTML preview generation
- [ ] Send flow with confirmation
- [ ] Progress indicators
- [ ] Error handling

### Phase 4: Polish
- [ ] Stats dashboard
- [ ] Config file support
- [ ] Help screen
- [ ] Color themes

---

## 7. Dependencies (Cargo.toml)

```toml
[package]
name = "ccd-cli"
version = "0.1.0"
edition = "2021"
description = "Claude Code Daily Newsletter CLI"

[dependencies]
ratatui = "0.29"
crossterm = "0.28"
tokio = { version = "1", features = ["full"] }
reqwest = { version = "0.12", features = ["json"] }
serde = { version = "1", features = ["derive"] }
serde_json = "1"
toml = "0.8"
directories = "5"
anyhow = "1"
```

---

## 8. Success Criteria

1. **Functional:** Tip seçimi → Draft oluşturma → Preview → Send akışı çalışmalı
2. **Usable:** Vim-style navigation, hızlı keyboard shortcuts
3. **Reliable:** API hataları gracefully handle edilmeli
4. **Maintainable:** Modüler kod yapısı, clear separation of concerns

---

## 9. Out of Scope (v1)

- Twitter/Reddit scraper entegrasyonu (ayrı cron job olarak kalacak)
- Multi-project support (sadece claudecodedaily)
- Email template editor (hardcoded CLI-style template)
- Subscriber management (read-only stats)

---

*Plan approved: 2026-01-02*
*Next step: Create feature branch and start Phase 1*
