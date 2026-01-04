# 🚀 Claude Code Daily

> **Fresh Claude Code tips, every single day.** Auto-curated from the developer community.

[![Daily Update](https://github.com/mrsarac/claude-code-daily/actions/workflows/daily-update.yml/badge.svg)](https://github.com/mrsarac/claude-code-daily/actions/workflows/daily-update.yml)
[![Tips Count](https://img.shields.io/badge/tips-120+-blue)](./tips/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Twitter](https://img.shields.io/badge/Follow-%40theRenaisseur-1DA1F2?logo=twitter)](https://twitter.com/theRenaisseur)

---

## 🎯 Today's Tip

> **Git Worktree Orchestration** — Run an "Orchestrator Agent" on your main branch. Delegate subtasks to other agents running in different Git worktrees on separate branches. This enables massive parallelization.
>
> ```bash
> git worktree add ../feature-auth feature/auth
> cd ../feature-auth && claude
> ```
>
> *Source: Pushkar Jain via [Alex Albert's Thread](https://x.com/alexalbert__/status/2004575443484319954)*

---

## 📚 The Four Pillars

| Pillar | Core Idea | Impact |
|--------|-----------|--------|
| **🎭 Orchestration** | Claude as conductor, not worker | 10x parallelization |
| **📝 Context** | Markdown bridges between sessions | Zero knowledge loss |
| **⚡ Separation** | Planning ≠ Implementation | Reliable outputs |
| **🔌 Extension** | MCP servers for real-world access | Unlimited capabilities |

---

## 🏆 Top 10 Game Changers

| # | Technique | Category |
|---|-----------|----------|
| 1 | [Git Worktree Orchestration](./tips/categories/orchestration.md#1-git-worktree-orchestration) | Orchestration |
| 2 | [The Full Automation Loop](./tips/categories/workflow.md#2-the-full-automation-loop) | Workflow |
| 3 | [Skill-Based Worktrees](./tips/categories/orchestration.md#3-skill-based-worktrees) | Orchestration |
| 4 | [Markdown Bridge Documents](./tips/categories/context-management.md#4-markdown-bridge-documents) | Context |
| 5 | [Automated Documentation Agent](./tips/categories/tooling.md#5-automated-documentation-agent) | Tooling |
| 6 | [Manual Subagent Management](./tips/categories/subagents.md#6-manual-subagent-management) | Subagents |
| 7 | [Context7 & GitTrees MCP](./tips/categories/tooling.md#7-context7-gittrees-mcp) | Tooling |
| 8 | [Small Subagents for Everything](./tips/categories/subagents.md#8-small-subagents-for-everything) | Subagents |
| 9 | [The Sensei Pattern](./tips/categories/subagents.md#9-the-sensei-pattern) | Subagents |
| 10 | [Cost Optimization](./tips/categories/workflow.md#10-cost-optimization) | Workflow |

---

## 📂 Browse by Category

- **[🎭 Orchestration](./tips/categories/orchestration.md)** — Parallel agents, worktrees, delegation
- **[📝 Context Management](./tips/categories/context-management.md)** — Bridges, compaction, memory
- **[⚡ Workflow](./tips/categories/workflow.md)** — Planning, cost optimization, patterns
- **[🤖 Subagents](./tips/categories/subagents.md)** — Delegation, coordination, MCP
- **[🔧 Tooling](./tips/categories/tooling.md)** — Notifications, exports, integrations

---

## 🤖 How This Works

```
┌─────────────────────────────────────────────────────────────┐
│                    Daily at 00:00 UTC                       │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐  │
│  │ Dev.to  │    │   HN    │    │ Reddit  │    │ Gemini  │  │
│  │   RSS   │ -> │   RSS   │ -> │   RSS   │ -> │ Curate  │  │
│  └─────────┘    └─────────┘    └─────────┘    └─────────┘  │
│                                                             │
│  Sources:                                                   │
│  • Dev.to #claude, #claudecode, #anthropic                 │
│  • Hacker News "claude code" (hnrss.org)                   │
│  • r/ClaudeAI on Reddit                                    │
└─────────────────────────────────────────────────────────────┘
```

---

## 🌟 Star This Repo

If you find these tips useful:
1. ⭐ **Star** this repo to get daily tips in your feed
2. 👀 **Watch** for releases to get notified of curated collections
3. 🍴 **Fork** to customize your own tip collection

---

## 🤝 Contributing

Found a great Claude Code tip? [Submit it here!](./CONTRIBUTING.md)

We accept tips from:
- Personal experience
- Community discussions
- Blog posts (with attribution)

---

## 📜 Credits

This project started with 50 tips curated from [Alex Albert's viral thread](https://x.com/alexalbert__/status/2004575443484319954). See [CREDITS.md](./CREDITS.md) for full attribution.

---

## 📄 License

MIT © [Mustafa Saraç](https://github.com/mrsarac)

---

<p align="center">
  <sub>Built with 🧠 by <a href="https://neurabytelabs.com">NeuraByte Labs</a></sub>
</p>
