"""Compare constant fingerprints of a Comparator challenge with its solution.
Usage: python3 -I compare.py challenge.tsv solution.tsv [name ...]
Rows: name, module, kind, universe params, type hash, value hash (definitions only).
For definitions/inductives/constructors/recursors the type (and value) must match;
for theorems only the type is compared (the solution supplies the proof)."""
import sys, collections
def load(p):
    d = {}
    for l in open(p, encoding='utf-8'):
        f = l.rstrip('\n').split('\t')
        if len(f) >= 6: d[f[0]] = f[1:]
    return d
ch, so = load(sys.argv[1]), load(sys.argv[2])
focus = sys.argv[3:]
res = collections.Counter(); bad = []
for n, (mod, kind, lp, ty, val) in sorted(ch.items()):
    s = so.get(n)
    if s is None:
        res[f'{kind}: missing in solution'] += 1; bad.append((n, kind, 'MISSING')); continue
    smod, skind, slp, sty, sval = s
    if (kind, lp, ty) != (skind, slp, sty):
        res[f'{kind}: TYPE DIFFERS'] += 1; bad.append((n, kind, 'type/kind differs', smod)); continue
    if kind in ('def', 'opaque') and val != sval:
        res[f'{kind}: VALUE DIFFERS'] += 1; bad.append((n, kind, 'value differs', smod)); continue
    res[f'{kind}: identical'] += 1
for k, v in sorted(res.items()): print(f'{v:6d}  {k}')
for b in bad[:40]: print('  ', *b)
for n in focus:
    print('focus', n, 'challenge', ch.get(n), 'solution', so.get(n))
