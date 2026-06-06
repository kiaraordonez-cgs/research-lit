---
title: "{{title}}"
authors: [{% for a in creators %}"{{a.firstName}} {{a.lastName}}"{% if not loop.last %}, {% endif %}{% endfor %}]
year: {{date | format("YYYY")}}
journal: "{{publicationTitle}}"
doi: "{{DOI}}"
zotero: "@{{citekey}}"
type: 
models: 
sectors: 
levers: 
regions: 
themes: 
status: to-read
rating: 
date_read: 
---

# {{title}}

> [!summary] One-sentence summary
> _In your own words — fill in when you read it._

## Why I read it / how it connects
- 

## Key points
- 

## Methods / model
- Model(s): 
- Regional/sector resolution: 
- Key assumptions worth remembering: 

## Figures & numbers to reference later
- 

## Open questions / critiques
- 

{% persist "notes" %}{% endpersist %}
