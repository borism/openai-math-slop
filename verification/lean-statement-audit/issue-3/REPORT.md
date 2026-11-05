# Issue 3: papers catalogued as "formalized main result" whose Lean covers only part of the paper

Follow-up to borism/openai-math-slop#3. Upstream tree: openai/math `4eaee8754`.
- Paths are relative to that tree.
- No Lean toolchain was available during this review, so nothing was compiled; Lean statements were read as source.
- Paper arguments were read and re-derived by hand, with computational checks for 195.

## Summary
| fam | paper | what the Lean proves | review depth | verdict on the paper's text |
|---|---|---|---|---|
| 277 | Threshold parallel repetition | `δ^13` rate; paper claims `δ^5` | §4 re-derived line by line; §§2–3, 5–6 not reviewed | **concern**: `δ^5` rests only on an unrefereed external estimate (Song), not retrievable; the Lean neither uses nor certifies it |
| 195 | Complete local domain w/o small CM module | an existential that `C[[x,y,z]]` satisfies | full read of `paper.tex`, `surface.tex`; computations re-derived; script | **no gap found** at this depth |
| 301 | Trace cone / Razak–Jacelon | §2 ideal-transport lemmas | skeleton plus external-theorem interfaces (4,808 lines) | **not reviewed in depth**; concern about how Gabe's theorems are applied |
| 312 | Grothendieck homotopy hypothesis | `thm:main` (elementary expansion) | skeleton | **low concern**; issue softened |
| 290 | Bounded recovery / bicentralizer | §4 only | skeleton: reduction and end of rigidity proof | mismatch confirmed; no gap in parts read |
| 212 | Strict convexity, FPP limit shape | differentiability half | skeleton | mismatch confirmed; strict-convexity part (5,043 lines) unformalized |
| 027 | Integral points, character varieties | seam compatibility | skeleton | mismatch confirmed |
| 066 | Uniform Cartier sections | chart compactness | skeleton | mismatch confirmed |
| 237 | Critical honeycomb chords | `B_h ≍ (1+h)^{-1/4}` (correction) | skeleton | mismatch confirmed; the bound is an input imported from a companion |

## Corrections to issue 3 as filed

1. **237.** The Lean proves the full two-sided bound, not just finiteness of bridge sums.
   - `HoneycombBridgeMassSupport` proves `c(1+h)^{-1/4} ≤ B_h ≤ C(1+h)^{-1/4}` for all `h`.
     - Statement: `lean/ComparatorChallenges/HoneycombBridgeMassSupport.lean:66–72`.
     - Proof: `lean/OAI/Combinatorics/HoneycombChords/BridgeMass.lean:114` (no sorry in the file; not compiled).
   - The "finiteness" wording comes from a stale first paragraph of `lean/docs/237.md`; the page's last paragraph states the bound.
   - The bound is clause 1 of Prop `c:finite` (`…/Critical-honeycomb-chords…/build/sections/inputs.tex:10–13`).
   - The paper imports it from its companion *Uniform marked-polygon estimates and sharp finite bridge moments*, Thm 1.1 (`inputs.tex:44`).
   - The paper's own main theorem, `c:main` (`introduction.tex:31`, the `R^{4/3±ε}` chord law), is not formalized.
   - The companion papers are not in `formalization.yaml`.
2. **312.** The Lean proves the paper's labelled main theorem; only the title-level claim is unformalized.
   - The Lean proves the labelled `thm:main` (`00-introduction.tex:50`; `GrothendieckElementaryExpansion.lean:465`).
   - `cor:homotopy-hypothesis` (`04-consequences.tex:147`) and `cor:semimodel` (`:28`) are deduced from Henry 2016's conditional results: Props 5.3.6/5.3.7, Cor 5.3.12, Prop 4.4.4, Thm 5.1.2(5).
   - Only the title, abstract and catalogue overstate it.
   - Unchecked: whether the Lean's Ara–Henry coherator convention matches the one Henry's results need.

## 277: threshold parallel repetition (concern)

Paper: `preprints/Threshold-parallel-repetition-…-September-25-2026/build/sections/`.

**What the paper claims**
- `thm:main` (`00-introduction.tex:50–62`) states rate `κ₀δ^5/(1+log d)`.
- The introduction lists the "universal fifth-power application" as part of its contribution (`:161–166`).
- It says `δ^13` "already follows" from `thm:main` (`:166–169`).

