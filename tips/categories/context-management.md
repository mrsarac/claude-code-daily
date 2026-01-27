# 📝 Context Management Tips

> Markdown bridges between sessions. Zero knowledge loss.

---

## 4. Markdown Bridge Documents
**Source:** Saad

After every significant session, have Claude dump everything into a `.md` file with strict naming conventions.

```markdown
# SESSION_2025-12-31_auth-implementation.md

## Completed
- [x] JWT token generation
- [x] Refresh token flow

## Next Steps
- [ ] Add rate limiting
- [ ] Implement logout

## Key Decisions
- Using RS256 for token signing (security requirement)
```

---

## 13. Date Check Discipline
**Source:** Matthew Bergvinson

Add to your CLAUDE.md:
```markdown
### SESSION STARTUP (MANDATORY)
1. CHECK DATE: Always verify today's date
2. LOAD BRIDGE: Read corecontext.md
```

---

## 14. Pre-tagging Files
**Source:** Hubab

Tag relevant files before starting work. Use voice dictation to quickly mark files as "relevant to current task."

---

## 15. The Follow-Up Command
**Source:** Felipe Matos

Create a `/follow-up` command that triggers when context reaches 70%:
- Summarize completed work
- Prepare self-contained prompt for next session
- List key files modified

---

## 16. Compact for Clarity
**Source:** XenZee

`/compact` isn't just for cleanup—it's **mandatory** in long sessions to prevent "hallucination fog."

---

## 17. SQLite as Project Context
**Source:** Buddy Hadry

Use SQLite database as project context storage. Tables for decisions, file changes, and session history.

---

## 18. Clean Start Philosophy
**Source:** Magnus

Write plans continuously. When a phase completes, clear the session. Fresh start = fresh context = better output.

---

## 19. Continuous Claude
**Source:** dei

