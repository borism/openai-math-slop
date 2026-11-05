#!/usr/bin/env python3
"""Independent numerical falsification test of Proposition cert:universal in
"The critical dimension for one-phase Bernoulli minimizers" (openai/math).

Implemented only from the paper's text (sections/certificate.tex,
certificate-proof.tex Sec. cert:decode) and Table I (appendices/tables.tex);
it does not use the paper's verification code.

Interior claim: for unit symmetric trace-free A (5x5), p in R^5, g in R with
chi = 1-|p|^2-g^2 >= 0, the quadratic form I(X,w,z,l) satisfies
I >= eps*(z^2+|l|^2).  We assemble I as a 37x37 quadratic form (X in STF^3(R^5),
dim 30; w; z; l in R^5) per base point and compute the least eigenvalue of
I - eps*(z^2+|l|^2).
Boundary claim: g=0, |p|=1, Ap=lambda p, lambda<0  =>  S >= delta*.

Usage: python3 -I bernoulli_cert_test.py <tables.tex> <n_random> <n_climb> <seed>
"""
import itertools, re, sys
import numpy as np

a = 29 / 50
Q = 250000
EPS = 438907 / 12000000
DELTA = 6984137359 / 31250000000
RANK = {'f': 0, 'U': 2, 'K': 4, 'M': 1, 'P': 1}


def parse_table_I(path):
    text = open(path, encoding='utf-8').read()
    body = text.split(r'\subsection{Table I')[1].split(r'\subsection{Table II')[0]
    rows = {k: [] for k in RANK}
    for line in body.splitlines():
        m = re.fullmatch(r'([fUKMP]) (\d+) (-?\d+)', line.strip())
        if m:
            rows[m[1]].append((m[2], int(m[3])))
    return rows


LET = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def compile_monomial(code, r):
    """Return (h, b, edges) and an einsum plan for a Table-I monomial of rank r."""
    assert len(code) % 3 == 0, code
    trip = [code[i:i + 3] for i in range(0, len(code), 3)]
    h, b, j = map(int, trip[0])
    assert j == 0, ('Table I rows must have no w,z', code)
    out = LET[:r]
    nxt = r
    terms = []          # list of (kind, power or None, subscript)
    used = []
    for t in trip[1:]:
        u, v, k = int(t[0]), int(t[1]), int(t[2])
        idx = []
        for e in (u, v):
            if e < r:
                idx.append(out[e]); used.append(e)
            elif e == 5:
                L = LET[nxt]; nxt += 1
                idx.append(L); terms.append(('p', None, L))
            else:
                raise ValueError(('unexpected endpoint in Table I', code, e))
        terms.append(('A', k, idx[0] + idx[1]))
    assert sorted(used) == list(range(r)), ('free slots must occur exactly once', code)
    return h, b, terms, out


def make_poly(rows, name):
    r = RANK[name]
    comp = [(compile_monomial(code, r), c) for code, c in rows[name]]
    paths = {}

    def evaluate(A, p, g):
        dt = np.result_type(A, p, g)
        res = np.zeros((5,) * r, dtype=dt)
        Ak = [np.eye(5, dtype=dt), A, A @ A, A @ A @ A]
        tr3 = np.trace(Ak[3])
        for idx, ((h, b, terms, out), c) in enumerate(comp):
            ops, subs = [], []
            for kind, k, s in terms:
                ops.append(Ak[k] if kind == 'A' else p); subs.append(s)
            scal = (g ** h) * (tr3 ** b) * c / Q
            if ops:
                expr = ','.join(subs) + '->' + out
                if idx not in paths:
                    paths[idx] = np.einsum_path(expr, *ops, optimize='greedy')[0]
                val = np.einsum(expr, *ops, optimize=paths[idx])
            else:
                val = np.ones((), dtype=dt)
            res = res + scal * val
        return res
    return evaluate


