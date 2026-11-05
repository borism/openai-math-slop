# Issue 6: catalogue hygiene, the ω ≤ 9/4 trust audit, and the whole-tree scan

Follow-up to borism/openai-math-slop#6. Upstream: openai/math `4eaee8754`; earlier revisions are named where they are used.

## Task 1: the "300/719" coverage figure
Script: `scripts/coverage_candidates.py`; output: `outputs/coverage-candidates.txt`.

**Counts at fd4aeeb2e**

| Candidate numerator | Count |
|---|---|
| yaml sources | 173 |
| yaml sources + related | 203 |
| `main_results` entries | 200 |
| Comparator configs | 416 |
| Configs not named `*Support` | 409 |
| `theorem_names` | 537 |
| lean/docs files | 242 |
| Papers linked from docs | 341 |
| Docs table rows | 426 |
| CONTENTS families with a (Lean) link | 242 |
| Manuscripts in Lean families | 475 |
| Manuscripts in Lean families and linked from docs | 339 |
| Sources ∪ docs-linked papers | 342 |

None of about 30 candidates equals 300, and no sum or difference of two candidates does either.

**Denominator.** The CONTENTS headline count is 722 → 719 → 721 at adc7f1241 / fd4aeeb2e / 4eaee8754, so 719 matches fd4aeeb2e.

**Oct 7 additions** (`outputs/oct7-additions.txt`): 11 sources and 11 configs.
- 6 are real results: Hadwiger, the stable coordinate, L log L, the explicit DFT power saving, L = RL = BPL, and one-tape two-fifths space.
- 5 are support-only: small Cohen–Macaulay, honeycomb chords, integral points on character varieties, the trace cone, and uniform Cartier sections.

**Earlier wording.** At adc7f1241 the README said only "Many, but not all".

**Current state at 4eaee8754.** `README.md:21` and the history say ~42%, while `formalization.yaml` lists 176 of 721 (24%). Five of those are support-only, so at most 171 have a Comparator-checked main theorem.

## Task 2: ω(ℂ) ≤ 9/4
**(a) Statement**
- Paper Thm 1.1 (`paper.tex:45`) matches `OAI/LinearAlgebra/MatrixMultiplication/AuxiliarySeparation/Main.lean:21` and `:28`.
- The challenge's `omega` is `sInf {τ | AdmissibleExponent F τ}` (confirmed with `#print`).
- In Lean, `sInf` of an empty or unbounded-below set of reals is 0, so the bound would be trivially true in those cases. The tree rules this out:
  - `admissibleExponent_bddBelow` (`Arithmetic/LowerBound.lean:203`) proves the set is bounded below by 2, via n² ≤ cost.
  - The proof uses `csInf_le` / `le_csInf` (`RankExponent.lean:142–146`, `:169`).

**(b) Trust**
- The import closure (129 files) has zero hits for every pattern, including `set_option`.
- The patched fixed-point-theorems package (6 files) is also clean.

**(c) Structure.** The Lean modules follow the paper's argument:
- characters: `Character/Basic.lean:35–55`, `Existence.lean:25`
- separation and entropy
- concavity: `Polynomial/Inequalities.lean:54`
- tripling: `Polynomial/Inequalities.lean:75`
- growth: `Polynomial/Inequalities.lean:110`, `:117`
- t ≤ 3/4, then the exact-rank → arithmetic bridge

**(d) Loopholes: none found**
- The two cost models are identical: `ComplexArithmetic/Complexity.lean:17` and `Arithmetic/Compatibility.lean:153` translate gates one for one.
- The tree also proves ω(ℂ) < 2.267 (`ComplexBounds/SquareBound.lean:104`), outside any Comparator config.
- Sanity check (`scripts/profile_sanity.py`): on the flattening characters, every profile inequality in the paper holds for a, b, h < 300. The tripling slack is exactly 2(a−1)².
- The challenge statement elaborates in Lean 4.34.1 with Mathlib d13f23b (`outputs/mm-challenge-probe.lean.txt`).

**Build target for the axiom check** (`outputs/nine-fourths-build-target.txt`)
- **Smallest module:** `OAI.LinearAlgebra.MatrixMultiplication.AuxiliarySeparation.Main`, declaration `OAI.MatrixMultiplication.AuxiliarySeparation.omega_le_nine_quarters`.
  - Closure inside lean/OAI: 129 files, 20,694 lines.
  - Only non-Mathlib package: fixed-point-theorems @ 770940dd, plus `lean/patches/fixed-point-theorems-lean4341.patch` (6 files, 3,176 lines, Mathlib only).
