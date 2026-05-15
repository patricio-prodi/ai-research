---
type: source
title: "AI’s trillion-dollar opportunity: Context graphs"
article: "raw/AI’s trillion-dollar opportunity Context graphs.md"
source_url: "https://foundationcapital.com/ideas/context-graphs-ais-trillion-dollar-opportunity"
author: "Foundation Capital"
published: 2025-12-22
ingested: 2026-05-15
tags: [enterprise-ai, systems-of-record, context-graph, agentic-ai, vc-thesis, decision-trace]
key_concepts: [context-graph, decision-trace, systems-of-record, systems-of-agents, agentic-ai]
---

# AI’s trillion-dollar opportunity: Context graphs

[Article](raw/AI’s%20trillion-dollar%20opportunity%20Context%20graphs.md) published 2025-12-22 by Foundation Capital.

## Overview

A VC thesis arguing that the next trillion-dollar enterprise platforms will not be the existing [[concepts/systems-of-record|systems of record]] (Salesforce, Workday, SAP) extended with AI, nor the data warehouses (Snowflake, Databricks) repositioned as "truth registries." Instead, they will be **[[concepts/systems-of-agents|systems of agents]]** that sit in the execution path and persist [[concepts/decision-trace|decision traces]] — the inputs, policies, exceptions, approvers, and rationale that justified each action. Aggregated over time, those traces form a **[[concepts/context-graph|context graph]]**: a queryable record of *why* the business did what it did. This, the post argues, is the structural advantage incumbents cannot replicate.

The piece is explicitly framed as a rebuttal/extension of Jamin Ball’s "[Long Live Systems of Record](https://cloudedjudgement.substack.com/p/clouded-judgement-121225-long-live)" — which contends that incumbents survive the agent transition by becoming better governed canonical sources. Foundation Capital agrees agents need canonical data, but argues Ball’s frame ignores the layer that "actually runs enterprises": the decision traces currently buried in Slack threads, deal desks, escalation calls, and people’s heads.

## Key Claims

- **Rules ≠ decision traces.** Rules tell an agent *what should happen in general* ("use official ARR for reporting"). Decision traces capture *what happened in this specific case* ("we used X definition, under policy v3.2, with a VP exception, based on precedent Z, and here’s what we changed"). Agents need both, but only one is currently captured by enterprise software.
- **The missing layer is decision traces, not data.** The wall agents hit when shipping into real workflows isn’t missing or dirty data — it’s missing *reasoning artifacts*: exception logic in people’s heads, precedent from past decisions, cross-system synthesis, and approval chains that happen on Zoom and Slack.
- **Systems of agents have a structural advantage: they sit in the execution path.** They see what inputs were gathered across systems, what policies were evaluated, what exception route was invoked, who approved, and what state was written — at the moment of decision, not after the fact via ETL.
- **Incumbents are structurally blocked from capturing this.** Operational systems (Salesforce, ServiceNow, Workday) are siloed and prioritize *current state*, not state at decision time. Data warehouses (Snowflake, Databricks) are in the *read* path, after decisions are made.
- **Context graphs compound.** Every automated decision adds a trace; every trace becomes searchable precedent. Even when a human still makes the call, the workflow layer captures inputs, approvals, and rationale as durable precedent rather than letting them die in Slack.
- **Three startup paths.** (1) Replace systems of record outright at transition moments (Regie vs. Outreach/Salesloft). (2) Replace modules and become the system of record for a sub-workflow while syncing final state back to the incumbent (Maximor in finance). (3) Start as an orchestration layer and let the persisted decision lineage become the authoritative artifact (PlayerZero in production engineering).
- **Observability for agents will be critical infrastructure.** As traces accumulate, enterprises will need monitoring, debugging, and evaluation — Foundation positions Arize as the "Datadog for agent decision quality."
- **Signals for founders.** (a) High headcount on a workflow → decision logic too complex for traditional tooling. (b) Exception-heavy decisions (deal desks, underwriting, compliance) → precedent matters. (c) Org-chart "glue functions" (RevOps, DevOps, SecOps) → tells where no single system of record owns the cross-functional workflow.

## Evidence / Data

This is a **thesis essay**, not an empirical paper. No surveys, benchmarks, or quantitative claims. Evidence is illustrative:

