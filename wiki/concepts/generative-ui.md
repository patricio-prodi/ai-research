---
type: concept
title: "Generative UI"
aliases: [agent-driven UI, agentic UI, dynamic UI generation, gen UI]
sources: [google-a2ui-introduction, google-a2ui-v09]
related_concepts: [agentic-ai, a2a-protocol, mcp-server, latent-vs-deterministic]
related_entities: [google, a2ui, copilotkit]
last_updated: 2026-05-20
---

# Generative UI

The ability for AI agents to **generate contextually relevant user interfaces** on the fly — composing forms, pickers, charts, and layouts tailored to the specific task at hand rather than displaying pre-built static screens.

## Core idea

Text-only agent interaction forces users into expensive multi-turn exchanges for structured input (e.g., choosing a date + time + party size for a restaurant booking requires 5–6 back-and-forth messages). An agent that can generate the right form directly collapses this to a single interaction.

From [[sources/google-a2ui-introduction|Google A2UI (2025)]]:
> "With A2UI, LLMs can compose bespoke UIs from a catalog of widgets to provide a graphical, beautiful, easy to use interface for the exact task at hand."

## The trust boundary problem

In a single-app context, agents can manipulate the DOM directly. In a **multi-agent mesh** (see [[concepts/agentic-ai]]), the agent doing the work is often remote — running on a different server, owned by a different organization. It cannot touch the host UI layer; it must send messages.

Traditional solutions:
- **iframes with HTML/JS**: heavy, visually disjointed, requires sandboxing, doesn't inherit host app styling
- **Executable code injection**: unacceptable security risk from untrusted remote LLMs

The design requirement: UI that is **"safe like data, but expressive like code"**.

## A2UI's approach: declarative native components

[[entities/a2ui|A2UI]] (Google, 2025) is the first open format targeting this problem. Its design principles:

### 1. Declarative, not executable
The agent sends a JSON payload describing a tree of UI components from a **client-maintained catalog** of pre-approved widgets (`Card`, `Button`, `TextField`, `DatePicker`, etc.). The agent can only request components from this catalog — it cannot inject arbitrary HTML or JS. This eliminates a class of UI injection attacks.

### 2. Flat, incrementally updateable
The UI is a flat list of components with ID references, not a deeply nested tree. This makes it:
- Easy for LLMs to generate incrementally (token-by-token streaming)
- Easy to update in-place as conversation evolves (the agent sends only changed components by ID)

### 3. Framework-agnostic
The same A2UI JSON payload renders via Flutter, Lit Web Components, Angular, and React (added in v0.9). The client maps abstract component descriptions to its own native widgets — so the rendered UI inherits the host app's branding and accessibility features automatically.

### 4. Bring your own design system
A key v0.9 lesson: the built-in "Basic" component set is a fallback, not the expectation. Agents should adapt to the client's *existing* component catalog, not require teams to rebuild around a new one. This is what makes the protocol adoptable in enterprise contexts without redesigning the front end.

### 5. Multi-transport
A2UI payloads travel over [[concepts/a2a-protocol|A2A Protocol]], AG UI, MCP, WebSockets, REST, or any custom transport. Transport is fully abstracted from the UI format.

## Comparison with adjacent approaches

| Approach | Rendering model | Who controls styling | Security mechanism |
|---|---|---|---|
| **A2UI (Google)** | Client's native components from pre-approved catalog | Client | Catalog allowlist; no executable code |
| **MCP Apps** | Sandboxed iframe serving HTML | Server | iframe isolation |
| **AG UI (CopilotKit)** | State sync + chat scaffolding; A2UI as the UI format | Host app | N/A (pipes, not rendering) |
| **ChatKit (OpenAI)** | Optimized for OpenAI platform | Platform | Platform-controlled |

The A2UI / MCP Apps contrast is architecturally sharp: A2UI is **native-first** (the client renders with its own components, inheriting brand and a11y), while MCP Apps are **content-first** (the server controls the HTML, the client sandboxes it). Neither is universally better — native-first requires a pre-built catalog; content-first gives the server more expressive power at the cost of visual consistency.

## Resilient streaming: the production enabler

Real LLM output is partial and often malformed JSON. The A2UI Agent SDK (v0.9) handles this with **incremental parse+heal**: it reads the LLM's token stream, corrects errors on the fly, and emits complete components to the renderer as they become available — no waiting for a full valid JSON block. Without this, generative UI is demo-ware; with it, the UX is responsive even on slow inference.

## Evidence of production use

- **Flutter GenUI SDK** uses A2UI as its UI declaration format between server-side agents and Flutter apps — production-quality validation
- **Opal** (Google's AI mini-app builder, hundreds of thousands of users) integrated A2UI for dynamic UI generation
- **Gemini Enterprise** integrating A2UI for enterprise agent workflow UIs
- **Personal Health Companion** (Codemate/Rebel App Studio, Flutter): replaces fragmented medical record dashboards with context-driven generative UI widgets
- **Life Goal Simulator** (Very Good Ventures, Flutter): Gemini + GenUI SDK generates personalized financial planning UI from a widget catalog

## Ecosystem (as of April 2026)

Four months after v0.8, the protocol has meaningful third-party adoption:
- **AG2** (AutoGen creators): native `A2UIAgent` 
- **Oracle**: Agent Spec + AG UI + A2UI enterprise stack
- **Vercel**: json-renderer proof of concept
- **CopilotKit / AG UI**: day-0 full support; AG UI middleware lets any AG UI agent drive A2UI on day zero

## Design tension: catalog breadth vs. security

The security model depends on the catalog being a curated allowlist. A narrower catalog means less expressive power for agents; a broader catalog means more surface area for misuse. This is the core tradeoff that different use cases will resolve differently (enterprise: tight catalog + tight brand; consumer app: wider catalog for richer interaction).

## Relationship to latent vs. deterministic

From [[concepts/latent-vs-deterministic]]: the distinction between LLM judgment and deterministic computation. Generative UI lives at this boundary — the *composition* of a UI (which components to use, how to arrange them, what data model to expose) is a latent/LLM task, while the *rendering* is deterministic (native component code). A2UI formalizes this split: the agent owns the structure, the client owns the rendering.

## Related pages

- [[concepts/a2a-protocol]] — transport for A2UI messages
- [[concepts/agentic-ai]] — multi-agent mesh context
- [[concepts/mcp-server]] — MCP Apps comparison
- [[concepts/latent-vs-deterministic]] — structural split between LLM composition and deterministic rendering
- [[entities/a2ui]] — the reference open-source implementation
- [[entities/google]] — A2UI originator
- [[entities/copilotkit]] — AG UI / day-0 A2UI collaborator
- [[sources/google-a2ui-introduction]] — v0.8 announcement (conceptual foundation)
- [[sources/google-a2ui-v09]] — v0.9 release (production hardening, ecosystem growth)
