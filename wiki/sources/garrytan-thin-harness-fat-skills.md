---
type: source
title: "Thin Harness, Fat Skills"
article: "raw/Thin Harness, Fat Skills.md"
source_url: "https://x.com/garrytan/status/2042925773300908103"
author: "[[garry-tan]]"
published: 2026-04-11
ingested: 2026-04-16
tags: [agent-architecture, skill-files, claude-code, productivity, llm-workflow]
key_concepts: [thin-harness-fat-skills, skill-files, resolvers, latent-vs-deterministic, diarization]
---

# Thin Harness, Fat Skills

**Author**: [[entities/garry-tan|Garry Tan]] (YC president), published 2026-04-11 on X.

Source: [raw/Thin Harness, Fat Skills.md](../raw/Thin%20Harness%2C%20Fat%20Skills.md)

## Overview

Garry Tan's framework for understanding why some AI coding agent users are 100x–1000x more productive than others. The productivity gap is not from better models — both the 2x and 100x users access the same models. The difference is **architecture**: a thin CLI harness wrapped around fat, reusable skill files. Tan distills this into five definitions and a concrete three-layer system design.

Published shortly after Anthropic accidentally shipped the full Claude Code source (~512,000 lines) to npm on March 31, 2026 — which Tan says confirmed what he had been teaching at YC.

## Key claims

1. **The gap is architectural, not model-level.** Steve Yegge: agents make engineers "10x to 100x as productive as Cursor/chat users today, and roughly 1000x as productive as Googlers in 2005." Same models; different harness design.

2. **The harness should be thin.** ~200 lines of code. JSON in, text out. Read-only by default. Does four things: runs the model in a loop, reads/writes files, manages context, enforces safety. The anti-pattern is a fat harness — 40+ tool definitions eating the context window, MCP round-trips taking 2–15 seconds per operation.

3. **Skills should be fat.** Reusable markdown procedures encoding judgment, process, domain knowledge. This is where 90% of the value lives. Skills work like method calls: same procedure, different parameters, radically different capabilities.

4. **Resolvers route context on demand.** Load the right document at the right moment. Prevents context bloat. A 20,000-line CLAUDE.md degrades model attention; ~200 lines of pointers + resolvers is the correct structure.

5. **Latent vs. deterministic is the key design split.** LLMs excel at judgment (latent space). Same-input-same-output operations belong in deterministic code. Misassigning problems to the wrong side is the most common mistake in agent design.

6. **Diarization makes AI useful for real knowledge work.** Reading everything about a subject and writing a structured profile — catching the gap between what someone says and what they're actually building. Can't be done with SQL or RAG; requires genuine synthesis.

## Evidence and examples

- **Claude Code source leak (March 31, 2026)**: Tan reviewed the 512,000-line codebase. Key techniques: live repo context, prompt caching, purpose-built tools, context bloat minimization, structured session memory, parallel sub-agents.

- **Playwright CLI vs Chrome MCP**: Purpose-built CLI handles each browser operation in ~100ms. Chrome MCP takes ~15 seconds for screenshot-find-click-wait-read. 75x speed difference illustrates thin harness vs fat harness.

- **YC Startup School case study (July 2026, projected)**: 6,000 founders. Traditional: 15-person program team, breaks above 200 founders. Agentic: /enrich-founder skill diarizes all profiles nightly, /match-* skills run three distinct matching strategies. Model catches gaps (founder says "observability tool" but 80% of commits are billing code). The /improve skill reads NPS surveys post-event and rewrites matching rules. 12% "OK" ratings → 4% after one learning cycle.

- **Skill self-improvement instruction**: Tan's rule for his own agent: "You are not allowed to do one-off work. If I ask you to do something… you must codify it into a skill file. If it should run automatically, put it on a cron. The test: if I have to ask you for something twice, you failed." Got 1,000 likes, 2,500 bookmarks.

## Notable quotes

> "The secret isn't the model. It's the thing wrapping the model."

> "Markdown is, in fact, a more perfect encapsulation of capability than rigid source code, because it describes process, judgment, and context in the language the model already thinks in."

> "Push intelligence up into skills. Push execution down into deterministic tooling. Keep the harness thin."

> "Every skill you write is a permanent upgrade to your system. It never degrades. It never forgets. It runs at 3 AM while you sleep. And when the next model drops, every skill instantly gets better."

## Implications

- The dominant strategy for AI productivity is **architectural clarity**, not model selection or prompt tricks.
- Skills compound. As models improve, every skill automatically improves in its latent steps while deterministic steps remain reliable.
- The "thin harness, fat skills" pattern applies beyond coding: any knowledge work domain (legal, research, recruiting, logistics) can be structured this way.
- The learning loop (survey → diarize → rewrite skill) is Tan's candidate for the most valuable loop in 2026 knowledge work.

## Related pages

- [[concepts/thin-harness-fat-skills]]
- [[concepts/skill-files]]
- [[concepts/resolvers]]
- [[concepts/latent-vs-deterministic]]
- [[concepts/diarization]]
- [[concepts/agentic-ai]]
- [[entities/garry-tan]]
- [[entities/y-combinator]]
- [[entities/anthropic]]
