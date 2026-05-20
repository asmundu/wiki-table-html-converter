#!/bin/bash
# Convenience wrapper for Wikipedia table extraction
# Usage: ./convert-wiki-table.sh "Page Title" "Table Name"
# Output filename is automatically generated from table name and timestamp

if [ $# -ne 2 ]; then
    echo "Usage: ./convert-wiki-table.sh \"Page Title\" \"Table Name\""
    echo ""
    echo "The output HTML filename is automatically generated."
    echo ""
    echo "Examples:"
    echo "  ./convert-wiki-table.sh \"List of countries by population\" \"Countries by population\""
    echo "  ./convert-wiki-table.sh \"All-time Olympic Games medal tables\" \"Medal\""
    exit 1
fi

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PYTHON_SCRIPT="$SCRIPT_DIR/.github/skills/wikipedia-table-to-html/scripts/extract_table.py"

if [ ! -f "$PYTHON_SCRIPT" ]; then
    echo "Error: Cannot find extract_table.py"
    exit 1
fi

python3 "$PYTHON_SCRIPT" "$1" "$2"
