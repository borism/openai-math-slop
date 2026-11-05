# Issue 4: "(Lean)" links on headline claims the Lean does not formalize

This is the work for borism/openai-math-slop#4. It used the upstream openai/math checkout at commit `4eaee8754`, read-only, and ran everything on copies in scratch.

Platform: 4-vCPU Intel Xeon @ 2.80 GHz, Linux 6.18, GCC 13.3.0, Python 3.13.16, NumPy 2.5.3. SymPy 1.14.0 and mpmath came from a throwaway scratch venv. Nothing here needed Lean.

Each claim below carries one of three tags:
- **Checked**: run or recomputed; output is in `outputs/`.
- **Read**: every line read and the argument followed.
- **Skimmed**: statement, structure or proof sketch only.

A negative result means only that this method found nothing wrong. It does not mean the claim is verified.

## Summary

| Family | Headline part outside the Lean | Work done | Result |
|---|---|---|---|
| 266 MUB d=6 | ≤ 3 MUBs (the Lean proves ≤ 5, `MUBSix.lean:56-59`) | Checked: hashes, the shipped checker, a rebuild, and a bit-exact rerun of 97 of the 100 native invocations. Read: all C++ sources and the checker | Pipeline reproduces and is consistent. The reduction to the five lemmas and the soundness of the C++ are not verified |
| 261 2D Anderson | Pure-point spectral type (the Lean covers the spectrum set only) | Read: readout (`spectral.tex`). Checked: an S-matrix sanity test | Readout is sound. `boot:fractional` (about 5k lines) not reviewed |
| 367 Bernoulli | Flatness for d ≤ 6 (the Lean covers the d = 7 example only) | Checked: independent falsification test of `cert:universal`. Skimmed: flux and cutoff argument | No violation. Smallest margins 2.35 (interior) and 1.24 (boundary, vs δ* ≈ 0.2235) |
| 229 three-state | Non-reconstruction at and below KS, and the SBM corollary (the Lean covers above KS only) | Checked: `loc:pair` and `pos:radial` falsification, plus the paper's replay and UBSan run. Read: reductions, coverage, `grid.cpp` | All pass. §3 entropy argument and §5 weighted reduction not reviewed |
| 194 Lech | All characteristics and all flat maps (the Lean covers the char-p Dutta domain case only) | Read: reductions, char-p assembly, char-0 transfer | Scaffolding reads as correct. `thm:complex`, the length inputs and the mixed-characteristic section not reviewed |
| other 16 | — | Not reached | — |

---

## 1. MUB in dimension 6 (family 266)

Paper: `preprints/The-maximum-number-of-mutually-unbiased-bases-in-dimension-six-September-24-2026/`. Paths below are relative to it.

The Lean challenge `lean/ComparatorChallenges/MUBSix.lean:56-59` proves `∀ n, Attainable n → n ≤ 5`, plus two Hadamard lemmas (`lean/docs/266.md`). The headline bound of 3 rests entirely on the computer-assisted exclusion of four bases, which is not formalized.

### 1a. What the shipped checker establishes (Read)

`verification/saved-run/execution/check_records.py` is 373 lines.

What it reads: only `execution/data/`, `execution/commands.json` and `execution/results/` (`VERIFY.md:18-23`).

What it checks:
- complete parsing and EOF
- finite, in-bounds record fields (`check_records.py:66-101`)
- center-row bounds (`:226-236`)
- A progress lines
- B parent and output counts
- the fine-to-batch partition
- that C failures form an ordered subsequence (`:213-219`)
- the fallback input order
- final modulo-4 coverage

What it does not do:
- It runs no program.
- It evaluates none of the geometric or arithmetic predicates: seed cover, A cover, refinement cover, exclusion certificate.
- Cover numbers such as `checked_pairs` are parsed from text (`:237-246`), not recomputed.

It describes itself as "PASS within numerical consistency scope … no source, binary, or original execution provenance verification" (`:340,353`, and `VERIFY.md:29-31`).

The `results/` files are curated, not raw stdout:
- They drop fields such as `coverFailures`, `candidates` and `visit/near/cheap/lp`.
- They reformat `xs22829 build15.27` as `xs 22829`.
- They add a supervisor marker, `completed_write`, that the programs never print (`:246`). See `outputs/mub-rerun-lane2.txt`.

