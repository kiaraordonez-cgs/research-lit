#!/usr/bin/env python3
"""
zotero_csv_to_stubs.py
Convert a Zotero CSV export into Obsidian stub notes for the research-lit vault.

USAGE:
    python zotero_csv_to_stubs.py path\\to\\export.csv path\\to\\vault\\papers

  - First argument:  the CSV file exported from Zotero (right-click collection -> Export -> CSV)
  - Second argument: the target 'papers' folder inside your Obsidian vault
                     (e.g. C:\\Users\\kiara\\Desktop\\research-lit\\papers)

BEHAVIOR:
  - Creates one .md stub per paper, with your five-axis frontmatter, status: to-read.
  - SKIPS any paper whose note file already exists (never overwrites your work).
  - Reports how many were created vs. skipped.
  - Flags any papers with missing authors so you can fix them manually.

Run it any time you add papers to Zotero: re-export the CSV, run this, and only
the NEW papers get stubs. Existing notes are left untouched.
"""

import csv, re, os, sys

STOP = {'a','an','the','of','for','and','on','in','to','with','from','by','at','do','does','is','are'}

def parse_authors(raw):
    if not raw.strip():
        return []
    out = []
    for chunk in raw.split(';'):
        chunk = chunk.strip()
        if not chunk:
            continue
        if ',' in chunk:
            last, first = [p.strip() for p in chunk.split(',', 1)]
            out.append(f"{first} {last}".strip())
        else:
            out.append(chunk)
    return out

def last_name(raw):
    if not raw.strip():
        return 'anon'
    fa = raw.split(';')[0].strip()
    last = fa.split(',')[0].strip() if ',' in fa else (fa.split()[-1] if fa.split() else 'anon')
    return re.sub(r'[^a-z]', '', last.lower()) or 'anon'

def first_title_word(title):
    for w in re.findall(r"[A-Za-z]+", title):
        if w.lower() not in STOP:
            return w.lower()
    return 'untitled'

def get_year(r):
    y = (r.get('Publication Year') or '').strip()
    if y:
        return y
    m = re.search(r'(19|20)\d{2}', (r.get('Date') or '').strip())
    return m.group(0) if m else ''

def safe_filename(title):
    t = re.sub(r'[\\/:*?"<>|]', '', title)
    t = re.sub(r'\s+', ' ', t).strip()
    return t[:120]

def yaml_list(items):
    if not items:
        return '[]'
    return '[' + ', '.join('"' + i.replace('"', "'") + '"' for i in items) + ']'

def main():
    if len(sys.argv) != 3:
        print("Usage: python zotero_csv_to_stubs.py <export.csv> <vault/papers folder>")
        sys.exit(1)
    csv_path, out_dir = sys.argv[1], sys.argv[2]
    if not os.path.isfile(csv_path):
        print(f"CSV not found: {csv_path}"); sys.exit(1)
    os.makedirs(out_dir, exist_ok=True)

    rows = list(csv.DictReader(open(csv_path, encoding='utf-8-sig')))
    seen_keys = {}
    created, skipped, no_author = 0, 0, []

    for r in rows:
        title = (r.get('Title') or '').strip()
        if not title:
            continue
        fname = safe_filename(title) + '.md'
        path = os.path.join(out_dir, fname)

        # SAFETY: never overwrite an existing note
        if os.path.exists(path):
            skipped += 1
            continue

        authors = parse_authors(r.get('Author') or '')
        if not authors:
            no_author.append(title[:60])
        year = get_year(r)
        journal = (r.get('Publication Title') or '').strip()
        doi = (r.get('DOI') or '').strip()
        url = (r.get('Url') or '').strip()

        ck = last_name(r.get('Author') or '') + (year or 'nd') + first_title_word(title)
        if ck in seen_keys:
            seen_keys[ck] += 1
            ck = ck + chr(ord('a') + seen_keys[ck] - 1)
        else:
            seen_keys[ck] = 1

        fm = [
            '---',
            f'title: "{title.replace(chr(34), chr(39))}"',
            f'authors: {yaml_list(authors)}',
            f'year: {year}',
            f'journal: "{journal.replace(chr(34), chr(39))}"',
            f'doi: "{doi}"',
            f'url: "{url}"',
            f'zotero: "@{ck}"',
            'type: ', 'models: ', 'sectors: ', 'levers: ', 'regions: ', 'themes: ',
            'status: to-read', 'rating: ', 'date_read: ',
            '---',
        ]
        body = f'''
# {title}

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
'''
        with open(path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(fm) + body)
        created += 1

    print(f"Created {created} new stub note(s).")
    print(f"Skipped {skipped} (note already existed).")
    if no_author:
        print(f"\n{len(no_author)} new note(s) have NO author in the CSV — fill these in manually when you read them:")
        for t in no_author:
            print("  -", t)

if __name__ == '__main__':
    main()
