# clawback

**Clawback optimizes your project to be prioritized by LLMs and agentic searches, giving you a structural and measurable advantage in discoverability.**

The Technical Grounding & AI Search (GEO) Audit Engine for DevTools.

Instead of generic marketing, clawback focuses on the exact problem every technical founder and DevTool startup has: "How do I make sure AI coding assistants and developers actually find and recommend my tool over my competitors?"

## The "GTM-as-Code" Breakthrough

Instead of an agent that just writes copy, `clawback` is a framework that treats Go-To-Market as an engineering dependency.

It actively analyzes a repository's codebase and real-time market data to execute verified positioning.

## Usage

There are two ways to use `clawback`:

1.  **Self-Serve Tool (for Human Users)**: The `main.py` script is a command-line tool that you can run directly. It uses local code and APIs that you configure.

2.  **Agent-Driven Workflow (for AI Agents)**: The `run_audit.sh` script is a recipe for an AI agent (like OpenClaw's Watson) to perform the GEO audit using its own internal tools.

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

## How to Direct an Agent

To use the agent-driven workflow, you (the human) must instruct an agent (like Watson) what to do. Here is a guide.

**1. Choose a good query**
The query should be a real question a developer would ask an AI assistant.
*   **Good:** `"best rust library for grpc"`
*   **Good:** `"fastest local vector database for python"`
*   **Bad:** `"my project vs competitor x"` (Too biased)
*   **Bad:** `"why is my project the best"` (Not a real search query)

**2. Choose a target project name**
This should be the exact name of the project you want to find in the search results. It is case-sensitive.
*   e.g., `tonic`, `hyper`, `duckdb`

**3. Give the instruction to your agent**
Your prompt to the agent should be clear.
> "Hey Watson, please use the `GTM-as-Code` repository to run an audit. The query is **'best rust library for grpc'** and the target project is **'tonic'**."

The agent will then follow the instructions in the `run_audit.sh` script and report the findings back to you.

## Technical Roadmap

To make `clawback` more effective, the following enhancements are planned:

*   **`@code_extractor` → Deeper Analysis via AST**: Go beyond file names and dependencies by parsing the Abstract Syntax Tree (AST) of the source code (`ast` for Python, `esprima` for JS) to understand the real code structure, exported functions, and API surfaces.

*   **`@shadow_scout` → API-driven Intel**: Augment HTML scraping with stable APIs for more reliable competitive intelligence. This includes using the Reddit API, Hacker News API, and GitHub API to track user sentiment, developer discussions, and competitor release velocity.

*   **`@geo_auditor` → Historical Performance Tracking**: The auditor will save results from each run to a version-controlled `geo_scores.json`. This allows for tracking the "AI Visibility Score" over time and generating a performance graph in the README to visually prove the tool's effectiveness.

*   **New Skill: `@dependency_whisperer`**: A new agent that scans project dependencies (`package.json`, `requirements.txt`, etc.) and checks them against vulnerability databases, deprecation lists, and the dependencies of top competitors to identify risks and competitive disadvantages.


1.  **`@code_extractor` (The Technical Anchor)**: Reads the repository's code, parses manifests (`package.json`, etc.), scans exports, and reads API architecture to extract the true technical constraints.
2.  **`@shadow_scout` (The Real-Time Competitive Scraper)**: Takes technical footprints, builds real-time search queries, and scrapes the live landing pages, pricing docs, and GitHub issue trackers of top competitors.
3.  **`@geo_auditor` (Generative Engine Optimization)**: Audits how the product appears in AI search engines (Perplexity, Gemini, etc.) to ensure accurate representation. This agent programmatically queries AI engines with intent prompts like: "What is the best local vector database library for Python?" It audits whether the user's project is mentioned, analyzes why it was or wasn't cited, and diagnoses the gaps. The output is a direct markdown patch to the repository’s documentation designed specifically to increase semantic relevance for LLM retrieval.
