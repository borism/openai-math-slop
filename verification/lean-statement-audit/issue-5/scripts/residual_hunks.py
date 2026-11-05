#!/usr/bin/env python3
"""List residual token-level hunks of a commit's changes to the CM Hodge challenge tree after
normalising comments, import/open/namespace lines, visibility keywords, dotted-name prefixes and the
ComplexPoint -> ComplexSchemePoint rename.

Usage (inside a clone with both revisions): python3 -I residual_hunks.py <old-rev> <new-rev> <subdir-filter> <out>
"""
import difflib, re, subprocess, sys
old, new, filt, out = sys.argv[1:5]
P = 'lean/ComparatorChallenges/HodgeConjectureCMAbelianVarieties/HodgeConjecture/'

def show(r, f):
    p = subprocess.run(['git', 'show', f'{r}:{f}'], capture_output=True, text=True)
    return p.stdout if p.returncode == 0 else ''

def toks(t):
    t = re.sub(r'/-.*?-/', '', t, flags=re.S); t = re.sub(r'--.*', '', t)
    t = re.sub(r'^\s*(public\s+)?(meta\s+)?(import|open|namespace|end|section|module|open scoped)\b.*$', '', t, flags=re.M)
    t = re.sub(r'\b(public|private|protected)\s+', '', t); t = re.sub(r'@\[expose\]\s*', '', t)
    t = re.sub(r"\b(?:[A-Za-z_][\w']*\.)+([A-Za-z_][\w']*)", r'\1', t)
    t = re.sub(r'\bComplexSchemePoint\b', 'ComplexPoint', t)
    return re.findall(r"[\w']+|[^\s\w]", t)

files = subprocess.run(['git', 'ls-tree', '-r', '--name-only', new, '--', P + filt], capture_output=True, text=True).stdout.split()
with open(out, 'w') as fh:
    for f in files:
        ta, tb = toks(show(old, f)), toks(show(new, f))
        ops = [o for o in difflib.SequenceMatcher(None, ta, tb, autojunk=False).get_opcodes() if o[0] != 'equal']
        if not ops:
            continue
        e = sum(max(i2 - i1, j2 - j1) for _, i1, i2, j1, j2 in ops)
        fh.write(f'\n##### {f[len(P):]}  ({len(ops)} hunks, {e} token edits)\n')
        for k, (op, i1, i2, j1, j2) in enumerate(ops):
            ctx = ' '.join(ta[max(0, i1 - 12):i1])
            fh.write(f'[{k}] {op}  ...{ctx[-100:]}\n    OLD: {" ".join(ta[i1:i2])[:400]}\n    NEW: {" ".join(tb[j1:j2])[:400]}\n')
print('written', out)
