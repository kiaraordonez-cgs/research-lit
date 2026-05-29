# research-lit

Personal literature vault for IAM / energy modeling / climate policy.
Synced via Git. PDFs live in Google Drive (linked from Zotero), not in this repo.

## Structure
- `Home.md` — dashboard + live queries
- `MOCs/` — theme MOCs (concept hubs for synthesis)
- `papers/` — one note per paper, from the template
- `_templates/` — note template(s)

## The tagging design

Each paper is described along **five orthogonal axes** plus a `type`. Each axis is a YAML list, so a paper can have several values on each. Keep vocabularies small and consistent — Dataview queries depend on exact strings.

### `type` (single value — what kind of paper it is)
`empirical` · `modeling` · `review` · `scenario` · `ipcc-chapter` · `commentary`

### `models` (modeling tools used or analyzed)
Starter set: `gcam` · `dice` · `markal` · `iam-generic`
Add as needed; lowercase, hyphens for multi-word.

### `sectors` (physical sectors covered)
Starter set: `electricity` · `transportation` · `buildings` · `industry` · `agriculture` · `land-use` · `water` · `hydrogen` · `economy-wide`

### `levers` (policy or technology levers)
Starter set: `electrification` · `carbon-tax` · `dividend-recycling` · `standards` · `subsidy` · `negative-emissions` · `efficiency` · `demand-side`

### `regions` (geographic scope)
Starter set: `united-states` · `china` · `india` · `eu` · `developing-asia` · `global`

### `themes` (intellectual concern — match an MOC where possible)
Starter set: `equity` · `pathways` · `policy-design` · `health-cobenefits` · `investment` · `uncertainty` · `political-feasibility` · `technology-learning`

### Other fields
- `status`: `to-read` · `skimmed` · `read` · `deep-read`
- `rating`: 1–5
- `date_read`: YYYY-MM-DD

## Workflow
1. Capture in Zotero (auto-grabs metadata; PDF lives in Google Drive)
2. Create note in `papers/` (Templater applies the template)
3. Fill the frontmatter axes — only the relevant ones
4. Write the one-sentence summary in your own words
5. Add `[[wikilinks]]` to related papers
6. Git plugin auto-syncs every 10 min

## Vocabulary discipline
- When in doubt about an axis, prefer adding to `themes` over inventing a new axis
- Rename tags vault-wide with the Tag Wrangler plugin if a term drifts
- Don't agonize about completeness — the vocabulary grows with the library
