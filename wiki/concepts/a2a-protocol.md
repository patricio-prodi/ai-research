---
type: concept
title: "Agent-to-Agent Protocol (A2A)"
aliases: [A2A, A2A protocol, agent-to-agent]
sources: [google-a2ui-introduction, google-a2ui-v09]
related_concepts: [agentic-ai, generative-ui, mcp-server]
related_entities: [google]
last_updated: 2026-05-20
---

# Agent-to-Agent Protocol (A2A)

An open inter-agent communication protocol enabling agents from different organizations and platforms to collaborate in a **multi-agent mesh** — without sharing memory, tools, or context. Donated by Google to the Linux Foundation.

## Purpose

As agentic systems scale from single-org to cross-org, agents from Google, Cisco, IBM, SAP, Salesforce, and others need to interoperate. A2A provides the transport and messaging contract for this.

From [[sources/google-a2ui-introduction|Google A2UI (2025)]]:
> "This is why we collectively created the Agent-to-Agent (A2A) Protocol and donated it to the Linux Foundation: to enable agents to collaborate even when they don't share memory, tools, or context."

## Role in the generative UI stack

A2A is the transport layer; [[concepts/generative-ui|A2UI]] is the UI payload format. An orchestrator agent can:
1. Delegate work to a remote A2A subagent
2. Receive an A2UI-formatted response (a component tree blueprint)
3. Render the UI in the host application using the client's native components

This means the orchestrator can **read and reason about** the lightweight A2UI payload — unlike opaque iframe content, the structured JSON is transparent to intermediate agents.

## Relationship to MCP

[[concepts/mcp-server|MCP]] (Model Context Protocol) handles tool/resource discovery and invocation within a single agent's context. A2A handles **agent-to-agent communication across organizational boundaries**. They are complementary layers in the agentic stack, not competing standards.

## Status

- **v1.0 officially launched** April 2026 — stable protocol; governance: Linux Foundation (not Google-controlled)
- Serves as transport for both agent-to-agent communication and direct agent-to-frontend connections
- A companion protocol, **AG UI** ([[entities/copilotkit|CopilotKit]]), provides agent-frontend scaffolding and also supports A2A + A2UI
- Oracle, AG2, and other enterprise vendors have adopted A2A in their agentic stacks

## Related pages

- [[concepts/generative-ui]] — the UI payload format that travels over A2A
- [[concepts/agentic-ai]] — the multi-agent mesh context
- [[concepts/mcp-server]] — complementary protocol for tool access
- [[entities/google]] — originator, donated to Linux Foundation
- [[sources/google-a2ui-introduction]] — initial announcement
- [[sources/google-a2ui-v09]] — v0.9 release; notes A2A 1.0 launch
