#!/usr/bin/env python3
"""Per-file diff of the CM Hodge challenge tree (openai/math) against a Paul-Lez/HodgeConjecture commit.

Usage: python3 -I diff_vs_upstream.py <openai-math-git-dir> <challenge-rev> <upstream-clone> <upstream-rev> <outdir>
Writes <outdir>/summary.tsv and <outdir>/diffs/<path>.diff (unified diffs, header line dropped).
Token counts ignore comments, the 'This file has been modified.' line, import/open/namespace lines,
module/public/@[expose] keywords and dotted-name prefixes (so pure renames/namespacing count as 0).
"""
import difflib, os, re, subprocess, sys
om, rev, up, urev, out = sys.argv[1:6]
P = 'lean/ComparatorChallenges/HodgeConjectureCMAbelianVarieties/HodgeConjecture/'
os.makedirs(os.path.join(out, 'diffs'), exist_ok=True)

def git(d, *a):
    r = subprocess.run(['git', '-C', d, *a], capture_output=True, text=True, errors='replace')
    return r.stdout if r.returncode == 0 else None

def clean(t):
    return [l.rstrip() for l in t.splitlines() if l.strip() != 'This file has been modified.']

def toks(t):
    t = re.sub(r'/-.*?-/', '', t, flags=re.S); t = re.sub(r'--.*', '', t)
    t = re.sub(r'^\s*(public\s+)?(import|open|namespace|end|section|module|open scoped)\b.*$', '', t, flags=re.M)
    t = re.sub(r'\b(public|private|protected)\s+', '', t); t = re.sub(r'@\[expose\]\s*', '', t)
    t = re.sub(r"\b(?:[A-Za-z_][\w']*\.)+([A-Za-z_][\w']*)", r'\1', t)
    t = re.sub(r'\bComplexSchemePoint\b', 'ComplexPoint', t)
    return re.findall(r"[\w']+|[^\s\w]", t)

files = [l for l in git(om, 'ls-tree', '-r', '--name-only', rev, '--', P).split()]
rows = []
for f in files:
    rel = f[len(P):]
    a = git(up, 'show', f'{urev}:HodgeConjecture/{rel}')
    b = git(om, 'show', f'{rev}:{f}')
    if a is None:
        rows.append((rel, 'ONLY_IN_CHALLENGE', 0, len(toks(b)), '')); continue
    ca, cb = clean(a), clean(b)
    if ca == cb:
        rows.append((rel, 'identical', 0, 0, '')); continue
    d = list(difflib.unified_diff(ca, cb, f'upstream/{rel}', f'challenge/{rel}', lineterm='', n=2))
    p = os.path.join(out, 'diffs', rel + '.diff'); os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, 'w').write('\n'.join(d) + '\n')
    ta, tb = toks('\n'.join(ca)), toks('\n'.join(cb))
    ops = [o for o in difflib.SequenceMatcher(None, ta, tb, autojunk=False).get_opcodes() if o[0] != 'equal']
    e = sum(max(i2 - i1, j2 - j1) for _, i1, i2, j1, j2 in ops)
    added = sum(1 for l in d if l.startswith('+') and not l.startswith('+++'))
    removed = sum(1 for l in d if l.startswith('-') and not l.startswith('---'))
    rows.append((rel, 'differs', e, added, f'-{removed}/+{added} lines'))
with open(os.path.join(out, 'summary.tsv'), 'w') as fh:
    fh.write('file\tstatus\tresidual_token_edits\textra\tlines\n')
    for r in sorted(rows, key=lambda r: (-r[2], r[0])):
        fh.write('\t'.join(map(str, r)) + '\n')
from collections import Counter
c = Counter(r[1] for r in rows)
print(dict(c))
print('differs with residual token edits > 0:', sum(1 for r in rows if r[1] == 'differs' and r[2] > 0))
for r in sorted(rows, key=lambda r: -r[2])[:30]:
    if r[2] or r[1] != 'identical':
        print(r)
