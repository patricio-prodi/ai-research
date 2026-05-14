---
type: concept
title: "Agent Framework"
aliases: [agent frameworks, AI agent framework]
sources: [speakeasy-agent-framework-comparison]
related_concepts: [agentic-ai, durable-execution]
related_entities: [langchain, langgraph, crewai, pydanticai, mastra]
last_updated: 2026-05-12
---

# Agent Framework

An agent framework is a software platform providing abstractions, libraries, and primitives for building, deploying, and managing autonomous AI agents. 

## Types of Frameworks
According to [[speakeasy-agent-framework-comparison]], the ecosystem can be broadly divided into:
- **Code-first frameworks**: Offer libraries and primitives for developers in specific languages (e.g., Python, TypeScript). Examples include [[LangChain]], [[LangGraph]], [[CrewAI]], [[PydanticAI]], and [[Mastra]].
- **Hybrid frameworks**: Offer both a visual builder and a real code backend with parity between them. Examples include [[n8n]] and [[Vellum]].
- **SDKs**: Minimal abstractions (e.g., [[OpenAI Agents SDK]], [[Vercel AI SDK]]) that are suitable for simple linear tool-calling flows without the overhead of a full framework.

## When to use a framework
Frameworks are most valuable for intermediate-to-complex use cases involving:
- Human-in-the-loop workflows
- Multi-agent coordination
- Consistent tool schemas across a large codebase
- Built-in tracing and [[durable-execution]]

For very simple agents (2-3 linear tools), SDKs are preferred to avoid friction. For extremely complex orchestration or strict latency budgets, custom architectures might be better than fighting a framework's abstractions.
