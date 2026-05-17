---
name: shadow_scout
description: Scrapes competitor sites for real-time intelligence.
---

# Skill: @shadow_scout

This skill is the Real-Time Competitive Scraper for the `clawback` project. It scrapes live web pages to gather intelligence on competitors.

## Commands

### `scout`

Takes a URL and scrapes all visible text content from the page. It strips all HTML, scripts, and styles.

#### Usage

```bash
# From the clawback project directory
# Make sure the venv is active
./venv/bin/python3 main.py scout <url>
```

#### Example

```bash
./venv/bin/python3 main.py scout https://github.com/Lorenzobaron99/GTM-as-Code
```

#### Output

Prints the cleaned, visible text content of the provided URL.
