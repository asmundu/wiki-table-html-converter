---
name: wikipedia-table-to-html
description: 'Convert Wikipedia tables to beautiful HTML reports. Use when you need to extract and style a table from Wikipedia into a standalone, professional HTML document.'
argument-hint: 'wiki-page table-name'
user-invocable: true
---

# Wikipedia Table to HTML Report

Convert any table from a Wikipedia page into a professionally styled, standalone HTML report with just two parameters.

## When to Use

- Extract reference data from Wikipedia tables
- Create shareable, formatted reports from Wikipedia data
- Style and repurpose Wikipedia tables for presentations or documentation
- Generate one-off data snapshots without writing custom parsing code

## Parameters

The skill accepts exactly **two parameters** (the output filename is automatic):

1. **wiki-page**: The Wikipedia page title (e.g., "List of countries by population")
2. **table-name**: The table header/name to extract (e.g., "Countries by population")

## Procedure

1. Provide the Wikipedia page title and target table name
2. The [extraction script](./scripts/extract_table.py) fetches and parses the table
3. An HTML report is automatically generated with a name derived from the table name and timestamp
4. Output file opens ready to view in any browser

## What You Get

- **Clean HTML output**: Self-contained, no external dependencies
- **Professional styling**: Responsive design with alternating row colors and hover effects
- **Automatic naming**: Filename generated from table name + timestamp (e.g., `countries_by_population_20260520_143000.html`)
- **Metadata**: Table source, extraction timestamp, and row count included
- **Ready to share**: Single HTML file can be emailed or hosted

## Example

```
wiki-page: "List of countries by population"
table-name: "Countries by population"
```

Output: `countries_by_population_20260520_143000.html` (automatically named)

## Technical Details

- Uses Wikipedia's Python API for reliable table extraction
- Automatically handles table formatting variations
- Preserves data types and links where possible
- CSS-only styling (no JavaScript required for basic functionality)
- Filename auto-generated from table name and current timestamp
