#!/usr/bin/env python3
"""Rank Comparator challenges by challenge-side (non-Mathlib) declarations the statement can depend on.

Usage: python3 -I trust_surface.py <openai-math-checkout> > out.tsv
A challenge is the module named in each ComparatorChallenges/*.json (directory challenges such as
HodgeConjectureCMAbelianVarieties are counted with every .lean file in their directory).
Counts: data-like declarations (def/abbrev/structure/inductive/class/instance/opaque), proved
declarations (theorem/lemma), and non-blank lines.
"""
import glob, json, os, re, sys
root = sys.argv[1]
CC = os.path.join(root, 'lean', 'ComparatorChallenges')
data_re = re.compile(r'^\s*(?:@\[[^\]]*\]\s*)*(?:(?:private|protected|noncomputable|partial|unsafe|scoped|local)\s+)*(def|abbrev|structure|inductive|class|instance|opaque)\b', re.M)
thm_re = re.compile(r'^\s*(?:@\[[^\]]*\]\s*)*(?:(?:private|protected)\s+)*(theorem|lemma)\b', re.M)
rows = []
seen = set()
for j in sorted(glob.glob(os.path.join(CC, '*.json')) + glob.glob(os.path.join(CC, '*', 'main.json'))):
    cfg = json.load(open(j))
    mod = cfg.get('challenge_module', '')
    rel = mod.split('.', 1)[1] if '.' in mod else mod
    parts = rel.split('.')
    single = os.path.join(CC, *parts) + '.lean'
    if os.path.basename(j) == 'main.json':
        files = glob.glob(os.path.join(os.path.dirname(j), '**', '*.lean'), recursive=True)
        files = [f for f in files if not f.endswith('Solution.lean')]
        name = os.path.basename(os.path.dirname(j))
    else:
        files = [single] if os.path.exists(single) else []
        name = os.path.basename(j)[:-5]
    if name in seen or not files:
        continue
    seen.add(name)
    text = ''.join(open(f, encoding='utf-8', errors='replace').read() for f in files)
    text_nc = re.sub(r'/-.*?-/', '', text, flags=re.S)
    rows.append((len(data_re.findall(text_nc)), len(thm_re.findall(text_nc)),
                 sum(1 for l in text.splitlines() if l.strip()), len(files), name))
rows.sort(reverse=True)
print('challenge\tdata_decls\tproved_decls\tnonblank_lines\tfiles')
for d, t, l, n, name in rows:
    print(f'{name}\t{d}\t{t}\t{l}\t{n}')
