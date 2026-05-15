---
type: concept
title: "Decision Trace"
aliases: [decision trace, decision lineage, decision record]
sources: [foundation-capital-context-graphs]
related_concepts: [context-graph, systems-of-record, systems-of-agents, agentic-ai]
related_entities: []
last_updated: 2026-05-15
---

# Decision Trace

A **structured, re-playable record of how context turned into action on a single occasion**: what inputs were gathered across systems, what policy was evaluated, what exception route was invoked, who approved, and what state was written. Introduced by Foundation Capital in [[sources/foundation-capital-context-graphs|"AI’s trillion-dollar opportunity: Context graphs"]].

Decision traces are the **unit**; aggregated across entities and time, they form a [[concepts/context-graph|context graph]].

## Rules vs. Decision Traces

The article’s central distinction:

| | Rules | Decision Traces |
|---|---|---|
| Captures | *What should happen in general* | *What happened in this specific case* |
| Example | "Use official ARR for reporting" | "We used X definition, under policy v3.2, with a VP exception, based on precedent Z, and here’s what we changed" |
| Where stored today | Policies, runbooks, docs | Slack threads, Zoom calls, people’s heads |
| Captured by enterprise software? | Partially (in policy docs) | Almost never |

> "Agents don’t just need rules. They need access to the decision traces that show how rules were applied in the past, where exceptions were granted, how conflicts were resolved, who approved what, and which precedents actually govern reality." — [[sources/foundation-capital-context-graphs|Foundation Capital (2025)]]

## What a Decision Trace Contains

For each agent run (or human-approved decision in a human-in-the-loop workflow):

1. **Inputs gathered** — every record pulled across systems (CRM tier, support tickets, billing terms, recent incidents, Slack threads)
2. **Policy evaluated** — which policy version applied, which clauses fired
3. **Conflicts resolved** — which definitions or rules disagreed and how the conflict was settled
4. **Exception route invoked** — if the action departs from policy, what exception type
5. **Approvers** — identity and chain of approvals
6. **Rationale** — why the exception was justified, what precedent was cited
7. **Final state written** — what change landed in the downstream system

The critical property: **all of this is captured at commit time**, not reconstructed afterward. ETL-based reconstruction loses the state-of-the-world at decision time.

## Why Decision Traces Aren’t Captured Today

From [[sources/foundation-capital-context-graphs|Foundation Capital]]:

- **Exception logic lives in people’s heads.** "We always give healthcare companies an extra 10% because their procurement cycles are brutal." Tribal knowledge passed down through onboarding and side conversations.
- **Precedent from past decisions is unlinked.** "We structured a similar deal for Company X last quarter — we should be consistent." No system links those two deals or records why the structure was chosen.
- **Cross-system synthesis happens in heads.** A support lead checks ARR in Salesforce, sees escalations in Zendesk, reads a Slack churn thread, and decides. The ticket only says "escalated to Tier 3."
- **Approval chains happen outside systems.** A VP approves a discount on a Zoom call or in a Slack DM. The opportunity record shows the final price, not who approved the deviation or why.

> "This is what 'never captured' means. Not that the data is dirty or siloed, but that the reasoning connecting data to action was never treated as data in the first place." — Foundation Capital (2025)

## Why Agents Make This Capturable

When an agent runs an exception-heavy workflow, it must — for its own correctness — gather inputs, evaluate policy, resolve conflicts, and route approvals. If the orchestration layer emits a structured trace on every run, the reasoning that previously lived in heads becomes durable data **as a side effect of using the agent**.

This is why [[concepts/systems-of-agents|systems of agents]] startups have a structural advantage over both [[concepts/systems-of-record|systems of record]] and data warehouses: only the orchestration layer sees the full context at decision time.

## Human-in-the-Loop Capture

Decision traces don’t require full autonomy. From [[sources/foundation-capital-context-graphs|Foundation Capital]]:

> "None of this requires full autonomy on day one. It starts with human-in-the-loop: the agent proposes, gathers context, routes approvals, and records the trace. … Even when a human still makes the call, the graph keeps growing, because the workflow layer captures the inputs, approval, and rationale as durable precedent instead of letting it die in Slack."

This is the practical on-ramp: deploy the agent as a proposer/router; capture the trace whether the human or the agent makes the final call.

## Where Decision Traces Concentrate

The article identifies workflow categories where decision traces are dense and currently uncaptured:

- **Deal desks** (discount approvals, contract exceptions)
- **Underwriting** (risk classification, exception routing)
- **Compliance reviews** (policy fit, exception justification)
- **Escalation management** (support, security incidents)
- **Renewal logic** (discount caps, service-impact exceptions)
- **Production engineering triage** (incident root cause attribution — PlayerZero’s domain)

The common pattern: **"it depends" is the honest answer**, and the dependencies are cross-system.

## Related Pages

- [[concepts/context-graph]] — what decision traces aggregate into
- [[concepts/systems-of-agents]] — where decision traces are captured
- [[concepts/systems-of-record]] — what fails to capture them today
- [[concepts/agentic-ai]] — the orchestration technology
- [[sources/foundation-capital-context-graphs]] — primary source
