/-
SKETCH — statements ELABORATE, proofs are `sorry` (except where noted).
Checked with Lean 4.34.1 + Mathlib d13f23b (the upstream pin) by
`scripts/check_sketch.sh`, which inlines the body below after lines 1–75 of
upstream `lean/ComparatorChallenges/HyperbolicCones.lean` (4eaee8754) and runs
`lake env lean`: result 0 errors, only `declaration uses sorry` warnings
(see outputs/sketch-elaboration.txt). No proof here is checked.

Purpose: a formalization plan for Corollary `cor:reduced` of
"A Nonspectrahedral Hyperbolicity Cone" (openai/math family 095,
build/sections/reduced-polynomial.tex). The abstract headlines this degree-16
polynomial q; the Comparator `main_result` is about the degree-20 polynomial p.

Correction found while checking (numerically, scripts/reduced_numeric.py): with
the challenge's `phi`, `phi y T = C (Q(y) ⊗ Tᵀ) Cᵀ`; the paper's
`Φ_y(T) = C (Q(y) ⊗ T) Cᵀ` holds only for symmetric T (the only case the
paper uses). Steps 1–2 below carry the transpose.
-/
import ComparatorChallenges.HyperbolicCones

namespace OAI.Paper256

noncomputable section

-- BEGIN BODY
open Matrix

/-- `K_i = !![0, e_iᵀ; -e_i, 0]` (4×4). -/
def kMat {R : Type*} [CommRing R] (i : Fin 3) : Mat 4 R :=
  fun a b => Fin.cases (Fin.cases 0 (fun j => if j = i then 1 else 0) b)
    (fun a' => Fin.cases (if a' = i then -1 else 0) (fun _ => 0) b) a

/-- `C = (K₁ K₂ K₃)`, 4 × 12, columns indexed by `Fin 3 × Fin 4`. -/
def cMat {R : Type*} [CommRing R] : Matrix (Fin 4) (Fin 3 × Fin 4) R :=
  fun a jb => kMat jb.1 a jb.2

/-- The 16 × 16 block matrix `!![I₃ ⊗ X, Cᵀ; C (Q(y) ⊗ I₄), Z]`. -/
def reducedBlock {R : Type*} [CommRing R] (X Z : Mat 4 R) (y : Fin 3 → R) :
    Matrix ((Fin 3 × Fin 4) ⊕ Fin 4) ((Fin 3 × Fin 4) ⊕ Fin 4) R :=
  Matrix.fromBlocks (Matrix.kronecker (1 : Mat 3 R) X) cMat.transpose
    (cMat * Matrix.kronecker (qMatrix y) (1 : Mat 4 R)) Z

def reducedValue {R : Type*} [CommRing R] (X Z : Mat 4 R) (y : Fin 3 → R) : R :=
  (reducedBlock X Z y).det

/-- The reduced polynomial `q` in the challenge's 23 coordinates. -/
def reducedPolynomial : MvPolynomial Coord ℝ :=
  reducedValue
    (symmetricCoordinates fun ij => MvPolynomial.X (Sum.inl (Sum.inl ij)))
    (symmetricCoordinates fun ij => MvPolynomial.X (Sum.inl (Sum.inr ij)))
    (fun i => MvPolynomial.X (Sum.inr i))

/-- `det X` as a polynomial in the 23 coordinates. -/
def detX : MvPolynomial Coord ℝ :=
  (symmetricCoordinates fun ij => MvPolynomial.X (Sum.inl (Sum.inl ij)) :
    Mat 4 (MvPolynomial Coord ℝ)).det

/-- Step 1 (block identity, corrected with `Tᵀ`). Numerically verified
(max error 4e-15; the untransposed version fails by up to 21).
Route: `ext a b`; `Matrix.mul_apply`, `Fintype.sum_prod_type`,
`Fin.sum_univ_three/four`; `fin_cases`; `simp [phi, kMat, qMatrix]`; `ring`.
A brute-force `simp` attempt needed >4M heartbeats and still left `Fin.cases`
residue; a cleaner route is `phi y T = ∑ i j, Q i j • K_i Tᵀ K_jᵀ` first. -/
theorem phi_eq_kron {R : Type*} [CommRing R] (y : Fin 3 → R) (T : Mat 4 R) :
    phi y T = cMat (R := R) * Matrix.kronecker (qMatrix y) T.transpose *
      (cMat (R := R)).transpose := by
  sorry

