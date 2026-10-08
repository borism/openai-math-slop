# Check of holimart/math issue #2 (mod-8 congruence, Goldfeld 2-converse manuscript)

Issue: https://github.com/holimart/math/issues/2
Branch examined: `report/mod8-congruence-goldfeld-2converse` (fork `holimart/math`).
Claim under test: eq. `pw:split-mod8`, `a_p(E^(k)) = p+1 (mod 8)` for K-split good p, in the proof of
Lemma `pw:split-witness` (`build/sections/08-rational-converse.tex`), which is derived under the
branch assumption "equality never occurs" (`v(a(D)) >= omega(D)+1`).

## Verdict
The numerics in the issue are correct, but they do not disprove a conjecture or theorem. They show that
the "equality never occurs" branch is (in every case examined) empty, so the mod-8 derivation is vacuous
there. That is a presentation/logic weakness of one proof step, not a counterexample. The reporter says the same.

## What was verified
- Reproduction for `y^2 = x^3 - 25x`, k = -31: 207 K-split primes tested, 113 fail (matches the issue exactly;
  independent brute-force point count, `scripts/chk.py`, and PARI `ellap`, `scripts/d.py`).
- Other pairs named in the issue (congruent-number curves, `S0` = primes of 2N and of k, p <= 3000):
  (6,-47) 109/210, (7,-31) 108/207, (13,-79) 109/211, (31,-79) 107/211 fail. All have root number -1.
- Own sweep, congruent-number curves n < 60 with odd root number, 8 negative k, p <= 2000:
  188 pairs, 14241/27687 K-split primes fail (51%); no pair had zero failures. (Not the issue's 23 pairs;
  those are not listed in the issue, so the remaining 22 were not checked individually.)
- Equality witness D = 329 for (5,-31): sqrt(D) L(E^(kD),1)/L(E^(k),1) = 16.000... (37 digits);
  D = 7*47 is squarefree, K-split, square at S0 = {2,5,31}; valuation 4 = 2*omega(D).

## Equality-witness search (admissible squarefree D <= 1200, omega(D) <= 2, ratio rational with v2 = 2*omega(D))
| (n, k)    | witness D        |
|-----------|------------------|
| (5, -31)  | 329              |
| (7, -31)  | 785, 865, 1121   |
| (13, -79) | 913              |
| (31, -79) | 913              |
| (6, -47)  | 2257, 3073 (none up to 1200; found in the extended search D <= 3500, omega(D) <= 3) |

All 4 pairs the issue reports as "no witness (D <= 600)" have one once the search is extended: three by D <= 1200 and
(6,-47) at D = 2257 = 37*61 and D = 3073 = 7*439 (ratio 16, v2 = 4 = 2*omega) in the extended search to D <= 3500
(`scripts/f2.py`, `output/witness-search-n6-k-47-D3500-omega3.out`). So every pair named in the issue has an equality witness.

## Stand-in pairs (the issue's own 23 pairs are not listed, so they could not be checked individually)
10 curves y^2 = x(x-a)(x-b) (odd root number, conductor <= 3000, a,b in [-30,30]), up to 2 admissible negative k each
(k = 1 mod 8, |k| <= 200, even twist, L != 0): 20 pairs, selected by `scripts/g.py select`. These are NOT the reporter's pairs.
- Failure of the mod-8 congruence (p <= 3000): 1305 of 4157 K-split primes (23-54% per pair); every pair has failures.
- Witness search D <= 600 (`output/standin-pairs/results-D600-all20pairs.jsonl`): witnesses for 5 of 20 pairs
  (N=192,k=-71: D=505; N=480,k=-71/-191: D=409; N=576,k=-47: D=553; N=680,k=-191: D=321, 489).
- Rerun of the 15 witness-less pairs to D <= 2000 (`output/standin-pairs/results-D2000-nowitness-pairs.jsonl`, all 15 done; the last pair, N=2320 k=-111, was rerun separately with a 10 GB stack: 4 admissible D, no witness
  ): one further witness, N=2016, k=-47: D=1513. Many pairs have very few admissible D in the window
  (0-11), so "no witness" there reflects a thin search, not evidence of an empty equality branch.

