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

The skill accepts exactly **two parameters**:

1. **wiki-page**: The Wikipedia page title (e.g., "List of countries by population")
2. **table-name**: The table header/name to extract (e.g., "Countries by population, 2024")

## Procedure

1. Provide the Wikipedia page title and target table name
2. The [extraction script](./scripts/extract_table.py) fetches and parses the table
3. The [HTML template](./assets/report.html) renders the table with professional styling
4. Output is saved as a timestamped HTML file ready to share or open in browser

## What You Get

- **Clean HTML output**: Self-contained, no external dependencies
- **Professional styling**: Responsive design with sorting capability
- **Metadata**: Table source, extraction timestamp, and row count included
- **Ready to share**: Single HTML file can be emailed or hosted

## Example

```
wiki-page: "List of countries by population"
table-name: "Population and area by country, region, or territory"
```

Output: `wikipedia-table-report-[timestamp].html`

## Technical Details

- Uses Wikipedia's Python API for reliable table extraction
- Automatically handles table formatting variations
- Preserves data types and links where possible
- CSS-only styling (no JavaScript required for basic functionality)