### 1b. Hashes (Checked)

Script: `scripts/mub/mub_hash_check.py`. Output: `outputs/mub-hash-check.txt`.
- All 7 mathematical sources match `verification/code/extraction.json`, in both byte count and SHA-256.
- All 8 principal data files match Table `execute:hashes` (`build/sections/execution.tex:358-376`). The table was parsed from the LaTeX, not retyped.
- `abi-fp-probe.cpp` is shipped and used by `build.sh`, but it is not in the manifest.

Both manifests ship in the same release as the data, so matching proves consistency, not provenance. `README.md:12` says only that the manifest hashes the sources "as currently present". §1e is what links the current sources to the data.

### 1c. Checker run (Checked)

`python3 -I check_records.py` was run on a copy. It exited 0 with "PASS within numerical consistency scope" (`outputs/mub-checker-output.json`).

Its counts all match Table `execute:counts`:
- 249,878 centers and 151,744,086 checked pairs
- coarse records 764 / 774 / 757 / 788
- 600 mid records, and 22,379 fine records in 88 batches
- initial C: 163 bad, all in the `cap` category
- 15 fallback inputs and 1,127 fallback records
- final C: 282 / 282 / 282 / 281 done, 0 bad
- 100 child invocations

### 1d. Gap between the checker and Theorem `execute:finite-theorem` (Read)

The theorem is at `execution.tex:242-281`. Its hypotheses are:
1. the seven sources
2. the arithmetic conditions of Appendix `sec:rounding`
3. invocations meeting §`execute:control` "with the record provenance and batch checks stated there"

The proof chains five lemmas:
- `seed:cover` (`seed.tex:450`)
- `phase:A-cover` (`phase-cover.tex:986`)
- `refine:cover-preservation` (`refinement.tex:502`)
- `refine:batch-cover` (`refinement.tex:587`)
- `exclude:local-certificate` (`exclusion.tex:640`)

The proof itself says that "counts and hashes establish the identity and completeness of the finite chain, not those inequalities in isolation" (`execution.tex:278-280`).

The shipped checker covers only the count, order and partition part of hypothesis 3. The provenance part relies on artifacts the paper cites but the repository lacks:
- `verification/code/proof_run.py` (`execution.tex:119`)
- `build/build-manifest.json` (`:87`)
- `verification/computation/README.md` (`:381`)
- the `full-run-01/` archive with `pipeline/status.json` and `run.json` (`:386-389`)
- `verification/REPRODUCE.md` (`:390`)

`VERIFY.md:5-6` confirms that no compiled programs, raw logs or supervision code ship. Beyond the checker:
- The claim that the C++ correctly implements the five lemmas with sound one-sided rounding is left to the reader.
- The arithmetic model is assumed (`execution.tex:84-86`). The ABI probe only samples it (`VERIFY.md:53-54`).

### 1e. Rebuild and bit-exact rerun (Checked)

**Build.** I ran `compiled-build/build.sh` with GCC 13.3.0 and `-O3 -march=native -ffp-contract=off`. Both ABI/FP probes passed (`outputs/mub-build-log.txt`).

**Code generation.** VERIFY.md (`:56-60`) asks for a check of how `pow` is compiled. In the fresh `covrun`, the two `pow(...,2)` calls in `coverSeeds::run` (`covout.cpp:100-101`) compile to separately rounded binary64 operations:

| Step | Instruction | Address |
|---|---|---|
| scale | `vmulsd` | 6065 |
| square | `vmulsd` | 6069 |
| subtract | `vsubsd` | 606d |
| square root | `vsqrtsd` | 608c |
| add | `vaddsd` | 609d |
| second square | `vmulsd` | 60bb |

There is no dynamic `pow` symbol (`outputs/mub-covrun-pow-lowering.txt`). The paper's addresses (6035…608b, `execution.tex:94-97`) refer to its own binary, which is not shipped, so different addresses are expected.

**Rerun method.** Each stage was run from shipped sources on shipped inputs, under `LC_ALL=C`. Outputs were compared with `cmp` against the shipped data. Stdout was compared with the curated result after removing timing fields only, or as an in-order token subset (`scripts/mub/curated_subset.py`). The scripts are `scripts/mub/run_stage.sh`, `lanes.sh` and `lanes_resume.sh`; the resume script restarted after a container restart.

