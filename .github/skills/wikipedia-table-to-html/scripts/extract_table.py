#!/usr/bin/env python3
"""
Extract a Wikipedia table and convert it to HTML report.

Usage:
    python extract_table.py <wiki_page> <table_name>
"""

import sys
import re
import time
import warnings
from datetime import datetime

warnings.filterwarnings('ignore')

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
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
    ]
    
    wiki_url = f"https://en.wikipedia.org/wiki/{wiki_page.replace(' ', '_')}"
    
    for attempt in range(3):
        try:
            headers = {'User-Agent': user_agents[attempt % len(user_agents)]}
            response = requests.get(wiki_url, headers=headers, timeout=15)
            response.raise_for_status()
            return response.text
        except Exception as e:
            if attempt < 2:
                time.sleep(2)
                continue
            raise
    
    raise Exception(f"Failed to fetch {wiki_page}")


def extract_wikipedia_table(wiki_page: str, table_name: str) -> pd.DataFrame:
    """Extract a specific table from a Wikipedia page."""
    print(f"Fetching: {wiki_page}...")
    html_content = get_wikipedia_page_html(wiki_page)
    
    print(f"Parsing tables...")
    tables = pd.read_html(html_content)
    
    if not tables:
        print(f"Error: No tables found on page '{wiki_page}'")
        sys.exit(1)
    
    print(f"Found {len(tables)} table(s)")
    
    target_table = None
    for idx, table in enumerate(tables):
        if any(table_name.lower() in str(col).lower() for col in table.columns):
            target_table = table
            break
    
    if target_table is None:
        print(f"Using first table...")
        target_table = tables[0]
    
    return target_table


def create_html_report(df: pd.DataFrame, wiki_page: str, table_name: str) -> str:
    """Create a beautiful HTML report from the DataFrame."""
    sanitized_table = sanitize_filename(table_name)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"{sanitized_table}_{timestamp}.html"
    
    table_html = df.to_html(classes="data-table", border=0)
    
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Wikipedia Table: {table_name}</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif;
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
        }}
        
        .data-table td {{
            padding: 12px 15px;
            border-bottom: 1px solid #e9ecef;
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
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>{table_name}</h1>
            <p>Data from Wikipedia</p>
        </div>
        
        <div class="metadata">
            <div class="metadata-item">
                <span class="metadata-label">Source</span>
                <span class="metadata-value">{wiki_page}</span>
            </div>
            <div class="metadata-item">
                <span class="metadata-label">Date</span>
                <span class="metadata-value">{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</span>
            </div>
            <div class="metadata-item">
                <span class="metadata-label">Rows</span>
                <span class="metadata-value">{len(df):,}</span>
            </div>
            <div class="metadata-item">
                <span class="metadata-label">Columns</span>
                <span class="metadata-value">{len(df.columns)}</span>
            </div>
        </div>
        
        <div class="table-container">
            {table_html}
        </div>
        
        <div class="footer">
            <p>Wikipedia Table to HTML Converter</p>
        </div>
    </div>
</body>
</html>"""
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    return output_file


def main():
    if len(sys.argv) != 3:
        print("Usage: python extract_table.py <wiki_page> <table_name>")
        sys.exit(1)
    
    wiki_page = sys.argv[1]
    table_name = sys.argv[2]
    
    try:
        df = extract_wikipedia_table(wiki_page, table_name)
        print(f"Table: {len(df)} rows × {len(df.columns)} columns")
        print("Generating HTML...")
        output_path = create_html_report(df, wiki_page, table_name)
        print(f"\n✓ Created: {output_path}\n")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
