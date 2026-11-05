#!/usr/bin/env python3
"""Inventory of Lean comparator challenges vs docs scope notes vs papers.
Usage: python3 inv.py <math-repo-root> <outdir>"""
import json, os, re, sys, glob, collections

root, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
L = os.path.join(root, 'lean')
CC = os.path.join(L, 'ComparatorChallenges')

def read(p):
    with open(p, encoding='utf-8', errors='replace') as f:
        return f.read()

# --- configs
configs = {}
for j in sorted(glob.glob(os.path.join(CC, '*.json'))):
    name = os.path.basename(j)[:-5]
    try:
        cfg = json.loads(read(j))
    except Exception as e:
        cfg = {'_error': str(e)}
    configs[name] = cfg

# --- docs
docs = {}
for d in sorted(glob.glob(os.path.join(L, 'docs', '*.md'))):
    fam = os.path.basename(d)[:-3]
    t = read(d)
    papers = re.findall(r'\]\(\.\./\.\./preprints/([^/)]+)/paper\.pdf\)', t)
    chals = re.findall(r'\]\(\.\./ComparatorChallenges/([^)]+?)\.lean\)', t)
    chals += re.findall(r'\]\(\.\./ComparatorChallenges/([^)]+?)/Challenge\.lean\)', t)
    docs[fam] = {'papers': papers, 'challenges': chals, 'text': t}

# map challenge -> families
ch2fam = collections.defaultdict(list)
for fam, d in docs.items():
    for c in d['challenges']:
        ch2fam[c].append(fam)

# --- challenge statements
STD = {'propext', 'Quot.sound', 'Classical.choice'}
decl_re = re.compile(r'^(?:@\[[^\]]*\]\s*)?(?:private\s+|protected\s+|noncomputable\s+)*(theorem|lemma|def|abbrev|structure|class|inductive|axiom|opaque|instance|example)\s+([^\s:({\[]+)', re.M)

def challenge_path(cfg):
    m = cfg.get('challenge_module', '')
    p = os.path.join(L, *m.split('.')) + '.lean'
    return p

PAT = {
    'sInf/sSup': r'\bsInf\b|\bsSup\b|⨅|⨆|\biInf\b|\biSup\b',
    'toReal/toNNReal': r'\.toReal\b|ENNReal\.toReal|\.toNNReal\b|ENNReal\.toNNReal',
    'nat_sub_div': r'\(\s*\w+\s*-\s*\d+\s*\)|\bNat\.sub\b|/ \(?\d',
    'tsum/integral/deriv': r'∑\'|\btsum\b|∫|\bderiv\b|\bfderiv\b|\blimUnder\b',
    'Classical.choose': r'Classical\.choose|Classical\.epsilon|Exists\.choose',
    'Published/Assumption': r'\bPublished\w*|\bAssum\w*|\bHypothes\w*|\bInput\w*',
    'axiom_decl': r'^\s*axiom\s',
    'opaque_decl': r'^\s*(?:noncomputable\s+)?opaque\s',
    'sorry_count': r'\bsorry\b',
    'True_concl': r':\s*True\b|∧\s*True\b',
}

rows = []
for name, cfg in configs.items():
    r = {'config': name, 'families': ch2fam.get(name, [])}
    if '_error' in cfg:
        r['error'] = cfg['_error']; rows.append(r); continue
    p = challenge_path(cfg)
    r['challenge_file'] = os.path.relpath(p, root)
    r['exists'] = os.path.exists(p)
    r['theorems'] = cfg.get('theorem_names', [])
    r['definitions'] = cfg.get('definition_names', [])
    r['extra_axioms'] = sorted(set(cfg.get('permitted_axioms', [])) - STD)
    r['nanoda'] = cfg.get('enable_nanoda')
    if not r['exists']:
        rows.append(r); continue
    t = read(p)
    r['bytes'] = len(t)
    r['lines'] = t.count('\n')
    r['imports_oai'] = len(re.findall(r'^import\s+OAI', t, re.M))
    r['imports'] = re.findall(r'^import\s+(\S+)', t, re.M)
    decls = decl_re.findall(t)
    r['n_decls'] = len(decls)
    shortnames = [n for _, n in decls]
    # check theorem names exist (by last component or full)
    missing = []
    for th in r['theorems'] + r['definitions']:
        last = th.split('.')[-1]
        if last not in shortnames and th not in shortnames and not any(s.endswith(last) for s in shortnames):
            missing.append(th)
    r['missing_names'] = missing
    flags = {}
    for k, pat in PAT.items():
        n = len(re.findall(pat, t, re.M))
        if n: flags[k] = n
    r['flags'] = flags
    # sorry located outside the target theorems? count theorem-like decls with sorry
    rows.append(r)

with open(os.path.join(out, 'inventory.json'), 'w') as f:
    json.dump({'rows': rows, 'docs': {k: {'papers': v['papers'], 'challenges': v['challenges']} for k, v in docs.items()}}, f, indent=1)

# --- summary
print('configs', len(configs), 'docs', len(docs))
print('configs not linked from any docs note:', [r['config'] for r in rows if not r['families']])
print('docs links to missing challenges:', [(f, c) for f, d in docs.items() for c in d['challenges'] if c not in configs and c.split('/')[0] not in configs])
print('missing challenge files:', [r['config'] for r in rows if r.get('exists') is False])
print('theorem names not found:', [(r['config'], r['missing_names']) for r in rows if r.get('missing_names')])
print('extra axioms:', [(r['config'], r['extra_axioms']) for r in rows if r.get('extra_axioms')])
print('axiom/opaque decls:', [(r['config'], {k: v for k, v in r['flags'].items() if k in ('axiom_decl', 'opaque_decl')}) for r in rows if r.get('flags') and ('axiom_decl' in r['flags'] or 'opaque_decl' in r['flags'])])
print('nanoda true:', [r['config'] for r in rows if r.get('nanoda')])
print('challenges importing OAI modules:', [(r['config'], r['imports_oai']) for r in rows if r.get('imports_oai')])
print('docs with no papers:', [f for f, d in docs.items() if not d['papers']])
missing_papers = [(f, p) for f, d in docs.items() for p in d['papers'] if not os.path.isdir(os.path.join(root, 'preprints', p))]
print('docs links to missing paper dirs:', missing_papers)
sz = sorted(rows, key=lambda r: -r.get('bytes', 0))
print('largest challenges:', [(r['config'], r.get('bytes')) for r in sz[:15]])
print('smallest challenges:', [(r['config'], r.get('bytes')) for r in sz[-15:]])
c = collections.Counter()
for r in rows:
    for k in r.get('flags', {}):
        c[k] += 1
print('flag counts:', dict(c))
