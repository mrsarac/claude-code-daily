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


## 161. Use Ollama with Claude Code by Setting Environment Variables
**Source:** codemee (Devto)

You can configure Claude Code to use Ollama as a backend by setting the `ANTHROPIC_AUTH_TOKEN` and `ANTHROPIC_BASE_URL` environment variables. This allows Claude Code to use local or cloud-based models served by Ollama instead of the Anthropic API. The tip provides the exact environment variables and explains how to configure the base URL for both local and remote Ollama servers.

[Original](https://dev.to/codemee/rang-claude-code-chuan-jie-ollama-shi-yong-ben-di-duan-mo-xing-5aph) | Added: 2026-01-20

---


## 162. Customize Claude Code with PreToolUse Hooks
**Source:** Mike Lane (Devto)

Claude Code's PreToolUse hook system allows you to intercept and modify tool calls before execution. This lets you enforce project-specific rules, block dangerous operations (like `git reset --hard`), and inject contextual guidance, ensuring that the AI coding assistant adheres to your team's standards and conventions, rather than just its default training.

[Original](https://dev.to/mikelane/building-guardrails-for-ai-coding-assistants-a-pretooluse-hook-system-for-claude-code-ilj) | Added: 2026-01-20

---


## 164. Customize Claude Code Status Line
**Source:** yksugi (Reddit)

Customize the Claude Code CLI status line to display information such as the model, current directory, git branch, uncommitted file count, sync status, and token usage. Displaying the last message can also be useful to provide persistent context of the last prompt.

[Original](https://www.reddit.com/r/ClaudeAI/comments/1qgccgs/25_claude_code_tips_from_11_months_of_intense_use/) | Added: 2026-01-20

---


## 168. Customize Claude Code Behavior with PreToolUse Hooks
**Source:** Mike Lane (Devto)

Leverage Claude Code's PreToolUse hook system to enforce project-specific rules and prevent undesirable actions. This allows you to intercept tool calls before they're executed, blocking operations like 'git reset --hard' and injecting guidance such as mandating GPG-signed commits or using a specific GitHub organization. This ensures Claude Code adheres to your team's standards and workflows.

[Original](https://dev.to/mikelane/building-guardrails-for-ai-coding-assistants-a-pretooluse-hook-system-for-claude-code-ilj) | Added: 2026-01-22

---


## 171. Claude Code CLI: History-Based Autocomplete
**Source:** BuildwithVignesh (Reddit)

The Claude Code CLI now supports history-based autocomplete in bash mode. Users can type a partial command and press Tab to complete it from their bash command history, streamlining command entry and recall of previous commands. This feature improves efficiency and reduces typing errors when using the CLI for complex workflows.

[Original](https://www.reddit.com/r/ClaudeAI/comments/1qj9g2a/official_anthropic_just_released_claude_code_2114/) | Added: 2026-01-22

---


## 172. Install Claude Code CLI on Windows with Scoop
**Source:** 0xkoji (Devto)

This tip shows how to install Git via Scoop (a Windows package manager), set the path for Git Bash, and then install Claude Code using the provided PowerShell script. Finally, it validates the installation by checking the Claude Code version. This automates and simplifies the Claude Code CLI installation process on Windows.

[Original](https://dev.to/0xkoji/install-claude-code-on-windows-with-scoop-2452) | Added: 2026-01-23

---


## 173. Fix 'claude' not recognized error on Windows
**Source:** Yuto Takashi (Devto)

If you encounter a 'claude' is not recognized error on Windows after an update, it's due to Claude Code migrating to a new installation location. To fix this, you need to update your system's PATH environment variable to include the new Claude Code executable directory, resolving the issue and allowing you to use the `claude` command again.

[Original](https://dev.to/tielec-takashi/claude-code-stopped-working-on-windows-heres-the-quick-fix-5a36) | Added: 2026-01-23

---


## 176. Fix 'claude' command not recognized on Windows
**Source:** Yuto Takashi (Devto)

After Claude Code's auto-migration to native installation, the 'claude' command might not be recognized. The fix involves adding the new installation directory to your system's PATH environment variable, resolving the "'claude' is not recognized" error on Windows and restoring Claude Code CLI functionality.

[Original](https://dev.to/tielec-takashi/claude-code-stopped-working-on-windows-heres-the-quick-fix-5a36) | Added: 2026-01-24

---


## 180. Install Claude Code on Windows via Powershell
**Source:** 0xkoji (Devto)

This tip details how to install Claude Code CLI on Windows using Powershell and Scoop. First, install git via Scoop, then set an environment variable for the git bash path. Finally, install Claude Code using the provided install script and verify the installation by checking the version. This simplifies the setup process for Windows users.

[Original](https://dev.to/0xkoji/install-claude-code-on-windows-with-scoop-2452) | Added: 2026-01-25

---


## 181. Fix 'claude not recognized' error on Windows
**Source:** Yuto Takashi (Devto)

After Claude Code CLI's auto-migration to a native installation on Windows, the 'claude' command may not be recognized. This tip explains that the executable is in a new location not included in your system's PATH environment variable, and instructs users to update their PATH to resolve the issue and restore functionality. This is a quick and easy fix.

[Original](https://dev.to/tielec-takashi/claude-code-stopped-working-on-windows-heres-the-quick-fix-5a36) | Added: 2026-01-25

---


## 195. /copy command for easy clipboard access
**Source:** yksugi (Reddit)

The `/copy` command in Claude Code CLI allows you to quickly copy Claude's last response to your clipboard as markdown. This is useful for incorporating Claude's output into other documents or tools without manual copying and pasting.

[Original](https://www.reddit.com/r/ClaudeAI/comments/1qqxkuj/5_new_claude_code_tips_from_the_past_12_days/) | Added: 2026-01-31

---


## 196. Claude Code Plugins: Power-Up Your Workflows
**Source:** Dull_Preference_1873 (Reddit)

Leverage Claude Code plugins for enhanced workflows. Plugins bundle skills, MCPs, hooks, and agents into a single install, providing versioning, documentation, and easy management through the `/plugin` command. This centralizes dependencies and facilitates maintenance.

[Original](https://www.reddit.com/r/ClaudeAI/comments/1qrlsly/everyones_hyped_on_skills_but_claude_code_plugins/) | Added: 2026-01-31

---


## 199. Automate Claude Code workflows with Pre/Post Tool Hooks
**Source:** IulianHI (Reddit)

Leverage Claude Code's `PreToolUse` and `PostToolUse` hooks in `.claude/settings.json` to automatically trigger actions before and after tool calls. This enables automated linting after file edits or security checks before bash commands, enhancing workflow efficiency and security.

[Original](https://www.reddit.com/r/ClaudeAI/comments/1qstcb9/7_claude_code_power_tips_nobodys_talking_about/) | Added: 2026-02-02

---


## 200. Setting Up Claude Code CLI: Install, Auth, REPL
**Source:** Cristian Sifuentes (Devto)

This section focuses on the initial setup of Claude Code CLI. It provides guidance on installing the tool, authenticating it (presumably with API keys or a similar mechanism), and then effectively utilizing the REPL (Read-Eval-Print Loop) for interactive development. Details on editor integration for a more seamless workflow are also highlighted, providing actionable steps to get the CLI up and running.

[Original](https://dev.to/cristiansifuentes/conversational-development-with-claude-code-part-3-installing-trusting-and-operating-the-tool-2ekp) | Added: 2026-02-03

---


## 201. Manage Claude Code Providers with Profiles
**Source:** Rashed Iqbal (Devto)

Use `claude-provider` to manage multiple Claude Code configurations (base URL, key, model) via profiles. This allows you to switch between different providers or settings with a single command, either as a Claude Code plugin (slash commands) or as a standalone CLI tool, avoiding manual edits to the settings file.

[Original](https://dev.to/rashed_iqbal/switch-claude-code-providers-in-seconds-with-claude-provider-plugin-cli-3719) | Added: 2026-02-04

---


## 203. Claude CLI: Control PDF Read & Add MCP OAuth Credentials
**Source:** BuildwithVignesh (Reddit)

The Claude CLI now supports reading specific page ranges from PDFs using the `pages` parameter with the Read tool, optimizing context management for large documents. Additionally, you can now add pre-configured OAuth client credentials for MCP servers (like Slack) that don't support Dynamic Client Registration using the `--client-id` and `--client-secret` flags with the `claude mcp add` command, enabling integration with more platforms.

[Original](https://www.reddit.com/r/ClaudeAI/comments/1qv0oo5/official_anthropic_just_released_claude_code_2130/) | Added: 2026-02-04

---


## 206. Claude Code CLI 2.1.30: PDF Pages and OAuth Client Auth
**Source:** BuildwithVignesh (Reddit)

Claude Code CLI 2.1.30 adds functionality to specify page ranges when reading PDFs using the Read tool (e.g., `pages: "1-5"`). It also introduces pre-configured OAuth client credentials for MCP servers lacking Dynamic Client Registration, enabled via `--client-id` and `--client-secret` with `claude mcp add`. Large PDFs now return a lightweight reference when @ mentioned.

[Original](https://www.reddit.com/r/ClaudeAI/comments/1qv0oo5/official_anthropic_just_released_claude_code_2130/) | Added: 2026-02-05

---


## 217. Configure Claude Code Terminal & Effort Level
**Source:** BuildwithVignesh (Reddit)

Customize your Claude Code CLI experience by configuring terminal themes (light/dark), enabling notifications, and setting up newline handling for specific terminals using `/config` and `/terminal-setup`. Adjust the response verbosity and speed by selecting an effort level (Low, Medium, High) using the `/model` command, trading off token usage for speed.

[Original](https://www.reddit.com/r/ClaudeAI/comments/1r2b5xk/claude_code_creator_boris_shares_12_ways_that/) | Added: 2026-02-12

---


## 220. Managing Claude Code's Disk Usage
**Source:** uppinote (Reddit)

Claude Code's CLI stores session data under `~/.claude`, which can grow significantly over time due to session logs, debug logs, shell snapshots, file edit history, TODO files, and plans. To manage disk space, users can investigate the size of subdirectories within `~/.claude` using `du -sh ~/.claude/*/ | sort -rh` to identify the largest contributors and potentially prune or archive older data to reduce overall storage usage.

[Original](https://www.reddit.com/r/ClaudeAI/comments/1r2snly/cleanup_script_for_claude_mine_grew_to_13gb_in_4/) | Added: 2026-02-13

---


## 221. Customize Claude Code CLI Terminal
**Source:** BuildwithVignesh (Reddit)

This tip details how to configure the Claude Code CLI terminal for optimal usage. It includes commands to set light/dark mode using `/config`, enabling notifications for iTerm2 or setting custom notification hooks, and using `/terminal-setup` to enable shift+enter for newlines in specific terminals like Apple Terminal, Warp, and Alacritty. These customizations improve the user experience within the Claude Code CLI environment.

[Original](https://www.reddit.com/r/ClaudeAI/comments/1r2b5xk/claude_code_creator_boris_shares_12_ways_that/) | Added: 2026-02-13

---


## 224. Claude CLI: Authentication & Session Naming Updates
**Source:** BuildwithVignesh (Reddit)

The Claude CLI changelog introduces `claude auth` subcommands for login, status, and logout, streamlining authentication. Additionally, the `/rename` command now automatically generates session names from conversation context when no arguments are provided, enhancing workflow efficiency. These changes simplify authentication management and session organization within the Claude CLI.

[Original](https://www.reddit.com/r/ClaudeAI/comments/1r3lxpe/official_anthropic_just_released_claude_code_2141/) | Added: 2026-02-14

---


## 227. Generate Claude Code startup files with a script
**Source:** Yurukusa (Devto)

Automate the creation of your CLAUDE.md file using a Bash script. This script prompts you for key information about your project, team conventions, and safety rules, then generates a CLAUDE.md file ready to be used with Claude Code. This eliminates the manual effort of creating the file from scratch and ensures consistency across sessions.

[Original](https://dev.to/yurukusa/generate-your-claudemd-in-30-seconds-interactive-script-54n4) | Added: 2026-02-16

---

*[Back to Categories](../README.md)*
