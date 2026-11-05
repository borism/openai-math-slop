"""Sanity test of the scattering-matrix facts used at the start of Section boot (bootstrap.tex:30-45):
for real symmetric H (periodic 2D torus, iid uniform [-h,h] diagonal), real E, positive probe strengths eta_i
at distinct sites, Y = [sqrt(eta_i) e_i], G = (H - E - i Y Y^T)^{-1}:  S = 1 + 2i Y^T G Y is symmetric
(time reversal: H real) and unitary, and Y^T G Y is a contraction.  Also checks the Ward identity
Im G = G^* (Y Y^T) G ... in the form  G - G^* = 2i G^* Y Y^T G.  Usage: python3 -I smatrix_test.py TRIALS SEED"""
import sys
import numpy as np

def torus(L, h, rng):
    n = L * L; H = np.zeros((n, n))
    for x in range(L):
        for y in range(L):
            i = x * L + y
            for dx, dy in ((1, 0), (0, 1)):
                j = ((x + dx) % L) * L + (y + dy) % L
                H[i, j] += 1; H[j, i] += 1
    H += np.diag(rng.uniform(-h, h, n))
    return H

def main(trials, seed):
    rng = np.random.default_rng(seed); worst = np.array([0.0, 0.0, -np.inf, 0.0])
    for t in range(trials):
        L = int(rng.integers(3, 9)); h = float(rng.uniform(0.1, 6)); H = torus(L, h, rng); n = L * L
        E = float(rng.uniform(-4 - h, 4 + h)); k = int(rng.integers(1, n + 1))
        sites = rng.choice(n, k, replace=False); eta = rng.uniform(1e-3, 10, k)
        Y = np.zeros((n, k)); Y[sites, np.arange(k)] = np.sqrt(eta)
        G = np.linalg.inv(H - E * np.eye(n) - 1j * Y @ Y.T)
        K = Y.T @ G @ Y; S = np.eye(k) + 2j * K
        worst = np.maximum(worst, [np.abs(S - S.T).max(), np.abs(S.conj().T @ S - np.eye(k)).max(),
                                   np.linalg.norm(K, 2) - 1, np.abs((G - G.conj().T) - 2j * G.conj().T @ Y @ Y.T @ G).max()])
    print(f'trials={trials} max|S-S^T|={worst[0]:.2e} max|S*S-1|={worst[1]:.2e} max(||Y^T G Y||-1)={worst[2]:.2e} max Ward residual={worst[3]:.2e}')

if __name__ == '__main__':
    main(int(sys.argv[1]), int(sys.argv[2]))
