"""Independent falsification test of the radial inequality pos:radial (03-positive.tex:72-76, proved in
Lemma rad:lemma):  F(m) - lam^-2 F(1+lam v) >= (1-lam^2)/2 x^2  for positive m with <m>=1, 0<lam<1, where
F = 3I - 2J + (4/5)B,  I=<m log m>, J=<v log m>/2, u=log m-<log m>, B=<m u^2>/2, x=sum(v^2)/6, v=m-1.
Random sampling + hill climb in float64; the worst points are re-evaluated with mpmath at 50 digits.
Usage: python3 -I radial_test.py N K ITERS SEED   (needs mpmath for the recheck)"""
import sys
import numpy as np

def F(m):
    lm = np.log(m); v = m - 1
    I = (m * lm).mean(-1); J = (v * lm).mean(-1) / 2
    u = lm - lm.mean(-1, keepdims=True); B = (m * u * u).mean(-1) / 2
    return 3 * I - 2 * J + 0.8 * B

def slack(m, lam):
    v = m - 1; x = (v * v).sum(-1) / 6
    return F(m) - F(1 + lam[:, None] * v) / lam ** 2 - (1 - lam ** 2) / 2 * x ** 2, x

def decode(th):
    e = np.exp(th[:, :3] - th[:, :3].max(1, keepdims=True)); m = 3 * e / e.sum(1, keepdims=True)
    lam = 1 / (1 + np.exp(-th[:, 3]))
    return m, lam

def main(N, K, iters, seed):
    rng = np.random.default_rng(seed)
    worst_rel = np.inf; cand = []
    for alpha in (1.0, 0.2, 0.03):
        m = 3 * rng.dirichlet([alpha] * 3, N); m = np.maximum(m, 1e-300)
        lam = rng.uniform(0, 1, N)
        s, x = slack(m, lam)
        rel = np.where(x > 1e-6, s / np.maximum(x ** 2, 1e-300), np.inf)
        worst_rel = min(worst_rel, rel.min())
        for i in np.argsort(rel)[:20]:
            cand.append((m[i], lam[i]))
    print(f'random: {3*N} samples, float64 min slack/x^2 = {worst_rel:.6e} (float64 is unreliable for small lam)')
    th = rng.normal(size=(K, 4)) * rng.choice([0.05, 1, 4], size=(K, 1))
    def score(th):
        # float64-reliable region only: lam in [0.01, 1), x >= 1e-4; the mpmath recheck below is decisive
        m, lam = decode(th); s, x = slack(m, lam)
        return np.where((x > 1e-4) & (lam > 0.01), s / np.maximum(x ** 2, 1e-300), 1e3)
    f = score(th)
    for it in range(iters):
        c = th + rng.choice([1e-3, 1e-2, 1e-1, 1.0], size=(K, 1)) * rng.normal(size=(K, 4))
        fc = score(c); b = fc < f; th[b] = c[b]; f[b] = fc[b]
    order = np.argsort(f)[:20]
    print(f'hill climb (lam>=0.01, x>=1e-4): float64 min slack/x^2 = {f[order[0]]:.6e}')
    pts = [decode(th[i:i + 1]) for i in order] + [(c[0][None], np.array([c[1]])) for c in cand]
    import mpmath as mp
    mp.mp.dps = 50
    bad = 0
    worst = None
    for (m, lam) in pts:
        mm = [mp.mpf(float(t)) for t in m[0]]; s3 = sum(mm); mm = [3 * t / s3 for t in mm]
        L = mp.mpf(float(lam[0]))
        def Fm(q):
            lq = [mp.log(t) for t in q]; avl = sum(lq) / 3
            I = sum(t * l for t, l in zip(q, lq)) / 3; J = sum((t - 1) * l for t, l in zip(q, lq)) / 6
            B = sum(t * (l - avl) ** 2 for t, l in zip(q, lq)) / 6
            return 3 * I - 2 * J + mp.mpf(4) / 5 * B
        v = [t - 1 for t in mm]; x = sum(t * t for t in v) / 6
        s = Fm(mm) - Fm([1 + L * t for t in v]) / L ** 2 - (1 - L ** 2) / 2 * x ** 2
        if s < 0: bad += 1; print('VIOLATION', [float(t) for t in mm], float(L), float(s))
        r = s / x ** 2
        if worst is None or r < worst[0]: worst = (r, [float(t) for t in mm], float(L), float(x))
    print(f'mpmath (50 digits) recheck of {len(pts)} worst points (20 hill-climb + 60 random): violations={bad}')
    print(f'  least exact slack/x^2 = {float(worst[0]):.6e} at m={[round(t,6) for t in worst[1]]} lam={worst[2]:.6f} x={worst[3]:.3e}')

if __name__ == '__main__':
    main(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
