#!/bin/bash
# Convenience wrapper for Wikipedia table extraction
# Usage: ./convert-wiki-table.sh "Page Title" "Table Name" [output.html]

if [ $# -lt 2 ]; then
    echo "Usage: ./convert-wiki-table.sh \"Page Title\" \"Table Name\" [output.html]"
    echo ""
    echo "Examples:"
    echo "  ./convert-wiki-table.sh \"List of countries by population\" \"Countries by population\""
    echo "  ./convert-wiki-table.sh \"List of countries by population\" \"Countries by population\" my-report.html"
    exit 1
fi

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PYTHON_SCRIPT="$SCRIPT_DIR/.github/skills/wikipedia-table-to-html/scripts/extract_table.py"

if [ ! -f "$PYTHON_SCRIPT" ]; then
    echo "Error: Cannot find extract_table.py"
    exit 1
fi

python3 "$PYTHON_SCRIPT" "$1" "$2" "$3"
