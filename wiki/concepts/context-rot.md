---
type: concept
title: "Context Rot"
aliases: [resolver rot, routing table decay, resolver decay]
sources: [garrytan-resolvers-routing-table]
related_concepts: [resolvers, skill-files, thin-harness-fat-skills]
related_entities: [garry-tan]
last_updated: 2026-05-18
---

# Context Rot

The gradual decay of a [[concepts/resolvers|resolver]] (or any routing table / context document) as the system it describes evolves but the document does not. Identified by [[entities/garry-tan|Garry Tan]] in [[sources/garrytan-resolvers-routing-table]] as the long-term failure mode of agent governance.

## The decay timeline

Tan gives a concrete timeline from his 40+ skill system:

| Day | State |
|---|---|
| 1 | Routing table is perfect. Every skill registered. Every trigger accurate. |
| 30 | Three new skills built by sub-agents at 3 AM. Nobody updated the table. |
| 60 | Two trigger descriptions no longer match how users actually phrase things. "Track this flight" vs. "Is my flight delayed?" — same intent, different words, no trigger. |
| 90 | The resolver is a historical document. An artifact of what the system *used to* be able to do. |

## Symptoms

- Skills invoked by direct instruction ("read skills/flight-tracker/SKILL.md") instead of through the resolver — requiring the user to already know which skill to call.
- Missing capabilities: system claims to handle something it no longer routes to.
- Wrong skill fires for valid queries.

## Root causes

1. **Sub-agent spawning**: cron-driven agents build new skills that aren't registered in the resolver.
2. **Language drift**: trigger descriptions are written for how the developer phrases requests, not how users do.
3. **No org chart maintenance**: without someone responsible for updating the routing table, new capabilities go unregistered.

## Fixes

### Short-term: trigger evals
A test suite of sample inputs with expected skill outputs. Run after every resolver change. Catches false negatives (skill should fire, doesn't) and false positives (wrong skill fires). Both are fixable by editing markdown — no code changes needed.

### Medium-term: check-resolvable
A meta-skill that walks the entire chain (AGENTS.md → skill file → code) and finds dead links — skills that exist but have no path from the resolver. Tan's first run found 6 unreachable skills out of 40+ (15% dark). Run weekly as a linter.

### Long-term: self-healing resolver
A reinforcement learning loop that observes every task dispatch — which skill fired, which didn't, which had no match — and periodically rewrites the resolver based on observed evidence. Claude Code's **AutoDream** system (memory consolidation during idle time) is cited as a primitive version of this pattern applied to general context rather than routing specifically.

> "Eight hundred task dispatches over a month. The system sees that 'is my flight on time' never triggers flight-tracker but 'check my flight' does. It rewrites the trigger description."

## Why it matters

Context rot is more dangerous than a missing skill. A missing skill is honest — the system says "I can't do that." A rotten resolver creates the illusion of capability. Users believe the system handles something it no longer routes to, and only discover otherwise at the moment it matters.

At 40+ skills, a static resolver is a liability. Tan's thesis: the resolver must be **tested** (trigger evals), **audited** (check-resolvable), and eventually **self-healing** to remain coherent over time.

## Related pages

- [[concepts/resolvers]] — the routing table that rots
- [[concepts/skill-files]] — what the resolver routes to
- [[sources/garrytan-resolvers-routing-table]]