| Stage | Invocations | Byte comparison | Stdout | Wall time (this machine) |
|---|---|---|---|---|
| cover `covrun` | 1 | `centers.txt` IDENTICAL | N112 line matches | 670 s |
| A shard 0 | 1 of 4 | `coarse0.bin` and `bad0.txt` IDENTICAL | 63/63 lines subset-match | 2433 s |
| B mid (.07/.013) | 1 | `mid.bin` and `midbad.bin` IDENTICAL | MATCH | 2470 s (about 700 s of it SIGSTOP-paused) |
| B fine (.016/.005) | 1 | `fine.bin`, `finebad.bin` and `fdone.txt` IDENTICAL; 0 of 88 batch files differ | MATCH | 693 s |
| initial C | 88 | 88/88 `bad*.bin` IDENTICAL | 88/88 MATCH | 18–81 s each |
| B fallback (.011/.0038) | 1 | `fb1.bin` and `fb1bad.bin` IDENTICAL | MATCH | 14 s |
| final C | 4 | `fb1cbad0-3.bin` IDENTICAL | 4/4 MATCH | about 47 s each |

Initial C exited 0 for 73 batches and 1 for 15. The 15 are batches 3–8, 10, 52, 53, 55, 56, 78–80 and 84, exactly the 15 fallback inputs. This matches `execution.tex` §`execute:observed`.

Not rerun, for time: A shards 1–3. Their shipped outputs feed B mid, which reproduces, but that does not validate them.

Outputs: `outputs/mub-rerun-initialC-lane1.txt`, `outputs/mub-rerun-lane2.txt`, `outputs/mub-rerun-fallback-finalC.txt`.

**What this shows.**
- On an independent x86-64 machine, the shipped sources reproduce the shipped records bit for bit, for 97 of the 100 invocations.
- So for those stages, the October 4 data are exactly what the current sources compute. The "as currently present" caveat in `README.md:12` does not bite, and the curated results agree with real stdout.

**What this does not show.**
- That the C++ implements the paper's lemmas.
- That the rounding analysis is sound.

**Code reading.** I read all seven sources, `abi-fp-probe.cpp` and `build.sh`, but did not re-derive the interval and rounding proofs. In `stageC.cpp:526-565`, any record where `negative()` is false goes to the bad file:
- graph search gave up at the 5,000,000-step cap
- bin overflow
- cluster failure
- graph positive

The program then exits 1. A record is excluded only when every check passes, so failure modes are conservative. All 163 initial failures are `cap` (step limit). I found no defect, but this is a statement about code reading only.

**Verdict for 266.** The finite computation is reproducible and internally consistent. The mathematical reduction, and the claim that the code soundly implements it, are not verified by anything in the repository. Since the Lean bound is 5, not 3, "(Lean: partial)" is accurate.

---

## 2. Referee-style review of the unformalized headline directions

### 2.1 Family 261: 2D Anderson, pure point at every positive disorder

Paper: `preprints/Pure-Point-Spectrum-for-the-Two-Dimensional-Anderson-Model-at-Every-Positive-Disorder-September-23-2026/build/sections/`, about 5,970 lines.

The Lean, `PlanarAndersonSpectrum.lean:26-28`, proves almost-sure self-adjointness and `spectrum ℂ H = [-4-h, 4+h]`. That is a standard result. The pure-point type, which is Simon 2000 Problem 2, is not formalized.

**Readout (Read, `spectral.tex:12-177`).**
- Theorem `boot:fractional` (`bootstrap.tex:11-26`) gives E|(H_N−E)^{-1}_{xy}|^{s/2} ≤ A e^{−a·dist}, for 0 < s < 1/16, at fixed real E, uniformly in torus size.
- `spec:column` uses Fatou, a diagonal subsequence and weighted ℓ^q ⊂ ℓ² to get an ℓ² solution of (H−E)u = δ_x. Hence Γ_x(E) < ∞.
- Fubini, plus rank-one spectral averaging (`spec:averaging`, Simon–Wolff), gives a pure-point site measure for each x.
- Density of the span of the δ_x then gives pure-point spectrum.

I found no gap. Measurability is handled explicitly (`spectral.tex:146-152,166-170`), and cyclicity of δ_x is not assumed.

