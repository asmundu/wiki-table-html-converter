#!/usr/bin/env python3
"""
Extract a Wikipedia table and convert it to HTML report.

Usage:
    python extract_table.py <wiki_page> <table_name>

The output filename is automatically generated based on the table name and timestamp.
"""

import sys
import re
from datetime import datetime

try:
    import wikipedia
    import pandas as pd
    import requests
except ImportError:
    print("Error: Required packages not installed.")
    print("Install with: pip install wikipedia pandas requests")
    sys.exit(1)


def sanitize_filename(text: str) -> str:
    """Convert text to a safe filename."""
    # Remove special characters and spaces
    sanitized = re.sub(r'[^a-zA-Z0-9_-]', '', text.replace(' ', '_'))
    # Remove consecutive underscores
    sanitized = re.sub(r'_+', '_', sanitized)
    # Limit length
    return sanitized[:50]


def extract_wikipedia_table(wiki_page: str, table_name: str) -> pd.DataFrame:
    """
    Extract a specific table from a Wikipedia page.
    
    Args:
        wiki_page: Wikipedia page title
        table_name: Name/header of the table to extract
        
    Returns:
        pandas DataFrame containing the table
    """
    try:
        page = wikipedia.page(wiki_page)
    except wikipedia.exceptions.DisambiguationError as e:
        print(f"Error: '{wiki_page}' is ambiguous. Did you mean one of:")
        for option in e.options[:5]:
            print(f"  - {option}")
        sys.exit(1)
    except wikipedia.exceptions.PageError:
        print(f"Error: Wikipedia page '{wiki_page}' not found.")
        sys.exit(1)
    
    # Fetch page content with proper User-Agent to avoid 403 errors
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    try:
        response = requests.get(page.url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error: Failed to fetch page content: {e}")
        sys.exit(1)
    
    # Parse tables from the HTML
    try:
        tables = pd.read_html(response.text)
    except ValueError as e:
        print(f"Error: No tables found on page '{wiki_page}'")
        sys.exit(1)
    
    if not tables:
        print(f"Error: No tables found on page '{wiki_page}'")
        sys.exit(1)
    
    # Try to find table by name (first row contains headers)
    target_table = None
    for table in tables:
        # Check if any column header matches the table name (partial match)
        if any(table_name.lower() in str(col).lower() for col in table.columns):
            target_table = table
            break
    
    # If not found by header, use first table
    if target_table is None:
        print(f"Warning: Table '{table_name}' not found. Using first table from page.")
        target_table = tables[0]
    
    return target_table


def create_html_report(df: pd.DataFrame, wiki_page: str, table_name: str) -> str:
    """
    Create a beautiful HTML report from the DataFrame.
    
    Args:
        df: pandas DataFrame
        wiki_page: Original Wikipedia page
        table_name: Table name/description
        
    Returns:
        Path to created HTML file
    """
    # Generate automatic filename based on table name and timestamp
    sanitized_table = sanitize_filename(table_name)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"{sanitized_table}_{timestamp}.html"
    
    # Convert DataFrame to HTML table
    table_html = df.to_html(classes="data-table", border=0)
    
    # Create complete HTML document with styling
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Wikipedia Table Report: {table_name}</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 40px 20px;
        }}
        
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 10px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
            overflow: hidden;
        }}
        
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 40px;
            text-align: center;
        }}
        
        .header h1 {{
            font-size: 2.5em;
            margin-bottom: 10px;
            font-weight: 700;
        }}
        
        .header p {{
            font-size: 1.1em;
            opacity: 0.9;
        }}
        
        .metadata {{
            background: #f8f9fa;
            padding: 20px 40px;
            border-bottom: 1px solid #e9ecef;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            font-size: 0.95em;
        }}
        
        .metadata-item {{
            display: flex;
            flex-direction: column;
        }}
        
        .metadata-label {{
            font-weight: 600;
            color: #667eea;
            margin-bottom: 5px;
        }}
        
        .metadata-value {{
            color: #495057;
        }}
        
        .table-container {{
            padding: 40px;
            overflow-x: auto;
        }}
        
        .data-table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 0.95em;
        }}
        
        .data-table thead {{
            background: #667eea;
            color: white;
        }}
        
        .data-table th {{
            padding: 15px;
            text-align: left;
            font-weight: 600;
            white-space: nowrap;
        }}
        
        .data-table td {{
            padding: 12px 15px;
            border-bottom: 1px solid #e9ecef;
        }}
        
        .data-table tbody tr {{
            transition: background-color 0.2s ease;
        }}
        
        .data-table tbody tr:hover {{
            background-color: #f8f9fa;
        }}
        
        .data-table tbody tr:nth-child(even) {{
            background-color: #f8f9fa;
        }}
        
        .footer {{
            background: #f8f9fa;
            padding: 20px 40px;
            text-align: center;
            color: #6c757d;
            font-size: 0.9em;
            border-top: 1px solid #e9ecef;
        }}
        
        @media (max-width: 768px) {{
            .header {{
                padding: 20px;
            }}
            
            .header h1 {{
                font-size: 1.8em;
            }}
            
            .metadata {{
                grid-template-columns: 1fr;
                padding: 15px 20px;
            }}
            
            .table-container {{
                padding: 20px;
            }}
            
            .data-table th, .data-table td {{
                padding: 8px 10px;
                font-size: 0.85em;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>{table_name}</h1>
            <p>Data sourced from Wikipedia</p>
        </div>
        
        <div class="metadata">
            <div class="metadata-item">
                <span class="metadata-label">Source Page</span>
                <span class="metadata-value">{wiki_page}</span>
            </div>
            <div class="metadata-item">
                <span class="metadata-label">Extraction Date</span>
                <span class="metadata-value">{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</span>
            </div>
            <div class="metadata-item">
                <span class="metadata-label">Total Rows</span>
                <span class="metadata-value">{len(df):,}</span>
            </div>
            <div class="metadata-item">
                <span class="metadata-label">Total Columns</span>
                <span class="metadata-value">{len(df.columns)}</span>
            </div>
        </div>
        
        <div class="table-container">
            {table_html}
        </div>
        
        <div class="footer">
            <p>Generated by Wikipedia Table to HTML Converter | Data sourced from Wikipedia</p>
        </div>
    </div>
</body>
</html>"""
    
    # Write to file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    return output_file


def main():
    if len(sys.argv) != 3:
        print("Usage: python extract_table.py <wiki_page> <table_name>")
        print("\nThe output HTML filename is automatically generated from the table name and timestamp.")
        print("\nExample:")
        print('  python extract_table.py "World population" "Global"')
        print("\nOutput: global_20260520_143000.html")
        sys.exit(1)
    
    wiki_page = sys.argv[1]
    table_name = sys.argv[2]
    
    print(f"Fetching Wikipedia page: {wiki_page}")
    df = extract_wikipedia_table(wiki_page, table_name)
    
    print(f"Found table with {len(df)} rows and {len(df.columns)} columns")
    print("Generating HTML report...")
    
    output_path = create_html_report(df, wiki_page, table_name)
    
    print(f"✓ Report saved to: {output_path}")
    return output_path


if __name__ == "__main__":
    main()
