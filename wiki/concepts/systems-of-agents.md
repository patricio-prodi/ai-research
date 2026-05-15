---
type: concept
title: "Systems of Agents"
aliases: [system of agents, agent orchestration platform, agentic system of record]
sources: [foundation-capital-context-graphs]
related_concepts: [systems-of-record, context-graph, decision-trace, agentic-ai, agent-framework]
related_entities: []
last_updated: 2026-05-15
---

# Systems of Agents

A proposed new category of enterprise platform that **sits in the execution path of agentic workflows**, persists [[concepts/decision-trace|decision traces]], and accumulates them into a [[concepts/context-graph|context graph]] that becomes the authoritative record of *why* the business did what it did. Coined as a category by Foundation Capital in [[sources/foundation-capital-context-graphs|"AI’s trillion-dollar opportunity: Context graphs"]].

Where [[concepts/systems-of-record|systems of record]] own canonical *objects* (customers, employees, orders), systems of agents own canonical *decisions*.

## Structural Advantage

Systems of agents have a single property no incumbent can replicate: **they are in the orchestration path at commit time.** When an agent triages an escalation, responds to an incident, or decides on a discount, it:

1. Pulls context from multiple systems
2. Evaluates rules and policies
3. Resolves conflicts
4. Routes approvals
5. Acts and writes state

The orchestration layer sees the full picture — at the moment of decision, not after the fact via ETL. That visibility is the precondition for capturing a [[concepts/decision-trace|decision trace]].

> "Because it’s executing the workflow, it can capture that context at decision time — not after the fact via ETL, but in the moment, as a first-class record." — [[sources/foundation-capital-context-graphs|Foundation Capital (2025)]]

## Three Strategic Paths

[[sources/foundation-capital-context-graphs|Foundation Capital]] identifies three paths systems-of-agents startups can take. Each trades off speed of go-to-market against depth of long-term moat:

### Path 1: Replace the System of Record Outright

Build a new SoR designed for agentic execution from day one — event-sourced state, policy capture native to the architecture. Viable at transition moments when incumbents look misaligned with the new operating model.

**Example**: Regie is building an AI-native sales engagement platform to replace legacy platforms like Outreach/Salesloft. Those legacy platforms were designed for humans executing sequences across a fragmented toolchain; Regie is designed for a mixed team where the agent is a first-class actor (prospecting, outreach, follow-ups, routing, escalation to humans).

### Path 2: Replace the Module, Keep the Incumbent as Ledger

Target a specific sub-workflow where exceptions and approvals concentrate. Become the system of record *for those decisions* while syncing final state back to the incumbent.

**Example**: Maximor automates cash, close management, and core accounting workflows without ripping out the general ledger. The ERP remains the ledger; Maximor becomes the source of truth where the reconciliation logic lives.

### Path 3: Become a New System of Record by Persisting Decision Lineage

Start as an orchestration layer. Persist what enterprises never systematically stored — the decision-making trace. Over time, that replayable lineage becomes the authoritative artifact. The agent layer stops being "just automation" and becomes "the place the business goes to answer 'why did we do that?'"

**Example**: PlayerZero. Production engineering sits at the intersection of SRE, support, QA, and dev — a classic "glue function" where humans carry context that software doesn’t capture. PlayerZero starts by automating L2/L3 support, but the real asset is the context graph it builds: a living model of how code, config, infrastructure, and customer behavior interact in reality. That graph becomes the source of truth for "why did this break?" and "will this change break production?" — questions no existing system can answer.

## Adjacent Infrastructure: Agent Observability

As [[concepts/decision-trace|decision traces]] accumulate and context graphs grow, enterprises will need to monitor, debug, and evaluate agent behavior at scale. Foundation Capital positions this as a critical adjacent layer.

**Example**: Arize is building the observability layer for agents — visibility into how agents reason, where they fail, and how their decisions perform over time. Foundation Capital frames it as "Datadog for agent decision quality."

## Where to Build: Founder Signals

[[sources/foundation-capital-context-graphs|Foundation Capital]] identifies signals for where systems-of-agents categories will emerge.

### Signals that apply to all three paths

- **High headcount on a workflow.** If a company has 50 people routing tickets, triaging requests, or reconciling data between systems, the decision logic is too complex for traditional tooling — and labor is being spent because no software currently captures the reasoning.
- **Exception-heavy decisions.** Routine deterministic workflows don’t need decision lineage; the agent just executes. The interesting surfaces are where logic is complex, precedent matters, and "it depends" is the honest answer. Examples: deal desks, underwriting, compliance reviews, escalation management.

### Signal that points specifically to Path 3 (new SoR opportunities)

- **Organizations that exist at the intersection of systems.** RevOps, DevOps, SecOps. These "glue" functions emerge precisely because no single system of record owns the cross-functional workflow. The org chart created a role to carry the context that software doesn’t capture. An agent that automates that role doesn’t just run steps faster — it can *persist* the decisions, exceptions, and precedents the role was created to produce.

## Relationship to Other Wiki Concepts

- **[[concepts/agentic-ai|Agentic AI]]** is the *capability*. Systems of agents are the *commercial category* that capability creates.
- **[[concepts/agent-framework|Agent frameworks]]** ([[entities/langgraph|LangGraph]], [[entities/mastra|Mastra]], etc.) are the *implementation tooling*. Systems of agents are *products built on that tooling*.
- **[[concepts/context-graph|Context graphs]]** are the *output asset* that systems of agents accumulate.
- **[[concepts/systems-of-record|Systems of record]]** are the *category being reframed*.

## Open Questions

- Will Path 3 startups remain independent or be acquired by incumbents trying to retrofit context graphs? `[citation needed]`
- Is "decision lineage" a category enterprises will pay for as a line item, or only as a side effect of buying agent automation? `[citation needed]`
- How portable are context graphs across orchestration vendors? `[citation needed]`

## Related Pages

- [[concepts/context-graph]]
- [[concepts/decision-trace]]
- [[concepts/systems-of-record]]
- [[concepts/agentic-ai]]
- [[concepts/agent-framework]]
- Regie, Maximor, PlayerZero, Arize — named startup examples (no dedicated entity pages)
- [[sources/foundation-capital-context-graphs]] — primary source (Foundation Capital)