**Load-bearing and not verified: `boot:fractional`.** Its proof runs through hierarchy → impedance → screening → transmission → resonant → matrix → vanishing, about 5,000 lines. The core is Prop `van:zero` (`vanishing.tex:9-30`), a proof by contradiction that the limiting affine energy is d = 0.
- The only explicitly two-dimensional mechanism I found is the logarithmic voltage profile in a square annulus (`vanishing.tex:19-21`). That fits 2D log-capacity.
- `vanishing.tex:29` uses "dimension-independent moment bounds". A referee should check that no step would also go through in d = 3.

**Numerical check (Checked, low evidential value).** `scripts/anderson/smatrix_test.py` ran 300 random periodic tori. It confirms the set-up of `bootstrap.tex:30-45`:
- S = 1 + 2iYᵀGY is symmetric (time reversal) and unitary to 4e-15.
- ‖YᵀGY‖ ≤ 1.
- The Ward identity holds to 1e-13.

**Assessment.** Not confirmed. All the new content sits inside `boot:fractional`, which needs specialist review, starting with `van:zero` and `screen:limit`.

### 2.2 Family 367: Bernoulli flatness for d ≤ 6

Paper: `preprints/The-critical-dimension-for-one-phase-Bernoulli-minimizers-September-24-2026/`.

The Lean, `BernoulliNonflatInSeven.lean:78-80`, states only the existence of a nonflat one-homogeneous minimizer in d = 7. That is the De Silva–Jerison direction.

The new content is Theorem `cut:exclusion` (`cutoffs.tex:315-318`): d* ≠ 5, 6. It comes from three ingredients:
- a flux identity, `flux:interior-comparison` and `flux:boundary-comparison` (`flux.tex:128-290`, Skimmed)
- cutoff estimates (Skimmed)
- the algebraic certificate Prop `cert:universal` (`certificate.tex:33-71`), built from Table I (`appendices/tables.tex:58-296`), on STF tensors in R⁵

In this argument, `flux.tex:178-188` reduces the pointwise divergence inequality to `cert:interior` by exact completion of the square. I followed that step.

**Independent falsification test of `cert:universal` (Checked).**

`scripts/bernoulli/bernoulli_cert_test.py` was written from the text and the decoding (`certificate-proof.tex`). It does not use the paper's verification code. It:
- parses Table I: 34 f, 57 U, 34 K, 74 M and 32 P rows
- builds the tensor polynomials
- differentiates along the paper's D_l by complex step
- assembles 𝓘 as a 37×37 quadratic form in (X ∈ STF³, w, z, ℓ)
- takes least eigenvalues at random base points (half on χ = 0), then hill-climbs, then samples the boundary inequality

The run was `400 300 7` (`outputs/bernoulli-cert-run1.log`).

| Check | Result |
|---|---|
| f orthogonal invariance | equal to 1e-13 |
| Least eigenvalue of 𝓘 − ε*(z²+\|ℓ\|²), 400 random points | 8.00 |
| … after 300 hill-climb steps | 2.35, at \|p\|²+g² = 0.767 |
| min f − ε* | 487 |
| Boundary min 𝓢, 2,000 samples | 1.245, vs the claimed δ* = 0.2235 |

No violation was found, and the margins are not thin.

Caveats:
- This is sampling, not proof.
- The hill climb was short.
- A decoding error on my side would more likely produce spurious violations than spurious agreement. The test does exercise my reading of the decoding.

I did not read or run the paper's own `verification/checks/` and `verification/independent-certificate/` (about 100 KB of Python). Their README says they "do not certify equivalence between mathematical formulas and code, or the analytic proof".

Not reviewed: the geometric and analytic reduction to `cert:universal` (`reductions.tex`, `geometry.tex`, `cutoffs.tex`).

### 2.3 Family 229: three-state non-reconstruction at and below Kesten–Stigum

Paper: `preprints/The-exact-reconstruction-threshold-for-the-three-state-symmetric-channel-September-25-2026/`.

The Lean, `ThreeStateSupercritical.lean:98-103`, covers only reconstruction for bλ² > 1 and dλ² > 1.

**Reduction (Read: `02-foundations.tex:448-525` and `07-conclusion.tex`).** Prop `fnd:degradation` reduces everything to equality cases in three ways:
- channel scaling via a group-increment coupling
- truncating regular offspring
- Poisson thinning

