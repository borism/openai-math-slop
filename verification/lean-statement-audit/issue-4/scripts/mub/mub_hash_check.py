"""SHA-256 checks for the MUB d=6 package (family 266).
(1) the 7 C++ sources in verification/saved-run/compiled-build/source against verification/code/extraction.json;
(2) the 8 principal data files in verification/saved-run/execution/data against Table execute:hashes in
    build/sections/execution.tex (parsed from the LaTeX, not retyped).
Usage: python3 -I mub_hash_check.py <paper-dir>.  Prints one line per file and exits 1 on any mismatch."""
import hashlib, json, re, sys
from pathlib import Path

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def main(root):
    root = Path(root); bad = 0
    ext = json.loads((root / 'verification/code/extraction.json').read_text())
    src = root / 'verification/saved-run/compiled-build/source'
    print('# sources vs verification/code/extraction.json')
    for e in ext['files']:
        p = src / e['file']; h = sha(p); n = p.stat().st_size
        ok = h == e['sha256'] and n == e['bytes']; bad += not ok
        print(f"{'MATCH' if ok else 'MISMATCH'} {e['file']} bytes={n} sha256={h}")
    extra = sorted(set(x.name for x in src.iterdir()) - {e['file'] for e in ext['files']})
    print(f'# source files not listed in extraction.json: {extra}')
    tex = (root / 'build/sections/execution.tex').read_text()
    block = tex[tex.index(r'\label{execute:hashes}'):]
    block = block[:block.index(r'\end{longtable}')]
    rows = re.findall(r'\\texttt\{([\w.]+)\} & \{\\scriptsize\\texttt\{([0-9a-f]{64})\}\}', block)
    print(f'# data files vs Table execute:hashes ({len(rows)} rows)')
    data = root / 'verification/saved-run/execution/data'
    for name, want in rows:
        h = sha(data / name); ok = h == want; bad += not ok
        print(f"{'MATCH' if ok else 'MISMATCH'} {name} sha256={h}")
    print('RESULT', 'ALL MATCH' if bad == 0 else f'{bad} MISMATCHES')
    return 1 if bad else 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
