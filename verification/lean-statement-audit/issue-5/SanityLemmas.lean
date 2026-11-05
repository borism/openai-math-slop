/-
  ============================================================================
  ELABORATED, NOT PROVED. Every statement below type-checks against the real
  challenge definitions (Lean 4.34.1, Mathlib d13f23b, openai/math 4eaee8754):
  `lake env lean` reports 0 errors, and each theorem has a `sorry` warning.
  See ../issue-5/outputs/sanity-lemmas-elaboration.txt.
  ============================================================================
  These are proposed *statements*, all ending in `sorry`. They are meant to be
  added next to the Comparator challenge (as extra targets, or in a separate
  "sanity" module checked against the same definitions). They rule out the
  ways the bespoke definitions could collapse and make a challenge vacuous or
  trivially provable.

  Names and namespaces come from openai/math at 4eaee8754:
    lean/ComparatorChallenges/HodgeConjectureCMAbelianVarieties/{CM,Challenge}.lean
    .../HodgeConjecture/Definitions/AlgebraicGeometry/Hodge/Filtration.lean
    .../HodgeConjecture/Definitions/AlgebraicGeometry/Cycle/FundamentalClass.lean
    lean/ComparatorChallenges/CoarseAssembly.lean

  Status of each statement: TRUE in standard mathematics unless marked
  otherwise. For each one, the comment says which collapse it excludes.
-/
import ComparatorChallenges.HodgeConjectureCMAbelianVarieties.CM
import ComparatorChallenges.CoarseAssembly

namespace Issue5Sanity

/-! ## Part A: CM Hodge challenge -/

section Hodge

open CategoryTheory AlgebraicGeometry OAI.AlgebraicGeometry.ComplexPoint
open scoped OAI.AlgebraicGeometry.Hodge.Filtration.ComplexPoint
open _root_.OAI.AlgebraicGeometry.ComplexPoint.Basic.ComplexSchemePoint
open _root_.OAI.AlgebraicGeometry.ComplexMultiplication.Definitions
open _root_.OAI.AlgebraicGeometry.Foundations.ProjectiveSpaceIs

variable (X : Over (Spec ↧ℂ)) [IsIntegral X.left] [Smooth X.hom] [IsProjective X.hom]

/-- A1. Constant-sheaf cohomology is not degenerate in degree 0: `X(ℂ)` is connected.
Excludes: an analytic topology/sheaf-cohomology setup in which `H^0` is `0` or infinite
dimensional. `H^0` infinite-dimensional would mean, e.g., `X(ℂ)` got a totally disconnected
topology, and then `H^1` would also be wrong and `HasComplexMultiplication` unsatisfiable. -/
theorem finrank_H0 : Module.finrank ℚ (H^0(X; ℚ)) = 1 := by sorry

/-- A2. Finiteness of rational `H^1`. **Key non-vacuity check:** `CMH1Data.model` is a
ℚ-linear equivalence with a finite product of number fields. If `H^1(X; ℚ)` were not
finite-dimensional, `HasComplexMultiplication X` would be false for every `X` and the
challenge would be vacuously true. -/
theorem finite_H1 : Module.Finite ℚ (H^1(X; ℚ)) := by sorry

/-- A3. For an abelian variety, `dim H^1 = 2 · dim X`. Every CM field has even degree, so an
odd or wrong dimension would also make `HasComplexMultiplication` unsatisfiable. -/
theorem finrank_H1_abelian [GrpObj X] :
    (Module.finrank ℚ (H^1(X; ℚ)) : WithBot ℕ∞) = 2 * topologicalKrullDim X.left := by sorry

/-- A4. The rational-to-de Rham comparison is an isomorphism after `ℂ ⊗`.
`CMH1Data.preserves_hodgeFiltration` and `Hdg^p` are both read through this map. -/
theorem h1Comparison_bijective : Function.Bijective (h1Comparison X) := by sorry

