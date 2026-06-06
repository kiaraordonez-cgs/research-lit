# 📊 Literature Matrix

The living matrix of every paper in the vault. Updates automatically as you add or edit paper notes. This is the note the **PhD Operating System dashboard links to** (Quick Links → Lit Vault).

Cross-vault note: the PhD OS cannot query these papers directly (Dataview only sees its own vault). Reference individual papers from the PhD OS using the Better BibTeX citekey shown in the `zotero` field, e.g. `@budolfson2021protecting`.

---

## Full matrix
```dataview
TABLE
  authors[0] AS "First author",
  year AS "Year",
  journal AS "Journal",
  type AS "Type",
  themes AS "Themes",
  sectors AS "Sectors",
  models AS "Models",
  regions AS "Regions",
  status AS "Status",
  rating AS "★"
FROM "papers"
SORT year DESC
```

---

## Reading queue (unread, oldest first so nothing rots)
```dataview
TABLE authors AS "Authors", year AS "Year", themes AS "Themes", journal AS "Journal"
FROM "papers"
WHERE status = "to-read"
SORT year ASC
```

## Reading log (what I've finished, newest first)
```dataview
TABLE date_read AS "Read", rating AS "★", themes AS "Themes"
FROM "papers"
WHERE date_read
SORT date_read DESC
```

## Coverage check — papers per theme
```dataview
TABLE length(rows) AS "Papers"
FROM "papers"
FLATTEN themes AS theme
GROUP BY theme
SORT length(rows) DESC
```

## Coverage check — papers per sector
```dataview
TABLE length(rows) AS "Papers"
FROM "papers"
FLATTEN sectors AS sector
GROUP BY sector
SORT length(rows) DESC
```

---

### How to slice further
Copy any block above and change the `WHERE` line. Useful patterns:
- One model: `WHERE contains(models, "gcam")`
- One sector: `WHERE contains(sectors, "transportation")`
- One region: `WHERE contains(regions, "united-states")`
- Combine with `and`: `WHERE contains(models, "gcam") and contains(regions, "united-states")`
- Only high-value: `WHERE rating >= 4`
