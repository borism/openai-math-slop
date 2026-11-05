# Issue 5: CM Hodge provenance and the coarse assembly map

Follow-up to borism/openai-math-slop#5.
- **Revisions:** openai/math `4eaee8754`. The challenge tree before alignment is `42907c9e9`, which equals `204e5f8f8^`.
- **Upstream compared against:** Paul-Lez/HodgeConjecture, all 1027 commits scanned.
- **Method:** static reading and scripted diffs. A Lean toolchain only became available after this review; see "Lean check" below for what was compiled afterwards.

## 1. Upstream anchor (CM Hodge), high confidence
- No upstream commit contains the challenge tree exactly.
- The closest base is Paul-Lez/HodgeConjecture `9447d71c` (2026-09-27): 197 of 257 files are identical after normalization. Eight commits from 2026-09-22 to 2026-09-26 tie with it.
- Under `Definitions/`, only 7 files differ from that base. All 7 are Mathlib-version ports (`StdSimplex`→`Convexity.StdSimplex`, `dif_pos`→`dite_eq_left`, `coeff`, `ι_desc`).
  - Diffs: `outputs/pre-vs-upstream-9447d71c/` and `outputs/post-vs-upstream-9447d71c/`.
- `Statement.lean`, `Variants.lean`, `Hodge/Filtration.lean` and `Cycle/FundamentalClass.lean` were byte-identical to upstream before `204e5f8f8`.
- So the challenge is upstream `HodgeConjectureForAbelianVarieties` plus an `hCM` hypothesis.
- Only `CM.lean` (~60 lines, written by OpenAI) has no upstream anchor.
- It reads as the standard definition (medium-high confidence): `H¹(X;ℚ)` is free of rank 1 over a product of CM fields acting by `F¹`-preserving (hence Hodge) endomorphisms.

## 2. The alignment commit `204e5f8f8`, high confidence (medium-high for `Filtration.lean`)
After rename normalization, 13 `Definitions/` files keep token-level changes (`outputs/alignment-204e5f8f8-definitions-residual-hunks.txt`; per-file classes in `outputs/alignment-classification.tsv`). Every hunk falls into one of these classes:
- explicit-argument rewrites (`x.f` → `f x`);
- one abbrev fold (`RelativeCochainComplex`);
- `section`/`@[expose]` removals and one named local instance;
- in `Filtration.lean`: an identity bridge `siteSheafHom f := f` used only in proofs, a retargeted `implicit_reducible` attribute, a coercion form, and proof edits.

No hunk changes what a definition means. The bodies of `hodgeFiltration`, `hodgePiece`, `hodgeClasses` and `fieldToDeRhamCohomologyLinear` are untouched.

## 3. Hostile review for collapse (CM Hodge), medium-high confidence
- The analytic topology is the classical one.
- `Order.coheight` is codimension: `GenericPoint.lean:37-41` uses Mathlib's specialization order, with the generic point as `⊤`.
- The only `sorry` is the challenge hole at `Challenge.lean:43`. There are no axioms.
- **The one way the challenge could be vacuous:** if `H¹(X;ℚ)` were infinite- or odd-dimensional, `CMH1Data.model` could never exist, so `HasComplexMultiplication X` would be false for every `X`.
  - By reading, this does not happen, but no Lean lemma excludes it.
  - The sanity statements A1–A12 in `SanityLemmas.lean` cover this, cycle-class non-collapse, and a CM witness.

## 4. Coarse assembly (family 307)
`KX1`, `OddK`, `K1` and the Roe algebra read as standard. Two concerns:

**Zero-map fallbacks**
- `analyticFamilyIndex` (`CoarseAssembly.lean:5783-5785`) and `separatedIndexFamily` (`:6226-6230`) both have the form `if <Prop> then … else 0`.
- If either fallback were taken, `constructedCoarseAssembly` would be the zero map. Three parts of the target theorem (`:6629`) would then hold trivially:
  - `constructedCoarseAssembly α = 0`;
  - non-injectivity of the map;
  - non-injectivity of its rationalization.
- The `then` conditions are proved only in the solution tree (`AnalyticFamilyIndex.lean:43`, `SeparatedCoarseAssembly.lean:22`). Comparator checks only the target theorem, so it does not certify those proofs as part of the statement.

**Bespoke index formula**
- The per-scale index is `relativeClass (−c(F)²)`, where `c` is the Cayley transform (`:2192`, `:2233`, `:3978`).
- By hand, this is homotopic to the textbook `exp(πi(F+1))`, so it should be the Higson–Roe boundary map. No Lean statement says so.

The target claims a coarse Novikov counterexample in bounded geometry, so both points matter.

## 5. Trust surface
`scripts/trust_surface.py` gives an upper bound on data-like declarations per challenge module (`outputs/trust-surface.tsv`):

| challenge | data-like declarations |
|---|---|
| Hodge tree (259 files) | 1280 |
| EditApproximation | 1157 |
| SnakyCertificate | 670 |
| ThorpRouting | 357 |
| CKSBondiPenrose | 310 |
| CoarseAssembly | 216 |

Across all 419 challenges: 12,084 declarations and 117,516 lines.

## Recommendations
1. Pin `9447d71c` in the challenge README, and publish the upstream diff and the port list.
2. For each declaration touched by `204e5f8f8`, prove `old = new` by `rfl` in a side file that imports both trees.
3. Add non-collapse sanity lemmas as extra Comparator targets:
   - `H¹` is finite;
   - a CM witness and a non-CM example;
   - `algebraicCycleClassSpan X 0 = ⊤`;
   - a non-zero divisor class.
4. For CoarseAssembly:
   - either put the two `then`-branch facts into the target, or make the definitions take the proof so the `else 0` disappears;
   - add `multiplierBoundaryClass F = relativeClass (−exp(πiF))` and a non-collapse check.
5. Set `enable_nanoda` on both configs.

## Files
- `SanityLemmas.lean`: statements A1–A12 (Hodge) and B1–B4 (coarse assembly), all ending in `sorry`.
- `scripts/`: `match_upstream.py`, `diff_vs_upstream.py`, `residual_hunks.py`, `trust_surface.py`.
- `outputs/`:
  - `pre-vs-upstream-9447d71c/`, `post-vs-upstream-9447d71c/`
  - `alignment-204e5f8f8-definitions-residual-hunks.txt`, `alignment-classification.tsv`
  - `trust-surface.tsv`
