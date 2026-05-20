# Wikipedia Table to HTML Report Converter

Convert any Wikipedia table into a beautiful, professional HTML report with just **two parameters**:
- Wikipedia page name
- Table name

**Output filename is automatically generated** based on the table name and timestamp.

## 🚀 Quick Start

### Installation

1. Ensure this repository is cloned or accessible
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Usage

```bash
python .github/skills/wikipedia-table-to-html/scripts/extract_table.py "Page Title" "Table Name"
```

**Example:**
```bash
python .github/skills/wikipedia-table-to-html/scripts/extract_table.py \
  "List of countries by population" \
  "Countries by population"
```

Output: `countries_by_population_20260520_143000.html` (automatically named)

## ✨ Features

- **Two-parameter simplicity**: Just provide the Wikipedia page and table name
- **Beautiful styling**: Professional gradient design with responsive layout
- **Auto-generated filenames**: Derived from table name + timestamp
- **Self-contained**: Single HTML file, no external dependencies needed
- **Metadata included**: Source page, extraction timestamp, row/column counts
- **Mobile-friendly**: Responsive design works on all devices

## 📊 What You Get

Each generated report includes:
- Professional header with title and source attribution
- Metadata panel showing source page, date, and table dimensions
- Fully formatted and styled data table
- Responsive mobile design
- Clean footer with attribution

## 🔧 Requirements

- Python 3.7+
- `wikipedia` - Python Wikipedia API wrapper
- `pandas` - Data manipulation library

See `requirements.txt` for exact versions.

## 📝 Examples

### Popular Wikipedia Tables

```bash
# Countries by population (auto-named: countries_by_population_[timestamp].html)
python .github/skills/wikipedia-table-to-html/scripts/extract_table.py \
  "List of countries by population" \
  "Countries by population"

# Olympic medals (auto-named: medal_[timestamp].html)
python .github/skills/wikipedia-table-to-html/scripts/extract_table.py \
  "All-time Olympic Games medal tables" \
  "Medal count"

# Largest companies (auto-named: company_[timestamp].html)
python .github/skills/wikipedia-table-to-html/scripts/extract_table.py \
  "List of largest companies by revenue" \
  "Largest companies"
```

## 🎨 Output Preview

The generated HTML includes:
- Gradient purple header with white text
- Metadata section with 4 key statistics
- Sortable data table with alternating row colors
- Hover effects for better UX
- Mobile-responsive design
- Clean footer with attribution

## 🐛 Troubleshooting

**"Table not found" error:**
- Check the Wikipedia page title is correct
- Try a different table name or use the first table (script will auto-select)

**"Page not found" error:**
- Verify the exact Wikipedia page title
- Check for disambiguation pages

**Module import errors:**
- Reinstall requirements: `pip install -r requirements.txt --force-reinstall`

## 📜 License

This tool respects Wikipedia's licensing. Generated reports maintain proper attribution to Wikipedia.

## 🤝 Contributing

Improvements welcome! Feel free to enhance styling, add features, or improve compatibility.
