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
- Pages created: [[concepts/yc-application]], [[concepts/founder-traction]], [[entities/hendrick]], [[entities/conveo]]
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
