#!/usr/bin/env python3
"""
Extract a Wikipedia table and convert it to HTML report.

Usage:
    python extract_table.py <wiki_page> <table_name>
"""

import sys
import re
import os
from datetime import datetime

try:
    import pandas as pd
    import requests
except ImportError:
    print("Error: Required packages not installed.")
    print("Install with: pip install pandas requests lxml")
    sys.exit(1)


def sanitize_filename(text: str) -> str:
    """Convert text to a safe filename."""
    sanitized = re.sub(r'[^a-zA-Z0-9_-]', '', text.replace(' ', '_'))
    sanitized = re.sub(r'_+', '_', sanitized)
    return sanitized[:50]


def get_wikipedia_page_html(wiki_page: str) -> str:
    """Fetch Wikipedia page HTML."""
    wiki_url = f"https://en.wikipedia.org/wiki/{wiki_page.replace(' ', '_')}"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    
    print(f"Fetching: {wiki_url}")
    response = requests.get(wiki_url, headers=headers, timeout=15)
    response.raise_for_status()
    return response.text


def extract_wikipedia_table(wiki_page: str, table_name: str) -> pd.DataFrame:
    """Extract a specific table from a Wikipedia page."""
    print(f"\n1. Fetching page...")
    html_content = get_wikipedia_page_html(wiki_page)
    print(f"   ✓ Got HTML ({len(html_content)} bytes)")
    
    print(f"2. Parsing tables...")
    try:
        tables = pd.read_html(html_content)
        print(f"   ✓ Found {len(tables)} table(s)")
    except Exception as e:
        print(f"   ERROR parsing tables: {e}")
        raise
    
    if not tables:
        print(f"   ERROR: No tables found")
        sys.exit(1)
    
    target_table = None
    for idx, table in enumerate(tables):
        if any(table_name.lower() in str(col).lower() for col in table.columns):
            print(f"   ✓ Found matching table #{idx + 1}")
            target_table = table
            break
    
    if target_table is None:
        print(f"   Using first table...")
        target_table = tables[0]
    
    return target_table


def create_html_report(df: pd.DataFrame, wiki_page: str, table_name: str) -> str:
    """Create a beautiful HTML report from the DataFrame."""
    sanitized_table = sanitize_filename(table_name)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"{sanitized_table}_{timestamp}.html"
    
    print(f"3. Creating HTML...")
    
    try:
        table_html = df.to_html(classes="data-table", border=0)
        print(f"   ✓ Converted table to HTML")
    except Exception as e:
        print(f"   ERROR converting table: {e}")
        raise
    
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{table_name}</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 40px 20px;
            margin: 0;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 10px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            padding: 0;
        }}
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 40px;
            text-align: center;
        }}
        .header h1 {{
            margin: 0;
            font-size: 2.5em;
        }}
        .metadata {{
            background: #f8f9fa;
            padding: 20px 40px;
            border-bottom: 1px solid #e9ecef;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
        }}
        .metadata-item {{
            display: flex;
            flex-direction: column;
        }}
        .metadata-label {{
            font-weight: bold;
            color: #667eea;
        }}
        .table-container {{
            padding: 40px;
            overflow-x: auto;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 0.9em;
        }}
        thead {{
            background: #667eea;
            color: white;
        }}
        th {{
            padding: 12px;
            text-align: left;
        }}
        td {{
            padding: 10px 12px;
            border-bottom: 1px solid #e9ecef;
        }}
        tr:hover {{
            background: #f8f9fa;
        }}
        tr:nth-child(even) {{
            background: #f8f9fa;
        }}
        .footer {{
            background: #f8f9fa;
            padding: 20px 40px;
            text-align: center;
            border-top: 1px solid #e9ecef;
            color: #6c757d;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>{table_name}</h1>
            <p>Wikipedia Table Report</p>
        </div>
        <div class="metadata">
            <div class="metadata-item">
                <span class="metadata-label">Source</span>
                <span>{wiki_page}</span>
            </div>
            <div class="metadata-item">
                <span class="metadata-label">Date</span>
                <span>{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</span>
            </div>
            <div class="metadata-item">
                <span class="metadata-label">Rows</span>
                <span>{len(df):,}</span>
            </div>
            <div class="metadata-item">
                <span class="metadata-label">Columns</span>
                <span>{len(df.columns)}</span>
            </div>
        </div>
        <div class="table-container">
            {table_html}
        </div>
        <div class="footer">
            <p>Generated by Wikipedia Table to HTML Converter</p>
        </div>
    </div>
</body>
</html>"""
    
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        print(f"   ✓ Saved to: {output_file}")
    except Exception as e:
        print(f"   ERROR writing file: {e}")
        raise
    
    return output_file


def main():
    if len(sys.argv) != 3:
        print("Usage: python extract_table.py <wiki_page> <table_name>")
        sys.exit(1)
    
    wiki_page = sys.argv[1]
    table_name = sys.argv[2]
    
    print(f"\n{'='*60}")
    print(f"Wikipedia Table to HTML Converter")
    print(f"{'='*60}")
    print(f"Current directory: {os.getcwd()}")
    print(f"Page: {wiki_page}")
    print(f"Table: {table_name}\n")
    
    try:
        df = extract_wikipedia_table(wiki_page, table_name)
        print(f"   ✓ Table: {len(df)} rows × {len(df.columns)} columns\n")
        
        output_path = create_html_report(df, wiki_page, table_name)
        
        print(f"\n{'='*60}")
        print(f"✓ SUCCESS!")
        print(f"File: {os.path.abspath(output_path)}")
        print(f"{'='*60}\n")
        
    except Exception as e:
        print(f"\n{'='*60}")
        print(f"✗ ERROR: {e}")
        print(f"{'='*60}\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
