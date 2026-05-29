# 📚 Research Literature — Home

Entry point for the vault. Start here.

## 🗺️ Maps of Content (the seven big buckets)
- [[IAM-Methods]] — model development, methodology, scenario design
- [[Decarbonization-Pathways]] — mitigation pathways, net-zero, NETs
- [[Policy-Design]] — instruments, sequencing, mixes, enforcement
- [[Health-Cobenefits]] — air quality, health burden, co-benefits
- [[Equity-Distribution]] — distributional effects, justice
- [[Transport-Electrification]] — EVs, charging, travel demand
- [[Finance-Investment]] — investment needs, macro backdrop

## 📥 Inbox
Papers I've added but not yet processed into a full note:
- 

## 🔎 Live queries (requires the Dataview plugin)

### Unread papers
```dataview
TABLE year, journal, categories
FROM "papers"
WHERE status = "to-read"
SORT year DESC
```

### Everything tagged equity, newest first
```dataview
TABLE authors, year, status
FROM "papers"
WHERE contains(categories, "Equity-Distribution")
SORT year DESC
```

### High-rated papers I've deep-read
```dataview
TABLE rating, categories
FROM "papers"
WHERE rating >= 4 AND status = "deep-read"
SORT rating DESC
```

### Reading log — what I read and when
```dataview
TABLE date_read, rating
FROM "papers"
WHERE date_read
SORT date_read DESC
```
