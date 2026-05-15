---
type: source
title: "Deep Dive SKILL.md (Part 1/2)"
article: "raw/Deep Dive SKILL.md (Part 1.2).md"
source_url: "https://abvijaykumar.medium.com/deep-dive-skill-md-part-1-2-09fc9a536996"
author: "[[entities/ab-vijay-kumar|A B Vijay Kumar]]"
published: 2026-03-17
ingested: 2026-05-15
tags: [skill-files, agent-architecture, claude-code, progressive-disclosure, agent-skills-standard]
key_concepts: [skill-files, progressive-disclosure, thin-harness-fat-skills]
---

# Deep Dive SKILL.md (Part 1/2)

Article by [[entities/ab-vijay-kumar|A B Vijay Kumar]] (IBM Fellow, Master Inventor). Part 1 of a 2-part series. Part 2 covers building a SKILL.md from scratch.

Source: [raw/Deep Dive SKILL.md (Part 1.2).md](../raw/Deep%20Dive%20SKILL.md%20(Part%201.2).md)

---

## Overview

A technical deep-dive into the architecture, anatomy, lifecycle, and ecosystem of `SKILL.md` files — the open standard for packaging reusable AI agent expertise. The author argues that SKILL.md is "the most important skill to learn" for AI practitioners, having reached a point where he can do most of his work without writing code at all, only defining skills.

The article covers: the agent architecture layers, the formal frontmatter spec, the progressive disclosure loading mechanism, the 4-phase skill lifecycle, LLM-based routing, security considerations, versioning, testing/debugging, and a comparison with alternative approaches (AGENTS.md, Custom GPTs, fine-tuning, coding-tool-specific instruction files).

---

## Key claims

### Agent architecture layers

Skills operate at the **Identity Layer** — the top of a three-layer stack:

1. **Identity Layer**: personality, expertise, constraints, safety rules. Skills live here.
2. **Orchestration Layer**: Dynamic System Prompt (embeds skill catalog), LLM, Agent Runtime (thought-action loop), Task State.
3. **MCP Layer**: Tool Servers (file ops, API calls, DB queries), MCP Resources (read-access to external data).

The key insight: skills don't touch the MCP layer. They influence model behavior through the system prompt, and the model orchestrates everything else.

### Progressive disclosure — the core design principle

The mechanism that makes large skill collections tractable. See [[concepts/progressive-disclosure]].

- **Level 1 (~100 tokens/skill)**: On startup, only the `name` and `description` from YAML frontmatter are loaded into the system prompt.
- **Level 2 (<5,000 tokens, ideally)**: When a skill is selected as relevant, the full SKILL.md body loads.
- **Level 3 (unlimited)**: On-demand loading of `scripts/`, `references/`, and `assets/` files — only pulled when the instructions reference them.

> "With progressive disclosure, you can have dozens or even hundreds of skills installed, and the overhead is negligible."

### The 4-phase skill lifecycle

1. **Installation**: Drop folder in the right place. No registration, no build. For Claude Code: `~/.claude/skills/` (global) or `.claude/skills/` (project-level). For Claude.ai: upload zip via Settings > Features. For API: reference `skill_id` in container config.
2. **Discovery**: Agent scans skill directories on session start (or on file change — live file watching in Claude Code), reads only YAML frontmatter, builds catalog embedded in system prompt.
3. **Routing**: No algorithmic routing (no embeddings, classifiers, regex, or keyword matching). The skill catalog is formatted into a text block in the prompt and the LLM's forward pass decides which skill applies. LLMs tend to *undertrigger* — simple tasks the model can handle directly often don't invoke a skill. Complex, multi-step, or specialized domain tasks are more reliable triggers.
4. **Execution**: Full SKILL.md loads into context. Agent follows instructions; may selectively load additional files from `scripts/`, `references/`, or `assets/`.

### YAML frontmatter spec

Required fields: `name` (1–64 chars, lowercase letters/numbers/hyphens), `description` (critical: must include positive triggers AND negative boundaries — "Do NOT use for…").

Optional fields:
- `allowed-tools` (experimental): scopes which tools the skill can use (e.g. `Bash(git:*) Bash(jq:*)`)
- `license`: signals provenance and trust
- `metadata`: catch-all key-value map; recommended for `version`, `author`, `last-updated`

The `description` field is the routing signal. It must list specific trigger words, situations, AND explicit negative exclusions. The example given is the built-in `docx` skill, which lists "Word doc," ".docx," formatting elements, tracked changes — and closes with "Do NOT use for PDFs, spreadsheets, Google Docs, or general coding tasks."

### Security considerations

