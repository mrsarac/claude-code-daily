# ⚡ Workflow Tips

> Planning ≠ Implementation. Reliable outputs through separation.

---

## 2. The Full Automation Loop
**Source:** Ibrahim Hammad

The ultimate Claude Code workflow:

1. **Plan** with OpenSpec → create concrete specification
2. **New session** → fresh context
3. **Claude Code** → implement
4. **Codex MCP** → review
5. **Claude** → fix issues
6. **Repeat** until aligned

---

## 10. Cost Optimization Through Model Switching
**Source:** antfx

Three-phase approach:
1. **Claude CLI** → Research and create `FEATURE_plan.md`
2. **Cheaper model** (e.g., GPT-4 Mini, GLM) → Implement the plan
3. **Claude** → Polish and finalize

Reduces token costs by **60-70%** while maintaining quality.

---

## 22. Junior Dev Simulation
**Source:** Vince

Complete a task, copy the logic, run `/clear`. Start new session with:
> "A junior dev wrote this. Review and improve."

Forces Claude into critical evaluation mode.

---

## 23. Custom System Prompts
**Source:** Mng

Claude Code isn't just for coding. With custom system prompts in CLAUDE.md, transform it into any specialized agent.

---

## 25. Manual Iteration on Plans
**Source:** Aaron Yang

Before implementing, manually iterate on the `.md` plan file. This builds team memory and catches issues early.

---

## 27. Skill-Focused Loading
**Source:** Hakan Deryal

Create commands like `/backend`, `/frontend` that load only relevant files into context.

```markdown
<!-- .claude/commands/backend.md -->
Focus on backend files only:
- server/
- api/
- database/
Ignore frontend, tests, and documentation.
```

---

## 28. Sanitizer Hooks
**Source:** Dmytro Palaniichuk

Use hooks to compress and sanitize input data before it reaches Claude. Context savings add up.

---

## 29. Research & Plan Commands
**Source:** Daniel

Two-command workflow:
1. `/research_codebase` → `research.md`
2. `/create_plan` → `plan.md`

---

## 30. Mandate Files
**Source:** Tobias Bentzer

Create comprehensive "Mandate" files that persist across multiple sessions. Your project's constitution.

---

## 46. The Golden Rule
**Source:** pjay

> **Never do planning and implementation in the same session.**

Plan → New Session → Implement → Bridge. This rule alone prevents 80% of quality issues.

---




## 54. Using Claude Code to solve Advent of Code 2025
**Source:** Dinesh Kumar Gnanasekaran (Devto)


  
  
  Introduction


Let's be honest: with LLMs, the fun of Advent of Code is gone. You can paste any puzzle into ChatGPT or Claude and get a working solution in seconds. So I did it anyway, but to

