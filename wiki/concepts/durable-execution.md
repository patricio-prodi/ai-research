---
type: concept
title: "Durable Execution"
aliases: [crash-proof execution, checkpointing]
sources: [speakeasy-agent-framework-comparison]
related_concepts: [agent-framework]
related_entities: [langgraph]
last_updated: 2026-05-12
---

# Durable Execution

Durable execution refers to the ability of an agent or workflow to persist its state across server restarts, crashes, or long-running operations, allowing it to resume execution exactly where it left off.

## Implementations in Frameworks
- **Native Support**: [[LangGraph]] achieves durable execution natively through persistent checkpoints at every state transition, enabling features like time-travel debugging (replaying from prior checkpoints) and crash recovery.
- **External Integration**: Frameworks like [[PydanticAI]], [[OpenAI Agents SDK]], and [[Vercel AI SDK]] do not have built-in crash recovery and typically rely on external durable execution engines like Temporal, DBOS, or Inngest.
