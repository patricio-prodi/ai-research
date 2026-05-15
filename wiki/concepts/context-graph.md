---
type: concept
title: "Context Graph"
aliases: [context graph, decision context graph, decision lineage graph]
sources: [foundation-capital-context-graphs]
related_concepts: [decision-trace, systems-of-record, systems-of-agents, agentic-ai, knowledge-ontology]
related_entities: []
last_updated: 2026-05-15
---

# Context Graph

A **living record of [[concepts/decision-trace|decision traces]] stitched across entities and time so precedent becomes searchable.** Proposed by Foundation Capital in [[sources/foundation-capital-context-graphs|"AI’s trillion-dollar opportunity: Context graphs"]] as the structural asset that defines the next generation of enterprise systems of record.

> "Not 'the model’s chain-of-thought,' but a living record of decision traces stitched across entities and time so precedent becomes searchable." — Foundation Capital (2025)

## What It Is — and What It Isn’t

A context graph is **not**:
- A model’s internal chain-of-thought (transient, opaque)
- A log file (unstructured, not linked to business entities)
- A data warehouse (read path, post-decision, no rationale)
- A knowledge base of *rules* (general, not case-specific)

A context graph **is**:
- A graph whose **nodes** are the business entities the enterprise already cares about — accounts, renewals, tickets, incidents, policies, approvers, agent runs
- Whose **edges** are decision events: the moments where context turned into action
- And whose **payload** on each edge is the *"why" link* — what inputs were gathered, what policy was evaluated, what exception route was invoked, who approved, and what state was written

## Why It Compounds

The feedback loop is the key property:

1. Captured [[concepts/decision-trace|decision traces]] become searchable precedent.
2. Every automated decision adds another trace to the graph.
3. Similar cases can now be resolved by reference to prior decisions, increasing automation coverage.
4. Even when a human still makes the call, the workflow layer captures the inputs, approval, and rationale as durable precedent.

Each new decision both *uses* and *enriches* the graph. This is why Foundation Capital frames it as a structural advantage rather than a feature: incumbents that are not in the execution path cannot generate this loop.

## Why Incumbents Can’t Build It

The argument from [[sources/foundation-capital-context-graphs|Foundation Capital (2025)]]:

| Incumbent type | Architectural limitation | Why context graph is blocked |
|---|---|---|
| [[concepts/systems-of-record\|Systems of record]] (Salesforce, ServiceNow, Workday) | Current-state storage; siloed | Can’t replay state at decision time; can’t see cross-system synthesis |
| Data warehouses (Snowflake, Databricks) | Read path, post-ETL | Decision context is gone by the time data lands |
| Bolted-on AI (Agentforce, Now Assist) | Inherits parent’s blind spots | No cross-system view at commit time |

The point isn’t that incumbents can’t add AI features — they can. It’s that **capturing decision traces requires being in the execution path at commit time**, and incumbents are not.

## Where Context Graphs Get Built

[[concepts/systems-of-agents|Systems of agents]] startups sit *in the orchestration path*. When an agent triages an escalation, responds to an incident, or decides on a discount, it pulls context from multiple systems, evaluates rules, resolves conflicts, and acts. Because the orchestration layer is *executing* the workflow, it can capture context at decision time — as a first-class record — rather than reconstructing it via ETL.

PlayerZero is named as the canonical example: starting from L2/L3 production-engineering support, the asset isn’t the automation but **the context graph it accumulates**: a living model of how code, config, infrastructure, and customer behavior interact in reality — answering "why did this break?" and "will this change break production?"

## Practical Example (Renewal Agent)

A renewal agent proposes a 20% discount:

| Step | What happens | What the context graph captures |
|---|---|---|
| 1 | Policy caps renewals at 10% unless service-impact exception | Policy version + clause |
| 2 | Agent pulls three SEV-1 incidents from PagerDuty | Cross-system inputs |
| 3 | Agent reads open Zendesk "cancel unless fixed" escalation | Customer state |
| 4 | Agent finds prior renewal where VP approved similar exception | Precedent edge |
| 5 | Routes exception to Finance | Approval chain |
| 6 | Finance approves | Approver identity + reasoning |
| 7 | CRM writes "20% discount" | Final state |

The CRM ends up with **one fact**: "20% discount." The context graph ends up with **seven linked records** explaining why.

## Relationship to Adjacent Concepts

### vs. [[concepts/knowledge-ontology|Knowledge Ontology]]
[[entities/lassaad-gaiji|Gaiji]]’s pipeline extracts *rules* from documents into a structured KB at ingest time. The context graph captures *application of rules* — case-level decisions — at execution time. They are complementary halves of the same architectural shift away from RAG-shaped retrieval toward structured, queryable agent context:

| Dimension | Knowledge Ontology | Context Graph |
|---|---|---|
| What it captures | Rules and policies | Specific decisions applying rules |
| When | At document ingest | At decision execution time |
| Source | Documents and policies | Agent orchestration layer |
| Use | Agent reasons from KB | Agent reasons from precedent |

### vs. [[concepts/llm-wiki|LLM Wiki]]
Both are structured-knowledge artifacts maintained by AI. The LLM wiki captures *human-curated synthesis* of external sources. The context graph captures *machine-witnessed traces* of internal decisions.

### vs. [[concepts/agentic-ai|Agentic AI]] generally
Agentic AI is the *capability*. The context graph is the *byproduct that becomes the moat*. Foundation Capital’s thesis is that the byproduct is more valuable than the labor automation.

## Open Questions

- **Governance and privacy**: capturing why every decision was made includes capturing *who decided* and *based on what reasoning* — what regulatory regime governs this? `[citation needed]`
- **Schema portability**: if a context graph lives inside a startup’s orchestration layer, what happens on acquisition or vendor switch? `[citation needed]`
- **Replayability**: how is "state at decision time" reconstructed when upstream systems mutate? `[citation needed]`
- **Scale**: at what trace volume does the graph itself need its own retrieval / indexing layer? `[citation needed]`

## Related Pages

- [[concepts/decision-trace]] — the unit
- [[concepts/systems-of-agents]] — the architectural location where the graph is captured
- [[concepts/systems-of-record]] — the category the graph displaces
- [[concepts/knowledge-ontology]] — adjacent structured-knowledge pattern
- [[concepts/agentic-ai]] — the enabling technology
- [[sources/foundation-capital-context-graphs]] — primary source (Foundation Capital)
