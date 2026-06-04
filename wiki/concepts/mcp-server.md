---
type: concept
title: "Model Context Protocol (MCP) Server"
aliases: [MCP, MCP server]
sources: [speakeasy-agent-framework-comparison, gaiji-beyond-rag, google-a2ui-introduction]
related_concepts: [agent-framework, knowledge-ontology, generative-ui]
related_entities: [gram]
last_updated: 2026-05-20
---

# Model Context Protocol (MCP) Server

A Model Context Protocol (MCP) Server provides a standardized way for AI agents and LLMs to discover and interact with external tools, APIs, and data sources. 

## Role in Agent Frameworks
Modern [[agent-framework]] tools increasingly support MCP to streamline tool integration:
- Frameworks like [[LangChain]], [[CrewAI]] (via `MCPServerAdapter`), [[PydanticAI]], [[OpenAI Agents SDK]], [[Vercel AI SDK]], and [[n8n]] offer native or adapter-based support for MCP servers.
- Platforms like [[Gram]] are specifically designed for building production-ready MCP servers, allowing teams to curate focused toolsets and compose atomic tools into workflows to prevent agents from being confused by raw API exposure.

## MCP as a Knowledge Toolbox

[[entities/lassaad-gaiji|Gaiji]] in [[sources/gaiji-beyond-rag|"Beyond RAG"]] describes an **MCP toolbox** pattern that exposes two complementary routes to a single LLM or domain-specific agent:

1. **Semantic search tool** — vector-based Q&A retrieval (RAG side)
2. **Structured knowledge base** — topic-based lookup from the validated ontology (no vector search needed)

This lets the LLM choose the right access pattern for a given query. See [[concepts/knowledge-ontology]] for the full extraction pipeline.

## MCP Apps: UI as a resource

In November 2025, MCP introduced **MCP Apps** — a standard for servers to provide interactive interfaces. A tool returns a `ui:// URI`; the client fetches the content and renders it in a sandboxed `iframe`.

**How this differs from [[concepts/generative-ui|A2UI]]** (from [[sources/google-a2ui-introduction|Google A2UI (2025)]]):

- **MCP Apps** treat UI as a resource: the server controls the HTML content, the client sandboxes it. Server has more expressive freedom; the rendered UI may not match the host app's styling or branding.
- **A2UI** is native-first: the agent sends a blueprint of components from the client's pre-approved catalog; the client renders with its own widgets. The UI always inherits host app branding and accessibility.

Neither approach is universally superior. MCP Apps give servers more control; A2UI gives clients more control. The tradeoffs map to use cases: enterprise apps (tight brand requirements → A2UI), general-purpose tools (server controls experience → MCP Apps).

**Update (A2UI v0.9, April 2026):** A2UI now supports MCP as a transport layer — A2UI messages can be sent *over* MCP in addition to A2A, AG UI, WebSockets, and REST. The two standards can be operationally combined: MCP for tool invocation, A2UI (over MCP) for UI responses. Google also noted "better MCP Apps integrations" on their v0.9 roadmap.
