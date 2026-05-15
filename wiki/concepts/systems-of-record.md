---
type: concept
title: "Systems of Record"
aliases: [system of record, SoR, canonical systems]
sources: [foundation-capital-context-graphs]
related_concepts: [systems-of-agents, context-graph, decision-trace, agentic-ai]
related_entities: []
last_updated: 2026-05-15
---

# Systems of Record

The enterprise software pattern that **owns the canonical data, the workflow, and the lock-in for a category of business object**. Examples: Salesforce for customers, Workday for employees, SAP for operations. Collectively, this pattern created a trillion-dollar ecosystem.

> "Own the canonical data, own the workflow, own the lock-in." — [[sources/foundation-capital-context-graphs|Foundation Capital (2025)]]

This page tracks the **debate over whether systems of record survive the shift to AI agents**.

## The Two Positions

### Jamin Ball: "Long Live Systems of Record"

Jamin Ball’s "[Long Live Systems of Record](https://cloudedjudgement.substack.com/p/clouded-judgement-121225-long-live)" (cited in [[sources/foundation-capital-context-graphs|Foundation Capital, 2025]]) argues:

- Agents don’t replace systems of record; they raise the bar for what a good one looks like.
- Agents are cross-system and action-oriented. The UX of work is separating from the underlying data plane.
- Agents become the interface, but something still has to be canonical underneath.
- Warehouses (Snowflake, Databricks) become "truth registries"; CRMs become "state machines with APIs."
- The narrative is **evolution, not replacement**.

### Foundation Capital: Context Graphs Reframe the Question

Foundation Capital agrees agents need canonical data, but argues Ball’s frame ignores half the picture: the **[[concepts/decision-trace|decision traces]]** that show how rules were applied in the past, where exceptions were granted, who approved what, and which precedents govern reality.

The argument: incumbents are structurally blocked from capturing this layer.

| Incumbent type | Architecture | Blind spot |
|---|---|---|
| Operational SoRs (Salesforce, ServiceNow, Workday) | Current-state storage, siloed | Don’t preserve state at decision time; don’t see cross-system synthesis |
| Data warehouses (Snowflake, Databricks) | Read path, post-ETL | Receive data after decisions are made; can tell you *what* happened, not *why* |
| Bolted-on AI (Agentforce, Now Assist, Workday agents) | Inherit parent architecture | No cross-system view at commit time |

Foundation Capital’s conclusion:

> "The question isn’t whether systems of record survive — they will. The question is whether the next trillion-dollar platforms are built by adding AI to existing data, or by capturing the decision traces that make data actionable."

The implication: new systems of record will emerge, but **for decisions, not for objects**. See [[concepts/systems-of-agents|systems of agents]].

## What Existing Systems of Record *Do* Capture

The article concedes systems of record do their job for canonical object data:

- **Operational SoRs** are the authoritative source for who the customer / employee / order *currently is*.
- **Data warehouses** support time-based historical queries — you can compare metrics across periods.

What they don’t capture:

- **State of the world at decision time** — by the time data lands in Snowflake, the decision context is gone.
- **Cross-system synthesis** — no incumbent sits in the cross-system path; e.g., a support escalation depends on CRM tier + Zendesk + PagerDuty + Slack, but no single system sees all four.
- **Approval chains that happen outside systems** — Zoom calls, Slack DMs, deal desk huddles.
- **Exception logic and precedent** — lives in people’s heads.

## Incumbent Counter-Moves (and Why They Don’t Land)

Foundation Capital anticipates incumbents will respond:

1. **Build their own agent frameworks** (Agentforce, Now Assist, Workday agents). Limitation: inherit parent’s siloed, current-state architecture.
2. **Reposition warehouses as truth registries** (Snowflake/Cortex + Streamlit; Databricks + Neon + Lakebase + AgentBricks). Limitation: warehouses are in the read path, not the write path.
3. **Acquire orchestration startups** to bolt on capability.
4. **Lock down APIs, charge egress fees** — same hyperscaler playbook.

The structural argument: "Incumbents can make extraction harder, but they can’t insert themselves into an orchestration layer they were never part of."

## Three Startup Paths That Challenge Incumbents

Per [[sources/foundation-capital-context-graphs|Foundation Capital]], [[concepts/systems-of-agents|systems of agents]] startups can take three paths against existing SoRs:

1. **Replace outright** at transition moments — Regie vs. Outreach/Salesloft in sales engagement.
2. **Replace modules**, keep the incumbent as ledger — Maximor in finance (ERP stays as GL; Maximor owns reconciliation logic).
3. **Become new systems of record for decisions** — PlayerZero in production engineering (the context graph becomes the authoritative artifact).

## Related Pages

- [[concepts/systems-of-agents]] — the proposed new category
- [[concepts/context-graph]] — the structural asset that replaces "canonical data" as the lock-in
- [[concepts/decision-trace]] — the unit incumbents can’t capture
- Salesforce, Snowflake, Databricks, ServiceNow — major incumbents (no dedicated entity pages)
- Jamin Ball — author of the contrast thesis (no dedicated entity page)
- [[sources/foundation-capital-context-graphs]] — primary source (Foundation Capital)
