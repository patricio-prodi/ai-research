# Wiki Log

Append-only chronological record of all wiki operations.
Format: `## [YYYY-MM-DD] {operation} | {title}`
Operations: `ingest`, `query`, `lint`, `update`, `init`

---

## [2026-04-16] init | Wiki initialized

- Schema created: `CLAUDE.md`
- Structure created: `wiki/sources/`, `wiki/concepts/`, `wiki/entities/`, `wiki/topics/`
- Pages created: `wiki/index.md`, `wiki/log.md`

## [2026-04-16] ingest | Andrej Karpathy's LLM Knowledge Bases explained

- Source page: [[llm-knowledge-bases-explained]]
- Pages created: [[concepts/llm-wiki]], [[concepts/rag-vs-wiki]], [[entities/andrej-karpathy]]
- Pages updated: none (first ingest)

## [2026-04-16] ingest | AI 2027

- Source page: [[sources/ai-2027]]
- Pages created: [[concepts/agi-timelines]], [[topics/ai-forecasting]], [[entities/openai]], [[entities/anthropic]]
- Pages updated: [[entities/andrej-karpathy]] (OpenAI founding reference)

## [2026-04-16] ingest | Resilient by design: The agentic supply chain

- Source page: [[sources/agentic-supply-chain-deloitte]]
- Pages created: [[concepts/agentic-ai]], [[topics/agentic-systems]]
- Pages updated: [[concepts/llm-wiki]] (agentic AI cross-reference), [[entities/openai]]

## [2026-04-16] ingest | Thin Harness, Fat Skills

- Source page: [[sources/garrytan-thin-harness-fat-skills]]
- Pages created: [[concepts/thin-harness-fat-skills]], [[concepts/skill-files]], [[concepts/resolvers]], [[concepts/latent-vs-deterministic]], [[concepts/diarization]], [[entities/garry-tan]], [[entities/y-combinator]]
- Pages updated: [[concepts/agentic-ai]] (architecture section added), [[topics/agentic-systems]] (third domain added), [[entities/anthropic]] (Claude Code npm leak), [[wiki/index.md]]

## [2026-05-12] ingest | Choosing an agent framework: LangChain vs LangGraph vs CrewAI vs PydanticAI vs Mastra vs Vercel AI SDK

- Source page: [[sources/speakeasy-agent-framework-comparison]]
- Pages created: [[concepts/agent-framework]], [[concepts/mcp-server]], [[concepts/durable-execution]], [[entities/speakeasy-team]], [[entities/langchain]], [[entities/langgraph]], [[entities/crewai]], [[entities/pydanticai]], [[entities/mastra]], [[entities/vercel-ai-sdk]], [[entities/n8n]], [[entities/vellum]], [[entities/gram]], [[entities/openai-agents-sdk]]
- Pages updated: [[concepts/agentic-ai]], [[topics/agentic-systems]], [[wiki/index.md]]

## [2026-05-12] ingest | Tips from Hendrick: How to Nail Your YC Application

- Source page: [[sources/hendrick-yc-application-tips]]
- Pages created: [[concepts/yc-application]], [[concepts/founder-traction]]
- Entity pages not created (curator decision): Hendrick, Conveo — referenced as plain text via [[sources/hendrick-yc-application-tips]]
- Pages updated: [[entities/y-combinator]] (added YC application section), [[wiki/index.md]]

## [2026-05-14] ingest | Beyond RAG: How to Make Your AI Actually Know Things

- Source page: [[sources/gaiji-beyond-rag]]
- Pages created: [[sources/gaiji-beyond-rag]], [[entities/lassaad-gaiji]], [[concepts/knowledge-ontology]]
- Pages updated: [[concepts/rag-vs-wiki]] (third approach: structured KB + Gaiji quote), [[concepts/mcp-server]] (MCP toolbox dual-route pattern), [[wiki/index.md]]

## [2026-05-14] ingest | LLM Wiki (Karpathy's gist — primary source)