/-- A5. Filtration boundary values: `F^0 = ⊤` and `F^{n+1} H^n = ⊥`. -/
theorem hodgeFiltration_zero (n : ℤ) : hodgeFiltrationComplexSubmodule X 0 n = ⊤ := by sorry

theorem hodgeFiltration_top (n : ℕ) :
    hodgeFiltrationComplexSubmodule X ((n : ℤ) + 1) n = ⊥ := by sorry

/-- A6. `F^1 H^1` has the right size, `h^{1,0} = g = (1/2) b_1`. This excludes `F^1 = ⊥` or
`F^1 = ⊤`. Either degeneracy would make `preserves_hodgeFiltration` automatic, so the CM
hypothesis would become vacuous. That would not make the challenge vacuous, but it would
make it a different theorem. -/
theorem finrank_F1_H1 [GrpObj X] :
    2 * Module.finrank ℂ (hodgeFiltrationComplexSubmodule X 1 1) =
      Module.finrank ℚ (H^1(X; ℚ)) := by sorry

/-- A7. Cycle classes do not collapse in codimension 0. The class of `X` itself spans `H^0`.
This also fixes the convention `Order.coheight = codimension`. -/
theorem algebraicCycleClassSpan_zero : algebraicCycleClassSpan X 0 = ⊤ := by sorry

/-- A8. Cycle classes do not collapse in codimension 1. A hyperplane section of a positive
dimensional projective `X` has a non-zero class. With A9 this excludes the trivial truth
`Hdg^p = ⊥`. -/
theorem exists_nonzero_divisor_class (h : 0 < topologicalKrullDim X.left) :
    ∃ (x : X.left) (hx : Order.coheight x = 1), cycleComponentSheafClass X x hx ≠ 0 := by
  sorry

/-- A9. The easy direction: algebraic classes are Hodge classes. -/
theorem algebraicCycleClassSpan_le_hodgeClasses (p : ℕ) :
    algebraicCycleClassSpan X p ≤ Hdg^p(X; ℚ) := by sorry

/-- A10. `Hdg^p` is not everything. For an abelian surface, `h^{2,0} = 1 > 0`, so
`Hdg^1 ≠ H^2`. This excludes the degeneracy `Hdg^p = ⊤`, under which the statement would be
the false claim "every class is algebraic". -/
theorem hodgeClasses_ne_top_of_surface [GrpObj X] (h2 : topologicalKrullDim X.left = 2) :
    Hdg^1(X; ℚ) ≠ ⊤ := by sorry

/-- A11. **Key non-vacuity check for the CM hypothesis.** Some genuine CM abelian variety
satisfies all the hypotheses of `HodgeCM.hodge_conjecture_for_cm_abelian_varieties`, and its
`H^1` is non-zero. For example `E : y² = x³ - x` with CM by `ℚ(i)`. A concrete witness
(an explicit `X`) is better than an existential. -/
theorem exists_cm_witness :
    ∃ (Y : Over (Spec ↧ℂ)) (_ : IsIntegral Y.left) (_ : Smooth Y.hom)
      (_ : IsProjective Y.hom) (_ : GrpObj Y),
      HasComplexMultiplication Y ∧ 0 < Module.finrank ℚ (H^1(Y; ℚ)) := by sorry

/-- A12. CM is a real restriction. Some abelian variety (e.g. a non-CM elliptic curve)
fails `HasComplexMultiplication`. This excludes the degeneracy in which `H^1` or the
filtration collapses so that `CMH1Data` exists for every `X`. -/
theorem exists_non_cm :
    ∃ (Y : Over (Spec ↧ℂ)) (_ : IsIntegral Y.left) (_ : Smooth Y.hom)
      (_ : IsProjective Y.hom) (_ : GrpObj Y), ¬ HasComplexMultiplication Y := by sorry

end Hodge

/-! ## Part B: coarse assembly challenge (family 307) -/

section Coarse

open OAI OAI.CoarseAssembly OAI.CoarseAssembly.Rips OAI.CoarseAssembly.Analytic
open OAI.CoarseAssembly.DiscreteRoe

