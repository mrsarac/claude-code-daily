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


## 55. LLM-Council integration with Claude via Model Context Protocol
**Source:** NeitherRun3631 (Reddit)

This tip showcases an integration of Andrej Karpathy's llm-council project with Claude through the Model Context Protocol (MCP). This allows users to perform multi-LLM deliberation directly within Claude Desktop, VS Code, or any MCP-compatible client. Users can trigger the full 3-stage deliberation process (individual responses, peer rankings, synthesis) by prefacing their query with "Use council_query", streamlining complex reasoning tasks within the Claude environment.

[Original](https://www.reddit.com/r/ClaudeAI/comments/1q07mc8/built_an_mcp_server_for_andrej_karpathys_llm/) | Added: 2025-12-31

---


## 69. Troubleshooting Skill Triggering: Tips and Strategies
**Source:** diablodq (Reddit)

The user highlights a common issue where Claude's skills fail to trigger automatically despite providing relevant keywords in the skill descriptions. This suggests a challenge in AI orchestration and highlights the need for strategies to improve skill triggering reliability, perhaps involving more precise keywords, optimized skill descriptions, or a more explicit orchestration framework.

[Original](https://www.reddit.com/r/ClaudeAI/comments/1pzrl6e/how_do_you_get_claude_skills_to_trigger_reliably/) | Added: 2025-12-31

---

*[Back to Categories](../README.md)*