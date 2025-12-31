# 🤖 Subagent Tips

> Delegation, coordination, and MCP-powered capabilities.

---

## 6. Manual Subagent Management
**Source:** Marcin Dudek

When you sense context limits approaching, explicitly tell Claude:
> "For each task, delegate to a subagent. You are the manager—coordinate, don't execute."

This forces hierarchical execution and preserves main session context.

---

## 8. Small Subagents for Everything
**Source:** James Vanderhaak

Use subagents even for simple tasks. This extends main session context lifetime dramatically.

**Rule:** If a task takes more than 3 tool calls, spawn a subagent.

---

## 9. The Sensei Pattern
**Source:** Alizain Feerasta

Keep main context clean by using subagents liberally. Your main session is the "sensei"—it teaches and coordinates, but doesn't do the work itself.

Reference: [github.com/803/sensei](https://github.com/803/sensei)

---

## 31. Browser Agent Integration
**Source:** Alex Colon

Claude in Chrome extension: slower than alternatives, but more accurate for browser-based tasks.

---

## 32. Evolutionary Agents
**Source:** Aaron Erickson

AlphaEvolve-style agents that continuously improve themselves and spawn subagents. Compute-intensive but fascinating for experimentation.

---

## 34. Context-Aware Refactoring
**Source:** NowshadAhmad

Give Claude a messy function + your style constraints. Better than autocomplete for significant refactors.

---

## 36. Thinking Out Loud
**Source:** Yashas

Force agents to write out their reasoning before coding. Catches logic errors early.

---

## 37. MAID Runner Pattern
**Source:** Mamerto Fabian

Custom "Maid Runner" subagents with specialized `/spike` commands. Clean up and organize as you go.

---

## 39. Playwright MCP for UI
**Source:** Matheus Oliveira

Claude Code + Playwright MCP = automated browser control, UI testing, and "magic" workflows.

---

## 40. NotebookLM Integration
**Source:** Switchfin.ai

For large API documentation, connect Claude to NotebookLM via MCP. Specialized knowledge retrieval.

---


*[Back to Categories](../README.md)*