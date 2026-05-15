---
type: topic
title: "Agentic Systems: Applications and Implications"
sources: [agentic-supply-chain-deloitte, karpathy-llm-knowledge-bases, ai-2027, garrytan-thin-harness-fat-skills]
key_concepts: [agentic-ai, llm-wiki, agi-timelines, thin-harness-fat-skills, skill-files, latent-vs-deterministic, diarization]
last_updated: 2026-04-16
---

# Agentic Systems: Applications and Implications

**Thesis**: Agentic AI — AI that reasons, plans, and acts autonomously — is already producing concrete value in enterprise settings (supply chains) and personal knowledge work (LLM wikis). These are early-stage applications of a capability that, if forecasts are correct, will become dramatically more powerful within 2–3 years.

## Three application domains in this wiki

### 1. Enterprise: Agentic supply chains

From [[sources/agentic-supply-chain-deloitte]]: Manufacturers are deploying hierarchical agent systems (domain agents → task agents → cross-functional agents) to achieve always-on supply chain monitoring, autonomous workflow execution, and coverage beyond human scale.

Current state: >50% of supply chain executives report deploying AI agents. Gartner projects 50% of supply chain management solutions will use agents by 2030.

The organizing principle: **don't insert agents into old workflows — redesign workflows around agents**.

### 2. Personal: LLM wikis

From [[llm-knowledge-bases-explained]]: [[entities/andrej-karpathy|Karpathy]]'s knowledge base system. An LLM acts as compiler and librarian: reading raw sources, writing summaries, maintaining cross-references, flagging contradictions. The human reads the wiki; the LLM writes it.

Current state: proven at ~100-source scale without RAG infrastructure. The [[concepts/llm-wiki|LLM Wiki]] pattern this vault implements.

### 3. Architecture: Thin harness, fat skills

From [[sources/garrytan-thin-harness-fat-skills]]: [[entities/garry-tan|Garry Tan]] defines the internal architecture that makes agent systems productive. The 100x productivity gap between agent power users is not model-level — it's architectural.

The framework: a **thin CLI harness** (~200 lines) in the middle, **fat skill files** (markdown procedures) on top, and a **deterministic application layer** on the bottom. Skills work like method calls: same procedure, different parameters, radically different capabilities.

Key design distinctions: [[concepts/latent-vs-deterministic|latent vs. deterministic]] (most common mistake: putting combinatorial problems into LLM judgment), and [[concepts/diarization|diarization]] (reading a full corpus and synthesizing a structured profile — the step that enables real knowledge work beyond lookup).

The YC Startup School case: 6,000 founders, /enrich-founder runs nightly, /match-* skills handle three distinct matching strategies, /improve rewrites its own rules from NPS surveys. 12% "OK" ratings → 4% after one learning cycle.

### 4. Implementation: Agent Frameworks

From [[sources/speakeasy-agent-framework-comparison]]: The software ecosystem for building agentic systems has rapidly matured. The choice of [[concepts/agent-framework|agent framework]] dictates the architecture:

- **SDKs** ([[entities/openai-agents-sdk]], [[entities/vercel-ai-sdk]]): Best for simple, linear tool calling.
- **Code-first Frameworks** ([[entities/langgraph]], [[entities/mastra]], [[entities/pydanticai]], [[entities/crewai]]): Best for complex orchestration, multi-agent networks, and [[concepts/durable-execution]].
- **Hybrid Frameworks** ([[entities/n8n]], [[entities/vellum]]): Best for connecting APIs and exposing AI workflows to non-technical teams.

The selection of a framework requires matching the organization's technical language (Python vs. TypeScript) and the orchestration complexity of the agents being built.

## Common structural patterns

Both applications share the same underlying architecture:

| Pattern | Supply Chain | LLM Wiki |
|---|---|---|
| Hierarchical agents | Domain → Task → Cross-functional | Single agent + tools |
| Guardrails/schema | Policies and governance | `CLAUDE.md` |
| Human role | Oversight, strategy | Curation, direction |
| Memory | Short + long-term in agents | Wiki files as external memory |
| Human-AI interface | Copilots, chat, voice | Conversation + Obsidian |

## The redesign imperative

Both domains emphasize the same principle: agentic AI doesn't just automate existing processes — it enables fundamentally new operating models.

- Supply chains: continuous sensing and bounded autonomous action replace periodic human review cycles.
- Knowledge work: persistent, compounding wiki replaces ad hoc document retrieval (RAG).

Inserting an agent into an old process (RAG over existing docs, AI assistant inside existing workflow) is the weaker pattern. **Redesigning the process for agents** is where transformative value comes from.

## Implications for AGI transition

If [[concepts/agi-timelines|AGI]] arrives near 2027 ([[sources/ai-2027]]):

- Current agentic systems (bounded, specialized, within guardrails) are precursors to vastly more capable autonomous agents.
- The organizational and workflow redesigns happening now are rehearsals for deeper transformations.
- Supply chains and knowledge management are early test beds — the pattern will propagate to most knowledge work.

The question isn't whether to use agentic AI, but how to redesign workflows for it now while the stakes are lower and the capabilities are still bounded.

## Open questions

- At what scale do LLM wikis require RAG infrastructure vs. remaining index-based?
- What governance frameworks work for enterprise agentic systems when guardrails fail?
- How does the human role shift as agent autonomy increases toward AGI-level capability?
- Is there an optimal organizational structure for human-agent teams?

## Related pages

- [[concepts/agentic-ai]]
- [[concepts/thin-harness-fat-skills]]
- [[concepts/skill-files]]
- [[concepts/latent-vs-deterministic]]
- [[concepts/diarization]]
- [[concepts/llm-wiki]]
- [[concepts/agi-timelines]]
- [[sources/agentic-supply-chain-deloitte]]
- [[llm-knowledge-bases-explained]]
- [[sources/garrytan-thin-harness-fat-skills]]
- [[topics/ai-forecasting]]
