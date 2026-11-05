# Lean statement vs. paper audit of the openai/math formalizations

Snapshot: upstream `openai/math` main at `4eaee8754` (Oct 29, 2026). This
fork's `main` is still at `fd4aeeb2e` (Oct 7). Upstream has since added two
manuscripts, a CM Hodge formalization and the MUB run records, and changed
some Comparator configurations.

## What was checked

1. **Public verification work** on the release, summarized below.
2. **Every Lean-formalized family.** All 245 `lean/docs/NNN.md` scope notes,
   the 418 Comparator configurations and the papers they link. For each
   family, the Comparator target theorem(s) were read against the paper's
   abstract, its first theorem environment and the scope note
   (`output/dossiers-all-families.md`).
3. **The catalogue** (`lean/formalization.yaml`, `CONTENTS.md`, the
   Comparator README) against the scope notes.
4. **Hostile checks of selected definitions.** These were junk values
   (`sInf` of an empty set of naturals is 0, as in the Navier–Stokes critique
   below), the machine and complexity models behind headline complexity
   claims, and how large a statement's trusted definitional base is.

Not done: building or replaying any Lean. The container cannot download the
Lean toolchain (GitHub release assets return 403, and `releases.lean-lang.org`
and the Mathlib cache hosts are unreachable). Definitions were spot-checked,
not audited exhaustively.

## Public verification work found

