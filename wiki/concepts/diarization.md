---
type: concept
title: "Diarization"
aliases: [profile synthesis, document diarization, analyst brief]
sources: [garrytan-thin-harness-fat-skills]
related_concepts: [thin-harness-fat-skills, skill-files, latent-vs-deterministic, rag-vs-wiki]
related_entities: [garry-tan]
last_updated: 2026-04-16
---

# Diarization

Reading everything about a subject and writing a **structured profile** — a single page of judgment distilled from dozens or hundreds of documents. Tan's term for the skill type that makes AI genuinely useful for knowledge work (as opposed to lookup or retrieval tasks).

From [[sources/garrytan-thin-harness-fat-skills]] by [[entities/garry-tan|Garry Tan]].

## Definition

> "Diarization is the step that makes AI useful for real knowledge work. The model reads everything about a subject and writes a structured profile — a single page of judgment distilled from dozens or hundreds of documents."

The term is borrowed from audio processing (*speaker diarization* = identifying who spoke when), repurposed here to mean: reading a corpus and producing a structured intelligence brief.

Diarization is a purely [[concepts/latent-vs-deterministic|latent]] operation. It cannot be done with:
- **SQL queries** — no structured field captures the synthesis
- **RAG pipelines** — embedding similarity retrieves relevant chunks, but cannot hold contradictions in mind or notice what changed and when
- **Keyword filters** — can't detect gaps between stated and actual behavior

It requires the model to actually read, hold contradictions, notice temporal change, and synthesize structured intelligence.

## What diarization produces

Not a database lookup. Not a search result. An **analyst's brief**:

- What the subject says vs. what they're actually doing
- How the story has changed over time
- Contradictions across sources
- The pattern beneath the surface evidence

## Canonical example (YC Startup School)

From the article:

```
FOUNDER: Maria Santos
COMPANY: Contrail (contrail.dev)
SAYS: "Datadog for AI agents"
ACTUALLY BUILDING: 80% of commits are in billing module.
She's building a FinOps tool disguised as observability.
```

Producing this requires reading the GitHub commit history, the application essay, and the advisor 1:1 transcript simultaneously, holding all three in mind, and noticing the gap. No single-source search finds this. Diarization finds it.

A second example from the same case: "Kim applied as 'developer tools' but his 1:1 transcript reveals he's building compliance automation for SOC2. Move him to FinTech/RegTech." — no embedding captures this reclassification; it requires reading the full profile.

## Diarization in the /improve learning loop

Post-event NPS surveys → the model diarizes **mediocre** responses (not the outright bad ones, the "almost worked" ones) → extracts patterns → writes new rules back into matching skill files. This is how skills self-improve.

12% "OK" ratings → 4% after one cycle. The skill learned what "OK" actually meant.

## Relationship to the LLM Wiki

The INGEST operation in this vault is a form of diarization: reading a raw article and writing a structured wiki page that distills its claims, evidence, implications, and contradictions. The "Says vs. Actually Building" gap detection is analogous to flagging contradictions between sources.

> **Note:** The LLM Wiki concept (from [[sources/karpathy-llm-knowledge-bases|Karpathy]]) independently arrives at the same insight: LLMs can synthesize across documents in a way RAG cannot. Diarization is Tan's name for this capability in an agent context.

## Diarization vs. RAG

| | RAG | Diarization |
|---|---|---|
| Retrieves documents | Yes | Yes |
| Ranks by relevance | Yes | No — reads all |
| Holds contradictions | No | Yes |
| Detects temporal change | No | Yes |
| Produces structured brief | No | Yes |
| Notices unstated patterns | No | Yes |
| Scalable to millions of records | Yes | No — compute-intensive |

RAG is appropriate for retrieval at scale. Diarization is appropriate when depth and synthesis matter more than coverage.

## Related pages

- [[concepts/thin-harness-fat-skills]]
- [[concepts/skill-files]] — diarization is typically implemented as a skill
- [[concepts/latent-vs-deterministic]] — diarization is a latent-only operation
- [[concepts/rag-vs-wiki]] — the RAG vs. synthesis tradeoff
- [[sources/garrytan-thin-harness-fat-skills]]