## Matched-prime test of the proof's internal identity
The mod-8 step compares the congruence at p with the coefficient at D = p p' for a "matched" fresh K-split prime p'. Read
literally, it implies: if a_p != p+1 (mod 8) then v(a(pp')) = omega(pp') = 2 (equality at pp'), for every matched p'.
`scripts/m2.py` tests this (p' matched to p by p mod 8, a_p mod 8 and Legendre symbols at the odd primes of S0).
Outputs in `output/matched-prime-test/`.
- (5,-31) and (7,-31), p, p' <= 250, pp' <= 6500: 8 of 10 failing-p cases are equality cases, as the identity requires.
- The 2 exceptions (n=5,k=-31: p=19,p'=59, D=1121; n=7,k=-31: p=5,p'=101, D=505) have L(E^(kD),1)=0 exactly,
  so a(D)=0, strict, yet the congruence fails.
- Weaker matching (`weak-matching-5_-31.out`, p mod 8 and S0 classes only) gave more apparent violations; that
  matching is probably too loose and is kept for transparency.
- Caveat: the proof's "same finite data, including every support-unit test" is probably a stronger (Frobenius) condition than
  the one tested. Tiny sample; not evidence of a proof error until the exact matching condition is pinned down.

### Stricter matching (`scripts/m3.py`, outputs `m3_*.out`)
Matching p' to p on p mod 8, a_p mod 8, the 2-primary structure of E(F_p) truncated at 8, and Legendre symbols at the odd
primes of S0 (closer to "same Frobenius in Q(E[8])"): for failing p in (5,-31) and (7,-31), 8 of 11 (p,p') pairs are equality
cases (ratio 16, v2 = 4), and 3 are exact vanishing cases L(E^(kD),1)=0 (n=5: p=19,p'=59; n=7: p=5,p'=101 and p=41,p'=257).
Observed values of sqrt(D)L(E^(kD),1)/L(E^(k),1) at D=pp' are only 16 or 0 in these tests. The three vanishing cases
persist under the stricter matching, so they are not removed by it. Data the proof calls "same finite data, including every
support-unit test" is still not fully pinned down.

### Non-failing p under strict matching (`m3ok_*.out`)
For p satisfying the congruence, the proof's relation predicts v(a(pp')) >= 3. With strict matching: (5,-31) p=7 with p'=103 and
503 are both strict (a(pp')=0), consistent. The two apparent violations seen with loose matching (p=7,p'=47 and p=47,p'=103)
disappear when the 2-primary structure of E(F_p) is matched (47 and 103 have different class from 7 and 47). The other
tried primes (41, 47, 71) had no matched p' with pp' <= 9000, so this direction rests on very little data.

## Status of the 3 exceptions (Frobenius matching is not testable here)
The Chebotarev replacement of the Frobenius lift at p by a fresh prime p' (06-traces.tex, "Weight-two traces") works on the
integral lattice of the weight-two form H*theta, i.e. the finite sum of characteristic-zero Hecke systems containing the vector
and its diamond transforms. Since theta*(weight-3/2 form) is a generic weight-two form, its Hecke decomposition involves
eigensystems unrelated to E, and p' must match phi_p modulo m in the joint finite quotient of all of them. The tests above match
only E-visible data (p mod 8, a_p mod 8, 2-primary structure of E(F_p), S0 Legendre symbols), which is necessary at best and
not sufficient. Reproducing the full lattice is infeasible here (level ~ 4*N*(prod of S0 primes)^2). So the 3 exceptions
(D = 1121, 505, 10537, where a(pp')=0 but the congruence fails) do NOT show the identity is false for correctly matched p';
they are inconclusive and the "lead" is downgraded to "unresolved, probably an artefact of incomplete matching".
Integrality of H_{p} at index 1 holds in the tested instances (a(p)=0, p off the filter); integrality at all indices was not checked.

## Close reading of the lemma proof (08-rational-converse.tex, lines 470-700)
- The arithmetic from (a-1)(a-p-1)/4 even and a even to a = p+1 (mod 8) is correct.
- Since the congruence fails generically, the "equality never occurs" branch is empty whenever the derivation is valid,
  so everything after "we therefore assume" (the 1/4-divided form, the deeper bit) is vacuous. The authors' structure
  treats that branch as real.
- The 1/4-divided integrality (case J = U) also uses the mod-8 congruence, so it lives inside the same branch.
- Read tc:trace-algebra and tc:inertia-identity (06-traces.tex): the algebra t(u)t(v)=t(uv)+t(uv^-1) is the standard 2x2
  trace identity; the fresh-prime test (T_q f)[n] = f[qn] for q not dividing n is correct, and the Chebotarev replacement of
  the Frobenius lift by a fresh prime p' needs p' to share the Frobenius of phi_p in the finite quotient through which all
  forms in the orbit act mod m (so the matching condition is the Galois-image condition, not just p mod 8 and a_p mod 8).
  The inertia identity computation (both sides equal -2 z lambda mu with rho(tau)=diag(1,-1), rho(phi)=diag(lambda,mu)) checks out.
  The step that depends on the matching is "(t(phi_p) f)[p^2] = f[p^3] + (d(phi_p) f)[p]" with t(phi_p) replaced by T_p', which
  gives f[p'p^2], an expression in a(pp') times a Hecke factor in a_p. 
- Read prop:even-coefficients (05-coefficients.tex) and pw:recurrence (08-rational-converse.tex). g is a weight-3/2 form
  (Waldspurger/Shimura), with a(p^2 n) = (eta(p) a_p(E) - psi(p)(-n/p)) a(n) - p eta(p)^2 a(n/p^2) for good p. For p | n the
  Legendre symbol vanishes, so g[p^3 p'] = eta(p) a_p a(pp') and B_{p}[p'p^2] = eta(p)(a_p - 1) a(pp')/2, i.e.
  H_{p}[p'p^2] = eta(p)(a_p-1) a(pp')/4 (this is where the (a-1) factor in the proof comes from). Combined with
  H_{p}[p^3] = (a-1)(a-p-1)/4 the step amounts to: a(pp') * eta(p) = a_p - p - 1 (mod 4m), for matched p' and integral H.
  So the congruence a_p = p+1 (mod 8) is equivalent, within the proof, to v(a(pp')) >= 3, and failure to v(a(pp')) = 2.
  pw:recurrence (b_s recurrence, parity and mod 2^m statements) checks out by direct induction.
- Integrality of H_{p} needs B_{p}[1] = a(p)/2 even; in the tested instances p is off the filter (a(p)=0), so this is satisfied.
  I did not verify integrality of H at all indices.

## Caveats
- "Admissible" was implemented as: squarefree, every prime split in Q(sqrt k) and outside S0, D = 1 mod 8 and a
  quadratic residue mod each odd prime of S0. The manuscript's exact filter was not re-derived.
- "v" was taken to be the 2-adic valuation of the rational ratio.
- The first (3 GB stack) run of the n=31 search overflowed the PARI stack; it was rerun with a 10 GB stack
  (`output/witness-search-n31.out`).
- The issue text was read through a summarising fetch; the branch's `ISSUE-2026-10-08-mod8-congruence.md` was read in full.

## Reproduce
`pip install cypari2`, then:
- `python3 scripts/chk.py`  (pure Python, reproduces 207/113)
- `python3 scripts/c.py`  (D=329 check)
- `python3 scripts/f2.py 3500 w 8 2 6 -47 3`  (extended search: Dmax, w, stackGB, Dmin, n, k, max omega)
- `python3 scripts/f.py 1200 w 10`  (n=31, k=-79 witness search; third arg = PARI stack in GB)
- `python3 scripts/e.py 1200 w 3`  (witness search for the other pairs; `e.py 0 sweep 3` runs the sweep)
- `python3 scripts/g.py select` then `python3 scripts/g.py work <0-3> <stackGB> <Dmax>`  (stand-in pairs; writes pairs.json)
- `python3 scripts/m2.py <n> <k> <Pmax> <Dmax> <stackGB>`  (matched-prime test)
