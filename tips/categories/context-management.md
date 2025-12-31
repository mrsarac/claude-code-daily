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


## 54. Claude uses diagram context, unprompted!
**Source:** BenAttanasio (Reddit)

Claude apparently analyzed a diagram from Nano Banana Pro and incorporated its information into its response without being explicitly prompted to do so. This suggests strong context understanding and proactive use of visual data within the input. The unprompted behavior highlights Claude's ability to leverage information beyond simple keyword recognition.

[Original](https://www.reddit.com/r/ClaudeAI/comments/1q01a4d/opus_45_adorably_selfdeprecates/) | Added: 2025-12-31

---


## 64. Self-Learning Skills for Claude Agents
**Source:** bantler (Reddit)

This tip describes a method for improving Claude agents' efficiency by building self-learning capabilities. It addresses the problem of agents repeatedly guessing at solutions already found in previous runs. The proposed solution involves a 'sidecar memory' that records successful solutions ('Aha moments') and allows for backporting proven knowledge, preventing agents from starting from scratch each time and streamlining the workflow.

[Original](https://www.reddit.com/r/ClaudeAI/comments/1pzong4/letting_agent_skills_learn_from_experience/) | Added: 2025-12-31

---


## 66. Claude's Arithmetic Errors and Prompting for Correction
**Source:** PaulF707 (Reddit)

This highlights a common issue with LLMs: occasional arithmetic errors. The user found that Claude made a mistake in totaling monthly figures. The tip suggests that prompting Claude to explicitly double-check its calculations and confirm the total can help it identify and correct these errors. This underscores the importance of verifying LLM output, especially for numerical tasks, and using prompting to guide the model towards accuracy.

[Original](https://www.reddit.com/r/ClaudeAI/comments/1q05a1j/this_was_a_simple_arithmetic_mistake_on_my_part/) | Added: 2025-12-31

---

*[Back to Categories](../README.md)*