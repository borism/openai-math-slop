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
| (6, -47)  | none up to 1200  |

So 3 of the 4 pairs the issue reports as "no witness (D <= 600)" have one once the search is extended.
Only (6,-47) remains without a witness; the search is finite and does not exclude a larger D.

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
- `python3 scripts/f.py 1200 w 10`  (n=31, k=-79 witness search; third arg = PARI stack in GB)
- `python3 scripts/e.py 1200 w 3`  (witness search for the other pairs; `e.py 0 sweep 3` runs the sweep)