| Who | What | Relevant result |
|---|---|---|
| OpenAI (history.md) | internal audit | 3 withdrawals (sign error, Weil classes on abelian eightfolds, plus 2 dependents); 14 revisions |
| [Lattice24 / JJardine919](https://github.com/JJardine919/openai-math-audit) | LLM referee review of the 547 manuscripts **not** in `formalization.yaml` | 2 gaps: FK interfaces (critical; 1 dependent), MUB dim 6 (verifiability, addressed Oct 26). "No gap" for the rest |
| [grwtsk/openai-math](https://github.com/grwtsk/openai-math/issues/2) | trust-surface audit plan and static scans | Kaplansky target `KaplanskyDirectFiniteness` lacks finite presentation and odd torsion (the second target has both); quasi-RH Lean statement totalizes `riemannZeta 1`; Hecke junk value at s=0; `run_tac` in solutions; nanoda enabled in 2 of 418 configs |
| [yuyauchuncn](https://github.com/yuyauchuncn-dot/openai-math-audit) | structural audit (citation graph, revision diffs) | `review: unchecked`; three incompatible coverage denominators; 13 substantive revisions |
| [sunnyspot114514](https://github.com/sunnyspot114514/openai-math-audit) | Comparator replay | symmetric Mahler and polar Gromov width: exit 0, standard axioms |
| [queelius](https://github.com/queelius/openai-math-counterexamples) | recompute finite counterexamples | 63 families: 8 hold, 0 fail, 9 not explicit, 46 not finite |
| holimart/math#2 and our issue #1 | numerical check of the mod-8 step in the 2-converse paper | numerics correct but conditional on an apparently empty branch |
| Bastounis–Circelli–Hansen, arXiv 2610.08144 | Lean vs. natural-language proof (OpenAI's separate Navier–Stokes blow-up release) | Lean bound (10.19) mistranslated, including an `sInf` default-0 issue. That formalization is not in this repo |

## Results

Per-family table: `output/per-family-verdicts.tsv`. Reading notes:
`output/reading-notes.md`.

| Category | Families | Meaning |
|---|---|---|
| consistent (pass 1) | 210 | Lean target matches the paper's headline theorem, or the difference is a stated side result |
| **A** support-only, catalogued | 027, 066, 195, 237 (chords paper), 301 | `formalization.yaml` lists the paper as having a formalized main result, but the Lean proves only a supporting lemma |
| **B** weaker or partial, catalogued | 277, 212, 312, 290; 378 (minor) | listed in `formalization.yaml`, but the Lean statement is weaker than or misses the headline |
| **C** headline not formalized, "(Lean)" link shown | 009, 033, 126, 152, 159, 191, 194, 206, 222, 229, 230, 260, 261, 266, 269, 272, 280, 281, 323, 367, 371 | not in `formalization.yaml` (consistent), but CONTENTS.md attaches a "(Lean)" link to a blurb stating the unformalized headline |
| **D** trust surface | 032 (CM Hodge), 307 (coarse Novikov) | the statement rests on very large bespoke definition trees; CM Hodge's were changed after release |
| **E** hygiene | 095, 107 | abstract/scope-note mismatches |

### A. Support-only formalizations listed as formalized main results

The Oct 7 Comparator README said that five configurations "verify supporting
results, not the corresponding papers' main theorems":
CharacterVarietiesAllSeamsSupport, CartierChartCompactnessSupport,
SurfaceConeCandidateSupport, TraceIdealTransportSupport and
HoneycombBridgeMassSupport. **That section was deleted in the Oct 26 update
(`42907c9e9`).** All five are still in `formalization.yaml`
`status.main_results`, and their papers are still in `sources`, which the file
describes as the "Catalog of papers with a formalized main result":

- 027 *Integral points on character varieties of curves*: Lean proves
  seam-equation compatibility. The scope note says: "Existence of integral
  points and Zariski density are not established."
- 066 *Uniform Cartier sections for Fano type contractions*: Lean proves
  compactness of chart-field retractions. The scope note says it "does not
  construct a Cartier divisor …".
- 195 *A complete local domain without a small Cohen–Macaulay module*: Lean
  proves only that the candidate ring is a complete 3-dimensional normal
  local domain. Scope note: "it does not assert the absence of small
  Cohen–Macaulay modules."
- 301 *The trace cone classifies Razak–Jacelon stabilizations*: Lean proves
  the Section 2 ideal-transport lemma. Scope note: "This comparison does not
  establish that conclusion."
- 237 *Critical honeycomb chords with prescribed boundary endpoints* (listed):
  Lean proves finiteness of bridge sums. Scope note: "The paper's
  h^{4/3+o(1)} mean-length law and its central-visit and hexagonal-chord
  exponents are outside them."

**Coverage gap.** Lattice24 reviewed the 547 manuscripts it classed as
"without a Lean formalization", which is the complement of the catalogue.
Its `RESULTS.tsv` has no entry for any of these five papers, so they are
neither Lean-verified nor covered by the only complete public proof review.
The same holds for the B items 212, 277 and 312.

### B. Listed as formalized, but the Lean statement is weaker or partial

- **277** *Threshold parallel repetition for finite-dimensional entangled
  games*. The Lean bound is `exp(-κ δ^13 k/(1+log((a+1)(b+1))))`. The paper's
  Theorem 1.1 and abstract claim `δ^5`. The introduction (l.165–168) calls
  `δ^13` "the weaker rate" that "already follows", and calls the
  `δ^5` "universal fifth-power application" its contribution.
- **212** *Strict convexity and differentiability of the planar exponential
  first-passage limit shape*: strict convexity (in the title) is not
  formalized.
- **312** *The Grothendieck homotopy hypothesis via elementary expansions*:
  Lean proves the elementary-expansion theorem, which is the paper's
  `thm:main`. The homotopy hypothesis itself (title, abstract, CONTENTS
  blurb) is not formalized.
- **290** *Bounded recovery for modular spectral averages*: the recovery
  theorem is formalized. The bicentralizer triviality labelled `thm:main` is
  not.
- **378** *The Exponential Time Hypothesis is False*: the Lean time exponent
  is `n(log log n)^2/√log n` against the paper's `n log log n/√log n`. This
  still refutes ETH. The machine model was checked and is a genuine multitape
  TM with finitely many states over `Option Bool` tapes, with visited-space
  accounting.

### C. Headline not formalized, but a "(Lean)" link sits next to the headline

These are honestly scoped in the scope notes and are not in
`formalization.yaml`. CONTENTS.md, however, prints each family's headline
claim followed by "([Lean](lean/docs/NNN.md))". Lattice24's single-pass LLM
review ("no gap found") is the only check of these headline claims:

| fam | headline claim | what Lean proves |
|---|---|---|
| 261 | 2D Anderson model: pure-point spectrum at every disorder | a.s. spectrum = [-4-h, 4+h] (the classical part) |
| 194 | Lech's multiplicity conjecture | char-p Dutta-domain comparison (supporting) |
| 266 | N(6)=3 MUBs | family bound ≤5 plus Fourier vanishing |
| 229 | exact 3-state reconstruction threshold | only reconstruction above Kesten–Stigum (the classical direction) |
| 367 | critical dimension 7 for one-phase Bernoulli | existence of a nonflat minimizer in R^7, not flatness for d ≤ 6 |
| 272 | entangled state with zero distillable key | PPT-composition consequences |
| 230 | exact Hausdorff gauge for SLE (0 < H^h < ∞) | positivity only |
| 222 | Ising perceptron free energy | finiteness of the variational value |
| 281 | QAOA reaches the SK ground state | conditional SK variational identities |
| 260 | Bondi–Penrose inequality (CKS class) | end replacement plus Schwarzschild examples |
| 280 | VOA → completely rational conformal net, etc. | part (1) of five |
| 009 | Bogomolov–Pop reconstruction (bijection) | injectivity |
| 033 | reverse log-Kodaira inequality | only the fiber κ=−∞ branch |
| 126 | 2^{Ω(n)} PSD rank | n^{ω(1)} |
| 152 | zero-entropy system without smooth model | finite entropy |
| 159 | quasipolynomial Szemerédi bounds | only the reciprocal-sum consequence |
| 191 | Heilbronn bound for every large n | along a sequence |
| 206 | finite lattice representation undecidable | graph criterion only |
| 269 | Laughlin gap stability under disorder | unperturbed gap |
| 323 | separable quotient problem independent | CH direction only |
| 371 | blowup for every large odd power | arbitrarily large odd powers |

### D. Statements resting on large bespoke definitional bases

- **032 CM Hodge.** The challenge imports a 257-file, about 52,000-line
  definitional and lemma tree under
  `ComparatorChallenges/HodgeConjectureCMAbelianVarieties/HodgeConjecture`.
  Headers say it was adapted from Formal Conjectures and sphere-six-complex,
  and that "This file has been modified". On Oct 29, commit `204e5f8f8`
  ("Align CM Hodge comparator declarations with the Lean solution") changed
  259 files of this tree. After normalizing names, imports and visibility,
  131 files still have token-level changes
  (`output/hodge-alignment-diff.txt`). The largest are
  `Hodge/Filtration.lean` (+512/−59 tokens, new `siteSheafHom` definitions),
  `Hodge/AnalyticDifferentialForms.lean` and `Hodge/HolomorphicDeRham.lean`.
  They look like a port between Lean module systems, but the statement's
  meaning (`Hdg^p(X;ℚ)`, `algebraicCycleClassSpan`) depends on this tree. It
  was edited to match the solution and is not pinned to an upstream
  reference. Formal Conjectures main (2befc3a, Nov 4) contains no Hodge file
  to diff against.
- **307 coarse Novikov counterexample.** The statement is about
  `constructedCoarseAssembly` and `KX1`, defined inside a 331 KB challenge
  with 189 declarations. Whether these match standard coarse K-homology and
  Roe-algebra assembly is the whole content and is not machine-checked.
- Largest challenge files: EditApproximation 1.4 MB, CoarseAssembly 332 KB,
  CKSBondiPenrose 189 KB, ThomasonModelStructures 135 KB,
  CharacterCriterion 131 KB, ThorpRouting 93 KB.
- nanoda (an independent kernel) is enabled in only 2 of 418 configs. Two
  challenges import the OAI solution library (both are Support configs).

### E. Hygiene

- **095.** The abstract says "homogeneous polynomial of degree 16". That is
  the reduced polynomial q of Corollary `cor:reduced`, which is not
  formalized. Theorem 1.1 and the Lean are about the degree-20 p.
- **107.** `docs/107.md` links the "Below 2.258" and "Staggered extraction"
  papers and says the 9/4 bound "implies the paper's weaker 2.258 headline".
  The ω(ℂ) ≤ 9/4 Lean (`AuxiliarySeparation`) corresponds to
  *Matrix-Multiplication-Nine-Fourths-October-2-2026*. That paper is in
  `formalization.yaml` but linked from no scope note. The ω definition was
  checked: the admissible-exponent set is nonempty (τ=3) and bounded below
  by 2, so `sInf` is not junk.
- **"300 / 719 top-line results formalized" cannot be reproduced** from the
  repository: 173 (now 176) `formalization.yaml` sources, 340 (now 345)
  papers linked from scope notes, 242 (now 245) families with a "(Lean)"
  link, and 474 (now 482) manuscripts in such families. This matches
  yuyauchuncn's "three denominators" finding.

### Checks that found nothing

- **Natural-number `sInf` junk values** (the failure mode in arXiv
  2610.08144). The 13 explicit `sInf {n : ℕ | …}` definitions in challenges
  were inspected, including MaximalSeshadri's `idealOrder` (the order of a
  curve's local equation). None makes a target vacuous: each set is nonempty
  by construction or used only in lower bounds. Nine natural-number
  definitions written in tactic mode (`:= by …`) were not inspected.
- **Definitions checked and found faithful:** ETH machine model (378), QMA
  verifier and many-one reductions (275), random k-SAT threshold (235),
  ω(ℂ) (107), Kaplansky zero-divisor group conditions (196),
  noiseless-regression success threshold `((2:ℕ)/(3:ℕ) : ℝ≥0∞)` (140). The
  last relies on `binop%` coercing the leaves, so it is 2/3 rather than 0;
  confirming this with a Lean `#eval` is recommended.
- **Public claim not borne out:** the claim that family 130's Fourier Lean
  is "weaker than the paper" is wrong for the first paper. Its Theorem 1.1 is
  itself the subsequential statement.
- **Counterexample arithmetic:** 088's ratio 121·C(20,10)/(21·2^20) =
  22355476/22020096 checks.

## Reproduce

```sh
git clone https://github.com/openai/math && cd math && git checkout 4eaee8754
python3 -I scripts/inv.py . out                         # config/docs inventory
python3 -I scripts/dossier3.py . dossiers               # per-family dossiers
python3 -I scripts/catalogue_check.py .                 # catalogue vs scope notes
python3 -I scripts/hodge_alignment_diff.py              # needs commit 204e5f8f8
```