Skills inject instructions into the agent's context window — they shape how the agent thinks. A malicious skill could instruct the agent to exfiltrate data or silently modify code. Mitigations:
- `allowed-tools` field scopes permissions
- `license` field signals provenance
- For enterprises: treat skills like codebase dependencies — review, pin versions, audit changes; prefer project-level over global skills to limit blast radius

> "The best defense is the simplest one: read what you install."

The security model (skill signing, trust levels, sandboxed execution) is described as still evolving as of the article date.

### Versioning

No built-in version field in the required spec. Recommended approach: use `metadata.version` in frontmatter + Git for history, diffs, branching, rollback. Claude Code's live file watching means edits to a SKILL.md take effect on the next interaction within an active session — useful for development, dangerous for production edits during an active task.

### Testing and debugging

- Ask the agent: "Which skill did you use?" — it knows its context.
- Undertriggering fix: enrich the description with more trigger words and synonyms.
- Overtriggering fix: add "Do NOT use for…" boundaries.
- Create a test checklist of 10–15 natural language requests (should-trigger, shouldn't-trigger, ambiguous edge cases). Track triggering accuracy score iteratively.
- Body debugging: add a "Common Gotchas" or "Critical Rules" section to make the implicit explicit.

### Comparison with alternatives

| Approach | Progressive disclosure | Bundled scripts | Filesystem portability | Cross-platform standard |
|---|---|---|---|---|
| SKILL.md | ✓ | ✓ | ✓ | ✓ |
| AGENTS.md | ✗ (always-on) | ✗ | ✓ | ✓ |
| Custom GPTs | ✗ | ✗ | ✗ | ✗ |
| Fine-tuning | ✗ | ✗ | ✗ | ✗ |
| Code frameworks | ✗ | ✓ | ✗ | ✗ |

AGENTS.md vs. SKILL.md distinction: AGENTS.md is always loaded and tells the agent "here's how we do things around here." SKILL.md is on-demand and tells the agent "here's how to do this specific task." They're complementary.

Historical context: before SKILL.md standardization, every tool had its own format (`.cursor/rules/`, `.github/copilot-instructions.md`, `CLAUDE.md`, `.windsurfrules`, `JULES.md`). Teams resorted to symlinking files or CLI tools like `rule-porter` to convert between formats.

### Standardization and adoption

[[entities/anthropic|Anthropic]] published the Agent Skills specification at agentskills.io, Apache 2.0 (code) / CC-BY-4.0 (docs). Within days: Microsoft integrated into VS Code and GitHub Copilot; OpenAI adopted in Codex CLI and ChatGPT. Cursor, Amp, Goose, OpenCode, Letta followed. Vercel launched skills.sh.

By March 2026: the [Antigravity Awesome Skills library](https://github.com/sickn33/antigravity-awesome-skills) catalogued 1,234+ skills compatible with 16+ agents. Microsoft built an Agent Framework SDK (Python, C#, TypeScript) with a `SkillsProvider` class.

---

## Evidence and data quality

- Author is an IBM Fellow and Master Inventor with hands-on experience building skills
- Cites Anthropic's official Agent Skills specification and engineering blog
- Some forward-looking claims about adoption (March 2026 numbers) are presented as current fact — consistent with article date of March 2026
- Images referenced but not reproduced here (architecture diagrams, comparison tables)

---

## Implications

1. The SKILL.md format is now a genuine cross-platform standard — a skill written today works across all major AI coding tools.
2. Description engineering is the primary lever for skill quality — positive triggers AND negative exclusions both matter.
3. [[concepts/progressive-disclosure]] is the architectural mechanism that makes skill scalability possible; understanding it is key to building large skill libraries.
4. LLM-based routing is inherently probabilistic and tends to undertrigger — skill authors must compensate through description design and testing.
5. The security model for skills is immature — treating skills like code dependencies is the pragmatic defense.

---

## Key quotes

> "I am slowly starting to believe in `SKILL.md` will be the most important skill, I need to learn."

> "Skills operate at the highest level of the stack. They don't touch the MCP layer directly, they don't manage tool connections, and they don't handle state. They influence the model's behavior through the system prompt, and the model orchestrates everything else."

> "At the code level, there's no algorithmic routing. Claude Code doesn't use embeddings, classifiers, regex, keyword matching, or ML-based intent detection to decide which skill to invoke."

> "The best defense is the simplest one: read what you install."

---

## Related pages

- [[concepts/skill-files]] — core concept; significantly updated from this source
- [[concepts/progressive-disclosure]] — new concept; the 3-level loading mechanism
- [[concepts/thin-harness-fat-skills]] — complementary architecture principle
- [[concepts/resolvers]] — Tan's framing of skill routing
- [[entities/ab-vijay-kumar]] — author
- [[entities/anthropic]] — published the open spec
