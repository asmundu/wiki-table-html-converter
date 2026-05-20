# Usage Guide

## Installation

### Step 1: Clone or Access the Repository
```bash
git clone https://github.com/asmundu/wiki-table-html-converter.git
cd wiki-table-html-converter
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

Or with a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

### Method 1: Direct Python Execution

```bash
python .github/skills/wikipedia-table-to-html/scripts/extract_table.py "Page Title" "Table Name"
```

### Method 2: Using the Shell Wrapper (Linux/Mac)

```bash
chmod +x convert-wiki-table.sh
./convert-wiki-table.sh "Page Title" "Table Name"
```

### Method 3: As a VS Code Skill

If you've set up this as a VS Code skill in `.github/skills/`, use:
```
/wikipedia-table-to-html wiki-page:PageTitle table-name:TableName
```

## Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| `wiki-page` | Exact Wikipedia page title | "List of countries by population" |
| `table-name` | Table header or name to extract | "Countries by population" |
| `output_file` (optional) | Custom output filename | "my-report.html" |

## Examples

### Example 1: Countries by Population
```bash
python .github/skills/wikipedia-table-to-html/scripts/extract_table.py \
  "List of countries by population" \
  "Countries by population"
```

Output: `wikipedia-table-report-20260520_143000.html`

### Example 2: Olympic Medals
```bash
python .github/skills/wikipedia-table-to-html/scripts/extract_table.py \
  "All-time Olympic Games medal tables" \
  "Medal"
```

### Example 3: Fortune 500 Companies
```bash
python .github/skills/wikipedia-table-to-html/scripts/extract_table.py \
  "Fortune 500" \
  "Company"
```

### Example 4: Custom Output Filename
```bash
python .github/skills/wikipedia-table-to-html/scripts/extract_table.py \
  "List of countries by GDP" \
  "GDP" \
  "global-gdp.html"
```

## Finding Wikipedia Pages and Tables

### How to Find Wikipedia Page Names
1. Go to Wikipedia.org
2. Search for your topic
3. Use the exact page title shown in the browser address bar or page header

### How to Find Table Names
1. On the Wikipedia page, find the table you want
2. Look for:
   - The table's header/title
   - Column names
   - Any caption above the table
3. Use any unique word from the table to identify it

## Output

The script generates a professional HTML report with:

- **Beautiful Design**: Gradient purple header with white text
- **Metadata Section**: Shows source page, extraction date, row count, and column count
- **Responsive Table**: Styled data table with:
  - Alternating row colors for readability
  - Hover effects on rows
  - Mobile-friendly layout
- **Footer**: Attribution to Wikipedia

### Output File Format
```
wikipedia-table-report-YYYYMMDD_HHMMSS.html
```

Example: `wikipedia-table-report-20260520_143000.html`

Open in any web browser to view.

## Troubleshooting

### Issue: "Page not found"
**Solution**: 
- Verify the exact page title from Wikipedia
- Check for special characters or capitalization
- Try the page name without disambiguation info

### Issue: "No tables found"
**Solution**:
- The page may not have tables
- Try a different Wikipedia page
- Check if the page content is available

### Issue: "Table not found"
**Solution**:
- The specified table name wasn't matched exactly
- The script will auto-use the first table as a fallback
- Try using a different keyword from the table

### Issue: ImportError for wikipedia or pandas
**Solution**:
```bash
pip install --upgrade wikipedia pandas lxml
```

Or reinstall everything:
```bash
pip install -r requirements.txt --force-reinstall
```

### Issue: Permission denied (Linux/Mac)
**Solution**:
```bash
chmod +x convert-wiki-table.sh
chmod +x .github/skills/wikipedia-table-to-html/scripts/extract_table.py
```

## Advanced Usage

### Batch Processing Multiple Tables

Create a script `batch_convert.sh`:
```bash
#!/bin/bash

python .github/skills/wikipedia-table-to-html/scripts/extract_table.py \
  "List of countries by population" "Countries" "countries.html"

python .github/skills/wikipedia-table-to-html/scripts/extract_table.py \
  "All-time Olympic Games medal tables" "Medal" "olympics.html"

python .github/skills/wikipedia-table-to-html/scripts/extract_table.py \
  "List of largest companies by revenue" "Company" "companies.html"
```

Then run:
```bash
chmod +x batch_convert.sh
./batch_convert.sh
```

### Customizing the Output

Edit the HTML generation section in `extract_table.py` to customize:
- Colors (change hex values in CSS)
- Font sizes
- Table styling
- Layout and spacing

## Tips & Tricks

1. **Find unique table names**: Use distinctive column names as table identifiers
2. **Preview tables**: Scroll through Wikipedia to find exactly what you need first
3. **Save reports**: Generated HTML files are fully self-contained and portable
4. **Print to PDF**: Most browsers can print the HTML as PDF for sharing
5. **Check source**: Reports include Wikipedia attribution for credibility

## Support

For issues or questions:
1. Check the [README.md](README.md)
2. Review this usage guide
3. Verify your Wikipedia page title and table name
4. Check that dependencies are installed