[Original](https://dev.to/dineshgdk/using-claude-code-to-solve-advent-of-code-2025-2o16) | Added: 2026-01-04

---


## 56. [Boost]
**Source:** Panayiotis Tzagkarakis (Devto)


  
    
      
    
  
  
    
      Oh My Posh ❤️ Claude Code
      Jan De Dobbeleer ・ Dec 28
      
        #claude
        #ai
        #terminal
        #prompt
      
    
  





[Original](https://dev.to/ptzagk/-5bch) | Added: 2026-01-04

---


## 61. Enterprise-Ready AI Workflows: Formatted Reports + 80% Cost 
**Source:** Patrick Roebuck (Devto)

Just shipped v3.3.0 of Empathy Framework with features I wish existed when I was running AI at scale:



Formatted reports for every workflow (finally, readable output)

Cost guardrails so your doc-ge

[Original](https://dev.to/silversurfer562/enterprise-ready-ai-workflows-formatted-reports-80-cost-savings-5hc2) | Added: 2026-01-04

---


## 62. How I Built a Documentation-Driven Development Workflow with
**Source:** Huy Pham (Devto)

Ever had a PM write requirements in Slack, a developer interpret them differently, and QA test against something else entirely? I got tired of this chaos, so I built a workflow that makes documentatio

[Original](https://dev.to/quochuydev/how-i-built-a-documentation-driven-development-workflow-with-claude-code-1cbb) | Added: 2026-01-04

---


## 63. Claude Code in Production: 40% Productivity Increase on a La
**Source:** Dzianis Karviha (Devto)


  
  
  Introduction


Over the past 4 months since August 2025, I've been actively integrating Claude Code into my development workflow. After this period of experimentation and practice, I believe 

[Original](https://dev.to/dzianiskarviha/integrating-claude-code-into-production-workflows-lbn) | Added: 2026-01-04

---


## 64. Claude Coding A Blog Pipeline
**Source:** chrismo (Devto)

Lately, I've been working on trying to get a blog publishing pipeline up and running for all the various things I've been working on this past year. If you're reading this, then some part of it is at 

[Original](https://dev.to/chrismo/claude-coding-a-blog-pipeline-3e4f) | Added: 2026-01-04

---


## 65. Universal Knowledge Base for AI
**Source:** Alfredo Perez (Devto)

Okay, tell me if this sounds familiar: You're working on a new project and need to add a page, but suddenly you don't know what patterns to follow. You check the closest page to see how it's structure

[Original](https://dev.to/alfredoperez/universal-knowledge-base-for-ai-432g) | Added: 2026-01-04

---


## 66. The Ultimate Claude Code Tips Collection (Advent of Claude 2
**Source:** Damien Gallagher (Devto)


  
  
  The Ultimate Claude Code Tips Collection (Advent of Claude 2025)



Full Credit: This article is a summary of Ado's fantastic "Advent of Claude" series, where he shared daily Claude Code tips

[Original](https://dev.to/damogallagher/the-ultimate-claude-code-tips-collection-advent-of-claude-2025-5b73) | Added: 2026-01-04

---


## 67. Create Reliable Unit Tests with Claude Code
**Source:** Alfredo Perez (Devto)

So you're using Claude Code to generate tests and it's creating 45 test files that check if setTimeout works. Yeah, that's not what we want. And that's in the best-case scenario.

In the worst case? T

[Original](https://dev.to/alfredoperez/create-reliable-unit-tests-with-claude-code-4e8p) | Added: 2026-01-04

---


## 68. Using the VSCode Claude Code Extension with Bedrock and Clau
**Source:** Matt Bacchi (Devto)

Lots of folks use the Claude IDE, or the Claude Code VSCode extension. Unfortunately, your prompts and completions are used (by default) to train Claude models. [0]

AWS Bedrock, on the other hand, do

[Original](https://dev.to/aws-builders/using-the-vscode-claude-code-extension-with-bedrock-and-claude-sonnet-45-2d69) | Added: 2026-01-04

---


## 70. Debugging Random Reboots with Claude Code: A PSU Power Limit
**Source:** Eugene Oleinik (Devto)

My Linux server started rebooting randomly during CPU benchmarks. I had no idea where to start, so I asked Claude Code to help diagnose. Twenty minutes later, we found the root cause and a working fix

[Original](https://dev.to/evoleinik/debugging-random-reboots-with-claude-code-a-psu-power-limit-story-ai7) | Added: 2026-01-04

---


## 71. Reverse-engineering undocumented APIs with Claude
**Source:** Kalil (Devto)



🔗 Project: https://github.com/kalil0321/reverse-api-engineer

Many websites expose public APIs, but they’re often undocumented, poorly documented, or intentionally hard to find.

I’m currently build

[Original](https://dev.to/kalil0321/reverse-engineering-undocumented-apis-with-claude-1l33) | Added: 2026-01-04

---


## 75. The $1 Takeover: How the U.S. Government "Nationalized" Anth
**Source:** Om Shree (Devto)

In late 2025, a series of rapid-fire announcements from the Department of Energy (DOE) and Department of Defense (DOD) signaled a paradigm shift in American industrial policy. The "Genesis Mission" is

[Original](https://dev.to/om_shree_0709/the-1-takeover-how-the-us-government-nationalized-anthropic-3pp6) | Added: 2026-01-04

---


## 78. Intégration IA d'entreprise: accélérer l'adoption avec le pa
**Source:** Camille Vingere (Devto)

Intégration IA d'entreprise devient un impératif stratégique pour toute organisation qui veut gagner en efficacité et innover rapidement. Avec des partenariats comme Accenture–Anthropic, les entrepris

[Original](https://dev.to/camille_vingere_f1a536f90/integration-ia-dentreprise-accelerer-ladoption-avec-le-partenariat-accenture-anthropic-3ka7) | Added: 2026-01-04

---


## 79. Google engineer says Claude Code built in one hour what her 
**Source:** ksec (Hackernews)


Article URL: https://the-decoder.com/google-engineer-says-claude-code-built-in-one-hour-what-her-team-spent-a-year-on/
Comments URL: https://news.ycombinator.com/item?id=46477966
Points: 45
# Comment

[Original](https://the-decoder.com/google-engineer-says-claude-code-built-in-one-hour-what-her-team-spent-a-year-on/) | Added: 2026-01-04

---


## 82. How Boris Cherny (Creator of Claude Code) Uses Claude Code
**Source:** cocoflunchy (Hackernews)


Article URL: https://threadreaderapp.com/thread/2007179832300581177.html
Comments URL: https://news.ycombinator.com/item?id=46473778
Points: 5
# Comments: 0


[Original](https://threadreaderapp.com/thread/2007179832300581177.html) | Added: 2026-01-04

---


## 83. bcherny's Claude Code Setup
**Source:** doppp (Hackernews)


Article URL: https://twitter.com/i/status/2007179832300581177
Comments URL: https://news.ycombinator.com/item?id=46472311
Points: 5
# Comments: 1


[Original](https://twitter.com/i/status/2007179832300581177) | Added: 2026-01-04

---


## 84. The creator of Claude Code's Claude setup
**Source:** KothuRoti (Hackernews)


Article URL: https://twitter.com/bcherny/status/2007179832300581177
Comments URL: https://news.ycombinator.com/item?id=46470017
Points: 3
# Comments: 0


[Original](https://twitter.com/bcherny/status/2007179832300581177) | Added: 2026-01-04

---


## 86. From Zero to Rain: A Claude Code Case Study
**Source:** pj4533 (Hackernews)


Article URL: https://pj4533.com/sigh/
Comments URL: https://news.ycombinator.com/item?id=46455311
Points: 3
# Comments: 1


[Original](https://pj4533.com/sigh/) | Added: 2026-01-04

---


## 88. I Built and Shipped Dognames.vip in 24 Hours with ClaudeCode
**Source:** yeeyang (Hackernews)


Hi everyone,I'm a product manager. And as a non-coding PM, the idea of building an app from scratch by myself used to be a distant dream. But by collaborating with ClaudeCode, I was able to build and

[Original](https://news.ycombinator.com/item?id=44570584) | Added: 2026-01-04

---


## 89. Show HN: Claudecode.nvim – Bringing Claude to Neovim (+how t
**Source:** ThomasK33 (Hackernews)


Article URL: https://github.com/coder/claudecode.nvim
Comments URL: https://news.ycombinator.com/item?id=44161674
Points: 4
# Comments: 0


[Original](https://github.com/coder/claudecode.nvim) | Added: 2026-01-04

---


## 90. Usage Limits, Bugs and Performance Discussion Megathread - b
**Source:** sixbillionthsheep (Reddit)

Why a Performance, Usage Limits and Bugs Discussion Megathread? This Megathread makes it easier for everyone to see what others are experiencing at any time by collecting all experiences. Importantly,

[Original](https://www.reddit.com/r/ClaudeAI/comments/1pygdbz/usage_limits_bugs_and_performance_discussion/) | Added: 2026-01-04

---


## 91. Claude in Chrome expanded to all paid plans with Claude Code
**Source:** ClaudeOfficial (Reddit)

      Claude in Chrome is now available to all paid plans. It runs in a side panel that stays open as you browse, working with your existing logins and bookmarks. We’ve also shipped an integration wit

[Original](https://www.reddit.com/r/ClaudeAI/comments/1pq199v/claude_in_chrome_expanded_to_all_paid_plans_with/) | Added: 2026-01-04

---


## 93. Claude Code creator Boris shares his setup with 13 detailed 
**Source:** BuildwithVignesh (Reddit)

      I&#39;m Boris and I created Claude Code. Lots of people have asked how I use Claude Code, so I wanted to show off my setup a bit. My setup might be surprisingly vanilla. Claude Code works great 

[Original](https://www.reddit.com/r/ClaudeAI/comments/1q2c0ne/claude_code_creator_boris_shares_his_setup_with/) | Added: 2026-01-04

---


## 99. Claude Code vs Cursor for Non Technical User
**Source:** pellegrinoking (Reddit)

This might sound like a newb question so forgive me. I am 0% technical (I can code python at a 3rd grade level that&#39;s about it).  I have built a ton of cool stuff using Cursor (for example built r

[Original](https://www.reddit.com/r/ClaudeAI/comments/1q39t9b/claude_code_vs_cursor_for_non_technical_user/) | Added: 2026-01-04

---


## 100. I made a free VS Code extension to extract file paths for Cl
**Source:** quake2005 (Reddit)

I built a small VS Code extension that solves an annoying workflow problem when using Claude Code. The Problem: When you want Claude to analyze multiple files, you have to manually type out each @/pat

[Original](https://www.reddit.com/r/ClaudeAI/comments/1q38hx0/i_made_a_free_vs_code_extension_to_extract_file/) | Added: 2026-01-04

---


## 102. TIL Claude Code can speak to you when it needs help!
**Source:** anirishafrican (Reddit)

The pain here is sometimes you are running multiple terminals and you don&#39;t want to dangerously skip permissions. You can lose so much time being unaware that a tab needs your permission to contin

[Original](https://www.reddit.com/r/ClaudeAI/comments/1q2fhco/til_claude_code_can_speak_to_you_when_it_needs/) | Added: 2026-01-04

---


## 108. Want to learn how to make the most of Claude Code? Check out
**Source:** luongnv-com (Reddit)

      Want to learn how to make the most out of Claude Code - check this course release by Anthropic - 15 lectures - 1h video - 1 quiz - certificate Link: https://anthropic.skilljar.com/claude-code-in

[Original](https://www.reddit.com/r/ClaudeAI/comments/1q1z5ke/want_to_learn_how_to_make_the_most_of_claude_code/) | Added: 2026-01-04

---


## 110. Whats your way of learning w/ Claude?
**Source:** vignesh-aithal (Reddit)

I am a coder, and I know how to use Claude for coding and I am good at it. But, I am very poor at learning w/ Claude. I just say tech me this. But, it fails to tell explain me clearly all the things, 

[Original](https://www.reddit.com/r/ClaudeAI/comments/1q2vkxl/whats_your_way_of_learning_w_claude/) | Added: 2026-01-04

---


## 111. Intuitive interface by Opus 4.5
**Source:** rasheed106 (Reddit)

Hello All, Been working hard with Opus 4.5 on making the most intuitive interface for Fintech users.  I&#39;ve found that giving blanket commands via Cursor mostly doesn&#39;t work if you don&#39;t ha

[Original](https://www.reddit.com/r/ClaudeAI/comments/1q34cmy/intuitive_interface_by_opus_45/) | Added: 2026-01-04

---


## 113. My experience using Claude Code to build a full marketing si
**Source:** noveltysystems (Reddit)

I&#39;ve spent 20 years in marketing, and I can write code, but hadn&#39;t built a full site myself in a while. Needed a new one fast after walking away from a business I&#39;d spent two years buildin

[Original](https://www.reddit.com/r/ClaudeAI/comments/1q2pgnd/my_experience_using_claude_code_to_build_a_full/) | Added: 2026-01-04

---


## 116. Language learning with Claude?
**Source:** keftes (Reddit)

Hey everyone, I’m curious if anyone here has experimented with using Claude or Claude Code to teach themselves a foreign language. I’m specifically looking to learn basic Spanish for day-to-day intera

[Original](https://www.reddit.com/r/ClaudeAI/comments/1q2w5mh/language_learning_with_claude/) | Added: 2026-01-04

---


## 117. Custom slash command refusing to use MCP, how to fix?
**Source:** Fraysa (Reddit)

Hi everyone. I installed mcp-atlassian and configured it correctly - I can run `claude mcp list` and see that its conected. I created a custom slash command /investigate_jira to get issues about a JIR

[Original](https://www.reddit.com/r/ClaudeAI/comments/1q31xlm/custom_slash_command_refusing_to_use_mcp_how_to/) | Added: 2026-01-04

---


## 118. Built a pay-per-use Claude API - no account needed, pay with
**Source:** hot4botz (Reddit)

I built LightningProx, which is a way to access Claude without needing to manage API keys or an Anthropic account. Here’s the basic idea: you send a prompt to the API, it returns a small Lightning inv

[Original](https://www.reddit.com/r/ClaudeAI/comments/1q36xjw/built_a_payperuse_claude_api_no_account_needed/) | Added: 2026-01-04

---


## 120. Thanks Claude Opus for assisting me in saving a squirrel's l
**Source:** BiscuitShelter (Reddit)

      A squirrel we call Foxy was suffering really bad from mange in the middle of winter. I really wanted to figure out how to help her out, so I tried searching in the usual spots. A bunch of posts 

[Original](https://www.reddit.com/r/ClaudeAI/comments/1q2borj/thanks_claude_opus_for_assisting_me_in_saving_a/) | Added: 2026-01-04

---


## 122. Essential Claude Code CLI Commands for Beginners
**Source:** Ege Pakten (Devto)

This guide introduces essential Claude Code CLI commands like `/help`, `/add`, `/ls`, `/clear`, `/code`, and `/architect` to help beginners quickly understand and utilize the tool. These commands are fundamental for managing context, generating code, and planning projects within the Claude Code environment, enabling a streamlined development workflow.

[Original](https://dev.to/egepakten/claude-code-in-terminal-a-beginners-guide-to-10x-faster-development-3196) | Added: 2026-01-04

---


## 127. Mastering Claude Code CLI Commands
**Source:** Ege Pakten (Devto)

This guide provides a practical overview of essential Claude Code CLI commands like `/help`, `/add`, `/ls`, `/clear`, `/code`, and `/architect`. It focuses on using these commands to effectively manage context, write/edit code, and plan architectures directly within the terminal, streamlining your development workflow.

[Original](https://dev.to/egepakten/claude-code-in-terminal-a-beginners-guide-to-10x-faster-development-3196) | Added: 2026-01-05

---


## 131. Beginner's Guide to Claude Code CLI Commands
**Source:** Ege Pakten (Devto)

This guide introduces Claude Code CLI with a focus on essential commands like `/help`, `/add`, `/ls`, `/clear`, `/code`, and `/architect`. It helps new users understand how to interact with Claude Code through the terminal, manage context, write and edit code, and plan software architecture.

[Original](https://dev.to/egepakten/claude-code-in-terminal-a-beginners-guide-to-10x-faster-development-3196) | Added: 2026-01-06

---


## 133. Mastering Claude Code CLI: A Beginner's Guide
**Source:** Ege Pakten (Devto)

This guide provides a practical introduction to Claude Code CLI for beginners, focusing on essential commands like `/help`, `/add`, `/ls`, `/clear`, `/code`, and `/architect`. It outlines how to use these commands to effectively manage context, generate code, and plan software architecture directly from the terminal, supercharging the development workflow.

[Original](https://dev.to/egepakten/claude-code-in-terminal-a-beginners-guide-to-10x-faster-development-3196) | Added: 2026-01-07

---


## 141. Hot-reload Skills for faster iteration
**Source:** mDarken (Reddit)

Claude Code now supports automatic hot-reloading of skills. When you create or modify skills in the `~/.claude/skills` or `.claude/skills` directories, the changes are immediately available without requiring a restart of your Claude Code session. This feature speeds up the development and testing process by allowing you to quickly iterate on your skills.

[Original](https://www.reddit.com/r/ClaudeAI/comments/1q6q9my/claudecode_v210_just_dropped/) | Added: 2026-01-09

---


## 157. Structured Workflow with /plan, /execute, /verify, /ship
**Source:** milkphetamine (Reddit)

Automate code development workflows in Claude Code with a structured approach. The plugin enforces a sequence of /plan, /execute, /verify, and /ship commands. Progress is gated, preventing skipping steps. You cannot execute without a plan, verify without execution, or ship without verification, ensuring quality control at each stage.

[Original](https://www.reddit.com/r/ClaudeAI/comments/1qfigbs/claudikins_kernel_based_exactly_on_boris_chernys/) | Added: 2026-01-18

---


## 158. Faster Claude Code Execution with Auto-Paste
**Source:** coygeek (Reddit)

The new 'Yes, clear context and bypass permissions' option in Claude Code's plan mode enables faster plan execution. Selecting this option copies the plan to your clipboard, clears the current session, auto-pastes the plan, and immediately begins coding, streamlining the workflow.

[Original](https://www.reddit.com/r/ClaudeAI/comments/1qf91g4/clear_context_new_option_when_plan_finishes/) | Added: 2026-01-18

---


## 159. Control Claude Code with PreToolUse Hooks
**Source:** Mike Lane (Devto)

Use Claude Code's PreToolUse hook system to intercept tool calls, enforce project rules, and inject contextual guidance. This allows you to prevent dangerous operations like 'git reset --hard' and ensure compliance with team standards like GPG-signed commits or using the correct GitHub organization. Implement custom hooks to customize Claude Code's behavior and align it with your specific project requirements.

[Original](https://dev.to/mikelane/building-guardrails-for-ai-coding-assistants-a-pretooluse-hook-system-for-claude-code-ilj) | Added: 2026-01-19

---

*[Back to Categories](../README.md)*
