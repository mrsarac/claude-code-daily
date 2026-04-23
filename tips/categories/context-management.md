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


## 190. Maximize Claude Code Tokens with Context Management
**Source:** Richard Joseph Porter (Devto)

Optimize your Claude Code usage by employing context management commands like `/clear` to reset between unrelated tasks and `/compact` to summarize conversations proactively. This prevents unnecessary token consumption and maintains code quality by focusing the model's attention on relevant information, keeping your usage under the 30K token limit.

[Original](https://dev.to/richardporter/claude-code-token-management-8-strategies-to-save-50-70-on-pro-plan-3hob) | Added: 2026-01-29

---


## 191. CCK: Automate Claude.md for consistent Claude Code context
**Source:** takawasi (Hackernews)

Use the Claude Context Keeper (CCK) CLI tool to automatically generate a CLAUDE.md file describing your project structure, commands, and conventions. This ensures that Claude Code has consistent context at the beginning of each session, preventing the need for repetitive explanations. CCK can also inject relevant history into each turn.

[Original](https://news.ycombinator.com/item?id=46435083) | Added: 2026-01-29

---


## 192. Maximize Claude Code Usage with Context Management
**Source:** Richard Joseph Porter (Devto)

Optimize your Claude Code Pro plan by strategically managing context to avoid token limits. Use `/clear` to reset the context between unrelated tasks, preventing unnecessary token consumption. Employ `/compact` to summarize the context proactively, aiming for 70% capacity, and regularly monitor your usage with `/context`. Targeting under 30K tokens per session will help maintain code quality without hitting limits.

[Original](https://dev.to/richardporter/claude-code-token-management-8-strategies-to-save-50-70-on-pro-plan-3hob) | Added: 2026-01-30

---


## 193. CCK: Automate Claude.md and Context Injection for Claude Code
**Source:** takawasi (Hackernews)

Use Claude Context Keeper (CCK) to automatically generate a CLAUDE.md file that summarizes your project structure, commands, and conventions for Claude Code. CCK also offers per-turn context injection with history, using `cck setup --cb-style` and `cck watch --with-history`, improving Claude's understanding of your codebase and reducing repetitive explanations.

[Original](https://news.ycombinator.com/item?id=46435083) | Added: 2026-01-30

---


## 194. Maintain Context Across Claude Code Sessions with CCK
**Source:** takawasi (Hackernews)

Use Claude Context Keeper (CCK) to maintain project context across Claude Code sessions. CCK generates a CLAUDE.md file with project information that Claude Code reads at the beginning of each session. It can also inject relevant context into each turn using `cck watch --with-history`, improving Claude Code's understanding of your project and code.

[Original](https://news.ycombinator.com/item?id=46435083) | Added: 2026-01-31

---


## 202. CCK: Automate Claude.md for persistent code context
**Source:** takawasi (Hackernews)

Use Claude Context Keeper (CCK) to automatically generate and update a CLAUDE.md file from your codebase.  This file provides Claude with project context at the start of each session, eliminating the need to re-explain project structure, build commands, and conventions repeatedly. Install CCK and use the `cck sync` command to generate CLAUDE.md.

[Original](https://news.ycombinator.com/item?id=46435083) | Added: 2026-02-04

---


## 205. CCK: Automate Claude Code Context with CLAUDE.md and Watch
**Source:** takawasi (Hackernews)

Use Claude Context Keeper (CCK) to automate context management for Claude Code. Generate a CLAUDE.md file from your codebase, which Claude reads at session start, and utilize `cck watch --with-history` for per-turn context injection. This ensures Claude always has the necessary project information, build commands, and conventions without manual re-explanation.

[Original](https://news.ycombinator.com/item?id=46435083) | Added: 2026-02-05

---


## 207. Utilize Persistent Memory with MEMORY.md in Claude Code
**Source:** bitr8 (Reddit)

Claude Code CLI features a persistent memory function. By placing a `MEMORY.md` file within the `~/.claude/projects/<project-path>/memory/` directory, its content will be automatically loaded into the system prompt of each Claude Code session for that project, providing a persistent context for ongoing conversations and tasks.

[Original](https://www.reddit.com/r/ClaudeAI/comments/1qw9hr4/claude_code_has_an_undocumented_persistent_memory/) | Added: 2026-02-06

---


## 209. Automate Claude Context with cck (Claude Context Keeper)
**Source:** takawasi (Hackernews)

Use the `cck` CLI tool to automate context injection for Claude Code. It generates a `CLAUDE.md` file summarizing your project, ensuring Claude always has the necessary information. The tool can also inject relevant files and past conversations during each turn with the `--with-history` flag.

[Original](https://news.ycombinator.com/item?id=46435083) | Added: 2026-02-07

---


## 211. Control Claude Code's Behavior with Configuration
**Source:** Helder Burato Berto (Devto)

Claude Code can be configured to follow specific development standards, like enforcing immutability and TDD. This is crucial to prevent it from making unwanted changes. Clear instructions are necessary to avoid chaotic refactoring or excessive commenting. By properly configuring Claude Code, it can be turned into a tool that consistently aligns with your preferred workflow.

[Original](https://dev.to/helderberto/teaching-claude-code-your-standards-k9p) | Added: 2026-02-08

---


## 212. Streamline Claude Code Sessions with cck
**Source:** takawasi (Hackernews)

Use the `claude-context-keeper` (cck) CLI tool to automate context management in Claude Code. It generates a `CLAUDE.md` file summarizing your project for Claude Code, and it can inject relevant context from your codebase and chat history into each turn. Install with `pip install .`, generate the file with `cck sync`, and use `cck watch --with-history` to inject code snippets and previous messages, significantly improving Claude Code's understanding and performance.

[Original](https://news.ycombinator.com/item?id=46435083) | Added: 2026-02-08

---


## 214. Conserve Context: Avoid Redundant Agent Definitions
**Source:** Helder Burato Berto (Devto)

Claude Code has a limited context window. Avoid using overly detailed agent configurations, examples, or boilerplate. These consume valuable context that could be used for more relevant code analysis, leading to better results. Focus on providing only the necessary information to Claude, reducing redundancy and maximizing the effectiveness of each token.

[Original](https://dev.to/helderberto/what-your-claude-code-agents-dont-need-to-be-told-4ed5) | Added: 2026-02-10

---


## 219. Use CCK to manage Claude Code context
**Source:** takawasi (Hackernews)

The Claude Context Keeper (CCK) CLI tool automatically generates a CLAUDE.md file summarizing your project, enabling Claude Code to start with full context. CCK also offers per-turn context injection, enhancing Claude Code's understanding with relevant code snippets and history. Install with `pip install .`, sync with `cck sync`, set up with `cck setup --cb-style`, and watch with `cck watch --with-history`.

[Original](https://news.ycombinator.com/item?id=46435083) | Added: 2026-02-13

---


## 223. Maintain Claude Code Context with cck
**Source:** takawasi (Hackernews)

Use cck (Claude Context Keeper) to automatically generate a CLAUDE.md file summarizing your project, ensuring Claude Code always has the necessary context.  The `cck sync` command generates the CLAUDE.md, and `cck watch --with-history` injects relevant code history for each turn. This helps avoid redundant explanations in each session.

[Original](https://news.ycombinator.com/item?id=46435083) | Added: 2026-02-14

---


## 229. Optimize Claude Code Agent Token Usage with Task Tool
**Source:** amragl (Reddit)

When using the Task tool in Claude Code with custom agents, each task invocation reloads the entire agent prompt, leading to excessive token usage if agent definitions are large. Keep agent definition files concise to reduce token consumption and improve performance.

[Original](https://www.reddit.com/r/ClaudeAI/comments/1r5mdu0/heads_up_claude_code_task_tool_reloads_full_agent/) | Added: 2026-02-16

---


## 230. CCK: Automate Context Management for Claude Code
**Source:** takawasi (Hackernews)

The Claude Context Keeper (CCK) CLI tool automates the creation and injection of context into Claude Code sessions. It generates a `CLAUDE.md` file summarizing your project and can inject previous turn history into each interaction, eliminating the need to manually re-explain project details or repeat past conversations.

[Original](https://news.ycombinator.com/item?id=46435083) | Added: 2026-02-17

---


## 231. Enable Auto Memory in Claude Code for Performance Boost
**Source:** NegativeCandy860 (Reddit)

If you experience performance differences between Claude Code accounts using the same model and codebase, check if Auto Memory is enabled. Use `/memory` to check its status. If disabled, enable it by setting the environment variable `CLAUDE_CODE_DISABLE_AUTO_MEMORY=0`. This can significantly improve Claude Code's performance by allowing it to automatically retain relevant context.

[Original](https://www.reddit.com/r/ClaudeAI/comments/1r6j36u/claude_codes_auto_memory_is_so_good_make_sure_you/) | Added: 2026-02-17

---


## 235. CCK: Automate Claude Code Context with CLAUDE.md and CLI
**Source:** takawasi (Hackernews)

Use the Claude Context Keeper (CCK) CLI to automatically generate a CLAUDE.md file summarizing your project for Claude Code, ensuring consistent context across sessions. Additionally, CCK can be used to inject per-turn history into Claude Code prompts using `cck watch`, enabling more informed and contextualized interactions.

[Original](https://news.ycombinator.com/item?id=46435083) | Added: 2026-02-19

---


## 236. Streamline Claude Code sessions with cck sync & watch
**Source:** takawasi (Hackernews)

The Claude Context Keeper (cck) CLI tool automates context management for Claude Code. Use `cck sync` to generate a CLAUDE.md file describing your project, which Claude reads at the start of a session. Then, use `cck setup --cb-style` and `cck watch --with-history` to inject relevant code snippets and conversation history into each turn, eliminating redundant explanations and improving context retention.

[Original](https://news.ycombinator.com/item?id=46435083) | Added: 2026-02-20

---


## 241. Backup Claude Code Sessions to Avoid Data Loss
**Source:** decker (Devto)

Claude Code's compaction feature can silently delete session context. To prevent losing work, this tip provides a bash script to backup Claude Code sessions located at ~/.claude/projects/[hash]/[session-id].jsonl to a timestamped directory. This allows for restoring previous session states after compaction.

[Original](https://dev.to/gonewx/claude-code-session-recovery-the-complete-2026-guide-2aml) | Added: 2026-02-22

---


## 242. Consistent Claude Code with CLAUDE.md
**Source:** decker (Devto)

Maintain consistent AI behavior across Claude Code sessions by crafting a detailed and comprehensive CLAUDE.md file. Treat it as a crucial configuration to enforce coding styles, constraints (e.g., avoiding specific libraries like Redux), and project guidelines, preventing the AI from deviating in subsequent sessions.

[Original](https://dev.to/gonewx/the-claudemd-pattern-that-keeps-ai-coding-sessions-consistent-across-weeks-250j) | Added: 2026-02-23

---


## 243. Reduce Claude Code Cost by Managing Context Window Size
**Source:** Ethan Nguyen (Devto)

Reduce Claude Code costs by optimizing the context window. Understanding where tokens are being used and preventing unnecessary context bloat can significantly decrease expenses. Focus on strategies to limit the size of the context passed to Claude Code to achieve similar output quality at a lower cost, such as being more judicious with the files/snippets you include in your prompts.

[Original](https://dev.to/truongnguyenptit/how-i-cut-my-claude-code-bill-by-60-without-losing-productivity-29mn) | Added: 2026-02-23

---


## 245. Claude Code's Hidden Project Memory
**Source:** Dawid M. (Devto)

Claude Code automatically maintains a `MEMORY.md` file within the `~/.claude/projects/<project-path>/memory/` directory, scoped per project. This file persists architectural decisions, conventions, and preferences across sessions as Claude Code learns about your project, acting as an automatically updating project knowledge base.

[Original](https://dev.to/dawidm/claude-code-has-a-hidden-memory-system-you-probably-dont-know-about-4ak3) | Added: 2026-02-23

---


## 246. Use CLAUDE.md for Project Context in Claude Code
**Source:** myougaTheAxo (Devto)

The CLAUDE.md file acts as a briefing document for Claude Code, providing essential context about your project, coding conventions, and areas to avoid modifying. By placing a CLAUDE.md file in your project root, you ensure that each Claude Code session starts with a consistent understanding of the project, preventing the AI from operating in a vacuum.

[Original](https://dev.to/myougatheaxo/4-claudemd-patterns-that-actually-work-in-production-with-full-templates-1mbk) | Added: 2026-02-24

---


## 247. CCK: Automate Claude Context with Context Keeper
**Source:** takawasi (Hackernews)

Use `claude-context-keeper` (CCK) to automate context management for Claude Code. Generate a `CLAUDE.md` file summarizing your project, which Claude reads at the beginning of each session. Use `cck watch --with-history` to inject relevant context into each turn, maintaining a consistent and informed conversation with Claude Code.

[Original](https://news.ycombinator.com/item?id=46435083) | Added: 2026-02-24

---


## 248. Skills: Claude Code's Muscle Memory for Recurring Tasks
**Source:** TK Lin (Devto)

Claude Code forgets past solutions. Use "skills" (markdown files automatically loaded into context) to give it persistent memory. Skills allow Claude to recognize and address recurring problems, like specific bug patterns, without requiring repeated debugging. This creates a more efficient and reliable workflow by leveraging AI's pattern recognition with stored knowledge.

[Original](https://dev.to/stklen/shi-zhan-deduan-eta-112-no-claude-code-skills-he-shi-jian-mokaketabaguxiu-zheng-wo-anatahazao-rifan-sanakuteii-19ei) | Added: 2026-02-25

---


## 249. Skills: Give Claude Code Persistent Memory
**Source:** TK Lin (Devto)

Use Claude Code's 'skills' feature (markdown files that load automatically) to create persistent memories for your AI assistant. Skills record common problems, root causes, fixes, and trigger conditions, allowing Claude Code to automatically apply this knowledge when similar patterns are detected, preventing repetitive debugging.

[Original](https://dev.to/stklen/112-ge-shi-zhan-cui-lian-de-claude-code-skills-mei-ge-rang-wo-cai-keng-shu-xiao-shi-de-bug-xiu-fu-rang-ni-bu-bi-zai-cai-2dcn) | Added: 2026-02-25

---


## 250. Use CLAUDE.md to Brief Claude Code on Your Project
**Source:** myougaTheAxo (Devto)

To ensure Claude Code understands your project's context, conventions, and boundaries, create a CLAUDE.md file in the project root. Claude Code automatically reads this Markdown file at the start of each session, providing it with essential information and preventing it from starting from scratch each time.

[Original](https://dev.to/myougatheaxo/4-claudemd-patterns-that-actually-work-in-production-with-full-templates-1mbk) | Added: 2026-02-25

---


## 254. Claude Code: Auto-Memory for Persistent Context
**Source:** BuildwithVignesh (Reddit)

Claude Code CLI now features auto-memory. Useful context from previous interactions is automatically saved, enabling persistent cross-session memories. You can manage this memory using the `/memory` command to view or edit the automatically saved context. This allows Claude to retain information across different sessions without manual context injection.

[Original](https://www.reddit.com/r/ClaudeAI/comments/1rf6ajn/official_anthropic_just_released_claude_code_2159/) | Added: 2026-02-27

---


## 257. Automate Context with Claude Context Keeper (CCK)
**Source:** takawasi (Hackernews)

Use CCK to automatically generate a CLAUDE.md file that provides context to Claude Code at the start of each session. This eliminates the need to repeatedly explain project details and conventions. Additionally, CCK's 'watch' command can inject relevant history into each turn, improving context retention.

[Original](https://news.ycombinator.com/item?id=46435083) | Added: 2026-03-02

---


## 259. Use CLAUDE.md for Persistent Coding Standards
**Source:** Serenities AI (Devto)

Avoid repetitive instructions and inconsistent code generation by using a CLAUDE.md file. This file allows Claude Code to remember your coding standards, project conventions, and testing preferences across sessions, preventing it from forgetting corrected mistakes and improving overall productivity.

[Original](https://dev.to/serenitiesai/the-complete-guide-to-claudemd-files-for-ai-development-2026-4316) | Added: 2026-03-04

---


## 260. Claude Code: MEMORY.md truncation at 200 lines
**Source:** Jade Soriano (Devto)

Claude Code automatically loads MEMORY.md for context, but truncates it to the first 200 lines. Be aware of this limit when relying on MEMORY.md for large projects, as information beyond this point will be ignored. This impacts your ability to maintain project knowledge effectively.

[Original](https://dev.to/jadessoriano/memorymd-doesnt-scale-heres-what-does-34ic) | Added: 2026-03-04

---


## 262. Use /rules/ for persistent preferences in Claude Code
**Source:** Rick-D-99 (Reddit)

Leverage the `/rules/` directory in Claude Code to enforce consistent behaviors and preferences across all interactions. This is especially useful for ensuring compliance with security standards, mandating specific UI behaviors (like always accepting modal prompts with 'Enter'), and promoting the use of shared asset libraries.  Using `/rules/` prevents the AI from deviating from important guidelines and reduces the need for repeated instructions.

[Original](https://www.reddit.com/r/ClaudeAI/comments/1rkswjs/the_true_secret_to_token_savings/) | Added: 2026-03-05

---


## 264. CCK: Automate Claude Code Context with CLAUDE.md & Injection
**Source:** takawasi (Hackernews)

Use `cck` (Claude Context Keeper) to automate context management for Claude Code sessions. Generate a `CLAUDE.md` file containing project information for Claude to read at the beginning of each session. Employ per-turn context injection with `cck watch --with-history` to automatically include relevant code snippets and conversation history in each prompt, eliminating redundant explanations and improving efficiency.

[Original](https://news.ycombinator.com/item?id=46435083) | Added: 2026-03-06

---


## 265. Use .claudeignore to Reduce Token Usage
**Source:** Boucle (Devto)

The .claudeignore file prevents Claude Code from indexing unnecessary files like build artifacts and dependencies, saving tokens. By excluding these irrelevant files, Claude Code can focus on relevant code, reducing processing costs and improving efficiency. This simple step can significantly lower the cost of running autonomous agent loops.

[Original](https://dev.to/boucle2026/7-ways-to-cut-your-claude-code-token-usage-elb) | Added: 2026-03-07

---


## 271. Context Keeper CLI: Streamline Claude Code Sessions
**Source:** takawasi (Hackernews)

The Context Keeper CLI (cck) automates context management for Claude Code sessions. It generates a CLAUDE.md file summarizing your project structure for initial session ingestion and offers per-turn context injection using `cck watch --with-history` to maintain relevant history.

[Original](https://news.ycombinator.com/item?id=46435083) | Added: 2026-03-08

---


## 272. Prevent Redundant File Reads in Claude Code
**Source:** Boucle2026 (Reddit)

Optimize Claude Code efficiency by implementing a PreToolUse hook called 'read-once'. This hook tracks files read within a session and prevents Claude from re-reading unchanged files, saving significant token costs associated with repetitive file access. This technique addresses the issue of Claude Code re-reading files, potentially saving thousands of tokens in larger projects.

[Original](https://www.reddit.com/r/ClaudeAI/comments/1rnjf5e/i_built_a_claude_code_hook_that_stops_it_from/) | Added: 2026-03-08

---


## 275. Streamline Claude Code Sessions with Context Keeper
**Source:** takawasi (Hackernews)

Use Claude Context Keeper (cck) to automate the creation of a CLAUDE.md file that summarizes your project structure, build commands, and conventions. This eliminates the need to re-explain your project at the start of each Claude Code session.  CCK also offers per-turn context injection using `cck setup --cb-style` and `cck watch --with-history`.

[Original](https://news.ycombinator.com/item?id=46435083) | Added: 2026-03-09

---


## 280. Use CLAUDE.md for Project-Specific Instructions
**Source:** Warhol (Devto)

The `CLAUDE.md` file allows you to provide Claude Code with project-specific context at the start of each session. By placing this markdown file in the project root, you can guide Claude Code's suggestions and ensure it aligns with your project's architecture, patterns, and coding style. This helps to eliminate generic suggestions and incorrect code generation.

[Original](https://dev.to/the200dollarceo/the-claudemd-file-that-made-my-ai-coding-assistant-actually-useful-2dfg) | Added: 2026-03-12

---


## 281. Automated Context Management with cck CLI
**Source:** takawasi (Hackernews)

Use the `cck` CLI to automatically generate a `CLAUDE.md` file summarizing your project structure and conventions for Claude Code. Additionally, `cck watch --with-history` injects relevant context into each turn, streamlining interactions and improving Claude's understanding of your codebase without repetitive explanations.

[Original](https://news.ycombinator.com/item?id=46435083) | Added: 2026-03-12

---


## 283. Customize Claude Code Behavior with CLAUDE.md
**Source:** TAKUYA HIRATA (Devto)

Use a CLAUDE.md file at your project root to configure Claude Code's behavior and coding conventions. This file allows you to override default assumptions Claude Code makes, ensuring it adheres to your project's specific requirements and stylistic preferences during code generation and modification.

[Original](https://dev.to/th19930828/the-complete-guide-to-claudemd-turn-claude-code-into-your-project-custom-ai-5n7) | Added: 2026-03-14

---


## 284. Streamline Claude Code Sessions with CCK (Claude Context Keeper)
**Source:** takawasi (Hackernews)

Use the Claude Context Keeper (CCK) CLI tool to automatically generate a `CLAUDE.md` file summarizing your project structure, commands, and conventions. CCK also offers per-turn context injection, which can be set up with `cck setup --cb-style` and activated with `cck watch --with-history`. This ensures Claude has consistent and comprehensive context across coding sessions.

[Original](https://news.ycombinator.com/item?id=46435083) | Added: 2026-03-15

---


## 286. Automate Claude Code Context with cck CLI
**Source:** takawasi (Hackernews)

The cck CLI tool automates context management for Claude Code sessions by generating a CLAUDE.md file from your codebase and injecting relevant project history into each turn. This eliminates the need to re-explain project details and conventions at the start of each session, and during coding iterations, improving efficiency and consistency.

[Original](https://news.ycombinator.com/item?id=46435083) | Added: 2026-03-16

---


## 287. Exclude lockfiles to reduce token usage in Claude Code
**Source:** Zac (Devto)

Lockfiles like package-lock.json, yarn.lock, and pnpm-lock.yaml can consume significant tokens due to their size and are unnecessary for Claude Code's operation. Excluding these files reduces token usage per turn, saving money without impacting functionality. Add them to your .gitignore or equivalent exclusion mechanism to prevent them from being included as context.

[Original](https://dev.to/builtbyzac/5-things-eating-your-claude-code-tokens-that-arent-your-code-4667) | Added: 2026-03-17

---


## 288. Keep CLAUDE.md Focused for Efficient Context
**Source:** Zac (Devto)

To improve Claude's performance and reduce token usage, maintain concise and focused CLAUDE.md files. Avoid including extensive, irrelevant information like coding conventions or deployment steps. A smaller, more relevant CLAUDE.md ensures Claude can quickly access the necessary context without processing unnecessary tokens, especially during tasks like adjusting UI element spacing.

[Original](https://dev.to/builtbyzac/the-claudemd-routing-pattern-keep-it-minimal-delegate-the-rest-388a) | Added: 2026-03-17

---


## 289. Use .claudeignore to Optimize Claude Code Context
**Source:** Zac (Devto)

Improve Claude Code's performance by using a `.claudeignore` file in your project root. This prevents unnecessary files like build artifacts, lockfiles, and generated code from being loaded into Claude Code's context, freeing up valuable context budget for the files that are most relevant to your task. Ignoring irrelevant files can significantly improve Claude Code's understanding and response quality.

[Original](https://dev.to/builtbyzac/what-to-put-in-claudeignore-and-why-most-people-skip-it-1hdg) | Added: 2026-03-17

---


## 295. CCK: Streamline Claude Code with Automated Context
**Source:** takawasi (Hackernews)

Use Claude Context Keeper (CCK) to automatically generate a CLAUDE.md file describing your project structure, build commands, and conventions. CCK also allows injecting relevant context during each turn of your Claude Code session using `cck setup --cb-style` and `cck watch --with-history`, ensuring Claude always has the necessary information.

[Original](https://news.ycombinator.com/item?id=46435083) | Added: 2026-03-18

---


## 299. CCK: Automate Claude Code context via CLAUDE.md & Watch
**Source:** takawasi (Hackernews)

Use Claude Context Keeper (CCK) to automate context management for Claude Code CLI. Generate a CLAUDE.md file containing project information for Claude to read at the start of a session using `cck sync`. Then, use `cck watch --with-history` to inject relevant code snippets into each turn, enhancing Claude's awareness of your codebase and past interactions.

[Original](https://news.ycombinator.com/item?id=46435083) | Added: 2026-03-19

---


## 301. Shared CLAUDE.md for Team Context
**Source:** Jun Suzuki (Devto)

The Claude Code team uses a shared CLAUDE.md file stored in git. The entire team contributes to this file, providing a central, version-controlled repository of context for Claude Code interactions. This facilitates consistent and collaborative use of the CLI across the team, enabling what they call 'compound engineering'.

[Original](https://dev.to/szkjn/we-outgrew-claudemd-building-a-knowledge-layer-that-compounds-33f) | Added: 2026-03-20

---


## 302. Streamline Claude Code with Persistent Context via CCK
**Source:** takawasi (Hackernews)

Use the `claude-context-keeper` (cck) CLI to maintain context across Claude Code sessions. CCK generates a `CLAUDE.md` file summarizing your project, which Claude can reference at the beginning of each session. Additionally, `cck watch --with-history` enables per-turn context injection, improving code understanding and consistency by injecting previous turns.

[Original](https://news.ycombinator.com/item?id=46435083) | Added: 2026-03-21

---


## 303. CCK: Automate Claude Context with CLAUDE.md and Watch Mode
**Source:** takawasi (Hackernews)

Use Claude Context Keeper (CCK) to automatically generate a CLAUDE.md file containing project context, which Claude can read at the start of a session. Utilize CCK's watch mode to inject relevant files and command history into each turn, enhancing Claude's awareness of the current conversation and codebase.

[Original](https://news.ycombinator.com/item?id=46435083) | Added: 2026-03-23

---


## 311. Optimize CLAUDE.md for reliable instruction
**Source:** Aj (Devto)

Ensure CLAUDE.md instructions are consistently followed by keeping the file under 60 lines to prevent Claude from silently ignoring rules mid-session, respecting Claude's instruction budget of approximately 100-150 slots after its system prompt. This ensures that the most important configurations for the Claude Code CLI are reliably applied throughout the session.

[Original](https://dev.to/ajbuilds/your-claudemd-is-probably-broken-5-silent-failure-patterns-and-how-to-fix-them-1abn) | Added: 2026-03-26

---


## 312. CCK: Automate Claude.md Generation and Context Injection
**Source:** takawasi (Hackernews)

Use Claude Context Keeper (CCK) to automatically generate a CLAUDE.md file summarizing your project for Claude Code, and inject relevant context from past turns into each new prompt. Install with `pip install .`, generate the Claude.md file with `cck sync`, and set up context injection with `cck setup --cb-style` and `cck watch --with-history`.

[Original](https://news.ycombinator.com/item?id=46435083) | Added: 2026-03-26

---


## 316. Understanding the .claude/ Folder
**Source:** Alan West (Devto)

Most Claude Code issues stem from misunderstanding the .claude/ directory. The tip will explain the structure and functionality of this folder, which is crucial for ensuring Claude Code adheres to project-specific conventions and instructions specified in the CLAUDE.md file, improving code generation consistency.

[Original](https://dev.to/alanwest/why-claude-code-ignores-your-instructions-and-how-to-fix-it-1ljp) | Added: 2026-03-29

---


## 318. Use CLAUDE.md for Project Context & Consistency
**Source:** RAXXO Studios (Devto)

To ensure Claude Code generates code that fits your project's style, create a comprehensive CLAUDE.md file. This file should document your tech stack, project structure, naming conventions, and any hard rules. By referencing this file, Claude Code can avoid repetitive explanations, reduce errors, and consistently produce components that align with your project's existing patterns and design systems.

[Original](https://dev.to/raxxostudios/how-to-use-claude-code-for-web-development-complete-guide-4lg2) | Added: 2026-03-29

---


## 319. Automate Claude Code context injection with cck
**Source:** takawasi (Hackernews)

The Claude Context Keeper (cck) CLI tool automates context management for Claude Code sessions. It generates a CLAUDE.md file describing your project and injects relevant history into each turn.  Install cck, sync it to create CLAUDE.md, then use 'cck setup --cb-style' and 'cck watch --with-history' to automatically inject context and history into each Claude Code interaction.

[Original](https://news.ycombinator.com/item?id=46435083) | Added: 2026-03-29

---


## 321. Use CLAUDE.md for Persistent Project Context
**Source:** brian austin (Devto)

Create a CLAUDE.md file in your repository root (or .claude/ folder) to provide Claude Code with persistent project context. This file is automatically read at the start of each session, eliminating the need to repeatedly explain your stack, conventions, and potential issues, leading to more efficient and relevant code suggestions.

[Original](https://dev.to/subprime2010/claudemd-the-project-memory-file-that-makes-claude-code-10x-more-useful-22d6) | Added: 2026-03-30

---


## 325. Streamline Claude Code with Persistent Context
**Source:** takawasi (Hackernews)

Use the 'claude-context-keeper' (cck) CLI to manage and inject context into each Claude Code session. This tool addresses Claude's fresh-start behavior by generating a CLAUDE.md file from your codebase, which Claude reads at the start. Additionally, it supports per-turn context injection using 'cck setup --cb-style' and 'cck watch --with-history', allowing you to maintain context across interactions.

[Original](https://news.ycombinator.com/item?id=46435083) | Added: 2026-03-31

---


## 326. Control Claude Code Token Usage with ARCHITECTURE.md
**Source:** longdo102 (Reddit)

To reduce token consumption when using Claude Code, maintain an `ARCHITECTURE.md` file outlining your project's structure. By feeding this file to Claude, you constrain its exploration, preventing it from freely roaming the codebase and thus saving tokens and reducing the risk of hitting rate limits.

[Original](https://www.reddit.com/r/ClaudeAI/comments/1s8k12v/explore_just_burned_94k_tokens_in_3_minutes_im/) | Added: 2026-04-01

---


## 332. Use .claudeignore to control Claude Code context
**Source:** brian austin (Devto)

Prevent Claude Code from accessing sensitive files and large directories like node_modules by using a `.claudeignore` file. This file acts similarly to a `.gitignore`, allowing you to specify files and directories that Claude Code should exclude from its context, improving efficiency and preventing accidental exposure of sensitive information.

[Original](https://dev.to/subprime2010/claude-code-claudeignore-stop-leaking-secrets-and-nodemodules-into-your-context-54i2) | Added: 2026-04-03

---


## 338. Automate Context Injection with cck
**Source:** takawasi (Hackernews)

Use Claude Context Keeper (cck) to automate the creation of a CLAUDE.md file, ensuring Claude Code has up-to-date project context at the start of each session. Also, set up per-turn context injection with `cck watch --with-history`, allowing Claude Code to access previous conversation history and relevant codebase snippets for more informed code generation and problem-solving.

[Original](https://news.ycombinator.com/item?id=46435083) | Added: 2026-04-04

---


## 344. CCK: Automate Claude Code Context and History
**Source:** takawasi (Hackernews)

The Claude Context Keeper (CCK) CLI tool automates context management for Claude Code sessions. It generates a `CLAUDE.md` file summarizing your codebase for initial Claude Code ingestion, and offers per-turn context injection with command history, improving session continuity and reducing repetitive explanations.

[Original](https://news.ycombinator.com/item?id=46435083) | Added: 2026-04-05

---


## 349. Reduce Claude context size with codesight
**Source:** Eastern_Exercise2637 (Reddit)

Use `npx codesight --wiki` to reduce the number of tokens sent to Claude at the beginning of each session. By summarizing your codebase into a knowledge base, you can drastically reduce the initial context size from 47,450 tokens to a much smaller number, saving on token costs and improving Claude's focus.

[Original](https://www.reddit.com/r/ClaudeAI/comments/1sfdztg/90_fewer_tokens_per_session_by_reading_a/) | Added: 2026-04-09

---


## 350. Use CLAUDE.md for Project Context
**Source:** Seb (Devto)

Create a CLAUDE.md file at the project root to provide Claude Code with essential context. This allows Claude to understand the project structure, dependencies, and coding conventions, leading to more accurate and relevant suggestions. Referencing this file avoids repetitive context pasting.

[Original](https://dev.to/gurkiu/how-i-actually-use-claude-as-a-senior-dev-partner-not-just-a-code-generator-3ii6) | Added: 2026-04-10

---


## 352. CCK: Automate Claude Context for Consistent Sessions
**Source:** takawasi (Hackernews)

Use the Claude Context Keeper (CCK) CLI to automatically generate a CLAUDE.md file describing your project, ensuring Claude Code has consistent context across sessions. CCK's 'sync' command scans your codebase, creating a comprehensive CLAUDE.md that Claude reads at the beginning of each session, eliminating the need for repetitive explanations.

[Original](https://news.ycombinator.com/item?id=46435083) | Added: 2026-04-10

---


## 357. Auditing Claude Code Context Files for Drift
**Source:** Prestigious_Draw6633 (Reddit)

The tip highlights a common problem with Claude Code workflows: context files drifting silently as codebases evolve, leading to inefficient agent behavior. It suggests regularly auditing context files to ensure they accurately reflect the current state of the codebase, thereby improving the agent's ability to perform tasks effectively and avoid redundant tool calls or incorrect inferences.

[Original](https://www.reddit.com/r/ClaudeAI/comments/1skn98k/cleaned_up_my_claudemd_and_my_agent_sessions_got/) | Added: 2026-04-14

---


## 367. Unclog: Trim Claude Code Context Usage
**Source:** tomchill (Hackernews)

The `unclog` tool helps you identify and remove unnecessary files from your Claude Code CLI context (~/.claude) to reduce token usage. It scans your Claude Code directory, displays token counts for each file, and allows selective removal with automatic snapshots for reversibility. Install with `uv tool install unclog` and run with `unclog`.

[Original](https://github.com/thomaschill/unclog) | Added: 2026-04-20

---


## 368. Unclog: Manage Claude Code Context and Reduce Token Usage
**Source:** tomchill (Hackernews)

Use the 'unclog' tool to analyze and selectively remove files from your ~/.claude directory that are consuming excessive tokens. This helps reduce context window size and improve Claude Code performance. The tool creates snapshots for easy reversibility of changes.

[Original](https://github.com/thomaschill/unclog) | Added: 2026-04-20

---


## 370. Unclog: Manage Claude Code Context & Reduce Token Usage
**Source:** tomchill (Hackernews)

Use the `unclog` tool to analyze and reduce token usage in your Claude Code projects. It scans your `~/.claude` directory, identifies context-heavy files like MCPs, skills, and hooks, and allows you to selectively remove them while creating reversible snapshots. Install with `uv tool install unclog` and run with `unclog`.

[Original](https://github.com/thomaschill/unclog) | Added: 2026-04-21

---


## 371. CCK: Automate Claude Code Context with Claude Context Keeper
**Source:** takawasi (Hackernews)

Use Claude Context Keeper (CCK) to automatically generate a CLAUDE.md file summarizing your project's structure and conventions. This ensures Claude Code always has the necessary context at the start of each session. CCK also offers per-turn context injection using `cck watch --with-history` for even deeper contextual awareness.

[Original](https://news.ycombinator.com/item?id=46435083) | Added: 2026-04-23

---

*[Back to Categories](../README.md)*