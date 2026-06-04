---
type: entity
name: "A2UI"
kind: product
aliases: [A2UI project, Agent-to-UI]
sources: [google-a2ui-introduction, google-a2ui-v09]
related_concepts: [generative-ui, a2a-protocol]
last_updated: 2026-05-20
---

# A2UI

An open-source format, renderer library, and agent SDK for **agent-driven generative user interfaces**. Released publicly by [[entities/google|Google]] in December 2025 at v0.8; updated to v0.9 in April 2026. Apache 2 licensed.

## What it is

A2UI provides:
1. **A format** — a JSON-based declarative specification for UI component trees, optimized for LLM generation and incremental updates
2. **Renderer libraries** — Flutter (via GenUI SDK), Lit Web Components, Angular, React (v0.9); community renderers supported
3. **A2UI Agent SDK** (`pip install a2ui-agent-sdk`) — server-side SDK for integrating A2UI into any Python agent framework
4. **Transport integrations** — works over [[concepts/a2a-protocol|A2A Protocol]], AG UI, MCP, WebSockets, REST ([[entities/copilotkit|CopilotKit]])

## Key design choices

- **Declarative, not executable**: Agents only reference components from the client's pre-approved catalog — no arbitrary code injection
- **Bring your own design system**: agents adapt to the client's existing component catalog; the "Basic" built-in set is a fallback, not the expectation
- **Flat component list with ID refs**: LLM-friendly for incremental generation and diff-style updates
- **Resilient streaming**: the Agent SDK incrementally parses and heals partial/malformed LLM JSON, rendering components as they are generated
- **Framework-agnostic**: the same payload renders natively on any supported framework; client controls all styling

## Agent SDK features (v0.9)

- **Schema Manager**: manages spec version compatibility, generates the LLM system prompt
- **CatalogConfig**: define component catalog from JSON; optional few-shot examples for LLM guidance
- **Version negotiation**: dynamically selects best spec version based on client capabilities
- **Dynamic catalogs**: switch catalog schemas at runtime for user permissions or device constraints
- **Language features**: client-defined validation functions, client-to-server data syncing for collaborative editing

## Ecosystem (as of April 2026)

| Integrator | Integration |
|---|---|
| AG2 (AutoGen) | Native `A2UIAgent` built-in |
| Oracle | Agent Spec + AG UI + A2UI stack |
| Vercel | json-renderer proof of concept |
| CopilotKit / AG UI | Day-0 full support |
| Flutter GenUI SDK | Core UI declaration format |

## Status

- v0.9 as of April 2026
- In production: Opal (Google), Gemini Enterprise, Flutter GenUI SDK, Personal Health Companion (Codemate), Life Goal Simulator (Very Good Ventures)
- GitHub: [google/A2UI](https://github.com/google/A2UI)
- Docs: a2ui.org; A2UI Theater playground: a2ui-composer.ag-ui.com

## Related pages

- [[concepts/generative-ui]] — the concept A2UI implements
- [[concepts/a2a-protocol]] — transport layer; v1.0 launched April 2026
- [[entities/google]] — parent organization
- [[entities/copilotkit]] — AG UI integration partner
- [[sources/google-a2ui-introduction]] — v0.8 announcement
- [[sources/google-a2ui-v09]] — v0.9 release
