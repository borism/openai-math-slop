"""Independent falsification test of Lemma loc:pair (three-state paper, 04-local.tex:39-50).

Written from the definitions in 02-foundations.tex (fnd:complex, fnd:edge, fnd:product) and
04-local.tex:20-38, without using the paper's certificate code.  For a current likelihood vector m
(invariants X, y0) and a child vector c (invariants w, Y), the edge message is e = 1 - a(c - 1)
(lambda = -a), with z = a^2 w and B0 = -a^3 Y.  The pair output mean of f averages the six relative
label permutations pi with tilt Z_pi = <m * pi(e)>:  E_out f = (1/6) sum_pi Z_pi f(m*pi(e)/Z_pi).
d_x, d_e, d_n are E_out of x, y, x^2 minus X+z, y0+B0, X^2+z^2.  Each inequality is checked as
slack = RHS - LHS >= 0, with the slack scaled by X*z so that near-uniform inputs are not hidden.
Usage: python3 -I pair_test.py N SEED
"""
import itertools, sys
import numpy as np

W3 = np.exp(2j * np.pi * np.arange(3) / 3)
PERMS = list(itertools.permutations(range(3)))

def inv(m):
    zeta = (m * W3).sum(-1) / 3
    return np.abs(zeta) ** 2, np.real(zeta ** 3)

def pair(m, c, a):
    X, y0 = inv(m); w, Y = inv(c)
    e = 1 - a[:, None] * (c - 1)
    z, B0 = inv(e)
    Ex = np.zeros(len(m)); Ey = np.zeros(len(m)); En = np.zeros(len(m))
    for p in PERMS:
        W = m * e[:, p]
        Z = W.mean(-1)
        out = W / np.where(Z > 0, Z, 1)[:, None]
        xo, yo = inv(out)
        Ex += Z * xo / 6; Ey += Z * yo / 6; En += Z * xo ** 2 / 6
    dx = Ex - (X + z); de = Ey - (y0 + B0); dn = En - (X ** 2 + z ** 2)
    SA = X ** 2 * z; SB = X * z ** 2; S = SA + SB; Wp = y0 * z + X * B0
    checks = {
        'dn<=13/2Xz': 13 / 2 * X * z - dn,
        'de>=-79/250Xz': de + 79 / 250 * X * z,
        'de<=11Xz': 11 * X * z - de,
        'xpair': (-X * z - 2 * Wp + 2 * y0 * B0 + 51 / 20 * S) - dx,
        'ypair_lo': de - (6 * X * z - 6 * Wp + y0 * B0 - 19 / 2 * S),
        'ypair_hi': (6 * X * z - 6 * Wp + y0 * B0 + S) - de,
        'kpair': (-2 * X * z + 22 * Wp - 7 * y0 * B0 + 26 * SA + 111 / 2 * SB) - (5 / 2 * dn - 2 * de),
    }
    # consistency checks of the edge invariants against the paper's formulas
    assert np.allclose(z, a ** 2 * w, atol=1e-14) and np.allclose(B0, -a ** 3 * Y, atol=1e-14)
    return X * z, checks

def sample(rng, n):
    kinds = []
    for alpha in (1.0, 0.2, 0.05):            # interior and boundary-heavy
        kinds.append(rng.dirichlet([alpha] * 3, n))
    for eps in (1e-1, 1e-2, 1e-3):             # near-uniform, where the pair excess is O(Xz)
        v = rng.normal(size=(n, 3)); v -= v.mean(-1, keepdims=True)
        kinds.append((1 + eps * v / np.abs(v).max(-1, keepdims=True)) / 3)
    verts = np.eye(3)[rng.integers(0, 3, n)]   # exact vertices and edges of the simplex
    kinds.append(verts)
    t = rng.random((n, 1)); i = rng.integers(0, 3, n); j = (i + 1 + rng.integers(0, 2, n)) % 3
    edge = np.zeros((n, 3)); edge[np.arange(n), i] = t[:, 0]; edge[np.arange(n), j] = 1 - t[:, 0]
    kinds.append(edge)
    return kinds

def main(N, seed):
    rng = np.random.default_rng(seed)
    worst = {}
    total = 0
    ks = sample(rng, N)
    for pm in ks:
        for pc in ks:
            for amode in ('uniform', 'half'):
                a = rng.uniform(0, 0.5, N) if amode == 'uniform' else np.full(N, 0.5)
                m = 3 * pm[rng.permutation(N)]; c = 3 * pc[rng.permutation(N)]
                scale, checks = pair(m, c, a)
                total += N
                for k, s in checks.items():
                    ok = scale > 1e-12
                    rel = np.where(ok, s / np.where(ok, scale, 1), np.inf)
                    absmin = s.min()
                    r = rel.min()
                    prev = worst.get(k, (np.inf, np.inf))
                    worst[k] = (min(prev[0], r), min(prev[1], absmin))
    print(f'samples={total}')
    for k, (r, ab) in worst.items():
        print(f'{k:16s} min slack/(Xz)={r: .6e}  min abs slack={ab: .3e}  {"OK" if ab > -1e-12 else "VIOLATION?"}')

if __name__ == '__main__':
    main(int(sys.argv[1]), int(sys.argv[2]))