I checked the coupling algebra. A conjugation-invariant law on {1, ω, ω²} with mass p at 1 has mean (3p−1)/2, and means multiply under independent products. The reduction does not condition on survival.

**Coverage (Read, Table `tab:coverage`).** The equality cases are covered as follows:

| Case | Covered by |
|---|---|
| Positive λ | Analytic, §3 |
| Regular b ≥ 5 (a = b^{-1/2} ≤ 0.4472 < 0.448) | `interval.cpp` |
| Poisson a ≤ 0.477 (d ≥ (1000/477)² ≈ 4.3950) | `interval.cpp` |
| Regular b = 4, and Poisson 4 ≤ d ≤ 881/200 = 4.405 | grid |
| Negative λ with d < 4 | Follows from coloring at d = 4 by degradation |

There are no gaps. The code matches: `grid.cpp` uses ids 0…26 with d ∈ [4 + 0.015·id, 4 + 0.015·(id+1)], plus id −1 for b = 4. `interval.cpp` uses the a-ranges [0, .19], [.19, .448] and [.448, .477].

**`grid.cpp` (Read, 200 lines).** This is a sound Blackwell upper experiment:
- It uses A/AD ≥ d_min^{-1/2} together with the Poisson mean d_max.
- It lower-bounds e^{−d} by an alternating series that ends on a negative term.
- Rounded-down mass is completed by the perfectly informative state.
- Rounding to grid points is mean-preserving (both the miss = 1 and miss = 2 cases).
- The int128 accumulators stay below about 3e34.

The stopping test μ < 1/20 combines with `loc:gap` (`04-local.tex:15-19`).

**`loc:pair`, seven inequalities (`04-local.tex:39-50`), independent check (Checked).**
- `scripts/three-state/pair_test.py` implements d_x, d_e and d_n from the definitions: a six-permutation tilt average with edge e = 1 − a(c − 1). It does not use the paper's `pair.py`.
- 256,000 structured samples covered the interior, the boundary, near-uniform points, vertices and edges, with random a and with a = 1/2.
- A 400-start hill climb on slack/(Xz) found no violation.
- The 175 most adversarial points were rechecked in exact rationals (`pair_exact.py`): 0 violations.
- Some bounds are nearly tight at boundary configurations. For example, d_n ≤ (13/2)Xz is nearly tight at current (3/2, 3/2, 0) with child (0, 0, 3).

**`pos:radial`, F(m) − λ^{-2}F(1+λv) ≥ (1−λ²)x²/2 (`03-positive.tex:72-76`) (Checked).**
- `scripts/three-state/radial_test.py` and `radial_ratio.py` ran 600,000 random samples plus a hill climb.
- Float64 shows apparent violations of order −1e-4 relative. Rechecking at 50 digits shows they are cancellation artifacts at small λ.
- Exact recheck of the 100 worst points: 0 violations.
- The minimum exact ratio is 1.00006, at λ → 0 and m → 1. So the constant (1−λ²)/2 is sharp in that limit.

**Paper's own replay (Checked).**
- `verification/reproduce.py` (read in full, together with `pair.py`, `interval.cpp` and `grid.cpp`) reports PASS: 37/37 subprocess records, and source SHA-256s match.
- The UBSan build of `interval.cpp` runs clean on cases 0/1/2, with visited-box totals 414080, 756096 and 1004426 as stated.
- Output: `outputs/three-state-paper-replay.txt`.

**Not reviewed:**
- the §3 entropy and moment argument, beyond `pos:radial`
- how `interval.cpp`'s four coefficient rows encode `wei:exclusion` (§5)
- the SBM transfer (Skimmed; cites Mossel–Sly–Sohn Thm 2.1 and Abbe–Sandon)

**Assessment.** Everything I could test independently passes. The two analytic exclusions still need review.

### 2.4 Family 194: Lech's conjecture

Paper: `preprints/Lechs-multiplicity-conjecture-September-23-2026/build/`.

The Lean, `DuttaDomain.lean` (`DuttaDomainClaim`), covers e(D) ≤ χ_∞(F) for short complexes over complete local domains of characteristic p. That is Corollary `cor:dutta-domain` (`charp.tex:193`). The headline covers every characteristic and every flat local map.

