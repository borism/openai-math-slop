#!/usr/bin/env python3
"""Try to reproduce the "300 / 719 top-line results formalized" figure.

Computes every plausible coverage count from repository artifacts at a list of
git revisions of openai/math (read via `git show`, no checkout needed).

Usage (inside a clone containing the revisions):
    python3 -I coverage_candidates.py adc7f1241 fd4aeeb2e 42907c9e9 4eaee8754
"""
import json, re, subprocess, sys
from collections import OrderedDict


def git(*a):
    return subprocess.run(['git', *a], capture_output=True, text=True).stdout


def show(rev, path):
    return git('show', f'{rev}:{path}')


def ls(rev, path):
    return [p for p in git('ls-tree', '-r', '--name-only', rev, path).split('\n') if p]


PAPER_LINK = re.compile(r'preprints/([^/\]\s]+?)/[^/\s]*?\.pdf')


def candidates(rev):
    c = OrderedDict()
    pre = sorted(set(p.split('/')[1] for p in ls(rev, 'preprints') if p.count('/') >= 2))
    readmes = {d: show(rev, f'preprints/{d}/README.md') for d in pre}
    withdrawn = {d for d, t in readmes.items() if re.search(r'withdrawn|retracted', t, re.I)}
    superseded = {d for d, t in readmes.items() if re.search(r'superseded|previous (version|edition)|has been revised|newer version', t, re.I)}
    c['preprint dirs'] = len(pre)
    c['preprint dirs flagged withdrawn'] = len(withdrawn)
    contents = show(rev, 'CONTENTS.md')
    m = re.search(r'\*\*(\d+) manuscripts covering (\d+) result families', contents)
    c['CONTENTS headline manuscripts'] = int(m.group(1)) if m else None
    c['CONTENTS headline families'] = int(m.group(2)) if m else None

    # formalization.yaml
    y = show(rev, 'lean/formalization.yaml')
    src = re.findall(r'id: \.\./preprints/([^/]+)/', y.split('related_formalizations:')[0])
    c['yaml sources (entries)'] = len(src)
    c['yaml sources (distinct dirs)'] = len(set(src))
    rel = y.split('related_formalizations:')[1].split('status:')[0] if 'related_formalizations:' in y else ''
    c['yaml related_formalizations entries'] = len(re.findall(r'^\s*- id:', rel, re.M))
    mr = re.findall(r'comparator_config: ComparatorChallenges/([^\s]+)\.json', y)
    decl = re.findall(r'declaration: (\S+)', y)
    c['yaml main_results entries'] = len(mr)
    c['yaml main_results distinct configs'] = len(set(mr))
    c['yaml main_results distinct declarations'] = len(set(decl))
    c['yaml sources + related'] = len(src) + c['yaml related_formalizations entries']

    # Comparator configs
    cfgs = [p for p in ls(rev, 'lean/ComparatorChallenges') if p.endswith('.json')]
    tn = []
    for p in cfgs:
        try:
            tn += json.loads(show(rev, p)).get('theorem_names', [])
        except Exception:
            pass
    c['comparator configs'] = len(cfgs)
    c['comparator configs not *Support'] = len([p for p in cfgs if not p.endswith('Support.json')])
    c['comparator theorem_names (total)'] = len(tn)
    c['comparator theorem_names (distinct)'] = len(set(tn))

    # docs scope notes
    docs = [p for p in ls(rev, 'lean/docs') if p.endswith('.md')]
    dp = set(); per_doc = []; rows = 0; rows_nosupport = 0; first_paper = set()
    for p in docs:
        t = show(rev, p)
        ps = PAPER_LINK.findall(t.split('## Scope')[0])
        if ps:
            first_paper.add(ps[0])
        ps = set(PAPER_LINK.findall(t))
        dp |= ps; per_doc.append(len(ps))
        table = t.split('## Comparator links')[-1] if '## Comparator links' in t else ''
        for line in table.splitlines():
            if line.startswith('| ') and not line.startswith('| Result') and not line.startswith('| ---'):
                rows += 1
                if not re.search(r'support|lemma|auxiliar|ingredient', line, re.I):
                    rows_nosupport += 1
    c['lean/docs files'] = len(docs)
    c['distinct papers linked from lean/docs'] = len(dp)
    c['sum over docs of linked papers'] = sum(per_doc)
    c['docs-linked papers not withdrawn'] = len(dp - withdrawn)
    c['docs: first-listed paper per scope note'] = len(first_paper)
    c['docs Comparator-link table rows'] = rows
    c['docs table rows not mentioning support/lemma'] = rows_nosupport

    # CONTENTS families / manuscripts
    parts = re.split(r'\*\*(\d{3})\. ', contents)
    fam_lean = 0; ms_lean = set(); ms_all = set(); fam_lean_first = 0
    for i in range(1, len(parts), 2):
        body = parts[i + 1]
        head = body.split('</td>')[0]
        papers = PAPER_LINK.findall(body)
        ms_all |= set(papers)
        if 'lean/docs/' in head:
            fam_lean += 1; ms_lean |= set(papers)
            if papers: fam_lean_first += 1
    c['CONTENTS families'] = len(parts) // 2
    c['CONTENTS families with (Lean) link'] = fam_lean
    c['CONTENTS manuscripts (distinct links)'] = len(ms_all)
    c['manuscripts in (Lean) families'] = len(ms_lean)
    c['manuscripts in (Lean) families AND linked from docs'] = len(ms_lean & dp)
    c['yaml sources U docs-linked'] = len(set(src) | dp)

    # overview.tex
    ov = show(rev, 'overview.tex')
    c['overview \\resultentry count'] = len(re.findall(r'\\resultentry\{', ov))
    c['overview mentions of Lean (word)'] = len(re.findall(r'\bLean\b', ov))

    # papers referenced from Lean sources (docstrings / comments)
    leanfiles = [p for p in ls(rev, 'lean') if p.endswith('.lean')]
    c['lean files'] = len(leanfiles)
    return c, dp, set(src), ms_lean


revs = sys.argv[1:] or ['adc7f1241', 'fd4aeeb2e', '4eaee8754']
res = {}
for r in revs:
    res[r] = candidates(r)
keys = list(res[revs[0]][0].keys())
w = max(len(k) for k in keys)
print('candidate'.ljust(w), *[r[:9].rjust(10) for r in revs])
for k in keys:
    print(k.ljust(w), *[str(res[r][0].get(k)).rjust(10) for r in revs])

# brute force: which candidate or simple combination equals 300 (at fd4aeeb2e)?
target_rev = 'fd4aeeb2e' if 'fd4aeeb2e' in res else revs[-1]
vals = {k: v for k, v in res[target_rev][0].items() if isinstance(v, int)}
hits = [k for k, v in vals.items() if v == 300]
print(f'\nsingle candidates equal to 300 at {target_rev}:', hits or 'none')
pairs = [(a, b, vals[a] + vals[b]) for a in vals for b in vals if a < b and vals[a] + vals[b] == 300]
diffs = [(a, b) for a in vals for b in vals if a != b and vals[a] - vals[b] == 300]
print('pairwise sums equal to 300:', pairs or 'none')
print('pairwise differences equal to 300:', diffs or 'none')

# deltas between first two revisions ("6 formalizations and 5 other additions")
if len(revs) >= 2:
    a, b = revs[0], revs[1]
    print(f'\ndeltas {a} -> {b}:')
    for k in keys:
        va, vb = res[a][0].get(k), res[b][0].get(k)
        if isinstance(va, int) and isinstance(vb, int) and va != vb:
            print(f'  {k}: {va} -> {vb} ({vb - va:+d})')