def stf3_basis():
    vecs = []
    for i, j, k in itertools.combinations_with_replacement(range(5), 3):
        T = np.zeros((5, 5, 5))
        for perm in set(itertools.permutations((i, j, k))):
            T[perm] = 1
        v = np.einsum('ijj->i', T)
        J = np.einsum('ij,k->ijk', np.eye(5), v) + np.einsum('ik,j->ijk', np.eye(5), v) + np.einsum('jk,i->ijk', np.eye(5), v)
        T = T - J / 7
        vecs.append(T.ravel())
    M = np.array(vecs)
    U, s, Vt = np.linalg.svd(M, full_matrices=False)
    B = Vt[s > 1e-10]
    assert B.shape[0] == 30
    return B.reshape(30, 5, 5, 5)


XB = stf3_basis()


class Point:
    """Precompute values and complex-step Jacobians of f,U,K,M,P at (A,p,g)."""
    def __init__(self, polys, A, p, g):
        self.A, self.p, self.g = A, p, g
        self.val = {k: polys[k](A, p, g).real for k in polys}
        hstep = 1e-30
        self.jac = {k: [] for k in polys}   # list over 31 coordinate directions
        dirs = []
        for i in range(5):
            for j in range(5):
                E = np.zeros((5, 5)); E[i, j] = 1
                dirs.append((E, np.zeros(5), 0.0))
        for i in range(5):
            e = np.zeros(5); e[i] = 1
            dirs.append((np.zeros((5, 5)), e, 0.0))
        dirs.append((np.zeros((5, 5)), np.zeros(5), 1.0))
        for dA, dp, dg in dirs:
            for k in polys:
                v = polys[k](A + 1j * hstep * dA, p + 1j * hstep * dp, g + 1j * hstep * dg)
                self.jac[k].append(v.imag / hstep)
        for k in polys:
            self.jac[k] = np.array(self.jac[k])          # (31, *shape)

    def D(self, k, X, w, z):
        """D_l F as array with leading slot l."""
        A, p, g = self.A, self.p, self.g
        q = np.einsum('lij,ij->l', X, A)
        out = []
        for l in range(5):
            dA = X[l] - q[l] * A
            dp = w * A[l] - g * z * np.eye(5)[l]
            dg = z * p[l]
            coef = np.concatenate([dA.ravel(), dp, [dg]])
            out.append(np.tensordot(coef, self.jac[k], axes=(0, 0)))
        return np.array(out)

    def interior(self, X, w, z, l):
        A = self.A
        f, U, K, M, P = (self.val[k] for k in 'fUKMP')
        d = np.eye(5)
        q = np.einsum('lij,ij->l', X, A)
        C = K - np.transpose(K, (1, 0, 2, 3))
        G = np.einsum('li,jk->lijk', d, U) + C
        # D_l G_lijk : derivative slot contracted with first slot of G
        DU = self.D('U', X, w, z)            # (m, j, k)
        DK = self.D('K', X, w, z)            # (m, l, i, j, k)
        DC = DK - np.transpose(DK, (0, 2, 1, 3, 4))
        DG = np.einsum('li,ljk->ijk', d, DU) + np.einsum('llijk->ijk', DC)
        DM = np.einsum('ll->', self.D('M', X, w, z))
        DP = np.einsum('ll->', self.D('P', X, w, z))
        Df = self.D('f', X, w, z)            # (l,)
        t1 = z * z * (5 * np.einsum('jk,jk->', U, A)
                      + np.einsum('lijk,lj,ik->', C, d, A) + np.einsum('lijk,lk,ij->', C, d, A) - 4 * f)
        t2 = np.einsum('ijk,ijk->', DG + (2 * a - 1) * np.einsum('l,lijk->ijk', q, G), X)
        t3 = w * (DM + (2 * a + 1) * q @ M)
        t4 = z * (DP + 2 * a * q @ P)
        t5 = f * (l @ l) - (Df + 2 * a * q * f) @ l
        return t1 + t2 + t3 + t4 + t5

    def interior_form(self):
        n = 37
        def unpack(v):
            X = np.tensordot(v[:30], XB, axes=(0, 0))
            return X, v[30], v[31], v[32:37]
        diag = np.zeros(n)
        E = np.eye(n)
        for i in range(n):
            diag[i] = self.interior(*unpack(E[i]))
        Mq = np.diag(diag)
        for i in range(n):
            for j in range(i + 1, n):
                s = self.interior(*unpack(E[i] + E[j]))
                Mq[i, j] = Mq[j, i] = (s - diag[i] - diag[j]) / 2
        # subtract eps*(z^2+|l|^2)
        for i in range(31, 37):
            Mq[i, i] -= EPS
        return Mq


