---
title: "Beyond RAG: How to Make Your AI Actually Know Things"
source: "https://lassaadgaiji998726.substack.com/p/beyond-rag-how-to-make-your-ai-actually?utm_campaign=post&utm_medium=email&triedRedirect=true"
author:
  - "[[Lassaad Gaiji]]"
published: 2026-04-24
created: 2026-04-24
description: "A practical architecture for building AI that reasons from structured knowledge, not document chunks"
tags:
  - "raw"
---
Everyone reaches for RAG. You have documents, data feeds, or internal content you want an AI to reason about, so you chunk everything up, generate embeddings, throw it in a vector database, and call it a day. It works. Kind of.

But after building a system where an AI agent needed to *act* on knowledge from multiple data sources, not just answer questions about them, I hit a wall that RAG couldn’t climb. It forced me to rethink the whole approach.

![](https://substackcdn.com/image/fetch/$s_!gOyw!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3dcbad71-66b1-49e7-8925-8b83ab151096_1284x589.jpeg)

This is my cat, he doesn't know what a RAG is.

---

## What Is RAG?

RAG stands for Retrieval-Augmented Generation. The idea is straightforward: instead of relying solely on what an LLM was trained on, you give it access to your own data at query time. When a user asks a question, the system searches that data for the most relevant passages and injects them into the prompt, augmenting the model’s response with your content.

In practice it looks like this: you take your data sources (documents, databases, internal wikis, whatever), split the content into small chunks, convert each chunk into a vector embedding (a numerical representation of its meaning), and store everything in a vector database. When a question comes in, you convert it into an embedding too, find the chunks closest to it in vector space, and hand those to the LLM as context.

It’s a powerful pattern, and it’s become the default starting point for anyone building AI on top of data.

---

## The Problem with RAG

RAG is optimized for *retrieval*. That’s it. You ask a question, you get back the most semantically similar chunks, and you hope the answer is in there somewhere.

This works great for Q&A. It falls apart the moment you need your AI to *reason consistently* from the rules and policies embedded in your data.

Here’s the core issue: **chunks are context-free fragments**. A business rule or policy might span two chunks, sit under a heading that got cut off, and share a vector space with a completely unrelated paragraph. Your retrieval is working fine, your *understanding* of the data is broken.

The moment you need an agent that doesn’t just answer questions about your data, but *applies* its contents reliably across many requests, RAG starts showing its limits.

Those are fundamentally different problems.

---

## Two Pipelines, Two Purposes

The shift in thinking that unlocked everything was separating the pipeline into two distinct concerns:

![](https://substackcdn.com/image/fetch/$s_!JPvB!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F88093788-3730-4850-8140-0113da2f8d48_1302x1292.png)

The RAG pipeline stays. It’s still useful for direct Q&A lookups. But the extraction pipeline runs in parallel and produces something fundamentally different: a **structured knowledge base** of reusable rules and policies distilled from your data.

---

## How the Extraction Pipeline Works

### 1\. Parse at the Section Level

Chunking is the wrong unit for extraction. Rules, policies, and frameworks often span multiple paragraphs, splitting them into retrieval-optimized chunks destroys the context the LLM needs to understand them.

Instead, store full pages separately, preserving the structure the extraction step depends on:

```markup
CREATE TABLE DOCUMENT_PAGE (
  id          SERIAL PRIMARY KEY,
  document_id INTEGER REFERENCES DOCUMENT ON DELETE CASCADE,
  page_number INTEGER,
  page_text   TEXT
);
```

This sits alongside your chunks table, which handles the RAG side:

```markup
CREATE TABLE DOCUMENT_CHUNK (
  id              SERIAL PRIMARY KEY,
  document_id     INTEGER REFERENCES DOCUMENT ON DELETE CASCADE,
  chunk_id        INTEGER,
  page_number     INTEGER,
  section_title   TEXT,
  chunk_type      TEXT,
  chunk_index     INTEGER,
  overlap_text    TEXT,
  chunk_text      TEXT,
  chunk_embedding VECTOR(1536)
);
```

Two tables, two purposes.

### 2\. Extract in Parallel by Section

Each section is sent to the LLM with a targeted extraction prompt, not “answer a question”, but “identify and structure the rules, policies, and decision frameworks in this content.”

Running this in parallel keeps it fast even for large data sources.

### 3\. Store a Structured Ontology

The output isn’t raw text, it’s structured, queryable rows:

```markup
CREATE TABLE DOCUMENT_ONTOLOGY (
  id          SERIAL PRIMARY KEY,
  document_id INTEGER REFERENCES DOCUMENT ON DELETE CASCADE,
  page_number INTEGER,
  topic         TEXT,   -- e.g. "refund policy", "onboarding"
  category      TEXT,   -- "rule", "policy", "constraint", "process"
  content       TEXT,   -- the extracted ontology entry
  confidence    TEXT,   -- high / medium / low
  status      TEXT DEFAULT 'draft',
  created_at  TIMESTAMP DEFAULT NOW()
);
```

And a companion table to track quality issues flagged during consolidation:

```markup
CREATE TABLE DOCUMENT_ONTOLOGY_FLAG (
  id           SERIAL PRIMARY KEY,
  document_id  INTEGER REFERENCES DOCUMENT ON DELETE CASCADE,
  flag_type    TEXT,
  description  TEXT,
  ontology_ids INTEGER[],
  status       TEXT DEFAULT 'open',
  created_at   TIMESTAMP DEFAULT NOW()
);
```

### 4\. Surface Contradictions and Gaps

The consolidation step is handled by a dedicated **consolidation AI agent** that does something RAG never could: it looks across all extracted ontology entries and identifies conflicts (two rules that contradict each other) and gaps (topics referenced but never fully specified). These are flagged for human review before moving forward.

This is especially valuable in domains where consistency matters, compliance, support, legal, ops. Your AI shouldn’t quietly apply two conflicting policies depending on which chunk happened to score highest.

### 5\. Synthesise and Activate

Once consolidation is complete, a dedicated **synthesis AI agent** produces the clean, validated knowledge base. It reorganises all validated ontology entries into a structured markdown document, grouped by topic and category (rules, recommendations, processes), preserving every specific detail without adding or merging anything. The result is stored, versioned, and activated by the domain expert via UI:

```markup
CREATE TABLE PARTY_KNOWLEDGE_BASE (
  party_knowledge_base_id SERIAL PRIMARY KEY,
  party_id                INTEGER REFERENCES PARTY ON DELETE CASCADE,
  knowledge_base_domain_id TEXT REFERENCES KNOWLEDGE_BASE_DOMAIN,
  content                 TEXT,
  version                 INTEGER DEFAULT 1,
  is_active               BOOLEAN DEFAULT FALSE,
  created_at              TIMESTAMP DEFAULT NOW()
);
```

Conflicts detected across documents are tracked separately:

```markup
CREATE TABLE PARTY_KNOWLEDGE_CONFLICT (
  party_knowledge_conflict_id SERIAL PRIMARY KEY,
  party_id                    INTEGER REFERENCES PARTY ON DELETE CASCADE,
  document_id                 INTEGER REFERENCES DOCUMENT ON DELETE CASCADE,
  description                 TEXT,
  status                      TEXT DEFAULT 'open',
  created_at                  TIMESTAMP DEFAULT NOW()
);
```

This knowledge base is then exposed via an MCP toolbox alongside a semantic search tool, giving the LLM access to both routes: structured knowledge retrieval and vector-based Q&A.

---

## The Role of Prompts

Each AI agent in the pipeline has a distinct, narrowly scoped prompt. This is intentional, separating concerns across agents keeps each prompt focused and the outputs predictable.

The **extraction agent** is not asked to summarise or answer questions. Its sole job is to identify and structure the rules, policies, constraints, and processes embedded in a section of content. It classifies each entry by topic and category, and assigns a confidence level when the intent is ambiguous.

The **consolidation agent** never sees the raw source content. It works exclusively from the extracted ontology entries produced by the extraction agent. Its job is to look across the full set of entries and reason about consistency, flagging contradictions where two entries conflict, gaps where a topic is referenced but never fully defined, and ambiguities where the intent of a rule is unclear. Every flag it raises requires human review before the pipeline can proceed.

The **synthesis agent** receives the validated ontology entries and produces a clean, structured markdown document, the final knowledge base. It groups entries by topic and category, and rewrites each one as a clear, concise bullet point in professional language. It preserves all specific details. The output follows a consistent structure that makes the knowledge base immediately readable by domain experts and queryable by the LLM.

This separation means that at no point does a single agent carry too much responsibility. Each one does one thing well, and the human review step between consolidation and synthesis ensures that what reaches the knowledge base has been intentionally approved.

**A note on topics and categories.** The extraction agent can generate topics and categories dynamically, but this leads to inconsistent labelling across documents. The better approach is to define them upfront based on a specific domain, and inject them into the prompt, ensuring the knowledge base stays structured and consistent regardless of the source.

---

## The LLM Uses the Knowledge Base, Not Chunks

With both pipelines in place, the MCP toolbox exposes two things: a semantic search tool for Q&A lookups, and the structured knowledge base for reasoning. This toolbox can serve any consumer, a general-purpose LLM, or a domain-specific AI agent built on top of it. When a new request comes in:

1. Retrieve relevant ontology entries by topic (fast, structured lookup, no vector search needed)
2. Inject them into the system prompt as explicit rules
3. The LLM or domain-specific agent reasons *from* the knowledge base, not *through* a pile of chunks

The result is an AI that behaves predictably and consistently, because it’s working from a curated, structured knowledge base rather than hoping the right chunk showed up in the top-5 retrieval results.

---

## When RAG Is Enough (And When It Isn’t)

To be clear: RAG isn’t wrong. It’s just often applied to problems it wasn’t designed for.

If your users are asking questions *about* your data, RAG is great. If your AI needs to *act on* that knowledge, reliably, repeatedly, with human oversight, you need a knowledge base.

---

## Trigger It Asynchronously

The entire pipeline runs asynchronously via a message queue. Each step, extraction, consolidation, synthesis, is triggered by a message, decoupling the slow processing work from the fast request-handling path and making the pipeline resilient to failures at any stage.

---

## A Living Knowledge Base

This isn’t a one-time process. Every time a new data source is ingested, it goes through the same pipeline, parsing, extraction, consolidation. But crucially, the consolidation step doesn’t just look at the new source in isolation. It runs against the existing knowledge base, detecting contradictions and gaps across the full body of knowledge accumulated so far.

The result is a final synthesis that supersedes the previous version, reviewed, activated, and ready for the LLM or AI agents. The knowledge base evolves with every source, growing more complete and more consistent over time.

This is what separates it from a static RAG index. It’s not an append-only store of chunks, it’s a living, curated representation of domain knowledge that gets sharper the more you feed it.

---

## Wrapping Up

RAG is the right default for Q&A. But if you’re building an AI that needs to reason from domain knowledge, apply rules consistently, or be auditable by domain experts, you’re not building a search engine, you’re building a knowledge base. Those require different pipelines, different data models, and a different mental model.

The extra upfront investment pays off the moment your AI starts making decisions that actually need to be correct.

---

## Get in Touch

If this resonates with a problem you’re facing, or you’re curious whether this architecture fits your use case, I’d love to hear from you. Whether you’re exploring the concept or ready to build a prototype, feel free to reach out.

[https://www.linkedin.com/in/lassaadgaiji](https://www.linkedin.com/in/lassaadgaiji)

lassaad.gaiji@gmail.com