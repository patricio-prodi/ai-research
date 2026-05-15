---
type: source
title: "Andrej Karpathy's LLM Knowledge Bases explained"
article: "articles/Andrej Karpathy's LLM Knowledge Bases explained.md"
source_url: "https://medium.com/data-science-in-your-pocket/andrej-karpathys-llm-knowledge-bases-explained-2d9fd3435707"
author: "Mehul Gupta"
published: 2026-04-12
ingested: 2026-04-16
tags: [knowledge-management, llm-workflow, obsidian, rag, wiki]
key_concepts: [llm-wiki, rag-vs-wiki]
---

# Andrej Karpathy's LLM Knowledge Bases explained

> Source: [Medium — Data Science in Your Pocket](https://medium.com/data-science-in-your-pocket/andrej-karpathys-llm-knowledge-bases-explained-2d9fd3435707) by Mehul Gupta | Published 2026-04-12

## Overview

A secondhand explanation of [[entities/andrej-karpathy|Andrej Karpathy]]'s personal workflow shift: from writing code to building LLM-maintained knowledge bases. Karpathy described the system himself; this article summarizes it in accessible terms. The core idea is using an LLM as a *compiler* that converts a raw folder of documents into an organized, interlinked wiki.

## Key claims

1. **Karpathy shifted from coding to "knowledge work"** — he now spends most of his time using AI to organize research rather than write software.

2. **The system has 7 steps**: Ingest → Compile → View (Obsidian) → Q&A → Output → Lint → Extra tools.

3. **The LLM acts as a compiler**: it reads raw files (articles, PDFs, code, images, datasets) and produces a wiki of linked markdown files — summaries, categorized articles, cross-references.

4. **No RAG needed at moderate scale**: Karpathy's wiki (~100 articles, ~400,000 words) is well-organized enough that the LLM can navigate it via an index without vector search infrastructure.

5. **Outputs are filed back**: The LLM produces markdown notes, Marp slides, or Matplotlib charts — and these outputs get added back into the wiki, compounding the knowledge base.

6. **Linting keeps it healthy**: Periodic health checks find contradictions, fill gaps (using web search), and surface connections that suggest new research directions.

7. **Future goal — fine-tuning**: Karpathy wants to eventually fine-tune a model on the wiki so the knowledge is baked in rather than retrieved at query time.

## Toolchain

| Tool | Role |
|---|---|
| Obsidian Web Clipper | Browser extension: saves web articles as markdown |
| Obsidian | IDE / viewer for the wiki |
| Marp | Markdown → slide deck |
| Matplotlib | Charts/graphs from AI-generated code |
| Custom search script | LLM-callable CLI search over wiki files |

## Quotes

> "Think of a knowledge base as a super-powered, digital encyclopedia that is built just for you."

> "The Golden Rule: Karpathy rarely touches the Wiki files himself. He treats the Wiki as 'AI territory.' The AI writes it, updates it, and maintains it. Karpathy just reads it."

> "Karpathy points out that right now, this is a 'hacky' collection of scripts. But he believes there is a huge opportunity here for someone to build a polished product that makes this easy for everyone."

## Implications

- The LLM-wiki pattern is a practical alternative to RAG that works well at moderate scale (<500 sources).
- The human's role shifts entirely to curation and direction; the LLM handles all bookkeeping.
- This workflow is directly applicable to this vault — see [[concepts/llm-wiki]] for the full pattern.

## Limitations / caveats

- This is a secondhand account (Mehul Gupta summarizing Karpathy). Some details may be simplified.
- Scale limits not clearly defined — at what point does index-based navigation break down vs. RAG?
- Fine-tuning ambition is noted but unproven in this context.

## Related pages

- [[concepts/llm-wiki]] — the full pattern derived from this and other sources
- [[concepts/rag-vs-wiki]] — comparison of RAG vs. wiki approach
- [[entities/andrej-karpathy]] — about Karpathy
