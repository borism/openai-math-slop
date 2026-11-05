#!/usr/bin/env python3
"""Token-level diff of the CM Hodge Comparator challenge files changed by
openai/math commit 204e5f8f8 ("Align CM Hodge comparator declarations with the
Lean solution"). Dotted identifiers are reduced to their last component and
import/open/namespace/visibility lines are dropped, so pure renames and
module-system changes count as zero. Remaining token edits are listed.

Usage (inside a clone that has 204e5f8f8): python3 -I hodge_alignment_diff.py
"""
import difflib, re, subprocess

C = '204e5f8f8'
files = subprocess.run(['git', 'show', '--name-only', '--format=', C],
                       capture_output=True, text=True).stdout.split()
files = [f for f in files if f.endswith('.lean') and 'HodgeConjectureCMAbelianVarieties' in f]


def toks(t):
    t = re.sub(r'/-.*?-/', '', t, flags=re.S)
    t = re.sub(r'--.*', '', t)
    t = re.sub(r'^\s*(public\s+)?(import|open|namespace|end|section|module|open scoped)\b.*$', '', t, flags=re.M)
    t = re.sub(r'\b(public|private|protected)\s+', '', t)
    t = re.sub(r'@\[expose\]\s*', '', t)
    t = re.sub(r"\b(?:[A-Za-z_][\w']*\.)+([A-Za-z_][\w']*)", r'\1', t)
    return re.findall(r"[\w']+|[^\s\w]", t)


rows = []
for f in files:
    a = subprocess.run(['git', 'show', f'{C}^:{f}'], capture_output=True, text=True).stdout
    b = subprocess.run(['git', 'show', f'{C}:{f}'], capture_output=True, text=True).stdout
    ta, tb = toks(a), toks(b)
    ops = difflib.SequenceMatcher(None, ta, tb, autojunk=False).get_opcodes()
    ins = sum(j2 - j1 for op, i1, i2, j1, j2 in ops if op in ('insert', 'replace'))
    dele = sum(i2 - i1 for op, i1, i2, j1, j2 in ops if op in ('delete', 'replace'))
    rows.append((ins + dele, f.split('Varieties/')[1], len(ta), len(tb), ins, dele))
rows.sort(reverse=True)
print(f'files changed by {C} in the CM Hodge challenge tree: {len(rows)}')
print('files with zero token change after normalisation:', sum(1 for r in rows if r[0] == 0))
print('files with residual token changes:', sum(1 for r in rows if r[0] > 0))
print('largest residual changes (edits, file, old tokens, new tokens, inserted, deleted):')
for r in rows[:25]:
    print(' ', r)
