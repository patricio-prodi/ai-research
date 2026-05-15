---
type: concept
title: "Progressive Disclosure"
aliases: [progressive loading, three-level loading, skill progressive disclosure]
sources: [vijaykumar-skill-md-deep-dive]
related_concepts: [skill-files, thin-harness-fat-skills, resolvers]
related_entities: [anthropic]
last_updated: 2026-05-15
---

# Progressive Disclosure

The loading mechanism that makes large skill libraries tractable: an agent loads only minimal metadata for all installed skills at startup, escalating to full instructions and then deep reference materials only when a skill is actually selected and needed. Described by [[entities/ab-vijay-kumar|A B Vijay Kumar]] as "the core design principle" of the Agent Skills system in [[sources/vijaykumar-skill-md-deep-dive]].

## The three levels

**Level 1 — Metadata only (~100 tokens per skill)**

At session start (or when skill files change), the agent scans all installed skill directories and reads only the YAML frontmatter `name` and `description` fields. This catalog is embedded into the system prompt. Cost: roughly 100 tokens per installed skill regardless of how large the skill body is.

**Level 2 — Full instructions (<5,000 tokens, ideally)**

When the LLM's routing decision identifies a skill as relevant to the current request, the full `SKILL.md` body loads into the active context. This is the playbook — step-by-step workflows, examples, code patterns, domain-specific rules. The spec recommends keeping this under 5,000 tokens.

**Level 3 — Deep reference material (only when needed)**

If the skill's body instructions reference supplementary files in `scripts/`, `references/`, or `assets/` directories, the agent can selectively load those too. Examples: a form-filling guide, a migration risk catalog, an exhaustive API reference, executable Python/Bash scripts. There is no practical limit on the total knowledge bundled at this level — it is invisible unless actually needed.

## Why it matters

Without progressive disclosure, every installed skill would add its full body to the system prompt on startup. Ten skills at 5,000 tokens each would consume 50,000 tokens before any user message. With progressive disclosure, ten skills cost ~1,000 tokens at Level 1 — negligible.

> "Install ten skills, and your agent's context window would be stuffed with instructions, leaving barely any room for the actual conversation. With progressive disclosure, you can have dozens or even hundreds of skills installed, and the overhead is negligible."
— [[sources/vijaykumar-skill-md-deep-dive]]

## Graceful degradation

The system degrades cleanly. A simple skill with just a `SKILL.md` file and no supplementary directories works perfectly at two levels instead of three. A skill with a massive reference library costs nothing extra until those references are actually referenced by the body instructions. No caching layer, no separate service, no startup penalty beyond reading a few hundred bytes of YAML per skill.

## Implementation in Claude Code

In [[entities/anthropic|Anthropic]]'s Claude Code, Level 1 discovery happens on session start and — uniquely — also on live file change (file watching). This means editing a `SKILL.md` and saving it updates the agent's behavior on the very next interaction, with no restart. Useful for skill development; risky for editing production skills during an active task.

## Relationship to the description field

Because Level 1 is the *only* representation of a skill that the LLM sees when making its routing decision, the `description` field in frontmatter is the single most important piece of a skill. It must pack enough signal — trigger words, situations, explicit negative exclusions — into ~100 tokens to guide reliable routing. See [[concepts/skill-files]] for description engineering guidance.

## Relationship to resolvers

[[concepts/resolvers]] is Garry Tan's framing of the same routing problem: when task type X appears, load document Y. Progressive disclosure is the formal specification of how that routing works inside the Agent Skills standard — the metadata scan is the resolver table, the LLM routing decision is the lookup, and Level 2/3 loading is the result.

## Related pages

- [[concepts/skill-files]] — what gets loaded at each level
- [[concepts/resolvers]] — Tan's complementary framing of context routing
- [[concepts/thin-harness-fat-skills]] — the architecture progressive disclosure enables
- [[sources/vijaykumar-skill-md-deep-dive]]
