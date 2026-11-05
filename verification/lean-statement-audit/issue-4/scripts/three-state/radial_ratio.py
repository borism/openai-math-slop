"""Companion to radial_test.py: minimise the ratio  [F(m) - lam^-2 F(1+lam v)] / [(1-lam^2) x^2 / 2]
(must be >= 1 by pos:radial) over lam in [0.01, 0.99], x >= 1e-4, by hill climb; recheck the 20 lowest
points at 50 digits with mpmath.  Usage: python3 -I radial_ratio.py K ITERS SEED"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, mpmath as mp
from radial_test import F
def decode(th):
    e = np.exp(th[:, :3] - th[:, :3].max(1, keepdims=True)); m = 3 * e / e.sum(1, keepdims=True)
    lam = 0.01 + 0.98 / (1 + np.exp(-th[:, 3])); return m, lam
def ratio(th):
    m, lam = decode(th); v = m - 1; x = (v * v).sum(-1) / 6
    r = (F(m) - F(1 + lam[:, None] * v) / lam ** 2) / ((1 - lam ** 2) / 2 * x ** 2)
    return np.where(x > 1e-4, r, 1e3)
def exact(m, L):
    mp.mp.dps = 50
    mm = [mp.mpf(float(t)) for t in m]; s = sum(mm); mm = [3 * t / s for t in mm]; L = mp.mpf(float(L))
    def Fm(q):
        lq = [mp.log(t) for t in q]; a = sum(lq) / 3
        return 3 * sum(t * l for t, l in zip(q, lq)) / 3 - 2 * sum((t - 1) * l for t, l in zip(q, lq)) / 6 + mp.mpf(4) / 5 * sum(t * (l - a) ** 2 for t, l in zip(q, lq)) / 6
    v = [t - 1 for t in mm]; x = sum(t * t for t in v) / 6
    return (Fm(mm) - Fm([1 + L * t for t in v]) / L ** 2) / ((1 - L ** 2) / 2 * x ** 2), mm, L, x
K, iters, seed = map(int, sys.argv[1:4]); rng = np.random.default_rng(seed)
th = rng.normal(size=(K, 4)) * rng.choice([0.05, 1, 4], size=(K, 1)); f = ratio(th)
for it in range(iters):
    c = th + rng.choice([1e-3, 1e-2, 1e-1, 1.0], size=(K, 1)) * rng.normal(size=(K, 4))
    fc = ratio(c); b = fc < f; th[b] = c[b]; f[b] = fc[b]
order = np.argsort(f)[:20]
print(f'hill climb: float64 min ratio = {f[order[0]]:.9f}')
res = [exact(*[a[0] for a in decode(th[i:i + 1])]) for i in order]
r, mm, L, x = min(res, key=lambda t: t[0])
print(f'mpmath recheck of 20 lowest: min ratio = {float(r):.9f} (must be >= 1) at m={[round(float(t),6) for t in mm]} lam={float(L):.6f} x={float(x):.3e}; below 1: {sum(1 for t in res if t[0] < 1)}')
