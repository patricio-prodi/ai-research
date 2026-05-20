---
title: "A2UI v0.9: The New Standard for Portable, Framework-Agnostic Generative UI- Google Developers Blog"
source: "https://developers.googleblog.com/a2ui-v0-9-generative-ui/"
author:
  - "[[Google]]"
published: 2026-04-17
created: 2026-05-18
description: "Discover A2UI v0.9, the framework-agnostic standard for Generative UI. Learn how the new Agent SDK, shared web-core library, and cross-platform renderers allow AI agents to drive your existing design system on any device with low-latency streaming."
tags:
  - "inbox"
---
developers.googleblog.com uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more](https://policies.google.com/technologies/cookies?hl=en)

## A2UI v0.9: The New Standard for Portable, Framework-Agnostic Generative UI

APRIL 17, 2026

[Google A2UI Team](https://developers.googleblog.com/search/?author=Google+A2UI+Team)

![Hero](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/Hero.original.jpg)

Generative UI allows AI agents to generate tailored UI widgets in real-time, matching the interface to the user’s specific interaction. But to move from demos to production, we need a clean separation of concerns. A2UI v0.9 is our answer; a framework-agnostic standard for declaring UI intent. It allows local or remote agents to communicate with any client application using a common language, ensuring your agent can generate your UI using your existing component catalog on any device.

## Agents can “speak” UI with your design system, no need to change.

<video controls=""><source src="https://storage.googleapis.com/gweb-developer-goog-blog-assets/original_videos/a2ui-component-catalogs.mp4" type="video/mp4"><p>Sorry, your browser doesn't support playback for this video</p></video>

A2UI is designed to work on web, mobile, and anywhere else your users are.

## What's New in A2UI v0.9

This release focuses on making it easier than ever to build agents and integrate with your existing frontends. This release hardens our internal abstractions, simplifies streaming, and improves developer experience.

- **From "Standard" to "Basic":** Frontend developers don't want new components. They already have a design system and components they use. Agents should respond dynamically, using existing front ends. We renamed our optional component set to 'Basic' to make this more clear. Check out the [component catalog](https://a2ui.org/concepts/catalogs) docs and code samples, connect A2UI to your awesome front ends.
- **A Shared Web-Core Library:** On the client side, we've introduced a shared [web-core](https://github.com/google/A2UI/tree/main/renderers/web_core) library which vastly simplifies any browser UI renderer. We've also landed the official React renderer and version-bumped all [A2UI supported renderers](https://a2ui.org/reference/renderers/) (Flutter, Lit, Angular, and React), while carving out a dedicated spot for [community renderers](https://a2ui.org/ecosystem/renderers/).
- **The Agent SDK:** Building the agent side of the equation just got a lot easier with [A2UI Agent SDK](https://a2ui.org/reference/agents/). We’ve optimized the generation pipeline with new caching layers to ensure a high-performance, low-latency UI experience.
- **New Language Features:** A2UI 0.9 adds client-defined functions (perfect for validation), client-to-server data syncing to support collaborative editing with your agent, improved error handling, and a simplified, modular schema.
- **Simplified Transports:** We've refined our transport interfaces so connecting your agents and clients is much smoother. A2UI over MCP, Websockets, REST, AG UI, A2A, or whatever you want.

<video controls=""><source src="https://storage.googleapis.com/gweb-developer-goog-blog-assets/original_videos/a2ui_scroller_Composer_2.mp4" type="video/mp4"><p>Sorry, your browser doesn't support playback for this video</p></video>

This example shows a replay of streaming chunks, slowing down and replaying scenarios across renderers

Adding A2UI to any python agent is now a simple pip install or uv add away (go and kotlin coming soon).

```shell
pip install a2ui-agent-sdk
```

Integrating A2UI into your existing agent is a straightforward 5-step process. Here’s the "Hello World" of A2UI integration:

```python
# Step 1: Define your catalog (basic or bring your own) with optional examples
my_catalog = CatalogConfig.from_path(
    name="<MY_CATALOG_NAME>",
    catalog_path=("file:///path/to/catalog.json"),
    # Optional: help LLM with "few-shot" learning
    examples_path="path/to/examples/folder/*.json"
),

# Step 2: Initialize the Schema Manager to manage A2UI Spec versions
schema_manager = A2uiSchemaManager(
    version="0.9",
    catalogs=[my_catalog],
)

# 3. Generate the System Prompt, handles A2UI instructions
system_instruction = schema_manager.generate_system_prompt(
    role_description="You are a helpful assistant great at generating UI...",
) 

# Step 4: Initialize your LLM Agent with the generated instructions
my_agent = AnyAgentFrameworkLLMAgent(instruction=system_instruction, ...)

# Step 5. Execute and Stream the UI
def handle_turn(user_query):
    llm_response = my_agent.respond(user_query)

    # In your executor the SDK helps parse, fix, and validate the LLM's JSON on the fly

    selected_catalog = schema_manager.get_selected_catalog()
    final_parts = parse_response_to_parts(llm_response, selected_catalog.validator)
    yield {
        "is_task_complete": True,
        "parts": final_parts,
    }
```

**Go Beyond the Basics**

While the example above shows a simple static integration, the A2UI agent SDK is built for production-grade complexity. Out of the box, it supports:

- **Version Negotiation:** Dynamically select the best A2UI specification version based on the client's capabilities.
- **Dynamic Catalogs:** Switch between multiple catalog schemas at runtime to match specific user permissions or device constraints.
- **Resilient Streaming:** Incrementally parse and heal LLM output, allowing the client to render UI components as they are being generated—no waiting for the full JSON block.

Explore our [Agent Samples](https://github.com/google/A2UI) to see these advanced features in action.

We are working on some neat things like better MCP Apps integrations, progressive disclosure “skills” for A2UI, human intent abstractions, PII support, and a lot more. Take a look at our updated [roadmap](https://a2ui.org/roadmap/) and be sure to show us what **you** are working on.

## The Growing Generative UI Ecosystem

A standard is only as good as the ecosystem around it, and the landscape is evolving rapidly.

![](https://www.youtube.com/watch?v=ps-gn4j3_g8)

[Link to Youtube Video](https://www.youtube.com/watch?v=ps-gn4j3_g8) (visible only when JS is disabled)

- **AG2:** Built by the creators of AutoGen, created [A2UIAgent](https://docs.ag2.ai/latest/docs/user-guide/reference-agents/a2uiagent/) as a native integrations of A2UI, see it in action in the above video.
- **A2A 1.0:** Agent-to-Agent (A2A) [1.0 protocol has officially launched](https://a2a-protocol.org/latest/announcing-1.0/). It serves as a robust transport for remote agents communicating with other agents, or simply connecting agents directly to frontends.
- **Vercel's json-renderer:** Vercel recently launched [json-renderer which supports A2UI](https://json-render.dev/docs/a2ui) as a proof of concept. This could become a dedicated renderer for A2UI for the Vercel community.
- **Oracle’s Agent Spec:** recently shipped [Agent Spec + AG UI + A2UI + AG UI](https://blogs.oracle.com/ai-and-datascience/announcing-agent-spec-for-a2ui-copilotkit-ag-ui) support; Agent Spec defines what runs, AG‑UI carries the interaction, and A2UI defines what the user touches. Swap implementations at any layer while keeping the experience stable.
- **AG-UI:** Support for connecting a broad spectrum of GenUI capabilities into agentic web apps, including A2UI, MCP Apps and Open Generative UI.

We're seeing incredible implementations of A2UI across the industry. Here are a few recent sightings:

## Personal Health Companion

The GenUI Personal Health Companion is an open-source app designed to eliminate "data silos" and "navigation fatigue" by replacing static dashboards with a modular, AI-driven interface. Developed by [Rebel App Studio](https://rebelappstudio.com/), [Codemate’s](https://codemate.com/creative-tech/) specialist Flutter team, this solution leverages real-time data orchestration to bridge the gap between fragmented medical records and wearable telemetry. Rather than forcing users to dig through sub-menus, the app utilizes a central LLM-powered chat that can dynamically generate UI widgets on the fly, surfacing critical lab results, vaccine expirations, or clinic locations based on immediate context. By grounding AI insights directly in the user’s unique health data, the app transforms passive health tracking into a proactive, intent-driven assistant built for the modern digital patient.

Dive deeper into how the Health Companion was built on [Codemate’s blog](https://codemate.com/articles/flutter-genui-demo/) —and explore the [open-source demo on GitHub](https://github.com/rebelappstudio/genui_personal_health_companion).

<video controls=""><source src="https://storage.googleapis.com/gweb-developer-goog-blog-assets/original_videos/frame-l.mp4" type="video/mp4"><p>Sorry, your browser doesn't support playback for this video</p></video>

## Personal Financial Planner

The Life Goal Simulator is an interactive demonstration of how Generative UI bridges the gap between consumer expectations and the static experiences currently offered by the financial services industry. Built by [Very Good Ventures](https://verygood.ventures/) (VGV)—a Flutter and GenUI consultancy trusted by brands like Toyota and GEICO—the app moves beyond traditional, one-size-fits-all interfaces by putting the user’s life at the center of the experience. By selecting a persona and a goal, such as saving for retirement or a first home, users hand the wheel to Gemini, which utilizes the Flutter GenUI SDK to generate a native-feeling, real-time UI from a curated catalog of interactive widgets like sliders, bar charts, and multi-selects.

Check out the [open-source code](https://github.com/VGVentures/genui_life_goal_simulator) for this demo, and you can also see a [live interactive demo](https://gcn26demo.vgv.ai/) of this experience.

<video controls=""><source src="https://storage.googleapis.com/gweb-developer-goog-blog-assets/original_videos/VGV_2.mp4" type="video/mp4"><p>Sorry, your browser doesn't support playback for this video</p></video>

### A2UI with any Agent Framework (via AG-UI)

Any agent that already speaks AG-UI can drive A2UI v0.9 on day zero. No custom integration is required. This works through AG-UI's middleware system: a small piece of code that plugs into your existing agent pipeline. It teaches your agent how to speak A2UI, wires the responses correctly, and handles streaming, converting the agent's output into components your UI can render immediately, using A2UI's built-in renderers or your own custom components.

<video controls=""><source src="https://storage.googleapis.com/gweb-developer-goog-blog-assets/original_videos/A2UI_-_AG-UI_Starter.mp4" type="video/mp4"><p>Sorry, your browser doesn't support playback for this video</p></video>

Get this starter template running in your machine

```shell
npx copilotkit@latest create my-app --framework a2ui
```

## Get Started

Ready to unshackle your agents and let them drive your front end with whatever components you have?

Check out our new [A2UI Theater](https://a2ui-composer.ag-ui.com/theater?scenario=restaurant-finder) for a replay or dive into the [A2UI.org](http://a2ui.org/) for docs, samples and dev guides to start building flexible, portable generative UIs today.