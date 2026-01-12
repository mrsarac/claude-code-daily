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



## 138. Run Skills in Forked Sub-Agent Contexts
**Source:** mDarken (Reddit)

Claude Code now supports running skills and slash commands in a forked sub-agent context. By adding `context: fork` in the skill's frontmatter, you can isolate the skill's execution environment. This allows for better resource management, prevents interference between skills, and potentially enables more complex multi-agent workflows. This feature is configured within the skill definition itself, making it straightforward to implement.

[Original](https://www.reddit.com/r/ClaudeAI/comments/1q6q9my/claudecode_v210_just_dropped/) | Added: 2026-01-08

---


## 145. Researching complex topics with async subagents in Claude Code
**Source:** sberens (Hackernews)

Use Claude Code with async subagents to research multiple aspects of a complex topic like the California budget simultaneously. This approach enables parallel processing of different budget line items across various years, allowing for efficient data gathering and context addition. While frontend modifications may still require manual effort, this method can significantly accelerate research throughput.

[Original](https://california-budget.com) | Added: 2026-01-12

---


## 146. Use Async Subagents for Research with Claude Code
**Source:** sberens (Hackernews)

Claude Code can leverage async subagents to efficiently research multiple budget line items across various years. This method allows for parallel processing of complex research tasks, significantly increasing throughput and providing contextual information with graphs. This is particularly useful for users who are new to the subject matter and require in-depth data analysis.

[Original](https://california-budget.com) | Added: 2026-01-12

---

*[Back to Categories](../README.md)*