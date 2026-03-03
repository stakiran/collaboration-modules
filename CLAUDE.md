# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a **knowledge repository**, not a code repository. It contains "Collaboration Modules" — conceptual tools for flexible multi-person collaboration, authored by [sta](https://github.com/stakiran). All content is written in Japanese (UTF-8).

**Do not write code** unless explicitly instructed. Your role is to propose relevant collaboration modules and engage in discussion about them.

## Structure

- `modules/concept/` — **Conceptware**: actionable methods, mindsets, and approaches (~73 modules)
- `modules/context/` — **Contextware**: verbalized implicit customs, conventions, and practices (~16 modules)
- Each module is one Markdown file. Module name = filename or the top-level heading
- Key terms are bolded at their definition. Modules often define original terminology or coined words
- A module containing only `see: filename` is a **pointer** — the actual content lives in the referenced file

### Contextware vs Conceptware

Contextware describes existing implicit cultural patterns. Conceptware describes novel approaches usable as tools. Contextware with high novelty (not yet widely adopted) is classified as Conceptware instead.

## Key Conventions

- `AGENTS.md` is the primary instruction file (README.md redirects to it)
- `.memo/` — output directory for query responses. Do not scan unless asked
- `.context/` — user-provided context files. Do not scan unless asked
- `.log/` — log files. Gitignored
- When encountering unfamiliar terms, search other modules for definitions
- Read modules in bulk rather than one-by-one, then reason over the merged content
- Modules contain only conceptual explanations and examples — no cost-benefit analyses, case studies, or persuasive content by design
