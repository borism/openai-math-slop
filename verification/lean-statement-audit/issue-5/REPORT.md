# Issue 5: CM Hodge provenance and the coarse assembly map

Follow-up to borism/openai-math-slop#5.
- **Revisions:** openai/math `4eaee8754`. The challenge tree before alignment is `42907c9e9`, which equals `204e5f8f8^`.
- **Upstream compared against:** Paul-Lez/HodgeConjecture, all 1027 commits scanned.
- **Method:** static reading and scripted diffs, followed by a Lean check once a toolchain was available (see "Lean check" below).

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

## Lean check (added after the review)
Lean 4.34.1, Mathlib `d13f23b`, openai/math `4eaee8754`. Tools: `../lean-checks/`.

**1. Challenges compile.**
- `ComparatorChallenges.CoarseAssembly` and the CM Hodge tree (`HodgeConjecture.*` plus `ComparatorChallenges.HodgeConjectureCMAbelianVarieties.CM`) build cleanly.
- The only warnings are the expected `sorry`s on the target theorems.

**2. Sanity lemmas elaborate.**
- All 16 statements in `SanityLemmas.lean` (A1–A12, B1–B4) type-check against the real challenge definitions (`outputs/sanity-lemmas-elaboration.txt`); their proofs are still `sorry`.
- B1–B3 needed small fixes: a local `Ring` instance, natural-number scales, the current `NormedSpace.exp` signature, and an explicit `IsClosed` argument.

**3. The zero-map fallbacks are never taken.**
- The 212-module closure of `OAI.Topology.CoarseAssembly.AnalyticFamilyIndex` and `…SeparatedCoarseAssembly` was built, so the kernel checked every proof in it (`outputs/coarse-then-branch-axioms.txt`).
- `analyticFamilyIndex_eq_lift` holds for all `o, hr, χ, η`: `analyticFamilyIndex` *is* the `QuotientAddGroup.lift` of the `then` branch.
- `separatedIndexFamily_atScale` holds for all `o, n`: the family *is* `separatedRipsIndex` at every scale.
- Both, and `analyticFamilyIndexFree_relation`, depend only on `[propext, Classical.choice, Quot.sound]`.
- So neither `else 0` branch is ever used, and `constructedCoarseAssembly` is not the zero map by fallback.

**4. Same definitions in challenge and solution** (`outputs/coarse-fingerprint-compare.txt`)
- Every constant declared in `ComparatorChallenges.CoarseAssembly` was fingerprinted (kind, universe parameters, type hash, value hash for definitions) and compared with the solution's `OAI.Topology.CoarseAssembly.Definitions` closure.
- Identical: 322 definitions, 12 inductives, 17 constructors, 12 recursors, and the types of 790 helper theorems. These include `constructedCoarseAssembly`, `analyticFamilyIndex` and `separatedIndexFamily`.
- So item 3 applies to the challenge's definitions, not just to the solution's copies.

**5. Not done: the target theorem itself.**
- `bounded_geometry_graph_counterexample_unconditional` lives downstream of `OAI.Analysis.NuclearUltrapower.SOSSemantics`. That module checks a large sum-of-squares certificate: its input `SOSResidual` compiles to a 101 MB `.olean`.
- It was killed twice at about 13 GB RSS, the container's memory cap, the second time with `LEAN_NUM_THREADS=2` (`outputs/sos-semantics-oom.txt`).
- So the target's axioms were not printed. Rebuilding it needs a machine with more memory.

**Effect on §4 above.**
- The zero-map concern is resolved as a matter of fact.
- What remains is presentational: the challenge statement still certifies nothing about the fallbacks by itself, so the recommendation to remove the `else 0` stands.
- Non-collapse beyond the fallbacks (B4) and the Cayley-vs-exponential formula (B3) remain open.

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
- `SanityLemmas.lean`: statements A1–A12 (Hodge) and B1–B4 (coarse assembly), all ending in `sorry`; all elaborate.
- `AxiomsCoarse.lean`: the axiom check for the two `then`-branch lemmas.
- `scripts/`: `match_upstream.py`, `diff_vs_upstream.py`, `residual_hunks.py`, `trust_surface.py`.
- `outputs/`:
  - `pre-vs-upstream-9447d71c/`, `post-vs-upstream-9447d71c/`
  - `alignment-204e5f8f8-definitions-residual-hunks.txt`, `alignment-classification.tsv`
  - `trust-surface.tsv`
  - `sanity-lemmas-elaboration.txt`, `coarse-then-branch-axioms.txt`, `coarse-fingerprint-compare.txt`, `coarse-challenge-fingerprints.tsv`, `sos-semantics-oom.txt`
