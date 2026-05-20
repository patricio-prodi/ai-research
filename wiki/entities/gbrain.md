---
type: entity
name: "GBrain"
kind: product
aliases: [gbrain, GStack, OpenClaw, Hermes Agent]
sources: [garrytan-resolvers-routing-table, garrytan-thin-harness-fat-skills]
related_concepts: [resolvers, thin-harness-fat-skills, skill-files, context-rot]
last_updated: 2026-05-18
---

# GBrain

Open-source personal AI brain system created by [[entities/garry-tan|Garry Tan]]. The full architecture for building a personal mini-AGI using the [[concepts/thin-harness-fat-skills|thin harness, fat skills]] pattern with the [[concepts/resolvers|resolver]] pattern built in.

**Repository**: github.com/garrytan/gbrain

## Components

### GBrain (knowledge layer)
The memory/knowledge base component. A git repo you own, organized around a `RESOLVER.md` decision tree, directory structure (people, companies, civic, sources, etc.), and `_brain-filing-rules.md` for filing governance.

- `gbrain init` creates `RESOLVER.md`, the decision tree, and disambiguation rules automatically
- Ships with `check-resolvable` built in
- 25,000+ files in Tan's production instance
- Processes ~200 inputs/day

### GStack (coding/skills layer)
The fat skills component. A library of markdown skill files (slash commands) that call the knowledge in GBrain. 72,000+ GitHub stars as of April 2026.

**Repository**: github.com/garrytan/gstack

### OpenClaw / Hermes Agent (harness layer)
The thin harness conductor. Runs the agent loop, manages sessions, executes crons. GBrain and GStack are skills that plug into it.

## Architectural significance

GBrain is a concrete production implementation of the full architecture described in [[sources/garrytan-thin-harness-fat-skills]] and [[sources/garrytan-resolvers-routing-table]]:

- Resolver pattern is baked into `gbrain init` — not something to discover by breaking things
- check-resolvable is a built-in skill (linter for the routing table)
- Brain-writing skills are mandated to read `RESOLVER.md` before creating any page
- The system embodies the lessons Tan learned from a 20,000-line CLAUDE.md failure

## Philosophy

> "This isn't a SaaS product. It's an architecture. The source code is open. The skills are markdown. The brain is a git repo you own. If any piece disappeared tomorrow, your knowledge survives as plain text files."

## Related pages

- [[entities/garry-tan]]
- [[concepts/resolvers]]
- [[concepts/thin-harness-fat-skills]]
- [[concepts/skill-files]]
- [[sources/garrytan-resolvers-routing-table]]
- [[sources/garrytan-thin-harness-fat-skills]]
