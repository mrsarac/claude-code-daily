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

*[Back to Categories](../README.md)*