# AI Research Wiki — Schema

You are the maintainer of this LLM wiki. This vault is a personal knowledge base for AI research. You write and maintain the wiki; the user reads it, curates sources, and directs the analysis.

---

## Directory layout

```
ai-research/
├── CLAUDE.md              ← this file (schema + operating rules)
├── articles/              ← raw sources (READ ONLY — never modify)
├── wiki/
│   ├── index.md           ← content catalog (update on every ingest)
│   ├── log.md             ← append-only chronological log
│   ├── sources/           ← one summary page per article
│   ├── concepts/          ← ideas, techniques, frameworks, methods
│   ├── entities/          ← people, companies, organizations, products
│   └── topics/            ← broader synthesis across multiple sources
└── wip/                   ← scratch space (not part of the wiki)
```

**articles/** is the source of truth. Never edit files there. The wiki is built from them.

---

## Frontmatter conventions

Every wiki page starts with YAML frontmatter. Use the appropriate template:

### Source page (`wiki/sources/`)
```yaml
---
type: source
title: "Full article title"
article: "articles/Exact Filename.md"
source_url: "https://..."
author: "Name or [[Entity Name]]"
published: YYYY-MM-DD
ingested: YYYY-MM-DD
tags: [tag1, tag2]
key_concepts: [concept-slug, concept-slug]
---
```

### Concept page (`wiki/concepts/`)
```yaml
---
type: concept
title: "Concept Name"
aliases: [alt name, alt name]
sources: [source-slug, source-slug]
related_concepts: [concept-slug, concept-slug]
related_entities: [entity-slug]
last_updated: YYYY-MM-DD
---
```

### Entity page (`wiki/entities/`)
```yaml
---
type: entity
name: "Full Name"
kind: person | org | company | product | lab
aliases: [short name]
sources: [source-slug]
related_concepts: [concept-slug]
last_updated: YYYY-MM-DD
---
```

### Topic page (`wiki/topics/`)
```yaml
---
type: topic
title: "Topic Title"
sources: [source-slug, source-slug]
key_concepts: [concept-slug]
last_updated: YYYY-MM-DD
---
```

---

## Linking conventions

- Use `[[Page Title]]` Obsidian-style wikilinks for internal links.
- Always link on first mention of a concept, entity, or source in any page.
- Source pages link to `articles/Filename.md` via `article:` frontmatter field and inline link in the body.
- Concept and entity slugs are lowercase-hyphenated (e.g. `agentic-ai`, `andrej-karpathy`).
- File names match slugs: `wiki/concepts/agentic-ai.md`, `wiki/entities/andrej-karpathy.md`.

---

## Naming conventions

| Category | Pattern | Example |
|---|---|---|
| Source | `{author-or-topic}-{short-title}.md` | `karpathy-llm-knowledge-bases.md` |
| Concept | `{concept-name}.md` | `agentic-ai.md` |
| Entity | `{entity-name}.md` | `andrej-karpathy.md` |
| Topic | `{topic-name}.md` | `ai-forecasting.md` |

---

## Operations

### INGEST (adding a new source)

When the user says "ingest or process [article]":

1. Read the article fully.
2. Discuss key takeaways with the user if they want (optional).
3. Create `wiki/sources/{slug}.md` with a structured summary: overview, key claims, evidence/data, implications, quotes.
4. Update `wiki/index.md`: add the new source to the Sources section.
5. For each key concept in the article:
   - If a concept page exists: update it with new evidence, quotes, or contradictions.
   - If it doesn't exist: create `wiki/concepts/{slug}.md`.
6. For each key entity (person, org, company) in the article:
   - If an entity page exists: add new info, update source list.
   - If it doesn't exist: create `wiki/entities/{slug}.md`.
7. If the article contributes to a topic synthesis: update or create the relevant `wiki/topics/` page.
8. Mark the raw file as ingested by running:
   ```
   python3 scripts/mark_ingested.py "raw/filename.md"
   ```
   This is the **only** allowed write operation on the `raw/` folder. Do not edit raw files directly.
9. Append an entry to `wiki/log.md`:
   ```
   ## [YYYY-MM-DD] ingest | Article Title
   - Source page: [[sources/slug]]
   - Pages created: list
   - Pages updated: list
   ```

A single ingest typically touches 5–15 wiki pages.

### QUERY (answering questions)

When the user asks a question:

1. Read `wiki/index.md` to identify relevant pages.
2. Read the relevant wiki pages (not raw articles — use the wiki).
3. Synthesize an answer with inline citations linking to wiki pages.
4. If the answer is substantive and reusable, offer to save it as a new `wiki/topics/` or `wiki/concepts/` page.
5. Append a log entry:
   ```
   ## [YYYY-MM-DD] query | Question summary
   - Pages consulted: list
   - Output filed: [[topics/slug]] or none
   ```

### LINT (health check)

When the user says "lint the wiki":

1. Scan all wiki pages for:
   - Contradictions between pages
   - Stale claims superseded by newer sources
   - Orphan pages (no inbound links from other wiki pages)
   - Concepts mentioned but lacking their own page
   - Missing cross-references
   - Frontmatter with empty required fields
2. Produce a lint report listing issues by severity.
3. Fix issues the user approves.
4. Append a log entry:
   ```
   ## [YYYY-MM-DD] lint | Wiki health check
   - Issues found: N
   - Fixed: list
   - Deferred: list
   ```

---

## Content quality rules

- **Source pages**: Focus on what the article actually says. Attribute claims. Note methodology, data quality, author credibility.
- **Concept pages**: Define the concept clearly. Show how different sources agree or disagree. Track how the concept evolves across sources.
- **Entity pages**: Stick to facts. Note roles, affiliations, relevant contributions. Link to sources.
- **Topic pages**: These are synthesis — write a thesis, not just a list. State what you (the wiki, based on the sources) believe and why.
- **Flag contradictions explicitly**: When two sources disagree, note it with a `> **Contradiction:** ...` blockquote in both pages.
- **Do not hallucinate**: If a claim isn't in a source, don't write it. Use `[citation needed]` for gaps to fill later.

---

## index.md structure

```markdown
# Wiki Index

_Last updated: YYYY-MM-DD — N sources, M pages_

## Sources
| Slug | Title | Date | Tags |
|---|---|---|---|

## Concepts
| Slug | Title | Summary |
|---|---|---|

## Entities
| Slug | Name | Kind |
|---|---|---|

## Topics
| Slug | Title | Sources |
|---|---|---|
```

---

## log.md structure

Each entry uses a consistent prefix so it's greppable:
```
## [YYYY-MM-DD] {operation} | {title}
```

Operations: `ingest`, `query`, `lint`, `update`, `init`

---

## Reminders

- You write the wiki. The user reads it.
- Never edit `articles/`. It's the immutable source of truth.
- Keep `index.md` and `log.md` always current.
- When in doubt about how to classify something, ask the user.
- Prefer updating existing pages over creating new ones for minor additions.
- The wiki should be usable in Obsidian — test that wikilinks are valid.
