# 🎭 Orchestration Tips

> Claude as conductor, not worker. 10x parallelization through intelligent delegation.

---

## 1. Git Worktree Orchestration
**Source:** Pushkar Jain

Run an "Orchestrator Agent" on your main branch. Delegate subtasks to other agents running in different Git worktrees on separate branches.

```bash
# Create worktree for feature
git worktree add ../feature-auth feature/auth

# Run Claude in worktree with specific context
cd ../feature-auth && claude
```

**Why it works:** Each agent gets isolated context. No cross-contamination. Merge when ready.

---

## 3. Skill-Based Worktrees
**Source:** Sean T

Define specific "skills" for agents in each worktree. One agent handles backend logic, another handles frontend styling, another handles testing.

```
project/
├── main/           # Orchestrator
├── backend/        # Backend specialist agent
├── frontend/       # Frontend specialist agent
└── testing/        # QA specialist agent
```

---

## 11. Refactor Cycle Pattern
**Source:** Rob Richardson

For refactoring tasks:
1. Give Claude an example `.md` file + target file
2. Complete the refactor
3. Fork/rewind to original prompt
4. Provide different target file
5. Repeat with fresh context each time

---

## 12. Cross-Platform Planning
**Source:** AJ Avanti

Use Claude.ai Projects for planning → Ask for Claude Code prompt → CC creates implementation plan → Send plan back to Claude Chat for review → Implement.

---

## 21. Three-Step Prompt Pattern
**Source:** Elyass Tarik

1. Write prompt
2. Convert to MD with Sonnet
3. Execute with Opus

Higher quality output through prompt refinement.

---

## 24. Rewind Power
**Source:** Alizain Feerasta

Use `/rewind` generously. Breaking out of linear conversation flow helps manage context effectively.

---

## 26. Plugin Workflows
**Source:** Jay W

Use plugins to create static and dynamic subagent workflows without framework dependencies.

---

## 33. Load Distribution
**Source:** jkpelaez

Use `aimaestro23` to coordinate agents and distribute load across multiple accounts/machines.

---

## 35. Competitive Agents
**Source:** EddieBe

Have two agents solve the same problem, then merge the best solutions. Competition drives quality.

---

## 38. Manual Planning Mode
**Source:** anotheryou

Explicit two-phase: "Create detailed MD plan" → Review → "Now implement iteratively, wait for my test after each step."

---



## 57. Reflections of Claude Code from CHANGELOG
**Source:** Oikon (Devto)

I'm Oikon. I typically share Claude Code insights on X (Twitter).

As this eventful year of 2025 draws to a close, I wanted to reflect on Claude Code. For me personally, 2025 was the year AI agents to

