import json
import argparse

def analyze_package_json(file_path):
    """
    Reads and analyzes a package.json file to extract key info.
    """
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)

        name = data.get('name', 'N/A')
        description = data.get('description', 'N/A')
        dependencies = data.get('dependencies', {})
        dev_dependencies = data.get('devDependencies', {})

        print(f"--- Analysis of {file_path} ---")
        print(f"Project Name: {name}")
        print(f"Description: {description}")
        print("\\nDependencies:")
        if dependencies:
            for dep, version in dependencies.items():
                print(f"  - {dep}: {version}")
        else:
            print("  (None)")
        
        print("\\nDev Dependencies:")
        if dev_dependencies:
            for dep, version in dev_dependencies.items():
                print(f"  - {dep}: {version}")
        else:
            print("  (None)")

    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from {file_path}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

import requests
from bs4 import BeautifulSoup

def scout_url(url):
    """
    Scrapes the visible text content from a URL.
    """
    print(f"--- Scouting {url} ---")
    try:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        response.raise_for_status()  # Raise an exception for bad status codes
        soup = BeautifulSoup(response.text, 'html.parser')

        # Remove script and style elements
        for script_or_style in soup(["script", "style"]):
            script_or_style.decompose()

        # Get text and clean it up
        text = soup.get_text()
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = '\\n'.join(chunk for chunk in chunks if chunk)

        print(text)

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while scouting {url}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def audit_geo(query, target_project):
    """
    (Placeholder) Audits how a project appears in AI search engines for a given query.
    """
    print(f"--- GEO Audit ---")
    print(f"Query: '{query}'")
    print(f"Target Project: '{target_project}'")
    print("\\n(Placeholder) Simulating queries to AI search engines...")
    print("Result: Target project was NOT found in the top results.")
    print("Recommendation: (Placeholder) Improve documentation with keywords related to the query.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Clawback: A GTM-as-Code tool.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Sub-parser for the 'extract' command
    parser_extract = subparsers.add_parser(
        "extract",
        help="Analyze a package.json file.",
        description="Reads a package.json file and extracts key information like name, description, and dependencies."
    )
    parser_extract.add_argument("file", help="Path to the package.json file.")

    # Sub-parser for the 'scout' command
    parser_scout = subparsers.add_parser(
        "scout",
        help="Scrape the visible text from a URL.",
        description="Takes a URL and extracts all visible text content, stripping HTML tags, scripts, and styles."
    )
    parser_scout.add_argument("url", help="The URL to scrape.")

    # Sub-parser for the 'audit' command
    parser_audit = subparsers.add_parser(
        "audit",
        help="(Placeholder) Audit a project's visibility in AI search.",
        description="Simulates querying AI search engines to see if a project is mentioned for a specific query."
    )
    parser_audit.add_argument("query", help="The search query to test (e.g., 'best vector db').")
    parser_audit.add_argument("project", help="The name of the project to look for.")


    args = parser.parse_args()

    if args.command == "extract":
        analyze_package_json(args.file)
    elif args.command == "scout":
        scout_url(args.url)
    elif args.command == "audit":
        audit_geo(args.query, args.project)
