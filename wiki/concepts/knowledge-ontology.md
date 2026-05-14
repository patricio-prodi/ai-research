---
type: concept
title: "Knowledge Ontology (Structured Extraction Pipeline)"
aliases: [knowledge ontology, structured knowledge extraction, extraction pipeline, knowledge base pipeline]
sources: [gaiji-beyond-rag]
related_concepts: [rag-vs-wiki, llm-wiki, mcp-server, agentic-ai]
related_entities: [lassaad-gaiji]
last_updated: 2026-05-14
---

# Knowledge Ontology (Structured Extraction Pipeline)

A pattern for converting unstructured documents into a structured, queryable knowledge base by running a multi-agent extraction pipeline at ingest time. Proposed by [[entities/lassaad-gaiji|Lassaad Gaiji]] in [[sources/gaiji-beyond-rag|"Beyond RAG"]].

## The Core Problem It Solves

[[concepts/rag-vs-wiki|RAG]] retrieves the most semantically similar chunks — but chunks are context-free fragments. A business rule may span two chunks, sit under a truncated heading, and share vector space with an unrelated paragraph. This is fine for Q&A. It breaks when an AI agent needs to *apply* rules consistently and be auditable.

The extraction pipeline compiles structured knowledge *once at ingest time*, so the LLM reasons from curated rules rather than hoping the right chunk scored highest.

## The Dual Pipeline

Two pipelines run in parallel on the same documents:

| Pipeline | Unit | Purpose |
|---|---|---|
| RAG | Chunks + embeddings | Semantic Q&A lookup |
| Extraction | Full pages + ontology rows | Structured knowledge base for agent reasoning |

Both are exposed via an [[concepts/mcp-server|MCP toolbox]], giving the LLM access to both routes.

## Extraction Pipeline Steps

### 1. Parse at Section Level
Full document pages are stored in a `DOCUMENT_PAGE` table — separate from the `DOCUMENT_CHUNK` table used for RAG. This preserves the structural context that chunking destroys.

### 2. Extract in Parallel
Each section is sent to the **extraction agent** with a targeted prompt: *identify and structure the rules, policies, constraints, and processes embedded in this content.* Extraction runs across sections in parallel. The agent classifies each entry:
- **Topic** — e.g., "refund policy", "onboarding"
- **Category** — `rule`, `policy`, `constraint`, `process`
- **Confidence** — `high`, `medium`, `low`

> Defining topics and categories *upfront* (injecting a domain-specific list into the extraction prompt) is critical. Dynamic generation leads to inconsistent labelling across documents.

### 3. Store a Structured Ontology
Extracted entries are stored in `DOCUMENT_ONTOLOGY` — structured, queryable rows. A companion `DOCUMENT_ONTOLOGY_FLAG` table tracks quality issues.

### 4. Surface Contradictions and Gaps
The **consolidation agent** — which never sees raw source content — reviews all extracted ontology entries and flags:
- **Contradictions** — two entries that conflict
- **Gaps** — topics referenced but never fully specified
- **Ambiguities** — unclear intent

Every flag requires human review before the pipeline proceeds. This is the step [[concepts/rag-vs-wiki|RAG]] cannot replicate: it prevents an AI from "quietly applying two conflicting policies depending on which chunk happened to score highest."

### 5. Synthesize and Activate
The **synthesis agent** receives validated ontology entries and produces a clean, structured markdown document grouped by topic and category. Stored in `PARTY_KNOWLEDGE_BASE` with:
- Version number
- `is_active` flag (domain expert activates via UI)
- Cross-document conflict tracking (`PARTY_KNOWLEDGE_CONFLICT`)

## The Three Agents

Each agent is narrowly scoped — separating concerns keeps prompts focused and outputs predictable:

| Agent | Input | Output |
|---|---|---|
| Extraction | Raw document section | Classified ontology entries |
| Consolidation | All ontology entries (no raw source) | Contradiction/gap flags for human review |
| Synthesis | Validated ontology entries | Clean versioned markdown knowledge base |

## Living Knowledge Base

Every new source runs through the full pipeline. Crucially, the consolidation step checks the new source against the *existing* knowledge base — not just the new source in isolation. The synthesis supersedes the previous version. The KB grows sharper with every source.

> "It's not an append-only store of chunks, it's a living, curated representation of domain knowledge that gets sharper the more you feed it." — [[entities/lassaad-gaiji|Gaiji]]

## Relationship to the LLM Wiki

This pattern is a **database-driven implementation** of the same philosophy as [[concepts/llm-wiki|LLM Wiki]]: compile knowledge at ingest time, don't re-derive it at query time. The differences:

| Dimension | LLM Wiki | Knowledge Ontology |
|---|---|---|
| Storage | Markdown files (Obsidian) | Relational database tables |
| Structure | Wiki pages + wikilinks | Schema-enforced rows (topic, category, confidence) |
| Agent architecture | Single ingest session | Three specialized agents (extraction / consolidation / synthesis) |
| Human oversight | Wiki author reads and curates | Explicit approval gate between consolidation and synthesis |
| Versioning | Git | `version` + `is_active` fields in DB |
| Scale target | ~100s of sources | Potentially larger (async, parallel, queued) |

## When to Use

Especially valuable in domains where **consistency matters** — compliance, support, legal, ops — and where an AI agent must *act on* domain knowledge, not just answer questions about it.

## Related Pages

- [[concepts/rag-vs-wiki]] — the broader RAG vs. compiled knowledge debate
- [[concepts/llm-wiki]] — markdown-based variant of the same philosophy
- [[concepts/mcp-server]] — toolbox pattern for exposing both KB and RAG routes
- [[concepts/agentic-ai]] — multi-agent pipeline context
