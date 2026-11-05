#!/usr/bin/env python3
"""Independent arithmetic/algebra checks for family 195,
"A Complete Local Domain Without a Small Cohen-Macaulay Module" (openai/math 4eaee87).

Checks:
 1. Chern numbers of the complete-quadrangle Kummer cover (surface.tex), recomputed
    from the stratification of B and the Hurwitz formula, specialised at n=1 (B itself).
 2. Noether integrality of chi(O_X) for primes n.
 3. The numbers used in the counterexample (n=7) and the threshold n^2 > 40.
 4. The Riemann-Roch "variance" identity (paper.tex eq:RR-variance) symbolically.
 5. The Bogomolov + Hodge-index bound of Lemma lem:factor (paper.tex l.555-603).
 6. The elementary inequality in Lemma lem:lattice (paper.tex l.516-521), randomised.
 7. The mixture formula (paper.tex eq:mixture) and the 1/4 variance bound, randomised.
Run with the Sage venv python (needs sympy): python3 -I check_195_small_cm.py
"""
import itertools
import random
from fractions import Fraction as Fr

import sympy as sp

# ---- 1-3: surface invariants -------------------------------------------------
def invariants(n):
    d = n ** 5
    KB2 = 5
    # Hurwitz: K_X = pi^*(K_B + (1-1/n) Delta), Delta ~ -2 K_B
    KX2 = d * (Fr(1) - Fr(2, n)) ** 2 * KB2
    # stratification: e(B)=7, Delta = 10 rational curves, 15 nodes (Petersen incidence)
    eB, comps, nodes = 7, 10, 15
    e_delta_open = comps * (2 - 3)            # each P^1 minus its 3 nodes
    e_complement = eB - e_delta_open - nodes   # = 2
    c2 = d * e_complement + Fr(d, n) * e_delta_open + Fr(d, n * n) * nodes
    H2 = Fr(5 * d, n * n)
    return KX2, c2, H2

for n in [1, 3, 5, 7, 11]:
    KX2, c2, H2 = invariants(n)
    chi = (KX2 + c2) / 12
    gap = KX2 - 2 * c2
    print(f"n={n:2d}: K^2={KX2}, c2={c2}, chi={chi}, K^2-2c2={gap}, H^2={H2}, 6H^2={6*H2}, obstruction violated={gap > 6*H2}")
    if n == 1:
        assert (KX2, c2) == (5, 7), "n=1 must give the degree-5 del Pezzo B"
    else:
        assert chi.denominator == 1
        assert gap == n ** 3 * (n * n - 10) and H2 == 5 * n ** 3
KX2, c2, H2 = invariants(7)
assert H2 == 1715 and KX2 - 2 * c2 == 13377 and 6 * H2 == 10290
print("threshold: K^2-2c2 > 6H^2  <=>  n^2 > 40; smallest prime is",
      min(p for p in [3, 5, 7, 11] if p * p > 40))

# Petersen-graph incidence of the 10 branch components (Figure fig:branch-incidence)
pts = [1, 2, 3, 4]
lines = [frozenset(c) for c in itertools.combinations(pts, 2)]
verts = [('e', i) for i in pts] + [('L', l) for l in lines]
def meet(u, v):
    if u[0] == 'e' and v[0] == 'L':
        return u[1] in v[1]
    if u[0] == 'L' and v[0] == 'e':
        return v[1] in u[1]
    if u[0] == 'L' and v[0] == 'L':
        return u[1] != v[1] and not (u[1] & v[1])   # opposite lines meet off exceptionals
    return False                                   # exceptional curves are disjoint
edges = [(u, v) for u, v in itertools.combinations(verts, 2) if meet(u, v)]
degs = {v: sum(1 for e in edges if v in e) for v in verts}
assert len(edges) == 15 and set(degs.values()) == {3}
print("branch incidence: 10 components, 15 nodes, every component meets 3 others: OK")

# ---- 4-5: Riemann-Roch variance and the factor bound ------------------------
t, mu, k, h, chi_, ch2, c1K, u = sp.symbols('t mu k h chi ch2 c1K u', real=True)
m, q = sp.symbols('m q', real=True)
lhs = t ** 2 / 2 + (sp.Rational(3, 2) + m) * t + 1 + sp.Rational(3, 2) * m + q
rhs = t ** 2 / 2 + (mu - k / (2 * h)) * t + chi_ / h + ch2 / (u * h) - c1K / (2 * u * h)
sol = sp.solve([sp.Eq(lhs.coeff(t, 1), rhs.coeff(t, 1)), sp.Eq(lhs.subs(t, 0), rhs.subs(t, 0))], [m, q], dict=True)[0]
expr = sp.simplify(2 * sol[q] - sol[m] ** 2)
target = sp.Rational(1, 4) + 2 * chi_ / h + (2 * ch2 / u - c1K / u) / h - (mu - k / (2 * h)) ** 2
assert sp.simplify(expr - target) == 0
assert sp.simplify(sol[m] - (mu - k / (2 * h) - sp.Rational(3, 2))) == 0
print("eq:RR-variance and the slope formula for c1(f_*G)/rk: OK (symbolic)")

# Bound: with Bogomolov 2ch2/u <= c1^2/u^2, C = c1/u - K/2, Hodge index C^2 h <= (C.H)^2,
# 2q - m^2 <= 1/4 + (2c2 - K^2)/(12h) using Noether 12 chi = K^2 + c2.
K2, c2s = sp.symbols('K2 c2', real=True)
bound = sp.Rational(1, 4) + 2 * ((K2 + c2s) / 12) / h - K2 / (4 * h)
assert sp.simplify(bound - (sp.Rational(1, 4) - (K2 - 2 * c2s) / (12 * h))) == 0
print("Lemma lem:factor final bound 1/4 - (K^2-2c2)/(12h): OK (symbolic)")

# ---- 6: lattice inequality ----------------------------------------------------
random.seed(1)
for _ in range(20000):
    N = random.randint(1, 12)
    J = random.randint(1, 8)
    n_ = [random.randint(0, N) for _ in range(J)]
    lhs_ = N * sum((2 * j + 1) * n_[j] for j in range(J)) - sum(n_) ** 2
    ident = sum(nj * (N - nj) for nj in n_) + 2 * sum(n_[j] * (N - n_[l]) for j in range(J) for l in range(j))
    assert lhs_ == ident >= 0
print("Lemma lem:lattice identity and nonnegativity: OK (20000 random cases)")

# ---- 7: mixture formula and variance <= 1/4 ------------------------------------
for _ in range(5000):
    r = random.randint(1, 6)
    ws = [Fr(random.randint(1, 9)) for _ in range(r)]
    s = sum(ws); ws = [w / s for w in ws]
    base = Fr(random.randint(-20, 20), 7)
    ms = [base + Fr(random.randint(0, 100), 100) for _ in range(r)]   # interval of length <= 1
    qs = [Fr(random.randint(-50, 50), 13) for _ in range(r)]
    vs = [2 * qi - mi ** 2 for qi, mi in zip(qs, ms)]
    mbar = sum(w * mi for w, mi in zip(ws, ms))
    vF = sum(w * 2 * qi for w, qi in zip(ws, qs)) - mbar ** 2
    assert vF == sum(w * vi for w, vi in zip(ws, vs)) + sum(w * (mi - mbar) ** 2 for w, mi in zip(ws, ms))
    assert sum(w * (mi - mbar) ** 2 for w, mi in zip(ws, ms)) <= Fr(1, 4)
print("eq:mixture and weighted variance <= 1/4 on an interval of length 1: OK (5000 random cases)")
print("ALL CHECKS PASSED")
