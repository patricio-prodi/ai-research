---
type: concept
title: "RAG vs. LLM Wiki"
aliases: [retrieval-augmented generation, rag, vector search, embedding search]
sources: [karpathy-llm-knowledge-bases, karpathy-llm-wiki-gist]
related_concepts: [llm-wiki]
related_entities: []
last_updated: 2026-05-14
---

# RAG vs. LLM Wiki

Two fundamentally different approaches to using LLMs with a document collection. Understanding the distinction is central to the [[concepts/llm-wiki|LLM Wiki]] pattern.

## RAG (Retrieval-Augmented Generation)

The dominant approach. At query time:
1. Embed the query into a vector.
2. Retrieve the most similar document chunks from a vector database.
3. Pass retrieved chunks to the LLM as context.
4. LLM generates an answer from the chunks.

**No knowledge is accumulated.** The LLM re-derives everything from scratch on every query. Infrastructure required: embedding models, vector database, chunking pipeline.

Examples (per [[sources/karpathy-llm-wiki-gist]]): NotebookLM, ChatGPT file uploads, most enterprise document Q&A systems.

> "Ask a subtle question that requires synthesizing five documents, and the LLM has to find and piece together the relevant fragments every time. Nothing is built up." — [[entities/andrej-karpathy|Karpathy]]

## LLM Wiki

At ingest time:
1. LLM reads the source document.
2. LLM writes and updates wiki pages — summaries, cross-references, entity updates, contradiction notes.
3. Knowledge is compiled once and persisted.

At query time:
1. LLM reads the wiki index.
2. Drills into relevant pages.
3. Synthesizes from pre-compiled, cross-referenced knowledge.

**Knowledge accumulates.** Every source strengthens the existing synthesis. Cross-references are pre-built. Contradictions are pre-flagged.

## Comparison

| Dimension | RAG | LLM Wiki |
|---|---|---|
| Knowledge persistence | None — re-derived every query | Persistent — wiki grows over time |
| Cross-document synthesis | Done at query time, every time | Done at ingest time, once |
| Infrastructure | Vector DB, embedding pipeline | Just markdown files |
| Scale ceiling | High (millions of docs) | Moderate (~100s of sources) |
| Query latency | Fast | Fast (if wiki is well-indexed) |
| Contradiction detection | Unreliable | Explicit — flagged during ingest |
| Human oversight | Low | High — human reads the wiki |
| Maintenance cost | Low (just add to the vector store) | Higher (ingest updates many pages) |

## When to use which

**RAG is better when**:
- You have thousands of documents and can't afford per-document ingest cost.
- Sources are stable (no need for incremental synthesis).
- You need fast, low-maintenance Q&A.

**LLM Wiki is better when**:
- You're accumulating knowledge over weeks/months.
- Deep synthesis across sources matters more than recall breadth.
- You want to read and navigate the knowledge base yourself (Obsidian).
- You care about contradiction detection and evolving understanding.
- Scale is moderate (up to ~hundreds of sources).

## [[entities/andrej-karpathy|Karpathy]]'s finding

At ~100 articles (~400,000 words), a well-organized wiki with a good index file allows the LLM to navigate without any RAG infrastructure. The index is enough. RAG adds complexity without proportional benefit at that scale.

## Related pages

- [[concepts/llm-wiki]] — the full LLM Wiki pattern
