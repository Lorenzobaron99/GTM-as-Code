---
name: code_extractor
description: Reads a repository's code to find ground truth about what it does.
---

# Skill: @code_extractor

This skill is the Technical Anchor for the `clawback` project. It reads a target repository to understand its technical reality, ignoring marketing language.

## Commands

### `extract`

Analyzes a dependency manifest file (like `package.json`) to extract key information.

#### Usage

```bash
# From the clawback project directory
# Make sure the venv is active
./venv/bin/python3 main.py extract <path_to_package.json>
```

#### Example

```bash
./venv/bin/python3 main.py extract ./test_package.json
```

#### Output

Prints a summary of the project's name, description, dependencies, and dev dependencies.
