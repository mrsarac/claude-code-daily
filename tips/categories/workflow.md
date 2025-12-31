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



## 58. AI Legislation Analysis: TF-IDF Clustering & Co-sponsorship
**Source:** YungBoiSocrates (Reddit)

This tip details a workflow for analyzing AI legislation. It involves pulling bill text and metadata (2019-2024), using TF-IDF to categorize bills by policy area, and analyzing co-sponsorship networks to identify relationships between legislators. The analysis reveals a low passage rate, a post-ChatGPT surge in bills, and a partisan divide in legislative focus, with Democrats emphasizing regulation and privacy.

[Original](https://www.reddit.com/r/ClaudeAI/comments/1q06w2h/given_the_recent_executive_order_by_trump_to/) | Added: 2025-12-31

---


## 59. Automate Admin Tasks with Claude Code: Email, Outreach, Research
**Source:** mikelupu (Reddit)

This prompt explores using Claude Code for automating administrative tasks like email replies, proactive outreach, and web research/tracking. It encourages users to share their automation workflows, especially those triggered automatically or scheduled, to expand the understanding of Claude's non-coding automation capabilities beyond simple summarization.

[Original](https://www.reddit.com/r/ClaudeAI/comments/1q0483v/what_have_you_automated_with_claudeai_besides/) | Added: 2025-12-31

---


## 60. AI-Assisted OSS Maintenance with Claude Code
**Source:** st0012 (Reddit)

This submission describes the user's experience using Claude Code to improve their OSS maintenance and contributions over the past six months. It potentially offers valuable insights into practical applications of AI for streamlining open-source development workflows and could be a useful resource for others looking to leverage AI in this domain.

[Original](https://www.reddit.com/r/ClaudeAI/comments/1q0ffja/ai_and_open_source_a_maintainers_take_end_of_2025/) | Added: 2025-12-31

---


## 67. Direct Prompts vs. Agents: A Trade-off Analysis
**Source:** theelectronicgenius (Reddit)

The provided feedback highlights the trade-offs between using direct prompts and more complex agent-based workflows with Claude. While agents offer potential benefits, direct prompts can sometimes be faster and more effective. Choosing the optimal approach depends on the specific task and desired balance of speed and quality. The user tested various configurations including agents, MCP servers, and parallelism via worktrees.

[Original](https://www.reddit.com/r/ClaudeAI/comments/1pzkuef/pushing_claude_code/) | Added: 2025-12-31

---

*[Back to Categories](../README.md)*