- Source page: [[sources/karpathy-llm-wiki-gist]]
- Pages created: [[sources/karpathy-llm-wiki-gist]]
- Pages updated: [[concepts/llm-wiki]] (application domains, schema layer, CLI tools/qmd, tips and tricks, Memex quote), [[concepts/rag-vs-wiki]] (primary source citation, Karpathy quote, named RAG examples), [[entities/andrej-karpathy]] (primary vs. secondhand source distinction, new quote), [[wiki/index.md]]
- Note: this is Karpathy's own gist — the canonical first-person description of the pattern. Supersedes [[llm-knowledge-bases-explained]] as authoritative reference but both are retained.

## [2026-05-15] ingest | Deep Dive SKILL.md (Part 1/2)

- Source page: [[sources/vijaykumar-skill-md-deep-dive]]
- Pages created: [[sources/vijaykumar-skill-md-deep-dive]], [[concepts/progressive-disclosure]], [[entities/ab-vijay-kumar]]
- Pages updated: [[concepts/skill-files]] (formal spec, lifecycle phases, security, versioning, testing, comparison table; second source added), [[wiki/index.md]] (counts, all tables, coverage map)

## [2026-05-15] ingest | AI's trillion-dollar opportunity: Context graphs

- Source page: [[sources/foundation-capital-context-graphs]]
- Pages created: [[sources/foundation-capital-context-graphs]], [[concepts/context-graph]], [[concepts/decision-trace]], [[concepts/systems-of-record]], [[concepts/systems-of-agents]]
- Pages updated: [[concepts/agentic-ai]] (commercial implication: context graph as moat), [[topics/agentic-systems]] (fifth domain: systems of agents and context graphs; new open questions), [[entities/y-combinator]] (stripped broken references), [[wiki/index.md]] (counts, sources/concepts/entities tables, coverage map with "deliberately not given their own page" subsection)

## [2026-05-18] ingest | Resolvers: The Routing Table for Intelligence

- Source page: [[sources/garrytan-resolvers-routing-table]]
- Pages created: [[sources/garrytan-resolvers-routing-table]], [[concepts/context-rot]], [[entities/gbrain]]
- Pages updated: [[concepts/resolvers]] (major expansion: fractal resolvers, trigger evals, check-resolvable, self-healing, governance mandates, management metaphor), [[entities/garry-tan]] (added second source, gbrain reference, updated key positions), [[concepts/thin-harness-fat-skills]] (added second source), [[topics/agentic-systems]] (added §4 Governance: Resolver architecture; renumbered §4→6, §5→7), [[wiki/index.md]] (counts 11 sources 56 pages, new entries in sources/concepts/entities tables, coverage map additions)

## [2026-05-20] ingest | A2UI v0.9: The New Standard for Portable, Framework-Agnostic Generative UI

- Source page: [[sources/google-a2ui-v09]]
- Pages created: [[sources/google-a2ui-v09]]
- Pages updated: [[entities/a2ui]] (v0.9 status, Agent SDK features, ecosystem table, new production examples, updated renderer list), [[concepts/generative-ui]] (added §Bring your own design system, §Resilient streaming, §Ecosystem, expanded production evidence; v0.9 source added), [[concepts/a2a-protocol]] (A2A 1.0 launched; Oracle/AG2 adoption noted; v0.9 source added), [[concepts/mcp-server]] (added A2UI-over-MCP transport note, roadmap signal), [[entities/vercel-ai-sdk]] (added json-renderer generative UI signal), [[wiki/index.md]] (counts 13 sources 65 pages; new source row; coverage map: ag2, oracle, resilient-streaming)

## [2026-05-20] ingest | Introducing A2UI: An open project for agent-driven interfaces

- Source page: [[sources/google-a2ui-introduction]]
- Pages created: [[sources/google-a2ui-introduction]], [[concepts/generative-ui]], [[concepts/a2a-protocol]], [[entities/google]], [[entities/a2ui]], [[entities/copilotkit]]
- Pages updated: [[concepts/agentic-ai]] (added multi-agent mesh UI trust boundary section; linked generative-ui and a2a-protocol; added google to related_entities), [[concepts/mcp-server]] (added MCP Apps comparison section; contrast with A2UI native-first approach), [[wiki/index.md]] (counts 12 sources 64 pages; new rows in all four tables; coverage map additions for opal, flutter, ag-ui-protocol)
