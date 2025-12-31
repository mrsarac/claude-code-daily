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

*[Back to Categories](../README.md)*