[Original](https://dev.to/oikon/reflections-of-claude-code-from-changelog-833) | Added: 2026-01-04

---


## 73. Top 17 Claude Code OSS Tools! Complete Guide to GitHub Open 
**Source:** takuya (Devto)

Hey everyone, Have you tried Claude Code yet? Honestly, I know many of you are tired of hearing "AI writing code." But seriously, once you actually touch it, you realize it's not just a tool—it feels 

[Original](https://dev.to/nakamura_takuya/top-17-claude-code-oss-tools-complete-guide-to-github-open-source-dev-environments-1n0e) | Added: 2026-01-04

---


## 74. CLAUDE.md: Building Persistent Memory for AI Coding Agents
**Source:** Eugene Oleinik (Devto)

AI coding agents have a memory problem. Every new session starts from zero. The agent that spent 20 minutes yesterday figuring out your project's quirky database connection string? Gone. The workaroun

[Original](https://dev.to/evoleinik/claudemd-building-persistent-memory-for-ai-coding-agents-5322) | Added: 2026-01-04

---


## 77. Anthropic Unveils ‘Agent Skills,’ Raising the Stakes in Ente
**Source:** Logic Verse (Devto)

Anthropic has announced the launch of enterprise-grade “Agent Skills,” a new framework designed to make AI agents more capable, reliable, and reusable across business workflows. At the same time, the 

[Original](https://dev.to/logicverse_2025/anthropic-unveils-agent-skills-raising-the-stakes-in-enterprise-ai-30m9) | Added: 2026-01-04

---


## 81. A Guide to Claude Code 2.0 and getting better at using codin
**Source:** Anon84 (Hackernews)


Article URL: https://sankalp.bearblog.dev/my-experience-with-claude-code-20-and-how-to-get-better-at-using-coding-agents/
Comments URL: https://news.ycombinator.com/item?id=46476771
Points: 3
# Comme

[Original](https://sankalp.bearblog.dev/my-experience-with-claude-code-20-and-how-to-get-better-at-using-coding-agents/) | Added: 2026-01-04

---


## 92. I reverse-engineered the workflow that made Manus worth $2B 
**Source:** Signal_Question9074 (Reddit)

      Meta just acquired Manus for $2 billion. I dug into how their agent actually works and open-sourced the core pattern. The problem with AI agents: after many tool calls, they lose track of goals.

[Original](https://www.reddit.com/r/ClaudeAI/comments/1q2p03x/i_reverseengineered_the_workflow_that_made_manus/) | Added: 2026-01-04

---


## 95. Claude Code will ignore your CLAUDE.md if it decides it's no
**Source:** PoorPhipps (Reddit)

Noticed this in a recent blog post by humanlayer here:  ## Claude often ignores CLAUDE.md Regardless of which model you&#39;re using, you may notice that Claude frequently ignores your CLAUDE.md file&

[Original](https://www.reddit.com/r/ClaudeAI/comments/1q34sel/claude_code_will_ignore_your_claudemd_if_it/) | Added: 2026-01-04

---


## 106. Vibe to Prod – Open source full-stack template optimized for
**Source:** muyenlee (Reddit)

Just open-sourced a production-ready full-stack template specifically designed for AI-assisted development with Claude Code. **What it includes:** - Go backend with Chi router - Next.js 14 frontend wi

[Original](https://www.reddit.com/r/ClaudeAI/comments/1q36i9d/vibe_to_prod_open_source_fullstack_template/) | Added: 2026-01-04

---


## 107. Running Multiple AI Coding Agents in Parallel with Full Dev 
**Source:** zxcvbk (Reddit)

      This is how I run multiple Claude Code agents in parallel, each with their own isolated environment (database, frontend, backend). Great for parallelizing feature work or trying multiple approac

[Original](https://www.reddit.com/r/ClaudeAI/comments/1q2zl06/running_multiple_ai_coding_agents_in_parallel/) | Added: 2026-01-04

---


## 114. CC-Flow (subscription wrapper)
**Source:** fourthwaiv (Reddit)

https://github.com/astoreyai/ccflow Production middleware bridging Claude Code CLI with SDK-like Python interfaces. ccflow enables subscription-based usage (Pro/Max) instead of API token billing, with

[Original](https://www.reddit.com/r/ClaudeAI/comments/1q32dv7/ccflow_subscription_wrapper/) | Added: 2026-01-04

---


## 119. How do you fairly benchmark Claude 4.5 Opus across different
**Source:** Most_Remote_4613 (Reddit)

I’d really appreciate it if there’s already a test/benchmark for this (or any existing results someone can share). I’m trying to compare Claude 4.5 Opus across multiple products: Kiro IDE, Claude Code

[Original](https://www.reddit.com/r/ClaudeAI/comments/1q2v0cb/how_do_you_fairly_benchmark_claude_45_opus_across/) | Added: 2026-01-04

---


## 140. Skills and Sub-agents for Scalable Workflows
**Source:** Sandeep Thuthike (Devto)

Claude Code uses Skills (filesystem-based documentation) and Sub-agents (execution engines) as primitives for building scalable workflows. Skills define how work should be done, while Sub-agents execute the work, often in parallel. This combination enables efficient orchestration of complex tasks within the Claude Code environment.

[Original](https://dev.to/sandeep_thuthike/claude-skills-vs-sub-agents-architecture-use-cases-and-effective-patterns-2moa) | Added: 2026-01-09

---

*[Back to Categories](../README.md)*