**Reductions (Read: `reductions.tex:1-367`).**
- `lem:reduction` is standard, as in Ma Lemma 2.2. It proceeds by completion, then localizing at a minimal Q over 𝔪S with Nagata's e(S_Q) ≤ e(S), then a prime filtration with additivity to reach a domain source, then residue-field extension. In mixed characteristic it uses a DVR tower V[X]/(f), which works even when the residue extension is inseparable.
- `prop:setup` builds T = R ⊗_A U by Cohen factorization (AFH).
- e(T) = e(R) follows by flatness over R[[W]].
- pd_T S ≤ b by the fiber argument; J is perfect of grade b.
- Equidimensionality, and the complete-intersection (or regular) property of T_Q over the generic point of R, follow.

All of these read as correct.

**Char-p case (Read: `charp.tex:1-138`).** It combines:
- `thm:complex` applied per component with s = q − c, giving e_HK(HD, D) ≥ e(D)
- HK associativity (Huneke Thm 3.14)
- Ma's HK identity with complete-intersection T_Q

That yields e(S) = e_HK(H, T) ≥ e(T) = e(R). The assembly is correct given those inputs.

**Char-0 case (Read: `charzero.tex`, all 419 lines).** This follows Ma §5. I checked:
- e(R) ≥ r, from the vanishing (u−r+1)-minors together with the retained reduction 𝔞^{j+1} ⊆ (t)𝔞^j
- locality and residue field K
- e(S) ≤ e(S₀). Monic initial relations reduced mod (t) keep their leading monomial, so the new initial ideal contains J.
- the Artin approximation, étale descent and spreading out to a finite residue field

All correct.

**Not reviewed:**
- `thm:complex`, the new uniform estimate (`complex.tex`, 643 lines)
- `thm:length-inputs` (`lengths.tex`)
- the mixed-characteristic section (`mixed.tex`)

**Assessment.** The scaffolding reads as correct. The new mathematics, `thm:complex` and the mixed-characteristic length inputs, needs specialist review.

### Not reached

I did no referee work on families 009, 033, 126, 152, 159, 191, 206, 222, 230, 260, 269, 272, 280, 281, 323 and 371.

---

## 3. CONTENTS.md patch

`contents-lean-links.patch` is a unified diff against upstream `CONTENTS.md` at `4eaee8754`, generated by `scripts/make_patch.sh`.
- It changes exactly 21 lines, `([Lean](lean/docs/NNN.md))` → `([Lean: partial](lean/docs/NNN.md))`, for 009, 033, 126, 152, 159, 191, 194, 206, 222, 229, 230, 260, 261, 266, 269, 272, 280, 281, 323, 367 and 371.
- Each link occurs exactly once; the script asserts this.
- Reverting the label gives back the original file byte for byte.
- `patch --dry-run -p1` applies cleanly to the fork's `CONTENTS.md`, with a −9 line offset for hunks 3–21.

## 4. Files

- `scripts/`
  - `make_patch.sh`
  - `mub/`: `mub_hash_check.py`, `run_stage.sh`, `lanes.sh`, `lanes_resume.sh`, `curated_subset.py`
  - `bernoulli/bernoulli_cert_test.py`
  - `three-state/`: `pair_test.py`, `pair_climb.py`, `pair_dump.py`, `pair_exact.py`, `radial_test.py`, `radial_ratio.py`
  - `anderson/smatrix_test.py`
- `outputs/`
  - `mub-hash-check.txt`
  - `mub-checker-output.json`
  - `mub-build-log.txt`
  - `mub-covrun-pow-lowering.txt`
  - `mub-rerun-initialC-lane1.txt`
  - `mub-rerun-lane2.txt`
  - `mub-rerun-fallback-finalC.txt`
  - `bernoulli-cert-run1.log`
  - `three-state-pair-random.txt`
  - `three-state-pair-climb-points.txt`
  - `three-state-pair-exact.txt`
  - `three-state-radial.txt`
  - `three-state-paper-replay.txt`
  - `anderson-smatrix-test.txt`
- `contents-lean-links.patch`
- `COMMENT.md`

Two process notes:
- The Bernoulli test and B mid were each briefly paused with SIGSTOP, to keep to two CPU-heavy processes at a time.
- A container restart interrupted the lanes after initial-C batch 56. They were resumed with `lanes_resume.sh`, and batch 57 and covrun were restarted from scratch.
