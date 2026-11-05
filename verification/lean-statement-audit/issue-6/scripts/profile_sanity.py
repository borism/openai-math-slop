#!/usr/bin/env python3
"""Sanity check of the Nine-Fourths paper's profile inequalities on known
tensor characters: the three flattening ranks (Strassen's gauge points).

For the X-flattening character: lambda(B_X(m)) = 1, lambda(B_Y(m)) = lambda(B_Z(m)) = m,
so (pX, pY, pZ) = (0, 1, 1) and t = 2/3; on C(a,b) the three flattening ranks are
a, b, a+b-1. The six leg permutations give each value twice, so
P(a,b) = (a^2 b^2 (a+b-1)^2)^(1/(6t)) = sqrt(a b (a+b-1)).
The same profile results from the Y- and Z-flattenings.

Checks (paper eq. profile-basic, Lemma concavity, Lemma tripling, Lemma growth):
  P(1,b) = b,  P(a,b) <= (a+b-1)^(1/t),  2P(a,b) >= P(a,b+1)+P(a,b-1),
  P(a,3h+a-1) >= 3P(a,h),  P(a,a) >= a^(4/3).
This only shows the inequalities are not contradicted by these characters; it
says nothing about the extremal character that determines omega.
"""
from math import sqrt

t = 2 / 3


def P(a, b):
    return sqrt(a * b * (a + b - 1))


bad = []
N = 300
for a in range(1, N):
    if abs(P(1, a) - a) > 1e-9:
        bad.append(('P(1,b)=b', a))
    if P(a, a) < a ** (4 / 3) - 1e-9:
        bad.append(('growth', a))
    for b in range(1, N):
        if P(a, b) > (a + b - 1) ** (1 / t) + 1e-9:
            bad.append(('upper', a, b))
        if b >= 2 and 2 * P(a, b) < P(a, b + 1) + P(a, b - 1) - 1e-9:
            bad.append(('concavity', a, b))
    for h in range(1, N):
        if P(a, 3 * h + a - 1) < 3 * P(a, h) - 1e-9:
            bad.append(('tripling', a, h))
print(f'checked 1 <= a,b,h < {N} for the flattening-rank characters (t = 2/3)')
print('violations:', bad[:10] if bad else 'none')
print('tripling slack identity: (3h+a-1)(3h+2a-2) - 9h(a+h-1) = 2(a-1)^2 >= 0 (exact)')
