#!/bin/bash
#
# run_audit.sh - An agent-driven workflow for the @geo_auditor skill.
#
# This script is designed to be executed by an OpenClaw agent (or similar).
# It cannot be run directly by a human user without the agent's tools.
#
# Usage: ./run_audit.sh "your search query" "your_project_name"

set -e

QUERY="$1"
TARGET_PROJECT="$2"

if [ -z "$QUERY" ] || [ -z "$TARGET_PROJECT" ]; then
    echo "Usage: $0 \"<query>\" \"<target_project>\""
    exit 1
fi

echo "--- Agent-Driven GEO Audit ---"
echo "Query: '$QUERY'"
echo "Target Project: '$TARGET_PROJECT'"
echo ""
echo "INSTRUCTION TO AGENT: The following command needs to be executed using your internal 'web_search' tool."
echo "If you do not have 'web_search', use another AI-powered search tool."
echo "Analyze the output for any mention of '$TARGET_PROJECT' and report the findings."
echo ""
echo "COMMAND: web_search(query=\"$QUERY\")"
