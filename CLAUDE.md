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



# Collaboration Modules

## このリポジトリの概要
このリポジトリは、コラボレーション（複数人による協業）を柔軟に行う際に使える「概念的な道具」を取り揃えている。これを **コラボレーションモジュール** と呼ぶ。このリポジトリは、筆者 [sta](https://github.com/stakiran) が開発したコラボレーションモジュールを取り揃えている。

## コラボレーションモジュールについて
コラボレーションモジュールは modules/ ディレクトリ配下に配置され、1-module 1-markdown-file で書かれている。モジュール名はファイル名または冒頭の大見出しとして記述される。また重要な用語は太字で定義することが多い。独自の用語を定義したり、造語していることもある。

コラボレーションモジュールの内容は概念的な説明といくつかの具体例に留まっており、コストメリットや事例やストーリーといった説得用の情報は一切含めていない。説得はこのリポジトリの責務ではない。このリポジトリはあくまでも、コラボレーションモジュールを提案することで読者のゼロをイチに近づけることにフォーカスする。

## コラボレーションモジュールのタイプについて
コラボレーションモジュールには Context と Concept がある。

Context は個人や組織が持つ特定の文脈を表現したものである。特に慣習（暗黙的な文化）、慣例（暗黙的なルール）、慣行（現場の実態）を言語化したものだ。しかし言語化は粗いものであり、特定の文脈を深く表現したものではない。このタイプのコラボレーションモジュールを **Contextware** と呼ぶ。 modules/context/ 配下に配置される。

Concept は何らかのやり方、考え方、あり方を指す。道具として使うことができる。ただし想定ターゲットや期待効果や具体的なプロセスといった細かい情報は扱っていない。このタイプのコラボレーションモジュールを **Conceptware** と呼ぶ。 modules/concept/ 配下に配置される。

### Contextware が Conceptware として扱われるケース
Contextware であっても新規性が高いものは Conceptware として扱う。これは Contextware が現代の、既存の暗黙的な文脈を表現するものだからだ。

例を挙げよう。コラボレーションモジュール「Full Four」にはフルリモート、フルフレックス、フルアシンク、フルマスクの 4 つのモジュールがある。フルアシンクとフルマスクについては、概念的には難しくないが、現時点(2026年2月)でまともに運用できている事例は皆無に等しい。Contextware と言えるほど既存ではなく、新規性が高いと言えよう。一方でフルリモートとフルフレックスについては、すでに定着している組織も多く、既存と言えよう。そもそも言葉からして既存である。全体としては Full Four は Contextware とみなしているが、これは筆者の主観である。つまり Full Four はまだまだ Contextware と言えるほど定着していない、と言っているに等しい。

このように、文脈を言語化したものであっても、その新しさによって Conceptware となることがある。この新しさの判断は筆者の主観で行う。

## コラボレーションモジュール・ポインタについて
あるコラボレーションモジュールのファイル内容が `see: ファイル名` または `see: モジュール名` とだけ書かれていることがある。これはポインタであり、実際の内容はポインタが指す先のファイルに記述されている。ファイル中のどこに記載されているかは不明であり、探す必要がある。

## ディレクトリ構造
- .memo/
    - 問い合わせに対する回答をファイルに出したい場合に使うディレクトリ
    - このディレクトリは走査しなくても良い。明示的に指示されたときだけ走査せよ
- .context/
    - 利用者は事前に周知させたいコンテキストを置くためのディレクトリ
    - このディレクトリは走査しなくても良い。明示的に指示されたときだけ走査せよ
- tools/
    - コラボレーションモジュールを道具として使うためのヒントを置くディレクトリ
    - このディレクトリは走査しなくても良い。明示的に指示されたときだけ走査せよ
- old/
    - コラボレーションモジュールのリポジトリ構成の履歴、特に古い版を置いておくディレクトリ
    - このディレクトリは走査しなくても良い。明示的に指示されたときだけ走査せよ
