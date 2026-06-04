---
type: source
title: "A2UI v0.9: The New Standard for Portable, Framework-Agnostic Generative UI"
article: "raw/A2UI v0.9 The New Standard for Portable, Framework-Agnostic Generative UI- Google Developers Blog.md"
source_url: "https://developers.googleblog.com/a2ui-v0-9-generative-ui/"
author: "[[Google]]"
published: 2026-04-17
ingested: 2026-05-20
tags: [generative-ui, a2ui, agent-architecture, a2a-protocol, flutter, open-source, streaming]
key_concepts: [generative-ui, a2a-protocol, mcp-server]
---

# A2UI v0.9: The New Standard for Portable, Framework-Agnostic Generative UI

[Source article](../raw/A2UI%20v0.9%20The%20New%20Standard%20for%20Portable%2C%20Framework-Agnostic%20Generative%20UI-%20Google%20Developers%20Blog.md)

## Overview

April 2026 follow-up from [[entities/google|Google]] on [[entities/a2ui|A2UI]], updating from v0.8 (Dec 2025) to v0.9. The release focuses on **developer experience, production hardening, and ecosystem growth**. The key conceptual shift: agents should adapt to *your existing design system*, not the other way around. The component set previously called "Standard" is renamed to "Basic" to emphasize it's an optional fallback, not the expected path.

## What's new in v0.9

### 1. "Standard" → "Basic" component set
Frontend developers already have a design system and component catalog. A2UI v0.9 makes this explicit: the optional built-in components are now called "Basic" to signal they are a starting point, not a requirement. The design intent: agents should respond using existing front ends.

### 2. Shared web-core library + official React renderer
A new shared [web-core](https://github.com/google/A2UI/tree/main/renderers/web_core) library vastly simplifies any browser-based renderer. This release adds the **official React renderer** alongside Flutter, Lit, and Angular. Community renderer slots added for ecosystem contributions.

### 3. A2UI Agent SDK (`pip install a2ui-agent-sdk`)
The server-side integration is now a single pip install. The SDK provides:
- **Schema Manager**: manages spec version compatibility; generates the LLM system prompt embedding A2UI instructions
- **CatalogConfig**: define your component catalog from a JSON file; optionally provide few-shot examples to help the LLM generate correctly
- **Response parser/validator**: incrementally parses and heals LLM JSON output on the fly — components render as they are generated, without waiting for a complete JSON block
- **Version negotiation**: dynamically selects the best spec version based on client capabilities
- **Dynamic catalogs**: switch catalog schemas at runtime for different user permissions or device constraints

Integration is a 5-step process: define catalog → init SchemaManager → generate system prompt → init agent → stream/parse response.

### 4. New language features
- **Client-defined functions**: server-side validation callbacks defined by the client (e.g., form validation rules)
- **Client-to-server data syncing**: supports collaborative editing between user and agent
- **Improved error handling** and a simplified, modular schema

### 5. Transport-agnostic
A2UI 0.9 works over: **MCP**, **WebSockets**, **REST**, **AG UI**, **A2A**, or any custom transport. The transport layer is now fully abstracted.

## Ecosystem growth

| Integrator | What they shipped |
|---|---|
| **AG2** (AutoGen creators) | Native `A2UIAgent` — built-in A2UI support in the AG2 multi-agent framework |
| **A2A 1.0** | [[concepts/a2a-protocol\|A2A Protocol]] officially launched v1.0; serves as transport for agent-to-agent and agent-to-frontend comms |
| **Vercel json-renderer** | Proof-of-concept renderer supporting A2UI; potential dedicated renderer for the Vercel/Next.js community |
| **Oracle Agent Spec** | Agent Spec + AG UI + A2UI: Agent Spec defines what runs, AG UI carries interaction, A2UI defines what the user touches; layers are swappable |
| **AG-UI (CopilotKit)** | Broader GenUI support: A2UI, MCP Apps, and Open Generative UI all supported |

## Production examples

**Personal Health Companion** (Rebel App Studio + Codemate, Flutter): eliminates "data silos" and "navigation fatigue" from fragmented medical records and wearable telemetry. LLM-powered chat dynamically generates UI widgets on the fly — lab results, vaccine expirations, clinic locations — based on immediate conversation context.

**Personal Financial Planner / Life Goal Simulator** (Very Good Ventures): user selects a persona and goal (retirement, first home); Gemini + Flutter GenUI SDK generates a native-feeling real-time UI from a curated widget catalog (sliders, bar charts, multi-selects). VGV is a Flutter/GenUI consultancy (clients include Toyota and GEICO).

## Key claims

1. **"Bring your own design system"**: the core positioning shift in v0.9. A2UI agents adapt to existing component catalogs — not the reverse.
2. **Resilient streaming** is production-critical: real LLM output is partial/malformed JSON; the SDK's incremental parse+heal makes progressive rendering practical without special LLM fine-tuning.
3. **Ecosystem momentum**: AG2, Oracle, Vercel all shipped integrations within ~4 months of the v0.8 launch. A2A 1.0 reaching stable is a meaningful governance signal.
4. **Roadmap signals**: MCP Apps integrations, progressive disclosure "skills" for A2UI, human intent abstractions, PII support — the protocol is moving up the stack.

## Implications

- The shift from "Standard" to "Basic" components reflects a lesson learned: enterprise and consumer teams won't rebuild their design systems for a new protocol. A2UI succeeds only if agents can speak *their* language, not a new one. This is the right call — interoperability demands meeting clients where they are.
- Resilient streaming (incremental parse+heal) is what makes generative UI usable in production. LLMs don't produce perfectly-formed JSON reliably; the SDK absorbs this failure mode. Without it, generative UI is demo-ware.
- Oracle's Agent Spec integration signals enterprise validation: large vendors adopting A2UI for their agentic platforms.

## Related pages

- [[sources/google-a2ui-introduction]] — v0.8 announcement (the predecessor; read first for conceptual foundation)
- [[concepts/generative-ui]] — core concept
- [[concepts/a2a-protocol]] — transport layer; 1.0 launched
- [[concepts/mcp-server]] — A2UI now runs over MCP transport
- [[entities/a2ui]] — the product; updated to v0.9
- [[entities/google]] — author
- [[entities/copilotkit]] — AG UI integration
- [[entities/vercel-ai-sdk]] — Vercel json-renderer proof of concept
