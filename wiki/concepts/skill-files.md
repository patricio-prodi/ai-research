---
type: concept
title: "Skill Files"
aliases: [skills, skill file, slash commands, agent skills]
sources: [garrytan-thin-harness-fat-skills]
related_concepts: [thin-harness-fat-skills, resolvers, latent-vs-deterministic, diarization, llm-wiki]
related_entities: [garry-tan]
last_updated: 2026-04-16
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

## Related pages

- [[concepts/thin-harness-fat-skills]] — the architecture these skills live in
- [[concepts/resolvers]] — how the right skill is loaded at the right time
- [[concepts/latent-vs-deterministic]] — which steps in a skill use LLM judgment vs. deterministic code
- [[concepts/diarization]] — a specific high-value skill pattern
- [[sources/garrytan-thin-harness-fat-skills]]