- **Full Comparator solution module:** `OAI.LinearAlgebra.MatrixMultiplication.Main`, 504 files and 82,623 lines, with the same single non-Mathlib dependency.

**Recommended:** an independent Comparator replay of `MatrixMultiplication.json` with nanoda, and expert review of the concavity and tripling lemmas. 2.25 is a large jump from about 2.371.

## Task 3: whole lean/OAI scan
Output: `outputs/trust-scan-oai-tree-summary.txt`. Scope: 162,417 files, 29.86M lines.

**Hard patterns:** 0 hits for `axiom`, `sorry`, `admit`, `native_decide`, `ofReduceBool`, `implemented_by`, `extern`, `unsafe`, `trustCompiler`, `skipKernelTC` and `maxHeartbeats 0`.

**Soft patterns**

| Pattern | Count |
|---|---|
| `decide +kernel` (adds no axiom) | 1,311,448 |
| `opaque` | 1,542 |
| `elab` / `macro` / `syntax` | 34,251 |
| `set_option` | 16,480 |
| `partial def` (all metaprogramming, `Computability/TypeSystem/Logic.lean:1961–2028`) | 6 |
| `run_tac` | 7 |
| `autoImplicit true` (`Computability/Logspace/*`) | 38 |
| `Decidable` overrides (both `inferInstanceAs`) | 2 |
| `csimp` (compiler-only) | 3 |

**13 environment-manipulation sites, all read by hand.** None can add a declaration:
- `Internal/RootAlias.lean:23` only adds parser aliases.
- The `Tracial*`, `NearAllOrders` and `Cartan*` sites add names to the library-suggestion deny list.
- Two sites clear the auxiliary-lemma cache.

**Comparator challenges** (678 files): 548 `sorry`s, all of them targets, and 84 auxiliary-lemma cache resets.

## Task 4: 095 Corollary `cor:reduced`
**Hand check:** 6 steps. Q(y)ᵢᵢ = yᵢ² + yᵢ₊₁², as in the paper (`01-introduction.tex:37–42`); the challenge matches.

**Numerical check** (`outputs/reduced-numeric.txt`, 200 random points, max relative error)

| Identity | Max error |
|---|---|
| `phi = C(Q⊗Tᵀ)Cᵀ` | 3.6e-15 |
| Untransposed form, non-symmetric T (fails) | 21 |
| Schur complement | 2e-14 |
| p = det X · q | 3.6e-14 |
| q(e) = 1 | exact |
| Degree 16 | 2.9e-14 |

**Transpose detail**
- The paper's identity Φ_y(T) = C(Q⊗T)Cᵀ (`reduced-polynomial.tex:17–18`) holds for symmetric T only.
- That is the only case the paper uses, so the proof is fine.
- The sketch's Steps 1–2 carry the transpose.

**Lean sketch**
- `ReducedPolynomialSketch.lean` elaborates against the inlined challenge text (`scripts/check_sketch.sh`, about 11 s): 0 errors and 10 `sorry` warnings (`outputs/sketch-elaboration.txt`).
- A brute-force `simp` proof of Step 1 was abandoned after more than 4M heartbeats; the sketch notes a better route.
- **Missing piece:** Gårding's convexity theorem, which is neither in Mathlib nor in `OAI.Analysis.HyperbolicCones`.

## Task 5: patches (both apply to 4eaee8754)
**`docs-107.patch`**
- Links the Nine-Fourths paper, which docs/107 has never linked since the first release.
- States that 9/4 is its Thm 1.1 and that the 2.258 square bound's certificate is not a Comparator target.
- Mentions the ω < 2.267 bound.
- Credits α > 0.465 and ω(1, 0.709, 1) < 2.092 to the 2.258 paper.

**`readme-coverage.patch`:** 176/721 (24%) listed; 5 support-only, so at most 171 have a checked main theorem; 245/373 families; 345 manuscripts linked from lean/docs.

## Confidence and limits
- **High:** tasks 1, 3 and 5.
- **Task 2:** high that the statement matches and the static scan is clean.
- **Task 4:** high that the mathematics is right; no proof in the sketch is checked.
- Static analysis and elaboration only; no proofs in the OAI tree were kernel-checked during this review. See the "Lean check" section, if present, for the later axiom check.
