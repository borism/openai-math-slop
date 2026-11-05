"""Hill-climb as in pair_climb.py, then print the 25 lowest-scoring points per inequality (7 floats per line)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from pair_climb import decode, score
K, iters, seed = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
rng = np.random.default_rng(seed)
for key in ['dn<=13/2Xz', 'de>=-79/250Xz', 'de<=11Xz', 'xpair', 'ypair_lo', 'ypair_hi', 'kpair']:
    th = rng.normal(size=(K, 7)) * rng.choice([0.05, 1, 4, 10], size=(K, 1))
    f = score(th, key)
    for it in range(iters):
        cand = th + rng.choice([1e-3, 1e-2, 1e-1, 1.0], size=(K, 1)) * rng.normal(size=(K, 7))
        fc = score(cand, key); b = fc < f; th[b] = cand[b]; f[b] = fc[b]
    for i in np.argsort(f)[:25]:
        m, c, a = decode(th[i:i + 1])
        print(' '.join(repr(float(t)) for t in list(m[0]) + list(c[0]) + [a[0]]))
