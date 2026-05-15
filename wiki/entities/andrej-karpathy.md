---
type: entity
name: "Andrej Karpathy"
kind: person
aliases: [karpathy]
sources: [karpathy-llm-knowledge-bases, karpathy-llm-wiki-gist]
related_concepts: [llm-wiki, rag-vs-wiki]
last_updated: 2026-05-14
---

# Andrej Karpathy

AI researcher and educator. One of the most prominent practitioners in the field.

## Background

- **Founding researcher at [[entities/openai|OpenAI]]** — part of the original team.
- **Former Director of AI at Tesla** — led Autopilot's computer vision and neural network work.
- Known for highly accessible technical writing and teaching (e.g., Neural Networks: Zero to Hero YouTube series, micrograd, minGPT).

## Relevance to this wiki

Karpathy publicly described a workflow shift from writing code to building LLM-maintained knowledge bases — the origin point of the [[concepts/llm-wiki|LLM Wiki]] pattern this vault implements. Two sources cover this:

- [[sources/karpathy-llm-wiki-gist]] — his own gist (primary source, 2026-04-01); the canonical description of the pattern
- [[llm-knowledge-bases-explained]] — secondhand explanation by Mehul Gupta (2026-04-12)

Key quote from [[sources/karpathy-llm-wiki-gist]]:
> "In practice, I have the LLM agent open on one side and Obsidian open on the other. The LLM makes edits based on our conversation, and I browse the results in real time — following links, checking the graph view, reading the updated pages. Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase."

His current research wiki: ~100 articles, ~400,000 words, maintained entirely by LLM.

## Stated future direction

Fine-tuning a model on the wiki to bake knowledge into model weights, eliminating the need to retrieve notes at query time.

## Related pages

- [[concepts/llm-wiki]]
- [[concepts/rag-vs-wiki]]
- [[sources/karpathy-llm-wiki-gist]]
- [[llm-knowledge-bases-explained]]
- [[entities/openai]]
