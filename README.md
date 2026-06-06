# research-lit

Personal literature vault for IAM / energy modeling / climate policy.
Synced via Git. PDFs live in Google Drive (linked from Zotero), not in this repo.
Companion to the separate **PhD Operating System** vault, which links here.

## Structure
- `Home.md` — dashboard
- `Literature Matrix.md` — the full live grid (PhD OS links to this)
- `MOCs/` — six theme hubs for synthesis
- `papers/` — one note per paper, from the template
- `_templates/` — note + Zotero-import templates

## Tagging design — five axes plus a type

Each axis is a YAML list; a paper can have several values per axis. Keep vocabularies small and exact (Dataview matches strings literally).

### `type` (one value)
`empirical` · `modeling` · `review` · `scenario` · `ipcc-chapter` · `commentary`

### `models`
`gcam` · `dice` · `markal` · `iam-generic` (extend as needed)

### `sectors`
`electricity` · `transportation` · `buildings` · `industry` · `agriculture` · `land-use` · `water` · `hydrogen` · `economy-wide`

### `levers`
`electrification` · `carbon-tax` · `dividend-recycling` · `standards` · `subsidy` · `negative-emissions` · `efficiency` · `demand-side`

### `regions`
`united-states` · `china` · `india` · `eu` · `developing-asia` · `global`

### `themes` (match an MOC where possible)
`equity` · `health` · `economic-cobenefits` · `pathways` · `policy-design` · `investment` · `uncertainty` · `political-feasibility` · `technology-learning`

### Other fields
- `status`: `to-read` · `skimmed` · `read` · `deep-read`
- `rating`: 1–5
- `date_read`: YYYY-MM-DD

## Cross-vault linking
The PhD Operating System vault references papers by **Better BibTeX citekey** (the `zotero` field, e.g. `@budolfson2021protecting`). That citekey is the universal paper ID across this vault, Zotero, the PhD OS, and Quarto/LaTeX.

## Workflow
1. Capture in Zotero (Connector). PDF added later, linked from Google Drive.
2. Generate stub note(s) via Zotero Integration plugin (batch import).
3. As you read: fill the axes, write the one-sentence summary, set `status` and `rating`.
4. Add `[[wikilinks]]` to related papers and relevant MOCs.
5. Git auto-syncs every 10 min.

## Renaming a theme/tag later
Frontmatter values, not `#tags`. Use the Tag Wrangler plugin, or a vault-wide find-and-replace. Update: (a) the value in paper notes, (b) the MOC filename, (c) the MOC's `WHERE contains(themes, "...")` line.
