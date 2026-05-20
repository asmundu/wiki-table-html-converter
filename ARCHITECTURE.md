# Architecture & Design

## Overview

The Wikipedia Table to HTML Converter is a lightweight tool that:
1. **Fetches** Wikipedia pages using the Wikipedia API
2. **Extracts** tables using pandas HTML parsing
3. **Renders** professional HTML reports with custom styling

## Component Architecture

```
┌─────────────────────────────────────────────────┐
│  extract_table.py                               │
│  ─ Main entry point                             │
│  ─ Command-line argument parsing                │
├─────────────────────────────────────────────────┤
│  extract_wikipedia_table()                      │
│  ─ Wikipedia API client                         │
│  ─ HTML table parsing                           │
│  ─ Error handling & disambiguation              │
├─────────────────────────────────────────────────┤
│  create_html_report()                           │
│  ─ DataFrame to HTML conversion                 │
│  ─ CSS styling & responsive design              │
│  ─ Metadata injection                           │
├─────────────────────────────────────────────────┤
│  Output: Self-contained HTML file               │
│  ─ No external dependencies                     │
│  ─ Mobile-responsive                            │
│  ─ Ready to share/print/host                    │
└─────────────────────────────────────────────────┘
```

## Technology Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| API Access | `wikipedia` library | Fetch Wikipedia pages reliably |
| Data Processing | `pandas` | Parse HTML tables into DataFrames |
| HTML Parsing | `lxml` (via pandas) | Extract table data from HTML |
| Styling | Pure CSS (no JS) | Responsive, portable design |
| Output | Self-contained HTML | Single file, no runtime dependencies |

## Data Flow

```
User Input (page + table name)
         ↓
Wikipedia API Lookup
         ↓
HTML Table Extraction
         ↓
Pandas DataFrame Creation
         ↓
CSS Styling & Templating
         ↓
Self-contained HTML File
         ↓
Browser Rendering
```

## File Structure

```
wiki-table-html-converter/
├── .github/skills/wikipedia-table-to-html/
│   ├── SKILL.md                          # Skill definition (VS Code)
│   ├── scripts/
│   │   └── extract_table.py              # Main extraction script
│   └── assets/                           # Reserved for future templates
├── README.md                              # Quick start guide
├── USAGE.md                               # Detailed usage documentation
├── ARCHITECTURE.md                        # This file
├── requirements.txt                       # Python dependencies
├── convert-wiki-table.sh                 # Shell wrapper (Unix/Linux)
└── .gitignore                             # Git exclusions

```

## Design Decisions

### 1. Two-Parameter Interface
**Decision**: Accept only `wiki-page` and `table-name`

**Rationale**:
- Minimizes user input complexity
- Wikipedia page titles are standardized
- Table names are visible on the page
- Reduces cognitive load

### 2. Self-Contained HTML Output
**Decision**: Single HTML file with embedded CSS

**Rationale**:
- Easy to share (no folder structures)
- Works offline immediately after generation
- No server/hosting required
- Can be emailed, printed, or archived
- Backward compatible with all browsers

### 3. CSS-Only Styling
**Decision**: No JavaScript in output

**Rationale**:
- Maximum browser compatibility
- Smaller file size
- Faster load time
- Works in restricted environments
- Can be printed directly

### 4. Pandas for Table Extraction
**Decision**: Use pandas.read_html()

**Rationale**:
- Handles complex table HTML automatically
- Robust to malformed HTML
- Consistent DataFrame output
- Built-in error handling
- Column type inference

## Error Handling Strategy

| Scenario | Handling | User Message |
|----------|----------|--------------|
| Page not found | Wikipedia exceptions caught | "Page not found" |
| Disambiguation page | Exception with suggestions | List alternatives |
| No tables on page | Caught and reported | "No tables found" |
| Table name not found | Auto-fallback to first table | "Using first table" |
| Network error | Exception propagates | Network error message |

## Performance Characteristics

- **Page fetch**: ~1-3 seconds (network dependent)
- **Table parsing**: <100ms for typical tables
- **HTML generation**: <50ms
- **Total time**: Typically 2-5 seconds
- **Output file size**: 50-500 KB (typical)

## Extensibility

Future enhancements could include:
- JavaScript table sorting
- Advanced filtering UI
- Export to CSV/JSON
- Multi-table reports
- Data transformation pipelines
- Custom styling templates
- Caching layer

## Security Considerations

- **Input validation**: Wikipedia titles validated by API
- **HTML escaping**: pandas handles DataFrame HTML escaping
- **No code execution**: Pure data pipeline
- **Source attribution**: All reports link back to Wikipedia
- **User data**: No user data collection or transmission

## Testing Strategy

Manual test cases for:
1. Common Wikipedia table types
2. Edge cases (special characters, numbers, links)
3. Disambiguation handling
4. Large table rendering
5. Network timeout scenarios
6. Various table formats

## Deployment

### Local Use
```bash
pip install -r requirements.txt
python .github/skills/wikipedia-table-to-html/scripts/extract_table.py ...
```

### VS Code Integration
- Place in `.github/skills/wikipedia-table-to-html/`
- VS Code auto-discovers and loads skill
- Appears in slash command menu

### GitHub Actions (Optional)
Can be automated in workflows to generate reports on schedule or trigger.
