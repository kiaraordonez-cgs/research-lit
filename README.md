# research-lit

Personal literature vault for IAM / energy modeling / climate policy.
Synced via Git. PDFs live in Google Drive (linked from Zotero), not in this repo.

## Structure
- `Home.md` — start here; dashboard + live queries
- `MOCs/` — the seven category hubs (Maps of Content)
- `papers/` — one note per paper, from the template
- `_templates/` — note template(s)

## Conventions (keep these consistent — queries depend on it)

**`type`** (pick one): `methods` · `empirical` · `review` · `scenario` · `ipcc-chapter` · `commentary`

**`status`** (pick one): `to-read` · `skimmed` · `read` · `deep-read`

**`categories`** (the big buckets — match MOC names exactly):
`IAM-Methods` · `Decarbonization-Pathways` · `Policy-Design` · `Health-Cobenefits` · `Equity-Distribution` · `Transport-Electrification` · `Finance-Investment`
A paper can have several. These are intentionally few and stable.

**`keywords`** — open-ended, granular, lowercase-with-hyphens. Let these proliferate; rename later if needed.

**`rating`** — 1–5, your subjective usefulness-to-me.

## Workflow (short version)
1. Capture in Zotero (auto-grabs metadata; PDF → Google Drive linked folder)
2. Generate/create note in `papers/` from `_templates/paper-template.md`
3. Write the one-sentence summary first, in your own words
4. Add `[[wikilinks]]` to related papers and to the relevant MOC(s)
5. Git plugin auto-syncs every 10 min
