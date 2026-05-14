---
type: concept
title: "Latent vs. Deterministic"
aliases: [latent space, deterministic execution, latent vs deterministic, agent design split]
sources: [garrytan-thin-harness-fat-skills]
related_concepts: [thin-harness-fat-skills, skill-files, diarization, agentic-ai]
related_entities: [garry-tan]
last_updated: 2026-04-16
---

# Latent vs. Deterministic

The most critical design distinction in agent systems: every step is either **latent** (LLM judgment) or **deterministic** (same input → same output, always). Confusing them is described by [[entities/garry-tan|Tan]] as "the most common mistake in agent design."

From [[sources/garrytan-thin-harness-fat-skills]].

## Definitions

**Latent space** — where intelligence lives. The model reads, interprets, decides. Judgment, synthesis, pattern recognition, reasoning under ambiguity. This is what LLMs are uniquely good at.

**Deterministic** — where trust lives. Same input, same output. Every time. SQL queries, compiled code, arithmetic, combinatorial optimization, API calls with known schemas.

## The canonical failure mode

> "An LLM can seat 8 people at a dinner table, accounting for personalities and social dynamics. Ask it to seat 800 and it will hallucinate a seating chart that looks plausible but is completely wrong."

Seating 800 people optimally is a combinatorial optimization problem — deterministic. Forcing it into latent space produces plausible-looking wrong answers. The LLM's judgment of personalities is latent (correct use); the assignment algorithm is deterministic (must be in code).

## Correct assignment

| Problem type | Correct layer | Why |
|---|---|---|
| Reading and synthesizing documents | Latent | Requires judgment, holds contradictions |
| SQL queries, data retrieval | Deterministic | Same input must yield same output |
| Classifying a founder's actual focus | Latent | Requires reading across sources |
| Assigning seats given a seating plan | Deterministic | Combinatorial, needs exact correctness |
| Diarizing a complex profile | Latent | Synthesis across contradictory evidence |
| Running an eval suite | Deterministic | Scores must be reproducible |
| Detecting gap between stated vs. actual work | Latent | Pattern recognition across documents |
| GitHub commit statistics | Deterministic | Exact counts from version control |

## In the three-layer architecture

In [[concepts/thin-harness-fat-skills|thin harness, fat skills]]:
- **Fat skills** (top layer): latent — step descriptions, judgment criteria, synthesis instructions
- **Deterministic application layer** (bottom): exact execution — `QueryDB`, `ReadDoc`, `Search`, `Timeline`
- **Thin harness** (middle): mostly deterministic (loop, file I/O) with minimal latent routing

The architectural principle follows directly: push intelligence up (where latent steps improve automatically with better models) and push execution down (where deterministic steps remain reliable regardless of model changes).

## YC Startup School example

The `/match-lunch` skill for 600 founders combines both:
- **Latent**: the LLM invents the themes for matching groups
- **Deterministic**: an algorithm assigns seats (no repeats, exact constraints)

Attempting to do the full assignment in latent space would produce plausible-sounding seating charts that violate constraints. Doing the theme invention deterministically is impossible — it requires judgment about meaning.

## Relationship to hallucination

Hallucination is often a sign of a **misassigned deterministic problem** in latent space. When a model produces a plausible-looking but incorrect seating chart or calculation, it is not failing at intelligence — it is being asked to do exact computation in a probabilistic system. The fix is architectural (move to deterministic layer), not model-selection.

## Related pages

- [[concepts/thin-harness-fat-skills]]
- [[concepts/skill-files]] — skills contain both latent and deterministic steps
- [[concepts/diarization]] — a latent-only operation (by definition)
- [[sources/garrytan-thin-harness-fat-skills]]
