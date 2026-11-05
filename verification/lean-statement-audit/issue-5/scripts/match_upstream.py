#!/usr/bin/env python3
"""Find the Paul-Lez/HodgeConjecture commit(s) closest to the CM Hodge challenge tree.

Usage: python3 -I match_upstream.py <openai-math-git-dir> <challenge-rev> <upstream-clone> [all]
Compares, per upstream commit, how many challenge files are byte-identical to the upstream file
after deleting the line 'This file has been modified.' and trailing whitespace.
"""
import subprocess, sys, hashlib, re
om, rev, up = sys.argv[1], sys.argv[2], sys.argv[3]
scan_all = len(sys.argv) > 4
P = 'lean/ComparatorChallenges/HodgeConjectureCMAbelianVarieties/HodgeConjecture/'

def git(d, *a):
    return subprocess.run(['git', '-C', d, *a], capture_output=True, text=True, errors='replace').stdout

def norm(t):
    t = '\n'.join(l.rstrip() for l in t.splitlines() if l.strip() != 'This file has been modified.')
    return hashlib.sha1(t.strip().encode()).hexdigest()

chal = {}
for line in git(om, 'ls-tree', '-r', rev, '--', P).splitlines():
    meta, path = line.split('\t')
    blob = meta.split()[2]
    chal[path[len(P):]] = norm(git(om, 'cat-file', '-p', blob))

refs = ['HEAD'] if not scan_all else [l.split()[0] for l in git(up, 'for-each-ref', '--format=%(objectname) %(refname)', 'refs/remotes').splitlines()]
commits = git(up, 'rev-list', '--date-order', *refs).split()
cache = {}
best = []
for c in commits:
    m = 0
    for line in git(up, 'ls-tree', '-r', c, '--', 'HodgeConjecture').splitlines():
        meta, path = line.split('\t')
        rel = path[len('HodgeConjecture/'):]
        if rel not in chal:
            continue
        blob = meta.split()[2]
        if blob not in cache:
            cache[blob] = norm(git(up, 'cat-file', '-p', blob))
        m += cache[blob] == chal[rel]
    best.append((m, c))
best.sort(reverse=True)
print(f'challenge rev {rev}: {len(chal)} files; scanned {len(commits)} upstream commits')
for m, c in best[:8]:
    info = git(up, 'log', '-1', '--format=%h %ad %s', '--date=iso', c).strip()
    print(f'{m:4d} identical  {info}')
