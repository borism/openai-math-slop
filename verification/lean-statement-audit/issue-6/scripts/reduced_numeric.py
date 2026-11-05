#!/usr/bin/env python3
"""Numerical sanity check of the 095 reduced-polynomial identities, using the
challenge's exact definitions (lean/ComparatorChallenges/HyperbolicCones.lean):
qMatrix, phi, matrixValue = det(det X * Z - phi_y(adj X)).

Checks, at random points (float64):
  (1) phi_y(T) = C (Q(y) ⊗ T^T) C^T for arbitrary T  (and != with T for non-symmetric T)
  (2) Schur: det [[I3⊗X, C^T],[C(Q⊗I4), Z]] = det(X)^3 det(Z - phi_y(X^{-1})) for symmetric X
  (3) p = det(X) * q at symmetric (X, Z, y)
  (4) q(e) = 1 at e = (I, I, 0);  homogeneity degree of q is 16 (scaling test)
"""
import numpy as np
rng = np.random.default_rng(0)

def Q(y):
    M = -np.outer(y, y)
    for i in range(3):
        M[i, i] = y[i] ** 2 + y[(i + 1) % 3] ** 2
    return M

def phi(y, X):
    q = Q(y); P = np.zeros((4, 4))
    P[0, 0] = np.trace(q @ X[1:, 1:])
    for j in range(3):
        P[0, j + 1] = -sum(X[0, k + 1] * q[k, j] for k in range(3))
    for i in range(3):
        P[i + 1, 0] = -sum(q[i, k] * X[k + 1, 0] for k in range(3))
        for j in range(3):
            P[i + 1, j + 1] = X[0, 0] * q[i, j]
    return P

def K(i):
    M = np.zeros((4, 4)); M[0, i + 1] = 1; M[i + 1, 0] = -1; return M

C = np.hstack([K(0), K(1), K(2)])          # 4 x 12, column index (i, c) -> 4*i + c

def adj(X):
    return np.linalg.det(X) * np.linalg.inv(X)

def p(X, Z, y):
    return np.linalg.det(np.linalg.det(X) * Z - phi(y, adj(X)))

def q(X, Z, y):
    B = np.block([[np.kron(np.eye(3), X), C.T], [C @ np.kron(Q(y), np.eye(4)), Z]])
    return np.linalg.det(B)

def sym(n):
    A = rng.standard_normal((n, n)); return A + A.T

err = {k: 0.0 for k in ['phi=C(Q⊗Tᵀ)Cᵀ', 'phi=C(Q⊗T)Cᵀ (nonsym T)', 'schur', 'p=detX*q', 'q(e)-1', 'deg16']}
for _ in range(200):
    y = rng.standard_normal(3); T = rng.standard_normal((4, 4))
    err['phi=C(Q⊗Tᵀ)Cᵀ'] = max(err['phi=C(Q⊗Tᵀ)Cᵀ'], np.abs(phi(y, T) - C @ np.kron(Q(y), T.T) @ C.T).max())
    err['phi=C(Q⊗T)Cᵀ (nonsym T)'] = max(err['phi=C(Q⊗T)Cᵀ (nonsym T)'], np.abs(phi(y, T) - C @ np.kron(Q(y), T) @ C.T).max())
    X, Z = sym(4), sym(4)
    r = q(X, Z, y); s = np.linalg.det(X) ** 3 * np.linalg.det(Z - phi(y, np.linalg.inv(X)))
    err['schur'] = max(err['schur'], abs(r - s) / max(1, abs(r)))
    a, b = p(X, Z, y), np.linalg.det(X) * q(X, Z, y)
    err['p=detX*q'] = max(err['p=detX*q'], abs(a - b) / max(1, abs(a)))
    lam = 1.7
    err['deg16'] = max(err['deg16'], abs(q(lam * X, lam * Z, lam * y) - lam ** 16 * q(X, Z, y)) / max(1, abs(q(X, Z, y)) * lam ** 16))
err['q(e)-1'] = abs(q(np.eye(4), np.eye(4), np.zeros(3)) - 1)
for k, v in err.items():
    print(f'{k:28s} max rel. error {v:.2e}')
