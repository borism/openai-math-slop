"""Check that each line of a curated result file is a token-subset (in order) of the corresponding kept
line of a rerun stdout.  Kept rerun lines: those whose first token equals the first token of some curated
line.  Usage: python3 -I curated_subset.py RERUN_STDOUT CURATED [EXTRA_CURATED_ONLY_TOKEN...]"""
import sys
rerun = [l.split() for l in open(sys.argv[1]).read().splitlines() if l.strip()]
cur = [l.split() for l in open(sys.argv[2]).read().splitlines() if l.strip()]
extra = set(sys.argv[3:])
cur = [c for c in cur if not (len(c) == 1 and c[0] in extra)]
heads = {c[0] for c in cur}
kept = [r for r in rerun if r[0] in heads]
ok = len(kept) == len(cur)
for r, c in zip(kept, cur):
    it = iter(r)
    if not all(any(t == u for u in it) for t in c):
        ok = False; print('DIFF', ' '.join(c), '|', ' '.join(r))
print(f'{sys.argv[2].split("/")[-1]}: curated lines={len(cur)} kept rerun lines={len(kept)} -> {"SUBSET MATCH" if ok else "MISMATCH"}')