**Re-derived, no error found**
- Sampling lemma (`04-threshold.tex:42–76`).
- Prop `prop:conditioning-to-tail` (`:82–185`):
  - rate arithmetic `c/r ≤ T/8 ≤ η/2` and `c(1+R/r) ≤ 3T/16`, using `r ≥ δ/(2q)` and `q log(1/q) ≤ 1/e`;
  - the bound `v + 7δ/16`;
  - the tensor-copy extension to all `k`.
- Main proof (`:214–231`): `T = (δ/4B₄)^4`, `κ₀ = 1/(16(4B₄)^4)`.

**The one analytic input for `δ^5`**
- It is Prop `prop:song-conditioning` (`:189–208`): `excess ≤ B₄τ^{1/4}`.
- The paper uses it "as an external theorem" from Zhao Song, ECCC TR26-199 (Aug 2026).
- Song's proof in turn builds on *Ten Advances*, Ch. 6.
- Neither source could be fetched (ECCC and cdn.openai.com are blocked here).

**What the Lean proves**
- Statement: `ComparatorChallenges/EntangledGames.lean:64–74`, universal `κ₀` at `δ^13`. The Lean never mentions Song.
- Its route (skimmed):
  - a conditioning step with budget `δ^8/2^80` (`OAI/Probability/EntangledGames/TestExtraction.lean:83–103`, via `good_event_step`);
  - a moment-method transfer in place of Prop 4.3 (`:107–114`);
  - `κ₀ = 2^-101` (`Main.lean:19`, `ExponentialBounds.lean:152`).

**Assessment**
- The Lean gives real machine-checked assurance for a universal `δ^13` theorem, but not for the paper's stated rate.
- The paper contains no Song-free proof of `δ^13`, so the Lean's argument is not documented anywhere in the paper.
- The cubic bound `cor:support-threshold` is outside both the Lean and this review.

**Proposals**
- Mark the entry `relationship: other`.
- Either formalize Song's Lemma 4.4, or state `thm:main` as conditional on it.
- Document the Lean's `δ^13` route in the paper.

## 195: no small CM module (no gap found)

**Read in full** (`paper.tex`):
- `thm:obstruction`: 119–126
- cone and model: 210–329
- extension: 331–375
- balancing: 402–443
- lattice: 467–523
- factor: 555–603
- proof: 605–627
- counterexample: 631–644
- corollary: 646–694

**Read in full** (`surface.tex`):
- smoothness: 117–217
- Chern numbers: 219–260
- positivity of `H = 3J−E`: 262–337

**Checks** (`scripts/check_195_small_cm.py`; output in `outputs/check_195_small_cm.txt`, all pass):
- Chern numbers from the branch stratification (10 rational curves, 15 nodes, Petersen incidence) plus Hurwitz.
- `n=1` gives the degree-5 del Pezzo.
- For prime `n`: `K²−2c₂ = n³(n²−10)` and `H² = 5n³`.
- For `n=7`:
  - `K² = 42875`, `c₂ = 14749`, `χ = 4802`;
  - `13377 > 6H² = 10290`;
  - the threshold is `n² > 40`.
- Symbolic: the RR-variance identity and the factor bound `1/4 − (K²−2c₂)/(12h)`.
- Randomized: the lattice identity (20,000 cases) and the mixture formula with variance ≤ 1/4 (5,000 cases).

**Not re-verified:** the standard external theorems (Bogomolov, Hodge index, Auslander–Buchsbaum, reflexive extension, HN filtrations).

**About the Lean**
- `SurfaceConeCandidateSupport.lean:8` is a pure existential.
- `ℂ[[x,y,z]]` satisfies it, and that ring is regular, hence Cohen–Macaulay.
- So the Lean has no bearing on the counterexample.

**Context and next steps**
- The work overlaps with Anghel 2026 and Chen 2026 (`paper.tex:148–166`).
- "No gap found" means one careful read plus arithmetic checks; specialist review is still needed.
- A natural Lean target: `thm:obstruction` for graded modules.

## 301: trace cone classifies stabilizations (not reviewed in depth)

**What the Lean proves:** the §2 statements in `TraceIdealTransportSupport.lean:61, 225, 229`, plus 14 provider lemmas that the config requires to be proved.

