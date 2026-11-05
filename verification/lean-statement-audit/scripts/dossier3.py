#!/usr/bin/env python3
"""Build one dossier per Lean docs family: scope note, challenge target statements,
and the paper's abstract + first theorem-like environments.
Usage: python3 dossier.py <math-repo-root> <outdir>"""
import json, os, re, sys, glob

root, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
L = os.path.join(root, 'lean')
CC = os.path.join(L, 'ComparatorChallenges')

def read(p):
    with open(p, encoding='utf-8', errors='replace') as f:
        return f.read()

def strip_comments_tex(t):
    return re.sub(r'(?<!\\)%.*', '', t)

def expand_inputs(path, depth=0):
    """Concatenate a tex file with its \\input / \\include children."""
    if depth > 4 or not os.path.exists(path):
        return ''
    t = strip_comments_tex(read(path))
    base = os.path.dirname(path)
    def rep(m):
        name = m.group(1).strip()
        cand = [os.path.join(base, name), os.path.join(base, name + '.tex')]
        for c in cand:
            if os.path.isfile(c):
                return expand_inputs(c, depth + 1)
        return ''
    return re.sub(r'\\(?:input|include|subfile)\{([^}]+)\}', rep, t)

def paper_text(pdir):
    b = os.path.join(pdir, 'build')
    if not os.path.isdir(b):
        b = pdir
    mains = []
    for f in glob.glob(os.path.join(b, '**', '*.tex'), recursive=True):
        t = read(f)
        if '\\documentclass' in t:
            mains.append(f)
    mains.sort(key=lambda f: (os.path.basename(f) not in ('paper.tex', 'main.tex'), len(f)))
    if not mains:
        return ''
    return expand_inputs(mains[0])

ENV = r'(theorem|maintheorem|mainthm|thm|theoremA|theoremx|thmx|corollary|cor|proposition|prop|conjecture)\*?'

def main_statements(t, k=1):
    ab = re.search(r'\\begin\{abstract\}(.*?)\\end\{abstract\}', t, re.S)
    res = []
    if ab:
        res.append('ABSTRACT: ' + ' '.join(ab.group(1).split())[:700])
    for m in re.finditer(r'\\begin\{' + ENV + r'\}(\[[^\]]*\])?(.*?)\\end\{\1\*?\}', t, re.S):
        body = ' '.join(m.group(3).split())
        res.append(f'[{m.group(1)}{m.group(2) or ""}] ' + body[:700])
        if len(res) >= k + 1:
            break
    return res

decl_start = re.compile(r'^(?:@\[[^\]]*\]\s*)?(?:private\s+|protected\s+|noncomputable\s+)*(theorem|lemma|def|abbrev|structure|class|inductive|axiom|opaque|instance)\s+([^\s:({\[]+)', re.M)

def lean_decls(t):
    ms = list(decl_start.finditer(t))
    out = []
    for i, m in enumerate(ms):
        end = ms[i + 1].start() if i + 1 < len(ms) else len(t)
        # trim trailing 'end X' / namespace lines
        body = t[m.start():end]
        body = re.sub(r'\n(end\b.*|namespace\b.*|section\b.*|open\b.*|variable\b.*|universe\b.*)\s*$', '', body.rstrip())
        out.append((m.group(1), re.sub(r'\.\{[^}]*\}$', '', m.group(2)), body.rstrip()))
    return out

def challenge_files(fam_doc):
    t = fam_doc
    cs = re.findall(r'\]\(\.\./ComparatorChallenges/([^)]+?)\.lean\)', t)
    return cs

docs = sorted(glob.glob(os.path.join(L, 'docs', '*.md')))
index = []
for d in docs:
    fam = os.path.basename(d)[:-3]
    t = read(d)
    papers = re.findall(r'\]\(\.\./\.\./preprints/([^/)]+)/[^)]*\.pdf\)', t)
    chals = challenge_files(t)
    sc=t.split('## Comparator links')[0].split('## Scope',1)[-1].strip()
    parts = [f'# FAMILY {fam}: '+t.splitlines()[0].lstrip('# ')+'\n', 'SCOPE: '+' '.join(sc.split())[:900]]
    for c in chals:
        p = os.path.join(CC, c + '.lean')
        j = os.path.join(CC, c.split('/')[0] + '.json')
        cfg = json.loads(read(j)) if os.path.exists(j) else {}
        names = [n.split('.')[-1] for n in cfg.get('theorem_names', [])]
        parts.append(f'## CHALLENGE {c}  targets={cfg.get("theorem_names")} defs={cfg.get("definition_names")}\n')
        if not os.path.exists(p):
            parts.append('(file missing)\n'); continue
        ct = read(p)
        ds = lean_decls(ct)
        # print all non-theorem decl headers (first 3 lines), full text of target theorems
        hdr=[]
        for kind, name, body in ds:
            if name in names:
                parts.append(body[:1800] + "\n")
            else:
                hdr.append(kind+' '+name)
        parts.append('DEFS(%d): '%len(hdr) + ', '.join(hdr[:30]))
    for pp in papers:
        pt = paper_text(os.path.join(root, 'preprints', pp))
        parts.append(f'## PAPER {pp}\n')
        for s in main_statements(pt):
            parts.append(s + '\n')
    txt = '\n'.join(parts)
    with open(os.path.join(out, fam + '.md'), 'w') as f:
        f.write(txt)
    index.append((fam, len(txt), len(chals), len(papers)))

with open(os.path.join(out, 'INDEX.tsv'), 'w') as f:
    for r in index:
        f.write('\t'.join(map(str, r)) + '\n')
print(len(index), sum(r[1] for r in index))