- **Concrete examples** of context loss: discount approved on a Zoom call (CRM shows final price, not who approved or why); support escalation depending on CRM tier + Zendesk history + PagerDuty outages + Slack churn-risk thread (ticket only says "escalated to Tier 3").
- **Worked example**: renewal agent proposes 20% discount; policy caps at 10% absent service-impact exception; agent pulls SEV-1 incidents from PagerDuty, escalation from Zendesk, prior VP-approved precedent; routes to Finance; Finance approves. The CRM ends up with one fact: "20% discount."
- **Portfolio mapping** to the three paths: Regie (replacement of AI SDR platform), Maximor (finance modules), PlayerZero (orchestration in production engineering), Arize (observability).

The piece names competitors’ AI bets — Agentforce (Salesforce), Now Assist (ServiceNow), Workday agents, Cortex/Streamlit acquisition (Snowflake), Neon acquisition, Lakebase, AgentBricks (Databricks) — and argues why each inherits architectural blind spots from their parent platform.

## Implications

- **For founders**: build where decision context is currently uncaptured (Slack threads, deal desks, escalation calls). Target high-headcount, exception-heavy workflows. Start human-in-the-loop; let the graph compound.
- **For incumbents**: governance retrofits and warehouse repositioning will not produce a context graph. The orchestration path is where decision context is born, and incumbents are not in it. Their countermeasures (acquisitions, egress fees, ecosystem lock-in) make extraction expensive but don’t insert them into orchestration.
- **For the agentic AI thesis broadly**: this reframes the value proposition of [[concepts/agentic-ai|agentic AI]]. Agents aren’t just labor-cost automation; they are *capture devices* for a category of business truth — *why decisions were made* — that has never been systematically stored.
- **Connection to [[concepts/knowledge-ontology|knowledge ontology]]**: Gaiji’s extraction pipeline compiles *rules* from documents into a structured KB. Foundation Capital’s thesis is about capturing *decision traces* — the case-level application of rules — at execution time. Both push back on the same RAG-shaped gap: that retrieval isn’t enough; the agent needs structured, queryable context.

## Quotes

> "Rules tell an agent *what should happen in general* ('use official ARR for reporting'). Decision traces capture *what happened in this specific case* ('we used X definition, under policy v3.2, with a VP exception, based on precedent Z, and here’s what we changed')."

> "We call the accumulated structure formed by those traces a **context graph**: not 'the model’s chain-of-thought,' but a living record of decision traces stitched across entities and time so precedent becomes searchable."

> "This is what 'never captured' means. Not that the data is dirty or siloed, but that the reasoning connecting data to action was never treated as data in the first place."

> "By the time data lands in Snowflake, the decision context is gone. A system that only sees reads, after the fact, can’t be the system of record for decision lineage. It can tell you what happened, but it can’t tell you why."

> "Incumbents can make extraction harder, but they can’t insert themselves into an orchestration layer they were never part of."

> "The question isn’t whether systems of record survive — they will. The question is whether the next trillion-dollar platforms are built by adding AI to existing data, or by capturing the decision traces that make data actionable."

## Author Credibility

Published on Foundation Capital’s "Ideas" blog. Foundation Capital is an early-stage VC firm; this is explicitly a **portfolio-aligned thesis** — three of the four startups named (Regie, Maximor, PlayerZero, Arize) appear to be portfolio companies or aligned founders. The piece should be read as a fund’s framing of an investment area, not a neutral analyst’s assessment.

- **Strengths**: clear architectural argument; useful taxonomy (rules vs. decision traces, three startup paths, founder signals); explicit engagement with a strong counter-thesis (Jamin Ball’s).
- **Weaknesses**: no empirical evidence of enterprise demand for "decision lineage" as a category; assumes orchestration-layer startups will retain their position rather than being acquired or commoditized; doesn’t address the regulatory / privacy implications of capturing decision rationale at scale.

## Related Pages

- [[concepts/context-graph]] — central concept
- [[concepts/decision-trace]] — the unit that aggregates into a context graph
- [[concepts/systems-of-record]] — the category being reframed
- [[concepts/systems-of-agents]] — the proposed new category
- [[concepts/agentic-ai]] — the underlying technology
- [[concepts/knowledge-ontology]] — adjacent pattern: structured knowledge extraction
- [[topics/agentic-systems]] — broader synthesis