/-- B1. Move `dif_pos` out of the solution tree. `analyticFamilyIndex` is
`if relations A ≤ ker … then lift … else 0` (CoarseAssembly.lean:5783-5785). The
solution-side `analyticFamilyIndex_eq_lift`
(lean/OAI/Topology/CoarseAssembly/AnalyticFamilyIndex.lean:43) proves the `then` branch, but
that file is not part of what Comparator checks against the challenge. -/
theorem analyticFamilyIndex_condition {Q : ℕ → Type} [∀ i, MetricSpace (Q i)]
    [∀ i, Fintype (Q i)] [∀ i, DecidableEq (Q i)] {A : Type} [NonUnitalCStarAlgebra A]
    {r : ℝ} (o : ∀ i, Q i) (hr : 0 ≤ r)
    (χ : ∀ i, C(Point (Q i) r, ℂ) →⋆ₐ[ℂ] ℂ) (η : ∀ i, C(Point (Q i) r, ℂ) →⋆ₙₐ[ℂ] A) :
    letI := separatedMetric o
    letI : Ring (Unitization ℂ (algebra (X := Sigma Q) (H := lp (fun _ : ℕ => ℂ) 2))) :=
      inferInstance
    relations A ≤ (analyticFamilyIndexFree o hr χ η).ker := by sorry

/-- B2. The same for `separatedIndexFamily` (CoarseAssembly.lean:6226-6230). Its `else` branch
is the zero family. The solution-side counterpart is `separatedIndexFamily_atScale`
(lean/OAI/Topology/CoarseAssembly/SeparatedCoarseAssembly.lean:22). -/
theorem separatedIndexFamily_atScale_eq {Q : ℕ → Type} [∀ i, MetricSpace (Q i)]
    [∀ i, Fintype (Q i)] [∀ i, DecidableEq (Q i)] (o : ∀ i, Q i) (n : ℕ) :
    letI := separatedMetric o
    (separatedIndexFamily o).atScale n = separatedRipsIndex o n (Nat.cast_nonneg n) := by sorry

/-- B3. The per-scale index is the standard Higson–Roe boundary map. The challenge uses the
rational unitary `-(F - i)²(F + i)⁻²` (`rationalBoundaryUnitary`, CoarseAssembly.lean:2233)
where the textbook formula is `exp(2πi·(F+1)/2) = -exp(πiF)`. The auditor checked by hand
that both are `1` at `±1` and wind once over `[-1,1]`, so they should define the same
relative `K₁` class. This lemma records that fact. Stated in the multiplier/Roe setting used
by `multiplierBoundaryClass` (CoarseAssembly.lean:3978). -/
theorem multiplierBoundaryClass_eq_exp {X H : Type} [Fintype X] [DecidableEq X]
    [PseudoMetricSpace X] [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H]
    (F : multiplierAlgebra (X := X) (H := H)) (hF : IsSelfAdjoint F)
    (hdefect : F.val ^ 2 - 1 ∈ algebra (X := X) (H := H))
    (hS : IsClosed ((algebra (X := X) (H := H)) : Set (Operator X H))) :
    multiplierBoundaryClass F hF hdefect =
      OperatorKTheory.relativeClass (hS := hS) (algebra (X := X) (H := H))
        ⟨-NormedSpace.exp ((Real.pi * Complex.I) • F.val), sorry⟩ sorry := by sorry

/-- B4. Non-collapse of the final map. `bounded_geometry_graph_counterexample_unconditional`
asserts `constructedCoarseAssembly α = 0` and non-injectivity. Both are trivial if
`constructedCoarseAssembly = 0`. Asking for one class with non-zero image excludes that.
(Whether such a class exists on `VertexUnion` is a mathematical question. If it does not,
replace this with B1+B2+B3 and a non-collapse test on a separated union of cycles.)
STATUS: conjectural / to be decided by the authors. -/
theorem constructedCoarseAssembly_ne_zero : constructedCoarseAssembly ≠ 0 := by sorry

end Coarse

end Issue5Sanity
