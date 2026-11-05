#!/usr/bin/env python3
"""Cross-check lean/formalization.yaml, lean/docs/*.md scope notes, Comparator configs
and CONTENTS.md at a given openai/math checkout.

Usage: python3 -I catalogue_check.py <math-repo-root>
"""
import glob, json, os, re, sys

root = sys.argv[1]
L = os.path.join(root, 'lean')


def read(p):
    with open(p, encoding='utf-8', errors='replace') as f:
        return f.read()


y = read(os.path.join(L, 'formalization.yaml'))
sources = set(re.findall(r'id: \.\./preprints/([^/]+)/', y))
main_cfgs = re.findall(r'comparator_config: ComparatorChallenges/([^\s]+)\.json', y)

docs = {}
for d in sorted(glob.glob(os.path.join(L, 'docs', '*.md'))):
    t = read(d)
    docs[os.path.basename(d)[:-3]] = {
        'papers': re.findall(r'\]\(\.\./\.\./preprints/(.+?)/[^/]*\.pdf\)', t),
        'configs': sorted(set(re.findall(r'\]\(\.\./ComparatorChallenges/([A-Za-z0-9]+)', t))),
        'text': t,
    }
docs_papers = set(p for d in docs.values() for p in d['papers'])

print('yaml sources (papers "with a formalized main result"):', len(sources))
print('yaml status.main_results configs:', len(main_cfgs), 'distinct', len(set(main_cfgs)))
print('papers linked from lean/docs scope notes:', len(docs_papers))
print('yaml sources not linked from any scope note:', sorted(sources - docs_papers))

# Supporting-result configs listed as main results
readme = read(os.path.join(L, 'ComparatorChallenges', 'README.md'))
support = re.findall(r'`([A-Za-z]+Support)\.json`', readme)
print('\nComparator README "supporting-result comparisons" section present:', bool(support))
# The section listing these was removed from the README in openai/math 42907c9e9
# (Oct 26, 2026); fall back to the configs whose names end in "Support".
if not support:
    support = sorted(os.path.basename(j)[:-5] for j in glob.glob(os.path.join(L, 'ComparatorChallenges', '*Support.json')))
print('supporting-result configs:', support)
for s in support:
    fams = [f for f, d in docs.items() if s in d['configs']]
    in_main = s in main_cfgs
    for f in fams:
        listed = [(p in sources, p) for p in docs[f]['papers']]
        print(f'  {s}: in yaml main_results={in_main}; docs/{f}.md papers ->',
              [('LISTED' if a else 'not listed') + ' ' + p[:70] for a, p in listed])

# Scope-note sentences admitting the main theorem is outside
pat = re.compile(r"(outside (this|these|the) (comparison|selected|statement)|not (included|established|part of)|does not (establish|assert|include|cover)|weaker|supporting)", re.I)
print('\nyaml-listed papers whose scope note contains a limitation sentence:')
for f, d in sorted(docs.items()):
    listed = [p for p in d['papers'] if p in sources]
    if not listed:
        continue
    scope = d['text'].split('## Comparator links')[0].split('## Scope', 1)[-1]
    sents = [s for s in re.split(r'(?<=[.!?])\s+', ' '.join(scope.split())) if pat.search(s)]
    if sents:
        print(f'  docs/{f}.md listed={len(listed)}:', ' || '.join(s[:200] for s in sents))

# Coverage-figure reproduction
contents = read(os.path.join(root, 'CONTENTS.md'))
parts = re.split(r'\*\*(\d{3})\. ', contents)
fam_lean = papers_total = papers_lean = 0
for i in range(1, len(parts), 2):
    body = parts[i + 1]
    lean = 'lean/docs/' in body.split('</td>')[0]
    n = len(re.findall(r'\]\((preprints/[^)]+\.pdf)\)', body))
    papers_total += n
    if lean:
        fam_lean += 1
        papers_lean += n
print(f'\nCONTENTS.md: families={len(parts)//2} with (Lean) link={fam_lean}; manuscripts={papers_total}; manuscripts in (Lean) families={papers_lean}')

# Comparator config hygiene
cfgs = {}
for j in glob.glob(os.path.join(L, 'ComparatorChallenges', '*.json')):
    cfgs[os.path.basename(j)[:-5]] = json.loads(read(j))
nanoda = [k for k, v in cfgs.items() if v.get('enable_nanoda')]
print(f'\nComparator configs: {len(cfgs)}; enable_nanoda=true: {nanoda}')
std = {'propext', 'Quot.sound', 'Classical.choice'}
print('configs permitting non-standard axioms:', [k for k, v in cfgs.items() if set(v.get('permitted_axioms', [])) - std])
imp = []
for p in glob.glob(os.path.join(L, 'ComparatorChallenges', '**', '*.lean'), recursive=True):
    if re.search(r'^import OAI', read(p), re.M) and not p.endswith('Solution.lean'):
        imp.append(os.path.relpath(p, L))
print('challenge files importing the OAI solution library:', imp)
