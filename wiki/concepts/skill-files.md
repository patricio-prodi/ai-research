---
type: concept
title: "Skill Files"
aliases: [skills, skill file, slash commands, agent skills, SKILL.md]
sources: [garrytan-thin-harness-fat-skills, vijaykumar-skill-md-deep-dive]
related_concepts: [thin-harness-fat-skills, resolvers, latent-vs-deterministic, diarization, llm-wiki, progressive-disclosure]
related_entities: [garry-tan, anthropic, ab-vijay-kumar]
last_updated: 2026-05-15
---

# Skill Files

Reusable markdown documents that teach an AI agent *how* to do something — encoding process, judgment, and domain knowledge as a procedure the model can execute. A core component of the [[concepts/thin-harness-fat-skills|thin harness, fat skills]] architecture.

Introduced as a formal concept by [[entities/garry-tan|Garry Tan]] in [[sources/garrytan-thin-harness-fat-skills]].

## What a skill file is

A skill file:
- Defines a **procedure** (steps, criteria, judgment calls) — not a goal
- Takes **parameters** (invocation supplies the world; the skill supplies the process)
- Is written in **markdown** — the language models already think in
- Acts like a **method call**: same skill, different arguments, radically different behavior

> "A skill file works like a method call. It takes parameters. You invoke it with different arguments. The same procedure produces radically different capabilities depending on what you pass in." — Tan

This is explicitly **not prompt engineering**. It is software design using markdown as the programming language and human judgment as the runtime.

## Example: /investigate

A single `/investigate` skill with seven steps (scope dataset → build timeline → diarize documents → synthesize → argue both sides → cite sources) and three parameters: `TARGET`, `QUESTION`, `DATASET`.

- Point at a safety scientist + 2.1M discovery emails → medical research analyst determining whether a whistleblower was silenced
- Point at a shell company + FEC filings → forensic investigator tracing coordinated campaign donations

Same skill file. Same seven steps. Completely different capability.

## Example: /match-* (three invocations of one skill)

From Tan's YC Startup School case (6,000 founders):
- `/match-breakout`: 1,200 founders, cluster by sector affinity, 30 per room — embedding + deterministic assignment
- `/match-lunch`: 600 founders, serendipity matching across sectors, 8 per table, no repeats — LLM invents themes, deterministic algorithm assigns seats
- `/match-live`: whoever is in the building now, nearest-neighbor embedding, 200ms, 1:1 pairs excluding prior meetings

Same matching skill, three invocations, three strategies.

## Why markdown beats code for skills

1. **Process and judgment in natural language**: Models execute markdown procedures better than rigid code because the instructions are expressed in the language they reason in.
2. **Contextual adaptability**: A markdown procedure can include conditional reasoning ("if X, then consider Y") that a function signature cannot.
3. **Self-modification**: Skills can be updated by the model itself as part of a learning loop (see [[concepts/diarization]] and the /improve pattern).

## The permanence property

Unlike code that must be maintained as APIs change, a well-written skill encodes **judgment** that remains valid across model upgrades. When a better model is deployed, every latent step in every skill automatically improves. Skills never degrade, never forget, and run unsupervised.

## The self-improvement loop

Tan's instruction to his own agent:
> "You are not allowed to do one-off work. If I ask you to do something and it's the kind of thing that will need to happen again, you must: do it manually the first time on 3–10 items. Show me the output. If I approve, codify it into a skill file. If it should run automatically, put it on a cron. The test: if I have to ask you for something twice, you failed."

A skill's `/improve` variant can read NPS surveys, diarize mediocre responses, extract patterns, and rewrite matching rules back into the skill. In the YC example: 12% "OK" ratings → 4% after one learning cycle.

## Relationship to this vault

The procedures in this vault's `CLAUDE.md` (INGEST, QUERY, LINT operations) are informal skill files — markdown-encoded procedures the LLM executes to maintain the wiki. The `CLAUDE.md` acts as both harness configuration and skill library.

## Formal specification (Agent Skills open standard)

[[entities/anthropic|Anthropic]] published the Agent Skills specification at agentskills.io (Apache 2.0 / CC-BY-4.0), which became an industry standard in weeks. Details from [[sources/vijaykumar-skill-md-deep-dive]].

### Skill directory structure

```
skill-name/
├── SKILL.md                 ← Required (frontmatter + body)
├── scripts/                 ← Optional: .py, .sh, .js executables
├── references/              ← Optional: detailed docs, domain guides, API references
└── assets/                  ← Optional: templates, config files, lookup tables
```

### YAML frontmatter fields

- `name` — required; 1–64 chars, lowercase letters/numbers/hyphens
- `description` — required; the routing signal. Must include **positive triggers** (trigger words, situations) AND **negative exclusions** ("Do NOT use for…"). This is the only thing the LLM sees when making routing decisions.
- `allowed-tools` — experimental; scopes which tools the skill may use (e.g. `Bash(git:*) Read`)
- `license` — signals provenance and trust; Anthropic-published skills use `Proprietary. LICENSE.txt has complete terms`
- `metadata` — optional catch-all map; recommended for `version`, `author`, `last-updated`

