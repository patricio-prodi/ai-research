---
type: concept
title: "Agentic AI"
aliases: [ai agents, autonomous agents, agentic systems]
sources: [agentic-supply-chain-deloitte, ai-2027, garrytan-thin-harness-fat-skills, foundation-capital-context-graphs]
related_concepts: [llm-wiki, agi-timelines, thin-harness-fat-skills, skill-files, latent-vs-deterministic, context-graph, decision-trace, systems-of-agents, systems-of-record]
related_entities: [openai, anthropic, garry-tan]
last_updated: 2026-05-15
---

# Agentic AI

AI systems that can **reason, plan, and act autonomously** to achieve specific objectives. Distinguished from passive LLMs by their capacity for multi-step action, tool use, and environmental feedback loops.

## Definition

From [[sources/agentic-supply-chain-deloitte|Deloitte (2026)]]:
> "AI agents possess short- and long-term memory, access a wide variety of tools, and can reason, plan, and act autonomously to achieve specific objectives."

Core capabilities:
- **Memory**: short-term (context window) and long-term (external storage, wiki, databases)
- **Tool use**: web search, code execution, API calls, file systems
- **Planning**: breaking goals into sub-tasks, sequencing actions
- **Autonomy**: operating with minimal human intervention within defined guardrails

## Three value modes (supply chain framing)

From [[sources/agentic-supply-chain-deloitte]]:

1. **Autonomous workflow execution** — performs routine and coordination-intensive tasks within guardrails, freeing humans for higher-value work. Reduces cycle times, improves accuracy.

2. **Always-on monitoring and response** — continuously senses changes, evaluates impact, takes bounded action in real time, unconstrained by human schedules or review cycles.

3. **Scaling beyond human limits** — applies consistent logic across millions of parts, suppliers, scenarios — coverage and depth far beyond human teams alone.

## Adoption signals

- >50% of supply chain executives report deploying AI agents to automate workflows (Deloitte-cited survey, 2026).
- Gartner: "By 2030, 50% of cross-functional supply chain management solutions will use intelligent agents."
- Gartner: "40% of enterprise applications will be integrated with task-specific AI agents by end of 2026, up from <5% today."

## Agent architecture patterns

**Hierarchical (supply chain model)**:
- *Domain agents*: orchestration layers, outcome owners, enforce policies/guardrails
- *Task-specific agents*: bounded data retrieval, analysis, execution
- *Cross-functional agents*: enterprise-wide governance and risk intelligence

**Flat (LLM Wiki model)**:
- Single agent with tool access (file read/write, search)
- Schema document (`CLAUDE.md`) serves as guardrails
- Human in the loop via conversation and review

## Implementation frameworks

The ecosystem of [[concepts/agent-framework|agent frameworks]] provides tooling to implement these patterns. Options range from minimal SDKs ([[entities/openai-agents-sdk]], [[entities/vercel-ai-sdk]]) for simple tools, to graph-based runtimes ([[entities/langgraph]]) for [[concepts/durable-execution]], to role-based multi-agent setups ([[entities/crewai]]). See [[sources/speakeasy-agent-framework-comparison]] for a comprehensive breakdown.

## Human role shift

Agentic AI consistently implies a human role shift:
- Away from: routine execution, manual handoffs, sequential decision-making
- Toward: oversight, orchestration, ethical judgment, strategic direction

Interaction modes: copilots, conversational chat, voice. Moving from static dashboards to dynamic collaboration.

## Relationship to AGI timelines

If [[concepts/agi-timelines|AGI]] arrives near 2027 as [[sources/ai-2027]] forecasts, current agentic AI systems are early-stage precursors. The capabilities described in the Deloitte supply chain article (bounded autonomy within guardrails) may look primitive within 2–3 years.

## Key design principle

> "Companies should reimagine and redesign supply chain workflows around the unique strengths of humans and agents rather than simply inserting AI agents into existing operating models." — Deloitte (2026)

This principle generalizes: agentic AI enables new operating models, not just automation of old ones.

## Architectural design principles (Tan, 2026)

From [[sources/garrytan-thin-harness-fat-skills|Garry Tan's "Thin Harness, Fat Skills"]] — the most specific architectural framework in this wiki for building productive agent systems:

- **[[concepts/thin-harness-fat-skills|Thin harness, fat skills]]**: Keep the program wrapper minimal (~200 lines); encode nearly all capability in reusable markdown skill files. The 100x productivity gap between users comes from this architectural choice, not model selection.
- **[[concepts/skill-files|Skill files]]** work like method calls — same procedure, different parameters. 90% of agent value lives in the skills layer.
- **[[concepts/latent-vs-deterministic|Latent vs. deterministic]]**: The most common mistake in agent design is putting deterministic problems (combinatorial optimization, exact computation) into latent space (LLM judgment). Every step must be consciously assigned to the right layer.
- **[[concepts/resolvers|Resolvers]]**: Route context to the model on demand rather than loading everything into the context window. Prevents the attention degradation that comes from bloated prompts.
- **[[concepts/diarization|Diarization]]**: Reading a full corpus and synthesizing a structured profile — the capability that makes agents genuinely useful for knowledge work beyond simple lookup.

The [[entities/anthropic|Anthropic]] Claude Code architecture (reviewed after accidental npm publish in March 2026) implements these principles: live repo context, prompt caching, purpose-built tools, context bloat minimization, structured session memory, parallel sub-agents.

## Commercial implication: the context graph as moat (Foundation Capital, 2025)

From [[sources/foundation-capital-context-graphs|Foundation Capital]]: the most valuable property of agentic AI in the enterprise is not the labor automation but the *byproduct*. Because an agent must — for its own correctness — gather inputs across systems, evaluate policy, resolve conflicts, and route approvals, the reasoning that previously lived in people’s heads becomes durable data **as a side effect of using the agent**.

The orchestration layer of an agentic system therefore sits in a privileged position: it captures **[[concepts/decision-trace|decision traces]]** at commit time. Aggregated over time, those traces form a **[[concepts/context-graph|context graph]]** — a queryable record of *why* the business did what it did.

Foundation Capital argues this creates a new commercial category — **[[concepts/systems-of-agents|systems of agents]]** — that displaces (or complements) traditional [[concepts/systems-of-record|systems of record]]. Incumbents (Salesforce, Snowflake, Databricks) are structurally blocked from capturing the same asset because they sit outside the execution path.

This reframes the business case for agentic AI: not just cost reduction via automation, but **capture of a previously uncaptured category of business truth**.

## Related pages

- [[concepts/llm-wiki]] — a specific agentic AI application (LLM as wiki maintainer)
- [[concepts/agi-timelines]] — how current agentic AI relates to AGI forecasts
- [[concepts/thin-harness-fat-skills]] — the architectural design framework
- [[concepts/context-graph]], [[concepts/decision-trace]], [[concepts/systems-of-agents]], [[concepts/systems-of-record]] — the commercial/structural framing
- [[topics/agentic-systems]] — synthesis across agentic AI applications
- [[entities/openai]], [[entities/anthropic]] — labs driving agentic AI development
- [[entities/garry-tan]] — architect of the thin harness framework
- Foundation Capital — VC thesis on context graphs (no dedicated entity page)
