---
name: geo_auditor
description: Audits a project's visibility in AI search engines.
---

# Skill: @geo_auditor

This skill handles Generative Engine Optimization (GEO). It audits how a project is perceived and ranked by AI search engines and coding assistants for specific queries.

## Commands

### `audit`

**(Current Implementation: Placeholder)**

Takes a search query and a target project name, and simulates auditing AI search engines to see if the project is mentioned.

#### Usage

```bash
# From the clawback project directory
# Make sure the venv is active
./venv/bin/python3 main.py audit "<query>" "<project_name>"
```

#### Example

```bash
./venv/bin/python3 main.py audit "best local vector db for python" "duckdb"
```

#### Output

Currently, this command prints a placeholder message indicating whether the project was found and gives a generic recommendation. The real logic will involve agentic queries to actual AI models.