### The description field is the most important part of a skill

Because [[concepts/progressive-disclosure|progressive disclosure]] means the LLM only sees Level 1 metadata when routing, the `description` field must do all the work. Key engineering principles:
- List specific trigger words and situations (not just a generic summary)
- Draw negative boundaries explicitly ("Do NOT use for X, Y, Z")
- Add synonyms for undertriggered skills (if users say "Docker" but the description says "containerized deployments," it may not trigger)
- Overtriggering fix: strengthen the negative exclusions

## Skill lifecycle (4 phases)

1. **Installation** — drop folder in place, no registration needed. Paths: `~/.claude/skills/` (global), `.claude/skills/` (project), zip upload for Claude.ai, `skill_id` in API container config.
2. **Discovery** — agent scans directories on startup and on file change (Claude Code uses live file watching); builds a catalog of name+description pairs embedded into the system prompt.
3. **Routing** — no algorithmic routing (no embeddings, classifiers, regex). The LLM reads the user request against the skill catalog and decides. Tendency: LLMs *undertrigger* — they don't invoke a skill when they believe they can handle the task directly. Complex, multi-step, specialized tasks are more reliable triggers.
4. **Execution** — full SKILL.md body loads into context; agent may selectively load scripts, references, or assets as needed.

## Security considerations

Skills inject instructions directly into the agent's context window. A malicious skill can shape how the agent behaves — including exfiltrating data or silently modifying code. Practical guidelines:
- Read a skill's SKILL.md before installing it (it's a text file)
- Prefer skills from known repositories (e.g. github.com/anthropics/skills)
- Use `allowed-tools` to scope permissions where available
- Be cautious with skills that include executable scripts
- Use project-level skills (`.claude/skills/`) over global (`~/.claude/skills/`) to limit blast radius
- Treat skills like codebase dependencies: review, pin versions, audit changes

The security model (skill signing, trust levels, sandboxed execution) is described as still evolving as of March 2026.

## Versioning

No built-in version field in the required spec. Best practice: use `metadata.version` in frontmatter + Git. Skills can be version-controlled alongside project code in `.claude/skills/`. Claude Code's live file watching means edits take effect on the next interaction — useful during development, risky during production tasks.

## Testing and debugging

- Ask the agent: "Which skill did you use?" — it knows its context.
- Undertriggering: add more trigger words and synonyms to the description.
- Overtriggering: add or strengthen "Do NOT use for…" boundaries.
- Create a test checklist of 10–15 natural language requests (should-trigger, shouldn't-trigger, ambiguous). Track triggering accuracy iteratively.
- Body quality: add "Common Gotchas" or "Critical Rules" sections to make the implicit explicit.

## Standardization and ecosystem (as of March 2026)

The open standard at agentskills.io was adopted by Microsoft (VS Code, GitHub Copilot), OpenAI (Codex CLI, ChatGPT), Cursor, Amp, Goose, OpenCode, Letta, and others within days of publication. Vercel launched skills.sh. The Antigravity Awesome Skills community library catalogued 1,234+ skills compatible with 16+ agents. Microsoft built an Agent Framework SDK (Python, C#, TypeScript) with a `SkillsProvider` class for filesystem discovery and loading.

## Limitations

From [[sources/vijaykumar-skill-md-deep-dive]]:
- Skills lack memory and cannot directly call APIs
- Context window limits apply
- Not suited for highly dynamic logic with complex branching or real-time feedback
- Effectiveness varies across models (cross-platform compatibility not guaranteed)

Best for: domain expertise that is mostly procedural — step-by-step workflows, formatting rules, code patterns, validation checklists, domain-specific pitfalls.

## SKILL.md vs. adjacent formats

| Format | Always loaded | On-demand | Portable | Bundled scripts |
|---|---|---|---|---|
| SKILL.md | ✗ | ✓ | ✓ | ✓ |
| AGENTS.md | ✓ | ✗ | ✓ | ✗ |
| CLAUDE.md / .cursorrules | ✓ | ✗ | ✗ | ✗ |
| Custom GPTs | ✓ | ✗ | ✗ | ✗ |

AGENTS.md is complementary: it provides always-on project context ("here's how we do things around here"), while SKILL.md provides on-demand task expertise ("here's how to do this specific task").

## Related pages

- [[concepts/thin-harness-fat-skills]] — the architecture these skills live in
- [[concepts/progressive-disclosure]] — the 3-level loading mechanism
- [[concepts/resolvers]] — how the right skill is loaded at the right time
- [[concepts/latent-vs-deterministic]] — which steps in a skill use LLM judgment vs. deterministic code
- [[concepts/diarization]] — a specific high-value skill pattern
- [[sources/garrytan-thin-harness-fat-skills]]
- [[sources/vijaykumar-skill-md-deep-dive]]
