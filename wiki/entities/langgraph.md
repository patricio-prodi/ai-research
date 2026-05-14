---
type: entity
name: "LangGraph"
kind: product
aliases: []
sources: [speakeasy-agent-framework-comparison]
related_concepts: [agent-framework, durable-execution]
last_updated: 2026-05-12
---

# LangGraph

A lower-level graph-based runtime and [[agent-framework]] that models agents as stateful graphs with explicit cycles.

## Characteristics
- Built for crash-proof, [[durable-execution]] using persistent checkpoints at every transition.
- Ideal for cyclic agent loops, human-in-the-loop workflows, and time-travel debugging.
- Has a steeper learning curve compared to abstraction-heavy frameworks like [[CrewAI]].