For context-preserving setups, check out [Continuous-Claude](https://github.com/parcadei/Continuous-Claude).

---

## 20. Team Memory Through Git
**Source:** Dipen Ved

Dump all context to a `.md` file, commit to git. Team members can pick up where you left off.

---

## 48. Live Documentation
**Source:** Duncan Soar

Maintain `corecontext.md` for new sessions, plus individual feature roadmaps for cross-session reference.

---



## 53. Memento: Give Claude Code Persistent Memory So You Stop Repe
**Source:** Sean K (Devto)

If you use Claude Code, you've probably had this experience:



You: Install the dependencies
Claude: npm install
You: No, use pnpm in this project
Claude: pnpm install





Next session? Same thing. 

[Original](https://dev.to/sean8/memento-give-claude-code-persistent-memory-so-you-stop-repeating-yourself-22je) | Added: 2026-01-04

---


## 55. Fixing Claude Code's Concurrent Session Problem: Implementin
**Source:** pepk (Devto)


  
  
  The Problem


Have you ever seen this error while running multiple Claude Code sessions?



Error: database is locked






Yeah, that was my first reaction too: "Wait, seriously?"

Memory MC

[Original](https://dev.to/daichikudo/fixing-claude-codes-concurrent-session-problem-implementing-memory-mcp-with-sqlite-wal-mode-o7k) | Added: 2026-01-04

---


## 59. Claude Code in Terminal: A Beginner's Guide to 10x Faster De
**Source:** Ege Pakten (Devto)

A beginner's guide to supercharging your development workflow with Claude Code





This space is for beginners and new grads who want practical, no-nonsense tutorials. Explore more posts at kerempakt

[Original](https://dev.to/egepakten/claude-code-in-terminal-a-beginners-guide-to-10x-faster-development-3196) | Added: 2026-01-04

---


## 60. Oh My Posh ❤️ Claude Code
**Source:** Jan De Dobbeleer (Devto)

Terminal customization just got a lot smarter. Oh My Posh now integrates with Claude Code through its statusline functionality, bringing real-time AI session information  and development context direc

[Original](https://dev.to/jandedobbeleer/oh-my-posh-claude-code-66f) | Added: 2026-01-04

---


## 69. Fixing Claude Code's SIGINT Problem: How I Built MCP Session
**Source:** pepk (Devto)


  
  
  Introduction


In my previous article, I implemented a WAL-mode SQLite backend for Memory MCP to solve database locking issues.

But that wasn't the end of the story.



[MCP Disconnected] me

[Original](https://dev.to/daichikudo/fixing-claude-codes-sigint-problem-how-i-built-mcp-session-manager-3nke) | Added: 2026-01-04

---


## 76. AI Engineering: Advent of AI with goose Day 13 - AI Scheduli
**Source:** Erica (Devto)

Day 13: Building a Complete Scheduling System with Terminal Integration

Today’s challenge focused on transforming scattered staff availability notes into a fully functional scheduling application. In

[Original](https://dev.to/eriperspective/ai-engineering-advent-of-ai-with-goose-day-13-scheduling-application-4069) | Added: 2026-01-04

---


## 80. Show HN: CCC – Control Claude Code Sessions Remotely via Tel
**Source:** kidandcat (Hackernews)


I built ccc to control Claude Code sessions from my phone via Telegram. It lets you start sessions remotely, get notifications when Claude finishes tasks, and seamlessly switch between phone and PC.F

[Original](https://github.com/kidandcat/ccc) | Added: 2026-01-04

---


## 87. Show HN: Cck ClaudeCode file change tracking and auto Claude
**Source:** takawasi (Hackernews)


Every Claude Code session starts fresh. You re-explain your project structure, build commands, and conventions. Every. Single. Time.I built cck to solve this. Two modes:*1. CLAUDE.md Generation*
```b

[Original](https://news.ycombinator.com/item?id=46435083) | Added: 2026-01-04

---


## 94. I got tired of Claude forgetting what it learned, so I built
**Source:** entheosoul (Reddit)

      After months of using Claude Code daily, I kept hitting the same wall: Claude would spend 20 minutes investigating something, learn crucial patterns about my codebase, then... memory compact. Go

[Original](https://www.reddit.com/r/ClaudeAI/comments/1q36l43/i_got_tired_of_claude_forgetting_what_it_learned/) | Added: 2026-01-04

---


## 96. Claude built me a WebUI to access Cli on my machine via mobi
**Source:** Salt-Willingness-513 (Reddit)

      Still amazed of this tool. Built this within some hours and even supports stuff like direct image upload and limit/context visualization. All directly built on my Unraid machine as docker contai

[Original](https://www.reddit.com/r/ClaudeAI/comments/1q30825/claude_built_me_a_webui_to_access_cli_on_my/) | Added: 2026-01-04

---


## 97. Built 30+ projects with Claude Code last year - so I made a 
**Source:** Equivalent-Yak2407 (Reddit)

I&#39;ve shipped over 30 side projects using Claude Code in the last year. VS Code extensions, SEO tools, SaaS apps, you name it. I keep seeing others here doing the same - shipping fast, stacking pro

[Original](https://www.reddit.com/r/ClaudeAI/comments/1q37sf3/built_30_projects_with_claude_code_last_year_so_i/) | Added: 2026-01-04

---


## 98. My claude code setup and how I got there
**Source:** moonshinemclanmower (Reddit)

      This last year has been hell of a journey, I&#39;ve had 8 days off this year and worked 18 hour stints for most of them, wiggling LLMs into bigger and smaller context windows with an obsessive c

[Original](https://www.reddit.com/r/ClaudeAI/comments/1q2snn6/my_claude_code_setup_and_how_i_got_there/) | Added: 2026-01-04

---


## 101. Claude Overflow - a plugin that turns Claude Code conversati
**Source:** ConstIsNull (Reddit)

      Had a fun experiment this morning: what if every time Claude answered a technical question, it automatically saved the response to a local StackOverflow-style site? What it does:  Intercepts tec

[Original](https://www.reddit.com/r/ClaudeAI/comments/1q31b93/claude_overflow_a_plugin_that_turns_claude_code/) | Added: 2026-01-04

---


## 103. Claude Code not reset the 5-hour limits!
**Source:** Necessary-Street-411 (Reddit)

It really upsets me that Claude Code very often does not clear the 5-hour usage. Two days ago I ended the day with 27% usage. 10 hours later I started a session with the same usage. It did not reset t

[Original](https://www.reddit.com/r/ClaudeAI/comments/1q2vbf4/claude_code_not_reset_the_5hour_limits/) | Added: 2026-01-04

---


## 104. Remote AI CLI Workflow via SSH client.
**Source:** whyjustwhyguy (Reddit)

I put together this &quot;document&quot; to help with setup to get a notification on a handheld device, like a smart phone or tablet Android or iOS, and the ability to type in response prompts into a 

[Original](https://www.reddit.com/r/ClaudeAI/comments/1q2uama/remote_ai_cli_workflow_via_ssh_client/) | Added: 2026-01-04

---


## 109. AI-Connect: Let your Claude Code instances talk to each othe
**Source:** Peuqui (Reddit)

TL;DR: Built an MCP bridge that lets multiple Claude Code instances communicate across machines. They can ask each other for code reviews, share context, and reach consensus on decisions. Early/rough 

[Original](https://www.reddit.com/r/ClaudeAI/comments/1q356ka/aiconnect_let_your_claude_code_instances_talk_to/) | Added: 2026-01-04

---


## 112. My claude code setup for work, and how I got there over the 
**Source:** moonshinemclanmower (Reddit)

This last year has been a journey, I&#39;ve had 8 days off this year and worked 18 hour stints for most of them, wiggling LLMs into bigger and smaller context windows with an obsessive commitment to f

[Original](https://www.reddit.com/r/ClaudeAI/comments/1q2uhqe/my_claude_code_setup_for_work_and_how_i_got_there/) | Added: 2026-01-04

---


## 115. I turned Spanish learning into a git repo + LLM prompts + a 
**Source:** curious_shawnyv (Reddit)

I’ve tried the normal ways to learn Spanish: apps, random Anki decks, half-finished grammar notebooks, podcasts, the “I’ll just grind Duolingo for 30 days” phase… you know the drill. The issue wasn’t 

[Original](https://www.reddit.com/r/ClaudeAI/comments/1q32cx2/i_turned_spanish_learning_into_a_git_repo_llm/) | Added: 2026-01-04

---


## 121. Use CLAUDE.md to Enforce Project Conventions
**Source:** Sean K (Devto)

Claude Code uses CLAUDE.md files to understand project conventions. Instead of manually correcting Claude repeatedly, proactively populate CLAUDE.md with key information like preferred package managers (e.g., "Use pnpm for dependency management") to ensure consistent behavior across sessions and avoid repetitive corrections.

[Original](https://dev.to/sean8/memento-give-claude-code-persistent-memory-so-you-stop-repeating-yourself-22je) | Added: 2026-01-04

---


## 124. CCK: Automate Claude Code Context Management
**Source:** takawasi (Hackernews)

Use Claude Context Keeper (CCK) to automatically generate a CLAUDE.md file summarizing your project for Claude Code, ensuring consistent context. Also allows per-turn context injection with history using the `cck watch --with-history` command, streamlining your workflow.

[Original](https://news.ycombinator.com/item?id=46435083) | Added: 2026-01-04

---


## 126. Use CLAUDE.md to persist project setup instructions
**Source:** Sean K (Devto)

Claude Code reads `CLAUDE.md` files to understand project conventions. Maintain a `CLAUDE.md` to instruct Claude Code to use specific tools (like pnpm) and configurations, avoiding repeated corrections across sessions. This provides a way to persist project-specific instructions without relying on session history.

[Original](https://dev.to/sean8/memento-give-claude-code-persistent-memory-so-you-stop-repeating-yourself-22je) | Added: 2026-01-05

---


## 129. Automate Claude Code Context with cck
**Source:** takawasi (Hackernews)

Use Claude Context Keeper (cck) to automate the creation and injection of context into your Claude Code sessions. This tool scans your codebase to generate a `CLAUDE.md` file for initial context and offers per-turn context injection, ensuring Claude Code is always aware of project details without manual re-explanation. Install with `pip install .` and sync your project with `cck sync`.

[Original](https://news.ycombinator.com/item?id=46435083) | Added: 2026-01-05

---


## 132. CCK: Automate Claude Code Context with CLAUDE.md
**Source:** takawasi (Hackernews)

Use the `claude-context-keeper` (cck) CLI tool to automatically generate a `CLAUDE.md` file containing your project structure, build commands, and conventions. This file can then be provided to Claude Code at the start of each session to avoid repetitive explanations, improving efficiency and consistency in your workflow.

[Original](https://news.ycombinator.com/item?id=46435083) | Added: 2026-01-06

---


## 136. Use CLAUDE.md to Persist Project Conventions
**Source:** Sean K (Devto)

Claude Code uses CLAUDE.md to learn project conventions, but manually maintaining this file is tedious. By actively updating CLAUDE.md with specific commands and preferences, you ensure that Claude consistently uses tools like `pnpm` instead of defaulting to `npm` across different sessions, avoiding repeated corrections and improving workflow efficiency.

[Original](https://dev.to/sean8/memento-give-claude-code-persistent-memory-so-you-stop-repeating-yourself-22je) | Added: 2026-01-08

---


## 137. CCK: Automate Claude Code Context with CLI
**Source:** takawasi (Hackernews)

Use the `claude-context-keeper` (cck) CLI to automatically generate a `CLAUDE.md` file containing your project's structure and conventions. This provides Claude Code with essential context at the start of each session, eliminating repetitive explanations. Additionally, `cck watch --with-history` enables per-turn context injection, providing even richer contextual awareness for Claude Code.

[Original](https://news.ycombinator.com/item?id=46435083) | Added: 2026-01-08

---


## 139. Make Claude Code remember conventions with CLAUDE.md
**Source:** Sean K (Devto)

Claude Code reads CLAUDE.md at the start of each session to learn project conventions. To avoid repeatedly correcting Claude, document important conventions like preferred package managers (e.g., pnpm install) in a CLAUDE.md file at the root of your project.

[Original](https://dev.to/sean8/memento-give-claude-code-persistent-memory-so-you-stop-repeating-yourself-22je) | Added: 2026-01-09

---


## 143. CCK: Automate Claude Code context using CLAUDE.md
**Source:** takawasi (Hackernews)

Use Claude Context Keeper (CCK) to automatically generate a CLAUDE.md file that summarizes your project structure, commands, and conventions. This eliminates the need to manually re-explain your project at the start of each Claude Code session, improving efficiency and reducing boilerplate. CCK can also inject context per turn, further enhancing Claude's understanding.

[Original](https://news.ycombinator.com/item?id=46435083) | Added: 2026-01-11

---


## 147. CCK: Automate Claude Code Project Context Injection
**Source:** takawasi (Hackernews)

Use Claude Context Keeper (CCK) to automatically generate a CLAUDE.md file summarizing your project, ensuring Claude Code always has the necessary context.  Then use `cck watch --with-history` to inject relevant history and context on each turn.  This eliminates redundant explanations and allows Claude Code to reason from a known state.

[Original](https://news.ycombinator.com/item?id=46435083) | Added: 2026-01-12

---


## 151. Custom MCP server for focused context
**Source:** betauser123 (Reddit)

This tip introduces a custom MCP server using the Claude Code CLI to provide Claude with targeted context, improving efficiency and reducing token usage. The server, implemented via `claude mcp add --scope user --transport stdio scantool -- uvx scantool`, leverages tree-sitter for parsing, call graph generation, and entropy analysis to extract relevant code snippets, enhancing Claude's ability to understand and process information effectively.

[Original](https://www.reddit.com/r/ClaudeAI/comments/1qd3afo/i_built_an_mcp_server_that_gives_claude_a_birds/) | Added: 2026-01-15

---


## 152. Manage Claude.md Size for Better Performance
**Source:** Eugene Oleinik (Devto)

Large CLAUDE.md files negatively impact Claude Code's performance by reducing available context and triggering more frequent compactions. Regularly review and trim CLAUDE.md to maintain optimal context window size and prevent degradation in session length and agent coherence. Consider using techniques to summarize or prioritize learnings within the CLAUDE.md file.

[Original](https://dev.to/evoleinik/the-best-agent-architecture-is-already-in-your-terminal-1fg0) | Added: 2026-01-16

---


## 153. Name Your Claude Sessions for Better Context Retrieval
**Source:** Rajesh Royal (Devto)

To avoid losing track of conversations and context in Claude Code, name your sessions descriptively. This helps you quickly identify and revisit specific discussions, especially when working on complex projects like code migrations or API refactoring, ensuring you can easily find past insights and solutions.

[Original](https://dev.to/rajeshroyal/named-sessions-your-git-branches-have-names-why-shouldnt-your-claude-sessions-43oc) | Added: 2026-01-16

---


## 154. CCK: Automate Claude Code Context & History Injection
**Source:** takawasi (Hackernews)

Use Claude Context Keeper (CCK) to automatically generate a CLAUDE.md file summarizing your project for Claude Code, ensuring it has the necessary context at the start of each session.  The `cck watch --with-history` command injects relevant code snippets and past conversation history into each turn, significantly improving Claude Code's understanding and ability to assist with complex coding tasks without manual copy-pasting.

[Original](https://news.ycombinator.com/item?id=46435083) | Added: 2026-01-17

---


## 155. Name Your Claude Sessions for Better Context
**Source:** Rajesh Royal (Devto)

Avoid losing track of your Claude sessions by naming them descriptively. This simple organizational habit can save you time and frustration, especially when working on complex projects involving multiple interactions with Claude. Clearly named sessions make it easy to quickly identify and revisit specific discussions or code explorations.

[Original](https://dev.to/rajeshroyal/named-sessions-your-git-branches-have-names-why-shouldnt-your-claude-sessions-43oc) | Added: 2026-01-18

---


## 156. CCK: Automate Claude Code Context with CLAUDE.md & Watch
**Source:** takawasi (Hackernews)

Use Claude Context Keeper (CCK) to automatically generate a `CLAUDE.md` file containing your project's structure and conventions, enabling Claude Code to start sessions with full context. Additionally, CCK's `watch` command injects relevant file history into each turn, improving Claude Code's awareness and problem-solving capabilities.

[Original](https://news.ycombinator.com/item?id=46435083) | Added: 2026-01-18

---


## 160. CCK: Claude Context Keeper CLI for Consistent Claude Code Sessions
**Source:** takawasi (Hackernews)

Use Claude Context Keeper (CCK) to automate Claude Code session setup.  CCK generates a `CLAUDE.md` file summarizing your project structure, commands, and conventions for Claude to read at the start of each session. It also offers per-turn context injection to maintain consistency across interactions, eliminating repetitive explanations and ensuring Claude always has the necessary context for effective collaboration.

[Original](https://news.ycombinator.com/item?id=46435083) | Added: 2026-01-19

---


## 163. Automate Claude Context with cck
**Source:** takawasi (Hackernews)

Use the `cck` (Claude Context Keeper) CLI tool to automate context management in your Claude Code sessions.  Generate a `CLAUDE.md` file summarizing your project structure and conventions, which Claude can read at the start of each session.  The `cck watch` command can also inject relevant historical context into each turn, improving Claude's understanding and reducing the need for repetitive explanations.

[Original](https://news.ycombinator.com/item?id=46435083) | Added: 2026-01-20

---


## 165. Compact Claude Code Context for Smaller Payloads
**Source:** anton (Devto)

Claude Code stores conversations locally and sends the entire history to Anthropic's servers with each message. Using the `/compact` command creates a summary checkpoint, significantly reducing API payload sizes (around 85%) at the cost of losing granular context from the older messages. This tip highlights how to manage and reduce the size of conversation history being sent to the API.

[Original](https://dev.to/rigby_/what-actually-happens-when-you-run-compact-in-claude-code-3kl9) | Added: 2026-01-21

---


## 166. Compacting Claude Code Conversations for Smaller Payloads
**Source:** anton (Devto)

Claude Code stores conversation history locally and sends it to Anthropic's servers with each message. Using the `/compact` command creates a summary checkpoint, significantly reducing API payload sizes (approximately 85%). This helps manage context and reduce costs, but it sacrifices fine-grained context from the entire history.

[Original](https://dev.to/rigby_/what-actually-happens-when-you-run-compact-in-claude-code-3kl9) | Added: 2026-01-21

---


## 167. Managing Claude Code Context with /clear and REWRITE.MD
**Source:** Dacadey (Reddit)

To prevent Claude Code from running out of context during multi-stage refactoring, instruct it to use the `/clear` command at the end of each stage. This clears the current context. Then, ask it to read a file like `REWRITE.MD` to refresh its understanding of the rewrite plan and progress, avoiding code quality degradation while maintaining context.

[Original](https://www.reddit.com/r/ClaudeAI/comments/1qhz46z/how_do_you_stop_running_out_of_context_on_long/) | Added: 2026-01-21

---


## 169. Compact Claude Code Context to Reduce Payload Size
**Source:** anton (Devto)

Claude Code stores conversation history locally and sends it to Anthropic with each message. The `/compact` command creates a summary checkpoint, significantly reducing API payload size (around 85%), but this comes at the cost of losing granular context. This tip highlights the trade-off between payload size and context retention when using `/compact`.

[Original](https://dev.to/rigby_/what-actually-happens-when-you-run-compact-in-claude-code-3kl9) | Added: 2026-01-22

---


## 170. Streamline Claude Code with Context Keeper (CCK)
**Source:** takawasi (Hackernews)

Use Claude Context Keeper (CCK) to automate context injection for Claude Code.  CCK generates a comprehensive CLAUDE.md file from your codebase that Claude reads at the beginning of each session, or injects relevant files into each turn. Install with `pip install .` and then use `cck sync` to create CLAUDE.md or `cck setup --cb-style` followed by `cck watch --with-history` for per-turn context injection.

[Original](https://news.ycombinator.com/item?id=46435083) | Added: 2026-01-22

---


## 174. Use @ to Inject Files and Directories into Claude Code Prompts
**Source:** Rajesh Royal (Devto)

The `@` mention in Claude Code allows you to directly inject file contents or directory listings into your prompts. This avoids having to copy and paste content or manually specify file paths, speeding up the process of providing context to Claude. This streamlines the interaction and eliminates friction when working with code.

[Original](https://dev.to/rajeshroyal/-mentions-the-2-character-shortcut-that-10x-your-ai-coding-speed-3jej) | Added: 2026-01-23

---


## 175. Reduce Claude Code API Payloads with /compact
**Source:** anton (Devto)

Claude Code CLI stores conversation history locally and sends the full history with each API request. The `/compact` command creates a summary checkpoint, significantly reducing the size of API payloads (approximately 85%) at the cost of some granular context. This can improve performance and reduce costs, but users should be aware of the trade-off between payload size and context retention.

[Original](https://dev.to/rigby_/what-actually-happens-when-you-run-compact-in-claude-code-3kl9) | Added: 2026-01-23

---


## 177. Use @ Mentions for Universal Context Injection in Claude Code
**Source:** Rajesh Royal (Devto)

The `@` mention feature in Claude Code allows you to directly inject files, list directories, or invoke tools into your prompt. This eliminates the need to manually navigate file trees or copy paths, streamlining the process of providing context to Claude and improving coding efficiency. Use `@` followed by the action to inject the necessary context.

[Original](https://dev.to/rajeshroyal/-mentions-the-2-character-shortcut-that-10x-your-ai-coding-speed-3jej) | Added: 2026-01-24

---


## 178. CCK: Automate Claude Code context with CLAUDE.md and history
**Source:** takawasi (Hackernews)

Use Claude Context Keeper (CCK) to automate context management for Claude Code sessions. Generate a `CLAUDE.md` file containing project structure and conventions, which Claude reads at session start. Enable per-turn context injection with `cck watch --with-history` for automated history inclusion.

[Original](https://news.ycombinator.com/item?id=46435083) | Added: 2026-01-24

---


## 179. Breadcrumbs: Git-Based Context Saving for Long Claude Code Runs
**Source:** entheosoul (Reddit)

Use "breadcrumbs", a pair of shell scripts leveraging git notes and jq, to save Claude's state before context compaction and reload it at session start. This helps Claude remember its progress, decisions, uncertainties, and next steps when working on long loops, preventing it from getting lost due to context limits. This solution involves pre-compaction and session-start hooks.

[Original](https://www.reddit.com/r/ClaudeAI/comments/1ql30yu/when_your_claude_code_session_compacts_midloop/) | Added: 2026-01-24

---


## 182. CCK: Automate Claude Code Context with CLAUDE.md & History
**Source:** takawasi (Hackernews)

Use Claude Context Keeper (CCK) to automatically generate a CLAUDE.md file summarizing your project and inject it into Claude Code sessions, ensuring Claude always has the necessary context.  The `cck sync` command generates the CLAUDE.md, and `cck watch --with-history` automatically includes previous turns to further improve context retention.

[Original](https://news.ycombinator.com/item?id=46435083) | Added: 2026-01-25

---


## 184. PMP-GYWD: Manage Claude Code Context with File Persistence
**Source:** Hawkbetsdefi (Reddit)

The PMP-GYWD framework helps manage Claude Code's context window limitations by automatically persisting project decisions and specifications into structured files. This includes architecture, test strategies, and feature planning in dedicated directories (.planning/, .claude-plugin/, .commands/gywd/). The `gywd init` command sets up the project's memory structure.

[Original](https://www.reddit.com/r/ClaudeAI/comments/1qlyrki/meet_pmpgywd/) | Added: 2026-01-25

---


## 185. Compact Claude Code Context for Smaller API Payloads
**Source:** anton (Devto)

Claude Code stores conversation history locally and sends it with each message. Using the `/compact` command creates a summary checkpoint, significantly reducing API payload sizes (around 85%). While this shrinks the context, it sacrifices granular detail from the previous conversation, balancing payload size with contextual precision.

[Original](https://dev.to/rigby_/what-actually-happens-when-you-run-compact-in-claude-code-3kl9) | Added: 2026-01-26

---


## 186. CCK: Automate Claude Code context injection
**Source:** takawasi (Hackernews)

The Claude Context Keeper (CCK) CLI automates context injection for Claude Code. It generates a CLAUDE.md file with project information, and automatically injects relevant files and conversation history into each turn using `cck watch --with-history`, eliminating repetitive project setup and improving efficiency.

[Original](https://news.ycombinator.com/item?id=46435083) | Added: 2026-01-26

---


## 188. Reduce Claude API payload size via /compact
**Source:** anton (Devto)

Claude Code stores conversation history locally and sends the full history with each message. The `/compact` command creates a summary checkpoint, reducing API payload size by approximately 85%. While this shrinks the payload, it also results in a loss of granular context from earlier messages, so use judiciously.

[Original](https://dev.to/rigby_/what-actually-happens-when-you-run-compact-in-claude-code-3kl9) | Added: 2026-01-27

---

*[Back to Categories](../README.md)*