# 📚 Research Literature — Home

Entry point for the lit vault. Start here.

## 📊 [[Literature Matrix]]
The full live grid of every paper. (This is what the PhD Operating System dashboard links to.)

## 🗺️ Theme MOCs (concept hubs — your synthesis lives here)
- [[Equity]]
- [[Health]]
- [[Economic-Cobenefits]]
- [[Pathways]]
- [[Policy-Design]]
- [[Investment]]

## 📥 Inbox
Papers added but not yet processed:
- 

## 🔎 Quick queries

### Unread queue
```dataview
TABLE year, authors, themes, sectors
FROM "papers"
WHERE status = "to-read"
SORT year DESC
```

### High-rated, deep-read
```dataview
TABLE rating, themes, sectors
FROM "papers"
WHERE rating >= 4 AND status = "deep-read"
SORT rating DESC
```

_Full matrix and more slices live in [[Literature Matrix]]._
