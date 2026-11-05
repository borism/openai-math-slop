#!/usr/bin/env python3
"""Static trust scan of Lean sources (no Lean toolchain needed).

Two modes:
  closure <lean-root> <Module.Name> [<Module.Name> ...]
      follow `import`/`public import` lines recursively from the given modules
      and scan only the closure (modules outside <lean-root>, e.g. Mathlib or
      other dependencies, are listed but not scanned);
  tree <lean-root> <subdir>
      scan every .lean file under <lean-root>/<subdir>.

Comments (line `--` and block `/- -/`, including docstrings) and string
literals are stripped before matching, so hits are in code. The pattern list
is in PATTERNS. Output: per-pattern counts and every hit with file:line.

Usage: python3 -I trust_scan.py closure lean OAI.LinearAlgebra.MatrixMultiplication.Main
       python3 -I trust_scan.py tree lean OAI
"""
import os, re, sys
from collections import defaultdict, OrderedDict

PATTERNS = OrderedDict([
    ('axiom decl', r'^\s*(?:@\[[^\]]*\]\s*)?(?:private\s+|protected\s+|noncomputable\s+|unsafe\s+|partial\s+)*axiom\s'),
    ('sorry', r'\bsorry\b'),
    ('admit', r'\badmit\b'),
    ('native_decide', r'\bnative_decide\b'),
    ('Lean.ofReduceBool / ofReduceNat (compiler-trusting axiom)', r'ofReduceBool|ofReduceNat|Lean\.reduceBool|Lean\.reduceNat'),
    ('decide +kernel (kernel reduction, no extra axiom)', r'decide\s*\+kernel|\bdecide!'),
    ('trustCompiler', r'trustCompiler'),
    ('implemented_by', r'implemented_by'),
    ('extern', r'@\[\s*extern|\bextern\b'),
    ('unsafe', r'\bunsafe\b'),
    ('opaque decl', r'^\s*(?:@\[[^\]]*\]\s*)?(?:private\s+|protected\s+|noncomputable\s+)*opaque\s'),
    ('partial def', r'\bpartial\s+def\b'),
    ('run_tac', r'\brun_tac\b'),
    ('elab/macro/syntax definition', r'^\s*(?:@\[[^\]]*\]\s*)?(?:scoped\s+|local\s+)?(?:elab|macro|macro_rules|elab_rules|syntax|notation3?|infixl?|infixr|prefix|postfix)\b'),
    ('set_option (any)', r'\bset_option\b'),
    ('set_option debug.skipKernelTC', r'skipKernelTC'),
    ('set_option allowUnsafeReducibility', r'allowUnsafeReducibility'),
    ('set_option maxHeartbeats 0', r'maxHeartbeats\s+0\b'),
    ('set_option autoImplicit true', r'autoImplicit\s+true'),
    ('Decidable instance override (instance : Decidable)', r'instance[^:]*:\s*Decidable\b'),
    ('csimp attribute', r'@\[[^\]]*\bcsimp\b'),
    ('addDecl / Environment manipulation', r'\baddDecl\b|\bmodifyEnv\b|\bEnvironment\.addDecl'),
])

HARD = ['axiom decl', 'sorry', 'admit', 'native_decide', 'Lean.ofReduceBool / ofReduceNat (compiler-trusting axiom)',
        'trustCompiler', 'implemented_by', 'extern', 'unsafe', 'set_option debug.skipKernelTC',
        'addDecl / Environment manipulation']


def strip(text):
    # remove block comments (nested) and line comments and string literals
    out = []
    i, n, depth = 0, len(text), 0
    in_str = False
    while i < n:
        if depth == 0 and not in_str and text.startswith('"', i):
            in_str = True; out.append(' '); i += 1; continue
        if in_str:
            if text[i] == '\\':
                out.append('  '); i += 2; continue
            if text[i] == '"':
                in_str = False
            out.append('\n' if text[i] == '\n' else ' '); i += 1; continue
        if text.startswith('/-', i):
            depth += 1; out.append('  '); i += 2; continue
        if depth > 0 and text.startswith('-/', i):
            depth -= 1; out.append('  '); i += 2; continue
        if depth > 0:
            out.append('\n' if text[i] == '\n' else ' '); i += 1; continue
        if text.startswith('--', i):
            j = text.find('\n', i)
            j = n if j < 0 else j
            out.append(' ' * (j - i)); i = j; continue
        out.append(text[i]); i += 1
    return ''.join(out)


IMPORT_RE = re.compile(r'^\s*(?:public\s+)?(?:meta\s+)?import\s+(?:all\s+)?([A-Za-z0-9_.«»\']+)', re.M)


def mod_path(root, mod):
    return os.path.join(root, *mod.split('.')) + '.lean'


def closure(root, mods):
    seen, external, stack = OrderedDict(), set(), list(mods)
    while stack:
        m = stack.pop()
        if m in seen or m in external:
            continue
        p = mod_path(root, m)
        if not os.path.exists(p):
            external.add(m); continue
        t = open(p, encoding='utf-8', errors='replace').read()
        seen[m] = p
        for imp in IMPORT_RE.findall(strip(t)):
            stack.append(imp)
    return seen, external


def scan(files, root):
    counts = defaultdict(int); hits = defaultdict(list); total_lines = 0
    for p in files:
        raw = open(p, encoding='utf-8', errors='replace').read()
        s = strip(raw)
        lines = s.split('\n'); total_lines += len(lines)
        rel = os.path.relpath(p, os.path.dirname(os.path.abspath(root)))
        for k, pat in PATTERNS.items():
            rx = re.compile(pat)
            for ln, line in enumerate(lines, 1):
                if rx.search(line):
                    counts[k] += 1
                    hits[k].append(f'{rel}:{ln}: {raw.splitlines()[ln-1].strip()[:160] if ln-1 < len(raw.splitlines()) else ""}')
    return counts, hits, total_lines


def main():
    mode, root = sys.argv[1], sys.argv[2]
    if mode == 'closure':
        seen, ext = closure(root, sys.argv[3:])
        files = list(seen.values())
        print(f'closure of {sys.argv[3:]}: {len(files)} local modules; '
              f'{len(ext)} external imports')
        tops = sorted(set(e.split('.')[0] for e in ext))
        print('external import roots:', tops)
    else:
        sub = os.path.join(root, sys.argv[3])
        files = [os.path.join(d, f) for d, _, fs in os.walk(sub) for f in fs if f.endswith('.lean')]
        print(f'tree {sub}: {len(files)} files')
    counts, hits, nlines = scan(sorted(files), root)
    print(f'lines scanned: {nlines}')
    print('\npattern counts (code only; comments/strings stripped):')
    for k in PATTERNS:
        print(f'  {k:52s} {counts.get(k, 0)}')
    print('\nhits for hard trust patterns:')
    for k in HARD:
        for h in hits.get(k, []):
            print(f'  [{k}] {h}')
    soft = [k for k in PATTERNS if k not in HARD]
    print('\nfirst 40 hits for other patterns:')
    for k in soft:
        for h in hits.get(k, [])[:40]:
            print(f'  [{k}] {h}')
    if mode == 'closure':
        print('\nclosure modules:')
        for m in seen:
            print('  ', m)


if __name__ == '__main__':
    main()
