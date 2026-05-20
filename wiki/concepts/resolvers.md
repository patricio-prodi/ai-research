---
type: concept
title: "Resolvers"
aliases: [resolver, context resolver, context routing, filing resolver, skill resolver]
sources: [garrytan-thin-harness-fat-skills, garrytan-resolvers-routing-table]
related_concepts: [thin-harness-fat-skills, skill-files, latent-vs-deterministic, context-rot]
related_entities: [garry-tan, gbrain]
last_updated: 2026-05-18
---

# Resolvers

A **routing table for context**: when task type X appears, load document Y first. Resolvers ensure the model has the right context at the right time, without loading everything into the context window simultaneously.

Defined by [[entities/garry-tan|Garry Tan]] in [[sources/garrytan-thin-harness-fat-skills]] as one of five definitions in the [[concepts/thin-harness-fat-skills|thin harness, fat skills]] architecture. Expanded in depth in [[sources/garrytan-resolvers-routing-table]].

> "A resolver is 200 lines of markdown that replaced 20,000 lines of crammed context. When it's missing, skills invent their own filing logic and everything slowly degrades. When it's present but untested, capabilities go dark. When it's tested but static, it rots within 90 days. When it's tested and self-healing, the system compounds."

## What resolvers do

- [[concepts/skill-files|Skills]] tell the model *how* to do something.
- Resolvers tell it *what to load* and *when*.

Without a resolver: a developer changes a prompt and ships it.
With a resolver: the model reads `docs/EVALS.md` first — which instructs: run the eval suite, compare scores, if accuracy drops more than 2%, revert and investigate. The developer didn't know the eval suite existed. The resolver loaded the right context at the right moment.

## The CLAUDE.md problem

Tan's confession: his CLAUDE.md grew to 20,000 lines. Every quirk, every pattern, every lesson ever encountered. Result: model attention degraded across the massive document.

> "Claude Code literally told me to cut it back."

Fix: ~200 lines of pointers + resolvers. Twenty thousand lines of knowledge accessible on demand, without polluting the context window. The resolver loads the right document when it matters.

> "You can't make someone smarter by shouting louder. You make them smarter by giving them the right book at the right moment."

## Resolvers are fractal

Resolvers exist at every layer of a system — not just the top:

- **Skill resolver** (`AGENTS.md`): maps task types to skill files. "Who is this person?" → brain-ops. "Ingest this PDF" → pdf-ingest.
- **Filing resolver** (`RESOLVER.md`): maps content types to directories. Person → `people/`. Company → `companies/`. Policy analysis → `civic/`.
- **Context resolver** (inside each skill): sub-routing within a skill. The executive assistant skill routes email triage, scheduling, and signature tracking to different sub-procedures.

Claude Code's skill `description` field is itself a resolver — the description *is* the routing signal. It's resolvers all the way down.

## Governance: the four mandates

From Tan's production system (200 inputs/day, 40+ skills, 25,000 files):

### 1. Every brain-writing skill reads the resolver
Ten of 13 brain-writing skills had hardcoded default paths. Fix: a shared `_brain-filing-rules.md` cataloguing misfiling patterns + a two-line mandate at the top of every brain-writing skill:

> "Before creating any new brain page, read `brain/RESOLVER.md` and `skills/_brain-filing-rules.md`. File by primary subject, not by source format or skill name."

### 2. Trigger evals
A test suite of sample inputs with expected skill outputs. Catches two failure modes:
- **False negative**: skill should fire but doesn't (trigger description wrong or missing)
- **False positive**: wrong skill fires (two triggers overlap)

Both are fixable by editing markdown. No code changes. Tan's suite: 50 inputs. Example:
```
Input: "check my signatures"   Expected: executive-assistant (signature section)
Input: "who is Pedro Franceschi"   Expected: brain-ops → gbrain search
Input: "save this article to brain"   Expected: idea-ingest + RESOLVER.md
```

> "If you can't prove the right skill fires for the right input, you don't have a system. You have a collection of skills and a prayer."

### 3. Check-resolvable (the meta-skill)
A skill that walks the entire chain — `AGENTS.md` → skill file → code — and finds dead links. Skills that exist but have no path from the resolver.

Tan's first run: 6 unreachable skills out of 40+ (15% of capabilities dark). A flight tracker nobody could invoke by asking about flights. A citation fixer not listed in the resolver at all. Fixed in an hour — just added triggers to `AGENTS.md`.

Now runs weekly. The resolver equivalent of a linter.

### 4. Self-healing resolver (forward-looking)
A reinforcement learning loop that observes every task dispatch and periodically rewrites the resolver based on observed evidence. Claude Code's **AutoDream** system (memory consolidation during idle time) is cited as a primitive version.

> "Eight hundred task dispatches over a month. The system sees that 'is my flight on time' never triggers flight-tracker but 'check my flight' does. It rewrites the trigger description."

## The invisible skill problem

A skill that exists but isn't reachable creates the illusion of capability — worse than not having the skill at all:

> "A missing skill is honest — the system says 'I can't do that' and you know to build it. A skill that exists but isn't reachable creates the illusion of capability. You think the system handles signatures. It doesn't. And you don't find out until the moment it matters."

## Resolvers as management

The organizational metaphor: in a system with 40+ skills and 25,000 files, you don't just have code — you have an organization.

| Org concept | Resolver equivalent |
|---|---|
| Employees | Skills |
| Org chart | Skill resolver (AGENTS.md) |
| Internal process | Filing rules (_brain-filing-rules.md) |
| Audit / compliance | check-resolvable |
| Performance reviews | Trigger evals |

> "The problem isn't that models aren't smart enough. The problem is that we've been building organizations with no management layer. Just a pile of talented employees and a vague hope they'll coordinate."

## Context rot

Resolvers decay over time — see [[concepts/context-rot]] for the full pattern and timeline. The short version: Day 1 is perfect; Day 90 is a historical document describing what the system *used to* be able to do.

## Claude Code's built-in resolver

[[entities/anthropic|Anthropic]]'s Claude Code implements a resolver natively: every skill has a `description` field, and the model matches user intent to skill descriptions automatically. The user doesn't need to remember that `/ship` exists — the description is the resolver.

This is a key architectural decision: intent routing happens in latent space (model judgment) rather than deterministic dispatch.

## Resolvers vs. RAG

RAG retrieves documents based on embedding similarity to a query. Resolvers are more structured: explicit rules mapping task types to documents, rather than probabilistic retrieval. Resolvers are deterministic by design; RAG is probabilistic.

For context management within an agent session, resolvers are more reliable than RAG when the routing logic is known in advance.

## Related pages

- [[concepts/thin-harness-fat-skills]]
- [[concepts/skill-files]]
- [[concepts/latent-vs-deterministic]]
- [[concepts/context-rot]]
- [[entities/gbrain]]
- [[sources/garrytan-thin-harness-fat-skills]]
- [[sources/garrytan-resolvers-routing-table]]
