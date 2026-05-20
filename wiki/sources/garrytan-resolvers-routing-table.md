---
type: source
title: "Resolvers: The Routing Table for Intelligence"
article: "raw/Resolvers The Routing Table for Intelligence.md"
source_url: "https://x.com/garrytan/status/2044479509874020852"
author: "[[garry-tan]]"
published: 2026-04-15
ingested: 2026-05-18
tags: [agent-architecture, resolvers, context-management, skill-files, claude-code, llm-workflow]
key_concepts: [resolvers, context-rot, thin-harness-fat-skills, skill-files]
---

# Resolvers: The Routing Table for Intelligence

**Author**: [[entities/garry-tan|Garry Tan]] ([@garrytan](https://x.com/garrytan))
**Published**: 2026-04-15
**Article**: [raw/Resolvers The Routing Table for Intelligence.md](../raw/Resolvers%20The%20Routing%20Table%20for%20Intelligence.md)

Sequel to [[sources/garrytan-thin-harness-fat-skills|"Thin Harness, Fat Skills"]]. Tan argues that resolvers — defined in the prior article — are the most important and overlooked part of the agent architecture. The article is a narrative deep-dive into resolver failures, fixes, and governance patterns drawn from his personal agent running 200 inputs/day on 25,000 files.

---

## Overview

Resolvers got no attention in the first article. That invisibility is exactly why they matter: they are catastrophic when absent and invisible when working. This piece corrects the gap.

> "A resolver is a routing table for context. When task type X appears, load document Y first."

---

## Key claims

### 1. The 20,000-line CLAUDE.md confession

Tan's own CLAUDE.md grew to 20,000 lines. Attention degraded, responses slowed, accuracy fell. Claude Code told him to cut it back. Fix: ~200 lines of pointers (a numbered decision tree mapping task types to documents). The result was faster responses, more accurate filing, fewer hallucinations — not because the model got smarter, but because context noise dropped.

> "You can't make someone smarter by shouting louder. You make them smarter by giving them the right book at the right moment."

### 2. The misfiling that revealed everything

When his idea-ingest skill filed Will Manidis's policy analysis "No New Deal for OpenAI" into `sources/` (for raw data dumps) instead of `civic/` (for policy analysis), Tan pulled the thread. He audited all 13 brain-writing skills: only 3 of 13 referenced the resolver. The other 10 had hardcoded paths.

Fix: a shared `_brain-filing-rules.md` document cataloguing common misfiling patterns, plus a mandate that every brain-writing skill reads `RESOLVER.md` before creating any page.

> "Two-line mandate at the top: Before creating any new brain page, read `brain/RESOLVER.md` and `skills/_brain-filing-rules.md`. File by primary subject, not by source format or skill name."

### 3. The invisible skill problem

The same pattern applies to skill routing, not just filing. A signature-tracking capability existed inside the executive assistant skill but had no trigger in the resolver. When users asked "check my signatures," the system had no path to the skill.

> "A missing skill is honest — the system says 'I can't do that' and you know to build it. A skill that exists but isn't reachable creates the illusion of capability."

### 4. Trigger evals

Fix for the invisible skill problem: a test suite of 50 sample inputs with expected skill outputs.

Two failure modes:
- **False negative**: skill should fire but doesn't (trigger description wrong or missing)
- **False positive**: wrong skill fires (two triggers overlap)

Both fixable by editing markdown. No code changes.

> "If you can't prove the right skill fires for the right input, you don't have a system. You have a collection of skills and a prayer."

### 5. Check-resolvable (the meta-skill)

A skill that walks the entire chain — `AGENTS.md` → skill file → code — and finds dead links (skills that exist but have no path from the resolver). First run found 6 unreachable skills out of 40+ (15% of capabilities were dark). Runs weekly. Acts as a linter for the resolver.

### 6. Context rot

Resolvers decay. Day 1 is perfect. Day 30: new skills built by sub-agents at 3 AM, nobody updated the table. Day 60: trigger descriptions no longer match how users phrase things. Day 90: the resolver is a historical document.

Forward-looking fix: an RLM (reinforcement learning) loop observing every task dispatch and periodically rewriting the resolver based on observed evidence. Claude Code's AutoDream memory consolidation system is cited as a primitive version.

### 7. Resolvers are fractal

Resolvers exist at every layer:
- **Skill resolver** (AGENTS.md): maps task types to skill files
- **Filing resolver** (RESOLVER.md): maps content types to directories
- **Context resolver** (inside each skill): sub-routing within a skill

Claude Code's skill description field is itself a resolver — the description *is* the routing signal.

### 8. Resolvers as management

The organizing metaphor: resolvers are management, not just routing. Skills are employees. The resolver is the org chart. Filing rules are internal process. Check-resolvable is audit and compliance. Trigger evals are performance reviews.

> "The problem isn't that models aren't smart enough. The problem is that we've been building organizations with no management layer."

---

## Evidence / data

- Personal production system: 200 inputs/day, 25,000 files, 40+ skills
- 3 of 13 brain-writing skills referenced the resolver (audit finding)
- First check-resolvable run: 6 unreachable skills out of 40+ (15% dark)
- 50-input trigger eval suite as standard practice

---

## Implications

1. Resolvers are not optional infrastructure — they are the governance layer. Their absence causes silent drift, not dramatic failure.
2. The "stuff everything in the system prompt" instinct is the canonical mistake for agent systems at scale.
3. Testing must include routing correctness (trigger evals), not just output quality.
4. Systems with 40+ skills require systematic reachability audits to maintain coherence.
5. Resolver maintenance must be automated (self-healing) or the table rots within 90 days.

---

## Quotes

> "A resolver is a routing table for context. When task type X appears, load document Y first. That's it. One sentence. But that one sentence is the difference between an agent that compounds intelligence and an agent that slowly forgets what it knows."

> "A resolver is 200 lines of markdown that replaced 20,000 lines of crammed context. When it's missing, skills invent their own filing logic and everything slowly degrades. When it's present but untested, capabilities go dark. When it's tested but static, it rots within 90 days. When it's tested and self-healing, the system compounds."

> "Almost nobody is building them explicitly. Everyone is cramming 20,000 lines into the system prompt and wondering why the model seems dumber than it should be. The model isn't dumb. It's drowning."

---

## Related pages

- [[concepts/resolvers]] — deep dive on the concept
- [[concepts/context-rot]] — the decay problem described in §6
- [[concepts/thin-harness-fat-skills]] — the prior article this follows up
- [[concepts/skill-files]] — what resolvers route to
- [[entities/garry-tan]]
- [[entities/gbrain]]
- [[sources/garrytan-thin-harness-fat-skills]]
