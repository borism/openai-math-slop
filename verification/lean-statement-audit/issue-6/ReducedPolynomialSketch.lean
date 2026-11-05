/-
UNCOMPILED SKETCH — not checked by Lean (no toolchain was available).
Purpose: a formalization plan for Corollary `cor:reduced` of
"A Nonspectrahedral Hyperbolicity Cone" (openai/math family 095,
preprints/A-Nonspectrahedral-Hyperbolicity-Cone-September-24-2026,
build/sections/reduced-polynomial.tex), on top of the existing Comparator
challenge `lean/ComparatorChallenges/HyperbolicCones.lean` (namespace
`OAI.Paper256`) and the existing solution `OAI.Analysis.HyperbolicCones`.

The abstract headlines this degree-16 polynomial q; the formalized
`main_result` is about the degree-20 polynomial p. Names below that are not
in the challenge are proposals; `sorry`s mark the proof obligations, each
annotated with the intended proof route.
-/
import ComparatorChallenges.HyperbolicCones

namespace OAI.Paper256

noncomputable section

open Matrix

/-- `K_i = !![0, e_iᵀ; -e_i, 0]` as a 4×4 matrix (paper, proof of cor:reduced). -/
def kMat {R : Type*} [CommRing R] (i : Fin 3) : Mat 4 R :=
  fun a b => Fin.cases (Fin.cases 0 (fun j => if j = i then 1 else 0) b)
    (fun a' => Fin.cases (if a' = i then -1 else 0) (fun _ => 0) b) a

/-- `C = (K₁ K₂ K₃)`, a 4 × 12 matrix with columns indexed by `Fin 3 × Fin 4`. -/
def cMat {R : Type*} [CommRing R] : Matrix (Fin 4) (Fin 3 × Fin 4) R :=
  fun a jb => kMat jb.1 a jb.2

/-- The 16 × 16 block matrix of eq. (reduced-polynomial):
`!![I₃ ⊗ X, Cᵀ; C (Q(y) ⊗ I₄), Z]`. -/
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

/-- Step 1 (block identity). `Φ_y(T) = C (Q(y) ⊗ T) Cᵀ` for every 4×4 `T`.
Route: `ext a b`; unfold `phi`, `cMat`, `kMat`; `simp [Matrix.mul_apply,
Matrix.kronecker, Fin.sum_univ_succ]`; `ring`. (Checked by hand in REPORT.md.) -/
theorem phi_eq_kron {R : Type*} [CommRing R] (y : Fin 3 → R) (T : Mat 4 R) :
    phi y T = cMat * Matrix.kronecker (qMatrix y) T * cMat.transpose := by
  sorry

/-- Step 2 (Schur complement). For invertible `X`,
`q = (det X)³ · det (Z - Φ_y(X⁻¹))`.
Route: `Matrix.det_fromBlocks₁₁` with `Invertible (1 ⊗ X)`,
`Matrix.det_kronecker` (det (1₃ ⊗ X) = det X ^ 3), mixed-product
`(Q ⊗ 1)(1 ⊗ X⁻¹) = Q ⊗ X⁻¹`, then `phi_eq_kron`. -/
theorem reducedValue_of_invertible (X Z : Mat 4 ℝ) (y : Fin 3 → ℝ) [Invertible X] :
    reducedValue X Z y = X.det ^ 3 * (Z - phi y X⁻¹).det := by
  sorry

/-- Step 3 (factorization) `p = det X · q` as polynomials.
Route: for invertible `X`, `adjugate X = det X • X⁻¹`, `phi` is linear in its
matrix argument, so `matrixValue X Z y = det X ^ 4 * det (Z - phi y X⁻¹)`
(`Matrix.det_smul`), which equals `det X * reducedValue X Z y` by Step 2.
Hence `(polynomial - detX * reducedPolynomial) * detX` vanishes at every real
point; `MvPolynomial.funext` (ℝ infinite) makes it zero, and `detX ≠ 0`
(evaluate at the base point) with `MvPolynomial` being a domain gives the
identity. No continuity argument is needed. -/
theorem polynomial_eq_detX_mul_reduced : polynomial = detX * reducedPolynomial := by
  sorry

/-- Step 4. `q` is homogeneous of degree 16.
Route: `main_result` gives `polynomial.IsHomogeneous 20`; `detX` is homogeneous
of degree 4 (`Matrix.det` of a matrix of degree-1 entries,
`MvPolynomial.IsHomogeneous.prod`/`det` lemma); in a domain, a factor of a
homogeneous polynomial by a nonzero homogeneous one is homogeneous
(compare top and bottom homogeneous components of each factor). -/
theorem reducedPolynomial_isHomogeneous : reducedPolynomial.IsHomogeneous 16 := by
  sorry

/-- Step 5. `q(e) = 1`. Route: `Q(0) = 0`, so the lower-left block vanishes and
`Matrix.det_fromBlocks_zero₂₁` gives `det (1 ⊗ 1) * det 1 = 1`. -/
theorem reducedPolynomial_eval_basePoint :
    MvPolynomial.eval (coordinates basePoint) reducedPolynomial = 1 := by
  sorry

/-- The line polynomial of `q`, as in the challenge. -/
def reducedLinePolynomial (x : Ambient) : Polynomial ℝ :=
  MvPolynomial.eval₂ Polynomial.C
    (fun i => Polynomial.C (coordinates basePoint i) * Polynomial.X -
      Polynomial.C (coordinates x i)) reducedPolynomial

/-- Step 6 (hyperbolicity). Every complex root of `t ↦ q(te - x)` is real.
Route: apply `MvPolynomial.eval₂` to Step 3: the challenge's `linePolynomial x`
equals `charpoly-like (det (t•1 - X)) * reducedLinePolynomial x`; a root of the
second factor is a root of the product, and `main_result` (or the existing
`linePolynomial_complex_roots_real`) makes it real. -/
theorem reducedLinePolynomial_roots_real (x : Ambient) (z : ℂ)
    (hz : (reducedLinePolynomial x).aeval z = 0) : z.im = 0 := by
  sorry

def reducedCone : Set Ambient :=
  {x | ∀ t : ℂ, (reducedLinePolynomial x).aeval t = 0 → t.im = 0 ∧ 0 ≤ t.re}

/-- Step 7a (easy inclusion). `cone ⊆ reducedCone`: roots of the factor are
roots of the product (Step 3 on lines). -/
theorem cone_subset_reducedCone : cone ⊆ reducedCone := by
  sorry

/-- Step 7b (hard inclusion). `reducedCone ⊆ cone`.
Paper route: `q` is even in `y` (`qMatrix (-y) = qMatrix y`), so the cone is
symmetric under `y ↦ -y`; by GÅRDING'S CONVEXITY THEOREM the midpoint
`(X, Z, 0)` lies in the cone; at `y = 0`, `q = (det X)^3 det Z`, forcing
`X ⪰ 0`; and `cone = {X ⪰ 0} ∩ reducedCone` (Step 3, the roots of
`det (t - X)` being the eigenvalues of `X`).
Formalization cost: Gårding's theorem (convexity of closed hyperbolicity
cones) is not in Mathlib and is not proved in `OAI.Analysis.HyperbolicCones`
(no `Convex ℝ cone` lemma exists there). It is the only nontrivial missing
ingredient; everything else is linear algebra on explicit matrices. -/
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
  sorry -- assemble Steps 4–7 with `main_result`

end

end OAI.Paper256
