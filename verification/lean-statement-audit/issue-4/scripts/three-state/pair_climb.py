"""Adversarial search for violations of Lemma loc:pair: minimise slack/(X z) over (current, child, a)
by a vectorised random-perturbation hill climb from K starts (no SciPy available).
Reuses pair() from pair_test.py (same directory).  Usage: python3 -I pair_climb.py K ITERS SEED"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from pair_test import pair

def decode(th):
    u = th[:, 0:3]; e = np.exp(u - u.max(1, keepdims=True)); m = 3 * e / e.sum(1, keepdims=True)
    u = th[:, 3:6]; e = np.exp(u - u.max(1, keepdims=True)); c = 3 * e / e.sum(1, keepdims=True)
    a = 0.5 / (1 + np.exp(-th[:, 6]))
    return m, c, a

def score(th, key):
    m, c, a = decode(th)
    scale, ch = pair(m, c, a)
    return np.where(scale > 1e-14, ch[key] / np.maximum(scale, 1e-300), 1e3)

def main(K, iters, seed):
    rng = np.random.default_rng(seed)
    keys = ['dn<=13/2Xz', 'de>=-79/250Xz', 'de<=11Xz', 'xpair', 'ypair_lo', 'ypair_hi', 'kpair']
    for key in keys:
        th = rng.normal(size=(K, 7)) * rng.choice([0.05, 1, 4, 10], size=(K, 1))
        f = score(th, key)
        for it in range(iters):
            step = rng.choice([1e-3, 1e-2, 1e-1, 1.0], size=(K, 1))
            cand = th + step * rng.normal(size=(K, 7))
            fc = score(cand, key)
            better = fc < f
            th[better] = cand[better]; f[better] = fc[better]
        i = np.argmin(f); m, c, a = decode(th[i:i + 1])
        X = abs((m[0] * np.exp(2j * np.pi * np.arange(3) / 3)).sum() / 3) ** 2
        print(f'{key:16s} min slack/(Xz)={f[i]: .6e} at current={np.round(m[0],5)} child={np.round(c[0],5)} a={a[0]:.5f} X={X:.3e}', flush=True)

if __name__ == '__main__':
    main(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
