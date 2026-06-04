---
type: source
title: "Introducing A2UI: An open project for agent-driven interfaces"
article: "raw/Introducing A2UI An open project for agent-driven interfaces- Google Developers Blog.md"
source_url: "https://developers.googleblog.com/introducing-a2ui-an-open-project-for-agent-driven-interfaces/"
author: "[[Google]]"
published: 2025-12-15
ingested: 2026-05-20
tags: [generative-ui, agent-architecture, multi-agent, a2ui, a2a-protocol, flutter, open-source]
key_concepts: [generative-ui, a2a-protocol, agentic-ai, mcp-server]
---

# Introducing A2UI: An open project for agent-driven interfaces

[Source article](../raw/Introducing%20A2UI%20An%20open%20project%20for%20agent-driven%20interfaces-%20Google%20Developers%20Blog.md)

## Overview

[[entities/google|Google]] publicly released [[entities/a2ui|A2UI]] (v0.8) in December 2025 — an open-source format and renderer set for **agent-driven user interfaces**. A2UI allows LLM agents to compose bespoke UIs from a catalog of pre-approved components and deliver them to any front-end application as a structured JSON payload, not executable code. Initial client renderers target Flutter, Web Components (Lit), and Angular.

The project was built with [[entities/copilotkit|CopilotKit/AG UI]], the Opal team at Google, Gemini Enterprise, and Flutter's GenUI SDK. It is Apache 2 licensed.

## The core problem A2UI solves

Text-only agent interaction requires expensive multi-turn exchanges for structured data (e.g., selecting a restaurant time slot). A better experience is an agent that generates the right form, picker, or dashboard directly. But in a multi-agent world, the agent doing the work is **remote** — it cannot touch the host application's DOM directly. It must send messages.

Previous options:
- **iframes with HTML/JS**: heavy, visually disjointed, security-complex
- **Executable code injection**: unacceptable risk from untrusted remote agents

A2UI's answer: a **declarative JSON format** — safe like data, expressive like code.

## Key claims

1. **Declarative, not executable.** The agent sends a blueprint of components from the client's pre-approved catalog. The client renders using its own native widgets. No arbitrary code runs.

2. **Flat, incrementally updateable.** UI is represented as a flat list of components with ID references — easy for LLMs to generate token-by-token, and easy to update in-place as the conversation evolves.

3. **Framework-agnostic.** The same A2UI JSON payload can be rendered by Flutter, Angular, Lit Web Components, SwiftUI, or any other framework. The client maps abstract descriptions to native widgets.

4. **LLM-friendly structured output.** Agents can generate A2UI either via generative structured output or by populating a template. Incremental updates enable progressive rendering.

5. **Multi-agent mesh compatible.** A2UI messages travel over [[concepts/a2a-protocol|A2A Protocol]] (and AG UI). An orchestrator agent can read and reason about lightweight A2UI payloads from subagents, enabling fluid agent-to-agent UI collaboration.

## Evidence / adoption

- Integrated into **Opal** (Google's AI mini-app builder, hundreds of thousands of users)
- Integrated into **Gemini Enterprise** for workflow automation UIs
- **Flutter's GenUI SDK** uses A2UI as the UI declaration format between server-side agents and the Flutter app
- **CopilotKit/AG UI** shipped day-0 compatibility; public [A2UI Widget Builder](https://go.copilotkit.ai/A2UI-widget-builder) available
- Multiple Google internal teams using it for AI-powered products

## Landscape positioning

A2UI is not a replacement for AG UI, Vercel AI SDK, or MCP Apps — it occupies a specific niche:

| Approach | Rendering model | Who controls styling | Trust boundary |
|---|---|---|---|
| **A2UI** | Native components from client catalog | Client | No executable code |
| **MCP Apps** | Sandboxed iframe with HTML content | Server/opaque | iframe isolation |
| **AG UI (pipes only)** | State sync / chat scaffolding | Host app | N/A |
| **ChatKit (OpenAI)** | Optimized for OpenAI ecosystem | Platform | Platform-specific |

A2UI's "native-first" approach gives the client full control over styling at the cost of requiring a pre-approved component catalog. MCP Apps allow richer server-side control but sacrifice visual consistency.

## Notable quotes

> "We needed a way to transmit UI that is **safe like data, but expressive like code**." — Google A2UI Team

> "A2UI is foundational to our work. It gives us the flexibility to let the AI drive the user experience in novel ways, without being constrained by a fixed front-end. Its declarative nature and focus on security allow us to experiment quickly and safely." — Dimitri Glazkov, Principal Engineer, Opal Team

> "Much like A2A lets any agent talk to another agent regardless of platform, A2UI standardizes the user interface layer and supports remote agent use cases through an orchestrator." — James Wren, Senior Staff Engineer, AI Powered Google

## Implications

- **Generative UI is the next frontier after text/image/code generation.** A2UI is the first credible open standard targeting it.
- **The multi-agent mesh creates a new UI problem.** When agents are remote and untrusted, you can't pass executable UI — you need a safe declarative layer. This is structurally analogous to why REST/JSON beat RPC for distributed systems.
- **Client control is a feature, not a limitation.** The tradeoff (client catalog limits what agents can render) buys brand consistency and security. Enterprise buyers likely prefer this over arbitrary iframe injection.
- **Flutter's GenUI SDK already uses A2UI**, meaning it has near-production validation, not just a spec. This is meaningful signal for v0.8.

## Related pages

- [[concepts/generative-ui]] — the core concept
- [[concepts/a2a-protocol]] — transport layer for A2UI messages
- [[concepts/agentic-ai]] — multi-agent mesh context
- [[concepts/mcp-server]] — MCP Apps comparison
- [[entities/google]] — author
- [[entities/a2ui]] — the project itself
- [[entities/copilotkit]] — day-0 collaborator
