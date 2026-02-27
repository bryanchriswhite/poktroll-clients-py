# poktroll-clients-py


---

# GOTCHA Framework Brief

> Add this to a project's CLAUDE.md to enable the full agent workflow.
> For setup, run: `~/Projects/assistant/tools/gotcha/setup.sh <project-path>`

## Architecture

This project uses the **GOTCHA Framework** — a 6-layer architecture for agentic systems:

| Layer | Purpose | Location |
|-------|---------|----------|
| **Goals** | Process definitions | `goals/` |
| **Orchestration** | AI coordination (you) | — |
| **Tools** | Deterministic scripts | `tools/` |
| **Context** | Reference material | `context/` |
| **Hardprompts** | Instruction templates | `hardprompts/` (symlinked) |
| **Args** | Behavior settings | `args/` |

## Sub-Agent Team

Available via `.claude/agents/` (symlinked from assistant):

| Agent | Role | Access |
|-------|------|--------|
| **implementer** | Write code, create files | Read/Write/Edit/Bash |
| **planner** | Design implementation plans | Read-only + web |
| **researcher** | Investigate codebase | Read-only + web |
| **reviewer** | Review code quality | Read-only + Bash |
| **tester** | Write and run tests | Read/Write/Edit/Bash |
| **validator** | Final quality gate | Read-only + Bash |

## Task Tracking (Beads)

This project uses Beads for task tracking. Core commands:

```bash
bd ready                    # Find available work
bd create --title="..." --type=task --priority=2  # Create task
bd update <id> --status=in_progress               # Claim work
bd close <id> --reason="..."                       # Complete task
bd sync                     # Push to remote at session end
```

**Session close protocol:** Always run `bd sync` before ending a session.

## Shared Resources

- **Hardprompts:** `hardprompts/` — instruction templates (symlinked to assistant)
- **Local overrides:** `hardprompts-local/` — project-specific overrides (first in fallback chain)
- **Project config:** `.gotcha.yaml` — project-specific agent overrides

## Key Rules

1. Check `tools/manifest.md` before writing new scripts
2. Check `goals/manifest.md` before starting tasks
3. Follow existing code patterns — read before writing
4. Use beads to track work — create issues before writing code
