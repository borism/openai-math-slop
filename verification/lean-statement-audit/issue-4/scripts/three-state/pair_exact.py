"""Exact rational re-evaluation of Lemma loc:pair at given points (Python Fractions; no rounding).
x = sum(v^2)/6, y = sum(v^3)/6 with v = m - 1 (02-foundations.tex fnd:fourier).
Input lines: 7 floats (current m0 m1 m2, child c0 c1 c2, a); each float is converted exactly."""
import sys, itertools
from fractions import Fraction as F
PERMS = list(itertools.permutations(range(3)))

def inv(m):
    v = [t - 1 for t in m]
    return sum(t * t for t in v) / 6, sum(t ** 3 for t in v) / 6

def pair(m, c, a):
    X, y0 = inv(m)
    e = [1 - a * (t - 1) for t in c]
    z, B0 = inv(e)
    Ex = Ey = En = F(0)
    for p in PERMS:
        W = [m[i] * e[p[i]] for i in range(3)]
        Z = sum(W) / 3
        if Z == 0: continue
        xo, yo = inv([t / Z for t in W])
        Ex += Z * xo / 6; Ey += Z * yo / 6; En += Z * xo * xo / 6
    dx = Ex - (X + z); de = Ey - (y0 + B0); dn = En - (X * X + z * z)
    SA = X * X * z; SB = X * z * z; S = SA + SB; Wp = y0 * z + X * B0
    return X * z, {
        'dn<=13/2Xz': F(13, 2) * X * z - dn,
        'de>=-79/250Xz': de + F(79, 250) * X * z,
        'de<=11Xz': 11 * X * z - de,
        'xpair': (-X * z - 2 * Wp + 2 * y0 * B0 + F(51, 20) * S) - dx,
        'ypair_lo': de - (6 * X * z - 6 * Wp + y0 * B0 - F(19, 2) * S),
        'ypair_hi': (6 * X * z - 6 * Wp + y0 * B0 + S) - de,
        'kpair': (-2 * X * z + 22 * Wp - 7 * y0 * B0 + 26 * SA + F(111, 2) * SB) - (F(5, 2) * dn - 2 * de),
    }

if __name__ == '__main__':
    bad = 0; n = 0
    for line in sys.stdin:
        vals = [F(float(t)) for t in line.split()]
        if len(vals) != 7: continue
        m = vals[0:3]; s = sum(m); m = [3 * t / s for t in m]
        c = vals[3:6]; s = sum(c); c = [3 * t / s for t in c]
        a = vals[6]
        scale, ch = pair(m, c, a); n += 1
        for k, v in ch.items():
            if v < 0:
                bad += 1; print('VIOLATION', k, float(v), float(v / scale) if scale else None, line.strip())
    print(f'points={n} exact violations={bad}')
