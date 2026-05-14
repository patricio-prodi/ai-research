---
type: source
title: "LLM Wiki"
article: "raw/llm-wiki.md"
source_url: "https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f"
author: "[[Andrej Karpathy]]"
published: 2026-04-01
ingested: 2026-05-14
tags: [knowledge-management, llm-workflow, obsidian, rag, wiki, architecture]
key_concepts: [llm-wiki, rag-vs-wiki]
---

# LLM Wiki

> Source: [GitHub Gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) by [[entities/andrej-karpathy|Andrej Karpathy]] | Published 2026-04-01

## Overview

The primary source for the [[concepts/llm-wiki|LLM Wiki]] pattern. This is Karpathy's own gist — an "idea file" designed to be copy-pasted to an LLM agent so it can instantiate the pattern for you. Describes the full architecture, operations, and philosophy in first-person. More detailed and authoritative than [[sources/karpathy-llm-knowledge-bases]], which was a secondhand summary.

The document is intentionally abstract — it communicates the pattern, not a specific implementation. Directory structure, schema conventions, page formats, and tooling are left to the user + LLM to co-design.

## Key claims

1. **The core problem with RAG**: "The LLM is rediscovering knowledge from scratch on every question. There's no accumulation." Subtle multi-document synthesis must be re-derived on every query. NotebookLM, ChatGPT file uploads, and most RAG systems work this way.

2. **The wiki as a compiled artifact**: The LLM "reads it, extracts the key information, and integrates it into the existing wiki — updating entity pages, revising topic summaries, noting where new data contradicts old claims." Knowledge is compiled once and kept current.

3. **Three-layer architecture**: Raw sources (immutable), the wiki (LLM-owned markdown), and the schema (`CLAUDE.md`/`AGENTS.md`) that governs LLM behavior. The schema is co-evolved by user and LLM over time.

4. **Answers can be filed back**: "Good answers can be filed back into the wiki as new pages. A comparison you asked for, an analysis, a connection you discovered — these are valuable and shouldn't disappear into chat history."

5. **index.md and log.md are special**: index.md is content-oriented (catalog); log.md is chronological (append-only record). Together they allow LLM navigation without vector search infrastructure.

6. **Scale limit acknowledged**: Works well at moderate scale (~100 sources, ~hundreds of pages). Beyond that, dedicated search tools like qmd are recommended.

7. **Vannevar Bush's Memex**: The pattern is spiritually close to Bush's 1945 vision of a private, curated knowledge store with associative trails. "The part he couldn't solve was who does the maintenance. The LLM handles that."

## Application domains

| Domain | Description |
|---|---|
| Personal | Goals, health, psychology — filing journal entries, articles, podcast notes |
| Research | Going deep on a topic over weeks/months — papers, articles, reports |
| Reading a book | Filing each chapter, building pages for characters/themes/plot threads |
| Business/team | Internal wiki fed by Slack threads, meeting transcripts, customer calls |
| Other | Competitive analysis, due diligence, trip planning, course notes, hobby deep-dives |

## Architecture detail

**Raw sources**: Immutable. LLM reads but never modifies. Source of truth.

**The wiki**: LLM creates, updates, cross-references, and maintains consistency. User reads; LLM writes.

**The schema**: The key configuration file. "It's what makes the LLM a disciplined wiki maintainer rather than a generic chatbot." Karpathy recommends co-evolving this with the LLM as you figure out what works for your domain.

## Operations detail

### Ingest
"Personally I prefer to ingest sources one at a time and stay involved — I read the summaries, check the updates, and guide the LLM on what to emphasize." Batch ingestion possible but less controlled.

### Query
Output formats beyond text: markdown pages, comparison tables, Marp slide decks, Matplotlib charts, canvases. Valuable answers should be filed back into the wiki.

### Lint
Periodically scan for: contradictions, stale claims, orphan pages, missing cross-references, data gaps fillable by web search. "The LLM is good at suggesting new questions to investigate and new sources to look for."

## CLI tools

At scale, a search engine over wiki pages becomes useful. Karpathy recommends [qmd](https://github.com/tobi/qmd):
- Local, on-device markdown search with hybrid BM25/vector search + LLM re-ranking
- Both CLI (shellable by LLM) and MCP server (native tool) interfaces

## Tips and tricks

- **Obsidian Web Clipper**: Browser extension → converts web articles to markdown for raw collection
- **Image handling**: Obsidian can download all images locally to `raw/assets/` via hotkey. LLM reads markdown text first, then views referenced images separately (current limitation: can't do both in one pass)
- **Graph view**: Best way to see wiki shape — hubs, orphans, clusters
- **Marp**: Markdown → slide decks (Obsidian plugin)
- **Dataview**: Obsidian plugin querying page frontmatter — generates dynamic tables/lists if LLM adds YAML metadata
- **Git**: "The wiki is just a git repo of markdown files. You get version history, branching, and collaboration for free."

## Quotes

> "The human's job is to curate sources, direct the analysis, ask good questions, and think about what it all means. The LLM's job is everything else."

> "In practice, I have the LLM agent open on one side and Obsidian open on the other. The LLM makes edits based on our conversation, and I browse the results in real time — following links, checking the graph view, reading the updated pages. Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase."

> "The tedious part of maintaining a knowledge base is not the reading or the thinking — it's the bookkeeping. Updating cross-references, keeping summaries current, noting when new data contradicts old claims, maintaining consistency across dozens of pages. Humans abandon wikis because the maintenance burden grows faster than the value."

## Implications

- This is the canonical source for the LLM Wiki pattern — more authoritative than secondhand accounts
- The schema layer (`CLAUDE.md`) is not just configuration but the mechanism that makes the LLM disciplined vs. generic
- Filing query answers back into the wiki is an underemphasized workflow — explorations should compound
- The intentionally abstract design means this gist can seed any LLM wiki in any domain

## Related pages

- [[concepts/llm-wiki]] — the full concept derived from this source
- [[concepts/rag-vs-wiki]] — RAG vs. wiki comparison
- [[entities/andrej-karpathy]] — author
- [[sources/karpathy-llm-knowledge-bases]] — secondhand explanation of the same pattern
