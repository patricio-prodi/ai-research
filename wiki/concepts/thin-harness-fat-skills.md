---
type: concept
title: "Thin Harness, Fat Skills"
aliases: [thin harness, fat skills, harness architecture]
sources: [garrytan-thin-harness-fat-skills]
related_concepts: [skill-files, resolvers, latent-vs-deterministic, diarization, agentic-ai]
related_entities: [garry-tan, y-combinator, anthropic]
last_updated: 2026-04-16
---

# Thin Harness, Fat Skills

A design principle for AI agent systems: keep the program wrapper minimal (~200 lines) and encode nearly all capability in reusable [[concepts/skill-files|skill files]]. Introduced by [[entities/garry-tan|Garry Tan]] in [[sources/garrytan-thin-harness-fat-skills]].

## The core insight

The 100x productivity gap between AI agent power users and typical LLM users does not come from better models. Both groups use the same models. The difference is architecture:

- **Fat harness, thin skills** (the anti-pattern): lots of tool definitions, MCP integrations, complex plumbing — intelligence is in the glue code, not the prompts. Heavy context usage, slow round-trips, fragile.
- **Thin harness, fat skills** (the pattern): minimal wrapper, with domain knowledge and process encoded in markdown skill files the model can read and execute.

## Three-layer architecture

```
┌─────────────────────────────────────┐
│  Fat skills (markdown procedures)   │  ← 90% of value lives here
│  Encode judgment, process, domain   │
├─────────────────────────────────────┤
│  Thin CLI harness (~200 lines)      │  ← JSON in, text out
│  Loop + file I/O + context + safety │
├─────────────────────────────────────┤
│  Deterministic application layer    │  ← QueryDB, ReadDoc, Search
│  Same input → same output, always   │
└─────────────────────────────────────┘
```

**Directional principle**: Push intelligence *up* into skills. Push execution *down* into deterministic tooling. The harness just connects them.

## What goes in the harness

Four things only:
1. Run the model in a loop
2. Read and write files
3. Manage context
4. Enforce safety

That is the full definition of thin. Adding tool definitions, MCP servers, REST API wrappers, or god-tools is the anti-pattern.

## What goes in skills

Everything else: step-by-step processes, judgment criteria, domain conventions, routing logic, quality standards. Written in markdown. Invoked like method calls with parameters.

## Why this compounds

When a new model drops, every latent step in every skill automatically improves — the model's judgment gets better. The deterministic layer stays perfectly reliable. Skills never degrade, never forget, run at any hour. Each skill written is a permanent capability upgrade.

> "Every skill you write is a permanent upgrade to your system." — [[entities/garry-tan|Tan]]

## Concrete performance example

Purpose-built Playwright CLI: ~100ms per browser operation.
Chrome MCP: ~15 seconds for screenshot-find-click-wait-read.
**75x speed difference** from harness design alone.

## Relationship to Claude Code

Tan reviewed the Claude Code source (~512,000 lines, accidentally published to npm by [[entities/anthropic|Anthropic]] on March 31, 2026). He reports it implements this architecture: live repo context, prompt caching, purpose-built tools, context bloat minimization, structured session memory, parallel sub-agents.

Claude Code's built-in [[concepts/resolvers|resolver]] matches user intent to skill descriptions automatically — the description field on each skill is the resolver.

## Related pages

- [[concepts/skill-files]] — what fat skills actually are
- [[concepts/resolvers]] — how context is routed to skills
- [[concepts/latent-vs-deterministic]] — the core design split
- [[concepts/diarization]] — the most demanding skill type
- [[concepts/agentic-ai]] — broader context on agent architecture
- [[sources/garrytan-thin-harness-fat-skills]]