**Hinges on** (located, not verified):
- `05-uniqueness.tex:452`: Gabe Thm 11.14, applied to `H⊗K`. The text says "Neither separability of H nor an absorption hypothesis on H is required."
- `05-uniqueness.tex:492`: Gabe Thm 13.9.
- `07-cone-correction.tex:297`: Gabe Def 5.4.
- `08-point-intertwining.tex:14–17`: adapts the proof of Gabe Thm 14.1, which has an O∞-stable target and is "not applied directly".
- `04-small-stabilizers.tex:251`: BGSW Lemma 3.5, also O∞-stable; re-proved here.

**Proposal:** a specialist check of these hypothesis transfers, starting with §8.

## 290: bounded recovery (skeleton)

**Main theorem**
- `thm:main` is `BC(M,φ) = ℂ1` for separable type III₁ factors (`01-introduction.tex:84–90`).
- The paper calls it an alternative proof of part of Houdayer–Marrakchi's announced Thm G (`:77–82`).

**Derivation**
- Reduction via HI2017 Prop 3.4 / Thm 3.5.
- Flow via AHHM2020 Thm A(ii, iv).
- Ergodicity via Marrakchi 2020 Thm D (`02-bicentralizers.tex:21–68`).
- Then `thm:rigidity` (§5), which uses bounded recovery (§4).

**Checked**
- The reduction proof (`02-bicentralizers.tex:70–95`), including the `b_s = β_{e^{-s}}` convention.
- The eigenvalue lemma and the countability case split (`05-spectral-rigidity.tex:240–334`).
- Both are consistent.

**Lean**
- Covers §4 only (`ComparatorChallenges/BoundedRecovery.lean:88`).
- `StandardModularData` (`:50–63`) axiomatizes the standard form through a closed Tomita graph; whether that model is faithful was not assessed.

## 212, 027, 066 (skeletons)

**212**
- `thm:exponential-shape` (`introduction.tex:21–30`) claims differentiability *and* strict convexity.
- `PlanarFirstPassage.lean:91` proves differentiability, unique supports and a C¹ boundary, at rate 1 (other rates follow by scaling).
- Strict convexity (`sections/strict/`, 5,043 lines) is a renormalization argument against a flat face.
  - Its crux is constants uniform in the scale.
  - It imports DK2016 Prop 1.1 and DHS2014 Thm 1.1 (`strict/preliminaries.tex:22–46`).
  - Unformalized and unreviewed.
- `thm:gamma-differentiability` (`:44–49`) is also unformalized.

**027**
- The Lean proves seam compatibility (`CharacterVarietiesAllSeamsSupport.lean:17`).
- Unformalized: character counting with Lang–Weil irreducibility, and the descent step (`introduction.tex:60–194`).

**066**
- The Lean proves chart compactness.
- The main theorem rests on Chen 2025 Thm 1.6 and a new birational theorem with heavy external inputs, Birkar and normalized volume (`introduction.tex:30–103`).

## Patches

**`formalization-yaml.patch`**
- Applies to upstream `4eaee8754`, not to the fork's older `main`.
- Annotates the 9 `sources` entries with schema-native fields:
  - `relationship`: `other` for 8 papers, `formalizes` for 312;
  - `location` (what is formalized) and `note` (what is not).
- Rewrites the header comment "Catalog of papers with a formalized main result".
- Adds YAML comments on the matching `status.main_results` entries (the schema has no note field there).
- Validation: the original and patched files both pass the v0.4 schema with 0 errors (`outputs/validate_yaml.txt`; schema from `raw.githubusercontent.com/mathlib-initiative/formalization.yaml`).
- Generator: `scripts/make_yaml_patch.py`.

**`comparator-readme.patch`**
- Restores, verbatim, the "Supporting-result comparisons" section from `fd4aeeb2e`.
- Adds a short list of comparisons weaker than the headline: EntangledGames, PlanarFirstPassage, BoundedRecovery, GrothendieckElementaryExpansion.

## Hygiene
- `HoneycombBridgeMassSupport.lean:71` has the docstring "Trusted reference hole only; missing necessary main obligation." It sits on the challenge's placeholder `sorry`, and the solution does prove the theorem, so the wording is misleading.
- `lean/docs/237.md`: the first paragraph ("finiteness") contradicts the last paragraph (the quarter-power bound).

## Limitations
- No Lean build was run.
- Song and *Ten Advances* Ch. 6 were unreachable.
- 301, 212, 027 and 066 were reviewed at skeleton depth; finding nothing there means nothing.
