---
type: concept
title: "Resolvers"
aliases: [resolver, context resolver, context routing]
sources: [garrytan-thin-harness-fat-skills]
related_concepts: [thin-harness-fat-skills, skill-files, latent-vs-deterministic]
related_entities: [garry-tan]
last_updated: 2026-04-16
---

# Resolvers

A **routing table for context**: when task type X appears, load document Y first. Resolvers ensure the model has the right context at the right time, without loading everything into the context window simultaneously.

Defined by [[entities/garry-tan|Garry Tan]] in [[sources/garrytan-thin-harness-fat-skills]] as one of five definitions in the [[concepts/thin-harness-fat-skills|thin harness, fat skills]] architecture.

## What resolvers do

- [[concepts/skill-files|Skills]] tell the model *how* to do something.
- Resolvers tell it *what to load* and *when*.

Without a resolver: a developer changes a prompt and ships it.
With a resolver: the model reads `docs/EVALS.md` first — which instructs: run the eval suite, compare scores, if accuracy drops more than 2%, revert and investigate. The developer didn't know the eval suite existed. The resolver loaded the right context at the right moment.

## The CLAUDE.md problem

Tan's confession: his CLAUDE.md grew to 20,000 lines. Every quirk, every pattern, every lesson ever encountered. Result: model attention degraded across the massive document.

> "Claude Code literally told me to cut it back."

Fix: ~200 lines of pointers + resolvers. Twenty thousand lines of knowledge accessible on demand, without polluting the context window. The resolver loads the right document when it matters.

This illustrates the **thin harness principle** applied to configuration: even the harness's own instructions should be pointer-based, not monolithic.

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
- [[sources/garrytan-thin-harness-fat-skills]]
