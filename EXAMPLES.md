# Quick Start Examples

Ready to convert Wikipedia tables? Here are some real-world examples you can run right now.

## 0️⃣ Before You Start

```bash
# Install dependencies (one time only)
pip install -r requirements.txt
```

## 1️⃣ Countries by Population

Extract the most populous countries in the world.

```bash
python .github/skills/wikipedia-table-to-html/scripts/extract_table.py \
  "List of countries by population" \
  "Countries by population"
```

**Output**: `wikipedia-table-report-[timestamp].html`  
**What you get**: Complete ranking of countries by population with estimates

---

## 2️⃣ Olympic Medals All-Time

Get historical Olympic Games medal data.

```bash
python .github/skills/wikipedia-table-to-html/scripts/extract_table.py \
  "All-time Olympic Games medal tables" \
  "Medal"
```

**Output**: Beautiful formatted Olympic records  
**What you get**: All-time medal counts by country across all Olympic Games

---

## 3️⃣ Fortune 500 Companies

Extract the largest US companies by revenue.

```bash
python .github/skills/wikipedia-table-to-html/scripts/extract_table.py \
  "Fortune 500" \
  "Fortune"
```

**Output**: Top 500 US companies ranked by revenue  
**What you get**: Company rankings, revenue figures, and industry data

---

## 4️⃣ Presidents of the United States

Get historical US presidential data.

```bash
python .github/skills/wikipedia-table-to-html/scripts/extract_table.py \
  "List of presidents of the United States" \
  "President"
```

**Output**: Complete presidential records  
**What you get**: All US presidents with terms and biographical data

---

## 5️⃣ FIFA World Cup Winners

Extract FIFA World Cup historical data.

```bash
python .github/skills/wikipedia-table-to-html/scripts/extract_table.py \
  "FIFA World Cup" \
  "World Cup"
```

**Output**: World Cup tournament history  
**What you get**: Winners, runners-up, and tournament results by year

---

## 6️⃣ Nobel Prize Winners

Get Nobel Prize recipient data.

```bash
python .github/skills/wikipedia-table-to-html/scripts/extract_table.py \
  "List of Nobel laureates by country" \
  "Nobel"
```

**Output**: Nobel Prize winners by country  
**What you get**: Categories, years, and recipient counts

---

## 7️⃣ Top Grossing Films

Extract the highest-grossing movies of all time.

```bash
python .github/skills/wikipedia-table-to-html/scripts/extract_table.py \
  "List of highest-grossing films of all time" \
  "Highest"
```

**Output**: Box office records  
**What you get**: Film titles, budgets, and worldwide box office totals

---

## 8️⃣ Internet Domains by Country

Get statistics on country-code top-level domains.

```bash
python .github/skills/wikipedia-table-to-html/scripts/extract_table.py \
  "Country code top-level domain" \
  "Country"
```

**Output**: Domain registry data  
**What you get**: ccTLD allocations by country

---

## 9️⃣ Tallest Buildings

Extract data on the world's tallest buildings.

```bash
python .github/skills/wikipedia-table-to-html/scripts/extract_table.py \
  "List of tallest buildings and structures" \
  "Building"
```

**Output**: Height rankings  
**What you get**: Buildings by height, location, and completion date

---

## 🔟 Nobel Physics Laureates by Year

Extract physics laureates with award data.

```bash
python .github/skills/wikipedia-table-to-html/scripts/extract_table.py \
  "List of Nobel laureates in Physics" \
  "Laureate"
```

**Output**: Physics Nobel Prize recipients  
**What you get**: Winners by year with contributions and affiliations

---

## 🔍 How to Find More Wikipedia Tables

1. Go to **Wikipedia.org**
2. Search for your topic
3. Look for tables on the page
4. Note the **page title** (from the browser URL or page header)
5. Note the **table name** (any unique word in the table header or first row)
6. Run the command!

---

## 💡 Pro Tips

### Tip 1: Finding Exact Page Names
Some Wikipedia pages have special formatting. Use the exact title from the browser:
- URL: `https://en.wikipedia.org/wiki/List_of_countries_by_population`
- Page name: "List of countries by population"

### Tip 2: Finding Exact Table Names
If you're not sure about the table name, just try common keywords:
- "by population" if it's about rankings
- The column header name
- Any descriptive text in the table

The script will auto-fallback to the first table if your name doesn't match exactly.

### Tip 3: Custom Output Names
```bash
python .github/skills/wikipedia-table-to-html/scripts/extract_table.py \
  "Page" "Table" "my-custom-name.html"
```

### Tip 4: Batch Processing
```bash
# Create multiple reports
for page in "List of countries by population" "All-time Olympic Games medal tables" "Fortune 500"; do
  python .github/skills/wikipedia-table-to-html/scripts/extract_table.py "$page" "$page"
done
```

---

## 🎯 What Makes a Good Wikipedia Table

The best Wikipedia tables for conversion have:
- ✅ Structured data (consistent columns)
- ✅ Reasonable row count (not too massive)
- ✅ Clear headers
- ✅ Related data (not randomly mixed)

Less ideal but still work:
- ⚠️ Tables with merged cells
- ⚠️ Very large tables (10,000+ rows)
- ⚠️ Complex nested headers

---

## ❓ Troubleshooting Quick Examples

**"Page not found"**
→ Check spelling and use exact Wikipedia page name

**"No tables found"**
→ The page may not have data tables, try a different page

**"Table not found"**
→ Script will use the first table anyway (this is usually fine!)

---

## 📊 Next Steps

1. ✅ Run one of the examples above
2. ✅ Open the generated `.html` file in your browser
3. ✅ Share the HTML file or print as PDF
4. ✅ Explore other Wikipedia pages with tables

Happy converting! 🎉
