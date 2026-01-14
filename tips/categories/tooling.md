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


## 58. I Built a Claude Code Plugin That Unifies 10 AI Image Provid
**Source:** Merlin Rabens (Devto)


  
  
  The Problem


Last month I was working on a project that needed AI-generated images. Sometimes I needed photorealistic product shots. Sometimes logos with clean typography. Sometimes artistic

[Original](https://dev.to/merlinrabens/i-built-a-claude-code-plugin-that-unifies-10-ai-image-providers-5gpd) | Added: 2026-01-04

---


## 72. I Used ClaudeCode to Rescue an npm Package with 760K Downloa
**Source:** steve greensill (Devto)


  
  
  The Inciting Incident


It started with a bug.

I was trying to get a unrelated typescript project running, when I hit an issue with one of its dependencies... license-checker. No big deal, I

[Original](https://dev.to/greenstevester/i-used-claudecode-to-rescue-an-npm-package-with-760k-downloads-and-now-i-have-a-mission-from-my-3kdj) | Added: 2026-01-04

---


## 85. Reverse engineered Claude Code's web tools
**Source:** liran_yo (Hackernews)


Article URL: https://medium.com/@liranyoffe/reverse-engineering-claude-code-web-tools-1409249316c3
Comments URL: https://news.ycombinator.com/item?id=46456648
Points: 3
# Comments: 0


[Original](https://medium.com/@liranyoffe/reverse-engineering-claude-code-web-tools-1409249316c3) | Added: 2026-01-04

---


## 105. Verify loop inspired by Boris Cherny work
**Source:** nyarumes (Reddit)

Hello guys I wanna present my verify loop - https://github.com/golovatskygroup/llm (Support Go, JS, Python) Please ask claude code to configure hooks for your project after you init by a script   &#32

[Original](https://www.reddit.com/r/ClaudeAI/comments/1q36iph/verify_loop_inspired_by_boris_cherny_work/) | Added: 2026-01-04

---


## 123. Use Goose for Real-Time Terminal Assistance
**Source:** Erica (Devto)

The tip suggests using Goose (likely a reference to the Claude Code CLI terminal integration) to provide real-time assistance while building a scheduling application. By observing terminal commands and understanding the context, Goose can offer guidance during the development process, streamlining the workflow compared to manual organization or spreadsheets.

[Original](https://dev.to/eriperspective/ai-engineering-advent-of-ai-with-goose-day-13-scheduling-application-4069) | Added: 2026-01-04

---


## 125. iOS Dev with Claude Code: XcodeBuildMCP Integration
**Source:** kodOZANI (Reddit)

Integrate Claude Code CLI with XcodeBuildMCP for iOS development workflows. Configure Claude Code to build, test, and run iOS simulators directly from the command line. This streamlines development by enabling rapid iterations and automated testing triggered by Claude Code, improving efficiency.

[Original](https://www.reddit.com/r/ClaudeAI/comments/1q3n0dg/complete_claude_code_setup_guide_for_iosswift/) | Added: 2026-01-04

---


## 128. Use Claude Code CLI for Building Apps with Terminal Guidance
**Source:** Erica (Devto)

Leverage Claude Code's terminal integration to build applications. The AI can observe commands, understand context, and offer real-time assistance while you build a system, potentially streamlining the development process compared to manual methods or spreadsheets. This allows Claude to guide the entire process directly from the terminal.

[Original](https://dev.to/eriperspective/ai-engineering-advent-of-ai-with-goose-day-13-scheduling-application-4069) | Added: 2026-01-05

---


## 130. Executable Markdown with Claude Code CLI via shebang
**Source:** jedwhite (Reddit)

This tip introduces an open-source tool that allows you to execute markdown files using Claude Code. By adding a shebang line (#!/usr/bin/env claude-run) to your markdown file, you can treat it as an executable script that utilizes Claude Code for processing, enabling workflows like automated codebase analysis and summarization directly from a markdown document.

[Original](https://www.reddit.com/r/ClaudeAI/comments/1q44kkd/make_markdown_files_executable_with_claude_code/) | Added: 2026-01-05

---


## 134. Tidy Claude Code: Remove Unused MCP Servers
**Source:** sr-white (Hackernews)

The `mcp-tidy` tool helps manage Claude Code's MCP server configurations by listing configured servers, checking their actual usage from transcript logs, and removing unused ones. This prevents unnecessary overhead from loading descriptions of forgotten servers into context, keeping Claude Code sessions leaner and more efficient.

[Original](https://github.com/nnnkkk7/mcp-tidy) | Added: 2026-01-07

---


## 135. Tidy Claude Code Configs with mcp-tidy
**Source:** sr-white (Hackernews)

The `mcp-tidy` tool helps manage your Claude Code MCP server configurations by listing configured servers, checking usage from transcript logs, and removing unused server entries. This prevents accumulating outdated server definitions in your `~/.claude.json`, which can reduce unnecessary overhead during Claude Code execution. Use `mcp-tidy list`, `mcp-tidy stats`, and `mcp-tidy remove` commands to maintain a clean and efficient configuration.

[Original](https://github.com/nnnkkk7/mcp-tidy) | Added: 2026-01-07

---


## 144. Claude Code CLI: Slash Commands Merged Into Skills
**Source:** shanraisshan (Reddit)

The SlashCommand tool is now integrated into the Skill tool within Claude Code CLI. This change simplifies the internal structure, meaning skills are now accessible via the slash command menu. However, existing folder structures in .claude/commands/ and .claude/skills/ remain unchanged, and your previously created commands and skills will function as before.

[Original](https://www.reddit.com/r/ClaudeAI/comments/1q92wwv/merged_commands_and_skills_in_213_update/) | Added: 2026-01-11

---


## 149. Integrate Google NotebookLM with Claude Code CLI
**Source:** Opposite_Fox5559 (Reddit)

This tip shows how to extend Claude Code CLI's capabilities by integrating with Google NotebookLM via an updated 'notebooklm-py' library. By injecting a custom skill into Claude, users can manage their NotebookLM research directly from the terminal, streamlining workflows and reducing context switching. This involves using a specific command to automatically inject the tool into Claude Code CLI, enhancing its functionality.

[Original](https://www.reddit.com/r/ClaudeAI/comments/1qasqn5/i_gave_claude_code_full_control_of_google/) | Added: 2026-01-13

---


## 150. Leverage Claude's Global Config and MCP Servers
**Source:** TheDecipherist (Reddit)

Use a global `~/.claude/CLAUDE.md` file to enforce project structure and prevent accidental secret exposure. MCP servers drastically expand Claude's capabilities. Context7 provides up-to-date documentation access. Custom commands and agents automate common tasks. Avoid mixing topics in a single chat to maintain performance and focus.

[Original](https://www.reddit.com/r/ClaudeAI/comments/1qbkk1n/the_complete_guide_to_claude_code_global_claudemd/) | Added: 2026-01-14

---

*[Back to Categories](../README.md)*
