# 📚 Research Literature — Home

Entry point for the vault. Start here.

## 🗺️ Theme MOCs (concept hubs — your synthesis lives here)
- [[Equity]]
- [[Pathways]]
- [[Policy-Design]]
- [[Health-Cobenefits]]
- [[Investment]]

## 📥 Inbox
Papers I've added but not yet processed:
- 

## 🔎 Live queries

### Unread queue
```dataview
TABLE year, authors, themes, sectors
FROM "papers"
WHERE status = "to-read"
SORT year DESC
```

### Reading log — what I read and when
```dataview
TABLE date_read, rating, themes
FROM "papers"
WHERE date_read
SORT date_read DESC
```

### High-rated, deep-read
```dataview
TABLE rating, themes, sectors
FROM "papers"
WHERE rating >= 4 AND status = "deep-read"
SORT rating DESC
```

### Slice by model (example: GCAM)
```dataview
TABLE year, authors, sectors, regions
FROM "papers"
WHERE contains(models, "gcam")
SORT year DESC
```

### Slice by sector (example: transportation)
```dataview
TABLE year, authors, regions, themes
FROM "papers"
WHERE contains(sectors, "transportation")
SORT year DESC
```

### Slice by region (example: United States)
```dataview
TABLE year, authors, sectors, themes
FROM "papers"
WHERE contains(regions, "united-states")
SORT year DESC
```

_Edit any query above to filter on different values. Combine fields with `and` for narrower slices, e.g. `contains(models, "gcam") and contains(sectors, "transportation")`._
