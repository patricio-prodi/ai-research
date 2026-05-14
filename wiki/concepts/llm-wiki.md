---
type: concept
title: "LLM Wiki"
aliases: [llm knowledge base, ai wiki, personal knowledge compiler]
sources: [karpathy-llm-knowledge-bases, karpathy-llm-wiki-gist]
related_concepts: [rag-vs-wiki, agentic-ai]
related_entities: [andrej-karpathy]
last_updated: 2026-05-14
---

# LLM Wiki

A pattern for building personal knowledge bases using LLMs as compilers and maintainers. Rather than retrieving from raw documents at query time ([[concepts/rag-vs-wiki|RAG]]), the LLM incrementally builds and maintains a persistent, interlinked wiki that sits between the user and raw sources.

## Core idea

The key insight is that the expensive part of knowledge management is not reading or thinking — it's the bookkeeping: updating cross-references, keeping summaries current, noting contradictions, maintaining consistency. Humans abandon wikis because the maintenance burden grows faster than the value. LLMs don't get bored and can touch 15 files in one pass.

**The wiki is a persistent, compounding artifact.** Cross-references are already there. Contradictions have already been flagged. Synthesis already reflects everything read so far. Every source added and every question asked makes it richer.

## Architecture

Three layers:

| Layer | Description | Ownership |
|---|---|---|
| Raw sources | Immutable documents (articles, papers, images, data) | User curates; never modified |
| The wiki | Structured, interlinked markdown files | LLM writes and maintains |
| The schema | `CLAUDE.md` / `AGENTS.md` — operating rules for the LLM | Co-evolved by user + LLM |

## Operations

### Ingest
Drop a new source → LLM reads it → extracts key info → integrates into existing wiki (updating entity pages, concept pages, noting contradictions, strengthening synthesis). A single source may touch 10–15 wiki pages.

### Query
Ask questions → LLM reads index → drills into relevant pages → synthesizes answer with citations → valuable answers filed back as new wiki pages. Explorations compound just like ingested sources.

### Lint
Periodic health check: find contradictions, stale claims, orphan pages, missing cross-references, concepts mentioned but lacking pages. Suggest new sources to investigate.

## Scale and indexing

At moderate scale (~100 sources, hundreds of pages), a well-maintained `index.md` is sufficient for the LLM to navigate without vector search or RAG infrastructure. The LLM reads the index first, then drills into relevant pages.

Adapted from [[entities/andrej-karpathy|Karpathy]]'s system: his wiki at ~100 articles and ~400,000 words works without RAG because it is well-organized and indexed.

## Human vs. LLM roles

| Human | LLM |
|---|---|
| Curate sources | Write summaries |
| Direct analysis | Maintain cross-references |
| Ask questions | File answers back into wiki |
| Read the wiki | Flag contradictions |
| Evolve the schema | Update all touched pages on ingest |

## Toolchain (Karpathy's)

- **Obsidian Web Clipper** — saves web articles as markdown
- **Obsidian** — IDE / viewer (graph view, Dataview, Marp plugin)
- **Claude Code / similar** — the LLM agent that writes the wiki
- **Marp** — markdown → slide decks
- **Custom CLI search** — LLM-callable search over wiki files

## Output formats

The LLM can produce output beyond plain text:
- Markdown pages (filed into wiki)
- Marp slide decks
- Matplotlib charts (via code execution)
- Comparison tables
- Canvases

## Application domains

From [[sources/karpathy-llm-wiki-gist|Karpathy's gist]], the pattern applies to any domain where knowledge accumulates over time:

| Domain | Description |
|---|---|
| Personal | Goals, health, psychology — filing journal entries, articles, podcast notes |
| Research | Deep-diving a topic over weeks/months |
| Reading | Filing each book chapter, building pages for characters/themes/plot |
| Business/team | Internal wiki fed by Slack threads, meeting notes, customer calls |
| Other | Competitive analysis, due diligence, trip planning, course notes |

The fan wiki analogy: "Think of fan wikis like Tolkien Gateway — thousands of interlinked pages built by volunteers over years. You could build something like that personally as you read, with the LLM doing all the cross-referencing and maintenance."

## The schema layer

The schema (`CLAUDE.md` / `AGENTS.md`) is what separates a disciplined wiki maintainer from a generic chatbot. It communicates structure, conventions, and workflows to the LLM. Karpathy recommends co-evolving it over time as you discover what works for your domain. This vault's schema is in `CLAUDE.md`.

## CLI tools at scale

At moderate scale the index file is sufficient for navigation. Beyond that, Karpathy recommends [qmd](https://github.com/tobi/qmd): on-device markdown search with hybrid BM25/vector search + LLM re-ranking. Available as both CLI (shellable by the agent) and MCP server (native tool). Simpler custom search scripts are also viable.

## Tips and tricks

- **Obsidian Web Clipper**: Browser extension that converts web articles to markdown
- **Image handling**: Download images locally to `raw/assets/`; LLM reads text first, then views images separately (can't do both in one pass — known limitation)
- **Marp**: Markdown → slide decks (Obsidian plugin)
- **Dataview**: Queries YAML frontmatter to generate dynamic tables/lists
- **Graph view**: Visual map of the wiki — shows hubs, orphans, clusters
- **Git**: Built-in version history, branching, and collaboration

## Future direction

[[entities/andrej-karpathy|Karpathy]]'s stated next step: **fine-tuning** a model on the wiki so the knowledge is baked into model weights rather than retrieved at query time. This would make the model an expert on the research domain without needing to read the notes.

## Relationship to Vannevar Bush's Memex

The LLM Wiki is spiritually close to Bush's 1945 Memex — a private, curated knowledge store with associative trails between documents. Bush's unsolved problem was maintenance. The LLM solves that.

> "The part he couldn't solve was who does the maintenance. The LLM handles that." — [[sources/karpathy-llm-wiki-gist]]

## Related pages

- [[concepts/rag-vs-wiki]] — why this differs from standard RAG
- [[concepts/agentic-ai]] — LLM agents as the engine behind this pattern
- [[entities/andrej-karpathy]] — originator of this workflow
