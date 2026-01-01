# 🔧 Tooling Tips

> Notifications, exports, integrations, and MCP servers.

---

## 5. Automated Documentation Agent
**Source:** Graeme

Create an agent that writes customer help documentation from feature branches (fed with PRD context). Achieves **95% accuracy** on first pass.

---

## 7. Context7 & GitTrees MCP Servers
**Source:** Multiple Users

For up-to-date library documentation (bypassing knowledge cutoff), connect:
- **Context7 MCP** → Real-time documentation
- **GitTrees MCP** → Repository exploration

```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@context7/mcp-server"]
    }
  }
}
```

---

## 41. Notification System
**Source:** Jairo

Create `/ping` command for Telegram notifications after every task. Add to CLAUDE.md: "Summarize and ping after each task."

---

## 42. Obsidian Export
**Source:** DiamondEyesFox

Export raw session logs to Obsidian. Maintain both summary and detailed logs for future reference.

---

## 43. File Discipline
**Source:** John Hashem

Treat memory files like code files. Naming conventions and organization are critical for maintainability.

---

## 44. Obsidian Trail
**Source:** Tyler Nishida

Every project should leave an Obsidian trail: decisions, implementations, pivots, and insights.

---

## 45. Architecture Skills
**Source:** Skill Creator

Write a Skill that explains your codebase patterns and architecture. New sessions understand context immediately.

---

## 47. Super-Charge Your Tools
**Source:** Meta Alchemist

Build your own toolkit:
- Memory layer
- Skill spawner (automatic skill generator)
- Vulnerability scanner

---

## 49. Custom Skills for Patterns
**Source:** Community

Write Skills that encode your team's patterns. Architecture decisions, naming conventions, testing strategies.

---

## 50. iMessage Context (Mac Only) ⚠️
**Source:** Gordon Wintrob

Read `~/Library/Messages/chat.db` for context. **Warning:** Privacy implications—evaluate carefully.

---


## 51. Reliable Element Interaction with Claude Code CLI
**Source:** yksugi (Reddit)

Improve Claude Code CLI interactions by using `read_page` to access the accessibility tree and `find` to locate elements via their descriptions. This allows interaction using element `ref`s instead of screen coordinates, providing more accurate and reliable clicking, especially when screenshots are unnecessary. Avoid taking screenshots unless explicitly required for a task.

[Original](https://www.reddit.com/r/ClaudeAI/comments/1q0pbuh/a_quick_tip_on_improving_the_performance_of/) | Added: 2025-12-31

---


## 52. Improve Claude Code Reliability with Accessibility Tree
**Source:** yksugi (Reddit)

Instead of relying on screenshots and screen coordinates for interaction, use `read_page` to access the accessibility tree and obtain element references. Then, use `find` to locate elements by their description and interact using `ref`. This approach offers increased accuracy and speed, avoiding the pitfalls of coordinate-based interaction that can be unreliable.

[Original](https://www.reddit.com/r/ClaudeAI/comments/1q0pbuh/a_quick_tip_on_improving_the_performance_of/) | Added: 2026-01-01

---

*[Back to Categories](../README.md)*
