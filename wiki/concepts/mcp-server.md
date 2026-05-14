---
type: concept
title: "Model Context Protocol (MCP) Server"
aliases: [MCP, MCP server]
sources: [speakeasy-agent-framework-comparison, gaiji-beyond-rag]
related_concepts: [agent-framework, knowledge-ontology]
related_entities: [gram]
last_updated: 2026-05-14
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