def random_unit_stf(rng):
    B = rng.standard_normal((5, 5)); A = (B + B.T) / 2; A -= np.trace(A) / 5 * np.eye(5)
    return A / np.linalg.norm(A)


def boundary_value(polys, lam_vec, Ub):
    """lam_vec: eigenvalues (first one = lambda<0), Ub orthogonal; p = Ub[:,0]."""
    A = Ub @ np.diag(lam_vec) @ Ub.T
    p = Ub[:, 0]; lam = lam_vec[0]; g = 0.0
    f, U, K, M = (polys[k](A, p, g) for k in 'fUKM')
    C = K - np.transpose(K, (1, 0, 2, 3))
    S0 = lam * A - A @ A
    V = (np.einsum('i,jk->ijk', p, S0) + np.einsum('j,ki->ijk', p, S0)
         + np.einsum('k,ij->ijk', p, S0) + np.einsum('i,j,k->ijk', p, p, p))
    return (-lam * f + np.einsum('jk,jk->', U, S0 + np.outer(p, p))
            + np.einsum('lijk,l,ijk->', C, p, V) + p @ M)


def main():
    tables, nrand, nclimb, seed = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
    rng = np.random.default_rng(seed)
    rows = parse_table_I(tables)
    print('Table I row counts', {k: len(v) for k, v in rows.items()})
    polys = {k: make_poly(rows, k) for k in RANK}

    # sanity: equivariance of f under rotation
    A = random_unit_stf(rng); p = rng.standard_normal(5); p *= 0.6 / np.linalg.norm(p); g = 0.3
    O, _ = np.linalg.qr(rng.standard_normal((5, 5)))
    print('f invariance check', polys['f'](A, p, g), polys['f'](O @ A @ O.T, O @ p, g))

    def sample_base(boundary_frac=0.5):
        A = random_unit_stf(rng)
        u = rng.standard_normal(6); u /= np.linalg.norm(u)
        rad = 1.0 if rng.random() < boundary_frac else rng.random() ** 0.5
        return A, u[:5] * rad, u[5] * rad

    def score(A, p, g):
        Mq = Point(polys, A, p, g).interior_form()
        return np.linalg.eigvalsh(Mq)[0]

    worst = (np.inf, None)
    fmin = np.inf
    for t in range(nrand):
        A, p, g = sample_base()
        fmin = min(fmin, polys['f'](A, p, g) - EPS)
        s = score(A, p, g)
        if s < worst[0]:
            worst = (s, (A, p, g))
    print(f'interior: random base points {nrand}, least eigenvalue of I-eps(z^2+|l|^2): {worst[0]:.6g}; min f-eps: {fmin:.6g}')
    # hill-climb from the worst point
    s0, (A, p, g) = worst
    step = 0.05
    for it in range(nclimb):
        A2 = A + step * random_unit_stf(rng); A2 -= np.trace(A2) / 5 * np.eye(5); A2 /= np.linalg.norm(A2)
        v = np.concatenate([p, [g]]) + step * rng.standard_normal(6)
        nv = np.linalg.norm(v)
        if nv > 1: v /= nv
        s = score(A2, v[:5], v[5])
        if s < s0:
            s0, A, p, g = s, A2, v[:5], v[5]
        elif it % 20 == 19:
            step *= 0.7
    print(f'interior: after {nclimb} hill-climb steps, least eigenvalue: {s0:.6g}  at |p|^2+g^2={p@p+g*g:.6f}')

    # boundary inequality
    bmin = np.inf
    for t in range(max(200, nrand * 5)):
        lam = rng.standard_normal(5); lam -= lam.mean(); lam /= np.linalg.norm(lam)
        neg = np.where(lam < 0)[0]
        i = rng.choice(neg)
        lam = np.concatenate([[lam[i]], np.delete(lam, i)])
        O, _ = np.linalg.qr(rng.standard_normal((5, 5)))
        val = boundary_value(polys, lam, O)
        bmin = min(bmin, val)
    print(f'boundary: min S over random samples: {bmin:.6g} (claimed >= delta* = {DELTA:.6g})')


if __name__ == '__main__':
    main()
