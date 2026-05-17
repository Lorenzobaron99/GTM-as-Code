# clawback

The Technical Grounding & AI Search (GEO) Audit Engine for DevTools.

Instead of generic marketing, clawback focuses on the exact problem every technical founder and DevTool startup has: "How do I make sure AI coding assistants and developers actually find and recommend my tool over my competitors?"

## The "GTM-as-Code" Breakthrough

Instead of an agent that just writes copy, `clawback` is a framework that treats Go-To-Market as an engineering dependency.

It actively analyzes a repository's codebase and real-time market data to execute verified positioning.

## How It Works

```
[Target Repo / Codebase] ──► [AST/Code Analyzer Skill] ──┐
                                                     ├──► [Clawback Swarm] ──► [1. THE_TRUTH.md]
[Competitor Sites]       ──► [Live Scraping Skill]     │                          [2. .agents/product-marketing.md]
[AI Search Engines]      ──► [Agentic Query Testing] ──┘
```

The system generates two specific, code-native files back into the workspace:

1.  **`THE_TRUTH.md`**: A brutal, un-fluffed teardown of what the code *actually* does vs. what competitors' code does (zero marketing fluff allowed).
2.  **`.agents/product-marketing.md`**: A machine-readable context file designed to be committed to the repo, ensuring other AI agents (Cursor, Claude Code, Copilot) explain the product accurately to end-users.

## Core Agent Skills

1.  **`@code_extractor` (The Technical Anchor)**: Reads the repository's code, parses manifests (`package.json`, etc.), scans exports, and reads API architecture to extract the true technical constraints.
2.  **`@shadow_scout` (The Real-Time Competitive Scraper)**: Takes technical footprints, builds real-time search queries, and scrapes the live landing pages, pricing docs, and GitHub issue trackers of top competitors.
3.  **`@geo_auditor` (Generative Engine Optimization)**: Audits how the product appears in AI search engines (Perplexity, Gemini, etc.) to ensure accurate representation.
