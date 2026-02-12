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


## 148. Parallel Editor Subagents in Claude Code for Writing
**Source:** ArtySuer (Reddit)

Improve Claude's writing feedback by using Claude Code to create multiple editor subagents. Each editor is trained on a specific writing style (e.g., Paul Graham, Bob Dylan) and provides independent feedback. The main Claude instance then synthesizes these perspectives, highlighting areas of agreement and disagreement to offer more nuanced and actionable writing suggestions. The /editors command in the provided GitHub repo facilitates this process.

[Original](https://www.reddit.com/r/ClaudeAI/comments/1qb59ya/15_claudes_arguing_about_an_essay/) | Added: 2026-01-13

---


## 189. Using Claude Code's Task Tool for Sub-Agents
**Source:** Bilal Haidar (Devto)

The Task tool in Claude Code allows for the creation of autonomous sub-agents to handle complex, multi-step operations. These sub-agents can work independently, enabling parallel processing and delegation of specific tasks within a larger workflow. This is beneficial for breaking down intricate problems into manageable components and leveraging specialized agents for each part.

[Original](https://dev.to/bhaidar/the-task-tool-claude-codes-agent-orchestration-system-4bf2) | Added: 2026-01-28

---


## 204. Async Subagents for Budget Research in Claude Code
**Source:** sberens (Hackernews)

Use async subagents within Claude Code to research and analyze multiple budget line items simultaneously across several years. This approach significantly accelerates research and contextualization, especially when dealing with large datasets or complex topics. While frontend modifications may require additional effort, this method substantially improves research throughput.

[Original](https://california-budget.com) | Added: 2026-02-05

---


## 210. Enable Agent Teams for Multi-Agent Collaboration
**Source:** BuildwithVignesh (Reddit)

Claude Code CLI now supports multi-agent collaboration using a research preview feature called 'agent teams'. To enable this token-intensive feature, you must set the environment variable `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`. This allows you to experiment with workflows involving multiple Claude instances working together on complex tasks.

[Original](https://www.reddit.com/r/ClaudeAI/comments/1qxas6v/official_anthropic_released_2132_with_12_cli_37/) | Added: 2026-02-07

---


## 216. Using Sub-Agents for Structured Planning in Claude Code
**Source:** Cristian Sifuentes (Devto)

Leverage Claude Code's sub-agent functionality to create specialized agents, such as an 'Architect' agent, that can generate structured implementation plans. This allows for reusable context via resume, versioned storage of plans in Markdown, and improved auditability within your Claude Code workflows. This tip focuses on a practical approach to planning within a Claude Code project.

[Original](https://dev.to/cristiansifuentes/conversational-development-with-claude-code-part-7-designing-sub-agents-for-planning-meet-1nlk) | Added: 2026-02-12

---

*[Back to Categories](../README.md)*