/-- Step 2 (Schur complement). Route: `Matrix.det_fromBlocks₁₁` with
`Invertible (1 ⊗ X)`, `Matrix.det_kronecker` (`det (1₃ ⊗ X) = det X ^ 3`),
mixed product `(Q ⊗ 1)(1 ⊗ X⁻¹) = Q ⊗ X⁻¹`, then `phi_eq_kron` with `T = (X⁻¹)ᵀ`.
For symmetric `X` (the polynomial case) `(X⁻¹)ᵀ = X⁻¹`, matching the paper. -/
theorem reducedValue_of_invertible (X Z : Mat 4 ℝ) (y : Fin 3 → ℝ) [Invertible X] :
    reducedValue X Z y = X.det ^ 3 * (Z - phi y (X⁻¹).transpose).det := by
  sorry

/-- Step 3 (factorization) `p = det X · q`. Route: for invertible symmetric `X`,
`adjugate X = det X • X⁻¹`, `phi` is linear in its matrix argument, so
`matrixValue X Z y = det X ^ 4 * det (Z - phi y X⁻¹)` (`Matrix.det_smul`),
`= det X * reducedValue X Z y` by Step 2. So `(polynomial - detX * q) * detX`
vanishes at every real point; `MvPolynomial.funext` makes it zero; `detX ≠ 0`
and `MvPolynomial` is a domain. -/
theorem polynomial_eq_detX_mul_reduced : polynomial = detX * reducedPolynomial := by
  sorry

/-- Step 4. Route: `main_result` gives degree 20 homogeneity; `detX` is
homogeneous of degree 4; a factor of a homogeneous polynomial in a domain by a
nonzero homogeneous one is homogeneous. -/
theorem reducedPolynomial_isHomogeneous : reducedPolynomial.IsHomogeneous 16 := by
  sorry

/-- Step 5. Route: `RingHom.map_det`, `Matrix.fromBlocks_map`; `qMatrix 0 = 0`
kills the lower-left block; `Matrix.det_fromBlocks_zero₂₁`. -/
theorem reducedPolynomial_eval_basePoint :
    MvPolynomial.eval (coordinates basePoint) reducedPolynomial = 1 := by
  sorry

def reducedLinePolynomial (x : Ambient) : Polynomial ℝ :=
  MvPolynomial.eval₂ Polynomial.C
    (fun i => Polynomial.C (coordinates basePoint i) * Polynomial.X -
      Polynomial.C (coordinates x i)) reducedPolynomial

/-- Step 6. Route: map Step 3 along the line; roots of a factor are roots of the
product; `main_result` makes them real. -/
theorem reducedLinePolynomial_roots_real (x : Ambient) (z : ℂ)
    (hz : (reducedLinePolynomial x).aeval z = 0) : z.im = 0 := by
  sorry

def reducedCone : Set Ambient :=
  {x | ∀ t : ℂ, (reducedLinePolynomial x).aeval t = 0 → t.im = 0 ∧ 0 ≤ t.re}

/-- Step 7a (easy inclusion), from Step 3 on lines. -/
theorem cone_subset_reducedCone : cone ⊆ reducedCone := by
  sorry

/-- Step 7b (hard inclusion). Paper route: `q` is even in `y`, so its cone is
symmetric under `y ↦ -y`; by GÅRDING'S CONVEXITY THEOREM the midpoint
`(X, Z, 0)` is in the cone; at `y = 0`, `q = (det X)^3 det Z` forces `X ⪰ 0`;
and `cone = {X ⪰ 0} ∩ reducedCone`. Gårding's theorem (convexity of closed
hyperbolicity cones) is in neither Mathlib nor `OAI.Analysis.HyperbolicCones`;
it is the only substantial missing ingredient. -/
theorem reducedCone_subset_cone : reducedCone ⊆ cone := by
  sorry

/-- The corollary as stated in the paper (abstract headline object). -/
theorem reduced_corollary :
    reducedPolynomial.IsHomogeneous 16 ∧
    MvPolynomial.eval (coordinates basePoint) reducedPolynomial = 1 ∧
    (∀ (x : Ambient) (z : ℂ), (reducedLinePolynomial x).aeval z = 0 → z.im = 0) ∧
    reducedCone = cone ∧
    ∀ (N : ℕ) (_hN : 0 < N) (L : Ambient →ₗ[ℝ] Sym N),
      reducedCone ≠ {x | (L x : Mat N ℝ).PosSemidef} := by
  sorry
-- END BODY

end

end OAI.Paper256
