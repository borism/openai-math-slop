# FAMILY 003: The quasi-Riemann hypothesis
SCOPE: The quasi-Riemann hypothesis asks for a fixed zero-free half-plane $\Re s>\theta$ with $\theta<1$. The formalization gives $\theta=7/8$ for the Riemann zeta function and every Dirichlet $L$-function, uniformly over all positive moduli and all characters. It also establishes the same bound for finite-order Hecke $L$-functions over $\mathbb Q(\sqrt{-3})$. The principal-character poles at $s=1$ are excluded in the Dirichlet and Hecke statements. The paper's later applications are not included. The formalized result gives a uniform logarithmic exclusion region for Landau–Siegel zeros. There is one constant $c>0$ such that every primitive nonprincipal real Dirichlet character of conductor $q\ge3$ and every real zero $0<\beta<1$ of its $L$-function satisfy $1-\beta\ge c/\log q$. Both character parities are included. No explicit value of $c$ is given. This excludes real zeros in $1-c/\log q<\be
## CHALLENGE QuasiRiemannHypothesis  targets=['OAI.riemannZeta_ne_zero_of_seven_eighths_lt_re'] defs=[]
theorem riemannZeta_ne_zero_of_seven_eighths_lt_re
    {s : ℂ} (hs : (7 / 8 : ℝ) < s.re) : riemannZeta s ≠ 0 := by
  sorry
DEFS(0): 
## CHALLENGE DirichletSevenEighths  targets=['OAI.DirichletCharacter.LFunction_ne_zero_of_seven_eighths_lt_re'] defs=[]
theorem LFunction_ne_zero_of_seven_eighths_lt_re
    {q : ℕ} [NeZero q] (χ : DirichletCharacter ℂ q) {s : ℂ}
    (hs : (7 / 8 : ℝ) < s.re) (hpole : ¬ (χ = 1 ∧ s = 1)) :
    _root_.DirichletCharacter.LFunction χ s ≠ 0 := by
  sorry
end DirichletCharacter
DEFS(0): 
## CHALLENGE HeckeSevenEighths  targets=['OAI.SevenEighths.HeckeFamily.LFunction_ne_zero_of_seven_eighths_lt_re'] defs=[]
theorem LFunction_ne_zero_of_seven_eighths_lt_re
    (χ : Character) {s : ℂ} (hs : (7 / 8 : ℝ) < s.re)
    (hpole : ¬ (χ.residue = 1 ∧ s = 1)) : LFunction χ s ≠ 0 := by sorry
end SevenEighths.HeckeFamily
end
DEFS(30): theorem rapid_product_sub, def product, theorem rapid_rescale, def rescale, def shiftedPair, theorem shiftedPair_k, theorem shiftedPair_f, theorem shiftedPair_differentiableAt, def scaledEvenPair, theorem scaledEvenPair_f_continuous, theorem scaledEvenPair_g_continuous, def rectangularPair, theorem rectangularPair_k, def xShift, def yShift, def parityPair, theorem locallyIntegrableOn_sum, def finitePair, def pair, def completed, def latticeL, abbrev K, abbrev O, def omega, def coordinateElement, structure Character, def elementCoeff, def coefficients, def continuedLattice, def LFunction
## CHALLENGE SiegelZeros  targets=['OAI.SiegelZeros.WeightedTorusJets.exists_absolute_real_zero_gap', 'OAI.SiegelZeros.WeightedTorusJets.dirichletRealZeroBound_proof'] defs=[]
theorem exists_absolute_real_zero_gap :
    ∃ c : ℝ, 0 < c ∧
      ∀ (q : ℕ) [NeZero q], 3 ≤ q →
      ∀ χ : DirichletCharacter ℂ q,
        χ.IsPrimitive → χ ≠ 1 → (∀ a : ZMod q, (χ a).im = 0) →
        ∀ β : ℝ, 0 < β → β < 1 → χ.LFunction (β : ℂ) = 0 →
          c ≤ (1 - β) * Real.log (q : ℝ) := by
  sorry
DEFS(1): theorem WeightedTorusJets.dirichletRealZeroBound_proof
## PAPER The-Quasi-Riemann-Hypothesis-September-30-2026
ABSTRACT: We prove that all finite-order Hecke $L$-functions over $\mathbb Q(\sqrt{-3})$ and all Dirichlet $L$-functions are zero-free in the half-plane $\Re s>7/8$, with the principal pole at $s=1$ allowed. In particular, the Riemann zeta function is zero-free in this half-plane, proving the quasi-Riemann hypothesis.
[theorem] \label{thm:main} Every finite-order Hecke $L$-function over $F=\mathbb Q(\sqrt{-3})$ has no zero in $\Re s>7/8$. The same holds for every Dirichlet $L$-function, including $\zeta(s)$. A pole at $s=1$ for a principal character is allowed.
## PAPER Uniform-exclusion-of-Landau-Siegel-zeros-October-1-2026
ABSTRACT: We prove the uniform exclusion of Landau--Siegel zeros. There is an absolute constant $c>0$ such that every real zero $\beta\in(0,1)$ of every primitive nonprincipal real Dirichlet $L$-function of conductor $q\ge3$ satisfies $(1-\beta)\log q\ge c$.
[theorem] \label{thm:main} There is an absolute constant $c>0$ such that every real zero $\beta\in(0,1)$ of every primitive nonprincipal real Dirichlet $L$-function of conductor $q\ge3$ satisfies \begin{equation}\label{eq:main} (1-\beta)\log q\ge c. \end{equation}
==================
# FAMILY 005: Irrationality of Catalan’s constant
SCOPE: The formalization proves that Catalan's constant $G=\sum_{j=0}^{\infty}(-1)^j/(2j+1)^2$ is irrational. This is the mathematical assertion in the paper's title.
## CHALLENGE Catalan  targets=['OAI.InternalCatalan.catalan_irrational'] defs=[]
theorem catalan_irrational :
    Irrational (∑' j : ℕ, (-1 : ℝ) ^ j / ((2 * j + 1 : ℕ) : ℝ) ^ 2) := by
  sorry
end InternalCatalan
DEFS(0): 
## PAPER Catalans-constant-is-irrational-September-24-2026
ABSTRACT: We prove that Catalan's constant $G=\sum_{j\geq0}(-1)^j/(2j+1)^2$ is irrational.
[theorem] \label{thm:main} Catalan's constant is irrational.
==================
# FAMILY 007: Ordinary two-point correlations and the corrected Elliott conjecture
SCOPE: The formalization proves ordinary two-point cancellation for multiplicative functions. For the Liouville function on every fixed pair of nonproportional affine forms, the correlation sum up to $X$ is $O(X/(\log X)^c)$ for an absolute $c>0$, with the implied constant depending on the forms. For two one-bounded multiplicative functions, if at least one is uniformly nonpretentious against all Dirichlet-character twists with frequency $|t|\le N$, then their shifted and nonproportional affine correlation sums divided by $N$ tend to zero. These are ordinary averages, with no logarithmic averaging.
## CHALLENGE OrdinaryElliott  targets=['OAI.OrdinaryCorrelations.binary_corrected_elliott'] defs=[]
theorem binary_corrected_elliott
    (f₁ f₂ : ℕ → ℂ) (hf₁ : OneBounded f₁) (hf₂ : OneBounded f₂)
    (hm₁ : Multiplicative f₁) (hm₂ : Multiplicative f₂)
    (hNP : UniformlyNonpretentious f₁ ∨ UniformlyNonpretentious f₂)
    (h₁ h₂ : ℕ) (hne : h₁ ≠ h₂) :
    Tendsto (shiftAverage f₁ f₂ h₁ h₂) atTop (nhds 0) := by
  sorry
end OrdinaryCorrelations
end
DEFS(6): def OneBounded, def Multiplicative, def distanceSq, def distance, def UniformlyNonpretentious, def shiftAverage
## CHALLENGE OrdinaryTwoPointCorrelations  targets=['OAI.OrdinaryTwoPointCorrelations.liouville_log_saving', 'OAI.OrdinaryTwoPointCorrelations.binary_corrected_elliott', 'OAI.OrdinaryTwoPointCorrelations.affine_corrected_elliott'] defs=[]
theorem liouville_log_saving :
    ∃ c : ℝ, 0 < c ∧ ∀ a₁ a₂ b₁ b₂ : ℕ,
      0 < a₁ → 0 < a₂ → a₁ * b₂ ≠ a₂ * b₁ →
      ∃ C : ℝ, 0 < C ∧ ∀ X : ℝ, 3 ≤ X →
        ‖affineSum liouville liouville a₁ a₂ b₁ b₂ ⌊X⌋₊‖ ≤
          C * X / Real.rpow (Real.log X) c := by
  sorry
theorem binary_corrected_elliott :
    ∀ f₁ f₂ : ℕ → ℂ, Multiplicative f₁ → Multiplicative f₂ →
      OneBounded f₁ → OneBounded f₂ →
      (UniformlyNonpretentious f₁ ∨ UniformlyNonpretentious f₂) →
      ∀ h₁ h₂ : ℕ, h₁ ≠ h₂ →
        Tendsto (fun N : ℕ => correlationSum f₁ f₂ h₁ h₂ N / (N : ℂ)) atTop (nhds 0) := by
  sorry
theorem affine_corrected_elliott :
    ∀ f₁ f₂ : ℕ → ℂ, Multiplicative f₁ → Multiplicative f₂ →
      OneBounded f₁ → OneBounded f₂ →
      (UniformlyNonpretentious f₁ ∨ UniformlyNonpretentious f₂) →
      ∀ a₁ a₂ b₁ b₂ : ℕ, 0 < a₁ → 0 < a₂ → a₁ * b₂ ≠ a₂ * b₁ →
        Tendsto (fun N : ℕ => affineSum f₁ f₂ a₁ a₂ b₁ b₂ N / (N : ℂ)) atTop (nhds 0) := by
  sorry
end OrdinaryTwoPointCorrelations
end
DEFS(9): def liouville, def correlationSum, def affineSum, def Multiplicative, def OneBounded, def primesUpTo, def squaredDistance, def characterTwist, def UniformlyNonpretentious
## PAPER Ordinary-two-point-correlations-of-multiplicative-functions-September-24-2026
ABSTRACT: We prove the ordinary two-point Chowla conjecture. For every fixed pair of nonproportional affine forms, the Liouville correlation has a power-of-logarithm saving at every cutoff, with an absolute exponent. We also prove the binary corrected Elliott conjecture for ordinary averages of complex multiplicative functions of modulus at most one, under uniform nonpretentiousness of at least one original factor. This qualitative conclusion holds in fixed residue classes and for fixed nonproportional affine forms.
[theorem[A logarithmic saving for affine Liouville correlations]] \label{thm:q-affine} There is an absolute constant \(c>0\) such that, for every fixed choice of integers \(a_1,a_2\ge1\) and \(b_1,b_2\ge0\) with \(a_1b_2-a_2b_1\ne0\), there is a constant \(C_{a_1,a_2,b_1,b_2}\) for which \[ \left|\sum_{1\le n\le X} \lambda(a_1n+b_1)\lambda(a_2n+b_2)\right| \le C_{a_1,a_2,b_1,b_2}\frac{X}{(\log X)^c} \qquad(X\ge3). \] The cutoff \(X\) may be any real number. No coprimality condition is imposed on the coefficients.
==================
# FAMILY 008: The Deligne–Drinfeld conjecture
SCOPE: The Deligne–Drinfeld conjecture predicts that the rational Grothendieck–Teichmüller Lie algebra is freely generated by one element in each odd weight $3,5,7,\ldots$. The formalization establishes this for the rational solution space of antisymmetry, the three-term equation, and the four-strand pentagon with the Ihara bracket. It also gives the corresponding continuous isomorphism after completion by weight. The regularized-transport proposition and graph-complex consequences are not included.
## CHALLENGE DeligneDrinfeld  targets=['OAI.DeligneDrinfeld.main'] defs=[]
theorem main : MainStatement := by
  sorry
end DeligneDrinfeld
end
DEFS(31): abbrev L, def x, def y, def eval, abbrev Edge, abbrev BraidFree, def chord, def braidRelations, def braidIdeal, abbrev T4, def t, def IsSolution, def W, structure Tangent, def Tangent.equiv, def tangentLift, def D, def ihara, inductive WeightedWord, def weightPiece, abbrev OddFree, def oddWeight, abbrev Fn, abbrev Ln, abbrev Wn, def Graded, abbrev OddCompletion, abbrev WCompletion, def completed, def completedInv
## PAPER The-Deligne-Drinfeld-conjecture-September-23-2026
ABSTRACT: We prove the Deligne--Drinfeld conjecture: the rational Grothendieck--Teichm\"uller Lie algebra is freely generated by one element in every odd weight at least three, with the corresponding isomorphism after weight completion.
[theorem] \label{thm:main} There are homogeneous elements \(\sigma_{2k+1}\in W_{2k+1}\), one for each \(k\ge1\), for which \[ \Lie_{\Q}\langle e_3,e_5,e_7,\ldots\rangle \longrightarrow (W,\{\, ,\,\}),\qquad e_{2k+1}\longmapsto\sigma_{2k+1}, \] is an isomorphism of graded Lie algebras. In particular, \(W\) is closed under the bracket \eqref{eq:ihara}. The induced map on completions by weight is a continuous graded isomorphism.
==================
# FAMILY 009: Function-field reconstruction from Milnor K-theory and Galois data
SCOPE: The Bogomolov–Pop reconstruction conjecture concerns recovering a function field and its constants from pro-$\ell$ abelian-by-central Galois data. The linked formalization proves injectivity of the reconstruction correspondence for function fields of transcendence degree at least two over algebraically closed fields of characteristic different from the prime $\ell$. If two isomorphisms of perfect closures preserving the constant fields induce the same Galois-data isomorphism modulo $\ell$-adic unit scaling, then they agree modulo Frobenius. The selected statement proves this uniqueness; existence of a field isomorphism for every admissible Galois-data isomorphism is outside it.
## CHALLENGE BogomolovPopInjectivity  targets=['OAI.BogomolovPop.main_graph_injective'] defs=[]
theorem main_graph_injective (ell : ℕ) [Fact ell.Prime]
    (k K l L : Type*) [Field k] [Field K] [Field l] [Field L]
    [IsAlgClosed k] [IsAlgClosed l] [Algebra k K] [Algebra l L]
    [Algebra.EssFiniteType k K] [Algebra.EssFiniteType l L]
    (hk : (ell : k) ≠ 0) (hl : (ell : l) ≠ 0)
    (hK : 2 ≤ Algebra.trdeg k K) (hL : 2 ≤ Algebra.trdeg l L) :
    ∀ (a a' : IsomF k K l L) (b : IsomCUnits ell K L),
      PhiGraph a b → PhiGraph a' b → a = a'  := by
  sorry
end BogomolovPop
end
DEFS(26): def proEllKernel, instance proEllKernel_normal, abbrev ProEll, def closedGammaThree, instance closedGammaThree_normal, abbrev PiA, abbrev PiC, theorem closedGammaThree_le, def centralProjection, abbrev Delta, def sourceCommutator, def abelianLift, theorem abelianLift_spec, def bracket, def BracketCompatible, abbrev PerfectFieldClosure, def PerfectIsom, def FrobeniusStep, abbrev IsomF, abbrev IsomC, def ScalarStep, abbrev IsomCUnits, def absoluteToPiA, def absoluteAction, def PullbackGraph, def PhiGraph
## PAPER The-Bogomolov-Pop-reconstruction-theorem-September-23-2026
ABSTRACT: We prove the Bogomolov--Pop reconstruction conjecture for function fields of transcendence degree at least two over arbitrary algebraically closed fields of characteristic different from $\ell$. The pro-$\ell$ abelian-by-central datum determines the perfect closure and its constant field, with precisely the Frobenius and $\ell$-adic unit ambiguities.
[theorem[Bogomolov--Pop reconstruction]] \label{thm:main} Let $k$ and $l$ be arbitrary algebraically closed fields of characteristics different from $\ell$, and let $K/k$ and $L/l$ be function fields with $\trdeg(K/k),\trdeg(L/l)\ge2$. Then \[ \Phi_{K,L}:\Isom_F^i(K,L)\longrightarrow \Isom^c(\Pi_L^a,\Pi_K^a)/\Zell^\times, \qquad [\alpha]\longmapsto[\alpha^*], \] is a bijection.
==================
# FAMILY 012: Independent largest prime factors of consecutive integers
SCOPE: Let $P^+(n)$ be the largest prime factor of $n$. The formalization proves the joint Dickman law in ordinary natural density: for every $0<a,b<1$, the density of integers satisfying $P^+(n)\le n^a$ and $P^+(n+1)\le n^b$ tends to $\rho(1/a)\rho(1/b)$, where $\rho$ is the Dickman function. It also proves that each of the orderings $P^+(n)<P^+(n+1)$ and $P^+(n+1)<P^+(n)$ has natural density $1/2$.
## CHALLENGE JointDickman  targets=['OAI.JointDickmanPaper.joint_law', 'OAI.JointDickmanPaper.increasing_order', 'OAI.JointDickmanPaper.decreasing_order'] defs=[]
theorem joint_law (a b : ℝ) (ha : 0 < a) (ha1 : a < 1) (hb : 0 < b) (hb1 : b < 1) :
    Tendsto (realDensity (fun n =>
      (n.maxPrimeFac : ℝ) ≤ (n : ℝ) ^ a ∧ ((n + 1).maxPrimeFac : ℝ) ≤ (n : ℝ) ^ b))
      atTop (𝓝 (Erdos970.NumberTheoryLean.Dickman.rho (1 / a) *
        Erdos970.NumberTheoryLean.Dickman.rho (1 / b))) := by
  sorry
/-- Corollary 2: the increasing strict ordering has natural density one half. -/
theorem increasing_order :
    Tendsto (realDensity (fun n => n.maxPrimeFac < (n + 1).maxPrimeFac))
      atTop (𝓝 (1 / 2)) := by
  sorry
/-- The reverse strict ordering also has natural density one half. -/
theorem decreasing_order :
    Tendsto (realDensity (fun n => (n + 1).maxPrimeFac < n.maxPrimeFac))
      atTop (𝓝 (1 / 2)) := by
  sorry
end JointDickmanPaper
DEFS(6): def kernel, def stepApprox, def delay, def rho, def empiricalCount, def realDensity
## PAPER The-joint-Dickman-law-for-consecutive-integers-September-24-2026
ABSTRACT: Let $P^+(n)$ denote the largest prime factor of $n$. We prove that $\log P^+(n)/\log n$ and $\log P^+(n+1)/\log n$ are asymptotically independent in ordinary natural density, with Dickman marginals. This resolves the Erd\H{o}s--Pomerance joint Dickman conjecture positively and implies that the ordering $P^+(n)<P^+(n+1)$ has natural density $1/2$.
[theorem[Joint Dickman law]] \label{thm:main} For every fixed $a,b\in(0,1)$, \[ \lim_{X\to\infty}\frac1X \#\{2\leq n\leq X:\Pplus(n)\leq n^a, \ \Pplus(n+1)\leq n^b\} =\rho(1/a)\rho(1/b). \] Here the limit is taken over all real $X$, with ordinary, unweighted counting.
==================
# FAMILY 013: Ostmann’s inverse Goldbach conjecture
SCOPE: The formalization proves Ostmann's inverse Goldbach conjecture. For any two sets $A,B$ of nonnegative integers, each containing at least two elements, the symmetric difference between their sumset $A+B$ and the set of primes is infinite. Thus no set differing from the primes by only finitely many elements can be decomposed as such a sumset. The linked statements include the full result and its two-infinite-summands case.
## CHALLENGE OstmannComplete  targets=['OAI.Ostmann.inverseGoldbach', 'OAI.Ostmann.twoInfiniteSummandsImpossible'] defs=[]
theorem inverseGoldbach : InverseGoldbach := by
  sorry
theorem twoInfiniteSummandsImpossible : TwoInfiniteSummandsImpossible := by
  sorry
end Ostmann
DEFS(5): def primes, abbrev sumset, def EventuallyPrimeSumset, def TwoInfiniteSummandsImpossible, def InverseGoldbach
## CHALLENGE OstmannPrimes  targets=['OAI.Ostmann.main'] defs=[]
theorem main : ∀ A B : Set ℕ, A.Nontrivial → B.Nontrivial →
    Set.Infinite ((A + B) ∆ {n : ℕ | Nat.Prime n}) := by
  sorry
end Ostmann
DEFS(0): 
## PAPER the-additive-indecomposability-of-the-primes-September-24-2026
ABSTRACT: We prove Ostmann's inverse Goldbach conjecture: no set differing from the primes by finitely many elements can be written as $A+B$, where $A$ and $B$ are sets of nonnegative integers with at least two elements each.
[theorem[Ostmann's conjecture]] \label{cor:ostmann} If $A,B\subseteq\N_0$ satisfy $|A|,|B|\ge2$, then $(A+B)\mathbin{\triangle}\mathcal P$ is infinite. Equivalently, every finite modification of $\mathcal P$ is additively indecomposable into two sets with at least two elements each.
==================
# FAMILY 015: Torus-packet equidistribution in prime, quartic, and sextic degrees
SCOPE: The formalization proves equidistribution of volume-weighted torus packets for totally real number fields of every fixed prime degree at least five. For any sequence of full lattices whose multiplier-order discriminants tend to infinity, the packet measures converge weakly to Haar probability measure and form a tight family, so no mass escapes. Arbitrary local homothety types are allowed, and the fields may vary along the sequence.
## CHALLENGE DukePrimeDegree  targets=['OAI.DukePrimeDegree.prime_degree_packet_measure_equidistribution_unconditional', 'OAI.DukePrimeDegree.prime_degree_packet_measures_tendsto_haar_unconditional'] defs=[]
theorem prime_degree_packet_measure_equidistribution_unconditional
    (d : ℕ) (hprime : Nat.Prime (d+1)) (hfive : 5 ≤ d+1)
    (K : ℕ → Type u) [∀ i, Field (K i)] [∀ i, NumberField (K i)]
    [∀ i, NumberField.IsTotallyReal (K i)]
    (M : ∀ i, PrimeDegreePackets.FullLattice (d+1) (K i))
    (σ : ∀ i, OrderedEmbeddings (d+1) (K i))
    (hn : ∀ i, Module.finrank ℚ (K i)=d+1)
    (hD : Tendsto (fun i => PrimeDegreePackets.multiplierDiscriminant (M i)) atTop atTop) :
    ∃ ν : Measure (X (d+1)), IsHaarProbability ν ∧
      WeakProbabilityConvergence (fun i => packetMeasure (M i) (σ i)) ν ∧
      IsTightMeasureSet (Set.range (fun i => packetMeasure (M i) (σ i))) := by
  sorry
/-- The complete packet measures converge weakly to any specified Haar
probability, in the formulation by bounded continuous test functions. -/
theorem prime_degree_packet_measures_tendsto_haar_unconditional
    (d : ℕ) (hprime : Nat.Prime (d+1)) (hfive : 5 ≤ d+1)
    (K : ℕ → Type u) [∀ i, Field (K i)] [∀ i, NumberField (K i)]
    [∀ i, NumberField.IsTotallyReal (K i)]
    (M : ∀ i, PrimeDegreePackets.FullLattice (d+1) (K i))
    (σ : ∀ i, OrderedEmbeddings (d+1) (K i))
    (hn : ∀ i, Module.finrank ℚ (K i)=d+1)
    (hD : Tendsto (fun i => PrimeDegreePackets.multiplierDiscriminant (M i)) atTop atTop)
    (m : ProbabilityMeasure (X (d+1)))
    (hm : IsHaarProbability (m : Measure (X (d+1)))) :
    WeakProbabilityConvergence (fun i => packetMeasure (M i) (σ i))
      (m : Measure (X (d+1))) := by
  sorry
end DukePrimeDegree
DEFS(38): abbrev G, def integralGroup, abbrev X, instance xMeasurableSpace, instance xBorelSpace, def rightAction, theorem rightAction_one, theorem rightAction_mul, def signMatrices, def rowLattice, structure FullLattice, def multiplierOrder, def integralElements, def multiplierDiscriminant, abbrev OrderedEmbeddings, def embeddingMatrix, def normalizedLattice, def latticePoint, abbrev LogCoordinates, def diagonalFlow, theorem diagonalFlow_zero, theorem diagonalFlow_add, def orbitMap, theorem orbitMap_zero, theorem orbitMap_add, def periodGroup, def diagonalOrbit, def orbitVolume, def orbitalHaar, def orbitProbability
## PAPER Equidistribution-of-Prime-Degree-Torus-Packets-with-Arbitrary-Local-Type-September-24-2026
ABSTRACT: We prove the packet form of the higher-dimensional Duke equidistribution problem for totally real fields of any fixed prime degree at least five, allowing arbitrary local homothety types of full lattices. As the multiplier-order discriminant tends to infinity, the volume-weighted packet measures converge to Haar probability measure, with no escape of mass.
[theorem] \label{thm:main} For every fixed prime $n\ge5$ and every sequence $(K_i,M_i,\sigma_i)$ as above with \mbox{$D(M_i)\to\infty$}, \[ \mu_{K_i,M_i,\sigma_i}\longrightarrow m_n. \] The convergence is weak convergence of probability measures. In particular, it holds against every continuous compactly supported function, and no mass escapes into the cusp.
==================
# FAMILY 017: The irrationality exponent of <i>π</i> is 2
SCOPE: The formalization proves that the irrationality exponent of $\pi$ is exactly two. For every $\nu>2$, all sufficiently large positive denominators $q$ satisfy $|\pi-p/q|\ge q^{-\nu}$ for every integer numerator $p$. It also states the exact supremum characterization using infinitely many rational approximations. The paper's convergence consequence for the Flint–Hills series is outside this selected statement.
## CHALLENGE PiExponent  targets=['OAI.PiExponent.main'] defs=[]
theorem main :
  (∀ ν : ℝ, 2 < ν → ∃ Q : ℤ, 2 ≤ Q ∧
    ∀ p q : ℤ, Q ≤ q →
      (q : ℝ) ^ (-ν) ≤ |Real.pi - (p : ℝ) / (q : ℝ)|) ∧
  sSup {ν : ℝ | 0 < ν ∧
    Set.Infinite {r : ℚ | 2 ≤ r.den ∧
      0 < |Real.pi - (r : ℝ)| ∧
      |Real.pi - (r : ℝ)| < (r.den : ℝ) ^ (-ν)}} = 2 := by
  sorry
end PiExponent
DEFS(0): 
## PAPER The-irrationality-exponent-of-pi-is-2-September-24-2026
ABSTRACT: We prove the conjecture that the irrationality exponent of \(\pi\) is \(2\). As a consequence, the classical Flint--Hills series \(\sum_{n\ge1}1/(n^3\sin^2 n)\) converges, with angles in radians.
[theorem] \label{thm:main} The irrationality exponent of \(\pi\) is \(2\). More precisely, for every real \(\nu>2\), there is an integer \(Q(\nu)\) such that \[ \left|\pi-\frac pq\right|\ge q^{-\nu} \qquad(p\in\ZZ,\ q\in\ZZ,\ q\ge Q(\nu)). \]
==================
# FAMILY 020: Squarefree quartics and power-free polynomial values
SCOPE: The formalized result proves positive-density power-free values for every integer polynomial $f$ irreducible over $\mathbb Q$ of degree $d\ge4$. Put $k=d-2$ and assume no prime $k$th power divides every value of $f$. Then the number of positive integers $n\le X$ for which $f(n)$ is $k$-free is $c_fX+o_f(X)$, where $c_f>0$ is the convergent product of local factors. Negative values are allowed and zero is excluded. No monicity, primitivity, or coefficient-height restriction is imposed.
## CHALLENGE PowerFreeValues  targets=['OAI.QuarticPowerFree.allDegrees'] defs=[]
theorem allDegrees (f : Polynomial ℤ)
    (hirr : Irreducible (f.map (Int.castRingHom ℚ)))
    (hdeglo : 4 ≤ f.natDegree)
    (hlocal : LocallyAdmissible f (f.natDegree - 2)) :
    DensityStatement f (f.natDegree - 2) := by
  sorry
end QuarticPowerFree
DEFS(7): def PowerFree, def rho, def count, def LocallyAdmissible, def localFactor, def densityConstant, def DensityStatement
## PAPER Squarefree-values-of-quartics-and-power-free-values-of-polynomials-September-24-2026
ABSTRACT: We prove that every irreducible integer quartic with no fixed prime-square divisor takes squarefree values with the predicted positive Euler-product density. More generally, we obtain the corresponding $(d-2)$-power-free density in degrees $4\le d\le8$. The proof combines number-field factorization, determinant estimates with adaptive auxiliary primes, and explicit low-degree geometry. Together with Browning's theorem for higher degrees, this gives the $(d-2)$-power-free density for every $d\ge4$.
[theorem] \label{thm:density} Let $f\in\Z[x]$ be irreducible over $\Q$, of degree $d$ with $4\le d\le8$, and put $k=d-2$. If \eqref{eq:local-admissibility} holds, then \[ S_{f,k}(X)=c_{f,k}X+o_f(X),\qquad c_{f,k}=\prod_p\left(1-\frac{\rho_f(p^k)}{p^k}\right)>0. \] No primitivity or sign condition on the leading coefficient is required.
==================
# FAMILY 021: A quadratic bound for Jacobsthal’s function
SCOPE: Let $h(k)$ be the least interval length that guarantees an integer coprime to any prescribed positive modulus with at most $k$ distinct prime factors. The formalization proves the paper's strengthened Jacobsthal bound $h(k)\le Ck^2/(\log\log(3k))^2$ for one absolute $C>0$ and every $k\ge1$. Intervals may begin at any signed integer. The earlier quadratic bound is also retained as a separate statement; the optimal order of growth is not determined.
## CHALLENGE Jacobsthal  targets=['OAI.Erdos970.Erdos970Final.erdos_970_quadratic'] defs=[]
theorem erdos_970_quadratic : NumberTheoryLean.Targets.JacobsthalQuadratic := by
  sorry
end Erdos970Final
end Erdos970
DEFS(2): def IsJacobsthalBound, def JacobsthalQuadratic
## CHALLENGE JacobsthalImproved  targets=['OAI.Erdos970.Erdos970Final.erdos_970_iterated_log'] defs=[]
theorem erdos_970_iterated_log : NumberTheoryLean.Targets.JacobsthalIteratedLog := by
  sorry
end Erdos970Final
end Erdos970
DEFS(2): def IsJacobsthalBound, def JacobsthalIteratedLog
## PAPER A-quadratic-bound-for-Jacobsthals-function-September-25-2026
ABSTRACT: Let $h(k)$ be the least integer such that every interval of $h(k)$ consecutive integers contains an integer coprime to any prescribed positive integer having at most $k$ distinct prime divisors. We prove $h(k)\ll k^2/(\log\log(3k))^2$, giving an affirmative answer to Jacobsthal's quadratic-bound question.
[theorem] \label{thm:main} There is an absolute constant $C>0$ such that \[ h(k)\le C\frac{k^2}{(\log\log(3k))^2} \qquad\text{for every integer }k\ge1. \]
==================
# FAMILY 023: Patterson's first moment for cubic Gauss sums
SCOPE: Patterson's first-moment conjecture concerns the average of normalized cubic Gauss sums over primary Eisenstein primes. The formalization proves the sharp-cutoff asymptotic with main term $\frac65c_*X^{5/6}/\log X$, where $c_*=(2\pi)^{2/3}/(3\Gamma(2/3))$. It also proves the corresponding angular comparison for every integer Fourier mode and cancellation of order $o(X^{5/6}/\log X)$ for each fixed nonzero mode. All primary Eisenstein primes are included, without an extra conjectural premise.
## CHALLENGE PattersonFirstMoment  targets=['OAI.CubicFirstMoment.patterson_firstMoment', 'OAI.CubicFirstMoment.patterson_angularComparison', 'OAI.CubicFirstMoment.patterson_angularCancellation'] defs=[]
theorem patterson_firstMoment : FirstMomentStatement := by
  sorry
/-- Model comparison in every fixed integer angular mode. -/
theorem patterson_angularComparison : AngularComparisonStatement := by
  sorry
/-- Cancellation at the first-moment scale for each nonzero angular mode. -/
theorem patterson_angularCancellation : AngularCancellationStatement := by
  sorry
end CubicFirstMoment
end
end
DEFS(21): def omega, def eisensteinRing, abbrev Eisenstein, def omegaE, def norm, def normNat, def primary, def primaryPrime, def modulus, abbrev Residues, def residueRepresentative, def cubicSymbolAtPrime, def additivePhase, def gaussAtPrime, def cStar, def primeCutoffSum, def firstMomentScale, def FirstMomentStatement, def theta, def AngularComparisonStatement, def AngularCancellationStatement
## PAPER An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026
ABSTRACT: We prove Patterson's first-moment conjecture for normalized cubic Gauss sums over all primary Eisenstein primes, unconditionally. The sharp-cutoff main term is $(6/5)c_*X^{5/6}/\log X$, where $c_*=(2\pi)^{2/3}/(3\Gamma(2/3))$. For every fixed nonzero angular Fourier mode of the prime argument, we also prove cancellation at the first-moment scale.
[theorem[First moment over primary primes]] \label{thm:main} As $X\longrightarrow\infty$, \begin{equation}\label{eq:main} \sum_{\substack{N\pi\le X\\\pi\equiv1\pmod3\ \mathrm{prime}}}G(\pi) =\frac65c_*\frac{X^{5/6}}{\log X} +o\!\left(\frac{X^{5/6}}{\log X}\right). \end{equation} The sum is over all primary primes in $\mathcal O$.
==================
# FAMILY 024: An asymptotic formula for the number of totients
SCOPE: Let $V(x)$ count the distinct values of Euler's totient function up to $x$. The formalization constructs the paper's explicit positive main term from finite arithmetic approximants and proves that their ratio tends to one. In particular, $V(cx)/V(x)\to c$ for every fixed $c>0$, answering the Erdős–Hall regular-variation question. The formalization also gives asymptotics for totients $v\le x$ whose least preimage $\ell(v)=\min\{n\ge1:\varphi(n)=v\}$ lies between $kx$ and $(k+1)x$. The associated coefficient is positive under the stated existence condition; when no totient $d$ satisfies $kd<\ell(d)$, the count and coefficient are identically zero. The cases $k=1,2$ have positive coefficients.
## CHALLENGE TotientAsymptotic  targets=['OAI.TotientAsymptotic.totient_asymptotic_formula', 'OAI.TotientAsymptotic.weighted_totient_asymptotic', 'OAI.TotientAsymptotic.weighted_totient_one_two', 'OAI.TotientAsymptotic.coefficient_nonnegative'] defs=[]
theorem totient_asymptotic_formula
    :
    TendstoUniformlyOn (fun H => AH H (fun _ => 1)) (A (fun _ => 1))
      atTop (Set.Ico (0 : ℝ) 1) ∧
    (∃ cMinus cPlus : ℝ, 0 < cMinus ∧ ∀ s ∈ Set.Ico (0 : ℝ) 1,
      cMinus ≤ A (fun _ => 1) s ∧ A (fun _ => 1) s ≤ cPlus) ∧
    Tendsto (fun x => V x/mainTerm x) atTop (nhds 1) ∧
    ∀ c : ℝ, 0 < c → Tendsto (fun x => V (c*x)/V x) atTop (nhds c) := by
  sorry
theorem weighted_totient_asymptotic
    (k : ℕ) (hk : 1≤k) :
    TendstoUniformlyOn (fun H => AH H (fk k)) (A (fk k)) atTop (Set.Ico (0 : ℝ) 1) ∧
    Tendsto (fun x => normalizedCount (N k) x-A (fk k) (theta x)) atTop (nhds 0) ∧
    ((∃ d : ℕ, IsTotient d ∧ k*d<ell d) →
      ∃ cMinus cPlus : ℝ, 0<cMinus ∧ 0<cPlus ∧
        (∀ s∈Set.Ico (0 : ℝ) 1, cMinus≤A (fk k) s ∧ A (fk k) s≤cPlus) ∧
        Tendsto (fun x => N k x/(tupleNormalization x*A (fk k) (theta x))) atTop (nhds 1) ∧
        ∀ᶠ x : ℝ in atTop, (cMinus/cPlus)*V x≤N k x ∧ N k x≤V x) ∧
    ((¬∃ d : ℕ, IsTotient d ∧ k*d<ell d) →
      (∀ x : ℝ, 0<x → N k x=0) ∧ (∀ s∈Set.Ico (0 : ℝ) 1, A (fk k) s=0)) := by
  sorry
theorem weighted_totient_one_two
    :
    ∀ k∈({1,2} : Finset ℕ), ∃ c : ℝ, 0<c ∧
      ∀ s∈Set.Ico (0 : ℝ) 1, c≤A (fk k) s := by
  sorry
theorem coefficient_nonnegative (H : ℕ) {s : ℝ}
    (hs : s ∈ Set.Ico (0 : ℝ) 1) : 0 ≤ AH H (fun _ => 1) s := by
  sorry
end TotientAsymptotic
end
DEFS(32): def IsTotient, def V, def ell, def a, def RenewalRootSet, def rho, def lam, def gamma, def g, def B, def psi, def m, def theta, def G, def P, def alpha, def largestPrimeFactor, structure TailDatum, def tailPrime, def tailLog, def IsWitness, def w, def witnesses, def D, def maxD, def AH, def A, def mainTerm, def N, def fk
## CHALLENGE TotientCompanionZero  targets=['OAI.TotientAsymptotic.companion_zero_case'] defs=[]
theorem companion_zero_case (k : ℕ) (_hk : 0 < k)
    (hno : ¬ ∃ d : ℕ, IsTotient d ∧ k*d < ell d) :
    (∀ x : ℝ, 0 < x → N k x = 0) ∧
    (∀ s ∈ Set.Ico (0 : ℝ) 1, A (fk k) s = 0) := by
  sorry
end TotientAsymptotic
end
DEFS(22): def IsTotient, def ell, def a, def RenewalRootSet, def rho, def lam, def gamma, def P, def alpha, def largestPrimeFactor, structure TailDatum, def tailPrime, def tailLog, def IsWitness, def w, def witnesses, def D, def maxD, def AH, def A, def N, def fk
## PAPER An-asymptotic-formula-for-the-number-of-totients-September-25-2026
ABSTRACT: Let $V(x)$ count the distinct values of Euler's totient function up to~$x$. We give an explicit asymptotic equivalent for $V(x)$. Its coefficient is a uniform limit of functions defined from finite arithmetic data. We also prove that $V(cx)/V(x)\to c$ as $x\to\infty$ for every fixed $c>0$, answering a question of Erd\H{o}s and Hall.
[theorem] \label{thm:main} For sufficiently large positive integers $H$, there are nonnegative functions $A_H(1;\cdot):[0,1)\to\mathbb R$, given by the finite arithmetic formula \eqref{eq:AH} below, which converge uniformly as $H\to\infty$ to a function $A(1;\cdot)$ satisfying \[ 0<\inf_{0\le s<1}A(1;s) \le\sup_{0\le s<1}A(1;s)<\infty. \] With the parameters \eqref{eq:renewal}--\eqref{eq:Gj}, \[ V(x)\sim\frac{x}{\log x}\,G_m A(1;\theta). \] Moreover, for every fixed real $c>0$, \[ \frac{V(cx)}{V(x)}\longrightarrow c. \]
==================
# FAMILY 025: Short Egyptian fractions
SCOPE: An Egyptian-fraction expansion writes a rational number as a sum of distinct unit fractions. The formalization proves that every $a/b$ with $1\le a<b$ has such an expansion and that the largest minimum length at denominator $b$ is $\Theta(\log\log b)$. If $F(k)$ counts exact $k$-term expansions of $1$, it also proves $\log\log F(k)=\Theta(k)$ and bounds every denominator in such an expansion. Every integer $m\ge2$ occurs as a denominator in an expansion of $1$, with length eventually at most $(257/\log2+\varepsilon)\log\log m$ for every $\varepsilon>0$; padding can preserve that denominator. If $v(k)$ is the least integer at least $2$ absent from all exact $k$-term expansions of $1$, then eventually $e^{e^{k/600}}\le v(k)\le1+k^{2^{k-1}}$, and $\liminf_{k\to\infty}\log\log v(k)/k\ge\log2/257$.
## CHALLENGE EgyptianFractions  targets=['OAI.Problem337.egyptian_length_is_minimum', 'OAI.Problem337.main_double_log_order', 'OAI.Problem337.one_expansions_finite_and_bounded', 'OAI.Problem337.counting_double_log_order', 'OAI.Problem337.exact_marker_padding', 'OAI.Problem337.every_exact_marker_occurs', 'OAI.Problem337.quantitative_marked_length', 'OAI.Problem337.missing_denominator_semantics', 'OAI.Problem337.prescribed_denominator_corollary'] defs=[]
theorem egyptian_length_is_minimum :
    ∀ a b : ℕ, 1 ≤ a → a < b →
  (∃ n : Fin (egyptianLength a b) → ℕ,
    IsEgyptianExpansion ((a : ℚ) / (b : ℚ)) n) ∧
  (∀ k : ℕ, (∃ n : Fin k → ℕ,
    IsEgyptianExpansion ((a : ℚ) / (b : ℚ)) n) →
    egyptianLength a b ≤ k) := by
  sorry
theorem main_double_log_order :
    ∃ c1 c2 : ℝ, 0 < c1 ∧ 0 < c2 ∧ ∃ b0 : ℕ,
  ∀ b : ℕ, b0 ≤ b →
    c1 * Real.log (Real.log (b : ℝ)) ≤ (maxEgyptianLength b : ℝ) ∧
    (maxEgyptianLength b : ℝ) ≤ c2 * Real.log (Real.log (b : ℝ)) := by
  sorry
theorem one_expansions_finite_and_bounded :
    (∀ k : ℕ, Set.Finite (OneExpansions k) ∧
    F k ≤ k ^ (2 ^ k - 1)) ∧
  (∀ k : ℕ, ∀ n : Fin k → ℕ, IsOneExpansion n →
    ∀ i : Fin k, n i ≤ k ^ (2 ^ i.val)) := by
  sorry
theorem counting_double_log_order :
    ∃ c C : ℝ, 0 < c ∧ 0 < C ∧ ∃ k0 : ℕ,
  ∀ k : ℕ, k0 ≤ k →
    c * (k : ℝ) ≤ Real.log (Real.log (F k : ℝ)) ∧
    Real.log (Real.log (F k : ℝ)) ≤ C * (k : ℝ) := by
  sorry
theorem exact_marker_padding :
    ∀ r : ℕ, 3 ≤ r → ∀ n : Fin r → ℕ, IsOneExpansion n →
  ∀ m : ℕ, (∃ i : Fin r, n i = m) →
    ∃ n' : Fin (r + 1) → ℕ,
      IsOneExpansion n' ∧ ∃ i : Fin (r + 1), n' i = m := by
  sorry
theorem every_exact_marker_occurs :
    ∀ m : ℕ, 2 ≤ m → ∃ k : ℕ, m ∈ D k := by
  sorry
theorem quantitative_marked_length :
    ∀ ε : ℝ, 0 < ε → ∃ mε : ℕ, 2 ≤ mε ∧
  ∀ m : ℕ, mε ≤ m →
    ∃ k : ℕ, ∃ n : Fin k → ℕ,
      IsOneExpansion n ∧
      (∃ i : Fin k, n i = m) ∧
      (k : ℝ) ≤ (257 / Real.log 2 + ε) * Real.log (Real.log (m : ℝ)) := by
  sorry
theorem missing_denominator_semantics :
    ∀ k : ℕ,
  Set.Finite (D k) ∧
  (∃ m : ℕ, m ∈ missingDenominators k) ∧
  2 ≤ v k ∧ v k ∉ D k ∧
  (∀ m : ℕ, 2 ≤ m → m < v k → m ∈ D k) ∧
  (1 ≤ k → v k ≤ 1 + k ^ (2 ^ (k - 1))) := by
  sorry
theorem prescribed_denominator_corollary :
    (∃ k0 : ℕ, ∀ k : ℕ, k0 ≤ k →
    Real.exp (Real.exp ((k : ℝ) / 600)) ≤ (v k : ℝ) ∧
    v k ≤ 1 + k ^ (2 ^ (k - 1))) ∧
  (Real.log 2 / 257 ≤ Filter.liminf prescribedSlope Filter.atTop ∧
    Filter.liminf prescribedSlope Filter.atTop ≤
      Filter.limsup prescribedSlope Filter.atTop ∧
    Filter.limsup prescribedSlope Filter.atTop ≤ Real.log 2) ∧
  (∀ c : ℝ, c < Real.log 2 / 257 → ∃ k0 : ℕ,
    ∀ k : ℕ, k0 ≤ k →
      Real.exp (Real.exp (c * (k : ℝ))) ≤ (v k : ℝ)) := by
  sorry
end Problem337
end
DEFS(11): def IsEgyptianExpansion, def egyptianLengths, def egyptianLength, def maxEgyptianLength, def IsOneExpansion, def OneExpansions, def F, def D, def missingDenominators, def v, def prescribedSlope
## CHALLENGE ShortEgyptianFractions  targets=['OAI.ShortEgyptian.main'] defs=[]
theorem main :
    (∀ a b : ℕ, 1 ≤ a → a < b → ∃ ns : List ℕ, IsExpansion a b ns) ∧
    ∃ c₁ c₂ : ℝ, 0 < c₁ ∧ 0 < c₂ ∧ ∃ b₀ : ℕ, 2 ≤ b₀ ∧
      ∀ b : ℕ, b₀ ≤ b →
        c₁ * Real.log (Real.log (b : ℝ)) ≤ (maxMinLength b : ℝ) ∧
        (maxMinLength b : ℝ) ≤ c₂ * Real.log (Real.log (b : ℝ)) := by
  sorry
end ShortEgyptian
DEFS(3): def IsExpansion, def minLength, def maxMinLength
## PAPER Short-Egyptian-fractions-September-25-2026
ABSTRACT: We prove a conjecture of Erd\H{o}s: for every sufficiently large integer $b$, every rational number $a/b$ with $1\le a<b$ is a sum of $O(\log\log b)$ distinct positive unit fractions, with an absolute implied constant. This order is best possible when the numerator varies. We also show that both the number of expansions of $1$ with exactly $k$ distinct terms and the least integer at least $2$ that never occurs as a denominator in such an expansion grow doubly exponentially in $k$: their double logarithms have order $k$.
[theorem] \label{thm:main} There are absolute constants $c_1,c_2>0$ and $b_0$ such that, for every integer $b\ge b_0$, \[ c_1\log\log b\le N(b)\le c_2\log\log b. \] In particular, the upper bound holds for every integer numerator $1\le a<b$.
==================
# FAMILY 026: Positive lower density of large prime gaps
SCOPE: The formalized supplement proves that the indices $n$ for which $p_n/n<p_{n+1}/(n+1)$ have positive lower asymptotic density, where $p_n$ is the $n$th prime. Thus the normalized prime sequence has a positive-density set of increases. This is the prime-ratio corollary associated with the paper's theorem on a positive lower density of large prime gaps.
## CHALLENGE PrimeGaps  targets=['OAI.Problem344.large_gaps_and_ratio_density'] defs=[]
theorem large_gaps_and_ratio_density :
    (∀ C : ℝ, 0 < C →
      ∃ c : ℝ, 0 < c ∧ ∃ N₀ : ℕ, ∀ N : ℕ, N₀ ≤ N →
        c * (N : ℝ) ≤ ((LargePrimeGaps.largeGapIndices C N).card : ℝ)) ∧
    0 < lowerAsymptoticDensity ratioIncreaseIndices := by
  sorry
end Problem344
end
DEFS(6): def prime, def largeGapIndices, def primeAt, def initialCount, def lowerAsymptoticDensity, def ratioIncreaseIndices
## PAPER Positive-lower-density-of-large-prime-gaps-September-25-2026
ABSTRACT: For every fixed $C>0$, we prove that a positive proportion of consecutive prime gaps exceed $C\log p$, where $p$ is the smaller prime. The proportion is bounded below for every sufficiently large initial segment of the prime sequence, with a constant depending on $C$. It follows that the indices at which $p_n/n$ increases have positive lower asymptotic density, answering a question of Erd\H{o}s and Prachar.
[theorem] \label{thm:main} For every fixed real $C>0$, there are constants $c(C)>0$ and $N_0(C)$ such that, for every integer $N\ge N_0(C)$, \[ \#\{1\le n\le N:p_{n+1}-p_n>C\log p_n\}\ge c(C)N. \]
==================
# FAMILY 027: Potential integral density on curve character varieties
SCOPE: The integral-density question asks whether integral points become Zariski dense in every component of a curve character variety after one finite extension of the number field. The linked formalization proves a supporting compatibility result for its marked-surface construction. Given a proper diagram with finitely many vertices, a chosen seam with maximal adjacent facet rank and a positive-genus parent, puncture data, an existing solution over a field, and a chosen boundary occurrence, the produced marked values satisfy every seam equation. Existence of integral points and Zariski density are not established. The paper's main theorem—potential integral density for $\mathrm{SL}_r$ curve character varieties over one finite extension, including prescribed quasi-unipotent boundary data and every irreducible component—is outside this comparison.
## CHALLENGE CharacterVarietiesAllSeamsSupport  targets=['OAI.IntegralCharacterVarieties.SurfacePresentation.Diagram.producedMarkedValues_allSeams'] defs=[]
theorem producedMarkedValues_allSeams :
    D.ProducedMarkedSeamEquations q hproper hmax hg P x b0 i0 := by
  sorry
end IntegralCharacterVarieties.SurfacePresentation.Diagram
end
DEFS(0): 
## PAPER Integral-points-on-character-varieties-of-curves-September-25-2026
ABSTRACT: We prove potential Zariski density of integral points on $\SL_r$-character varieties of smooth complex curves in every rank. The result allows prescribed quasi-unipotent boundary monodromy, including exact nonsemisimple conjugacy classes, and holds on every component over the full ring of integers of one finite extension. Here integrality is measured in the ambient character variety, while the exact boundary conditions are imposed on the complex representation.
[theorem] \label{thm:main} Let $X$ be a smooth connected complex algebraic curve and let $r\geq1$. For prescribed quasi-unipotent conjugacy classes $C_1,\ldots,C_s$ as above, let $K\subset\C$ be a number field containing their eigenvalues. There is a finite extension $L/K$ such that \[ M_r(X)(\cO_L)\cap Y(\C) \] is Zariski dense in $Y$, and hence in every irreducible component of $Y$. The same conclusion holds when only the characteristic polynomial of each boundary monodromy is prescribed, with all its roots roots of unity. It also holds for the entire character variety without boundary conditions; in that case one may take $K=\Q$. For the relative statements and for projective $X$, one may take dist
==================
# FAMILY 028: Uniformly bounded components of Gaussian-prime graphs
SCOPE: The Gaussian moat problem asks whether an infinite walk through distinct Gaussian primes can have bounded step lengths. The formalized result gives a negative answer for every real step bound $D$. More strongly, one finite bound depending only on $D$ limits the size of every connected component of the bounded-step graph and the length of every injective bounded-step walk. Axis primes and all associates are included. No explicit function of $D$ is supplied.
## CHALLENGE GaussianMoat  targets=['OAI.GaussianMoat.fullMain'] defs=[]
theorem fullMain : MainEndpoint ∧ UniformEndpoint := by
  sorry
end GaussianMoat
DEFS(5): abbrev PrimeVertex, def primeGraph, def component, def MainEndpoint, def UniformEndpoint
## PAPER Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026
ABSTRACT: We prove the Gaussian moat conjecture: no infinite walk through distinct Gaussian primes can have bounded steps. More strongly, for each fixed finite step bound, the connected components of the Gaussian-prime graph have uniformly bounded size. This bound applies to every starting prime, including primes on the coordinate axes, and is nonexplicit. The proof constructs a finite periodic sieve obstruction using geometric sampling and information-theoretic estimates.
[theorem[Uniform component bound]] \label{thm:main}\label{cor:uniform} For every finite real $D$ there is a finite $B_D$ such that every connected component of $G_D$ has at most $B_D$ vertices. The bound is independent of the starting prime and includes primes on the coordinate axes. Consequently every sequence of distinct Gaussian primes whose successive distances are at most $D$ has at most $B_D$ terms.
==================
# FAMILY 032: The rational Hodge conjecture for CM abelian varieties
SCOPE: The formalization proves that every rational Hodge class on a complex CM abelian variety is algebraic. For a smooth integral projective group scheme $X$ over $\mathbb C$ with the stated complex-multiplication data and every $p\ge0$, each rational Hodge class of degree $2p$ is a rational linear combination of cycle classes of codimension-$p$ algebraic subvarieties. The result applies in every dimension and codimension. The complex-multiplication hypothesis is expressed on geometric rational $H^1$: it is a finite direct sum of rank-one vector spaces over CM number fields, and their diagonal action preserves the holomorphic Hodge filtration under the rational-to-de Rham comparison. The fields may differ among the summands. The paper's consequences for the Tate conjecture over finite fields and the Hodge standard conjecture in arbitrary characteristic are outside this selected statement. We 
## CHALLENGE HodgeConjectureCMAbelianVarieties/Challenge  targets=None defs=None
DEFS(1): theorem hodge_conjecture_for_cm_abelian_varieties
## PAPER The-rational-Hodge-conjecture-for-CM-abelian-varieties-October-6-2026
ABSTRACT: We prove the rational Hodge conjecture for complex abelian varieties with complex multiplication: every rational Hodge class on such a variety is a rational linear combination of algebraic cycle classes. As consequences, we obtain the generalized Hodge conjecture for CM abelian varieties, the Tate conjecture for abelian varieties over finite fields, and the Hodge standard conjecture for abelian varieties in arbitrary characteristic.
[theorem] \label{thm:cm} Let \(A\) be a complex CM abelian variety. For every integer \(p\geq0\), the Betti cycle-class map \[ \operatorname{cl}_B:\CH^p(A)_{\Q} \longrightarrow H^{2p}(A,\Q)\cap H^{p,p}(A) \] is surjective, where \(\CH^p(A)_{\Q}=\CH^p(A)\otimes_{\Z}\Q\) and the intersection is taken in \(H^{2p}(A,\C)\). In particular, the rational Hodge conjecture holds in every codimension on every finite product of complex CM abelian varieties and on every power of such a product.
==================
# FAMILY 033: Iitaka subadditivity, variation, and logarithmic additivity
SCOPE: The paper studies logarithmic Kodaira additivity for connected-fiber morphisms of smooth projective reduced simple-normal-crossing pairs that are smooth on all boundary strata away from the base boundary. The linked formalization proves the negative-fiber branch: for a very general base point, if the logarithmic Kodaira dimension of the fiber is $-\infty$, then the total logarithmic Kodaira dimension equals the sum of the base and fiber dimensions and is $-\infty$. Every positive-degree logarithmic pluriform section on the total space then vanishes. The finite-dimension and negative-base branches of the paper's additivity theorem are outside this selected statement.
## CHALLENGE LogKodairaFiberNegative  targets=['OAI.ReverseLogKodaira.SmoothProjectiveVariety.veryGenerally_fiber_negative_branch'] defs=[]
theorem veryGenerally_fiber_negative_branch
    {X Y : SmoothProjectiveVariety} {E : X.ReducedSNCBoundary} {D : Y.ReducedSNCBoundary}
    (f : StratumSmoothFibration X Y E D) :
    VeryGenerally Y fun y => y.point ∈ D.complement ∧
      ∀ F : FiberModel f.toBoundaryFibration y, F.boundary.kodaira = ⊥ →
        E.kodaira = D.kodaira + F.boundary.kodaira ∧
        ∀ (m : ℕ), 0 < m → ∀ s : X.RationalPluriform m, s ∈ E.sections m → s = 0 := by sorry
end ReverseLogKodaira.SmoothProjectiveVariety
end
DEFS(32): abbrev complexBase, abbrev projectiveGrading, abbrev complexProjectiveSpace, def projectiveConstants, def complexProjectiveStructure, structure SmoothProjectiveVariety, def globalConstants, def constants, def functionFieldConstants, lemma germ_constants, abbrev RationalCanonical, abbrev RationalPluriform, def regularPluriformLattice, def IsCartierIdeal, structure ReducedSNCBoundary, def ideal, def support, def IsLogPluriform, lemma isLogPluriform_zero, lemma isLogPluriform_add, lemma isLogPluriform_smul, def sections, def HasImageDimensionAtLeast, def kodaira, structure ComplexPoint, def complexBasePoint, def ComplexPoint.point, def ReducedSNCBoundary.complement, structure BoundaryFibration, structure StratumSmoothFibration
## PAPER The-reverse-logarithmic-Kodaira-inequality-and-additivity-September-26-2026
ABSTRACT: We prove the reverse logarithmic Kodaira inequality for a surjective connected-fiber morphism $f:(X,E)\to(Y,D)$ of smooth projective reduced simple-normal-crossing pairs, with $\Supp(f^*D)\subseteq\Supp E$, such that $X$ and every boundary stratum are smooth over $Y\setminus\Supp D$. Together with logarithmic subadditivity, the inequality gives additivity, including both negative-infinity cases. This resolves Popa's logarithmic additivity conjecture positively in the projective reduced-SNC, stratum-smooth setting.
[theorem[Reverse logarithmic Kodaira inequality]] \label{thm:upper-bound} Under these hypotheses, \begin{equation}\label{eq:upper-bound} \kappa(X,L_X)\leq\kappa(Y,L_Y)+\kappa(F,L_F). \end{equation} If either term on the right is $-\infty$, then $H^0(X,mL_X)=0$ for every $m>0$.
==================
# FAMILY 039: Nagata’s conjecture and maximal Seshadri constants
SCOPE: Nagata's conjecture asserts that a nonzero effective plane curve of degree $d$, with multiplicities at least $m_i$ at $r\ge10$ very general points, satisfies $\sum_i m_i<d\sqrt r$. The formalization establishes this inequality simultaneously for all curves and multiplicity vectors outside one countable union of proper Zariski-closed exceptional sets with nonempty complement. Reducible curves, repeated components, and unequal multiplicities are included, in both effective-curve and homogeneous-polynomial formulations. The formalization also includes the passage from homogeneous effective cycles to equations. The maximality question asks whether the multipoint Seshadri constant reaches the upper bound $\sqrt{L^2/r}$ at very general points once $r$ is sufficiently large. The formalized result establishes this for every smooth integral complex projective surface $S$ and ample line bundle $L$
## CHALLENGE Nagata  targets=['OAI.Nagata.Workers.W30.exists_positive_degree_equation_of_homogeneous_cycle', 'OAI.Nagata.nagata_conjecture', 'OAI.Nagata.nagata_conjecture_coordinates'] defs=[]
theorem exists_positive_degree_equation_of_homogeneous_cycle
    (cycle : Ideal TernaryPolynomial →₀ ℕ) (nonzero : cycle ≠ 0)
    (homogeneous : ∀ ideal ∈ cycle.support,
      ideal.IsPrime ∧ ideal ≠ ⊥ ∧ ideal.IsPrincipal ∧
        ideal.IsHomogeneous (MvPolynomial.homogeneousSubmodule (Fin 3) ℂ)) :
    ∃ polynomial : TernaryPolynomial,
      polynomial ≠ 0 ∧ polynomial.IsHomogeneous polynomial.totalDegree ∧
        0 < polynomial.totalDegree ∧ equationIdealCycle polynomial = cycle := by
  sorry
end Nagata.Workers.W30
theorem nagata_conjecture :
    ∀ count : ℕ, 10 ≤ count →
      ∃ exceptional : ℕ → Set (OrderedDistinctPoints count),
        (∀ index, IsConfigurationZariskiClosed (exceptional index) ∧
          exceptional index ≠ Set.univ) ∧
        (∃ points : OrderedDistinctPoints count, ∀ index, points ∉ exceptional index) ∧
        ∀ points : OrderedDistinctPoints count, (∀ index, points ∉ exceptional index) →
          ∀ curve : Workers.W10.EffectivePlaneCurve, ∀ multiplicities : Fin count → ℕ,
            (∀ index, multiplicities index ≤ W15.curveOrdinaryMultiplicity curve (points.val index)) →
            (∑ index, (multiplicities index : ℝ)) <
              (Workers.W10.curveDegree curve : ℝ) * Real.sqrt (count : ℝ) := by
  sorry
theorem nagata_conjecture_coordinates : FullNagata := by
  sorry
end Nagata
end
DEFS(45): def pointIdeal, def orderAtLeast, def translateHom, theorem translateHom_C, theorem translateHom_X, theorem translateHom_neg_comp, theorem translateHom_comp_neg, def translateEquiv, theorem translateEquiv_apply, theorem translate_ne_zero, theorem translated_support_nonempty, def ordinaryMultiplicity, abbrev PlanePoint, abbrev OrderedDistinctPoints, structure MultihomogeneousEquation, def equationVanishes, def IsProductZariskiClosed, def IsConfigurationZariskiClosed, abbrev ChartVariables, def dehomogenize, def chartCoordinates, def multiplicityAtLeast, theorem chart_exists, abbrev TernaryPolynomial, def equationMultiplicity, def associatePrincipalIdeal, def equationIdealCycle, abbrev PlanePolynomial, structure NonzeroHomogeneousForm, theorem homogeneous_eval_scale
## CHALLENGE MaximalSeshadriConstants  targets=['OAI.MaximalSeshadri.Geometry.maximalSeshadriConstants'] defs=[]
theorem maximalSeshadriConstants (S : Surface) (L : LineBundle S.scheme)
    (hL : LineBundle.IsAmple S.scheme L) : EventualMaximalSeshadri S L := by
  sorry
end MaximalSeshadri.Geometry
DEFS(45): def complexProjectiveSpace, def constantsInDegreeZero, def projectiveSpaceToSpec, structure Surface, structure LineBundle, def moduleTensor, def modulePow, def structureSheaf, abbrev GlobalSections, def sectionOpen, def LineBundle.IsAmple, def restrictScalar, lemma restrictScalar_naturality, def sheafHomSMul, instance sheafHomModule, instance sheafLinear, instance schemeHasExt, def baseScalars, abbrev cohomology, def cohomologyDimension, def eulerCharacteristic, def selfIntersection, structure IntegralCurve, def curveDegree, abbrev complexBase, abbrev ComplexPoint, def ComplexPoint.image, def surfacePower, def tupleImage, def tupleZariskiTopology
## PAPER Nagatas-Conjecture-for-Plane-Curves-September-23-2026
ABSTRACT: We prove that a nonzero effective plane curve of degree $d$ at $r\ge10$ very general complex points has total multiplicity strictly less than $d\sqrt r$. The inequality holds simultaneously for all curves, including reducible and nonreduced curves, and establishes Nagata's conjecture in its strict, nonhomogeneous form.
[theorem] \label{thm:main} For every integer $r\ge10$, there is a countable union $E_r$ of proper Zariski-closed subsets of $U_r$, with nonempty complement, such that the following holds for every tuple $(p_1,\ldots,p_r)\notin E_r$. If $C$ is a nonzero effective plane curve of degree $d\ge1$ and $m_1,\ldots,m_r\in\Z_{\ge0}$ satisfy $\mult_{p_i}C\ge m_i$, then \[ d\sqrt r>\sum_{i=1}^r m_i. \]
## PAPER Maximal-Seshadri-Constants-on-Arbitrary-Polarized-Surfaces-September-23-2026
==================
# FAMILY 047: Zariski cancellation and affine fibrations over the complex numbers
SCOPE: Affine-space cancellation asks whether $X\times\mathbb A^1\cong\mathbb A^{n+1}$ forces $X\cong\mathbb A^n$. The formalized result gives an explicit finite-type complex domain $A$ of Krull dimension four with $A[w]\cong\mathbb C[x_1,\ldots,x_5]$ but $A\not\cong\mathbb C[x_1,\ldots,x_4]$. Thus adjoining one variable erases a genuine algebraic distinction. The separate stable-coordinate and general line-bundle lifting consequences are not included.
## CHALLENGE ComplexCancellation  targets=['OAI.ComplexCancellation.main'] defs=[]
theorem main : MainStatement := by
  sorry
end ComplexCancellation
end
DEFS(10): abbrev P, def p, def s, def u, def F, def J, def x, def H, abbrev A, def MainStatement
## PAPER An-explicit-failure-of-complex-affine-space-cancellation-September-23-2026
ABSTRACT: We construct an explicit integral complex affine fourfold $X$ with $X\times\mathbb A^1\cong\mathbb A^5$ but $X\not\cong\mathbb A^4$. This gives a negative answer to Zariski's affine-space cancellation problem over $\mathbb C$ in dimension four. The same construction disproves the Stable Coordinate Conjecture in ambient dimension five and yields smooth $\mathbb A^3$-fibrations over $\mathbb A^1$ and $\mathbb A^2$ that are not Zariski-locally trivial. These fibrations disprove the Dolgachev--Weisfeiler affine-fibration conjecture over these bases.
[theorem] \label{thm:main} The algebra $A$ in \eqref{eq:example} is an integral complex algebra of dimension four. For an independent variable $w$, \[ A[w]\simeq\kk\poly5, \qquad A\not\simeq\kk\poly4. \] Consequently the Zariski cancellation problem over the complex numbers has a negative answer in dimension four.
==================
# FAMILY 049: A stable-coordinate counterexample in four variables
SCOPE: The stable coordinate conjecture predicts that a polynomial that becomes a coordinate after adjoining variables was already a coordinate. The formalization gives an explicit degree-five polynomial in four complex variables that becomes a coordinate after adjoining one variable but is not a coordinate in four variables. Every fiber is isomorphic to affine three-space, yet no fiber can be carried to a coordinate hyperplane by an ambient polynomial automorphism. The Abhyankar–Sathaye conjecture predicts that a polynomial defining an affine-space quotient must be an ambient coordinate. For every $n\ge4$, the formalized counterexample gives $F\in\mathbb C[x_1,\ldots,x_n]$ with quotient $\mathbb C[x_1,\ldots,x_n]/(F)\cong\mathbb C[y_1,\ldots,y_{n-1}]$, although $F$ is not a coordinate. A companion gives $n-1$ commuting, locally nilpotent derivations, linearly independent over the polynomial ri
## CHALLENGE AbhyankarSathaye  targets=['OAI.AbhyankarSathaye.exists_noncoordinate_polynomial'] defs=[]
theorem exists_noncoordinate_polynomial (n : ℕ) (hn : 4 ≤ n) :
    ∃ F : MvPolynomial (Fin n) ℂ,
      Nonempty ((MvPolynomial (Fin n) ℂ ⧸ Ideal.span {F}) ≃ₐ[ℂ]
        MvPolynomial (Fin (n - 1)) ℂ) ∧
      ¬ ∃ (equiv : MvPolynomial (Fin n) ℂ ≃ₐ[ℂ] MvPolynomial (Fin n) ℂ)
        (index : Fin n), equiv (MvPolynomial.X index) = F := by
  sorry
end AbhyankarSathaye
DEFS(0): 
## CHALLENGE CommutingDerivations  targets=['OAI.AbhyankarSathaye.CommutingDerivations.commuting_derivations_with_ordinary_extras'] defs=[]
theorem commuting_derivations_with_ordinary_extras (n : ℕ) (hn : 4 ≤ n) :
    ∃ d : Fin (n-1) → Derivation ℂ (MvPolynomial (Fin n) ℂ) (MvPolynomial (Fin n) ℂ),
      (∀ i, d i (extendedF hn + 1) = 0) ∧
      (∀ i j p, d i (d j p) = d j (d i p)) ∧
      (∀ i, LocallyNilpotent (d i)) ∧
      LinearIndependent (MvPolynomial (Fin n) ℂ) d ∧
      (∀ p, (∀ i, d i p = 0) ↔
        p ∈ Algebra.adjoin ℂ ({extendedF hn} : Set (MvPolynomial (Fin n) ℂ))) ∧
      (∀ g, (∀ i, d i g = 0) →
        ¬ ∃ (e : MvPolynomial (Fin n) ℂ ≃ₐ[ℂ] MvPolynomial (Fin n) ℂ) (j : Fin n),
          e (X j) = g) ∧
      (∀ i : Fin (n-4), d (blocksToOutput hn (Sum.inl i)) =
        pderiv (blocksToAmbient hn (Sum.inl i))) := by
  sorry
end CommutingDerivations
end AbhyankarSathaye
end
DEFS(17): def S, def P, abbrev R, def h, def u, def v, def w, def x, def y, def s, def p, def F, def fourInclusion, def extendedF, def blocksToAmbient, def blocksToOutput, def LocallyNilpotent
## CHALLENGE StableCoordinateFour  targets=['OAI.StableCoordinate.principal_package'] defs=[]
theorem principal_package : PrincipalPackage := by
  sorry
end StableCoordinate
DEFS(13): abbrev R, def Q, def f, def IsCoordinate, def stabilize, def IsOneStableCoordinate, def fiberIdeal, abbrev FiberRing, def IsAffineThreeSpaceFiber, def IsRectifiableFiber, def PolynomialPackage, def FiberPackage, def PrincipalPackage
## PAPER An-explicit-noncoordinate-polynomial-with-affine-three-space-zero-fibre-September-24-2026
ABSTRACT: We construct an explicit counterexample to the Abhyankar--Sathaye conjecture: a noncoordinate polynomial in four complex variables whose zero fibre is affine three-space. Adjoining variables gives counterexamples in every ambient dimension at least four.
[theorem] \label{thm:main} The polynomial $F$ defined in \eqref{eq:xyz}--\eqref{eq:F} satisfies \[ R/(F)\cong\CC^{[3]}, \qquad \grad F(2,0,-1/2,1/2)=0. \] Consequently $F$ is not a coordinate of $R$.
## PAPER A-stable-coordinate-that-is-not-a-coordinate-in-four-variables-October-5-2026
ABSTRACT: We construct an explicit degree-five polynomial over $\C$ that is not a coordinate in four variables but becomes one after adjoining a single variable. This gives a counterexample to the stable coordinate conjecture in four variables. Every fiber is isomorphic to affine three-space, yet its embedding in affine four-space is not rectifiable. Thus the example also disproves the Abhyankar--Sathaye embedding conjecture in ambient dimension four.
[theorem] \label{thm:main} In $R=\C[x_1,x_2,x_3,x_4]$, put \begin{equation}\label{eq:explicit-counterexample} Q=x_2^2-x_4^2+x_1x_3, \qquad f=x_1-2Q\bigl(Q(x_2+x_4)+x_1x_4\bigr). \end{equation} There is a $\C$-algebra automorphism of $R[w]$ sending $f$ to $x_1$, but there is no such automorphism of $R$.
==================
# FAMILY 050: A counterexample to Griffiths’ positivity conjecture
SCOPE: Griffiths' positivity conjecture predicts that every ample holomorphic vector bundle on a smooth complex projective variety admits a smooth Hermitian metric with strictly Griffiths-positive curvature. The formalized counterexample starts with a rank-two algebraic bundle $G$ on $\mathbb P^1\times\mathbb P^1$. Its coordinatewise power pullbacks, tensored with $\mathcal O(1,1)$, are ample for every positive power but admit no such metric for all sufficiently large powers. The separate very-ampleness result for all admissible even exponents is not included.
## CHALLENGE QuadricBundles  targets=['OAI.QuadricCounterexample.main_theorem'] defs=[]
theorem main_theorem : SourceMainTheorem := by
  sorry
end QuadricCounterexample
end
DEFS(34): abbrev ProjectiveLine, abbrev QuadricSurface, def reciprocalP1, def affineP1, def affineQuadric, def coordP1, def coordQuadric, def powerP1, def powerQuadric, abbrev BaseCoordinates, abbrev FiberCoordinates, abbrev TwoMatrix, abbrev BasePolynomial, def baseEval, def AlgebraicallyRegularOn, def principalChart, structure AlgebraicRankTwoBundle, def domain, def coordinateDomain, def dualTransition, def hyperplaneTransition, def polarizationTransition, def IsPowerPullbackTwist, structure SymmetricSection, def SymmetricSection.value, def ProjectiveAlgebraicCone, def sectionVector, def GivesClosedProjectiveEmbedding, def IsAmple, def holomorphicMetricDerivative
## PAPER ample-rank-two-bundles-on-the-quadric-surface-without-griffiths-positive-metrics-September-24-2026
ABSTRACT: We give counterexamples to Griffiths' conjecture in rank two on the quadric surface $\PP^1\times\PP^1$. We construct an explicit bundle $G$ whose coordinatewise power pullbacks, tensored with $\OO(1,1)$, are ample for every positive power, but admit no smooth strictly Griffiths-positive Hermitian metric for all sufficiently large powers.
[theorem] \label{thm:main} There is an algebraic vector bundle $G$ of rank two on $S$ such that, for every positive integer $m$, the bundle \[ E_m=f_m^*G\otimes P \] is ample. There is an integer $m_0$ such that $E_m$ admits no smooth Hermitian metric with strictly Griffiths-positive Chern curvature for every $m\ge m_0$.
==================
# FAMILY 052: Tangent splittings and product decompositions
SCOPE: The splitting question asks whether a holomorphic decomposition of the tangent bundle comes from a product decomposition of the universal cover. The formalized result gives an affirmative answer for a compact connected Kähler manifold whose tangent bundle splits into two positive-rank, integrable holomorphic subbundles. The universal cover is a product of connected simply connected complex manifolds of the prescribed dimensions, and the differential identifies the two tangent factors with the original summands. Both integrability assumptions are required. Automatic integrability and the paper's additional corollaries are not included. The formalization proves integrability of both summands in a holomorphic splitting of the tangent bundle of a rationally connected projective manifold. More precisely, for a compact connected complex manifold of dimension at least two with a projective embe
## CHALLENGE KahlerSplitting  targets=['OAI.UniversalCoverSplitting.main'] defs=[]
theorem main (X : ComplexManifold.{u} n) [CompactSpace X.Carrier]
    [ConnectedSpace X.Carrier] (hn : 2 ≤ n) (hr₁ : 0 < r₁) (hr₂ : 0 < r₂)
    (g : KahlerMetric X) (S : HolomorphicSplitting X r₁ r₂)
    (h₁ : Integrable S.projection) (h₂ : Integrable (complementaryProjection S))
    (Z : ComplexManifold.{v} n) (π : OrdinaryUniversalCover X Z) :
    ∃ (Y₁ : ComplexManifold.{v} r₁) (Y₂ : ComplexManifold.{v} r₂),
      ConnectedSpace Y₁.Carrier ∧ ConnectedSpace Y₂.Carrier ∧
      SimplyConnectedSpace Y₁.Carrier ∧ SimplyConnectedSpace Y₂.Carrier ∧
      CompatibleProduct S π Y₁ Y₂ := by
  sorry
end UniversalCoverSplitting
end
DEFS(17): abbrev Model, abbrev model, structure ComplexManifold, abbrev Tangent, abbrev RealMetricField, def metricInChart, def fundamentalInChart, structure KahlerMetric, abbrev ProjectionField, def projectionInChart, def HolomorphicProjection, def Integrable, structure HolomorphicSplitting, def complementaryProjection, def LocalBiholomorphism, structure OrdinaryUniversalCover, def CompatibleProduct
## CHALLENGE SplitTangentIntegrability  targets=['OAI.SplitTangent.integrability_main'] defs=[]
theorem integrability_main : IntegrabilityStatement.{u} := by
  sorry
end SplitTangent
end
DEFS(20): structure ComplexManifold, abbrev Model, abbrev ModelWithCorners, abbrev Tangent, abbrev ProjectiveSpace, def projectiveCoordinates, structure ProjectiveEmbedding, structure RationalCurve, def RationalCurve.value, abbrev PairPolynomial, def Bihomogeneous, def pairEval, def IsZariskiOpenPair, def RationallyConnected, structure TangentSplitting, def TangentSplitting.first, def TangentSplitting.second, def HolomorphicSectionOn, def Integrable, def IntegrabilityStatement
## PAPER Universal-cover-splitting-for-compact-Kahler-manifolds-September-23-2026
ABSTRACT: We prove the two-summand form of Beauville's compatible splitting conjecture. If the tangent bundle of a compact connected K\"ahler manifold decomposes into two integrable holomorphic subbundles of positive rank, then its ordinary universal cover admits a product decomposition whose factor tangent bundles are the lifted specified summands.
[theorem] \label{thm:main} Let $X$ be a compact connected K\"ahler manifold of complex dimension $n\geq2$, and let \[ T_X=E_1\oplus E_2 \] be a specified decomposition into integrable holomorphic subbundles of positive ranks $r_1,r_2$. If $\pi:\widetilde X\to X$ is the ordinary universal covering map, there are connected simply connected complex manifolds $Y_1,Y_2$ and a biholomorphism $\Phi:\widetilde X\to Y_1\times Y_2$ such that \[ \dd\Phi(\pi^*E_i)=\pr_i^*T_{Y_i}\qquad(i=1,2), \] where $\dd\pi$ identifies $T_{\widetilde X}$ with $\pi^*T_X$. In particular, $\dim_\C Y_i=r_i$.
## PAPER Integrability-of-split-tangent-bundles-on-rationally-connected-manifolds-September-23-2026
ABSTRACT: We prove that both summands of every specified holomorphic splitting of the tangent bundle of a smooth rationally connected projective complex manifold into two positive-rank subbundles are integrable. This proves H\"oring's conjecture on rationally connected projective manifolds. H\"oring's product theorem then gives a product decomposition compatible with the specified splitting.
[theorem[Automatic integrability]] \label[theorem]{thm:main} Let \(X\) be a smooth connected projective complex manifold of dimension at least two. Suppose that two general points of \(X\) lie on the image of a morphism \(\PP^1\to X\). For every specified holomorphic decomposition \[ T_X=E_1\oplus E_2 \] into subbundles of positive rank, both \(E_1\) and \(E_2\) are integrable.
==================
# FAMILY 058: Semialgebraic universal covers and bounded domains
SCOPE: The formalized result answers the paper's symmetry question affirmatively. A nonempty connected bounded semialgebraic subset, relatively open in a complex affine algebraic set, is smooth and biholomorphic to a bounded symmetric domain whenever a discrete group acts properly and holomorphically with compact quotient. The action need not be free, and the ambient algebraic set may be singular.
## CHALLENGE SymmetricDomains  targets=['OAI.Release061.main'] defs=[]
theorem main {n : ℕ} (V U : Set (Affine n))
    (hV : IsAffineAlgebraic V) (hUV : U ⊆ V)
    (hopen : IsOpen ((Subtype.val : V → Affine n) ⁻¹' U))
    (hconn : IsConnected U) (hsa : IsSemialgebraic U)
    (hbounded : Bornology.IsBounded U)
    (Γ : Type*) [Group Γ] [TopologicalSpace Γ] [DiscreteTopology Γ]
    [MulAction Γ U] [ProperSMul Γ U]
    [CompactSpace (Quotient (MulAction.orbitRel Γ U))]
    (hhol : ∀ γ : Γ, HolomorphicOnSubset U (fun p => (γ • p : U).val)) :
    IsSmooth U ∧ ∃ (m : ℕ) (D : Set (Affine m)),
      IsBoundedSymmetricDomain D ∧ Nonempty (Biholomorph U D) := by
  sorry
end Release061
DEFS(8): abbrev Affine, def realCoordinates, def IsAffineAlgebraic, inductive IsSemialgebraic, def HolomorphicOnSubset, structure Biholomorph, def IsSmooth, def IsBoundedSymmetricDomain
## PAPER Symmetry-of-semialgebraic-bounded-domains-with-compact-quotient-September-24-2026
ABSTRACT: Every nonempty connected semialgebraic bounded open subset of a complex affine variety admitting a properly discontinuous cocompact group of biholomorphisms is smooth and biholomorphic to a bounded symmetric domain. This answers the bounded-domain question of Koll\'ar and Pardon affirmatively.
[theorem] \label{thm:main} Let \(U\) be a nonempty connected semialgebraic bounded open subset of a complex affine variety. Suppose that a group \(\Gamma\) of biholomorphisms acts properly discontinuously on \(U\) and that \(U/\Gamma\) is compact. Then \(U\) is smooth and is biholomorphic to a bounded symmetric domain.
==================
# FAMILY 066: Bounded klt complements for Fano contractions
SCOPE: The paper develops uniform Cartier sections for Fano-type contractions as a step toward bounded klt complements. The linked formalization proves a local compactness result: for positive numbers $a_i$, the chart-field retractions indexed by nonnegative weights satisfying $\sum_i a_iw_i=1$ form a compact set in the pointwise topology on the fraction field. The chart is built over an algebraically closed field from the localization of a polynomial ring at its origin. Its local domain is Noetherian, essentially of finite type and formally unramified over that localization, and formally étale over the polynomial ring. This compactness result applies to one such chart. It does not construct a Cartier divisor through a prescribed base point whose pullback has a positive log-canonical-threshold bound along the whole fibre depending only on dimension and discrepancy, as required by the paper's un
## CHALLENGE CartierChartCompactnessSupport  targets=['OAI.CartierSections.isCompact_closedChartFieldRetraction_cone'] defs=[]
lemma isCompact_closedChartFieldRetraction_cone
    (a : σ → NNReal) (ha : ∀ i, 0 < a i) :
    IsCompact ((fun w : σ → NNReal => fun x : K =>
      closedChartFieldRetraction (σ := σ) (k := k) (R := R) (A := A) w x) ''
      normalizedWeights a) := by
  sorry
end ClosedChartFieldTopology
end CartierSections
end
DEFS(0): 
## PAPER Uniform-Cartier-sections-for-Fano-type-contractions-September-25-2026
ABSTRACT: We prove the Cartier-divisor conjecture of Birkar and Shokurov for rational boundaries in characteristic zero and for real boundaries over $\C$. For an $\epsilon$-lc Fano type contraction with positive-dimensional base and nef negative log canonical class, a Cartier divisor through any prescribed base point can be chosen with pullback log canonical threshold bounded below in terms of the dimension and $\epsilon$ alone.
[maintheorem[Uniform Cartier sections]] \label{thm:main} For every integer $d>0$ and every real number $\epsilon>0$, there is a real number $\tau=\tau(d,\epsilon)>0$ with the following property. Let $(X,B)$ be an $\epsilon$-lc rational pair of dimension $d$, and let $f:X\to Z$ be a Fano type contraction of normal integral quasi-projective varieties with $\dim Z>0$. Suppose that $-(K_X+B)$ is nef over $Z$. For every closed point $z\in Z$, there are an open neighbourhood $U$ of $z$ and a nonzero effective Cartier divisor $D$ on $U$, with $z\in\Supp D$, such that \[ \bigl(f^{-1}(U),B|_{f^{-1}(U)}+\tau f^*D\bigr) \quad\text{is log canonical.} \]
==================
# FAMILY 071: Koebe’s circle-domain conjecture
SCOPE: The formalization proves the removability-to-rigidity direction of the He–Schramm conjecture. If a circle domain has conformally removable boundary, then every conformal equivalence from it to another circle domain agrees on the source with a Möbius transformation. There is no bound on the number of complementary components. The same Comparator file also states Koebe's circle-domain theorem, which gives a circle-domain representative for every domain in the Riemann sphere. Koebe's circle-domain conjecture asks whether every domain in the Riemann sphere is conformally equivalent to a circle domain, whose complementary components are round disks or points. The formalization proves this for every domain. It also proves rigidity under a separate hypothesis: a conformal equivalence between circle domains is a Möbius transformation when the source boundary is conformally removable.
## CHALLENGE KoebeCircleDomains  targets=['OAI.Problem047.koebe_circle_domain', 'OAI.Problem047.removability_implies_rigidity'] defs=[]
theorem koebe_circle_domain :
    ∀ U : Set Sphere, IsOpen U → IsConnected U →
      ∃ (V : Set Sphere) (f : Sphere → Sphere),
        IsCircleDomain V ∧ IsConformalEquivalence f U V := by
  sorry
theorem removability_implies_rigidity :
    ∀ (U V : Set Sphere) (f : Sphere → Sphere),
      IsCircleDomain U → IsCircleDomain V →
      IsConformallyRemovable (frontier U) → IsConformalEquivalence f U V →
      ∃ M : Mobius, ∀ p ∈ U, f p = M • p := by
  sorry
end Problem047
end
DEFS(13): abbrev Sphere, abbrev Mobius, def sphereInv, def finiteCoord, def chart, def chartSymm, def IsConformalAt, def IsConformalOn, def IsConformalEquivalence, def IsRoundClosedDisk, def IsCircleDomain, def OrientationPreserving, def IsConformallyRemovable
## CHALLENGE KoebeCircleDomains  targets=['OAI.Problem047.koebe_circle_domain', 'OAI.Problem047.removability_implies_rigidity'] defs=[]
theorem koebe_circle_domain :
    ∀ U : Set Sphere, IsOpen U → IsConnected U →
      ∃ (V : Set Sphere) (f : Sphere → Sphere),
        IsCircleDomain V ∧ IsConformalEquivalence f U V := by
  sorry
theorem removability_implies_rigidity :
    ∀ (U V : Set Sphere) (f : Sphere → Sphere),
      IsCircleDomain U → IsCircleDomain V →
      IsConformallyRemovable (frontier U) → IsConformalEquivalence f U V →
      ∃ M : Mobius, ∀ p ∈ U, f p = M • p := by
  sorry
end Problem047
end
DEFS(13): abbrev Sphere, abbrev Mobius, def sphereInv, def finiteCoord, def chart, def chartSymm, def IsConformalAt, def IsConformalOn, def IsConformalEquivalence, def IsRoundClosedDisk, def IsCircleDomain, def OrientationPreserving, def IsConformallyRemovable
## PAPER Removable-Boundaries-and-Rigidity-of-Circle-Domains-September-23-2026
ABSTRACT: We prove that a circle domain with conformally removable boundary is conformally rigid, with no restriction on the number of complementary components. This establishes the removability-to-rigidity direction of the He--Schramm Conjecture.
[theorem] \label{thm:main} Every circle domain with conformally removable boundary is conformally rigid. More explicitly, if $\Omega,\Omega'\subset\Chat$ are circle domains, $\partial\Omega$ is conformally removable, and $f\colon\Omega\to\Omega'$ is a conformal equivalence, then there is a M\"obius transformation $M$ such that $f=M|_\Omega$.
## PAPER Koebes-Circle-Domain-Conjecture-September-23-2026
ABSTRACT: We prove that every domain in the Riemann sphere is conformally equivalent to a circle domain, resolving Koebe's circle-domain conjecture positively.
[theorem[Circle-domain uniformization]] \label{thm:main} Every nonempty connected open set $G\subset\Chat$ is conformally equivalent to a circle domain.
==================
# FAMILY 072: Brennan's conjecture and the integral-means spectrum
SCOPE: Brennan's conjecture asserts that $|\phi'|^s$ is area-integrable for $4/3<s<4$ when $\phi$ conformally maps a simply connected plane domain with nontrivial spherical boundary onto the disk. The formalization establishes this interval, along with area integrability of $|f'|^t$ for univalent disk maps when $-2<t<2/3$. It also gives the uniform inverse-square radial-mean bound with exponent $-1-\varepsilon$ for every $\varepsilon>0$ and the spectrum value $B_{\mathcal S}(-2)=1$. The Koebe map and its inverse give divergence at all four boundary exponents. Kraetzer's proposed integral-means spectrum predicts $B_b(-1)=1/4$ for bounded univalent maps. The formalized result proves $B_b(-1)<1/4$, contradicting that prediction. The underlying estimate gives constants $0<\varepsilon<1/4$ and $C<\infty$ such that the normalized circular mean of $|f'|^{-1}$ is at most $C(1-r)^{-1/4+\varepsilon}$ for
## CHALLENGE Brennan  targets=['OAI.Brennan.main_theorem'] defs=[]
theorem main_theorem : MainStatement := by
  sorry
end Brennan
end
DEFS(8): def disk, def UnivalentOn, def Schlicht, def integralMean, def beta, def spectrum, def SphericalBoundaryNontrivial, def MainStatement
## CHALLENGE BrennanSharp  targets=['OAI.Brennan.Sharp.sharp_endpoints'] defs=[]
theorem sharp_endpoints : SharpEndpointStatement := by
  sorry
end Sharp
end Brennan
end
DEFS(8): def disk, def UnivalentOn, def Schlicht, def koebeMap, def koebeDomain, def koebeInverse, def areaMoment, def SharpEndpointStatement
## CHALLENGE StrictMeans  targets=['OAI.StrictInverseFirstPower.main'] defs=[]
theorem main :
    (∃ ε C : ℝ, 0 < ε ∧ ε < 1 / 4 ∧
      ∀ (f : ℂ → ℂ), NormalizedUnivalent f →
        ∀ r : ℝ, 1 / 2 ≤ r → r < 1 →
          integralMean (-1) f r ≤ C * (1 - r) ^ (-(1 / 4 : ℝ) + ε)) ∧
    boundedSpectrum (-1) < (1 / 4 : EReal) ∧
    (¬ ∀ p : ℝ, boundedSpectrum p = kraetzerPrediction p) := by
  sorry
end StrictInverseFirstPower
DEFS(7): def disk, def NormalizedUnivalent, def BoundedNormalizedUnivalent, def integralMean, def growthExponent, def boundedSpectrum, def kraetzerPrediction
## PAPER Brennans-conjecture-and-sharp-inverse-square-integral-means-September-24-2026
ABSTRACT: We prove Brennan's conjecture: if a simply connected plane domain admits a conformal bijection $\varphi$ onto the unit disk, then $|\varphi'|^s$ is area-integrable for every $4/3<s<4$. We also prove the sharp inverse-square integral-means exponent $B_{\SSS}(-2)=1$ for the normalized schlicht class $\SSS$.
[theorem[Brennan's conjecture and inverse-square means]] \label{thm:main} For every $\varepsilon>0$ there is $C_\varepsilon<\infty$ such that \begin{equation}\label{eq:main-uniform} M_{-2}[f'](r)\le C_\varepsilon(1-r)^{-1-\varepsilon} \qquad\left(f\in\SSS,\ \frac12\le r<1\right). \end{equation} Moreover, $B_{\SSS}(-2)=1$. Let $W\subset\CC$ be any simply connected domain whose boundary in the Riemann sphere contains at least two points. Every conformal bijection $\varphi:W\to\DD$ satisfies \[ \int_W|\varphi'(z)|^s\dd A(z)<\infty \qquad\left(\frac43<s<4\right). \] Equivalently, every univalent map $f:\DD\to\CC$ satisfies \[ \int_{\DD}|f'(w)|^t\dd A(w)<\infty \qquad\left(-2<t<\frac23\right). \]
## PAPER A-strict-inverse-first-power-bound-for-univalent-functions-September-24-2026
ABSTRACT: We prove a uniform upper bound for inverse-first-power integral means of normalized univalent disk maps with exponent strictly below \(1/4\). Consequently, the bounded universal integral-means spectrum satisfies \(B_b(-1)<1/4\), disproving Kraetzer's conjectured spectrum at \(p=-1\).
[theorem[Uniform inverse-first-power bound]] \label{thm:main} There exist constants \(0<\varepsilon<1/4\) and \(C<\infty\) such that \begin{equation}\label{eq:uniform} M_{-1}[f'](r)\le C(1-r)^{-1/4+\varepsilon} \qquad\text{for every }f\in\SSS\text{ and every }1/2\le r<1. \end{equation} Consequently \(B_b(-1)<1/4\), and Kraetzer's conjectured identity \eqref{eq:kraetzer} is false.
==================
# FAMILY 073: The Falconer distance conjecture
SCOPE: The formalization proves the Falconer distance conjecture in every dimension. For every integer $d\ge2$ and compact set $E\subset\mathbb R^d$ with Hausdorff dimension greater than $d/2$, the set $\{\lVert x-y\rVert:x,y\in E\}$ has positive Lebesgue measure. The linked statements include both this all-dimensional result and the earlier planar case.
## CHALLENGE PlanarFalconer  targets=['OAI.PlanarFalconer.mainTarget_proved'] defs=[]
theorem mainTarget_proved : MainTarget := by
  sorry
end PlanarFalconer
DEFS(3): abbrev Plane, def distanceSet, def MainTarget
## CHALLENGE FalconerAllDimensions  targets=['OAI.Falconer.falconer_distance_conjecture'] defs=[]
theorem falconer_distance_conjecture :
    ∀ (d : ℕ), 2 ≤ d → ∀ E : Set (EuclideanSpace ℝ (Fin d)), IsCompact E →
      (d : ℝ≥0∞) / 2 < dimH E →
        0 < volume {r : ℝ | ∃ x ∈ E, ∃ y ∈ E, dist x y = r} := by
  sorry
end Falconer
DEFS(0): 
## PAPER The-Falconer-distance-conjecture-in-all-dimensions-September-23-2026
ABSTRACT: We resolve the Falconer distance conjecture in every dimension. For every integer \(d\ge2\), a compact subset of \(\R^d\) with Hausdorff dimension greater than \(d/2\) determines a set of Euclidean distances of positive Lebesgue measure.
[theorem] \label{thm:main} Let \(d\ge2\) be an integer and let \(E\subset\R^d\) be compact. If \(\dim_H E>d/2\), then \[ \cL^1(\Delta(E))>0. \]
==================
# FAMILY 075: The $`L\log L`$ Fourier-convergence conjecture
SCOPE: The $L\log L$ Fourier-convergence conjecture asks whether ordinary symmetric Fourier partial sums converge almost everywhere at this integrability scale. The formalization proves this for every measurable complex-valued function on $\mathbb T=\mathbb R/(2\pi\mathbb Z)$ satisfying $\int_{\mathbb T}|f|\log(2+|f|)<\infty$. Outside one measurable null set, $\sum_{k=-N}^{N}\widehat f(k)e^{ikx}\to f(x)$ along the full sequence $N\to\infty$.
## CHALLENGE FourierLLogL  targets=['OAI.FourierLLogL.paperMain'] defs=[]
theorem paperMain (f : AddCircle (2 * Real.pi) → ℂ)
    (hfm : AEStronglyMeasurable f AddCircle.haarAddCircle)
    (hfi : Integrable (fun x ↦ ‖f x‖ * Real.log (2 + ‖f x‖))
      AddCircle.haarAddCircle) :
    ∃ E : Set (AddCircle (2 * Real.pi)),
      MeasurableSet E ∧ AddCircle.haarAddCircle E = 0 ∧ ∀ x ∉ E,
        Tendsto
          (fun N : ℕ ↦
            ∑ k ∈ Finset.Icc (-(N : ℤ)) (N : ℤ), fourierCoeff f k * fourier k x)
          atTop (𝓝 (f x)) := by
  sorry
DEFS(1): instance circlePeriod_pos
## PAPER Almost-everywhere-Fourier-convergence-in-L-log-L-September-23-2026
ABSTRACT: We prove that the ordinary symmetric Fourier partial sums of every complex-valued function in $L\log L$ on the circle converge almost everywhere to the function along the full sequence. This establishes the classical $L\log L$ sufficiency conjecture.
[theorem[Almost-everywhere convergence in $L\log L$]] \label{thm:main} For every complex-valued $f\in L\log L(\mathbb T)$, there is a measurable set $N_f$ of measure zero such that \[ \lim_{N\to\infty}S_Nf(x)=f(x) \qquad (x\in\mathbb T\setminus N_f). \] The limit is along the full sequence $N=0,1,2,\ldots$.
==================
# FAMILY 076: Real ultraflat Littlewood polynomials and unbounded binary merit factors
SCOPE: The formalization gives real Littlewood polynomials of every sufficiently large length whose maximum modulus on the unit circle is at most $(1+\eta)\sqrt N$ for any fixed $\eta>0$. Thus the smallest possible maximum is asymptotically minimal through all integer lengths. A further statement chooses one family of real sign polynomials for all lengths such that, for every fixed finite $p>0$, the $L^p$ mean of $\bigl||P_N(z)|/\sqrt N-1\bigr|$ on the unit circle tends to zero. The results are existential and do not give an effective convergence rate or a signing algorithm.
## CHALLENGE AsymptoticallyMinimalLittlewood  targets=['OAI.AsymptoticallyMinimalLittlewood.main'] defs=[]
theorem main : MainStatement := by
  sorry
end AsymptoticallyMinimalLittlewood
DEFS(3): def littlewoodValue, def IsRealSigning, def MainStatement
## CHALLENGE LittlewoodFiniteFlatness  targets=['OAI.AsymptoticallyMinimalLittlewoodFiniteFlatness.main'] defs=[]
theorem main : MainStatement := by
  sorry
end AsymptoticallyMinimalLittlewoodFiniteFlatness
end
DEFS(3): def littlewoodValue, def IsRealSigning, def MainStatement
## PAPER Asymptotically-minimal-maxima-of-real-Littlewood-polynomials-September-23-2026
ABSTRACT: We prove that the minimum possible maximum modulus on the unit circle of a polynomial with $N$ consecutive real coefficients in $\{-1,1\}$ is $(1+o(1))\sqrt N$, as $N$ tends to infinity through all integers. This disproves the real-sign analogue of Erd\H{o}s's fixed relative-gap conjecture. As a consequence, the largest binary merit factor at length $N$ tends to infinity through all integer lengths, disproving Turyn's conjecture.
[theorem] \label{thm:main} For Littlewood polynomials with real coefficients, \[ \lim_{N\to\infty}m_N=1. \] Equivalently, for every $\eta>0$ there is $N_0$ such that for every integer $N\ge N_0$ there are signs $\varepsilon_0,\ldots,\varepsilon_{N-1}$ with \[ \max_{|z|=1}\left|\sum_{k=0}^{N-1}\varepsilon_kz^k\right| \le(1+\eta)\sqrt N. \]
==================
# FAMILY 079: Local smoothing for the Euclidean wave equation
SCOPE: For every dimension $n\ge 2$ and every $2\le p<\infty$, the formalization bounds the $L^p(\mathbb R^n\times[1,2])$ norm of the Euclidean half-wave by a constant times the $W^{s,p}(\mathbb R^n)$ norm of its Schwartz initial data. The Sobolev order is $s=\max(0,(n-1)/2-n/p)+\varepsilon$ for every $\varepsilon>0$, and $s=0$ is allowed at $p=2$. In dimension three this gives the critical $L^3$ estimate with arbitrarily small positive Sobolev loss. The formalization also gives uniform Bochner–Riesz multiplier bounds, spherical extension estimates, and Stein square-function bounds in their strict ranges. The Kakeya maximal operator satisfies an $L^n$ bound with loss $\delta^{-\varepsilon}$ for every $\varepsilon>0$ at tube radii $0<\delta\le 1$. Every subset of $\mathbb R^n$ containing a unit segment in each direction has Hausdorff dimension $n$. The development also proves a logarithmic lower
## PAPER Local-smoothing-for-the-Euclidean-wave-equation-October-25-2026
ABSTRACT: We prove Sogge's local smoothing conjecture for the Euclidean wave equation in every spatial dimension at least two. We deduce the Bochner--Riesz conjecture, maximal estimates for these means, and sharp bounds for Stein's square function. We obtain Fourier restriction estimates for the sphere, the compact paraboloid, and the truncated cone throughout the interior of the conjectured range, as well as local smoothing for the Schr\"odinger equation. We also prove the Kakeya and Nikodym maximal conjectures; in particular, every Euclidean Kakeya set has full Hausdorff dimension.
[theorem[Euclidean local smoothing]] \label{thm:local-smoothing} For \(n\ge2\), \(2\le p<\infty\) and \(\varepsilon>0\), \begin{equation}\label{eq:sogge} \|U(T)f\|_{L^p(\RR^n\times I)} \le C_{n,p,\varepsilon}\|J^{s_+(p)+\varepsilon} f\|_{L^p(\RR^n)} . \end{equation} At \(p=2\) one can take \(\varepsilon=0\).
## PAPER Critical-local-smoothing-for-the-three-dimensional-wave-equation-September-24-2026
ABSTRACT: We prove the critical $L^3$ local smoothing estimate for the wave equation in three spatial dimensions, with every positive Sobolev loss. This resolves Sogge's Euclidean local smoothing conjecture in dimension three.
[theorem[Critical local smoothing]] \label{thm:main} For every $\eps>0$ there exists $C_\eps<\infty$ such that \begin{equation}\label{eq:intro-main} \norm{Uf}_{L^3(\R^3\times[1,2])} \le C_\eps\norm{J^\eps f}_{L^3(\R^3)} \qquad (f\in\mathcal S(\R^3)). \end{equation}
==================
# FAMILY 081: Riesz transforms and rectifiability in higher codimension
SCOPE: The formalized result proves that bounded Riesz transforms force quantitative uniform rectifiability in higher codimension. For $d\ge4$ and $2\le n\le d-2$, an $n$-Ahlfors–David regular measure whose positive hard truncations have one uniform $L^2$ operator bound has big pieces of Lipschitz images. The mass fraction and Lipschitz constant depend only on the dimensions and the stated regularity and operator bounds, and work at every support point and admissible radius, including unbounded support. The variation and principal-value corollary is not included.
## CHALLENGE RieszQuantitative  targets=['OAI.RieszRectifiability.quantitative_higher_codimension_riesz_rectifiability'] defs=[]
theorem quantitative_higher_codimension_riesz_rectifiability : QuantitativeFullStatement := by
  sorry
end RieszRectifiability
DEFS(8): abbrev Ambient, def AdmissibleRadius, def kernel, def truncated, def ADRegularWithConstant, def RieszL2BoundedWithConstant, def BallImageConclusion, def QuantitativeFullStatement
## PAPER Riesz-transforms-and-uniform-rectifiability-in-higher-codimension-September-24-2026
ABSTRACT: We prove that an $n$-Ahlfors--David regular Radon measure on $\R^d$ is uniformly $n$-rectifiable if its $n$-dimensional Riesz transform is uniformly bounded from scalar $L^2(\mu)$ to vector-valued $L^2(\mu)$ over all positive hard truncations, for integers $d\ge4$ and $2\le n\le d-2$. This gives a positive answer to the David--Semmes Riesz-transform question in its remaining higher-codimension range. The conclusion gives uniform big pieces of Lipschitz images of Euclidean balls.
[theorem] \label{thm:main} Let $d\ge4$ and $2\le n\le d-2$ be integers. Let $\mu$ be an $n$-Ahlfors--David regular Radon measure on $\R^d$ satisfying \eqref{eq:riesz-bound}. Then $\mu$ is uniformly $n$-rectifiable in the sense of Definition~\ref{def:ur}. Its constants $\theta$ and $M$ can be chosen in terms of $d,n,C_{\rm AD}$ and $C_{\rm R}$ alone.
==================
# FAMILY 082: Annular variation and dyadic absolute bounds for the triangular Hilbert transform
SCOPE: The formalized result proves the symmetric maximal estimate for the triangular Hilbert transform: for arbitrary complex $F,G\in L^3(\mathbb R^2)$, the $L^{3/2}$ norm of the supremum over all finite hard-truncation intervals is at most $C\|F\|_3\|G\|_3$ for one absolute constant $C$. It also establishes a common full-measure set on which the truncated integrals are defined and almost-everywhere measurability of the maximal output.
## CHALLENGE TriangularHilbert  targets=['OAI.TriangularHilbert.main_estimate'] defs=[]
theorem main_estimate : MainEstimate := by
  sorry
end TriangularHilbert
end
DEFS(9): abbrev Plane, structure Endpoints, def annulus, def integrand, def truncation, def GoodPoint, def maximal, def maximalNorm, def MainEstimate
## PAPER The-maximal-triangular-Hilbert-transform-at-the-symmetric-point-September-24-2026
==================
# FAMILY 083: Hilbert transforms along Lipschitz directions
SCOPE: The formalization proves uniform $L^2$ bounds for short Hilbert transforms along Lipschitz unit vector fields in the plane, including fields depending on both coordinates. For Lipschitz constant $K>0$, every hard truncation with $0<\varepsilon\le R\le1/(10^6K)$ has one universal $L^2$ bound on Schwartz functions, independent of the inner cutoff. At a fixed short scale for $1$-Lipschitz fields, the formalization also gives principal-value and weak-$(2,2)$ estimates and bounded extensions to all of $L^2$. These results establish the stated short-scale form of Stein's question.
## CHALLENGE LipschitzHilbert  targets=['OAI.LipschitzHilbert.main', 'OAI.LipschitzHilbert.uniform_truncation'] defs=[]
theorem main :
    ∃ a : ℝ, a∈Ioo 0 (1/2) ∧ ∃ C : ℝ≥0, 0<C ∧ ShortHilbertConclusion a C := by
  sorry
/-- The same uniform estimate at the reciprocal-Lipschitz truncation scale. -/
theorem uniform_truncation :
    ∃ C : ℝ, 0<C ∧ ∀ K : ℝ≥0, 0<K → ∀ epsilon R : ℝ,
      0<epsilon → epsilon≤R → R≤1/(1000000*(K:ℝ)) →
      ∀ v : Plane → Plane, LipschitzWith K v → (∀ x, ‖v x‖=1) →
      ∀ f : SchwartzMap Plane ℂ,
        eLpNorm (shortTransform v epsilon R f) 2 volume≤ENNReal.ofReal (C*‖f.toLp 2 volume‖) := by
  sorry
end LipschitzHilbert
end
DEFS(8): abbrev Plane, abbrev DirectionPlane, def sample, def shortTransform, def directionalKernel, def twoSidedTruncation, def smoothPrincipalValue, def ShortHilbertConclusion
## PAPER A-uniform-Hilbert-transform-estimate-for-Lipschitz-directions-September-25-2026
ABSTRACT: We prove a uniform \(L^2\) bound for the Hilbert transform along a Lipschitz unit vector field in the plane, with integration restricted to a fixed absolute multiple of the reciprocal Lipschitz seminorm. The bound is uniform in the inner truncation and holds for fields depending on both coordinates. This gives an affirmative answer to Stein's weak-\((2,2)\) conjecture.
[theorem] \label{thm:main} There are absolute constants \(a_*\in(0,1/2)\) and \(C_*<\infty\) such that every Lipschitz field \(v:\R^2\to S^1\) with \(\Lip(v)\le1\) satisfies \[ \sup_{0<\epsilon<a_*} \norm{H_{v,a_*}^{\epsilon}f}_{L^2(\R^2)} \le C_*\norm{f}_{L^2(\R^2)} \qquad(f\in\mathcal S(\R^2)). \] Its symmetric principal value therefore satisfies \[ \norm{H_{v,a_*}f}_2\le C_*\norm f_2, \qquad \big|\{x:|H_{v,a_*}f(x)|>\lambda\}\big| \le C_*^2\lambda^{-2}\norm f_2^2 \quad(\lambda>0). \]
==================
# FAMILY 084: The geometric case of the Erdős similarity conjecture
SCOPE: The formalization proves the dyadic case of the Erdős similarity conjecture. For every $0<\eta<1$, it constructs a compact set $E\subset[0,1]$ of measure greater than $1-\eta$ that contains no affine copy of $\{2^{-n}:n\ge1\}$. Explicitly, for every translation $x$ and every nonzero real dilation $s$, some point $x+s2^{-n}$ lies outside $E$. Both signs of $s$ are included.
## CHALLENGE DyadicAvoidance  targets=['OAI.Problem310.dyadic_affine_avoidance'] defs=[]
theorem dyadic_affine_avoidance :
    ∀ η : ℝ, 0 < η → η < 1 → ∃ E : Set ℝ,
      E ⊆ Set.Icc (0 : ℝ) 1 ∧ IsCompact E ∧
      MeasureTheory.volume E > ENNReal.ofReal (1 - η) ∧
      ∀ x s : ℝ, s ≠ 0 → ∃ n : ℕ, 1 ≤ n ∧
        x + s * dyadicPoint n ∉ E := by
  sorry
end Problem310
end
DEFS(1): def dyadicPoint
## PAPER The-dyadic-case-of-the-Erdos-similarity-conjecture-September-25-2026
ABSTRACT: We construct a compact subset of the unit interval, of measure arbitrarily close to one, that contains no affine copy of the dyadic sequence $\{2^{-n}:n\ge1\}$. The conclusion holds for every translation and every nonzero real dilation, of either sign, proving the dyadic case of the Erd\H{o}s similarity conjecture.
[theorem] \label{thm:main} For every $\eta\in(0,1)$, there is a compact set $E_\eta\subseteq[0,1]$ with $m(E_\eta)>1-\eta$ such that \[ \text{for every }x\in\R\text{ and every }s\in\R\setminus\{0\}, \quad x+sD\nsubseteq E_\eta. \] Equivalently, for every such $x,s$ there is an integer $n\ge1$ with $x+s2^{-n}\notin E_\eta$.
==================
# FAMILY 085: Endpoint Sobolev regularity of centered disk averages
SCOPE: The centered disk maximal operator takes the supremum of averages of $|f|$ over disks centered at each point. The formalization proves that every real $f\in W^{1,1}(\mathbb R^2)$ has a maximal function that is finite almost everywhere, belongs to $W^{1,1}_{\mathrm{loc}}$, and has a globally integrable weak gradient satisfying $\|\nabla Mf\|_1\le C\|\nabla f\|_1$ for one absolute constant $C$. The earlier signed finite-band estimate for smooth compactly supported functions is also retained. The general endpoint statement covers the Sobolev setting of the paper; a BV extension is outside these statements.
## CHALLENGE SignedFiniteBand  targets=['OAI.SignedDisk.CenteredDiskEndpoint.main_signed_finite_band'] defs=[]
theorem main_signed_finite_band : SignedFiniteBandStatement := by
  sorry
end CenteredDiskEndpoint
end SignedDisk
end
DEFS(7): abbrev Plane, def diskAverage, def testPartial, def HasWeakGradient, def gradientNorm, def signedBand, def SignedFiniteBandStatement
## CHALLENGE DiskMaximal  targets=['OAI.CenteredDiskEndpoint.main_endpoint'] defs=[]
theorem main_endpoint : EndpointStatement := by
  sorry
end CenteredDiskEndpoint
end
DEFS(9): abbrev Plane, def absoluteDiskAverage, def maximal, def maximalReal, def testPartial, def HasWeakGradient, def InW11Loc, def gradientNorm, def EndpointStatement
## PAPER An-Endpoint-Gradient-Bound-for-the-Centered-Disk-Maximal-Operator-September-26-2026
ABSTRACT: We prove the endpoint gradient bound $\|\nabla Mf\|_1\le C\|\nabla f\|_1$ for every real-valued $f\in W^{1,1}(\R^2)$, where $Mf(x)$ is the supremum of the averages of $|f|$ over disks centered at $x$, and $C$ is an absolute constant. The maximal function belongs to $W^{1,1}_{\mathrm{loc}}(\R^2)$ and has a globally integrable weak gradient. This gives a positive resolution of the planar centered-disk case of the endpoint question of Haj{\l}asz and Onninen.
[theorem] \label{thm:main} There is an absolute constant $C<\infty$ such that, for every real-valued $f\in W^{1,1}(\R^2)$, the function $Mf$ is locally integrable, belongs to $W^{1,1}_{\mathrm{loc}}(\R^2)$, and satisfies \begin{equation}\label{eq:main} \int_{\R^2}|\nabla Mf|\,\dd x \le C\int_{\R^2}|\nabla f|\,\dd x. \end{equation} In particular, its distributional derivatives are represented by globally integrable functions.
==================
# FAMILY 087: The Mahler conjectures, functional inequalities and polar-product symplectic width
SCOPE: The symmetric Mahler conjecture predicts $|K||K^\circ|\ge4^n/n!$ for every origin-symmetric convex body $K\subset\mathbb R^n$. The formalization establishes this for every $n\ge1$ and characterizes equality exactly by invertible linear images of Hanner bodies, built from intervals using Cartesian products and convex-hull joins. The nonsymmetric Mahler conjecture and the functional inequalities are not included. The general Mahler conjecture gives a sharp lower bound for the volume product of a convex body and its polar. For every $n\ge1$ and compact convex body $K\subset\mathbb R^n$ with nonempty interior, the formalization proves $\inf_{z\in\mathrm{int}\,K}|K|\,|(K-z)^\circ|\ge (n+1)^{n+1}/(n!)^2$. Equality holds exactly when $K$ is a simplex. The paper's functional inequality is outside this selected statement. For an origin-symmetric convex body $K\subset\mathbb R^n$, $n\ge2$, the for
## CHALLENGE MahlerConjecture  targets=['OAI.SymmetricMahler.symmetric_mahler'] defs=[]
theorem symmetric_mahler {n : ℕ} (hn : 1 ≤ n)
    {K : Set (Fin n → ℝ)} (hK : IsCompact K) (hconv : Convex ℝ K)
    (hsym : ∀ x ∈ K, -x ∈ K) (hint : (interior K).Nonempty) :
    (4:ℝ)^n/(Nat.factorial n:ℝ) ≤
      (volume K).toReal*(volume (coordinatePolar K)).toReal := by
  sorry
end
end SymmetricMahler
DEFS(1): def coordinatePolar
## CHALLENGE SymmetricMahlerEquality  targets=['OAI.SymmetricMahler.symmetric_mahler_equality'] defs=[]
theorem symmetric_mahler_equality {n : ℕ} (hn : 1 ≤ n)
    {K : Set (Fin n → ℝ)} (hK : IsCompact K) (hconv : Convex ℝ K)
    (hsym : ∀ x ∈ K, -x ∈ K) (hint : (interior K).Nonempty) :
    ((volume K).toReal * (volume (coordinatePolar K)).toReal =
      (4 : ℝ)^n / (Nat.factorial n : ℝ)) ↔ IsLinearHanner K := by
  sorry
end
end SymmetricMahler
DEFS(5): def coordinatePolar, def hannerProduct, def hannerJoin, inductive IsHanner, def IsLinearHanner
## CHALLENGE GeneralMahler  targets=['OAI.GeneralMahler.general_mahler'] defs=[]
theorem general_mahler {n : ℕ} (hn : 1 ≤ n)
    (K : Set (EuclideanSpace ℝ (Fin n)))
    (hcompact : IsCompact K) (hconvex : Convex ℝ K)
    (hinterior : (interior K).Nonempty) :
    ((n : ℝ) + 1) ^ (n + 1) / (Nat.factorial n : ℝ) ^ 2 ≤ volumeProduct K ∧
      (volumeProduct K = ((n : ℝ) + 1) ^ (n + 1) / (Nat.factorial n : ℝ) ^ 2 ↔
        ∃ vertices : Fin (n + 1) → EuclideanSpace ℝ (Fin n),
          AffineIndependent ℝ vertices ∧ K = convexHull ℝ (range vertices)) := by
  sorry
end GeneralMahler
end
DEFS(3): abbrev Rn, def polarAt, def volumeProduct
## CHALLENGE SymmetricPolar  targets=['OAI.SymmetricPolar.symmetric_polar_main'] defs=[]
theorem symmetric_polar_main {n : ℕ} (hn : 2 ≤ n)
    (K : Set (Position n)) (hK : IsSymmetricConvexBody K) :
    gromovWidth (polarProduct K) = 4 ∧
      ∀ c : ℝ, 0 < c → c < 4 →
        HasSymplecticEmbedding (capacityBall n c) (polarProduct K) := by
  sorry
end SymmetricPolar
DEFS(9): abbrev Position, abbrev Phase, def IsSymmetricConvexBody, def polar, def polarProduct, def capacityBall, def omega0, def HasSymplecticEmbedding, def gromovWidth
## PAPER The-symmetric-Mahler-conjecture-and-its-equality-cases-September-22-2026
ABSTRACT: We resolve the symmetric Mahler conjecture positively, including its equality classification. Every origin-symmetric convex body in $\R^n$ has volume product at least $4^n/n!$, with equality exactly for invertible linear images of Hanner polytopes.
[theorem] \label{thm:main} For every integer $n\ge1$ and every origin-symmetric convex body $K\subset\R^n$, \begin{equation}\label{eq:main-inequality} |K|\,|K^\circ|\ge\frac{4^n}{n!}. \end{equation} Equality holds if and only if $K$ is a linear Hanner body.
## PAPER The-Mahler-Conjecture-for-General-Convex-Bodies-September-22-2026
ABSTRACT: We resolve the Mahler conjecture for general convex bodies positively. For every convex body $K\subset\mathbb R^n$, $n\ge1$, with Santal\'o point $s(K)$, $|K|\,|(K-s(K))^\circ|\ge (n+1)^{n+1}/(n!)^2$, with equality exactly for simplices.
[theorem[General Mahler conjecture]] \label{thm:mahler} For every integer $n\ge1$ and every convex body $K\subset\mathbb R^n$, \[ P(K)\ge\frac{(n+1)^{n+1}}{(n!)^2}. \] Equality holds if and only if $K$ is a simplex.
## PAPER Symplectic-Balls-in-Symmetric-Polar-Products-September-22-2026
ABSTRACT: For every integer $n\ge2$ and every origin-symmetric convex body $K\subset\R^n$, we prove that the Gromov width of $\interior K\times\interior K^\circ$ is $4$. We construct smooth symplectic embeddings of standard balls of every capacity $0<c<4$ into this polar product. Volume preservation then resolves the symmetric Mahler conjecture positively in every dimension.
[theorem] \label{thm:main} For every integer $n\ge2$ and every origin-symmetric convex body $K\subset\R^n$, \[ c_G(U_K)=4. \] More precisely, for every $0<c<4$ there is a smooth symplectic embedding $B^{2n}(c)\hookrightarrow U_K$.
==================
# FAMILY 088: Sharp projection-body inequalities and a counterexample to simplex maximization
SCOPE: Petty's projection-volume conjecture predicts $\displaystyle \frac{|\Pi K|}{|K|^{n-1}}\ge \kappa_{n-1}^{n}\kappa_n^{2-n},$ with equality exactly for ellipsoids; here $\kappa_j$ is the volume of the Euclidean unit ball in dimension $j$. The formalization establishes this for every convex body $K\subset\mathbb R^n$ and every $n\ge4$. Other inequalities in the projection-body family are not included. Brannen's simplex-maximization conjecture predicts that a simplex maximizes normalized projection-body volume $|\Pi K|/|K|^{n-1}$ in dimension $n$. The formalized counterexample is the product of two ten-dimensional simplices. Its normalized projection volume, divided by that of a twenty-dimensional simplex, is $\displaystyle \frac{22{,}355{,}476}{22{,}020{,}096}>1.$ Thus the proposed maximum fails in dimension $20$. The paper's exponential-factor result for every sufficiently large dimension i
## CHALLENGE PettyProjectionVolume  targets=['OAI.PettyProjection.petty_projection_volume'] defs=[]
theorem petty_projection_volume (n : ℕ) (hn : 4 ≤ n)
    (K : Set (Space n)) (hK : IsConvexBody K) :
    pettyConstant n ≤ projectionRatio K ∧
      (projectionRatio K = pettyConstant n ↔ IsEllipsoid K) := by
  sorry
end PettyProjection
end
DEFS(10): abbrev Space, def IsConvexBody, def unitBall, def kappa, def perpendicular, def shadowVolume, def projectionBody, def projectionRatio, def pettyConstant, def IsEllipsoid
## CHALLENGE ProjectionCounterexample  targets=['OAI.ProjectionCounterexample.universal_simplex_upper_bound_false'] defs=[]
theorem universal_simplex_upper_bound_false :
    ¬ (∀ P : Set (E 20), IsConvexBody P → ratio P ≤ ratio (simplex 20)) := by
  sorry
end ProjectionCounterexample
end
DEFS(8): abbrev E, def simplex, def IsConvexBody, def project, def projectionVolume, def projectionBody, def bodyVolume, def ratio
## CHALLENGE ProjectionVolume  targets=['OAI.Paper092.product_counterexample'] defs=[]
theorem product_counterexample :
    (IsCompact productWitness ∧ Convex ℝ productWitness ∧
      (interior productWitness).Nonempty) ∧
    normalizedProjectionVolume productWitness / simplexConstant 20 =
      (121 * (Nat.choose 20 10 : ℝ)) / (21 * (2 : ℝ) ^ 20) ∧
    normalizedProjectionVolume productWitness / simplexConstant 20 =
      (22355476 : ℝ) / 22020096 ∧
    1 < normalizedProjectionVolume productWitness / simplexConstant 20 ∧
    (volume (projectionBody productWitness)).toReal >
      simplexConstant 20 * (volume productWitness).toReal ^ 19 := by
  sorry
end Paper092
end
DEFS(11): def simplexConstant, abbrev Euclidean, def normalHyperplane, def projectionVolume, def brightness, def projectionBody, def normalizedProjectionVolume, def standardSimplex, def firstBlock, def secondBlock, def productWitness
## PAPER Pettys-projection-volume-conjecture-in-dimensions-at-least-four-September-24-2026
ABSTRACT: We prove that ellipsoids uniquely minimize the volume of the projection body among convex bodies of fixed volume in every dimension at least four. This proves Petty's projection-volume conjecture in these dimensions.
[theorem] \label{thm:main} For every integer $n\ge4$ and every convex body $K\subset\R^n$, \begin{equation}\label{eq:main} \frac{|\Pi K|}{|K|^{n-1}} \ge \kappa_{n-1}^{\,n}\kappa_n^{\,2-n}. \end{equation} Equality holds if and only if $K=a+TB_2^n$ for some $a\in\R^n$ and some invertible linear map $T$.
## PAPER A-product-counterexample-to-the-simplex-maximum-for-projection-body-volume-September-24-2026
ABSTRACT: The product of two ten-dimensional simplices has larger normalized projection-body volume than a twenty-dimensional simplex. This gives a counterexample to Brannen's proposed simplex maximum.
[theorem] \label{thm:counterexample} Let \(T_{10}=\conv(0,e_1,\ldots,e_{10})\subset\R^{10}\), where the \(e_i\) are the coordinate unit vectors, and let \(K=T_{10}\times T_{10}\subset\R^{20}\). Then \[ \frac{R_{20}(K)}{c_{20}} =\frac{121\binom{20}{10}}{21\cdot2^{20}} =\frac{22\,355\,476}{22\,020\,096}>1. \] Thus \(K\) violates \eqref{eq:proposed-bound} in dimension twenty.
==================
# FAMILY 089: Bounded-distortion <i>L</i><sub>1</sub> embeddings of planar and bounded-treewidth graphs
SCOPE: The planar case of the Gupta–Newman–Rabinovich–Sinclair embedding problem asks for a universal distortion bound in $L_1$. The formalized result gives one constant $C$ for every finite connected planar graph with arbitrary positive real edge lengths: its weighted shortest-path metric embeds into real $L_1$ with distortion at most $C$. The constant is independent of the number of vertices and the ratios between edge lengths; singleton graphs are included. The formalized result gives a uniform $L_1$ embedding bound for each bounded-treewidth class. For every bag-size bound $k\ge2$, there is a constant $C(k)$ such that the weighted shortest-path metric of every nonempty finite connected graph with a tree decomposition of bag size at most $k$ embeds into finite-dimensional real $L_1$ with distortion at most $C(k)$. Edge lengths may be arbitrary positive real numbers, and the constant is indep
## CHALLENGE PlanarL1  targets=['OAI.PlanarL1.planar_graph_metrics_embed_L1'] defs=[]
theorem planar_graph_metrics_embed_L1 : MainStatement := by
  sorry
end PlanarL1
DEFS(4): def IsPlanar, def walkLength, def graphDistance, def MainStatement
## CHALLENGE BoundedTreewidthL1  targets=['OAI.BoundedTreewidthL1.main_theorem'] defs=[]
theorem main_theorem : MainStatement := by
  sorry
end BoundedTreewidthL1
end
DEFS(5): def walkLength, def shortestPathDistance, def HasTreeDecomposition, def HasL1Embedding, def MainStatement
## PAPER Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026
ABSTRACT: We prove that every finite connected planar graph with arbitrary positive real edge lengths embeds into real $L_1$ with a universal distortion bound. This resolves the planar embedding conjecture positively.
[theorem] \label{thm:main} There is a finite universal constant $C\ge1$ with the following property. For every finite connected planar graph $G=(V,E)$ with strictly positive real edge lengths, there exist a measure space $(\Omega,\mathcal F,\mu)$ and a map $f:V\to L_1(\Omega,\mathcal F,\mu;\R)$ such that \[ d_G(x,y)\le\|f(x)-f(y)\|_1\le C d_G(x,y) \qquad(x,y\in V). \]
## PAPER L1-Embeddings-of-Graphs-of-Bounded-Treewidth-September-23-2026
ABSTRACT: For every fixed treewidth bound, the shortest-path metrics of finite connected graphs with arbitrary positive real edge lengths embed into real $L_1$ with uniformly bounded distortion. This resolves the bounded-treewidth case of the Gupta--Newman--Rabinovich--Sinclair conjecture positively.
[theorem] \label{thm:main} For every integer $k\ge2$ there is a finite constant $C_k\ge1$ with the following property. If a finite connected graph $G=(V,E)$ admits a tree decomposition with bags of size at most $k$, then, for every edge-length function $\ell:E\to(0,\infty)$, there is a map $F$ from $V$ into a real $L_1$ space such that \begin{equation}\label{eq:main-embedding} d_{G,\ell}(u,v) \le \|F(u)-F(v)\|_1 \le C_k\,d_{G,\ell}(u,v) \qquad(u,v\in V). \end{equation} The constant is independent of the number of vertices, the depth of the decomposition, and all ratios of edge lengths.
==================
# FAMILY 090: Triangular-lattice optimality, long-range Riesz and Coulomb energies, and spherical logarithmic energy
SCOPE: The formalization proves that the density-one triangular lattice minimizes lower energy per particle among all locally finite planar configurations of centered-disk density one, for every nonnegative completely monotone function of squared distance. Infinite energies are allowed in the comparison. It also constructs sharp radial Schwartz minorants for every Gaussian potential: each minorant lies below the Gaussian, has nonnegative real Fourier transform, agrees with the Gaussian at nonzero triangular-lattice points, and vanishes on nonzero dual-lattice points after Fourier transformation. For the stated parameter range, the formalization includes the explicit atomic interpolation construction. The planar Cohn–Elkies sharpness conjecture asks whether the two-point Fourier method attains the optimal circle-packing density. The formalization constructs a radial Schwartz function $f$ on $\ma
## CHALLENGE AtomicGaussian  targets=['OAI.AtomicTriangular.sharp_gaussian_minorants_atomic'] defs=[]
theorem sharp_gaussian_minorants_atomic (α : ℝ) (hα : 0 < α) :
    ∃ f : SchwartzMap Plane ℝ,
      Radial f ∧ (∀ x, f x ≤ gaussian α x) ∧
      (∀ w, (realFourier f w).im = 0 ∧ 0 ≤ (realFourier f w).re) ∧
      (∀ a ∈ A, a ≠ 0 → f a = gaussian α a) ∧
      (∀ w ∈ dualA, w ≠ 0 → realFourier f w = 0) ∧
      (1 ≤ α → Construction.HasAtomicConstruction α f) := by
  sorry
end AtomicTriangular
end
DEFS(68): abbrev Plane, def b, def triangularPoint, def A, def dualA, def gaussian, def Radial, def realFourier, def b, def h, def H, def eta, def kappa, def residues, def residue, def Node, def FiniteNodes, def sineFactor, def P, def dBasis, def cBasis, def finiteC, def finiteD, def phase, def atomFactor, def atomPolynomial, def cAtomPolynomial, def dAtomPolynomial, def fourierCoeff, def frequency
## CHALLENGE TriangularEnergy  targets=['OAI.AtomicTriangular.universal_energy_minimum'] defs=[]
theorem universal_energy_minimum (g : ℝ → ℝ) (C : Set Plane)
    (hg : AdmissiblePotential g) (hC : LocallyFinite C) (hd : DensityOne C) :
    latticeEnergy g ≤ energy g C ∧ latticeEnergy g = energy g A := by
  sorry
end AtomicTriangular
end
DEFS(20): abbrev Plane, def LocallyFinite, def diskPoints, def diskCount, def DensityOne, def AdmissiblePotential, def diskEnergy, def energy, abbrev Plane, def b, def triangularPoint, def A, abbrev LocallyFinite, abbrev diskPoints, abbrev diskCount, abbrev DensityOne, abbrev AdmissiblePotential, abbrev diskEnergy, abbrev energy, def latticeEnergy
## CHALLENGE TriangularGaussian  targets=['OAI.AtomicTriangular.sharp_gaussian_minorants_with_construction'] defs=[]
theorem sharp_gaussian_minorants_with_construction (α : ℝ) (hα : 0 < α) :
    ∃ f : SchwartzMap Plane ℝ,
      Radial f ∧ (∀ x, f x ≤ gaussian α x) ∧
      (∀ w, (realFourier f w).im = 0 ∧ 0 ≤ (realFourier f w).re) ∧
      (∀ a ∈ A, a ≠ 0 → f a = gaussian α a) ∧
      (∀ w ∈ dualA, w ≠ 0 → realFourier f w = 0) ∧
      (1 ≤ α → AtomicConstruction α f) := by
  sorry
end AtomicTriangular
end
DEFS(67): abbrev Plane, def b, def triangularPoint, def A, def dualA, def gaussian, def Radial, def realFourier, def b, def h, def H, def eta, def kappa, def residues, def residue, def Node, def FiniteNodes, def sineFactor, def P, def dBasis, def cBasis, def finiteC, def finiteD, def phase, def atomFactor, def atomPolynomial, def cAtomPolynomial, def dAtomPolynomial, def fourierCoeff, def frequency
## CHALLENGE PlanarPacking  targets=['OAI.sharp_fourier_certificate'] defs=[]
theorem sharp_fourier_certificate :
    ∃ f : SchwartzMap SharpPlanar.Plane ℝ, SharpPlanar.SharpCertificate f := by
  sorry
DEFS(4): abbrev Plane, def Radial, def fourier, def SharpCertificate
## PAPER An-atomic-certificate-for-triangular-lattice-universal-optimality-September-26-2026
ABSTRACT: We prove that the density-one triangular lattice minimizes the lower energy per particle for every nonnegative completely monotone function of squared distance, among all locally finite planar configurations of centered disk density one. The comparison includes infinite energies. The proof constructs sharp Gaussian Fourier minorants using an atomic interpolation certificate.
[theorem[Universal energy minimum]] \label{thm:universal} For every smooth nonnegative completely monotone function $g$ on $(0,\infty)$ and every locally finite planar set $\mathcal C$ of centered disk density one, \[ E_g(\mathcal C)\ge \sum_{a\in A\setminus\{0\}}g(|a|^2)=E_g(A). \] The comparison and the equality are in the extended nonnegative reals.
## PAPER A-sharp-Fourier-certificate-for-planar-circle-packing-September-23-2026
ABSTRACT: We resolve the planar Cohn--Elkies sharpness conjecture: the two-point Fourier bound attains the optimal circle-packing density $\pi/(2\sqrt3)$. We construct a radial Schwartz certificate and prove its global sign conditions using rigorous interval arithmetic and analytic estimates. The same certificate recovers the classical uniqueness of the triangular packing among periodic equality cases.
[theorem[Sharp Fourier certificate]] \label{intro:main} There is a real radial Schwartz function $f:\RR^2\to\RR$ such that \begin{equation}\label{intro:conditions} \widehat f(0)=1,\qquad f(0)=\frac{2}{\sqrt3},\qquad \widehat f(\xi)\ge0\quad(\xi\in\RR^2),\qquad f(x)\le0\quad(|x|\ge1). \end{equation}
==================
# FAMILY 091: Logarithmic and <i>L</i><sub><i>p</i></sub> Brunn–Minkowski inequalities and the B-conjecture
SCOPE: The logarithmic Brunn–Minkowski conjecture asserts that logarithmic interpolation of origin-symmetric convex bodies preserves the geometric-mean lower bound for volume. The formalized result proves, for every dimension $n\ge1$, such bodies $K,L\subset\mathbb R^n$, and $0\le t\le1$, that their logarithmic Wulff combination has volume at least $|K|^{1-t}|L|^t$. It assumes neither boundary smoothness nor coordinatewise unconditionality.
## CHALLENGE LogBrunnMinkowski  targets=['OAI.LogBrunnMinkowski.main'] defs=[]
theorem main (n : ℕ) (hn : 1 ≤ n) (K L : Set (Space n))
    (hK : IsConvexBody K) (hL : IsConvexBody L)
    (hsK : OriginSymmetric K) (hsL : OriginSymmetric L)
    (t : ℝ) (ht0 : 0 ≤ t) (ht1 : t ≤ 1) :
    (volume K) ^ (1 - t) * (volume L) ^ t ≤ volume (logCombination K L t) := by
  sorry
end LogBrunnMinkowski
end
DEFS(6): abbrev Space, def IsConvexBody, def OriginSymmetric, def support, def wulff, def logCombination
## PAPER The-logarithmic-Brunn-Minkowski-conjecture-September-23-2026
ABSTRACT: We prove the logarithmic Brunn--Minkowski conjecture for arbitrary origin-symmetric convex bodies in every dimension. The theorem also gives the symmetric $L_p$ Brunn--Minkowski inequality for every $0<p<1$. Combined with Saroglou's transfer theorem and a support-subspace reduction, it yields the logarithmic inequality for every even log-concave Radon measure and the scalar-dilation $(B)$-conjecture.
[theorem[Even logarithmic Brunn--Minkowski inequality]] \label{thm:main} Let $n\ge1$ and let $K,L\subset\R^n$ be convex bodies satisfying $K=-K$ and $L=-L$. For every $0\le\lambda\le1$, \begin{equation}\label{eq:main} \left|\mathcal W[h_K^{1-\lambda}h_L^\lambda]\right| \ge |K|^{1-\lambda}|L|^\lambda. \end{equation}
==================
# FAMILY 092: The optimal order of convex-body covering density
SCOPE: The formalized result gives an absolute constant $C>0$ such that every convex body $K\subset\mathbb R^n$, $n\ge2$, admits a covering by translates along one full-rank lattice $L$ with density $|K|/\mathrm{covol}(L)\le Cn\log n$. The covering is exact, and no symmetry, boundary regularity, or volume normalization is assumed. The formalization determines the order of the largest covering density in dimension $n$. For all sufficiently large $n$, the suprema of translative covering density and lattice covering density are each bounded above and below by absolute positive multiples of $n\log n$, both over all convex bodies and over centrally symmetric convex bodies.
## CHALLENGE SingleLatticeCovering  targets=['OAI.SingleLatticeCovering.single_lattice_covering'] defs=[]
theorem single_lattice_covering :
    ∃ C : ℝ, 0 < C ∧ ∀ (n : ℕ), 2 ≤ n →
      ∀ (K : Set (Space n)), IsConvexBody K →
        ∃ (L : Submodule ℤ (Space n)) (_ : DiscreteTopology L),
          IsZLattice ℝ L ∧ LatticeCovers K L ∧
            (volume K).toReal / ZLattice.covolume L ≤ C * (n : ℝ) * Real.log (n : ℝ) := by sorry
end SingleLatticeCovering
DEFS(3): abbrev Space, def IsConvexBody, def LatticeCovers
## CHALLENGE CoveringDensity  targets=['OAI.CoveringOrder.optimal_order'] defs=[]
DEFS(23): abbrev Space, structure LatticeCover, def euclideanVolume, def euclideanCovolume, def latticeDensity, def thetaL, abbrev Space, def cube, def LocallyFiniteCenters, def Covers, def ConvexBody, def CentrallySymmetric, def upperCenterIntensity, def thetaT, abbrev Body, abbrev SymmetricBody, def translativeSup, def symmetricTranslativeSup, def latticeSup, def symmetricLatticeSup, def orderBounds, def OptimalOrder, theorem CoveringOrder.optimal_order
## PAPER A-single-lattice-covering-bound-of-order-n-log-n-September-23-2026
ABSTRACT: Every convex body in $\R^n$, $n\ge2$, admits a covering by translates along one full-rank lattice with density at most $Cn\log n$, for an absolute constant $C$. No symmetry or boundary regularity is assumed.
[theorem] \label{thm:main} There is an absolute constant $C>0$ such that, for every integer $n\ge2$ and every convex body $K\subset\R^n$, one full-rank lattice $\Lambda$ satisfies \[ K+\Lambda=\R^n,\qquad \frac{\vol_n(K)}{\det\Lambda}\le Cn\log n. \] No symmetry or boundary regularity is assumed.
## PAPER Translative-covering-densities-of-order-n-log-n-September-23-2026
ABSTRACT: For every sufficiently large dimension $n$, we construct a centrally symmetric convex body whose translative covering density exceeds $c n\log n$, where $c>0$ is absolute. This disproves the existence of a universal linear upper bound and matches the order of Rogers' upper bound.
[theorem] \label{thm:main} There are absolute constants $c>0$ and $n_0$ such that, for every integer $n\ge n_0$, some centrally symmetric convex body $K_n\subset\mathbb R^n$ satisfies \[ \theta_T(K_n)>c n\log n. \]
==================
# FAMILY 094: Subpolynomial dimension reduction in <i>L</i><sub><i>p</i></sub>
SCOPE: For $p>1$, $p\ne2$, the formalization bounds the least dimension needed to embed every $n$-point subset of real $L_p$ with distortion $D$. For each fixed $D>1$, there is a constant $C=C(p,D)$ such that this dimension lies between $\log n/\log(1+2D)$ and $\exp(C(\log n)^{\gamma(p)})$ for every $n\ge2$, where $\gamma(p)=2-p$ for $p<2$ and $1-2/p$ for $p>2$. At distortion $1$ and $n\ge9$, it lies between $\lfloor(n-1)/4\rfloor^2$ and $\binom n2$. The least dimension is attained, and its logarithm divided by $\log n$ tends to $0$ for $D>1$ and to $2$ for $D=1$.
## CHALLENGE SubpolynomialLp  targets=['OAI.SubpolynomialLp.source_main'] defs=[]
theorem source_main (p : ℝ) (hp : 1 < p) (hp2 : p ≠ 2) :
    (∀ D : ℝ, 1 < D → ∃ C : ℝ, ∀ n : ℕ, 2 ≤ n →
      GoodDimension.{u} p n D (dimension.{u} p n D) ∧
      Real.log (n : ℝ) / Real.log (1 + 2 * D) ≤ (dimension.{u} p n D : ℝ) ∧
      (dimension.{u} p n D : ℝ) ≤ Real.exp (C * Real.log (n : ℝ) ^ gamma p)) ∧
    (∀ n : ℕ, 9 ≤ n →
      GoodDimension.{u} p n 1 (dimension.{u} p n 1) ∧
      ((n - 1) / 4) ^ 2 ≤ dimension.{u} p n 1 ∧
      dimension.{u} p n 1 ≤ n.choose 2) ∧
    (∀ D : ℝ, 1 ≤ D →
      Tendsto (fun n : ℕ => Real.log (dimension.{u} p n D : ℝ) / Real.log (n : ℝ))
        atTop (𝓝 (if 1 < D then 0 else 2))) := by
  sorry
end SubpolynomialLp
end
DEFS(4): def coordinateDistance, def GoodDimension, def dimension, def gamma
## PAPER Subpolynomial-dimension-reduction-in-Lp-September-23-2026
ABSTRACT: For every fixed $1<p<\infty$ and $D>1$, every $n$-point subset of a real $L_p$ space embeds into $\ell_p^d$ with distortion at most $D$ and subpolynomial dimension $d=n^{o(1)}$. The target has the same exponent $p$, and the embedding need not be linear.
[theorem] \label{thm:main} Fix $1<p<\infty$, $p\ne2$, and put \[ \gamma(p)= \begin{cases} 2-p,&1<p<2,\\ 1-2/p,&2<p<\infty. \end{cases} \] For every $D>1$ there is a constant $C_{p,D}<\infty$ such that, for every integer $n\ge2$, \begin{equation}\label{eq:main-bounds} \frac{\log n}{\log(1+2D)} \le d_p(n,D) \le \exp\!\bigl(C_{p,D}(\log n)^{\gamma(p)}\bigr). \end{equation} For exact embeddings, \begin{equation}\label{eq:exact-bounds} \left\lfloor\frac{n-1}{4}\right\rfloor^2 \le d_p(n,1)\le\binom n2\qquad(n\ge9). \end{equation} Consequently, \[ \lim_{n\to\infty}\frac{\log d_p(n,D)}{\log n} =\begin{cases}0,&D>1,\\2,&D=1.\end{cases} \]
==================
# FAMILY 095: Hyperbolicity cones without semidefinite lifts
SCOPE: The generalized Lax conjecture predicts that every hyperbolicity cone is spectrahedral. The formalized counterexample is an explicit homogeneous polynomial of degree $20$ in $23$ real variables. It is hyperbolic, but its closed hyperbolicity cone cannot be represented as the positive-semidefinite region of any finite real symmetric linear matrix pencil, in any positive matrix size.
## CHALLENGE HyperbolicCones  targets=['OAI.Paper256.main_result'] defs=[]
theorem main_result :
    Module.finrank ℝ Ambient = 23 ∧
    polynomial.IsHomogeneous 20 ∧
    polynomial.totalDegree = 20 ∧
    MvPolynomial.eval (coordinates basePoint) polynomial = 1 ∧
    (∀ (x : Ambient) (z : ℂ), (linePolynomial x).aeval z = 0 → z.im = 0) ∧
    ∀ (N : ℕ) (_hN : 0 < N) (L : Ambient →ₗ[ℝ] Sym N),
      cone ≠ {x | (L x : Mat N ℝ).PosSemidef} := by
  sorry
end Paper256
end
DEFS(15): abbrev Mat, abbrev Sym, instance instFiniteDimensionalSym, abbrev Ambient, abbrev SymIndex, abbrev Coord, def qMatrix, def phi, def matrixValue, def symmetricCoordinates, def polynomial, def coordinates, def basePoint, def linePolynomial, def cone
## PAPER A-Nonspectrahedral-Hyperbolicity-Cone-September-24-2026
ABSTRACT: We construct a homogeneous polynomial of degree $16$ in $23$ real variables whose hyperbolicity cone has no representation by a finite homogeneous real symmetric linear matrix inequality. This disproves the geometric Generalized Lax conjecture.
[theorem] \label{thm:main} The polynomial \eqref{eq:polynomial} is homogeneous of degree $20$ and hyperbolic with respect to $e=(I_4,I_4,0)$, with $p(e)=1$. Its closed hyperbolicity cone $K=\Lambda_+(p,e)$ is not spectrahedral: for every finite $N\geq1$ and every real linear map $L:\Sym^4\times\Sym^4\times\R^3\to\Sym^N$, \[ K\ne\{(X,Z,y):L(X,Z,y)\succeq0\}. \]
==================
# FAMILY 096: The Gaussian propeller conjecture in every dimension
SCOPE: The Gaussian propeller problem asks how large the sum of squared Gaussian first moments can be over a partition. The formalized result proves the sharp bound $9/(8\pi)$ for every positive dimension and every positive number of labelled cells, allowing empty cells and arbitrary masses. In dimension at least two with at least three cells, three planar sectors of angle $120^\circ$, extended in orthogonal directions, attain equality. The separate Gaussian-maxima and kernel-clustering consequences are not included.
## CHALLENGE GaussianPropeller  targets=['OAI.GaussianPropeller.all_partitions'] defs=[]
theorem all_partitions : AllPartitions := by
  sorry
end GaussianPropeller
DEFS(8): abbrev Space, def gaussian, def IsPartition, def centroid, def value, def coord, def propeller, def AllPartitions
## PAPER The-Gaussian-Propeller-Bound-in-Every-Dimension-September-24-2026
ABSTRACT: We prove the Gaussian propeller conjecture: for every finite measurable partition of a Euclidean space, the sum of the squared lengths of its Gaussian first moments is at most $9/(8\pi)$. For dimension at least two and at least three cells, three planar sectors of angle $2\pi/3$, extended by an orthogonal Euclidean factor, attain the bound.
[theorem] \label{thm:main} For all positive integers $d$ and $k$, every measurable partition $(A_1,\ldots,A_k)$ of $\mathbb R^d$ satisfies \[ \sum_{i=1}^k\left\|\int_{A_i}x\,d\gamma_d(x)\right\|^2 \le\frac9{8\pi}. \] Empty cells are allowed. The constant is sharp whenever $d\ge2$ and $k\ge3$: three planar sectors of angle $2\pi/3$, multiplied by the orthogonal complement of their plane, attain equality, with any further cells empty.
==================
# FAMILY 097: The Euclidean Steinitz–Bergström bound
SCOPE: The formalized result gives the Euclidean Steinitz–Bergström bound with one absolute constant $C$. For every finite family of vectors in the unit ball of $\mathbb R^d$, signs can be chosen so that every prefix in the prescribed order has norm at most $C\sqrt d$. When the vector sum is zero, a permutation makes every unsigned prefix satisfy the same bound. Repeated and zero vectors are included. The result is existential and does not supply an online algorithm.
## CHALLENGE SteinitzBergstrom  targets=['OAI.EuclideanSteinitzBergstrom.main'] defs=[]
theorem main : ∃ C : ℝ, SignedPrefixBound C ∧ OrderingPrefixBound C := by
  sorry
end EuclideanSteinitzBergstrom
DEFS(3): abbrev Vector, def SignedPrefixBound, def OrderingPrefixBound
## PAPER The-Euclidean-Steinitz-Bergstrom-theorem-September-24-2026
ABSTRACT: Every prescribed-order finite sequence of vectors in the Euclidean unit ball of $\R^d$ has one signing for which every signed prefix has norm at most $C\sqrt d$, with $C$ absolute and independent of the sequence length. Consequently, every indexed zero-sum family of unit-ball vectors admits an ordering with the same bound for its unsigned partial sums. This determines the Euclidean Steinitz constant up to absolute factors, $S_2(d)=\Theta(\sqrt d)$, and resolves the Euclidean Steinitz--Bergstr\"om conjecture.
[theorem[Prescribed-order signed prefixes]] \label{thm:signing} There is an absolute constant $C$ such that, for all integers $d,N\ge1$ and every sequence $v_1,\ldots,v_N\in\R^d$ with $\lVert v_i\rVert_2\le1$, there are signs $\varepsilon_1,\ldots,\varepsilon_N\in\{-1,1\}$ for which \[ \max_{0\le k\le N} \left\lVert\sum_{i=1}^k\varepsilon_i v_i\right\rVert_2\le C\sqrt d. \] The same signs control all prefixes, and $C$ is independent of $d$, $N$ and the sequence.
==================
# FAMILY 098: Compact counterexamples to bi-Lipschitz dimension reduction
SCOPE: The formalized result gives a doubling subset of real $\ell_2$, with doubling constant at most $76800$, that admits no bi-Lipschitz embedding into any finite-dimensional Euclidean space at any finite distortion. A companion gives one universal doubling constant such that every infinite-dimensional real Banach space contains a compact doubling subset with no bi-Lipschitz embedding into any finite-dimensional normed space.
## CHALLENGE DoublingHilbert  targets=['OAI.DoublingHilbert.main'] defs=[]
theorem main : ∃ S : Set RealL2,
    DoublingAtMost S 76800 ∧
      ∀ k : ℕ, 0 < k → ¬ AdmitsBiLipschitzEmbedding S k := by
  sorry
end DoublingHilbert
DEFS(3): abbrev RealL2, def DoublingAtMost, def AdmitsBiLipschitzEmbedding
## CHALLENGE CompactBanach  targets=['OAI.CompactBanach.main'] defs=[]
theorem main : ∃ Λ : ℕ, ∀ (B : Type u) [NormedAddCommGroup B] [NormedSpace ℝ B]
    [CompleteSpace B], ¬ FiniteDimensional ℝ B →
    ∃ K : Set B, IsCompact K ∧ DoublingAtMost K Λ ∧
      ∀ (E : Type v) [NormedAddCommGroup E] [NormedSpace ℝ E]
        [FiniteDimensional ℝ E], ¬ AdmitsBiLipschitzEmbedding K E := by
  sorry
end CompactBanach
DEFS(2): def DoublingAtMost, def AdmitsBiLipschitzEmbedding
## PAPER A-doubling-Hilbert-subset-with-no-finite-dimensional-bi-Lipschitz-embedding-September-25-2026
ABSTRACT: Every infinite-dimensional real Banach space contains a compact doubling subset that admits no bi-Lipschitz embedding into any finite-dimensional real normed space. The doubling constant has a universal bound, independent of the ambient Banach space. This answers the Lang--Plaut problem negatively, even for compact subsets of Hilbert space.
[theorem] \label{thm:main} There is a fixed subset $S$ of real $\ell_2$, equipped with its induced Hilbert distance, whose doubling constant is at most $76800$ and which admits no bi-Lipschitz embedding into $\R^k$ for any positive integer $k$, at any finite distortion.
==================
# FAMILY 099: The sharp exponential scale of edit-distance distortion
SCOPE: The formalization determines the exponential scale of the least $\ell_1$ distortion of unit-cost edit distance on strings of length at most $d$. For every sufficiently large $d$, uniformly over finite alphabets with at least two symbols, the distortion lies between $\exp(c\sqrt{\log d\,\log\log d})$ and $\exp(C\sqrt{\log d\,\log\log d})$ for absolute constants $c,C>0$. The lower bound has a witness consisting of binary strings of one common length, and the same scale controls the supremum over finite alphabets. The formalization gives two finite-circle constructions of binary strings whose least $\ell_1$ distortion is at least $\exp(c\sqrt{\log d\,\log\log d})$ for all sufficiently large length caps $d$. The witnesses use strings of one common length and include the binary coding transfers with their stated uniform bounds. It also gives a finite histogram embedding with distortion at mos
## CHALLENGE EditDistance  targets=['OAI.edit_distance_main'] defs=[]
theorem edit_distance_main : EditDistortion.MainClaim.{u} := by
  sorry
DEFS(12): inductive Step, inductive Script, def edit, abbrev L1, def distortion, def leastDistortion, abbrev Words, def E, def exponentScale, def alphabetSup, def BinaryWitness, def MainClaim
## CHALLENGE FiniteCircle  targets=['OAI.finiteCircle_fullMain'] defs=[]
theorem finiteCircle_fullMain : FiniteCircle.FullMain := by
  sorry
DEFS(42): inductive EditStep, inductive EditScript, def editDistance, def lcs, def deficit, abbrev Words, abbrev RealL1, def distortion, def optimalDistortion, def E, def setDistortion, def alphabetSupremum, def exponentScale, def encode, def interval, def OffsetLocal, def indexSpan, def AnchorLocal, def SubstitutionBounds, def TwoCodes, def period, def circleSize, def MaskPrimes, def ExcludedPrimes, abbrev MaskTag, def maskTags, def MaskAlphabet, instance maskAlphabetFintype, def MaskState, def shiftMaskState
## CHALLENGE BinaryEditLower  targets=['OAI.TreeEdit.binary_lower_bound'] defs=[]
theorem binary_lower_bound :
    ∃ c : ℝ, 0 < c ∧ ∃ d₀ : ℕ, ∀ d : ℕ, d₀ ≤ d →
      ∃ n : ℕ, 1 ≤ n ∧ n ≤ d ∧
        ∃ W : Finset (Word Bool n), 2 ≤ W.card ∧
          growth c d ≤ binarySetDistortion W := by
  sorry
end TreeEdit
DEFS(9): inductive EditStep, inductive EditScript, def ed, abbrev RealL1, abbrev Word, def distortion, def c1, def binarySetDistortion, def growth
## CHALLENGE TreeEdit  targets=['OAI.TreeEdit.binary_torus'] defs=[]
theorem binary_torus : BinaryLowerBound := by
  sorry
end TreeEdit
DEFS(7): inductive EditStep, inductive EditScript, def ed, abbrev RealL1, def distortion, def c1, def BinaryLowerBound
## PAPER Edit-Distance-in-l1-Matching-Bounds-up-to-Constants-in-the-Exponent-September-27-2026
ABSTRACT: We determine the exponential scale of the least $\ell_1$ distortion of unit-cost edit distance on all strings of length at most $d$. For every sufficiently large $d$, uniformly over finite alphabets of size at least two, the distortion lies between $\exp(c\sqrt{\log d\,\log\log d})$ and $\exp(C\sqrt{\log d\,\log\log d})$ for absolute constants $c,C>0$. The lower bound already holds on binary strings of one common length. Thus the order of logarithmic distortion is sharp up to absolute constants.
[theorem] \label{thm:main} There are absolute constants $c,C>0$ and an integer $d_0$ such that, for every integer $d\ge d_0$ and every finite alphabet $\Sigma$ with $|\Sigma|\ge2$, \begin{equation}\label{eq:main} \exp\!\bigl(c\sqrt{\log d\,\log\log d}\bigr) \le E_\Sigma(d)\le \exp\!\bigl(C\sqrt{\log d\,\log\log d}\bigr). \end{equation} The lower bound is witnessed by a subset of binary strings of one common length at most $d$. The same bounds hold for $\sup_{\Sigma:\,2\le|\Sigma|<\infty}E_\Sigma(d)$.
## PAPER Finite-Circle-Obstructions-Binary-Codes-and-Histogram-Embeddings-for-Edit-Distance-September-27-2026
ABSTRACT: We give two finite-circle constructions of binary strings whose least $\ell_1$ distortion is $\exp(\Omega(\sqrt{\log d\,\log\log d}))$, where $d$ bounds their length. Both constructions supply words of one common length for every sufficiently large cap. Two direct binary coding arguments transfer the constructions with absolute distortion and logarithmic block width. We also develop the overlapping-substring method of Ostrovsky and Rabani into a complete finite histogram embedding at the same exponential scale, uniformly over all finite alphabets and all words of length at most $d$, including the empty word.
[theorem] \label{thm:main} There are absolute constants $c,C>0$ and an integer $d_0$ such that, for every integer $d\geq d_0$ and every finite alphabet $\Sigma$ with $|\Sigma|\geq2$, \begin{equation}\label{eq:main} \exp\!\bigl(c\sqrt{\log d\,\log\log d}\bigr) \leq E_\Sigma(d)\leq \exp\!\bigl(C\sqrt{\log d\,\log\log d}\bigr). \end{equation} Each of our two lower constructions supplies a binary subset whose words have one common length at most $d$ and whose least $\ell_1$ distortion satisfies the lower bound. The upper bound is realized by a deterministic finite-dimensional map.
## PAPER Tree-Constructions-for-the-l1-Distortion-of-Binary-Edit-Distance-September-27-2026
ABSTRACT: We give two independent constructions of binary words of one length at most $d$ whose ordinary edit-distance metrics require $\ell_1$ distortion $\exp(\Omega(\sqrt{\log d\,\log\log d}))$ for every sufficiently large $d$. We also prove a constant-distortion binary conversion for one prescribed input length. Together with the companion upper embedding theorem, these lower bounds determine the order of logarithmic distortion uniformly over finite alphabets with at least two symbols.
[theorem[Binary lower bound]] \label{thm:binary} There are an absolute constant $c>0$ and an integer $d_0$ such that, for every integer $d\geq d_0$, there exist an integer $1\leq n\leq d$ and a finite set $\mathcal W\subseteq\{0,1\}^n$ with $|\mathcal W|\geq2$ satisfying \[ c_1(\mathcal W,\ED) \geq \exp\!\left(c\sqrt{\log d\,\log\log d}\right). \]
==================
# FAMILY 100: Cylinder coverings below the half-area bound
SCOPE: The half-area cylinder-covering conjecture predicts that a cylinder cover of a convex body has total perpendicular-base area at least half its smallest projection area. The formalization constructs finite covers of a regular tetrahedron by cylinders with compact triangular bases whose total area is strictly below that bound. For the explicit small parameter $\varepsilon$, the normalized area is $1/2-(13/6000)\varepsilon^2+O(\varepsilon^4)$, giving the strict saving. It also gives a counterexample to the directionwise normalized half-bound. The broader Comparator file includes the companion ruled-set and radial-sweep approximation results. The formalization approximates compact ruled families of line segments by finite cylinder covers with perpendicular-base area at most the integral projection cost plus any prescribed positive error. The selected results cover the stated $C^1$ hyperbolic
## CHALLENGE CylinderCovering  targets=['OAI.CylinderCovering.fourPaperMain'] defs=[]
theorem fourPaperMain :
    AngularExplicitStatement ∧
    RuledApproximation.HyperbolicStatement ∧
    RuledApproximation.NilpotentC1Statement ∧
    RegularParallelogramCounterexampleStatement ∧
    RegularOpenCounterexampleStatement ∧
    RadialSweep.AlignedStatement ∧
    RadialSweep.ActualSweepStatement := by
  sorry
end CylinderCovering
DEFS(108): abbrev Space, def H, def point, def K, def projection, def area, def shadowArea, def A_min, structure TriCylinder, def TriCylinder.carrier, def Covers, def totalArea, def relativeCost, def n, def η, def alpha, def beta, def d, def cutoffCoeff, def step, def mesh, def cutoff, def speedSq, def normalizedTerm, def unit, def tiltV, def tiltW, def lowerVertices, def upperVertices, abbrev Coord
## CHALLENGE TriangularCovering  targets=['OAI.TriangularCovering.main'] defs=[]
theorem main : A_min = H ∧ MainAsymptotic ∧ NormalizedCounterexample := by
  sorry
end TriangularCovering
end
DEFS(16): abbrev Space, def H, def point, def K, def projection, def area, def shadowArea, def A_min, structure TriCylinder, def TriCylinder.carrier, def Covers, def totalArea, def relativeCost, def n, def MainAsymptotic, def NormalizedCounterexample
## CHALLENGE CylinderCovering  targets=['OAI.CylinderCovering.fourPaperMain'] defs=[]
theorem fourPaperMain :
    AngularExplicitStatement ∧
    RuledApproximation.HyperbolicStatement ∧
    RuledApproximation.NilpotentC1Statement ∧
    RegularParallelogramCounterexampleStatement ∧
    RegularOpenCounterexampleStatement ∧
    RadialSweep.AlignedStatement ∧
    RadialSweep.ActualSweepStatement := by
  sorry
end CylinderCovering
DEFS(108): abbrev Space, def H, def point, def K, def projection, def area, def shadowArea, def A_min, structure TriCylinder, def TriCylinder.carrier, def Covers, def totalArea, def relativeCost, def n, def η, def alpha, def beta, def d, def cutoffCoeff, def step, def mesh, def cutoff, def speedSq, def normalizedTerm, def unit, def tiltV, def tiltW, def lowerVertices, def upperVertices, abbrev Coord
## CHALLENGE RuledCovering  targets=['OAI.RuledApproximation.fullMain'] defs=[]
theorem fullMain : FullMain := by
  sorry
end RuledApproximation
end
DEFS(46): abbrev Plane, abbrev Space, def vec2, def vec3, def axial, def IsParallelogram, def IsTriangle, structure Cylinder, def carrier, def area, def parallelogram, def triangle, def openBounded, def familySet, def familyArea, def HasFiniteCover, def SmoothNear, def HyperbolicAt, def weight, def physicalWeight, def ruled, def physicalRuled, def HyperbolicStatement, def PhysicalHyperbolicStatement, def OpenRectangleC2, def LogarithmicStatement, def ProductCellStatement, def OrthogonalGridStatement, def unitSquare, def IsSquareTile
## CHALLENGE CylinderCovering  targets=['OAI.CylinderCovering.fourPaperMain'] defs=[]
theorem fourPaperMain :
    AngularExplicitStatement ∧
    RuledApproximation.HyperbolicStatement ∧
    RuledApproximation.NilpotentC1Statement ∧
    RegularParallelogramCounterexampleStatement ∧
    RegularOpenCounterexampleStatement ∧
    RadialSweep.AlignedStatement ∧
    RadialSweep.ActualSweepStatement := by
  sorry
end CylinderCovering
DEFS(108): abbrev Space, def H, def point, def K, def projection, def area, def shadowArea, def A_min, structure TriCylinder, def TriCylinder.carrier, def Covers, def totalArea, def relativeCost, def n, def η, def alpha, def beta, def d, def cutoffCoeff, def step, def mesh, def cutoff, def speedSq, def normalizedTerm, def unit, def tiltV, def tiltW, def lowerVertices, def upperVertices, abbrev Coord
## CHALLENGE CylinderCovering  targets=['OAI.CylinderCovering.fourPaperMain'] defs=[]
theorem fourPaperMain :
    AngularExplicitStatement ∧
    RuledApproximation.HyperbolicStatement ∧
    RuledApproximation.NilpotentC1Statement ∧
    RegularParallelogramCounterexampleStatement ∧
    RegularOpenCounterexampleStatement ∧
    RadialSweep.AlignedStatement ∧
    RadialSweep.ActualSweepStatement := by
  sorry
end CylinderCovering
DEFS(108): abbrev Space, def H, def point, def K, def projection, def area, def shadowArea, def A_min, structure TriCylinder, def TriCylinder.carrier, def Covers, def totalArea, def relativeCost, def n, def η, def alpha, def beta, def d, def cutoffCoeff, def step, def mesh, def cutoff, def speedSq, def normalizedTerm, def unit, def tiltV, def tiltW, def lowerVertices, def upperVertices, abbrev Coord
## PAPER Finite-angular-cylinder-covers-below-the-half-area-bound-September-27-2026
ABSTRACT: A regular tetrahedron admits a finite cylinder covering with compact triangular perpendicular bases whose total area is less than half its minimum orthogonal projection area. This disproves the half-area cylinder-covering conjecture. By affine invariance, the same construction gives a counterexample to the directionwise normalized half-bound for every nondegenerate tetrahedron.
[theorem] \label{thm:counterexample} The tetrahedron \eqref{eq:tetrahedron} has $A_{\min}(K)=\sqrt2$. For every $0<\eps\le1/2000$, it admits a covering by $m=2\lceil2/\eps^2\rceil$ cylinders with compact triangular perpendicular bases such that \begin{equation}\label{eq:main-asymptotic} \frac1{\sqrt2}\sum_{i=1}^m|B_i| =\frac12-\frac{13}{6000}\eps^2+O(\eps^4). \end{equation} The remainder has absolute value at most $2\eps^4$, and the total base area is strictly less than $A_{\min}(K)/2$.
## PAPER Finite-cylinder-approximation-of-ruled-sets-September-27-2026
ABSTRACT: We approximate compact ruled families of segments by finitely many cylinders with square intercept tiles and perpendicular-base area at most their integral projection cost plus any positive error. The velocity field is $C^1$, and its differential has opposite real eigenvalues whose magnitudes are strictly below the inverse segment half-length; both eigenvalues may vanish. The result includes square-zero differentials with unrestricted shear and fields that pass between the two regimes. It holds for arbitrary compact label sets.
[proposition[Perpendicular base area]] \label{b:projection} Let $h>0$, let $T\subset\R^2$ be bounded and measurable, and let $g\in\R^2$. The image $F_h(\Cyl(T,g))$ is a cylinder whose perpendicular base has area $h|T|J_h(g)$. A compact nondegenerate parallelogram tile has a compact nondegenerate parallelogram base. An open tile gives an open base. The formula is unchanged after a Euclidean isometry.
## PAPER Slope-field-perturbations-of-the-two-cylinder-covering-September-27-2026
ABSTRACT: The two-cylinder covering of a regular tetrahedron can be perturbed to give finite covers with total perpendicular base area strictly below half its minimum projection area. These covers give negative answers to both the half-area question and the directionwise normalized half-bound conjecture. By affine invariance, the directionwise conclusion holds for every nondegenerate tetrahedron.
[theorem] \label{c:main} Every regular tetrahedron $K\subset\R^3$ of positive edge length admits a finite cylinder cover with compact parallelogram perpendicular bases such that \[ \sum_i|B_i|<\tfrac12 A_{\min}(K), \qquad \sum_i\frac{|B_i|}{|\pi_{u_i^\perp}K|}<\tfrac12. \] It also admits finite covers with bounded open measurable bases satisfying both inequalities.
## PAPER Finite-triangular-approximation-of-radial-sweeps-September-27-2026
ABSTRACT: We prove that radially aligned segment sweeps admit finite cylinder covers with one triangular base for each interval of any tagged partition. As the mesh tends to zero, the total perpendicular base area converges to a weighted parameter area. An explicit application covers every regular tetrahedron with total base area below half its minimum projection area, giving negative answers to the half-area question and the directionwise normalized 1-Codimensional Cylinder Covering Conjecture.
[theorem] \label{thm:radial} For the data in \eqref{eq:radial-sweep}, suppose that \[ w'(t)=\lambda(t)(a+tb)\qquad(t\in J) \] for a continuous real function $\lambda$. For any finite partition \(\alpha=t_0<t_1<\cdots<t_N=\beta\), put \(I_i=[t_{i-1},t_i]\) and choose arbitrary tags \(c_i\in I_i\). There are \(N\) cylinders covering \(\mathcal S\), with axes parallel to \(e+w(c_i)\) and nondegenerate compact triangular perpendicular bases. These covers can be chosen so that their total base area tends to \(\mathcal A\) as the mesh \(\delta=\max_i|I_i|\) tends to zero, uniformly over the partitions and tags. Alternatively, take each base to be the perpendicular projection of the actual compact sweep with
==================
# FAMILY 102: The Unique Games Conjecture and optimal approximation thresholds
SCOPE: The Unique Games conjecture asks for hardness of distinguishing nearly satisfiable unique games from games of very small value. The formalized result gives, for every fixed $0<\varepsilon,\delta<1/2$, a deterministic polynomial-time reduction from binary 3SAT to nonempty unweighted simple bipartite unique games. Satisfiable inputs have value at least $1-\varepsilon$ and unsatisfiable inputs have value at most $\delta$. The alphabet is a fixed $\mathbb F_2^s$ depending only on the errors, and every constraint is a translation. The formalized result establishes hardness of approximating Max-Cut beyond the Goemans–Williamson constant $\alpha_{\mathrm{GW}}$. For every fixed $\alpha_{\mathrm{GW}}<\alpha\le1$, it gives a deterministic polynomial-time reduction from binary 3SAT to a strictly separated Max-Cut gap on finite simple unweighted graphs. The reduction includes the explicit positive i
## CHALLENGE UniqueGamesTheorem  targets=['OAI.UniqueGamesTheorem.theorem11'] defs=[]
theorem theorem11 (ε δ : ℝ)
    (hε : 0 < ε) (hεhalf : ε < 1 / 2)
    (hδ : 0 < δ) (hδhalf : δ < 1 / 2) :
    Nonempty (Explicit.MachineOutputContract.BinaryGapReduction ε δ) := by
  sorry
end UniqueGamesTheorem
DEFS(31): structure PermutationTable, structure Constraint, def Constraint.satisfied, structure Instance, def countSatisfied, structure Literal, def Literal.eval, abbrev Clause, def Clause.eval, structure Formula, def Formula.Satisfiable, def bitsValue, def parseFrame, def parseName, def parseLiteral, def parseClause, def parseClauses, def decodeFormula, def language, abbrev F2, abbrev Vector, def IsTranslationInstance, def encodeWord, def encodeWords, def tableWords, def constraintWords, def gameWords, def gameBits, def FiniteAlphabet, structure SimpleBipartite
## CHALLENGE OptimalMaxCut  targets=['OAI.OptimalMaxCut.main'] defs=[]
DEFS(25): structure Literal, def Literal.eval, abbrev Clause, def Clause.eval, structure Formula, def Formula.Satisfiable, def bitsValue, def frame, def parseFrame, def nameBits, def parseName, def parseLiteral, def parseClause, def parseClauses, def decodeFormula, def alphaGW, def binary3SAT, structure Graph, def Graph.cutSize, def Graph.maxCut, structure ScaledGraph, def ScaledGraph.bits, structure GapReduction, def MainStatement, theorem OptimalMaxCut.main
## CHALLENGE VertexCover  targets=['OAI.VertexCover.explicit_cover_gap', 'OAI.VertexCover.every_fixed_factor_below_two'] defs=[]
theorem explicit_cover_gap (m : ℕ) (hm : 4 ≤ m) : Nonempty (GapReduction m) := by
  sorry
theorem every_fixed_factor_below_two (α : ℝ) (hα : 1 ≤ α) (hα2 : α < 2)
    (algorithm : Approximation α) : Nonempty ThreeSATDecision := by
  sorry
end VertexCover
DEFS(25): structure Literal, def Literal.eval, abbrev Clause, def Clause.eval, structure Formula, def Formula.Satisfiable, def bitsValue, def frame, def parseFrame, def nameBits, def parseName, def parseLiteral, def parseClause, def parseClauses, def decodeFormula, def ThreeSAT, structure ExplicitGraph, def Cover, def coverNumber, def bits, def FiniteAlphabet, structure GapReduction, def natListBits, structure Approximation, structure ThreeSATDecision
## CHALLENGE MinUncut  targets=['OAI.MinUncut.main'] defs=[]
theorem main : Nonempty Reduction := by
  sorry
end MinUncut
DEFS(18): structure Literal, def Literal.eval, abbrev Clause, def Clause.eval, structure Formula, def Formula.Satisfiable, def frame, def nameBits, def literalBits, def clauseBits, def clausesBits, def formulaBits, structure Output, def Output.uncut, def Output.opt, def Output.bits, def inputBits, structure Reduction
## CHALLENGE DirectedFeedback  targets=['OAI.DirectedFeedback.main'] defs=[]
DEFS(16): def natBits, def pairBits, def FiniteAlphabet, structure NPVerifier, def NPVerifier.Accepts, def InNP, structure Digraph, def IsCycle, def Feedback, def dfvs, def bits, structure GapInstance, def GapInstance.bits, structure GapReduction, def MainStatement, theorem DirectedFeedback.main
## PAPER The-Unique-Games-Theorem-September-23-2026
ABSTRACT: We prove the Unique Games Conjecture. For every fixed \(\varepsilon,\delta\in(0,1/2)\), we give a deterministic polynomial-time reduction from \(\mathrm{3SAT}\) to Unique Games over a fixed finite alphabet, with completeness at least \(1-\varepsilon\) and soundness at most \(\delta\).
[theorem[Unique Games Theorem]] \label{thm:ugc} For every fixed \(\varepsilon,\delta\in(0,1/2)\), there are an integer \(s\ge1\) and a deterministic polynomial-time reduction from \(\mathrm{3SAT}\) to explicit unweighted Unique Games instances \(G_\varphi\) over \(K=\F_2^s\) such that \[ \begin{aligned} \varphi\text{ satisfiable} &\quad\Longrightarrow\quad \val(G_\varphi)\ge1-\varepsilon,\\ \varphi\text{ unsatisfiable} &\quad\Longrightarrow\quad \val(G_\varphi)\le\delta. \end{aligned} \] The graph is simple and bipartite, and every constraint is a translation \(a(v_e)=a(u_e)+c_e\) of \(K\). The alphabet, the degree of the running-time polynomial, and its constants depend only on \(\varepsilon,\delta\).
## PAPER A-Direct-Proof-of-Optimal-Max-Cut-Hardness-September-23-2026
ABSTRACT: We prove that approximating Max-Cut on simple unweighted graphs within any fixed factor greater than the Goemans--Williamson constant is NP-hard.
[theorem] \label{thm:main} For every fixed $\alpha$ with $\GW<\alpha\le1$, it is NP-hard to approximate Max-Cut within a factor of $\alpha$. This holds for simple unweighted graphs.
## PAPER The-Factor-Two-Hardness-Threshold-for-Vertex-Cover-September-23-2026
ABSTRACT: We prove that minimum Vertex Cover is NP-hard to approximate within every fixed factor below two, even on simple unweighted graphs.
[theorem[Explicit cover gap]] \label{thm:gap} For every fixed integer \(m\geq4\), there is a deterministic polynomial-time reduction from \(\mathrm{3SAT}\) to finite simple undirected unweighted graphs with the following guarantees: \[ \begin{array}{ll} \text{the formula is satisfiable} &\Longrightarrow\quad \tau(G)<\left(\dfrac12+\dfrac1m\right)|V(G)|,\\[6pt] \text{the formula is unsatisfiable} &\Longrightarrow\quad \tau(G)>\left(1-\dfrac1m\right)|V(G)|. \end{array} \] The output lists all vertices and edges explicitly.
## PAPER Constant-factor-hardness-of-Min-UnCut-September-23-2026
ABSTRACT: For every fixed \(C>1\), approximating Min-UnCut within factor \(C\) is NP-hard, even on simple undirected unweighted graphs.
[theorem] \label{thm:main} For every fixed integer $K\ge2$, there is a deterministic polynomial-time many-one reduction mapping a $3$SAT formula $\varphi$ to a pair $(G,k)$, where $G$ is an explicit finite simple undirected unweighted graph and $k\ge1$ is a binary-encoded integer, such that \[ \begin{aligned} \varphi\text{ satisfiable}&\quad\Longrightarrow\quad \OPT_{\rm uncut}(G)\le k,\\ \varphi\text{ unsatisfiable}&\quad\Longrightarrow\quad \OPT_{\rm uncut}(G)>Kk. \end{aligned} \] For each fixed $K$, the graph size, full construction work, and bit complexity are polynomial in the bit length of $\varphi$. All constants are effective; no advice or oracle is supplied to the reduction.
## PAPER Constant-factor-hardness-of-directed-feedback-vertex-set-September-23-2026
ABSTRACT: Approximating minimum directed feedback vertex set within any fixed constant factor is NP-hard, even on unweighted digraphs.
[theorem] \label{thm:main} For every fixed real constant $A\ge1$, it is NP-hard to approximate minimum directed feedback vertex set within factor $A$ on unweighted digraphs. More precisely, there is a deterministic polynomial-time reduction from an NP-hard promise problem to instances $(G,k)$ with $k\in\N_{>0}$. The polynomial and its constants may depend on $A$. The reduction has the following alternatives: \[ \textnormal{YES: }\DFVS(G)\le k, \qquad \textnormal{NO: }\DFVS(G)>Ak. \]
==================
# FAMILY 103: Exact derandomization of logarithmic space: $`\mathsf L=\mathsf{RL}=\mathsf{BPL}`$
SCOPE: The formalization proves $\mathsf L=\mathsf{RL}=\mathsf{BPL}$ for binary languages in an explicit Turing-machine model with logarithmic workspace. The randomized classes use polynomial time: $\mathsf{RL}$ never accepts a no-instance and accepts a yes-instance with probability at least $1/2$, while $\mathsf{BPL}$ has acceptance probability at least $2/3$ on yes-instances and at most $1/3$ on no-instances. Thus bounded-error randomness does not enlarge deterministic logarithmic space in this model. The selected theorem asserts equality of the language classes. The paper's explicit compiler and numerical running-time bounds are not separately stated in this Comparator target.
## CHALLENGE LogspaceEquality  targets=['OAI.ExactDerandomization.exact_logarithmic_space_derandomization'] defs=[]
theorem exact_logarithmic_space_derandomization :
    L = RL ∧ RL = BPL := by
  sorry
end ExactDerandomization
DEFS(25): abbrev Word, abbrev Language, abbrev CoinTape, inductive Direction, inductive InputSymbol, def Direction.move, def Direction.moveInput, def readInput, structure Action, structure Machine, structure Configuration, def initial, def step, def run, def spaceThrough, def LogSpace, def Deterministic, def HaltsBy, def Decides, def extendCoins, def acceptanceProbability, def polynomialClock, def L, def RL, def BPL
## PAPER Exact-Derandomization-of-Logarithmic-Space-L-equals-RL-equals-BPL-September-23-2026
ABSTRACT: We prove $\Lclass=\RL=\BPL$, resolving the derandomization problem for polynomial-time randomized logarithmic space.
[theorem[Exact logarithmic-space derandomization]] \label{thm:main} \[ \Lclass=\RL=\BPL. \]
==================
# FAMILY 104: Quasipolynomial algorithms for mean-payoff, stochastic and parity games
SCOPE: The formalization checks that a specified two-step execution of Truffet's elimination procedure terminates with a feasible but nonoptimal output. It is a finite counterexample to that proposed optimization step. The formalized result gives one randomized algorithm for the complete zero-threshold winning set of every finite mean-payoff game with signed binary weights. It succeeds with probability at least $7/8$ and runs in quasipolynomial bit time on every random tape. Self-loops, parallel edges, and history-dependent strategies are allowed, and winning means a nonnegative liminf average payoff.
## CHALLENGE TruffetCounterexample  targets=['OAI.TruffetV4Counterexample.finite_execution_not_optimal'] defs=[]
theorem finite_execution_not_optimal :
    crossRowRestriction initial ∧
    ForcedSingletonStep initial middle 0 1 ∧
    ForcedSingletonStep middle finalState 1 0 ∧
    (¬ ∃ j, finalState.remaining j) ∧ stop finalState ∧
    feasible initial output ∧ feasible initial better ∧
    output 2 = 0 ∧ better 2 = 0 ∧
    (output 1 : Coeff) = eval (lowerForm initial 0 1) output ∧
    (output 0 : Coeff) = eval (lowerForm middle 1 0) output ∧
    eval initial.cost output = eval finalState.cost output ∧
    eval initial.cost better < eval finalState.cost output := by
  sorry
end TruffetV4Counterexample
end
DEFS(30): abbrev Coeff, abbrev Form, abbrev Var, abbrev RowIndex, def column, def nullForm, structure Row, structure State, def wellFormed, def eval, def feasible, def lower, def upper, def dominating, def eligible, def bounded, def stop, def switch, def failure, def lowerForm, def substitute, def cleanup, def advance, def ForcedSingletonStep, def initial, def middle, def finalState, def crossRowRestriction, def output, def better
## CHALLENGE RandomizedMeanPayoff  targets=['OAI.randomized_quasipolynomial_mean_payoff'] defs=[]
theorem randomized_quasipolynomial_mean_payoff : MeanPayoff.MainClaim := by
  sorry
DEFS(23): structure Game, def Strategy, def move, def position, def play, def meanPayoff, def Winning, def encodeNat, def encodeInt, def input, abbrev Symbol, inductive Direction, def Direction.offset, structure Action, structure Machine, structure Configuration, def initial, def step, def run, def padBits, def result, def CorrectOutput, def MainClaim
## PAPER Deterministic-quasipolynomial-time-mean-payoff-games-September-25-2026
ABSTRACT: We give a deterministic algorithm that computes the complete zero-threshold winning set of a finite mean-payoff game with arbitrary signed integer edge weights encoded in binary. For total explicit input length $L$, it uses $2^{O((\log(L+2))^2)}$ bit operations. A reduction also computes the exact rational value at every vertex and globally optimal positional strategies for both players within the same quasipolynomial bound.
[theorem] \label{thm:main} A uniform deterministic algorithm returns exactly the set \[ U=\bigl\{v\in V:\exists\text{ Max strategy }\sigma\ \forall\text{ Min strategies }\tau, \ \MP_w(\pi_{v,\sigma,\tau})\ge0\bigr\} \] for every game specified above. For an absolute constant $C>0$, the complete computation uses at most \[ 2^{C(\log_2(L+2))^2} \] bit operations in a standard model polynomially equivalent to a uniform deterministic Turing machine. The bound includes preprocessing, exact arithmetic, recursion, and output of the entire set $U$.
## PAPER Randomized-quasipolynomial-time-mean-payoff-games-September-25-2026
ABSTRACT: We give a randomized algorithm that computes the complete zero-threshold winning set of a finite mean-payoff game with arbitrary signed integer edge weights encoded in binary. For total explicit input length $L$, it uses $2^{O((\log(L+2))^2)}$ bit operations on every random tape and is correct with probability at least $7/8$. A polynomial-time check certifies the winning regions and positional strategies for both players or reports failure. Independent repetition therefore gives an always-correct algorithm with the same expected quasipolynomial bit bound.
[theorem] \label{thm:main} There is a uniform randomized algorithm that, for every such game, returns the entire set \[ U=\{v\in V:\text{there is a Max strategy }\sigma \text{ such that for every Min strategy }\tau,\ \operatorname{MP}_w(\pi_{v,\sigma,\tau})\ge0\} \] correctly with probability at least $7/8$. For an absolute constant $C>0$, on every random tape its total cost is at most \[ 2^{C(\log_2(L+2))^2} \] bit operations in a standard model polynomially equivalent to a uniform probabilistic Turing machine. The bound includes preprocessing, recursive calls, intermediate arithmetic, and random-bit generation.
==================
# FAMILY 105: Perfect completeness for 2-to-1 games
SCOPE: The formalized result establishes perfect-completeness hardness for 2-to-1 games. For every fixed rational $0<\delta<1$, a deterministic polynomial-time reduction from binary 3SAT produces a nonempty unweighted game of value exactly $1$ on satisfiable inputs and at most $\delta$ on unsatisfiable inputs. Each constraint projection has exactly two preimages for each output label. The alphabet depends only on $\delta$, and the runtime is measured in the original input bit length.
## CHALLENGE PerfectCompleteness  targets=['OAI.PerfectCompleteness.Theorem11.exists_reduction'] defs=[]
theorem exists_reduction (δ : ℚ) (positive : 0 < δ) (less_than_one : δ < 1) :
    Nonempty (PerfectCompleteness.BinaryGapReduction δ) := by
  sorry
end PerfectCompleteness.Theorem11
DEFS(30): def encodeWord, def encodeWords, def FiniteAlphabet, structure Literal, def Literal.eval, abbrev Clause, def Clause.eval, structure Formula, def Formula.Satisfiable, def bitsValue, def parseFrame, def parseName, def parseLiteral, def parseClause, def parseClauses, def decodeFormula, def language, structure ProjectionTable, structure Edge, structure Instance, abbrev Labeling, def Edge.satisfied, def countSatisfied, def maxSatisfied, def value, def tableWords, def edgeWords, def gameWords, def gameBits, structure BinaryGapReduction
## PAPER Perfect-completeness-for-2-to-1-games-September-23-2026
ABSTRACT: We prove the 2-to-1 Games Conjecture with perfect completeness. For every fixed rational $\delta\in(0,1)$, it is NP-hard to distinguish satisfiable 2-to-1 games from games of value at most $\delta$, with a fixed alphabet and an explicitly listed unweighted multiset of constraints.
[theorem] \label{thm:main} For every fixed rational $\delta\in(0,1)$ there are an integer $q=q(\delta)\ge2$ and a deterministic polynomial-time reduction from $3$-SAT to 2-to-1 games with alphabets $[2q]$ and $[q]$ such that: \begin{enumerate}[label=\textup{(\roman*)}] \item a satisfiable formula produces a game of value $1$; \item an unsatisfiable formula produces a game of value at most $\delta$. \end{enumerate} The output contains a nonempty explicit list of unweighted edge occurrences and an explicit table for every projection map. Every table has exactly two preimages for each right answer. The polynomial running-time bound is in the ordinary binary input length; its degree and constants may depe
==================
# FAMILY 106: Hardness of coloring three-colorable graphs
SCOPE: The formalized result shows hardness of finding large independent sets even under a three-colorability promise. For every fixed $0<\delta<1/3$, a deterministic polynomial-time reduction maps binary 3SAT formulas to nonempty finite simple graphs. Satisfiable formulas produce three-colorable graphs; unsatisfiable formulas produce graphs whose largest independent set has fewer than $\delta$ times the number of vertices. The complete adjacency-matrix output is included in the runtime bound.
## CHALLENGE IndependentSets  targets=['OAI.LargeIndependentSets.mainTheoremReal'] defs=[]
theorem mainTheoremReal :
    ∀ δ : ℝ, 0 < δ → δ < 1 / 3 → Nonempty (RealGraphReduction δ) := by
  sorry
end
end LargeIndependentSets
DEFS(14): structure Literal, structure Formula, def Formula.Satisfiable, def frame, def nameBits, def literalBits, def clauseBits, def formulaBits, structure Graph, def Graph.Independent, def Graph.independenceNumber, def Graph.ThreeColorable, def graphBits, structure RealGraphReduction
## PAPER Hardness-of-finding-large-independent-sets-in-three-colorable-graphs-September-24-2026
ABSTRACT: We prove that, for every fixed $0<\delta<1/3$, it is NP-hard to distinguish three-colorable graphs from graphs in which every independent set has fewer than $\delta$ times the number of vertices. Consequently, for every fixed integer $c\ge3$, finding a proper $c$-coloring of a three-colorable graph is NP-hard.
[theorem] \label{thm:main} For every fixed real $0<\delta<1/3$, there is a deterministic polynomial-time algorithm $R_\delta$ that maps each explicitly encoded Boolean $3$-CNF formula $\phi$ to a nonempty finite simple undirected unweighted graph $G_\phi$ such that \[ \begin{array}{ll} \phi\text{ is satisfiable} &\Longrightarrow G_\phi\text{ is three-colorable},\\[2pt] \phi\text{ is unsatisfiable} &\Longrightarrow \alpha(G_\phi)<\delta\,|V(G_\phi)|. \end{array} \] The running time and explicit output size are polynomial in the ordinary binary encoding length of $\phi$. Their constants and polynomial degree may depend on the fixed $\delta$, but not on $\phi$. The coloring in the first implication cover
==================
# FAMILY 107: Matrix multiplication with exponent at most 9/4
SCOPE: The formalized results bound the complex matrix-multiplication exponent by $\omega(\mathbb C)\le9/4$, the dual exponent by $\alpha>0.465$, and the rectangular exponent at aspect ratio $0.709$ by $\omega(\mathbb C;1,0.709,1)<2.092$. The dual exponent is the supremum of rectangular aspect ratios attainable with exponent $2$. The arithmetic model counts additions, subtractions, and multiplications in finite division-free programs, with arbitrary positive exponent slack. The square bound implies the paper's weaker $2.258$ headline bound. The formalized result gives the unconditional bound $\omega(F)<2.371054886006746$ for every field $F$, including finite fields and fields of positive characteristic. The exponent counts additions, subtractions, and multiplications in finite division-free arithmetic programs, with arbitrary positive exponent slack. No numerical inequalities remain as hypothes
## CHALLENGE MatrixMultiplication  targets=['OAI.MatrixMultiplication.complex_omega_le_nine_quarters', 'OAI.MatrixMultiplication.complex_alpha_gt_93_div_200', 'OAI.MatrixMultiplication.complex_rectangular_omega_lt_523_div_250'] defs=[]
theorem complex_omega_le_nine_quarters :
    Arithmetic.omega ℂ ≤ (9 : ℝ) / 4 := by
  sorry
theorem complex_alpha_gt_93_div_200 :
    (93 : ℝ) / 200 < Arithmetic.complexAlpha := by
  sorry
theorem complex_rectangular_omega_lt_523_div_250 :
    Arithmetic.rectangularOmega ℂ ((709 : ℝ) / 1000) < (523 : ℝ) / 250 := by
  sorry
end MatrixMultiplication
DEFS(18): inductive Gate, def eval, def cost, inductive Program, def eval, def cost, abbrev MatrixInput, def matrixInputs, structure MatrixAlgorithm, def eval, def Correct, def cost, def AdmissibleExponent, def omega, def innerSize, def RectangularAdmissibleExponent, def rectangularOmega, def complexAlpha
## CHALLENGE MatrixFields  targets=['OAI.MatrixAllFields.MatrixMultiplication.AllFieldMain.omega_lt_source_constant'] defs=[]
theorem omega_lt_source_constant (F : Type u) [Field F] :
    Arithmetic.omega F < (2371054886006746 : ℝ) / 10 ^ 15 ∧
    (2371054886006746 : ℝ) / 10 ^ 15 < (2371056 : ℝ) / 10 ^ 6 := by
  sorry
end MatrixAllFields.MatrixMultiplication.AllFieldMain
DEFS(14): inductive Gate, def eval, def cost, inductive Program, def eval, def cost, abbrev MatrixInput, def matrixInputs, structure MatrixAlgorithm, def eval, def Correct, def cost, def AdmissibleExponent, def omega
## PAPER Complex-Matrix-Multiplication-Below-2.258-and-Rectangular-Bounds-September-24-2026
ABSTRACT: Over every field of characteristic zero, we prove that the square matrix-multiplication exponent satisfies \(\omega<2.258\), the dual exponent satisfies \(\alpha>0.465\), and \(\omega(1,0.709,1)<2.092\). The strict square and \(k=0.709\) rectangular bounds also hold over every field except possibly in one finite set of positive characteristics, in the arithmetic-operation model.
[theorem] \label{thm:main}\label{thm:square}\label{thm:rectangular} Over \(\C\), the arithmetic matrix-multiplication exponents satisfy \[ \omega<\frac{1129}{500}=2.258,\qquad \alpha>0.465,\qquad w(0.709)<2.092. \]
## PAPER Staggered-extraction-for-exact-matrix-multiplication-over-every-field-September-24-2026
ABSTRACT: We prove that the arithmetic exponent of square matrix multiplication over every fixed field satisfies $\omega<2.371054886006746$. This includes every positive characteristic.
[theorem] \label{thm:main} Over every fixed field $\F$, the arithmetic exponent of square matrix multiplication satisfies \[ \omega_\F<2.371054886006746<2.371054887. \]
==================
# FAMILY 108: A cubic permanent–determinant lower bound
SCOPE: The formalization proves a cubic lower bound for both exact and border determinantal representations of the complex $m\times m$ permanent. For $m\ge1408$, every affine-linear determinant representation of size $n$, including coefficientwise limits, satisfies $n\ge m^3/(5529600e)$. A general supporting theorem applies to a polynomial in $d\ge2$ variables whose first nonzero homogeneous Taylor term has degree $r\ge2$ and no nonzero singular zero. Its exact and border determinantal sizes are at least $(r-1)(d-1)/(4e)$. The paper's algebraic-branching-program consequences are outside these statements.
## CHALLENGE PermanentCubic  targets=['OAI.PermanentBorder.permanent_cubic_lower_bounds'] defs=[]
theorem permanent_cubic_lower_bounds :
    (∀ (m n : ℕ), 1408 ≤ m → HasBorderDeterminant n (permanentPolynomial m) →
      (m : ℝ)^3 / (5529600 * Real.exp 1) ≤ (n : ℝ)) ∧
    (∀ (m n : ℕ), 1408 ≤ m → HasExactDeterminant n (permanentPolynomial m) →
      (m : ℝ)^3 / (5529600 * Real.exp 1) ≤ (n : ℝ)) := by
  sorry
end PermanentBorder
DEFS(6): abbrev Variables, abbrev Poly, def permanentPolynomial, def affineMatrixPolynomial, def HasBorderDeterminant, def HasExactDeterminant
## CHALLENGE SmoothInitialForm  targets=['OAI.PermanentBorder.smooth_initial_form_lower_bound'] defs=[]
theorem smooth_initial_form_lower_bound (d r : ℕ) (g : Poly (Fin d))
    (a : Fin d → ℂ) (hd : 2 ≤ d) (hr : 2 ≤ r)
    (hG : homogeneousComponent r
      (affineSubstitution a (fun i j : Fin d => if i = j then 1 else 0) g) ≠ 0)
    (hlow : ∀ j < r, homogeneousComponent j
      (affineSubstitution a (fun i j : Fin d => if i = j then 1 else 0) g) = 0)
    (hs : ∀ y : Fin d → ℂ,
      eval y (homogeneousComponent r
        (affineSubstitution a (fun i j : Fin d => if i = j then 1 else 0) g)) = 0 →
      (∀ i, eval y (pderiv i (homogeneousComponent r
        (affineSubstitution a (fun i j : Fin d => if i = j then 1 else 0) g))) = 0) →
      y = 0) :
    ∀ n : ℕ,
      (HasBorderDeterminant n g →
        ((r - 1 : ℕ) : ℝ) * ((d - 1 : ℕ) : ℝ) / (4 * Real.exp 1) ≤ (n : ℝ)) ∧
      (HasExactDeterminant n g →
        ((r - 1 : ℕ) : ℝ) * ((d - 1 : ℕ) : ℝ) / (4 * Real.exp 1) ≤ (n : ℝ)) := by
  sorry
end PermanentBorder
DEFS(5): abbrev Poly, def affineMatrixPolynomial, def HasBorderDeterminant, def HasExactDeterminant, def affineSubstitution
## PAPER A-cubic-lower-bound-for-border-determinantal-complexity-of-the-permanent-September-24-2026
ABSTRACT: We prove that the complex border determinantal complexity of the $m\times m$ permanent is $\Omega(m^3)$, allowing arbitrary affine-linear determinant representations and coefficientwise limits. It also gives cubic lower bounds for exact determinantal complexity and for the numbers of vertices and edges in affine-linear algebraic branching programs, including coefficientwise limits with a fixed vertex or edge budget.
[theorem] \label{thm:main} There exist absolute constants $c>0$ and $m_0$ such that, for every integer $m\ge m_0$, \[ \bdc(\per_m)\ge c m^3. \] One may take $c=1/(5\,529\,600e)$ and $m_0=1408$.
==================
# FAMILY 110: Optimal-order randomized <i>k</i>-server on arbitrary metrics
SCOPE: The formalization proves an $O((\log(k+1))^2)$ competitive ratio for randomized $k$-server against oblivious finite request sequences. For every $k\ge2$, every metric space containing at least $k+1$ points, and every initial configuration, one policy works for all request sequences, including in infinite and unbounded spaces. The bound permits a configuration-dependent additive constant, which is zero when the initial server positions are distinct. The universal multiplicative constant is independent of the metric and $k$. The formalization constructs one uniform randomized bit algorithm for $k$-server on finite rational metrics, for $2\le k<n$. Its expected movement on every oblivious finite request sequence is at most an absolute multiple of $(\log(k+1))^2$ times the offline optimum, plus a finite instance-dependent additive constant. Preprocessing is polynomial in the encoded input le
## CHALLENGE KServer  targets=['OAI.KServer.main_theorem'] defs=[]
theorem main_theorem : MainStatement.{u} := by
  sorry
end KServer
end
DEFS(9): abbrev Configuration, def LabelDistribution, abbrev Policy, def serve, def serviceCost, def pathProbability, def expectedCost, def optimalCost, def MainStatement
## CHALLENGE UniformKServer  targets=['OAI.UniformKServer.uniform_squared_logarithmic_main'] defs=[]
theorem uniform_squared_logarithmic_main : UniformAlgorithmClaim := by
  sorry
end UniformKServer
DEFS(31): structure RationalMetric, abbrev Configuration, abbrev History, def serve, def costAlong, def offlineCost, inductive HeadMove, structure BitTape, def blank, def ofWord, def shift, structure BitAction, structure BitMachine, structure MachineState, def initial, def step, def run, def install, def natCode, def rationalCode, def instanceCode, def bitValue, def outputValue, def polynomialBudget, def requestBudget, def boot, def requestStep, inductive Reachable, def selectedLabel, def machineExpectedCost
## PAPER Squared-logarithmic-randomized-k-server-on-arbitrary-metrics-September-24-2026
## PAPER Uniform-computation-of-the-squared-logarithmic-k-server-bound-September-24-2026
ABSTRACT: We construct a uniform randomized \(k\)-server algorithm on finite rational metrics with competitive ratio \(O(\log^2(k+1))\) against oblivious request sequences. Preprocessing is polynomial in the input length, and per-request bit complexity is polynomial in that length and the binary request-counter length. The additive movement constant is finite and instance-dependent, but may be enormous. The construction uses the companion squared-logarithmic existence theorem.
[theorem] \label{thm:main} There are an absolute constant \(C\) and a polynomial \(p\) with the following property. Let \(n\ge3\), \(2\le k<n\), let \(d\) be a rational metric on \(X=\{1,\ldots,n\}\), and let \(s\in X^k\) be an initial labeled tuple, with repetitions allowed. Write \(L\) for the total binary encoding length of \(n,k,d,s\). A single uniform randomized online algorithm preprocesses these data in at most \(p(L)\) bit operations and serves request \(r_t\), for every reachable history and internal state, in at most \[ p\!\left(L+\left\lceil\log_2(t+1)\right\rceil\right) \] additional bit operations. It uses only unbiased random bits and moves exactly one chosen server to each request, perm
==================
# FAMILY 111: One-sample matroid prophet inequalities against an almighty adversary
SCOPE: The formalization proves a one-sample matroid prophet inequality with expected reward at least $2^{-310}$ times the expected offline optimum. Each element has one independent sample paired with an identically distributed nonnegative online value, and all coordinates are independent. The rule and finite seed law depend only on the labeled matroid; choices are irrevocable and feasible after every prefix. The arrival order may depend measurably on all samples, values, and the seed, and only the offline optimum must be integrable. A supporting hidden-vector selection result for fixed nonnegative matroid weights gives expected worst-order reward at least $2^{-293}$ times the optimum, again with a finite seed law and prefix feasibility.
## CHALLENGE MatroidProphet  targets=['OAI.MatroidProphet.one_sample'] defs=[]
DEFS(17): abbrev Weights, abbrev Seed, abbrev ArrivalOrder, instance arrivalOrderMeasurableSpace, abbrev History, structure OnlineRule, def prefixIndex, def history, def decisionAt, def acceptedThrough, def accepted, def reward, def optimum, def Feasible, def pairedCoordinates., def OneSampleChallenge., theorem one_sample.
## CHALLENGE MatroidSecretary  targets=['OAI.MatroidProphet.Assigned.one_sample', 'OAI.MatroidProphet.Assigned.hidden_vector', 'OAI.MatroidProphet.Assigned.secretary'] defs=[]
theorem hidden_vector : MatroidProphet.HiddenVectorChallenge := by
  sorry
DEFS(33): abbrev Weights, abbrev Seed, abbrev ArrivalOrder, instance arrivalOrderMeasurableSpace, abbrev History, structure OnlineRule, def prefixIndex, def history, def decisionAt, def acceptedThrough, def accepted, def reward, def optimum, def Feasible, def pairedCoordinates., def OneSampleChallenge., instance arrivalOrderMeasurableSingletonClass, structure HiddenRule, def observed, def hiddenAcceptedThrough, def hiddenReward, def hiddenWorstReward, def HiddenVectorChallenge, structure SecretaryRule, def SamePrefix, def secretaryDecisionAt, def secretaryAcceptedThrough, def secretaryReward, def SecretaryFeasible, def uniformArrivalLaw
## PAPER One-Sample-Suffices-for-Matroid-Prophet-Inequalities-against-an-Almighty-Adversary-September-23-2026
ABSTRACT: We prove that one independent sample per element suffices for a constant-competitive prophet inequality on every finite matroid. The guarantee holds even when the arrival-order adversary observes all samples, all online values, and the algorithm's entire random seed. The rule needs no description of the value distributions and achieves the absolute competitive ratio $2^{-310}$.
[theorem] \label{thm:main} There is a measurable online selection rule, independent of the value distributions, with the following property. Let $M=(E,\mathcal I)$ be any finite known labeled matroid, and let $(S_e,V_e:e\in E)$ be mutually independent nonnegative real random variables, with $S_e$ and $V_e$ having the same arbitrary law $D_e$. Assume $\Ex[\OPT_M(V)]<\infty$. The rule receives exactly the sample vector $S$ before arrivals and uses a seed $R$ independent of $S,V$. For every measurable permutation rule $\pi$ depending on $M$, the laws $(D_e)$, $S$, $V$, and $R$, the rule accepts an independent set $A$, irrevocably deciding at each arrival using only the available history, and \begin{equat
==================
# FAMILY 112: Beyond the square-root exponent for depth-three circuits
SCOPE: The formalized result gives one polynomial-time Boolean language whose exact depth-three OR–AND–OR circuit size eventually exceeds $2^{A\sqrt n}$ for every fixed $A>0$. The language and its polynomial-time algorithm are fixed before $A$ is chosen, while circuits may vary with the input length. Gates have unrestricted finite fan-in and sharing, with free input negations and constants. The result does not assert a fixed exponent $n^{1/2+\varepsilon}$ or a lower bound for unrestricted depth.
## CHALLENGE DepthThree  targets=['OAI.DepthThreeLowerBound.exists_polynomial_time_language_depth_three_lower_bound'] defs=[]
theorem exists_polynomial_time_language_depth_three_lower_bound :
    ∃ (L : List Bool → Bool) (M : FiniteMultiTapeMachine) (C a : ℕ),
      0 < C ∧ 0 < a ∧
      (∀ w : List Bool, MultiTapeHaltsIn M w (L w) (C * (w.length + 1) ^ a)) ∧
      ∀ A : ℝ, 0 < A → ∃ N : ℕ, ∀ n : ℕ, N ≤ n →
        ∀ D : Circuit3 (Fin n), D.Computes (fun x => L (List.ofFn x)) →
          (2 : ℝ) ^ (A * Real.sqrt (n : ℝ)) < (D.gateCount : ℝ) := by
  sorry
end DepthThreeLowerBound
DEFS(24): abbrev Cube, abbrev Literal, def eval, abbrev GateInput, abbrev RawClause, def eval, def eval, structure Circuit3, def gateCount, def middleEval, def eval, def Computes, def runSteps, inductive HeadMove, def HeadMove.apply, structure MultiTapeCfg, abbrev MultiTapeCode, def multiTapeUpdate, def multiTapeStep, structure FiniteMultiTapeMachine, abbrev Cfg, abbrev step, def init, def MultiTapeHaltsIn
## PAPER Beyond-the-Square-Root-Exponent-for-Depth-Three-Boolean-Circuits-September-23-2026
ABSTRACT: We construct a language in deterministic polynomial time whose \(n\)-bit membership function requires \(2^{\omega(\sqrt n)}\) gates in an unbounded-fan-in OR--AND--OR circuit. The bound holds at every sufficiently large input length and counts all gates, including the bottom layer.
[theorem] \label{thm:main} There is a language \(L\subseteq\bits^*\), a deterministic Turing machine deciding \(L\), and fixed positive integers \(C,a\) such that the machine runs in time at most \(C(n+1)^a\) on every input of length \(n\). If \(f_n\) is the membership function of \(L\) on \(\bits^n\), then \[ \lim_{n\to\infty}\frac{\log_2 S_3(f_n)}{\sqrt n}=\infty. \] Equivalently, for every real \(A>0\), there is an integer \(N_A\) such that \[ S_3(f_n)>2^{A\sqrt n}\qquad\text{for every }n\ge N_A. \] No uniformity or bottom fan-in restriction is imposed on the circuits.
==================
# FAMILY 113: Approximate counting and entropy of perfect matchings
SCOPE: The formalization gives a fully polynomial randomized approximation scheme for counting perfect matchings in every finite simple undirected graph. For rational $0<\varepsilon<1$ and $0<\delta<1/2$, it returns a nonnegative rational estimate with relative error at most $\varepsilon$ with probability at least $1-\delta$. If the graph has no perfect matching, every execution returns zero. The algorithm is a fixed finite-alphabet randomized machine. Its worst-case running time is polynomial in the binary input length, $\varepsilon^{-1}$, and $\log(\delta^{-1})$, including on unsuccessful random tapes. For feasible edge marginals $x$ of perfect matchings in a loopless multigraph on $2m$ vertices, let $F(x)=-\sum_e x_e\log x_e$, $B(x)=-\sum_e(1-x_e)\log(1-x_e)$, and let $H(x)$ be the maximum entropy of a matching law with those marginals. The formalization proves $F(x)-(2-2/m)B(x)\le H(x)\le F
## CHALLENGE MatchingFPRAS  targets=['OAI.MatchingFPRAS.thm_main'] defs=[]
theorem thm_main : MainStatement := by
  sorry
end MatchingFPRAS
DEFS(18): structure GraphInput, def Perfect, def perfectMatchings, def Z, abbrev Symbol, def encodeNat, def encodeInt, def encodeRat, def encodeInput, structure RandomMachine, structure Configuration, def tick, def initial, def run, def Outputs, def timeBound, def goodTapes, def MainStatement
## CHALLENGE MatchingEntropy  targets=['OAI.MatchingEntropy.entropy_main'] defs=[]
theorem entropy_main (G : LooplessGraph V E) (m : ℕ)
    (hm : 0 < m) (hV : Fintype.card V = 2 * m)
    (hPM : Nonempty G.Matching) (y : E → ℝ) (hy : y ∈ G.polytope) :
    marginalEntropy y - maxMatchingEntropy G y ≤
      8 * (m : ℝ) * (1 - Real.exp (-marginalEntropy y / (m : ℝ))) := by
  sorry
end MatchingEntropy
end
DEFS(13): def probabilitySimplex, structure LooplessGraph, def Incident, def IsPerfectMatching, abbrev Matching, instance matchingFintype, def indicator, def polytope, def mean, def feasibleLaws, def entropy, def marginalEntropy, def maxMatchingEntropy
## CHALLENGE BinaryMatching  targets=['OAI.BinaryMatching.deterministic_approximate_counting'] defs=[]
theorem deterministic_approximate_counting :
    ∃ A : Input → ℕ,
      ∃ machine : Turing.TM2ComputableInPolyTime encodeInput Nat.bits A,
        (∀ k, Finite (machine.tm.Γ k)) ∧
        (∃ P : Polynomial ℕ, ∀ G,(A G).bits.length≤P.eval (encodeInput G).length) ∧
        ∀ G,A G≤count G ∧ count G≤2^(9*G.n)*A G ∧ (A G=0 ↔ count G=0) := by
  sorry
end BinaryMatching
DEFS(14): structure LooplessGraph, def Incident, def IsPerfectMatching, abbrev Matching, instance matchingFintype, abbrev Pair, def completeGraph, structure Record, structure Input, def multiplicity, def count, def encodeNat, def encodeRecord, def encodeInput
## CHALLENGE SingletonLoopMatching  targets=['OAI.LoopMatching.fullEndpoint'] defs=[]
theorem fullEndpoint : FullEndpoint := by
  sorry
end LoopMatching
DEFS(24): structure LooplessGraph, def Incident, abbrev Pair, def completeGraph, structure Record, structure Input, def multiplicity, def encodeNat, def encodeRecord, def encodeInput, structure LoopRecord, structure Input, abbrev Input.n, def loopMultiplicity, def IsPartialMatching, abbrev PartialMatching, instance partialMatchingFintype, def loopVertices, def weight, def count, def encodeLoopRecord, def encodeInput, def encodeOutput, def FullEndpoint
## CHALLENGE MatchingEntropyBounds  targets=['OAI.MatchingEntropyBounds.Refined.pointwise_entropy'] defs=[]
DEFS(15): structure LooplessGraph, def Incident, instance incidentDecidable, def IsPerfectMatching, abbrev Matching, instance matchingFintype, def indicator, def polytope, def mean, def probabilitySimplex, def LooplessGraph.feasibleLaws, def entropy, def maxMatchingEntropy, def complementEntropy, theorem Refined.pointwise_entropy
## CHALLENGE TriangleFace  targets=['OAI.TriangleFace198.triangle_expansion_face'] defs=[]
theorem triangle_expansion_face {V : Type uV} {E : Type uE}
    [Fintype V] [Fintype E] [DecidableEq V] [DecidableEq E] (G : LooplessGraph V E) (v : V)
    (hdeg : Fintype.card {e : E // G.Incident v e} = 3)
    (_hmatching : Nonempty G.Matching) :
    ∃ (c : E → Fin 3) (hc : LocalLabels G v c),
      let H := triangleExpansion G c v
      let f := localExtension G c v hc
      let Q := {y | y ∈ H.polytope ∧ H.cutMass y (triangleVertices v) = 1}
      f '' G.polytope = Q ∧
      Convex ℝ Q ∧ IsExtreme ℝ H.polytope Q ∧
      (∀ x, oldRestriction (f x) = x) ∧
      (∀ y ∈ Q, f (oldRestriction y) = y) ∧
      (∀ x e, f x (Sum.inl e) = x e) ∧
      (∀ x i, f x (Sum.inr i) = x (localEdge G c v hc i)) ∧
      (∀ x, (∀ e, x e = (1/3 : ℝ)) → ∀ e, f x e = (1/3 : ℝ)) ∧
      (∀ x ∈ G.polytope, CanonicalFace198.minFace H.polytope (f x) = f '' CanonicalFace198.minFace G.polytope x)  := by
  sorry
end TriangleFace198
end
DEFS(25): structure LooplessGraph, def Incident, instance incidentDecidable, def IsPerfectMatching, abbrev Matching, instance matchingFintype, def indicator, def polytope, def Crosses, instance crossesDecidable, def cut, def degree, def cutMass, def triangleTip, def triangleCollapse, def reattach, theorem collapse_reattach, def triangleExpansion, def triangleVertices, def facesThrough, def minFace, def LocalLabels, def localEdge, def localExtension, def oldRestriction
## PAPER A-Fully-Polynomial-Randomized-Approximation-Scheme-for-Perfect-Matchings-in-General-Graphs-September-23-2026
ABSTRACT: We give a fully polynomial randomized approximation scheme (FPRAS) for counting perfect matchings in arbitrary finite simple undirected graphs, resolving the general-graph perfect-matching approximation problem. The algorithm returns zero with certainty when no perfect matching exists. Otherwise, it achieves relative error $\eps$ with failure probability at most $\delta$ in worst-case bit time polynomial in the input length, $\eps^{-1}$, and $\log\delta^{-1}$.
[theorem] \label{thm:main} There is a uniform classical randomized algorithm which, given $G$ and rational parameters $0<\eps<1$ and $0<\delta<1/2$, returns a nonnegative rational number $\widehat Z$ such that \[ \Prb\bigl[(1-\eps)Z(G)\le \widehat Z\le(1+\eps)Z(G)\bigr] \ge 1-\delta. \] If $Z(G)=0$, the output is zero with certainty. The worst-case bit running time is polynomial in the input encoding length, $\eps^{-1}$, and $\log\delta^{-1}$.
## PAPER Entropy-and-Face-Dimension-of-the-Perfect-Matching-Polytope-September-23-2026
ABSTRACT: We prove the perfect-matching entropy conjecture of Anari, Oveis Gharan, and Vinzant. For every feasible vector $x$ of perfect-matching edge marginals in a loopless labelled multigraph on $2m\ge2$ vertices, the maximum entropy $H(x)$ of a matching law with marginals $x$ satisfies \[ F(x)-(2-2/m)B(x)\le H(x)\le F(x), \] where $F(x)=-\sum_e x_e\log x_e$ and $B(x)=-\sum_e(1-x_e)\log(1-x_e)$. This bound holds throughout the polytope, including its boundary. We also prove the sharp bound $|\supp x|-\dim F_x\le3m-2$, where $F_x$ is the minimal face of the perfect-matching polytope containing $x$.
[theorem[Pointwise entropy bounds]] \label{ent:main} Let $G$ be a loopless multigraph on $2m\ge2$ vertices with at least one perfect matching. For every $x\in P(G)$, \begin{equation}\label{intro:main-bound} F(x)-\left(2-\frac2m\right)B(x) \le H(x)\le F(x). \end{equation}
==================
# FAMILY 114: Approximate counting of common integer polymatroid bases
SCOPE: The formalized result gives a fully polynomial randomized approximation scheme for the number of common bases of two equal-rank matroids on an enumerated finite ground set, using independence oracles. For rational $0<\varepsilon,\delta<1$, the nonnegative rational output has relative error at most $\varepsilon$ with probability at least $1-\delta$. A zero count produces zero on every execution. Oracle calls and bit operations have polynomial bounds on every random tape in the input size, $\varepsilon^{-1}$, and $\log(\delta^{-1})$.
## CHALLENGE CommonBasesFPRAS  targets=['OAI.common_bases_fpras'] defs=[]
theorem common_bases_fpras : CommonBasesFPRAS.MainTheorem := by
  sorry
DEFS(15): abbrev IndependenceOracle, def ExactOracles, def commonBaseCount, inductive Instruction, def Program, def binaryValue, structure MachineConfig, def inputLength, def initialConfig, def machineStep, def execution, def finiteBits, def relativeAccuracy, def resourceBound, def MainTheorem
## PAPER Approximate-counting-of-common-bases-of-two-matroids-September-23-2026
ABSTRACT: We give a fully polynomial randomized approximation scheme for counting the common bases of two arbitrary matroids of the same rank, supplied by independence oracles. The algorithm requires no explicit representation of either matroid and has polynomial bounds on both oracle calls and bit operations on every execution.
[theorem] \label{thm:main} There is a single randomized oracle algorithm with the following guarantee. Given independence oracles for arbitrary rank-$r$ matroids $M_1,M_2$ on $[n]$, and rational $\epsilon,\delta\in(0,1)$, it outputs a nonnegative rational $\widehat Z$ such that \[ \Prob\bigl[(1-\epsilon)Z(M_1,M_2)\le\widehat Z \le(1+\epsilon)Z(M_1,M_2)\bigr]\ge1-\delta. \] If $Z(M_1,M_2)=0$, its output is always zero. On every execution, the number of oracle calls and the number of other bit operations are bounded by a fixed polynomial in \[ n,\qquad \ell,\qquad \epsilon^{-1},\qquad \log\delta^{-1}, \] where $\ell$ is the binary encoding length of $n,r,\epsilon,\delta$. The algorithm uses only indepen
==================
# FAMILY 115: Sampling and counting contingency tables with arbitrary margins
SCOPE: The formalization gives an exact uniform sampler for nonnegative integer contingency tables with arbitrary prescribed row and column sums having equal totals. It terminates almost surely, every halted output is feasible, and each table has exactly the uniform limiting probability. Expected bit complexity is polynomial in the dimensions and the binary length of the margins. It also gives a sampler with a fixed polynomial time bound on every execution whose total-variation error is at most $2^{-k}$ for requested precision $k\ge1$. The same Comparator file includes the companion approximation scheme for counting tables with individual cell bounds. The formalization gives a fully polynomial randomized approximation scheme for counting nonnegative integer matrices with prescribed row sums, column sums, and individual entry bounds. Both dimensions may vary, the margins and bounds are binary en
## CHALLENGE ContingencyTables  targets=['OAI.ContingencyTables.boundedSampling', 'OAI.ContingencyTables.exactSampling', 'OAI.ContingencyTables.counting'] defs=[]
theorem boundedSampling : Algorithms.BoundedSamplingStatement := by sorry
/-- Exact uniform sampling in polynomial expected bit time. -/
theorem exactSampling : Algorithms.ExactSamplingStatement := by sorry
/-- A cell-bounded FPRAS, with zero output on every infeasible execution. -/
theorem counting : Algorithms.CountingStatement := by sorry
end ContingencyTables
DEFS(35): abbrev Symbol, def encodeNat, def encodeInt, def encodeRat, structure RandomMachine, structure Configuration, def tick, def initial, def run, def Outputs, def HasMargins, def Table, def BoundedTable, theorem entry_le_row, theorem entry_le_total, instance table_finite, instance table_fintype, instance boundedTable_fintype, abbrev Machine, abbrev Symbol, def encodeMatrix, def encodeMargins, def encodeSamplingInput, def encodeCountingInput, theorem alphabetSize_neZero, def OutputsTable, def tableMass, def haltMass, def samplingSize, def BoundedSamplingStatement
## CHALLENGE ContingencyTables  targets=['OAI.ContingencyTables.boundedSampling', 'OAI.ContingencyTables.exactSampling', 'OAI.ContingencyTables.counting'] defs=[]
theorem boundedSampling : Algorithms.BoundedSamplingStatement := by sorry
/-- Exact uniform sampling in polynomial expected bit time. -/
theorem exactSampling : Algorithms.ExactSamplingStatement := by sorry
/-- A cell-bounded FPRAS, with zero output on every infeasible execution. -/
theorem counting : Algorithms.CountingStatement := by sorry
end ContingencyTables
DEFS(35): abbrev Symbol, def encodeNat, def encodeInt, def encodeRat, structure RandomMachine, structure Configuration, def tick, def initial, def run, def Outputs, def HasMargins, def Table, def BoundedTable, theorem entry_le_row, theorem entry_le_total, instance table_finite, instance table_fintype, instance boundedTable_fintype, abbrev Machine, abbrev Symbol, def encodeMatrix, def encodeMargins, def encodeSamplingInput, def encodeCountingInput, theorem alphabetSize_neZero, def OutputsTable, def tableMass, def haltMass, def samplingSize, def BoundedSamplingStatement
## PAPER Exact-Uniform-Sampling-of-Contingency-Tables-with-Arbitrary-Margins-September-24-2026
ABSTRACT: We give an exact uniform sampler for nonnegative integer contingency tables with arbitrary prescribed margins. It terminates almost surely and has expected bit complexity polynomial in both dimensions and the binary length of the margins. No positivity, balance, sparsity, or fixed-dimension assumption is required.
[theorem] \label{thm:main} For arbitrary nonnegative integer margins of equal total, the following algorithms exist in the model of unbiased random bits and bit operations. \begin{enumerate}[label=\textup{(\roman*)}] \item Given an integer $k\ge1$, a bounded-time algorithm outputs a table in $\Omega(r,c)$ whose law is within $2^{-k}$ in total variation of the uniform law. Its running time is polynomial in $m,n,\log(N+1),k$. \item An algorithm outputs an exactly uniform table in $\Omega(r,c)$, terminates almost surely, and has expected running time polynomial in $m,n,\log(N+1)$. \end{enumerate} The polynomials are uniform over all margin vectors. No positivity, sparsity, balance, or fixed-dimension hyp
## PAPER An-FPRAS-for-Cell-Bounded-Contingency-Tables-September-24-2026
ABSTRACT: We give a fully polynomial randomized approximation scheme for counting nonnegative integer matrices with prescribed row sums, column sums, and individual entry bounds. Both dimensions vary, all numerical data are encoded in binary, and zero bounds are allowed. The algorithm uses only unbiased random bits and has a polynomial bound on its bit operations on every execution.
[theorem] \label{thm:main} There is one randomized algorithm with the following guarantee. Given $(r,c,b)$ as above and rational $\varepsilon,\delta\in(0,1)$, it outputs a nonnegative rational $\widehat Z$ such that \[ \P\bigl((1-\varepsilon)Z(r,c,b)\le \widehat Z \le(1+\varepsilon)Z(r,c,b)\bigr)\ge1-\delta. \] If $\Omega(r,c,b)$ is empty, the output is zero on every execution. The algorithm uses independent unbiased bits, and one fixed polynomial in $L$, $\varepsilon^{-1}$, and $\log(\delta^{-1})$ bounds its total bit operations on every execution, where $L$ is the total binary input length, including the accuracy parameters. No counting or sampling oracle is required.
==================
# FAMILY 116: Uniform black-box noncommutative identity testing across characteristics
SCOPE: The formalization gives one explicit tuple of rational matrices that simultaneously detects every nonzero division-free noncommutative formula with at most $s$ gates in $n$ variables, for $n,s\ge1$. Evaluation at that tuple is a nonzero matrix over every characteristic-zero field. The selected theorem states this universal hitting property. The paper's deterministic polynomial bit-construction bound and matrix-dimension bound $O(ns^2)$ are not separately asserted in it. The formalized result constructs polynomial-size hitting lists for noncommutative rational formulas with rational constants, addition, multiplication, and inverse gates. Given the number of variables and a formula-size bound, one deterministic polynomial-time machine outputs rational matrix tuples of a common positive dimension. Every admissible nonzero formula within the size bound evaluates to an invertible matrix on so
## CHALLENGE FormulaHitting  targets=['OAI.NCHitting.universal_hitting'] defs=None
theorem universal_hitting (n s : ℕ) (hn : 1 ≤ n) (hs : 1 ≤ s)
    (F : Type u_2) [Field F] [CharZero F] (f : Formula F n)
    (hsize : f.size ≤ s) (hf : ∃ w, f.coeff w ≠ 0) :
    f.eval (Matrix.scalar (Fin (dimension n s)))
      (fun i r q => (generator n s i r q : F)) ≠ 0 := by
  sorry
end NCHitting
DEFS(10): abbrev Word, abbrev WordSeries, def convolution, inductive Formula, def size, def coeff, def eval, def dimension, def matrixEntry, def generator
## CHALLENGE RationalHitting  targets=['OAI.RationalHitting.main'] defs=None
theorem main : MainStatement := by
  sorry
end RationalHitting
DEFS(22): inductive Formula, def size, inductive Eval, abbrev Mat, abbrev Tuple, def Evaluates, def Admissible, def Nonzero, structure Output, def encodeNat, def encodeRat, def encodeTuple, def encodeOutput, abbrev Alphabet, abbrev Machine, abbrev Config, def tapeBit, def unaryInput, def run, def OutputsWithin, def Hits, def MainStatement
## PAPER One-Rational-Matrix-Hitting-Point-for-Noncommutative-Formulas-September-24-2026
ABSTRACT: We construct, in deterministic polynomial bit time, one tuple of rational matrices that detects every nonzero polynomial computed by a noncommutative division-free formula of a prescribed size. The matrices have dimension $O(ns^2)$ for $n$ variables and formula size $s$, and the same tuple works over every field of characteristic zero.
[theorem] \label{thm:main} There is a deterministic algorithm which, given integers $n,s\ge1$, constructs a tuple \[ \mathbf T_{n,s}\in\Mat_d(\Q)^n, \qquad d\le 2ns^2, \] in time polynomial in $n,s$, measured in bit operations. The numerators and denominators of its entries have bit length $O(\log(ns+1)+ns^2\log(n+1))$. For every field $F$ of characteristic zero and every $0\ne f\in\mathsf{Form}_{n,s}(F)$, \[ f(\mathbf T_{n,s})\ne0, \] where the tuple is viewed over $F$ through the canonical embedding $\Q\hookrightarrow F$. The construction uses $d=2ns^2$ when $ns\ge2$ and $d=1$ when $n=s=1$.
## PAPER Polynomial-Hitting-Lists-for-Noncommutative-Rational-Formulas-September-24-2026
ABSTRACT: We construct, in deterministic polynomial bit time, a polynomial-size list of rational matrix tuples for noncommutative rational formulas over $\Q$ of bounded tree size. Every nonzero admissible formula has a defined, invertible value at one tuple, with no separate bounds on inverse nesting or rational constant heights. Matrix dimensions, entry bit lengths, and total output length are polynomially bounded.
[theorem] \label{thm:main} There are a deterministic Turing machine $G$ and fixed positive integers $C,k$ with the following property. Given $1^n,1^s$, where $n,s\geq1$, the machine outputs a finite list $\mathcal H_{n,s}$ of $n$-tuples of rational square matrices, in at most $C(n+s+1)^k$ bit operations. The entire output, with signed binary numerators and positive binary denominators, has at most $C(n+s+1)^k$ bits. For every nonzero admissible rational formula $\Phi$ in $n$ variables of size at most $s$, some tuple in $\mathcal H_{n,s}$ is a defined evaluation of $\Phi$ with invertible value. The same list works for all such formulas, regardless of the bit lengths of their rational constants or their
==================
# FAMILY 117: Uniform sparsest cut: hardness and semidefinite gaps
SCOPE: The formalized result gives integrality gaps for the Goemans–Linial relaxation of uniform sparsest cut. Along a sequence of instance sizes $n\to\infty$, the ratio of the integral optimum to the positive relaxation optimum is at least $c\sqrt{\log n}/(\log\log n)^3$ for one absolute $c>0$. Every unordered pair has unit demand, and the relaxation uses squared Euclidean distances satisfying the triangle inequalities. The result is an existential sequence, not a bound for every size or a computational hardness theorem.
## CHALLENGE UniformSparsestCut  targets=['OAI.UniformSparsestCut.mainGap'] defs=[]
theorem mainGap :
    ∃ c : ℝ, 0 < c ∧
      ∃ n : ℕ → ℕ, ∃ C : (j : ℕ) → Capacity (n j),
        (∀ j, 2 ≤ n j) ∧
        Tendsto n atTop atTop ∧
        (∀ j, 0 < glValue (C j)) ∧
        ∀ᶠ j in atTop,
          c * Real.sqrt (Real.log (n j : ℝ)) / (Real.log (Real.log (n j : ℝ))) ^ 3 ≤
            OPT (C j) / glValue (C j) := by
  sorry
end UniformSparsestCut
end
DEFS(7): structure Capacity, def pairSum, def cutRatio, def OPT, def NegativeType, def Feasible, def glValue
## PAPER Near-square-root-logarithmic-integrality-gaps-for-uniform-sparsest-cut-September-24-2026
ABSTRACT: We construct uniform sparsest-cut instances whose Goemans--Linial semidefinite integrality gap is at least $c\sqrt{\log n}/(\log\log n)^3$ along a sequence $n\to\infty$. The demand is one between every pair of distinct vertices, and the capacities are nonnegative real numbers. This matches the Arora--Rao--Vazirani upper bound up to a power of $\log\log n$.
[theorem] \label{thm:main} There are an absolute constant $c>0$ and capacity instances $C^{(j)}$ on $n_j\to\infty$ vertices, with $\GL(C^{(j)})>0$, such that \[ \frac{\OPT(C^{(j)})}{\GL(C^{(j)})} \ge c\,\frac{\sqrt{\log n_j}}{(\log\log n_j)^3} \] for all sufficiently large $j$. The demand is one between every pair of distinct vertices.
==================
# FAMILY 118: Bin packing and unbounded configuration-LP gaps
SCOPE: The formalized results rule out a universal additive bound for the configuration linear program in bin packing. For every integer $c\ge0$, there are an integer $B$ and a rational instance with $5B$ items whose individual-copy and size-type configuration-LP values both equal $B$, but whose integral optimum is greater than $B+c$. Distinguishing a packing in $B$ bins from the absence of one in $B+c$ bins is NP-hard for each fixed $c$. A deterministic polynomial-time algorithm with a fixed absolute additive allowance exists exactly when $P=NP$; under that equality, an optimal algorithm is constructed.
## CHALLENGE BinPackingGap  targets=['OAI.BinPackingGap.main_results'] defs=[]
theorem main_results :
    (∀ c : ℕ, ∃ I : Instance, ∃ B : ℕ,
      I.n = 5 * B ∧
      (∀ i, (1 / 6 : ℚ) < I.size i ∧ I.size i < 1) ∧
      B + c < opt I ∧ individualLP I = (B : ℝ) ∧ typeLP I = (B : ℝ)) ∧
    (∀ c : Nat, PackingGapNPHard c) ∧
    ((∃ c : Nat, Nonempty (AbsoluteAdditiveAlgorithm c)) ↔ PEqualsNP) ∧
    (PEqualsNP → ∃ algorithm : AbsoluteAdditiveAlgorithm 0,
    (∀ (items : RawInstance) (valid : items.Valid), ∃ packing : RawPacking,
      algorithm.run (BinaryEncoding.rawInstanceBits items) = some packing ∧
      packing.Feasible items ∧ packing.bins = opt (items.toInstance valid)) ∧
    algorithm.run (BinaryEncoding.rawInstanceBits []) = some ⟨0, []⟩ ∧
    (∀ input : List Bool, BinaryEncoding.decodeRawInstance input = none →
      algorithm.run input = none) ∧
    (∀ items : RawInstance, ¬ items.Valid →
      algorithm.run (BinaryEncoding.rawInstanceBits items) = none))  := by
  sorry
end BinPackingGap
end
DEFS(70): def encodeWord, def FiniteAlphabet, def pairBits, structure NPVerifier, def NPVerifier.Accepts, def InNP, def bitsValue, def frame, def parseFrame, def nameBits, def parseName, structure Instance, abbrev Item, structure Packing, def HasPacking, def singletonPacking, theorem exists_packing, def opt, def IndividualConfiguration, def NumericalSize, theorem positive, def multiplicity, def capacityBound, theorem capacityBound_spec, def TypeConfiguration, theorem count_lt_bound, def boundedCounts, theorem boundedCounts_injective, def Feasible, def objective
## PAPER Additive-hardness-and-unbounded-configuration-gaps-in-bin-packing-September-24-2026
ABSTRACT: We disprove the Modified Integer Round-Up Conjecture for bin packing by constructing instances with arbitrarily large additive gaps between the configuration-LP value and the integral optimum. We also prove that, for every fixed nonnegative integer $c$, distinguishing instances that fit in $B$ bins from those requiring more than $B+c$ bins is NP-hard. Both results hold with rational item sizes greater than $1/6$, so each bin contains at most five items.
[theorem[Unbounded configuration gap]] \label{thm:unbounded-gap} For every integer $c\ge0$, there is a finite rational bin-packing instance $I$ and an integer $B$ such that every item size exceeds $1/6$ and \begin{equation}\label{eq:main-gap} \LP(I)=B, \qquad \OPT(I)>B+c. \end{equation} The equality for the fractional optimum also holds for the configuration LP whose patterns are subsets of the individual item copies.
==================
# FAMILY 119: The Courtade–Kumar and Hellinger conjectures
SCOPE: The formalization proves sharp contraction of the information carried by a binary channel under independent symmetric noise on a uniform discrete cube. At each fixed initial information level, a noisy coordinate channel attains the maximum retained information. It also proves the refined Boolean bound that accounts for output bias, with strict improvement for nonconstant biased outputs at nonzero noise correlation, and the selected mean-dependent entropy-production inequality. For Boolean functions this includes the Courtade–Kumar inequality $I(f(X);Y)\le1-h_2(\varepsilon)$ in bits at crossover probability $0\le\varepsilon\le1/2$, where $h_2$ is binary entropy. A coordinate and its complement attain equality.
## CHALLENGE CourtadeKumar  targets=['OAI.LeanBlast.CourtadeKumar.courtadeKumarAndAttainment'] defs=[]
theorem courtadeKumarAndAttainment : FullStatement := by
  sorry
end LeanBlast.CourtadeKumar
end
DEFS(16): abbrev Cube, abbrev Cube, def cubeAverage, def ell, def bitFlipKernel, def jointProbability, def functionMarginal, def observationMarginal, def xlogx, def binaryEntropy, def mutualInformation, def dictator, def complementDictator, def CourtadeKumarStatement, def DictatorAttainmentStatement, def FullStatement
## CHALLENGE SoftChannel204  targets=['OAI.SoftChannel204.fullMain'] defs=[]
theorem fullMain : FullMain := by
  sorry
end SoftChannel204
end
DEFS(34): abbrev Cube, def sign, def avg, def L, def psi, def H, def info, def psiInv, def kernel, def noise, def Closed, def Interior, def softCoordinate, def flip, def numberOperator, def production, def F, def S, def reserve, def hybrid, def softJoint, def boolJoint, def leftMarginal, def rightMarginal, def mutualInformation, def binaryEntropyBits, def SoftContraction, def SoftAttainment, def SoftInformationIdentity, def RefinedBoolean
## PAPER Sharp-binary-information-contraction-on-the-discrete-cube-September-24-2026
ABSTRACT: We prove sharp contraction of the information carried by a binary channel under independent symmetric noise on a uniform discrete cube. At fixed initial information, a noisy coordinate retains the most information. The Boolean specialization resolves the Courtade--Kumar conjecture and gives an output-entropy refinement. We also establish a stronger mean-dependent entropy-production bound. The proof combines an explicit three-point optimizer for the local joining problem, two entropy capacities, and a common-output thinning inequality, followed by dimension induction and integration along the noise semigroup.
[theorem[Sharp soft-channel contraction]] \label{main:soft} For every finite $n\ge0$, every $u:\Omega_n\to[-1,1]$, and $-1\le\rho\le1$, \begin{equation} I(T_\rho u) \le\psi\!\left(|\rho|\,\psi^{-1}(I(u))\right). \label{main:interpolation} \end{equation} The inverse is the nonnegative increasing branch on $[0,L]$. For $n\ge1$, every soft coordinate $u(x)=a x_i$, $|a|\le1$, attains equality.
==================
# FAMILY 121: Almost-linear approximation of edit distance
SCOPE: The formalization gives a randomized $(1+\varepsilon)$-approximation for unit-cost edit distance between explicitly stored integer strings, for every fixed rational $0<\varepsilon<1$. Its estimate is at least the true distance and at most $(1+\varepsilon)$ times it with probability at least $2/3$; equal strings return zero on every execution. For total length at most $N$ and integer symbols bounded by a fixed polynomial in $N$, expected work is at most $(N+2)^{1+\eta}$ for every fixed $\eta>0$ and all sufficiently large $N$. Space is polynomially bounded on every execution.
## CHALLENGE EditApproximation  targets=['OAI.EditApproximation.almostLinearEditDistanceRawBand'] defs=[]
theorem almostLinearEditDistanceRawBand (epsilon : OAI.EditApproximation.BinaryFraction)
    (hepsilon : 0 < epsilon.value) (_hepsilonOne : epsilon.value < 1)
    :
    (∀ (source target : List ℤ) (N : ℕ), source.length + target.length ≤ N →
      (2 / 3 : ℝ) ≤ (OAI.EditApproximation.computedFullLaw (source.map OAI.EditApproximation.integerSymbolCode) (target.map OAI.EditApproximation.integerSymbolCode) N epsilon).real
        {outcome | EditDistortion.edit source target ≤ OAI.EditApproximation.integerBinaryAnswerRawBand source target N epsilon outcome ∧
          (OAI.EditApproximation.integerBinaryAnswerRawBand source target N epsilon outcome : ℝ) ≤
            (1 + (epsilon.value : ℝ)) * OAI.EditDistortion.edit source target}) ∧
    (∀ (source target : List ℤ) (N : ℕ), source = target → ∀ outcome,
      OAI.EditApproximation.integerBinaryAnswerRawBand source target N epsilon outcome = 0) ∧
    (∀ (C : ℕ) (eta : ℝ), 0 < eta → ∀ᶠ N : ℕ in atTop,
      ∀ source target : List ℤ, source.length + target.length ≤ N →
        (∀ z ∈ source ++ target, z.natAbs ≤ (N + 2) ^ C) →
        (∫ outcome, OAI.EditApproximation.integerBinaryWorkRawBand source target N epsilon outcome
          ∂OAI.EditApproximation.computedFullLaw (source.map OAI.EditApproximation.integerSymbolCode) (target.map OAI.EditApproximation.integerSymbolCode) N epsilon) ≤
            (N + 2 : ℝ) ^ (1 + eta)) ∧
    (∀ C : ℕ, ∀ᶠ N : ℕ in atTop, ∀ source target : List ℤ,
      source.length + target.length ≤ N →
        (∀ z ∈ source ++ target, z.natAbs ≤ (N + 2) ^ C) →
        ∀ outcome, OAI.EditApproximation.integerBinarySpaceFootprintRawBand source target N epsilon outcome ≤ (N + 2) ^ (C + 65564)) := by
  sorry
end OAI.EditApproximation
DEFS(1155): def bitWordValue, def bitSum, def bitCarry, structure UnreducedRational, def orderingMatches, def bitOrdering, def bitDifference, def bitBorrow, structure SignedBinary, def signedMagnitude, def trimBitWordWithWork, def balancedCut, def gridRound, def rationalMinimum, structure RationalBellmanAction, def rationalRefinementUpdate, def heightExponent, def coarseExponent, structure IntegerParameters, structure RationalParameters, def gridPointsBetween, def scaledSeedValue, def dyadicScales, def seedGridSpacing, def finiteAssignments, def powerTwoWord, def filterWithWork, def allWithWork, def arithmeticMapWithWork, def arithmeticFlatMapWithWork
## PAPER An-Almost-Linear-Approximation-Scheme-for-Edit-Distance-September-24-2026
ABSTRACT: We give a uniform randomized approximation scheme for unit-cost edit distance. For every fixed rational $\varepsilon\in(0,1)$, it estimates the distance between arbitrary explicitly stored strings of total length $N$ within a factor $1+\varepsilon$ with probability at least $2/3$, in worst-case expected time $N^{1+o(1)}$ on a logarithmic-word RAM. The algorithm supports polynomially bounded integer alphabets and returns zero deterministically on equal strings.
[theorem] \label{thm:main} There is one uniform randomized algorithm that, given $x,y$ and a rational $\varepsilon\in(0,1)$, returns a nonnegative integer $\widehat D$ such that \[ \Pr\bigl[\ED(x,y)\le \widehat D\le(1+\varepsilon)\ED(x,y)\bigr] \ge \frac23. \] For every fixed rational $\varepsilon$, its worst-case expected running time on strings of total length $N$ is $N^{1+o(1)}$ as $N\to\infty$ on the logarithmic-word RAM. The expectation is over internal randomness only, and the bound includes input processing, preprocessing, numerical work, random sampling and all data-structure operations. Equal strings return zero deterministically.
==================
# FAMILY 122: Quantitative trace-reconstruction bounds with a uniform decoder
SCOPE: The formalization proves superpolynomial sample lower bounds for exact worst-case reconstruction of binary words from independent deletion traces, with unrestricted computation and any fixed positive success probability. For every fixed deletion probability $q\in(0,1)$, sample complexity grows faster than every fixed power of the word length; the minimum total-variation distance between two one-trace laws decays faster than every inverse power. More quantitatively, along sequences with $q^3\log n\to\infty$, the required number of samples is at least $n^{c\log(q^3\log n)}$ eventually for every fixed $0<c<1/(4\log2)$. All logarithms are natural.
## CHALLENGE TraceReconstruction  targets=['OAI.TraceReconstruction.quantitative_sample_lower_bound', 'OAI.TraceReconstruction.superpolynomial_one_trace', 'OAI.TraceReconstruction.superpolynomial_sample_complexity'] defs=[]
theorem quantitative_sample_lower_bound
    (s c : ℝ) (hs : s ∈ Set.Ioc 0 1)
    (hc : c ∈ Set.Ioo 0 (1 / (4 * Real.log 2)))
    (n : ℕ → ℕ) (q : ℕ → ℝ)
    (hn : Tendsto n atTop atTop)
    (hq : ∀ k, q k ∈ Set.Ioo 0 1)
    (hscale : Tendsto (fun k => (q k) ^ 3 * Real.log (n k)) atTop atTop) :
    ∀ᶠ k in atTop,
      ENNReal.ofReal ((n k : ℝ) ^ (c * Real.log ((q k) ^ 3 * Real.log (n k)))) ≤
        sampleComplexity (n k) (q k) s := by
  sorry
theorem superpolynomial_one_trace
    (q : ℝ) (hq : q ∈ Set.Ioo 0 1) (C : ℝ) (hC : 0 < C) :
    Tendsto (fun n : ℕ => (n : ℝ) ^ C * minTraceTV n q) atTop (𝓝 0) := by
  sorry
theorem superpolynomial_sample_complexity
    (q : ℝ) (hq : q ∈ Set.Ioo 0 1) (s : ℝ) (hs : s ∈ Set.Ioc 0 1)
    (C : ℝ) (hC : 0 < C) :
    Tendsto
      (fun n : ℕ => sampleComplexity n q s / ENNReal.ofReal ((n : ℝ) ^ C))
      atTop (𝓝 ⊤) := by
  sorry
end TraceReconstruction
end
DEFS(13): abbrev Word, abbrev Mask, abbrev Trace, def traceOfMask, def maskWeight, def traceMass, def traceSpace, def traceTV, def IsEstimator, def reconstructionSuccess, def SufficientBudget, def sampleComplexity, def minTraceTV
## PAPER quantitative-lower-bounds-for-trace-reconstruction-September-24-2026
ABSTRACT: Exact worst-case reconstruction of a binary word from independent deletion traces requires $n^{\Omega(\log\log n)}$ samples for every fixed deletion probability $q\in(0,1)$, even with unrestricted computation and any fixed positive success probability. This gives a negative answer to the polynomial-sample question for binary trace reconstruction. More generally, when $q^3\log n\to\infty$, we prove a lower bound of $n^{c\log(q^3\log n)}$ samples for every fixed $0<c<1/(4\log2)$. Here $q$ is the known deletion probability, and all logarithms are natural.
[theorem[Quantitative sample lower bound]] \label{thm:main} Fix $s\in(0,1]$ and $0<c<1/(4\log2)$. Along every sequence of instances $(n,q)$ with $n\to\infty$, $q\in(0,1)$, and $q^3\log n\to\infty$, \begin{equation}\label{eq:main-bound} T_{q,s}(n)\ge n^{c\log(q^3\log n)} \end{equation} eventually. All logarithms are natural. In particular, for each fixed deletion probability $q\in(0,1)$ and fixed positive success probability $s$, the required sample number is $n^{\Omega(\log\log n)}$.
==================
# FAMILY 124: Polynomial-time scheduling on three identical machines
SCOPE: The formalization gives a deterministic polynomial-time algorithm for scheduling nonempty collections of unit-length jobs with arbitrary acyclic precedence constraints on three identical parallel machines. It constructs a schedule of minimum makespan and decides exactly whether a valid specified deadline can be met. The algorithm is one fixed finite machine, and its running time is bounded by a polynomial in the binary input length.
## CHALLENGE ThreeMachine  targets=['OAI.ThreeMachine.main_theorem'] defs=[]
theorem main_theorem : ReleaseTheorem := by
  sorry
end ThreeMachine
DEFS(18): structure Instance, def Instance.edge, def Instance.acyclic, def Feasible, def encodeNat, def encodeList, def encodeInput, def encodeAnswer, def slots, def CorrectOutput, structure Machine, structure Configuration, def bitSymbol, def Machine.step, def Machine.initial, def Machine.run, def Machine.Produces, def ReleaseTheorem
## PAPER A-polynomial-time-algorithm-for-three-machine-unit-job-scheduling-September-24-2026
ABSTRACT: We give a uniform deterministic polynomial-time algorithm for scheduling unit-length jobs with arbitrary precedence constraints on three identical parallel machines. The algorithm constructs a schedule of minimum makespan and decides exactly whether all jobs can finish by a specified deadline. The proof reorganizes feasible schedules into intervals whose job sets have descriptions of bounded size. A dynamic program searches a family containing polynomially many such descriptions. Global boundary conditions and simplification of inherited information keep the descriptions bounded throughout the decomposition.
[theorem] \label{thm:main} Let an explicitly listed finite directed acyclic graph specify the precedence constraints on \(n\ge1\) nonpreemptive unit-length jobs on three identical machines. There is a uniform deterministic algorithm that constructs a feasible schedule of minimum makespan. Given also an integer deadline \(1\le T\le n\), it decides feasibility exactly and returns a schedule whenever the answer is affirmative. Both tasks can be performed in \(O((L+2)^{150020})\) steps on a deterministic multitape Turing machine, where \(L\) is the total binary input length.
==================
# FAMILY 125: The metric <i>k</i>-median approximation threshold and recovery
SCOPE: The formalization gives an exact-budget recovery algorithm for metric $k$-median on the stated polynomially bounded integral metrics. Suppose a supplied anchor represents all but logarithmically many comparison clusters by distinct proxies, with total proxy cost at most the comparison cost plus a sufficiently small relative error. The algorithm always opens at most $k$ facilities and, with any requested confidence, attains a $(1+2/e+\varepsilon)$ factor relative to those comparison centers in polynomial time. The linked final approximation result applies to arbitrary finite rational metrics. For one absolute $\sigma>0$, a polynomial-time fair-bit algorithm always returns a feasible solution, has expected cost at most $(2-\sigma)\mathrm{OPT}$, and attains the same factor with arbitrarily high polynomial confidence. The formalization gives, for every fixed $\varepsilon>0$, a deterministic 
## CHALLENGE KMedianRecovery  targets=['OAI.MetricKMedianRecovery.global_application'] defs=[]
theorem global_application : globalApplicationClaim := by
  sorry
end MetricKMedianRecovery
DEFS(19): structure RationalMetricInput, def size, def Feasible, def cost, def comparisonSets, lemma comparisonSets_nonempty, def optimum, def natBits, def rationalBits, def bits, def decodeOutput, def pairBits, structure BinaryRandomizedAlgorithm, def bitCount, abbrev Seed, def output, def successProbability, def expectedCost, def globalApplicationClaim
## CHALLENGE KMedianRefinedRecovery  targets=['OAI.MetricKMedianRecovery.RefinedRecovery.refined_recovery'] defs=[]
theorem refined_recovery :
    ∀ (bound : Polynomial ℕ) (ε L₀ : ℝ) (μ : ℚ),
      0 < ε → 0 < L₀ → 0 < μ → μ ≤ 1/4 → (μ : ℝ) ≤ ε/12 →
      ∃ A : BinaryRandomizedAlgorithm,
        PolynomialWork A bound ∧
        ∀ I : Input, I.Bounded bound → ∀ ζ : ℝ, 0 < ζ → ζ < 1 →
          (∀ s : Seed A I ζ, I.metric.Feasible (output A I ζ s)) ∧
          (∀ C : Certificate I μ L₀,
            1 - ζ ≤ successProbability A I ζ
              ((1 + 2 / Real.exp 1 + ε) * (I.metric.cost C.centers : ℝ))) := by
  sorry
end MetricKMedianRecovery.RefinedRecovery
DEFS(27): structure RationalMetricInput, def size, def Feasible, def cost, def natBits, def rationalBits, def bits, def decodeOutput, def pairBits, structure BinaryRandomizedAlgorithm, structure Input, abbrev Point, def size, def Bounded, def assign, def cluster, def clusterCost, def anchorBits, structure Certificate, def precision, def queryBits, def seedLength, abbrev Seed, def output, def successProbability, def workBound, def PolynomialWork
## CHALLENGE KMedianThreshold  targets=['OAI.MetricKMedian.threshold'] defs=[]
theorem threshold (h : Complexity.PNeNP) :
    sInf approximationFactors=1+2/Real.exp 1 := by
  sorry
end MetricKMedian
DEFS(19): structure Instance, def encodeNat, def encodeRat, def encodeInstance, def nearest, def cost, def feasibleSets, def optimum, def Correct, def FinitePolyTime, abbrev Word, abbrev Language, def encodeBit, def encodePair, def P, def NP, def PNeNP, def FactorCorrect, def approximationFactors
## CHALLENGE MetricKMedian  targets=['OAI.MetricKMedian.main_finite_work'] defs=[]
theorem main_finite_work : ∀ ε : ℝ, 0 < ε →
    ∃ (algorithm : Instance → List Bool) (P : Turing.TM2ComputableInPolyTime encodeInstance id algorithm),
      (∀ k : P.tm.K, Finite (P.tm.Γ k)) ∧ ∀ I, Correct ε I (algorithm I) := by
  sorry
end MetricKMedian
end
end
DEFS(9): structure Instance, def encodeNat, def encodeRat, def encodeInstance, def nearest, def cost, def feasibleSets, def optimum, def Correct
## PAPER Single-Exponential-Recovery-and-Bounded-Price-Strictness-for-Metric-k-Median-September-24-2026
ABSTRACT: We give an exact-budget recovery algorithm for metric $k$-median with single-exponential dependence on the number of comparison clusters without accurate, distinct proxies in a supplied anchor solution. On positive integral metrics of polynomially bounded diameter, a sufficiently small total proxy error and logarithmically many such clusters yield a $(1+2/e+\varepsilon)$ approximation in polynomial time with arbitrarily high success probability. We also prove bounded-price strictness for one compatible execution of the logarithmic-surplus construction. Together the recovery and payment arguments give a randomized $(2-\sigma)$ approximation, for an absolute $\sigma>0$, on arbitrary finite rat
[theorem[Refined recovery]] \label{ref:recovery} Let $D$ and $F$ be disjoint indexed sets in a metric whose distances between distinct indices are positive integers bounded by a fixed polynomial in $N=|D|+|F|$. Fix $\varepsilon>0$ and $0<L_0<\infty$, and choose a fixed rational parameter \[ 0<\mu\le \min\{1/4,\varepsilon/12\}. \] Let $S\subseteq F$ have cardinality $h\ge1$. Suppose there exists a comparison solution $O\subseteq F$ of cardinality $h$ and cost $P>0$, with a partition into good and bad centers and distinct proxies $\phi_i\in S$ for the good centers, such that \begin{equation}\label{ref:proxy-hypothesis} \sum_{i\ \mathrm{good}}\sum_{p\in C_i}d(p,\phi_i) \le P_g+\mu P, \qquad m:=|\{i:i\ \mathrm{bad}\}|\le L
## PAPER The-Approximation-Threshold-for-Metric-k-Median-September-24-2026
ABSTRACT: For every fixed \(\varepsilon>0\), we give a deterministic polynomial-time \((1+2/e+\varepsilon)\)-approximation for finite rational metric \(k\)-median with specified candidate facilities, opening at most \(k\) facilities. Under \(P\ne NP\), the infimum approximation factor in this model is therefore \(1+2/e\).
[theorem] \label{thm:main} For every fixed \(\varepsilon>0\), there is a deterministic algorithm which, given a finite rational metric \(k\)-median instance with \(1\le k\le |F|\), returns \(S\subseteq F\), \(|S|\le k\), such that \[ \sum_{j\in J}d(j,S)\le \left(1+\frac2e+\varepsilon\right)\OPT_k. \] Its running time is polynomial in the binary encoding length of the instance. The polynomial may depend on \(\varepsilon\).
==================
# FAMILY 126: Exponential semidefinite complexity of perfect matching
SCOPE: The paper proves exponential PSD-rank lower bounds for positively shifted matching matrices. The linked formalization records the related superpolynomial lower bounds: for every fixed $C>0$, the PSD rank of the selected perfect-matching slack matrix exceeds $n^C$ for all sufficiently large even $n$. Every exact affine semidefinite lift of the perfect-matching polytope likewise requires matrix size greater than $n^C$. These selected statements give superpolynomial growth. They do not state the paper's exponential bound for every fixed positive shift.
## CHALLENGE MatchingAffineLift  targets=['OAI.PerfectMatchingPSD.affine_lift_lower_bound'] defs=[]
theorem affine_lift_lower_bound :
    ∀ C : ℝ, 0 < C → ∃ n₀ : ℕ, 4 ≤ n₀ ∧
      ∀ n : ℕ, n₀ ≤ n → Even n → ∀ r : ℕ,
        HasAffineLift n r → (n : ℝ) ^ C < (r : ℝ) := by
  sorry
end PerfectMatchingPSD
DEFS(6): abbrev Edge, def IsPerfectMatching, abbrev PerfectMatching, def matchingPoint, def matchingPolytope, def HasAffineLift
## CHALLENGE MatchingPSD  targets=['OAI.PerfectMatchingPSD.main'] defs=[]
theorem main : MainClaim := by
  sorry
end PerfectMatchingPSD
DEFS(11): abbrev Edge, def IsPerfectMatching, abbrev PerfectMatching, abbrev OddCut, abbrev Row, def Crosses, def crossingCount, def slack, def HasFactorization, def psdRank, def MainClaim
## PAPER Exponential-PSD-rank-of-positively-shifted-matching-matrices-October-5-2026
ABSTRACT: For every fixed $0<\rho<1$, the matrix indexed by odd vertex sets $U$ and perfect matchings $M$ of $K_n$, with entries $|M\cap\delta(U)|-1+\rho$, has real positive semidefinite rank $2^{\Omega(n)}$ as even $n$ tends to infinity. Here $\delta(U)$ is the edge cut of $U$. Consequently, every exact semidefinite lift of the perfect matching polytope has exponential size.
[theorem] \label{thm:main} There is a constant $c>0$ such that, for every fixed $0<\rho<1$, there is $n_0=n_0(\rho)$ for which \[ \rankpsd A_n(\rho)\ge2^{cn} \] for every even $n\ge n_0$.
==================
# FAMILY 127: Average sensitivity of polynomial threshold functions
SCOPE: The formalized result proves the average-sensitivity bound $8d\sqrt n$ for every Boolean threshold function defined by a real multilinear polynomial of degree at most $d$ on the $n$-dimensional cube. The sign convention assigns value $1$ at zero. This establishes the stated asymptotic bound, rather than the separate conjecture identifying exact extremizers.
## CHALLENGE GotsmanLinial  targets=['OAI.LeanBlast.GotsmanLinial.gotsmanLinialStatement'] defs=[]
theorem gotsmanLinialStatement : GotsmanLinialStatement := by
  sorry
end LeanBlast.GotsmanLinial
DEFS(10): abbrev Cube, def cubeCoord, def flip, def thresholdSign, def sensitiveVertices, def averageSensitivity, def IsMultilinear, def polynomialValue, def polynomialThreshold, def GotsmanLinialStatement
## PAPER Average-Sensitivity-of-Polynomial-Threshold-Functions-September-25-2026
ABSTRACT: For every $n\ge1$ and $1\le d\le n$, we prove that a polynomial threshold function of degree at most $d$ on the uniform Boolean cube has average sensitivity at most $8d\sqrt n$. This proves the asymptotic form of the Gotsman--Linial conjecture. The bound is uniform in both parameters and uses the convention $\sgn(0)=1$.
[theorem] \label{thm:main} Let $n\ge1$ and $1\le d\le n$ be integers. Let $p$ be a real multilinear polynomial of degree at most $d$, and define $f:\{-1,1\}^n\to\{-1,1\}$ by $f(x)=\sgn(p(x))$, with $\sgn(0)=1$. Then, for average sensitivity under the uniform law, \[ I(f)\le 8d\sqrt n. \]
==================
# FAMILY 128: A factor-two approximation for shortest common superstring
SCOPE: The shortest common superstring problem asks for the shortest string containing each input string as a contiguous substring. The formalized result gives one deterministic polynomial-time algorithm whose output is a common superstring of length at most twice the unrestricted optimum. It applies to every finite list of explicitly encoded strings, with running time measured in input bits and the approximation ratio measured in symbol length.
## CHALLENGE Superstring  targets=['OAI.Superstring.main'] defs=[]
theorem main : ∃ f : Instance → Word,
    HasPolynomialImplementation f ∧
    ∀ S, IsCommonSuperstring S (f S) ∧ (f S).length ≤ 2 * opt S := by
  sorry
end Superstring
DEFS(10): abbrev Symbol, abbrev Word, abbrev Instance, def encodeList, def encodeSymbol, def encodeWord, def encodeInstance, def IsCommonSuperstring, def opt, def HasPolynomialImplementation
## PAPER A-Polynomial-Time-2-Approximation-for-Shortest-Common-Superstring-September-24-2026
ABSTRACT: We give a deterministic algorithm that, for every finite family of explicitly represented ordinary strings, outputs a common superstring of length at most twice the optimum in time polynomial in the total encoded input size, including symbol labels. The guarantee applies to the algorithm constructed here, not the classical maximum-overlap Greedy procedure.
[theorem] \label{thm:main} There is a deterministic algorithm, polynomial in the total encoded input size, that on every finite collection $\mathcal S$ of explicitly represented ordinary strings outputs a common superstring $T$ satisfying \[ \len{T}\le 2\OPT(\mathcal S). \]
==================
# FAMILY 129: Exponential state costs for two-way automata
SCOPE: The paper asks how many states are needed to complement or determinize two-way nondeterministic finite automata. The formalization gives, for every $n\ge4$, an explicit $n$-state automaton whose complement requires at least $\tfrac12 2^{\lfloor(n-4)/127\rfloor}-1$ states. For the same family of relational languages and every $n\ge131$, every equivalent deterministic two-way automaton requires at least $\tfrac12 2^{\lfloor(n-4)/127\rfloor}$ states. The alphabet grows with $n$, so neither complementation nor determinization has a polynomial state bound uniform over alphabets. The model has two endmarkers, left, right, and stay moves, and acceptance by a finite run. The separate results about one-way liveness and the Sakoda–Sipser problem are outside this scope. The formalization gives a family of one-way nondeterministic automata with $h+3$ states whose languages require exponentially many
## CHALLENGE TwoWayComplementation  targets=['OAI.TwoWayComplementation.complementation_lower_bound_finite'] defs=[]
theorem complementation_lower_bound_finite (n : ℕ) (hn : 4 ≤ n) :
    ∃ A : TwoNFA (SetRel (Fin (n - 2)) (Fin (n - 2))) (Fin n),
      ∀ (Q : Type*) [Fintype Q], ∀ B : TwoNFA (SetRel (Fin (n - 2)) (Fin (n - 2))) Q,
        B.language = A.languageᶜ →
          (1 / 2 : ℝ) * 2 ^ ((n - 4) / 127) - 1 ≤ (Fintype.card Q : ℝ) := by
  sorry
end TwoWayComplementation
DEFS(5): def relStar, structure TwoNFA, def tapeSymbol, def step, def language
## CHALLENGE TwoWayDeterminization  targets=['OAI.TwoWayComplementation.explicit_family_main'] defs=[]
theorem explicit_family_main (n : ℕ) (hn : 4 ≤ n) :
    ∃ A : TwoNFA (SetRel (Fin (n - 2)) (Fin (n - 2))) (Fin n),
      A.language = sourceLanguage (Fin (n - 2)) ∧
      (∀ (Q : Type*) [Fintype Q],
        ∀ B : TwoNFA (SetRel (Fin (n - 2)) (Fin (n - 2))) Q,
        B.language = A.languageᶜ →
          (1 / 2 : ℝ) * 2 ^ ((n - 4) / 127) - 1 ≤ (Fintype.card Q : ℝ)) ∧
      (131 ≤ n → ∀ (Q : Type*) [Fintype Q],
        ∀ D : TwoNFA (SetRel (Fin (n - 2)) (Fin (n - 2))) Q,
        D.Deterministic → D.language = A.language →
          (1 / 2 : ℝ) * 2 ^ ((n - 4) / 127) ≤ (Fintype.card Q : ℝ)) := by
  sorry
end TwoWayComplementation
DEFS(8): def relStar, structure TwoNFA, def tapeSymbol, def step, def language, def TwoNFA.Deterministic, def relationProduct, def sourceLanguage
## CHALLENGE OneWayLiveness  targets=['OAI.OneWayLiveness.main_theorem'] defs=[]
theorem main_theorem (h : ℕ) (hh : 2 ≤ h) :
    (∃ N : NMachine (Alphabet h) (h + 3), N.NoLeft ∧
      ∀ positive : Bool, N.Recognizes positive (OWL h)) ∧
    (∀ (positive : Bool) (s : ℕ) (D : DMachine (Alphabet h) s),
      D.Recognizes positive (OWL h) →
      2 ^ ((h - 2) / 31) ≤ 4 * (s + if positive then 2 else 1) ^ 2) := by
  sorry
end OneWayLiveness
DEFS(19): structure BRel, def live, abbrev Alphabet, def OWL, inductive Symbol, inductive Move, def Move.Rel, def scanned, abbrev Configuration, structure DMachine, structure NMachine, def DMachine.Step, def NMachine.Step, def FiniteRun, def DMachine.Accepts, def NMachine.Accepts, def NMachine.NoLeft, def NMachine.Recognizes, def DMachine.Recognizes
## PAPER An-exponential-state-lower-bound-for-two-way-nondeterministic-complementation-September-25-2026
ABSTRACT: We prove that two-way nondeterministic finite automata cannot be complemented with a polynomial number of states independent of the alphabet. For each $n\ge4$ we construct an $n$-state automaton over a finite alphabet whose complement requires at least $\tfrac12 2^{\lfloor(n-4)/127\rfloor}-1$ states.
[theorem] \label{main:theorem} For every integer $n\ge4$, set $H=\{1,\ldots,n-2\}$ and $\Sigma_n=\mathcal R_H$. There is an $n$-state 2NFA $A_n$ recognizing $L_H$ such that every 2NFA recognizing $\Sigma_n^*\setminus L(A_n)$ has at least \[ \frac12\,2^{\lfloor(n-4)/127\rfloor}-1 \] states. In particular, there is no polynomial state bound for complementation that is independent of the finite alphabet.
## PAPER An-exponential-two-way-deterministic-state-lower-bound-for-one-way-liveness-September-25-2026
ABSTRACT: One-way liveness on $h$ points accepts a word of binary relations when their ordered product is nonempty. For every $h\ge2$, it has a nondeterministic automaton with $h+3$ states and no left moves, whereas every equivalent $s$-state two-way deterministic automaton satisfies $4(s+2)^2\ge2^{\lfloor(h-2)/31\rfloor}$. Partial transition rules, stay moves, and nonaccepting infinite computations are allowed. The alphabets are finite and grow with $h$, so the result rules out an alphabet-independent polynomial state bound for deterministic two-way simulation, already for one-way nondeterministic sources.
[theorem] \label{thm:main} For every integer $h\ge2$, the language $\OWL_h$ is recognized by a nondeterministic automaton with $h+3$ states using no left moves. Every equivalent deterministic two-way automaton with $s$ states satisfies \begin{equation} \label{eq:main-bound} 4(s+2)^2\ge 2^{\lfloor(h-2)/31\rfloor}. \end{equation} If an initially accepting configuration counts as acceptance, $s+2$ in \eqref{eq:main-bound} may be replaced by $s+1$.
==================
# FAMILY 130: Exact Fourier transforms below $`n\log n`$
SCOPE: The formalized result gives exact discrete Fourier transforms with arbitrarily small normalized circuit cost along an unbounded sequence of lengths. For every $c>0$ and every cutoff $N_0\ge2$, some $n\ge N_0$ has a circuit computing the unnormalized DFT with fewer than $cn\log_2 n$ gates. Addition, subtraction, and multiplication by a predetermined complex scalar each cost one gate; diagonal scalings are charged. The result is subsequential, with no all-length, bounded-coefficient, conditioning, or bit-complexity claim. A separate uniform formalization gives fixed deterministic programs for every positive length $n$, computing the canonical discrete Fourier transform and the full convolution of two length-$n$ complex vectors exactly. Their work is $O(n(\log n)^{1-10^{-13}})=o(n\log n)$, including root-order selection and scalar preparation. The chosen root of unity is supplied; the model
## CHALLENGE ExactFourier  targets=['OAI.ExactFourier.main_theorem'] defs=[]
theorem main_theorem : MainStatement := by
  sorry
end ExactFourier
DEFS(10): inductive Gate, def Gate.eval, inductive Program, def Program.eval, structure Circuit, def Circuit.eval, def zeta, def fourierMatrix, def Circuit.Computes, def MainStatement
## CHALLENGE UniformFourier  targets=['OAI.PowerSaving.transform_main', 'OAI.PowerSaving.convolution_main'] defs=[]
theorem transform_main : DFTGoal := by
  sorry
/-- One fixed bilinear program computes convolution with the same asymptotic bounds. -/
theorem convolution_main : ConvGoal := by
  sorry
end
end PowerSaving
DEFS(56): def zeta, structure Tape, def empty, def tab, def look, theorem look_of_lt, theorem look_of_le, def set, def sow, def map, inductive Paint, inductive Ty, abbrev sc, def Ty.T, def Ty.blank, structure Bill, def pay, def pass, def one, def word, def steps, def sow, def tab, inductive NOp, inductive Atom, def NOp.run, def Atom.run, abbrev Port, inductive Code, def Handler
## PAPER Finite-tensor-savings-and-exact-Fourier-circuits-September-25-2026
ABSTRACT: We construct exact nonuniform Fourier circuits of size $o(n\log n)$ along an unbounded sequence of lengths, counting every addition, subtraction, and scalar multiplication. This refutes the $\Omega(n\log n)$ lower bound in the unrestricted complex linear-circuit model. The construction uses a finite tensor saving: a tensor power of some invertible nonmonomial complex matrix can be computed with fewer matrix calls than the standard tensor-axis algorithm on the same coordinates, when invertible monomial maps are allowed freely between calls.
[theorem] \label{thm:main} In this model, \[ \liminf_{n\to\infty}\frac{L(n)}{n\log_2 n}=0. \] Equivalently, for every $c>0$ and every integer $N_0\ge2$, there is an integer $n\ge N_0$ and an exact circuit for $F_n$ with fewer than $c n\log_2 n$ gates.
## PAPER An-explicit-power-saving-for-the-exact-discrete-Fourier-transform-September-25-2026
ABSTRACT: We give a deterministic algorithm that computes the discrete Fourier transform at every length $n$ in $O(n(\log n)^{1-10^{-13}})$ operations. The model uses exact complex arithmetic, unrestricted coefficients, specified Fourier roots, and unit-cost logarithmic-size indexing; scalar preparation and array organization are included.
[theorem] \label{thm:main} There is a single deterministic algorithm which, for every positive integer $n$ and every $x\in\C^n$, computes $F_nx$ exactly. In the model above, including scalar preparation, schedule construction, and index work, its running time is \begin{equation}\label{eq:main-bound} O\!\left(n(\log n)^\theta(\log\log n)^{4-\theta}\right) \end{equation} as $n\to\infty$. It suffices to supply the specified root $\zeta_{D_*}$ for an explicitly computable integer $D_*<1024n^3$.
==================
# FAMILY 131: Rapid mixing of graph switches for every degree sequence
SCOPE: The Kannan–Tetali–Vempala conjecture asks for polynomial mixing of the switch chain for every graphical degree sequence. The formalization proves the simple undirected case: for $n\ge4$, the lazy chain that proposes switches on four vertices has total-variation mixing time at distance $1/4$ at most $2n^8$. It also proves switch connectivity, the stated exponential total-variation bound, and a spectral gap of at least $1/(24n^2\binom n4)$ when more than one graph realizes the degree sequence. The paper's exactly uniform sampling algorithm is outside these selected chain estimates.
## CHALLENGE SwitchChain  targets=['OAI.Problem315.switch_chain_main', 'OAI.Problem315.switch_chain_tv_bound', 'OAI.Problem315.switch_connectivity'] defs=[]
theorem switch_chain_main :
    ∀ (n : Nat) (d : Fin n → Nat), 4 ≤ n → (∀ v, d v ≤ n - 1) → Graphical n d → ((∃ h : (∃ t : Nat, MixedAt n d t), mixingTime n d h ≤ 2 * n ^ 8) ∧ (stateCount n d = 1 → (MixedAt n d 0 ∧ ∀ h : (∃ t : Nat, MixedAt n d t), mixingTime n d h = 0)) ∧ (1 < stateCount n d → hasSpectralGapAtLeast n d ((1 : ℝ) / (24 * (n : ℝ) ^ 2 * (Nat.choose n 4 : ℝ))))) := by
  sorry
theorem switch_chain_tv_bound :
    ∀ (n : Nat) (d : Fin n → Nat), 4 ≤ n → (∀ v, d v ≤ n - 1) → Graphical n d → 1 < stateCount n d → ∀ (t : Nat) (G : GraphState n d), tvDistanceFrom n d t G ≤ Real.sqrt (stateCount n d : ℝ) / 2 * Real.exp (- (t : ℝ) / (24 * (n : ℝ) ^ 2 * (Nat.choose n 4 : ℝ))) := by
  sorry
theorem switch_connectivity :
    ∀ (n : Nat) (d : Fin n → Nat), 4 ≤ n → (∀ v, d v ≤ n - 1) → Graphical n d → ∀ G H : GraphState n d, Relation.ReflTransGen (SwitchStep n d) G H := by
  sorry
end Problem315
end
DEFS(28): def graphDegree, def Realizes, abbrev GraphState, def Graphical, abbrev FourSet, def IsPerfectMatchingOn, abbrev PerfectMatching, abbrev SwitchProposal, def removedMatching, def addedMatching, def validSwitch, def replaceEdges, def proposalResult, def allGraphStates, def allProposals, def stateCount, def switchKernel, def kernelPow, def uniformAverage, def uniformInner, def uniformVariance, def markovApply, def dirichletEnergy, def hasSpectralGapAtLeast, def tvDistanceFrom, def MixedAt, def mixingTime, def SwitchStep
## PAPER Polynomial-Mixing-of-the-Switch-Chain-for-Every-Graphical-Degree-Sequence-September-25-2026
ABSTRACT: We prove the simple-undirected form of the Kannan--Tetali--Vempala conjecture: the switch chain on simple undirected graphs mixes in polynomial time for every graphical degree sequence. For a lazy chain that proposes switches uniformly on four vertices, the total-variation mixing time at distance $1/4$ is at most $2n^8$. We also give an exactly uniform sampler for every graphical labeled degree vector. It uses unbiased random bits, terminates almost surely, and has expected polynomial bit running time.
[theorem] \label{thm:main} For every $n\ge4$ and every graphical degree vector $d$, \[ t_{\mathrm{mix}}(d)\le 2n^8. \] If $|\Omega_d|>1$, the spectral gap of $P_d$ is at least $[24n^2\binom n4]^{-1}$.
==================
# FAMILY 132: A superquadratic separation of sensitivity and block sensitivity
SCOPE: The formalized result disproves a universal quadratic bound of block sensitivity by sensitivity for total Boolean functions. For every integer $d\ge1$, it constructs a nonconstant function with $\mathrm{bs}(f)/s(f)^2\ge2^d/(4(d+2)^2)$, making the ratio unbounded. The formalization also gives a fixed exponent $\alpha>2$ and a sequence with $s(f)^\alpha\le\mathrm{bs}(f,0)$ while the latter tends to infinity; here $\mathrm{bs}(f,0)$ is block sensitivity at the all-zero input.
## CHALLENGE SensitivitySeparation  targets=['OAI.Paper320.quantitative_separation'] defs=[]
theorem quantitative_separation (d : ℕ) (hd : 1 ≤ d) :
    ∃ (n : ℕ) (f : (Fin n → Bool) → Bool),
      0 < n ∧ f (fun _ => false) = false ∧
      (∃ x y : Fin n → Bool, f x ≠ f y) ∧
      (2 : ℝ) ^ d / (4 * ((d : ℝ) + 2) ^ 2) ≤
        (blockSensitivity f : ℝ) / (sensitivity f : ℝ) ^ 2 := by
  sorry
end Paper320
end
DEFS(5): def flip, def sensitivityAt, def sensitivity, def blockSensitivityAt, def blockSensitivity
## PAPER A-superquadratic-separation-between-sensitivity-and-block-sensitivity-September-25-2026
ABSTRACT: We disprove the quadratic strengthening of the Sensitivity Conjecture by constructing nonconstant total Boolean functions whose block sensitivity grows faster than any constant multiple of sensitivity squared. In fact, for some fixed \(\alpha>2\), our examples have unbounded block sensitivity and satisfy \(\bs(f)\ge s(f)^\alpha\).
[theorem] \label{thm:main} For every real \(C>0\), there are a positive integer \(n\) and a nonconstant total Boolean function \(f:\{0,1\}^n\to\{0,1\}\) such that \[ \bs(f)>C\,s(f)^2. \] More precisely, for every integer \(d\ge1\) the construction below gives a nonconstant total Boolean function \(f\) with \[ \frac{\bs(f)}{s(f)^2}\ge \frac{2^d}{4(d+2)^2}. \]
==================
# FAMILY 133: The computational complexity of Weisfeiler–Leman refinement
SCOPE: The formalization gives the paper's parity-lift graph construction for every Weisfeiler–Leman dimension $k\ge4$, under both joint and separate conventions. From a finite choice system it constructs two equal-size uncolored graphs that are Weisfeiler–Leman equivalent exactly when the system has no successful compatible choice. The same equivalence holds for the pure variant. A successful choice is detected by the specified early round: round two in the joint convention and round one in the separate convention. The graph-size bound is linear in the choice-system size with a factor depending on $k$. The paper's conditional running-time exclusions are outside these selected construction statements. The formalization proves that deciding whether Weisfeiler–Leman refinement of a supplied dimension identifies a graph is EXPTIME-complete under polynomial-time many-one reductions. The input is a 
## CHALLENGE ParityLifts  targets=['OAI.ParityWL.parity_reduction'] defs=None
theorem parity_reduction : ParityReductionStatement := by
  sorry
end ParityWL
DEFS(37): abbrev Bit, abbrev MainPair, abbrev Helper, abbrev TemplateVertex, structure ChoiceSystem, def ChoiceSystem.Successful, def ChoiceSystem.SizeAtMost, def helperIncident, def templateAdj, def template, abbrev BaseVertex, def baseType, inductive BaseArc, def baseGraph, def baseProjection, def Tag, instance tagFintype, abbrev LiftVertex, def liftGraph, def starParity, def zeroLift, def starLift, inductive Convention, def bagParameter, def detectionRound, def orderFactor, abbrev AtomicType, def JointColor, def SeparateColor, def atomicType
## CHALLENGE WLIdentification  targets=['OAI.WLIdentification.main'] defs=[]
theorem main : EXPTIMEComplete dimensionLanguage :=
  by
    sorry
end WLIdentification
DEFS(32): structure Graph, def Isomorphic, def NeighborColor, def neighborColor, def neighborHistogram, def TupleColor, def tupleColor, def tupleHistogram, def Equivalent, def Identifies, def WLdim, abbrev Word, abbrev BinaryLanguage, def binaryValue, def matrixWord, def inputWord, def dimensionLanguage, inductive Move, def Move.displacement, structure Machine, structure Configuration, def inputSymbol, def initial, def Halted, def step, def run, def Output, def DecidesWithin, def InEXPTIME, def ComputesWithin
## CHALLENGE WeisfeilerLeman  targets=['OAI.WLTime.unconditional_time_lower_bound'] defs=[]
DEFS(51): inductive Convention, def Graph, def adj, def diameterTwo, abbrev AtomicColor, def Color, def tupleColor, def histogram, def Equivalent, def encodeNat, def matrixBits, def encodePair, inductive Move, def Move.displacement, structure TM, structure Config, def symbol, def initial, def halted, def step, def run, def halts, def time, def accepts, def outputs, abbrev Word, def wordBits, def registerBits, structure WordOperation, inductive RAMInstruction
## CHALLENGE VariableWL  targets=['OAI.VariableWL.main'] defs=[]
theorem main : EXPTIMEComplete WL ∧ EXPTIMEComplete SubWL := by
  sorry
end VariableWL
DEFS(27): abbrev Word, inductive Motion, def Motion.displacement, structure Machine, structure Configuration, def wordCells, def initial, def scanned, def step, def run, def OutputsWithin, abbrev Language, def InEXPTIME, def PolytimeReduces, def EXPTIMEComplete, structure Graph, abbrev Tuple, def Color, def color, def histogram, def Equivalent, def integerCode, def graphCode, def pairCode, def WL, def Subcubic, def SubWL
## PAPER Parity-lifts-and-bounded-treewidth-witnesses-for-Weisfeiler-Leman-equivalence-September-25-2026
ABSTRACT: For \(k\ge4\), we construct two uncolored graphs that are \(k\)-dimensional Weisfeiler--Leman equivalent exactly when a prescribed finite-domain choice system has no compatible choice. The system has \(k+1\) domains for joint refinement and \(k\) for separate-coordinate refinement. A successful choice is detected after two joint rounds or one separate round. Applied to sparse satisfiability, the reduction gives fixed-dimension \(n^{\Omega(k)}\) time exclusions under positive-rate ETH, even for deciding equality of these early histograms.
[theorem[Parity reduction]] \label{thm:choice-reduction} Fix \(k\ge4\), either refinement convention, and the corresponding \(t\) in \eqref{eq:bag-parameter}. From every choice system on \(t\) domains one can explicitly construct two uncolored simple graphs \(X_0,X_\star\) of equal order such that \[ X_0\equiv_k X_\star \quad\Longleftrightarrow\quad \text{the choice system has no successful choice}. \] The assertion holds both with common color names on separate graphs and with pure-tuple comparison in their disjoint union. If every domain and label set has size at most \(A\), where \(A\ge1\), their common order is at most \(A M_t\), where \[ M_t=t\,2^{\,t-2+3\binom{t-1}{2}}+12\binom t3. \] When a successful choice exi
## PAPER The-complexity-of-identifying-a-graph-by-Weisfeiler-Leman-refinement-September-25-2026
ABSTRACT: We prove that deciding whether Weisfeiler--Leman refinement of an input dimension identifies a given graph is EXPTIME-complete. The input is a nonempty finite simple uncolored graph in adjacency-matrix form and a positive binary-encoded dimension. Identification quantifies over every comparison graph.
[theorem] \label{thm:main} The following problem is EXPTIME-complete under deterministic polynomial-time many-one reductions: given a nonempty finite simple undirected uncolored graph $G$ by its adjacency matrix and a positive integer $k$ in binary, decide whether $\WLdim(G)\le k$. Here dimension one uses ordinary neighbor color refinement, and dimensions at least two use the joint-update rule described above.
## PAPER Unconditional-time-lower-bounds-for-Weisfeiler-Leman-equivalence-September-25-2026
ABSTRACT: For every sufficiently large fixed $k$, deciding whether two $n$-vertex graphs are $k$-Weisfeiler--Leman equivalent requires $n^{\Omega(k)}$ deterministic sequential time in the worst case. The bound holds at every sufficiently large graph order, even for simple connected uncolored graphs of diameter at most two, without a complexity assumption. Inputs are explicit adjacency matrices; the models are multitape Turing machines and sequential logarithmic-word RAMs with fixed polynomial-bit-time instructions. Both joint and separate replacement conventions are covered.
[theorem] \label{thm:main} There are absolute constants $c>0$ and $k_0$ with the following property. For every fixed integer $k\ge k_0$ and every correct deterministic decider $A$ for $k$-Weisfeiler--Leman equivalence, there is an integer $n_0=n_0(A,k)$ such that \[ T_A(n)\ge n^{ck} \qquad\text{for every integer }n\ge n_0. \] This holds for multitape Turing machines and for sequential random-access machines with $O(\log(n+2))$-bit addresses and words, boundedly many memory accesses per instruction, and fixed instructions computable in time polynomial in the word length. The same bound holds if $A$ is required to decide correctly only on pairs of simple connected uncolored graphs of diameter at most tw
## PAPER Variable-dimension-Weisfeiler-Leman-equivalence-on-general-and-subcubic-graphs-September-25-2026
ABSTRACT: Deciding joint-update \(k\)-dimensional Weisfeiler--Leman equivalence is \(\EXPTIME\)-complete when the two graphs are given by explicit adjacency matrices and \(k\ge2\) is encoded in binary. The result holds even for connected simple uncolored graphs of equal positive order and maximum degree at most three.
[theorem] \label{thm:main} Both \(\WL\) and \(\SubWL\) are \(\EXPTIME\)-complete under deterministic polynomial-time many-one reductions.
==================
# FAMILY 134: Generalized star height at most three
SCOPE: Generalized star height measures the nesting of Kleene stars in regular expressions that also allow Boolean operations. The formalization proves that every regular language over a finite alphabet has a generalized expression over the same alphabet of star height at most three. This is stronger than the bound of thirteen in the accompanying finite-monoid paper. The selected statement asserts the uniform expression bound, without separately encoding every construction step of that paper. The formalization proves that every regular language over a finite alphabet has a generalized regular expression over that same alphabet with star height at most three. Generalized expressions allow Boolean operations as well as concatenation and Kleene star. The bound of three implies the accompanying paper's bound of four; the selected statement concerns the expression bound itself. Generalized star heig
## CHALLENGE GeneralizedStarHeight  targets=['OAI.GeneralizedStarHeight.main'] defs=[]
theorem main {Alphabet : Type u} [Finite Alphabet] (L : Language Alphabet) (hL : L.IsRegular) :
    HasHeightAtMost L 3 := by
  sorry
end GeneralizedStarHeight
DEFS(4): inductive Expression, def language, def height, def HasHeightAtMost
## CHALLENGE GeneralizedStarHeight  targets=['OAI.GeneralizedStarHeight.main'] defs=[]
theorem main {Alphabet : Type u} [Finite Alphabet] (L : Language Alphabet) (hL : L.IsRegular) :
    HasHeightAtMost L 3 := by
  sorry
end GeneralizedStarHeight
DEFS(4): inductive Expression, def language, def height, def HasHeightAtMost
## PAPER Finite-Monoid-Computations-and-a-Uniform-Generalized-Star-Height-Bound-September-25-2026
ABSTRACT: Every regular language over a finite alphabet has a generalized regular expression of star height at most thirteen over that same alphabet. We prove this uniform bound by representing finite monoid computations as affine updates and recovering them through twelve successive split constructions.
[theorem] \label{thm:main} For every finite alphabet \(\Sigma\) and every regular language \(L\subseteq\Sigma^*\), \[ h_\Sigma(L)\le 13. \]
## PAPER Generalized-Star-Height-at-Most-Four-September-25-2026
ABSTRACT: Every regular language over a finite alphabet has generalized star height at most four over that same alphabet. We give a complete construction using an affine correction that hides one interval product, a finite clock, and several scales for moving boundaries through periodic words.
[theorem] \label{thm:main} For every finite alphabet $\Sigma$ and every regular language $L\subseteq\Sigma^*$, one has $h_\Sigma(L)\le4$.
## PAPER Generalized-Star-Height-at-Most-Three-September-25-2026
ABSTRACT: Every regular language over a finite alphabet has generalized star height at most three, with complement taken in the same free monoid. We express finite-monoid computations using a prefix code of word pieces.
[theorem] \label{thm:main} For every finite alphabet $\Sigma$ and every regular language $L\subseteq\Sigma^*$, \[ h_\Sigma(L)\le3. \]
==================
# FAMILY 135: Homogeneous depth-five lower bounds for iterated matrix multiplication
SCOPE: Let $\mathrm{IMM}_{n,n}$ be the $(1,1)$ entry of the product of $n$ independent $n\times n$ variable matrices. The formalization proves that, over every characteristic-zero field, syntactically homogeneous depth-five $\Sigma\Pi\Sigma\Pi\Sigma$ circuits computing this polynomial require at least $n^{\sqrt n/400}$ gates for all sufficiently large $n$, with a threshold independent of the field. Arbitrary bottom support, finite fan-in and fan-out, and sharing are allowed. It also gives, over every field and for $n\ge2$, circuits with at most $n^{\sqrt n+4}$ gates. These are the lower and upper bounds selected from the paper.
## CHALLENGE DepthFive  targets=['OAI.Problem335.main'] defs=[]
theorem main :
    (∃ threshold : ℕ, ∀ size : ℕ, threshold ≤ size →
      ∀ circuit : Depth5Circuit ℂ size, circuitValue circuit = imm ℂ size →
        (size : ℝ) ^ (Real.sqrt (size : ℝ) / 400) ≤ (circuitSize circuit : ℝ)) ∧
    (∃ threshold : ℕ, ∀ (FieldType : Type u) [Field FieldType] [CharZero FieldType],
      ∀ size : ℕ, threshold ≤ size → ∀ circuit : Depth5Circuit FieldType size,
        circuitValue circuit = imm FieldType size →
          (size : ℝ) ^ (Real.sqrt (size : ℝ) / 400) ≤ (circuitSize circuit : ℝ)) ∧
    (∀ (FieldType : Type u) [Field FieldType] (size : ℕ), 2 ≤ size →
      ∃ circuit : Depth5Circuit FieldType size, circuitValue circuit = imm FieldType size ∧
        circuitSize circuit ≤ upperGateBound size ∧
        (upperGateBound size : ℝ) ≤ (size : ℝ) ^ (Real.sqrt (size : ℝ) + 4)) := by
  sorry
end Problem335
end
DEFS(15): inductive D5Leaf, def d5LeafDegree, structure Depth5Circuit, def d5LeafValue, def bottomValue, def lowerValue, def middleValue, def upperValue, def circuitValue, def circuitSize, def immLayer, def imm, def ceilSqrt, def ceilDiv, def upperGateBound
## PAPER Homogeneous-depth-five-lower-bounds-for-iterated-matrix-multiplication-September-25-2026
ABSTRACT: Let $\IMM_{n,n}$ be the $(1,1)$ entry of a product of $n$ independent $n\times n$ matrices of variables. Over every field of characteristic zero, every syntactically homogeneous $\Sigma\Pi\Sigma\Pi\Sigma$ circuit computing $\IMM_{n,n}$ has at least $n^{\sqrt n/400}$ gates for all sufficiently large $n$, with an absolute threshold independent of the field. Bottom linear forms may have arbitrary support, and arbitrary finite fan-in, fan-out, and gate sharing are allowed. Over every field, a block expansion gives such circuits with at most $n^{\sqrt n+4}$ gates for $n\geq2$. Thus the gate complexity over characteristic-zero fields is $n^{\Theta(\sqrt n)}$.
[theorem] \label{thm:main} There exist absolute constants $c>0$ and $n_0$ such that, for every integer $n\geq n_0$, every syntactically homogeneous $\Sigma\Pi\Sigma\Pi\Sigma$ circuit over $\C$ computing $\IMM_{n,n}$ has size at least \[ n^{c\sqrt n}. \] One may take $c=1/400$.
==================
# FAMILY 137: One-tape time simulation in two-fifths-power space
SCOPE: The formalization gives two-fifths-power space simulation of a fixed deterministic machine with one writable tape and finitely many read-only input heads. Heads move at most one cell per step, initial contents are independent of the time bound, and contents and input symbols must be accessible in polylogarithmic space. Given a binary time cap $T\ge2$, the simulator returns the source's finite-control outcome and halting flag using $O(T^{2/5}(\log(T+2))^C)$ space. A second simulator needs no time cap: on an input that halts at time $t$, it returns the halted outcome using $O((t+2)^{2/5}(\log(t+2))^C)$ space. Simulation time is unrestricted. General multitape simulation, hierarchy consequences, and bounded-space-halting results are outside these selected statements.
## CHALLENGE OneTapeSpace  targets=['OAI.Fifths.Single.capped', 'OAI.Fifths.Single.unknown'] defs=[]
theorem capped [Fintype X] (A : M.Sym) (p q : ℝ) (hp : 1 ≤ p) (_hq : 1 ≤ q) :
    ∃ (N : TM X Unit M.Outcome) (e : ℕ) (c : ℝ), 0 < c ∧
      ∀ (x : List X) (T : ℕ), 2 ≤ T → M.Access A p q x T →
        ∃ b : ℕ, N.Within (binaryIn x (fun _ => T)) (M.outcome x T) b ∧
          (b:ℝ) ≤ c*(T:ℝ)^exponent*(Log T)^e := by
  sorry
theorem unknown [Fintype X] (A : M.Sym) (p q : ℝ) (hp : 1 ≤ p) (_hq : 1 ≤ q) :
    ∃ (N : TM X Empty M.Outcome) (e : ℕ) (c : ℝ), 0 < c ∧
      ∀ (x : List X), (∀ T, 2 ≤ T → M.Access A p q x T) →
        ∀ (t : ℕ), (M.outcome x t).2 = true →
          ∃ b, N.Within (files x) (M.outcome x t) b ∧
            (b:ℝ) ≤ c*((t:ℝ)+2)^exponent*(Log t)^e := by
  sorry
end Fifths.Single
DEFS(49): inductive Dir, def delta, inductive Mark, def see, def walk, inductive Runs, structure Inputs, structure Readers, structure Reads, structure Advances, def home, def see, def walk, structure Tape, structure WriteMove, def init, def see, def perform, structure TAction, structure TM, structure Cfg, def initial, def step, structure Window, def width, def ok, def bits, def Within, structure SingleAct, structure Single
## PAPER Simulating-One-Tape-Time-in-Two-Fifths-Power-Space-September-25-2026
ABSTRACT: We show that a fixed deterministic Turing machine with one writable tape and head can be simulated in \(O(T^{2/5}\polylog(T+2))\) work-space bits when a binary time cap \(T\ge2\) is supplied. The simulator computes the finite-control and halting outcome by time \(T\); its running time is unrestricted. The result allows a fixed number of read-only input heads and requires a fixed accessor that supplies every initial writable and read-only symbol within distance \(T\) of the relevant head origin in polylogarithmic space. This improves the square-root space exponent for one-tape machines, answering Williams's question for this model.
[theorem] \label{thm:main} Fix a deterministic machine with one writable tape and head, a fixed number of read-only input heads, unit movement and fixed origins for all heads, cap-independent symbol functions, and a fixed accessor as above. For every public input \(x\) and supplied binary cap \(T\ge2\) for which the access condition holds, its finite-control and halting outcome by time \(T\) can be computed deterministically in \(\softO(T^{2/5})\) work-space bits, excluding storage for the read-only input. Simulation time is unrestricted, and the final writable tape need not be materialized. If the access condition holds for \((x,T)\) at every \(T\ge2\), and the machine halts on \(x\) after \(t\) step
==================
# FAMILY 139: Subpolynomial query complexity for log-concave sampling
SCOPE: The formalized result determines the dimension exponent of exact value-and-gradient query complexity for well-conditioned log-concave sampling. For potentials with $V(0)=0$, $\nabla V(0)=0$, and $I\le\nabla^2V\le2I$, the least worst-case query budget achieving total-variation error at most $1/10$ is at most $C_\varepsilon d^\varepsilon$ for every $\varepsilon>0$, and at least $c\log d$ eventually. Hence the infimal polynomial exponent is zero. Algorithms may be measurable, randomized, and adaptive; arithmetic and bit costs are not bounded.
## CHALLENGE LogConcaveQuery  targets=['OAI.LogConcaveSampling.exact_source_main'] defs=[]
theorem exact_source_main :
    (∀ ε : ℝ, 0 < ε → ∃ C : ℝ, ∀ d : ℕ, 2 ≤ d →
      (queryComplexity d).toENNReal ≤ ENNReal.ofReal (C * (d : ℝ) ^ ε)) ∧
    (∃ c : ℝ, 0 < c ∧ ∃ d₀ : ℕ, 2 ≤ d₀ ∧ ∀ d : ℕ, d₀ ≤ d →
      ENNReal.ofReal (c * Real.log (d : ℝ)) ≤ (queryComplexity d).toENNReal) ∧
    gammaStar = 0 := by
  sorry
end LogConcaveSampling
end
DEFS(16): abbrev Point, abbrev Reply, abbrev Transcript, structure Admissible, def gibbsDensity, def partition, def gibbs, def TVAtMost, def firstOrderReply, structure OracleAlgorithm, def OracleAlgorithm.history, def OracleAlgorithm.run, def CanSample, def queryComplexity, def ExponentBound, def gammaStar
## PAPER Subpolynomial-query-complexity-for-well-conditioned-log-concave-sampling-September-26-2026
ABSTRACT: For every fixed $\varepsilon>0$, we give a sampling algorithm using at most $C_\varepsilon d^\varepsilon$ exact first-order queries on every execution for $C^2$ potentials on $\R^d$ with a known minimizer and Hessian between $I_d$ and $2I_d$. The output has total-variation distance at most $1/10$ from the target Gibbs law. Computation between queries is unrestricted. We also prove an $\Omega(\log d)$ query lower bound for arbitrary randomized adaptive algorithms, determining the optimal dimension exponent to be zero.
[theorem] \label{thm:main} In the oracle model above, for every \(\varepsilon>0\) there is \(C_\varepsilon<\infty\) such that \[ Q(d)\le C_\varepsilon d^\varepsilon \qquad(d\ge2). \] There are also absolute constants \(c>0\) and \(d_0\) such that \[ Q(d)\ge c\log d\qquad(d\ge d_0). \] The lower bound applies to arbitrary randomized adaptive first-order algorithms. In particular, \(\gamma_*=0\).
==================
# FAMILY 140: Memory–sample lower bounds for noiseless Gaussian regression
SCOPE: In noiseless Gaussian regression, a learner observes inner products of an unknown unit vector in $\mathbb R^d$ with independent standard Gaussian vectors. The formalization proves that, for every fixed $A>0$, there is $c_A>0$ such that, in sufficiently large dimension, a learner retaining at most $Ad^2$ bits between observations needs at least $c_A d\log(1/\varepsilon)$ observations to attain angular error at most $\varepsilon$ with probability at least $2/3$ for a uniformly random unit signal, for $0<\varepsilon\le1/10$. For memory $o(d^2)$, the constant can be universal, and the selected statement also permits success at least $2/3$ separately for every signal. The linked supporting results include inverse Gram-matrix moments, exact-projection densities, regularization bounds, and sphere- and cube-prior block estimates. The paper studies how posterior replicas—independent signals drawn
## CHALLENGE MemoryPrecision  targets=['OAI.MemoryPrecision.main'] defs=[]
theorem main :
  AmbientGramStatement ∧
  FiniteDensityStatement ∧
  MeasurableTestStatement ∧
  JointL1Statement ∧
  PointwiseDensityStatement ∧
  CoefficientStepStatement ∧
  Kernel.SourceEllipsoidStatement.{u} ∧
  CubeBlockStatement ∧
  (∃ D : ℝ, Real.exp 1 ≤ D ∧ ∃ d₀ : ℕ, ∃ hd₀ : 16 ≤ d₀, ∃ c : ℝ, 0 < c ∧
    ∀ d M T : ℕ, ∀ hd : d₀ ≤ d, M ≤ d^2 → ∀ ε : ℝ, 0 < ε → ε ≤ 1/10 →
    ∀ (Ω : Type u) [MeasurableSpace Ω] (ρ : Measure Ω), IsProbabilityMeasure ρ →
    ∀ K : Ω → MemoryPrecision.Kernel.Policy d M T,
      MemoryPrecision.Kernel.Policy.ModelAdmissible.{u} K ρ →
      MemoryPrecision.Kernel.Policy.Success K ρ
        (MemoryPrecision.Kernel.CubePrior (MemoryPrecision.Kernel.cubePrior_dimension hd₀ hd)) ε ≤
          min 1 (ENNReal.ofReal
            (D^((d/2)*(MemoryPrecision.Kernel.BlockCount T ((d/2)/4)+1)) * ε^((d/2:ℕ)/4:ℝ))) ∧
      ((∀ signal : MemoryPrecision.Kernel.Sphere d,
        (@OfNat.ofNat ℝ≥0∞ 2
          (@instOfNatAtLeastTwo ℝ≥0∞ 2 ENNReal.instAddCommMonoidWithOne.toNatCast inferInstance)) /
        (@OfNat.ofNat ℝ≥0∞ 3
          (@instOfNatAtLeastTwo ℝ≥0∞ 3 ENNReal.instAddCommMonoidWithOne.toNatCast inferInstance)) ≤
          (∫⁻ observation,
            MemoryPrecision.Kernel.Policy.experiment K
              (MemoryPrecision.Kernel.Policy.angleTest ε) (signal, observation)
            ∂ρ.prod (MemoryPrecision.Kernel.RowLaw d T))) →
        c*(d:ℝ)*Real.log (1/ε) ≤ (T:ℝ))) ∧
  (∃ C : ℝ, 0 < C ∧ ∃ d₀ : ℕ, 0 < d₀ ∧
    ∀ d M T : ℕ, d₀ ≤ d → ∀ ε : ℝ, 0 < ε → ε ≤ 1/10 →
    ∀ (Ω : Type u) [MeasurableSpace Ω] (ρ : Measure Ω), IsProbabilityMeasure ρ →
    ∀ L : Ω → MemoryPrecision.Kernel.Policy d M T,
      MemoryPrecision.Kernel.Policy.Admissible L ρ (MemoryPrecision.Kernel.UniformSphere d) →
      MemoryPrecision.Kernel.Policy.Success L ρ (MemoryPr
DEFS(77): abbrev Vector, abbrev Sphere, abbrev State, abbrev Action, abbrev Observations, abbrev Rows, def UniformSphere, def RowLaw, def ObservationReference, structure Policy, def Completed, def eval, def pathValue, def records, def outputTest, def angleTest, def chordTest, def experiment, structure Admissible, def Success, def ChordSuccess, abbrev Vector, abbrev UnitSphere, abbrev Space, def J, def AmbientBallBound, def InverseGram, def MatrixLabelReference, def ProjectionLaw, def ProjectedEllipsoid
## CHALLENGE NoiselessRegression  targets=['OAI.NoiselessRegression.main'] defs=[]
theorem main : SubquadraticMemory.{u} ∧ FixedQuadraticMemory.{u} := by
  sorry
end NoiselessRegression
end
DEFS(19): abbrev Vector, abbrev UnitSphere, abbrev State, abbrev Samples, def uniformSphere, def sampleLaw, def observationReference, structure Learner, abbrev RunStatus, def start, def run, def terminal, def estimate, structure Admissible, def angularError, def success, def uniformSuccess, def SubquadraticMemory, def FixedQuadraticMemory
## CHALLENGE PosteriorReplicas  targets=['OAI.PosteriorReplicas.source_main'] defs=[]
theorem source_main : EqualLabelMeasureIdentity ∧ EqualLabelVersions ∧
    GaussianReplicaBlock ∧ DistanceReplicaBlock ∧ HaarReplicaBlock ∧
    SyntheticReplicaBlock ∧ IncidenceReplicaBlock ∧
    PosteriorRegression.KernelSubquadraticMemory.{u} := by
  sorry
end PosteriorReplicas
DEFS(69): abbrev Vec, abbrev Rows, abbrev Labels, abbrev Data, abbrev Tuple, def sphereLaw, def gaussianRows, def labels, lemma measurable_labels, def messageKernel, def signalMessageLaw, def sideLaw, def messageEntropy, def conditionalInformation, def GaussianReplicaBlock, inductive BaseLaw, def BaseLaw.measure, def rowGram, def liftLabel, def kernelComponent, def baseFiber, def baseDensity, def tiltMass, def projectedDensity, def tiltedFiber, def differences, def differenceSpan, def affineVolume, def constrainedRows, def equalLabelLeft
## CHALLENGE GaussianFiniteEntropy  targets=['OAI.RepeatedLocalization.FiniteEntropy.finite_expected_regularization'] defs=[]
theorem finite_expected_regularization : FiniteEntropyStatement := by
  sorry
end FiniteEntropy
end RepeatedLocalization
DEFS(50): abbrev Coordinate, abbrev GaussianBlock, abbrev Label, abbrev History, abbrev Cell, instance cellMeasurableSpace, def initialCube, def cubePrior, def chart, def cellSet, def rootCell, def gaussianBlockLaw, def exactLabel, structure BlockRule, abbrev Rules, def past, def through, def blockProbability, def historyLikelihood, def experimentLaw, abbrev Disclosure, def ValidDisclosure, def transcriptMap, def augmentedLaw, def mutualInformation, def finalLevel, def MainStatement, def uniformCell, def Descendant, def threshold
## CHALLENGE GaussianInformation  targets=['OAI.RepeatedLocalization.repeated_localization', 'OAI.AllScaleInverseVolume.inverse_volume_without_support', 'OAI.KernelPotential.kernel_coercivity', 'OAI.KernelPotential.actual_row_drift'] defs=[]
theorem repeated_localization : MainStatement := by
  sorry
end RepeatedLocalization
open MeasureTheory Metric
open scoped ENNReal
namespace AllScaleInverseVolume
local instance namedAtLeastTwoTwo : Nat.AtLeastTwo 2 := ⟨Nat.le_refl 2⟩
theorem inverse_volume_without_support : InverseVolumeStatement := by
  sorry
end AllScaleInverseVolume
open MeasureTheory ProbabilityTheory Metric Set
open scoped ENNReal
namespace KernelPotential
local instance namedAtLeastTwoTwo : Nat.AtLeastTwo 2 := ⟨Nat.le_refl 2⟩
theorem kernel_coercivity : CoercivityStatement := by sorry
theorem actual_row_drift : DriftStatement := by sorry
end KernelPotential
DEFS(49): abbrev Coordinate, abbrev GaussianBlock, abbrev Label, abbrev History, abbrev Cell, instance cellMeasurableSpace, def initialCube, def cubePrior, def chart, def cellSet, def rootCell, def gaussianBlockLaw, def exactLabel, structure BlockRule, abbrev Rules, def past, def through, def blockProbability, def historyLikelihood, def experimentLaw, abbrev Disclosure, def ValidDisclosure, def transcriptMap, def augmentedLaw, def mutualInformation, def finalLevel, def MainStatement, abbrev Ambient, def gramVolume, def inverseVolume
## CHALLENGE ProjectionMoments  targets=['OAI.ProjectionMoments.main'] defs=[]
theorem main : MainStatement.{u} := by
  sorry
end ProjectionMoments
end
DEFS(90): abbrev Vector, abbrev UnitSphere, abbrev State, abbrev Samples, def uniformSphere, def sampleLaw, def observationReference, structure Learner, abbrev RunStatus, def start, def run, def terminal, def estimate, structure Admissible, def angularError, def uniformSuccess, def sphereLaw, def ambientSphereLaw, abbrev Learner.TaggedState, instance Learner.taggedMeasurableSpace, def Learner.taggedStart, structure Learner.MeasurableRules, structure FiniteKernelLearner, structure CompletedRules, def kernelRun, abbrev FiniteKernelLearner.Tape, def FiniteKernelLearner.destination, def FiniteKernelLearner.taggedKernel, def FiniteKernelLearner.terminalOutput, abbrev FiniteKernelLearner.Result
## CHALLENGE GaussianReplacement  targets=['OAI.CurrentProjection.mixedMomentMain', 'OAI.CurrentProjection.actualRowMain', 'OAI.CurrentProjection.actualRowRefinement', 'OAI.CurrentProjection.actualRowSourceMain', 'OAI.CurrentProjection.actualRowSourceRefinement', 'OAI.CurrentProjection.criticalComparisonMain', 'OAI.CurrentProjection.oneLevelComparisonMain', 'OAI.CurrentProjection.twoLabelComparisonMain', 'OAI.CurrentProjection.hybridBlockMain', 'OAI.CurrentProjection.fiberTwoPointMain', 'OAI.CurrentProjection.fiberBlockMain'] defs=[]
theorem mixedMomentMain : MixedMomentMain := by
  sorry
theorem actualRowMain {d m r q : ℕ} {W : Type*} [MeasurableSpace W]
    [Countable W] [MeasurableSingletonClass W]
    (hdim : AdmissibleDimensions d m r q)
    (P : Measure ((Sphere d×W)×Rows m d)) [IsProbabilityMeasure P]
    (ν : Measure (Sphere d)) [IsProbabilityMeasure ν]
    (hInd : (P.map swapLast).fst = ν.prod (gaussianRows m d))
    (H : ℝ) (hν : ν ≤ ENNReal.ofReal H • uniformSphere d)
    (hEntropy : shannonEntropy (P.map swapLast).snd ≠ ∞)
    (ρ : PositiveMessage (P.map swapLast).snd → Measure (Sphere d))
    [∀ w, IsFiniteMeasure (ρ w)]
    (_hρac : ∀ w, ρ w ≪ uniformSphere d)
    (B D : PositiveMessage (P.map swapLast).snd → ℝ)
    (hB : ∀ w, 0 < B w) (hD : ∀ w, 0 < D w)
    (hgB : ∀ w, LocalGrowth (ρ w) (m+r) (B w))
    (hgD : ∀ w, LocalGrowth (ρ w) (d-1) (D w))
    (hCI : Integrable (fun sw : Sphere d×W => Real.log (1+momentBound 9 d
      (completeFamily (P.map swapLast).snd B 1 sw.2) (completeFamily (P.map swapLast).snd D 1 sw.2))) P.fst) :
    ActualRowConclusion (r:=r) (q:=q) P (completeFamily (P.map swapLast).snd ρ 0)
      (completeFamily (P.map swapLast).snd B 1) (completeFamily (P.map swapLast).snd D 1) := by
  sorry
theorem actualRowRefinement {d m : ℕ} {W E : Type*} [MeasurableSpace W]
    [MeasurableSpace E] [Countable W] [MeasurableSingletonClass W]
    [Countable E] [MeasurableSingletonClass E]
    (P : Measure ((Sphere d×W)×Rows m d)) [IsProbabilityMeasure P]
    (e : Sphere d×W → E) (he : Measurable e)
    (_hEntropy : shannonEntropy
      ((P.map (fun p => ((p.1.1,(p.1.2,e p.1)),p.2))).map swapLast).snd ≠ ∞) :
    rowInformation (P.map (fun p => ((p.1.1,(p.1.2,e p.1)),p.2))) (gaussianRows m d) =
      rowInformation P (gaussianRows m d) := by
  sorry
theorem actualRowSourceMain {d m r q : ℕ} {W : Type*} [MeasurableSpace W]
    [Countable W] [MeasurableSingletonClass W]
    (hdim : AdmissibleDimensions d m r q)
    (P : Measure ((Sphere d×W)×Rows m d)) [IsProbabilityMeasure P]
    (ν : Measure (Sphere d)) [IsProbabilityMeasure ν]
    (hInd : (P.map swapLast).fst = ν.prod (gaussianRows m d))
    (H : ℝ) (hν : ν ≤ ENNReal.ofReal H • uniformSphere d)
    (hEntropy : shannonEntropy (P.map swapLast).snd ≠ ∞)
    (ρ : PositiveMessage (P.map swapLast).snd → Measure (Sphere d))
    [∀ w, IsFiniteMeasure (ρ w)]
    (_hρac : ∀ w, ρ w ≪ uniformSphere d)
    (B D : PositiveMessage (P.map swapLast).snd → ℝ)
    (hB : ∀ w, 0 < B w) (hD : ∀ w, 0 < D w)
    (hgB : ∀ w, LocalGrowth (ρ w) (m+r) (B w))
    (hgD : ∀ w, LocalGrowth (ρ w) (d-1) (D w))
    (hCI : Integrable (fun sw : Sphere d×W => Real.log (1+momentBound 9 d
      (completeFamily (P.map swapLast).snd B 1 sw.2) (completeFamily (P.map swapLast).snd D 1 sw.2))) P.fst) :
    ActualRowSourceConclusion (r:=r) (q:=q) P (completeFamily (P.map swapLast).snd ρ 0)
      (completeFamily (P.map swapLast).snd B 1) (completeFamily (P.map swapLast).snd D 1) := by
  sorry
theorem actualRowSourceRefinement {d m : ℕ} {W E : Type*} [MeasurableSpace W]
    [MeasurableSpace E] [Countable W] [MeasurableSingletonClass W]
    [Countable E] [MeasurableSingletonClass E]
    (P : Measure ((Sphere d×W)×Rows m d)) [IsProbabilityMeasure P]
    (ν : Measure (Sphere d)) [IsProbabilityMeasure ν]
    (hInd : (P.map swapLast).fst = ν.prod (gaussianRows m d))
    (e : Sphere d×W → E) (he : Measurable e)
    (hEntropy : shannonEntropy
      ((P.map (fun p => ((p.1.1,(p.1.2,e p.1)),p.2))).map swapLast).snd ≠ ∞) :
    actualConditionalRowInformation (P.map (fun p => ((p.1.1,(p.1.2,e p.1)),p.2))) =
      actualConditionalRowInformation P := by
  sorry
theorem criticalComparisonMain : CriticalComparisonMain := by
  sorry
theorem oneLevelComparisonMain : OneLevelComparisonMain := by
  sorry
theorem twoLabelComparisonMain : TwoLabelComparisonMain := by
  sorry
theorem hybridBlockMain : HybridBlockMain := by
  sorry
theorem fiberTwoPointMain : FiberTwoPointMain := by
  sorry
theorem fiberBlockMain : FiberBlockMain := by
  sorry
end CurrentProjection
end
DEFS(68): abbrev Vector, abbrev Sphere, abbrev Rows, def uniformSphere, def gaussianRows, def label, def LocalGrowth, def cubeAverage, def exactDensity, def AdmissibleDimensions, def momentConstant, def MixedMomentMain, instance gaussianRows_isProbabilityMeasure, lemma measurable_own_label, def swapLast, def rowInformation, def shannonEntropy, def conditionalMutualInformation, def actualExperiment, instance actualExperiment_isProbabilityMeasure, def actualObservation, instance actualObservation_isProbabilityMeasure, def selectedCube, def selectedExact, def momentBound, def logPositive, def logNegative, def extendedLogExpectation, def PositiveMessage, def completeFamily
## CHALLENGE SubsphereCurrent  targets=['OAI.SubsphereCurrent.full_current_main_scope'] defs=[]
theorem full_current_main_scope : CurrentMainScope.{u,v,w} := by
  sorry
end SubsphereCurrent
end
DEFS(61): abbrev Vector, abbrev UnitSphere, abbrev State, abbrev Samples, def uniformSphere, def sampleLaw, def observationReference, structure KernelLearner, abbrev RunStatus, def tagged, def run, def terminal, def estimateLaw, def angularError, def conditionalSuccess, def CompletedRules, structure SeededLearner, structure Admissible, def success, def uniformSuccess, def ExplicitPrecision, abbrev Vector, abbrev Sphere, def sphereLaw, structure Test, def Test.point, abbrev Vector, abbrev Sphere, abbrev Rows, abbrev Observation
## PAPER Memory-and-precision-in-noiseless-Gaussian-regression-September-27-2026
ABSTRACT: For every fixed \(A>0\), a learner that retains at most \(Ad^2\) bits between fresh exact Gaussian linear measurements needs \(\Omega_A(d\log(1/\epsilon))\) measurements to estimate a uniformly random unit vector to angular error at most \(\epsilon\), for any \(0<\epsilon\le 1/10\), with probability at least \(2/3\). The constant is absolute for \(o(d^2)\) memory.
[theorem[Memory and precision]] \label{h:main} For every fixed finite \(A>0\), there are constants \(c_A>0\) and \(d_A\) such that the following holds. Let \(d\ge d_A\), let \(0\le M\le Ad^2\) be an integer, and let \(0<\epsilon\le1/10\). For any learner in Definition~\ref{h:model}, draw \(S\sim\sigma_d\) independently of the rows and the learner's data-independent randomness. If \[ \Prob\{\arccos\ip{\widehat s}{S}\le\epsilon\}\ge\frac23, \] then its prescribed horizon satisfies \[ T\ge c_A\,d\log(1/\epsilon). \]
## PAPER Posterior-replicas-and-conditional-information-in-Gaussian-regression-September-27-2026
ABSTRACT: For a signal with density bounded by $L$ relative to uniform probability on $S^{d-1}$, we bound the information in a finite message $W$ formed from exact Gaussian measurements, conditional on an independent projection revealed only to the analyst. For explicit row counts proportional to $d$, the bound is $O(H(W)/d+d+\log(2+\log L))$. Consequently, a finite-state learner with $o(d^2)$ persistent bits and a deterministic sample horizon needs $\Omega(d\log(1/\epsilon))$ fresh noiseless Gaussian measurements for constant-probability angular accuracy $0<\epsilon\le1/10$ under the uniform spherical prior.
[theorem[Gaussian replica block bound]] \label{thm:gaussian-block} For all sufficiently large $d$, set \[ k=2\lfloor d/16\rfloor,\qquad m=k,\qquad t=m+1,\qquad \ell=4k. \] Suppose $p=f\sigma_d$ is a probability with $0\le f\le L<\infty$. In the block experiment above, let $A$ have $k$ rows and let $B$ have $\ell$ rows. There is an absolute constant $C$ such that \begin{equation}\label{eq:gaussian-block} I(S;W\mid B,BS) \le \frac{H(W)}{t}+Cd+C\log(2+\log L). \end{equation} The bound is uniform over the prior, the density bound $L$, and the message kernel. The labels used to produce $W$ are the exact values $AS$.
## PAPER Localization-costs-and-information-growth-for-exact-Gaussian-observations-September-27-2026
ABSTRACT: For the image of a uniform cube under a spherical coordinate map, we prove that finite messages from \(t\) blocks of \(\Theta(d)\) exact Gaussian measurements reveal only \(O_A(dt)\) information when each message has at most \(\exp(Ad^2)\) values, for fixed \(A\). The same bound holds when each message is supplemented with a nested cell that restores the required geometric spread.
[theorem[Repeated localization]] \label{ld:thm:main} There is an absolute constant $c>0$ with the following property. For any fixed $C_0>0$, consider the experiment above with $t\ge0$ blocks and $N\ge1$ possible message values, and suppose \begin{equation}\label{ld:eq:alphabet} \bigl(2/m+e^{-ck}\bigr)\log N\le C_0d. \end{equation} One can reveal nested dyadic cells $Q_0\supset Q_1\supset\cdots\supset Q_t$ containing $Z$, where $Q_i$ is a finite-valued measurable function of $Z$, the preceding revelations, and $W_1,\ldots,W_i$, so that the augmented transcript \[ \Pi_t=(W_1,Q_1,\ldots,W_t,Q_t) \] satisfies \begin{equation}\label{ld:eq:main} I(Z;\Pi_t)\le Cdt. \end{equation} Here $C$ is a constant depending only on $C_0$. If 
## PAPER Projection-moments-positive-cap-domination-and-Riesz-estimates-on-the-sphere-September-27-2026
ABSTRACT: We prove moment estimates for exact random projections of finite measures whose mass is controlled on Euclidean balls, and derive positive domination by countable sums of spherical cap measures. For learners with \(M=o(d^2)\) bits of memory, these estimates give three proofs that uniform-sphere average success at least \(2/3\) at angular accuracy \(0<\epsilon\le1/10\) requires \(\Omega(d\log(1/\epsilon))\) noiseless Gaussian observations. The three proofs keep their different stopping and accuracy costs explicit.
[theorem[Finite-memory precision bound]] \label{p:regression} Let \(M(d)=o(d^2)\) be a sequence of nonnegative integers and let \(0<\epsilon(d)\le1/10\). There is an absolute \(c>0\) such that, for all sufficiently large \(d\), every learner in the experiment above whose uniform-sphere average success satisfies \[ \Prob\{\arccos\inner{\widehat S}{S}\le\epsilon(d)\}\ge\frac23 \] must use \[ T(d)\ge c\,d\log\frac1{\epsilon(d)}. \] The dimension threshold may depend on the memory sequence. In particular, the conclusion holds when the same success probability is required separately for every \(s\in S^{d-1}\).
## PAPER Replacing-Gaussian-observations-in-memory-constrained-inference-September-27-2026
ABSTRACT: Replacing the Gaussian rows used to select a finite message by independent rows increases the remaining conditional information by at most \(Cd\), for a uniform spherical signal, message entropy at most \(d^2\), and the specified row dimensions proportional to \(d\). As an application, we prove that learners with \(M=o(d^2)\) persistent bits need \(T=\Omega(d\log(1/\epsilon))\) exact observations to attain uniform-sphere angular success at least \(3/5\), for \(0<\epsilon\le1/10\) and a deterministic finite horizon.
[proposition[The information identity and its density bound]] \label{prop:r-information-comparison} In the two experiments just defined, all quantities below are finite, and \begin{align} J_0(W)-J_1(W) &=h_0(Y\mid G,W)-h_1(Y\mid G,W)-I_1(S;G\mid W) \label{eq:r-information-identity}\\ &\le h_0(Y\mid G,W)+\E_1\log p_{\nu_W}(G,Y). \label{eq:r-information-density-bound} \end{align} If \(E=E(S,W)\) is countable and \(H(E\mid W)<\infty\), and the same deterministic refinement \(W'=(W,E)\) is used in both laws, then \begin{equation}\label{eq:r-refinement-charge} J_0(W)-J_1(W) \le J_0(W')-J_1(W')+H(E\mid W). \end{equation}
## PAPER Subsphere-methods-for-memory-sample-lower-bounds-in-noiseless-Gaussian-regression-September-27-2026
ABSTRACT: Let a finite-state streaming learner estimate a uniformly random unit vector from independent exact Gaussian linear measurements. We prove that \(o(d^2)\) bits of persistent memory and angular success probability at least \(2/3\) require at least \(2^{-16}d\log_2(1/\epsilon)\) samples for all sufficiently large \(d\), uniformly for \(0<\epsilon\le1/10\). The proof conditions each batch on its observed projection and controls the resulting random residual subsphere.
[theorem[Explicit noiseless precision bound]] \label{s:main} Let \(M:\mathbb N\to\mathbb Z_{\ge0}\) satisfy \(M(d)=o(d^2)\). There is a dimension threshold depending only on this memory sequence such that, for every larger \(d\), every \(0<\epsilon\le1/10\), and every learner in Definition~\ref{s:model}, the following implication holds. If \(S\) is uniform on \(S^{d-1}\), independently of the Gaussian rows and learner randomness, and \[ \Prob\{\arccos\ip{\widehat s}{S}\le\epsilon\}\ge\frac23, \] then \begin{equation}\label{s:main-bound} T\ge 2^{-16}d\log_2(1/\epsilon). \end{equation}
==================
# FAMILY 143: Hilbert's sixteenth problem: uniform bounds for limit cycles
SCOPE: For the quintic Liénard system $x'=y-F(x)$, $y'=-x$, the formalized result proves that every real polynomial $F$ of degree at most five yields at most two limit cycles, and that some such $F$ yields exactly two. Limit cycles are isolated images of nonconstant periodic solutions. No sign, parity, hyperbolicity, or amplitude restriction is imposed.
## CHALLENGE QuinticLienard  targets=['OAI.QuinticLienard.main'] defs=[]
theorem main :
    (∀ F : Polynomial ℝ, F.degree ≤ 5 → {C : Set Plane | IsLimitCycle F C}.encard ≤ 2) ∧
    (∃ F : Polynomial ℝ, F.degree ≤ 5 ∧ {C : Set Plane | IsLimitCycle F C}.encard = 2) := by
  sorry
end QuinticLienard
DEFS(5): abbrev Plane, def vectorField, def IsSolution, def IsPeriodicOrbit, def IsLimitCycle
## PAPER two-limit-cycles-for-quintic-lienard-systems-September-24-2026
ABSTRACT: Every classical Li\'enard system $\dot x=y-F(x)$, $\dot y=-x$, with $F$ an arbitrary real polynomial of degree at most five, has at most two geometrically distinct isolated periodic orbits, and the bound is attained. This proves the degree-five case of the Lins Neto--de Melo--Pugh conjecture.
[theorem] \label{thm:main} If $\deg F\le5$, the system \eqref{eq:original-system} has at most two limit cycles in $\R^2$. Some members of this class have two limit cycles. Thus its exact maximum is two.
==================
# FAMILY 144: Banach’s simple Lebesgue-spectrum problem
SCOPE: Banach's simple Lebesgue-spectrum problem asks for a probability-preserving transformation with simple Lebesgue spectrum on its mean-zero $L^2$ space. The formalization constructs a smooth volume-preserving diffeomorphism of the three-torus with this property. It gives a real-valued cyclic vector whose integer iterates form an orthonormal basis of the entire mean-zero space, and an isometric identification under which the Koopman operator becomes multiplication by the coordinate function on the circle. The transformation is also ergodic.
## CHALLENGE ThreeTorus  targets=['OAI.ThreeTorus.simple_lebesgue_spectrum'] defs=[]
theorem simple_lebesgue_spectrum : MainConclusion := by
  sorry
end ThreeTorus
end
DEFS(11): abbrev Torus, abbrev Cover, def project, def Smooth, def μ, abbrev H, def meanZero, abbrev H₀, abbrev CircleH, def IsReal, def MainConclusion
## PAPER A-smooth-three-torus-diffeomorphism-with-simple-Lebesgue-spectrum-September-23-2026
ABSTRACT: We solve the probability-preserving form of Banach's simple Lebesgue-spectrum problem in smooth dynamics. We construct a $C^\infty$ diffeomorphism of the three-torus that preserves standard volume and whose Koopman operator has simple Lebesgue spectrum on the entire mean-zero $L^2$ space.
[theorem] \label{thm:main} There exist a $C^\infty$ volume-preserving diffeomorphism $T\colon\T^3\to\T^3$ and a real function $f\in L^2_0(\T^3,\mu)$ such that \[ \{f\circ T^n:n\in\Z\} \] is an orthonormal basis of $L^2_0(\T^3,\mu)$. Consequently $T$ is ergodic, and $U_T$ on this space is unitarily equivalent to multiplication by the coordinate $w$ on $L^2(S^1,m)$.
==================
# FAMILY 145: Rokhlin’s multiple-mixing problem
SCOPE: Rokhlin's multiple-mixing problem asks whether ordinary mixing of one invertible probability-preserving transformation implies mixing of every finite order. The formalization proves this implication. For each $k\ge3$ and every $k$ measurable sets, the measure of their translated intersection tends to the product of their measures as all successive time gaps tend to infinity.
## CHALLENGE Rokhlin  targets=['OAI.Rokhlin.mixing_all_finite_orders'] defs=[]
theorem mixing_all_finite_orders (μ : Measure Ω) [IsProbabilityMeasure μ]
    (T : Ω ≃ᵐ Ω) (h_pres : MeasurePreserving T μ μ) (h_mix : IsMixing μ T) :
    ∀ k : ℕ, 3 ≤ k → MixingOfOrder μ T k := by
  sorry
end Rokhlin
DEFS(4): def timeMap, def IsMixing, def layoutTime, def MixingOfOrder
## PAPER Rokhlins-multiple-mixing-problem-for-one-transformation-September-23-2026
ABSTRACT: Every invertible mixing probability-preserving transformation is mixing of every finite order. Thus Rokhlin's multiple-mixing problem for a single transformation has an affirmative answer.
[theorem] \label{thm:main} Every invertible mixing probability-preserving transformation is mixing of every finite order. More explicitly, under the assumptions above, for every $k\ge3$ and every $A_1,\ldots,A_k\in\mathcal F$, \[ \mu\bigl(A_1\cap T^{-n_1}A_2\cap\cdots\cap T^{-(n_1+\cdots+n_{k-1})}A_k\bigr) \longrightarrow\prod_{i=1}^k\mu(A_i) \] as $\min(n_1,\ldots,n_{k-1})\to\infty$ through positive integers. No standardness or countable-generation assumption is imposed on the original probability space.
==================
# FAMILY 146: Positive metric entropy for the standard map
SCOPE: The formalization proves Sinai's positive-entropy conjecture for the standard sine map on the two-dimensional torus in the stronger form of a full positive parameter tail. For every sufficiently large parameter, normalized area has positive metric entropy, and a positive-area set has positive largest Lyapunov exponent with the stated derivative-growth limit. It also constructs a positive-area invariant ergodic hyperbolic component. That component splits into finitely many cyclic pieces on each of which the corresponding iterate is Bernoulli. No genericity assumption on the parameter is used.
## CHALLENGE StandardMapComponents  targets=['OAI.StandardMapEntropy.main_components'] defs=[]
theorem main_components : MainComponentsObligation := by
  sorry
end StandardMapEntropy
DEFS(20): abbrev Circle, abbrev Torus, lemma sine_periodic, def sine, def standardMap, def area, lemma cosine_periodic, def cosine, def torusPotential, def transferStep, def wedge, def tangentCoordinates, def standardDerivative, def standardDerivativeProduct, def VectorGrowth, def LyapunovSpectrumAt, def normalizedArea, def IsBernoulli, def HyperbolicBernoulliComponent, def MainComponentsObligation
## CHALLENGE StandardMapEntropy  targets=['OAI.StandardMapEntropy.main_entropy'] defs=[]
theorem main_entropy : MainObligation := by
  sorry
end StandardMapEntropy
DEFS(12): abbrev Circle, abbrev Torus, lemma sine_periodic, def sine, def standardMap, def area, def FinitePartition, def blockAtom, def blockEntropy, def partitionEntropy, def metricEntropy, def MainObligation
## CHALLENGE StandardMapLyapunov  targets=['OAI.StandardMapEntropy.main_entropy_complete'] defs=[]
theorem main_entropy_complete :
    ∃ k₀ : ℝ, 0 < k₀ ∧ ∀ k : ℝ, k₀ ≤ k →
      0 < metricEntropy area (standardMap k) ∧
      PositiveLargestLyapunov k ∧
      (0 < metricEntropy area (standardMap k) ↔ PositiveLargestLyapunov k) := by
  sorry
end StandardMapEntropy
DEFS(22): abbrev Circle, abbrev Torus, lemma sine_periodic, def sine, def standardMap, def area, def FinitePartition, def blockAtom, def blockEntropy, def partitionEntropy, def metricEntropy, lemma cosine_periodic, def cosine, def torusPotential, def transferStep, def tangentCoordinates, def standardDerivative, def standardDerivativeProduct, def wedge, def VectorGrowth, def LyapunovSpectrumAt, def PositiveLargestLyapunov
## PAPER Positive-Metric-Entropy-for-the-Standard-Map-at-Large-Parameters-September-23-2026
ABSTRACT: We prove that the standard sine map of the two-dimensional torus has positive metric entropy with respect to normalized area for every sufficiently large positive parameter. This gives a full parameter tail, and hence answers Sinai's positive-parameter-measure conjecture affirmatively.
[theorem] \label{main:entropy} There exists $k_0>0$ such that \[ h_m(f_k)>0\qquad\text{for every }k\ge k_0. \] Equivalently, for every such $k$ the largest Lyapunov exponent of $f_k$ is positive on a set of positive $m$-measure.
==================
# FAMILY 148: The entropy-rate dimension formula for self-similar measures
SCOPE: The formalization proves $\dim_H\mu=\min\{1,h_{\mathrm{RW}}/\chi\}$ for the lower Hausdorff dimension of every finite real self-similar probability measure with positive weights and nonzero contraction ratios of absolute value below one. Here $h_{\mathrm{RW}}$ is the entropy rate of random affine compositions and $\chi$ is the corresponding Lyapunov exponent in the same logarithmic base. Ratios may be signed and unequal, and exact overlaps are allowed. It also gives two consequences without exact overlaps: the usual entropy-over-Lyapunov formula for a common positive contraction ratio, and the attractor formula $\dim_H K=\min\{1,s\}$, where $s\ge0$ is the unique solution of $\sum_i|r_i|^s=1$. Absolute continuity is outside these statements.
## CHALLENGE SelfSimilar  targets=['OAI.EntropyRateDimension.entropy_rate_dimension'] defs=[]
theorem entropy_rate_dimension {ι : Type uι} [Fintype ι] [Nonempty ι]
    (S : System ι) (μ : Measure ℝ) [IsProbabilityMeasure μ]
    (hμ : S.SelfSimilar μ) :
    lowerHausdorffDimension μ = ENNReal.ofReal (min 1 (S.entropyRate / S.lyapunov)) := by
  sorry
end EntropyRateDimension
DEFS(12): structure System, def affine, def wordAffine, def completeMap, def wordWeight, def mapSupport, def mapMass, def walkEntropy, def entropyRate, def lyapunov, def SelfSimilar, def lowerHausdorffDimension
## CHALLENGE SelfSimilarCorollaries  targets=['OAI.EntropyRateDimension.Extensions.homogeneous_dimension_direct', 'OAI.CorSetReference.cor_set'] defs=[]
theorem homogeneous_dimension_direct {ι : Type uι} [Fintype ι] [Nonempty ι] (S : System ι)
    {lam : ℝ} (hlam : 0 < lam) (hr : ∀ i, S.ratio i = lam)
    (μ : Measure ℝ) [IsProbabilityMeasure μ] (hμ : S.SelfSimilar μ)
    (h : NoExactOverlaps S) :
    lowerHausdorffDimension μ =
      ENNReal.ofReal (min 1 (symbolEntropy S / Real.log (1/lam))) := by
  sorry
end Extensions
end EntropyRateDimension
end
open scoped BigOperators ENNReal
namespace CorSetReference
theorem cor_set {ι : Type uι} [Fintype ι] [Nonempty ι]
    (r t : ι → ℝ) (hr0 : ∀ i, 0 < |r i|) (hr1 : ∀ i, |r i| < 1)
    (hno : ∀ u v : List ι, u ≠ [] → v ≠ [] →
      word r t u = word r t v → u = v) :
    IsCompact (attractor r t) ∧ (attractor r t).Nonempty ∧
    (∃! s : ℝ, 0 ≤ s ∧ ∑ i, |r i| ^ s = 1) ∧
    (∀ s : ℝ, 0 ≤ s → (∑ i, |r i| ^ s = 1) →
      dimH (attractor r t) = ENNReal.ofReal (min 1 s)) := by
  sorry
end CorSetReference
DEFS(10): structure System, def affine, def wordAffine, def SelfSimilar, def lowerHausdorffDimension, def NoExactOverlaps, def symbolEntropy, def codingPoint, def attractor, def word
## PAPER The-entropy-rate-dimension-formula-for-self-similar-measures-on-the-line-September-24-2026
ABSTRACT: We prove that the Hausdorff dimension of every finite real self-similar measure equals the minimum of one and its random-walk entropy rate divided by its Lyapunov exponent. Exact overlaps are allowed, and the contraction ratios may be unequal and negative. This resolves the entropy-rate dimension conjecture.
[theorem] \label{thm:main} For every finite nonempty indexed family $\varphi_i(x)=r_i x+t_i$ on $\R$ with $0<|r_i|<1$, and every strictly positive probability vector $p$, its self-similar measure satisfies \[ \dim_H\mu_{\Phi,p} =\min\left\{1,\frac{h_{\mathrm{RW}}(\Phi,p)}{\chi(\Phi,p)}\right\}. \] No separation assumption is required; exact overlaps and repeated generators are allowed.
==================
# FAMILY 149: Classwise permanence for weakly reversible mass-action systems
SCOPE: The boundedness and persistence conjectures for mass-action systems ask whether positive concentrations remain finite and separated from zero. The formalization proves this for every finite weakly reversible reaction network with positive constant reaction rates and every strictly positive initial state. A global forward solution exists, and one $\varepsilon\in(0,1)$ bounds every concentration of every global forward solution between $\varepsilon$ and $\varepsilon^{-1}$ for all nonnegative times. The bound may depend on the network, rates, and initial state.
## CHALLENGE MassAction  targets=['OAI.Problem326.global_bounded_persistent_solution'] defs=[]
theorem global_bounded_persistent_solution :
    ∀ (d : ℕ) (N : ReactionNetwork d) (κ : Reaction N → ℝ),
      0 < d → WeaklyReversible N → (∀ e, 0 < κ e) →
      ∀ x0 : Fin d → ℝ, PositiveState x0 →
      ∃ ε : ℝ, 0 < ε ∧ ε < 1 ∧
        (∃ x : ℝ → (Fin d → ℝ), IsGlobalForwardSolution N κ x0 x) ∧
        ∀ x : ℝ → (Fin d → ℝ), IsGlobalForwardSolution N κ x0 x →
        ∀ t : ℝ, 0 ≤ t → ∀ i : Fin d, ε ≤ x t i ∧ x t i ≤ ε⁻¹ := by
  sorry
end Problem326
end
DEFS(8): structure ReactionNetwork, abbrev Reaction, def HasReaction, def WeaklyReversible, def monomial, def massAction, def PositiveState, def IsGlobalForwardSolution
## PAPER Boundedness-and-persistence-of-weakly-reversible-mass-action-systems-September-25-2026
ABSTRACT: We prove the boundedness and persistence conjectures for finite weakly reversible mass-action systems with positive constant reaction rates. For every positive initial condition, the solution exists for all forward time, and every concentration remains bounded above and bounded away from zero. The bounds may depend on the initial condition, and no boundedness assumption is imposed on its stoichiometric compatibility class.
[theorem] \label{thm:main} Let $d\ge1$, let $\mathcal C\subset\mathbb Z_{\ge0}^d$ be finite, let $\mathcal R$ be weakly reversible, and let all reaction rates be positive constants. For every $x^0\in\R_{>0}^d$, the solution of \eqref{eq:mass-action} with $x(0)=x^0$ exists for every $t\ge0$. There is a number $\varepsilon\in(0,1)$, depending on the network, the rates, and $x^0$, such that \begin{equation}\label{eq:main-bounds} \varepsilon\le x_i(t)\le\varepsilon^{-1} \qquad(t\ge0,\ 1\le i\le d). \end{equation}
==================
# FAMILY 150: Weak mixing of triangular billiards with an irrational angle
SCOPE: The formalization proves that the unit-speed billiard flow in every nondegenerate Euclidean triangle with at least one angle irrational relative to $\pi$ is ergodic for normalized area times uniform angular measure. It constructs the flow outside the null set of exceptional trajectories, proves uniqueness of the flight chain there, and establishes measure preservation and the flow law almost everywhere. No genericity or Diophantine condition on the irrational angle is assumed.
## CHALLENGE IrrationalTriangleBilliard  targets=['OAI.TriangularBilliards.irrational_triangle_billiard'] defs=[]
theorem irrational_triangle_billiard (Q : Triangle) (hQ : Q.HasIrrationalAngle) :
    MainConclusion Q := by
  sorry
end TriangularBilliards
end
DEFS(16): structure Triangle, def table, def side, def tangent, def angle, def HasIrrationalAngle, def reflect, instance circleMeasurableSpace, instance circleBorelSpace, abbrev Phase, structure FlightChain, def FlightChain.at, def billiardFlow, def angularMeasure, def phaseMeasure, def MainConclusion
## PAPER Ergodicity-of-triangular-billiards-with-an-irrational-angle-September-25-2026
ABSTRACT: We prove that the unit-speed billiard flow in every nondegenerate Euclidean triangle with at least one angle irrational relative to \(\pi\) is ergodic for normalized area times uniform angular measure. No genericity or Diophantine condition is required. The flow is considered outside the null set of trajectories that hit a vertex.
[theorem] \label{thm:main} Let \(Q\) be the interior of a nondegenerate Euclidean triangle with angles \(\alpha,\beta,\gamma\). Suppose that at least one of \[ \alpha/\pi,\qquad \beta/\pi,\qquad \gamma/\pi \] is irrational. The unit-speed billiard flow \(\Phi_t\), with specular reflection at the open sides, is ergodic on \(Q\times S^1\) for the probability measure \[ d\mu=\frac{dA\,d\theta}{2\pi\operatorname{Area}(Q)}. \] Here trajectories hitting a vertex in either time direction are discarded. In particular, if a measurable set \(A\) satisfies \(\mu(\Phi_t^{-1}A\mathbin\triangle A)=0\) for every \(t\in\R\), then \(\mu(A)\in\{0,1\}\).
==================
# FAMILY 151: A <i>C</i><sup>1</sup> counterexample to the entropy conjecture
SCOPE: Shub's entropy conjecture predicts that a smooth self-map's topological entropy is at least the logarithm of the spectral radius of its action on real homology. The formalization gives a counterexample to the general $C^1$ self-map version: a noninvertible $C^1$ map on a compact smooth manifold without boundary has topological entropy zero, while its action on second real homology has a nonzero eigenvector with eigenvalue $2$. Thus the homological lower bound is strictly positive and fails for this map.
## CHALLENGE C1EntropyCounterexample  targets=['OAI.Problem340.exists_C1_entropy_counterexample'] defs=[]
theorem exists_C1_entropy_counterexample :
    ∃ q : ℕ, 0 < q ∧ ∃ f : CounterexampleManifold q → CounterexampleManifold q, ∃ hf : IsC1SelfMap q f, Dynamics.coverEntropy f (Set.univ : Set (CounterexampleManifold q)) = (0 : EReal) ∧ (∃ v : RealSingularHomology 2 (CounterexampleManifold q), v ≠ 0 ∧ realHomologyMap 2 f hf.1 v = (2 : ℝ) • v) ∧ 0 < Real.log (2 : ℝ) ∧ Real.log (2 : ℝ) ≤ Real.log (totalRealHomologySpectralRadius f hf.1) ∧ ¬ Function.Bijective f ∧ 5 ≤ 2 * q + 3 := by
  sorry
end Problem340
end
DEFS(12): abbrev ClockAmbient, abbrev SphereAmbient, abbrev StandardClock, abbrev StandardSphere2, abbrev CounterexampleManifold, abbrev CounterexampleAmbient, def standardEmbedding, def IsC1SelfMap, def continuousMapOf, abbrev RealSingularHomology, def realHomologyMap, def totalRealHomologySpectralRadius
## PAPER A-C1-Counterexample-to-the-Entropy-Conjecture-September-25-2026
ABSTRACT: We disprove the general \(C^1\) self-map formulation of Shub's entropy conjecture. We construct a noninvertible \(C^1\) self-map of a compact smooth manifold without boundary whose topological entropy is zero, while its action on second real homology has eigenvalue \(2\). Thus the topological entropy is strictly smaller than the logarithm of the homological spectral radius.
[theorem] \label{thm:main} There are a positive integer \(q\) and a \(C^1\) self-map \(f\) of the compact smooth manifold \[ M=(\R/100\Z)\times(S^2)^{q+1} \] such that \(\htop(f)=0\) and \(f_*:H_2(M;\R)\to H_2(M;\R)\) has eigenvalue \(2\). In particular, \[ \htop(f)=0<\log 2\le \log\rho(f_*). \]
==================
# FAMILY 152: Zero entropy does not guarantee a smooth positive-volume model
SCOPE: The paper asks whether a measure-preserving system can be represented by a smooth diffeomorphism preserving positive smooth volume. The formalized supporting result constructs an ergodic invertible transformation of a standard nonatomic probability space with finite Kolmogorov–Sinai entropy that has no such model on any compact finite-dimensional manifold, including manifolds with smooth boundary. The comparison is measurable conjugacy after discarding null sets. The linked statement gives finite entropy; the paper's stronger zero-entropy conclusion is outside this statement.
## CHALLENGE SmoothObstruction  targets=['OAI.SmoothObstruction.main'] defs=[]
theorem main :
    ∃ (X : Type) (_ : MeasurableSpace X) (μ : Measure X)
      (_ : IsProbabilityMeasure μ) (T : X ≃ᵐ X),
      StandardNonatomic μ ∧ Ergodic T μ ∧ FiniteKSEntropy μ T ∧
        ¬ HasSmoothPositiveVolumeModel μ T := by
  sorry
end SmoothObstruction
DEFS(9): def entropyTerm, def blockEntropy, def FiniteKSEntropy, def ConullIsomorphic, def StandardNonatomic, def ConullConjugate, def SmoothPositiveDensity, def HasModelWith, def HasSmoothPositiveVolumeModel
## PAPER A-finite-entropy-system-without-a-smooth-positive-volume-model-September-25-2026
ABSTRACT: We construct an ergodic invertible transformation of a standard nonatomic probability space with zero Kolmogorov--Sinai entropy that has no smooth positive-volume model. More precisely, it is not measurably conjugate to any $C^\infty$ diffeomorphism preserving a strictly positive smooth probability density on a compact finite-dimensional manifold. A single example excludes every finite dimension, including models on nonorientable manifolds and manifolds with smooth boundary.
[theorem] \label{thm:main} There exists an ergodic invertible measure-preserving transformation $(X,\mu,T)$ of a standard nonatomic probability space such that $h_\mu(T)=0$ and $(X,\mu,T)$ is not measurably conjugate, on invariant conull sets, to any $C^\infty$ diffeomorphism of a compact finite-dimensional manifold preserving a strictly positive smooth probability density. The manifold may have smooth boundary and need not be orientable.
==================
# FAMILY 155: A counterexample to periodic tiling in dimension three
SCOPE: The periodic-tiling question asks whether a finite tile that tiles a lattice must admit a periodic tiling. The formalized counterexample is a finite tile in $\mathbb Z^3$ that tiles but has no complement invariant under a finite-index subgroup. Its unit-cube thickening also tiles $\mathbb R^3$ almost everywhere but admits no fully periodic tiling, even with arbitrary real translation vectors. The result also establishes that dimension three is the least lattice dimension where this failure occurs.
## CHALLENGE PeriodicTilingThree  targets=['OAI.PeriodicTilingThree.periodic_tiling_counterexample_and_minimality'] defs=[]
theorem periodic_tiling_counterexample_and_minimality :
    (∃ T : Finset (Lattice 3), T.Nonempty ∧
      (∃ A : Set (Lattice 3), Tiles T A) ∧
      (∀ A : Set (Lattice 3), Tiles T A → ¬ FullyPeriodic A) ∧
      (∃ A : Set (Space 3), AETiles (Thickening T) A) ∧
      (∀ A : Set (Space 3),
        AETiles (Thickening T) A → ¬ EuclideanFullyPeriodic A)) ∧
    IsLeast {d : ℕ | HasTileWithoutPeriodicComplement d} 3 := by
  sorry
end PeriodicTilingThree
end
DEFS(12): abbrev Lattice, def Tiles, def Period, def FullyPeriodic, abbrev Space, def castLattice, def unitCube, def Thickening, def AETiles, def latticeOfBasis, def EuclideanFullyPeriodic, def HasTileWithoutPeriodicComplement
## PAPER A-translational-tile-with-no-fully-periodic-tiling-in-dimension-three-September-23-2026
ABSTRACT: We construct a finite translational tile in $\Z^3$ that admits tilings but no fully periodic tiling. Its unit-cube thickening has the same property in $\R^3$, even when arbitrary real translations are allowed. This gives a negative resolution of the periodic tiling conjecture in dimension three.
[theorem] \label{thm:main} There is a finite nonempty set $T\subset\Z^3$ such that: \begin{enumerate}[label=\textup{(\roman*)}] \item $T$ tiles $\Z^3$ by translations, but no translation set $A$ with $A\oplus T=\Z^3$ is invariant under a subgroup of finite index in $\Z^3$; \item the set $\Omega=T+[0,1]^3$ tiles $\R^3$ by translations up to null sets, but no such tiling has a translation set invariant under a lattice of full rank in $\R^3$. \end{enumerate}
==================
# FAMILY 156: Borsuk's conjecture fails in dimension nine
SCOPE: Borsuk's conjecture predicts that every bounded subset of $\mathbb R^d$ can be covered by $d+1$ sets of strictly smaller diameter. The formalized counterexample is the compact set of rank-one orthogonal projectors onto lines in $\mathbb R^4$, with the Frobenius metric. It lies in the nine-dimensional affine space of trace-one symmetric matrices, has diameter $\sqrt2$, and cannot be covered by ten arbitrary sets of smaller diameter.
## CHALLENGE BorsukNine  targets=['OAI.BorsukNine.main_theorem'] defs=[]
theorem main_theorem :
    IsCompact projectorSet ∧
    projectorSet ⊆ traceOneSymmetric ∧
    Metric.diam projectorSet = Real.sqrt 2 ∧
    ¬ HasTenSmallCover := by
  sorry
end BorsukNine
DEFS(6): abbrev Vector4, abbrev Matrix4, def projector, def projectorSet, def traceOneSymmetric, def HasTenSmallCover
## PAPER A-nine-dimensional-counterexample-to-Borsuks-covering-assertion-September-23-2026
ABSTRACT: The compact set of rank-one orthogonal projectors on $\mathbb R^4$, with the Frobenius metric, cannot be covered by ten sets of strictly smaller diameter. It therefore gives a counterexample to Borsuk's conjecture in dimension nine.
[theorem] \label{thm:main} The compact set \[ X=\{uu^{\mathsf T}:u\in\mathbb R^4,\ \|u\|=1\} \subset\{A\in\operatorname{Sym}_4(\mathbb R):\operatorname{tr}A=1\}, \] with the Frobenius metric, has diameter $\sqrt2$ and cannot be covered by ten subsets of diameter strictly less than $\sqrt2$.
==================
# FAMILY 157: Graph coloring, clique minors, and Colin de Verdière invariants
SCOPE: Hadwiger's conjecture predicts $\chi(G)\le h(G)$ for every finite graph, where $h(G)$ is the largest clique-minor order. The formalization constructs arbitrarily large finite simple counterexamples with independence number at most two. For a graph on $m$ vertices it proves $h(G)<26m/75+2/3<m/2\le\chi(G)$. This disproves the ordinary chromatic form. The paper's fractional-chromatic strengthening and the Colin de Verdière consequence are outside this selected statement. The Linear List Hadwiger conjecture asks for a universal linear bound on list chromatic number in terms of clique-minor size. The formalization proves that there is one integer $C\ge1$ such that every finite nonempty simple graph $G$ satisfies $\chi_{\mathrm{list}}(G)\le C h(G)$, where $h(G)$ is the largest order of a clique minor. The constant is independent of the graph.
## CHALLENGE ListHadwiger  targets=['OAI.LinearListHadwiger.main_theorem'] defs=[]
theorem main_theorem : MainStatement := by
  sorry
end LinearListHadwiger
DEFS(6): def ListColorable, def Choosable, def listChromaticNumber, def HasCliqueMinor, def hadwigerNumber, def MainStatement
## CHALLENGE HadwigerCounterexample  targets=['OAI.HadwigerCounterexample.exists_counterexamples', 'OAI.HadwigerCounterexample.not_hadwiger_conjecture'] defs=[]
theorem exists_counterexamples (M : ℕ) : ∃ m : ℕ, max M 5 ≤ m ∧
    ∃ G : SimpleGraph (Fin m), G.indepNum ≤ 2 ∧
      (connectedMatchingNumber G : ℚ) < (m : ℚ) / 100 ∧
      (hadwigerNumber G : ℚ) < 26 * (m : ℚ) / 75 + 2 / 3 ∧
      26 * (m : ℚ) / 75 + 2 / 3 < (m : ℚ) / 2 ∧
      (m : ℚ) / 2 ≤ (G.chromaticNumber.toNat : ℚ) ∧
      hadwigerNumber G < G.chromaticNumber.toNat ∧
      G.chromaticNumber ≠ ⊤ ∧
      G.chromaticNumber = ↑(G.chromaticNumber.toNat) := by
  sorry
theorem not_hadwiger_conjecture :
    ¬ (∀ (m : ℕ) (G : SimpleGraph (Fin m)),
      G.chromaticNumber ≤ ↑(hadwigerNumber G)) := by
  sorry
end HadwigerCounterexample
DEFS(4): def IsTouchingMatching, def connectedMatchingNumber, def HasCliqueMinor, def hadwigerNumber
## PAPER A-linear-list-coloring-bound-in-terms-of-the-Hadwiger-number-September-23-2026
ABSTRACT: We prove that every finite nonempty graph $G$ satisfies $\chi_{\mathrm{list}}(G)\le C h(G)$ for an absolute integer $C$, where $h(G)$ is the largest order of a clique minor. This resolves the Linear List Hadwiger conjecture affirmatively.
[theorem] \label{thm:main} There is an absolute integer $C\ge1$ such that every finite nonempty simple graph $G$ satisfies \[ \ell(G)\le C h(G). \]
## PAPER A-counterexample-to-Hadwigers-conjecture-September-23-2026
ABSTRACT: We disprove Hadwiger's conjecture by constructing arbitrarily large graphs whose chromatic number exceeds their Hadwiger number. The examples have independence number at most two, and even their ordinary fractional chromatic number exceeds their Hadwiger number. Thus they also disprove the fractional-coloring weakening discussed by Reed and Seymour.
[theorem] \label{thm:main} There are arbitrarily large integers \(m\) for which an \(m\)-vertex finite simple graph \(G\) satisfies \[ \alpha(G)\le2 \qquad\text{and}\qquad \cm(G)<\frac{m}{100}. \]
==================
# FAMILY 158: The Euclidean plane cannot be colored with five colors
SCOPE: The Hadwiger–Nelson problem asks for the fewest colors needed to color the plane so that points at distance one have different colors. The formalized results prove that five colors do not suffice and that seven colors do suffice. The lower bound applies to arbitrary colorings, with no measurability or continuity assumption; the upper bound includes every boundary point of the coloring regions.
## CHALLENGE EuclideanFiveColor  targets=['OAI.EuclideanFiveColor.no_proper_five_coloring'] defs=[]
theorem no_proper_five_coloring : ¬ ∃ coloring : ℂ → Fin 5, ProperColoring 5 coloring := by
  sorry
end EuclideanFiveColor
DEFS(1): def ProperColoring
## CHALLENGE PlaneColoring  targets=['OAI.Problem160.properColoring_seven'] defs=[]
theorem properColoring_seven : ProperColoring 7 := by sorry
end Problem160
end
DEFS(2): abbrev Plane, def ProperColoring
## PAPER The-Euclidean-plane-is-not-five-colorable-September-23-2026
ABSTRACT: We prove that every coloring of the Euclidean plane with five colors has a monochromatic unit-distance pair, with no regularity assumption on the color classes. Consequently, the chromatic number of the plane is either six or seven.
[theorem] \label{thm:main} The Euclidean plane has no proper five-coloring, even when arbitrary color classes are allowed. Consequently, \[ 6\le \chi(\R^2)\le 7. \]
==================
# FAMILY 159: Erdős’s reciprocal-sum conjecture and quasipolynomial Szemerédi bounds
SCOPE: Erdős's reciprocal-sum conjecture asks whether every set of positive integers with divergent reciprocal sum contains arithmetic progressions of every finite length. The formalization proves this statement: for every requested length, such a set contains a progression with positive common difference. The selected theorem is the reciprocal-sum consequence. The paper's quantitative upper bound for the largest progression-free subset of $\{1,\ldots,N\}$ is outside this statement.
## CHALLENGE ErdosReciprocal  targets=['OAI.Erdos3.manuscriptReciprocalProgressionTheorem'] defs=[]
theorem manuscriptReciprocalProgressionTheorem : ReciprocalProgressionTheorem := by
  sorry
end Erdos3
DEFS(3): def HasAP, def reciprocalTerm, def ReciprocalProgressionTheorem
## PAPER Quasipolynomial-Bounds-for-Arithmetic-Progressions-September-23-2026
ABSTRACT: We prove Erd\H{o}s's conjecture that every set of positive integers with divergent reciprocal sum contains arithmetic progressions of every finite length. More quantitatively, for every fixed $k\ge3$, we show \[ r_k(N)\le C_kN\exp\bigl(-c_k(\log N)^{\varepsilon_k}\bigr) \] with $C_k,c_k,\varepsilon_k>0$, where $r_k(N)$ is the largest size of a subset of $\{1,\ldots,N\}$ with no nonconstant $k$-term arithmetic progression.
[theorem] \label{ap:main} For each fixed integer $k\ge3$ there are constants $C_k,c_k,\varepsilon_k>0$ such that, for every $N\ge2$, \begin{equation}\label{ap:density-bound} r_k(N)\le C_kN\exp\bigl(-c_k(\log N)^{\varepsilon_k}\bigr). \end{equation} Equivalently, there is $A_k\ge1$ such that an $\alpha$-dense subset of $[N]$ contains a nonconstant $k$-term progression whenever \begin{equation}\label{ap:threshold} \log N\ge A_k\bigl(2+\log(1/\alpha)\bigr)^{A_k}, \qquad 0<\alpha\le1. \end{equation}
==================
# FAMILY 160: Superexponential van der Waerden numbers
SCOPE: Let $W(r,k)$ be the least interval length forcing a monochromatic $k$-term arithmetic progression in every coloring with at most $r$ colors. The formalized result gives an absolute threshold $K$ such that $W(r,k)>k^{k\lfloor\log_2 r\rfloor/100000}$ for all $k\ge K$ and $r\ge2$. It also establishes the associated growth limits, finiteness, and boundary values. The sharper intermediate estimates used in the paper are not part of the described formalization.
## CHALLENGE QuantitativeVanDerWaerden  targets=['OAI.QuantitativeVanDerWaerden.uniform_lower_bound'] defs=[]
theorem uniform_lower_bound :
    ∃ K : ℕ, ∀ k ≥ K, ∀ r ≥ 2,
      (k : ℝ) ^ ((1 / 100000 : ℝ) * k * (Nat.log 2 r : ℝ)) < (W r k : ℝ) := by
  sorry
end QuantitativeVanDerWaerden
DEFS(4): def MonoAP, def HasMonoAP, def IsRamsey, def W
## PAPER Quantitative-Superexponential-Bounds-for-van-der-Waerden-Numbers-September-23-2026
ABSTRACT: We prove that there are absolute constants $c>0$ and $K_0$ such that $W_r(k)>k^{ck\lfloor\log_2 r\rfloor}$ for every $k\ge K_0$ and $r\ge2$. Consequently $W_r(k)^{1/k}\to\infty$ for each fixed $r\ge2$, giving a quantitative positive resolution of Erd\H{o}s's superexponential-growth question, including the two-color case.
[theorem] \label{main:intro} There is an absolute integer $K_0$ such that, for every integer $k\ge K_0$ and every integer $r\ge2$, \[ W_r(k)>k^{c k\lfloor\log_2r\rfloor}, \qquad c=10^{-5}. \]
==================
# FAMILY 161: Counterexamples to Sidorenko’s conjecture and the forcing conjecture
SCOPE: Sidorenko's conjecture predicts that every bipartite graph $H$ has homomorphism density at least the host graph's edge density raised to $|E(H)|$. The formalization disproves this for the paper's fixed bipartite graph with $35$ vertices and $66$ edges: it constructs a nonempty finite simple host graph with $t(H,G)<t(K_2,G)^{66}$. The separate forcing-conjecture consequence in the paper is outside this statement.
## CHALLENGE SidorenkoCounterexample  targets=['OAI.SidorenkoCounterexample.main'] defs=[]
theorem main : ∃ size : ℕ, 0 < size ∧ ∃ host : SimpleGraph (Fin size),
    (∃ left right, host.Adj left right) ∧ homDensity H host < (edgeDensity host) ^ 66 := by
  sorry
end SidorenkoCounterexample
DEFS(7): def faces, abbrev PatternVertex, def incidence, def H, def homCount, def homDensity, def edgeDensity
## PAPER A-counterexample-to-Sidorenkos-conjecture-September-23-2026
ABSTRACT: We disprove Sidorenko's conjecture with a bipartite graph on \(35\) vertices and \(66\) edges: its homomorphism density in some finite simple graph is smaller than the conjectured lower bound. The same connected graph also disproves the forcing conjecture: at one fixed density, asymptotically matching the edge and pattern densities does not imply quasirandomness.
[theorem] \label{thm:main} Let \(H\) be the incidence graph of the \(22\) triples on \(13\) points in Table~\ref{tab:complex}. This bipartite graph has \(35\) vertices and \(66\) edges. There is a finite simple undirected graph \(G\) with at least one edge such that \[ t(H,G)<p(G)^{66}. \]
==================
# FAMILY 162: Counterexamples to Ryser’s covering conjecture
SCOPE: Ryser's covering conjecture predicts that an intersecting $r$-partite hypergraph has a vertex cover of size at most $r-1$. The formalization proves that every sufficiently large prime $q$ has a finite intersecting $(q+1)$-partite, $(q+1)$-uniform hypergraph with covering number $q+1$ and exactly $q+1$ nonisolated vertices in each part. Thus the conjecture fails even with equal part sizes. The prime threshold is existential. Ryser's covering conjecture predicts $\tau\le(r-1)\nu$ for an $r$-partite hypergraph, where $\tau$ and $\nu$ are its covering and matching numbers. The formalized constructions give finite intersecting $r$-partite $r$-uniform hypergraphs with $\nu=1$ and $\tau=r$, contradicting the bound. The ranks have the form $r=p^n+1$: one fixed prime $p\equiv2\pmod3$ works for all sufficiently large prime degrees $n$, and a second result covers every sufficiently large such prime
## CHALLENGE BalancedRyser  targets=['OAI.Balanced.main_result'] defs=[]
theorem main_result : MainResult := by
  sorry
end Balanced
DEFS(8): structure PartiteHypergraph, abbrev Vertex, def Covers, def Intersecting, def Nonisolated, def HasCoverNumber, def BalancedCounterexample, def MainResult
## CHALLENGE RyserCovering  targets=['OAI.RyserCoveringCounterexample.exists_prime_eventually_counterexampleRank'] defs=[]
theorem exists_prime_eventually_counterexampleRank :
    ∃ p : ℕ, p.Prime ∧ 5 < p ∧ p % 3 = 2 ∧
      ∃ N : ℕ, ∀ n : ℕ, N ≤ n → n.Prime → 2 < n →
        CounterexampleRank (p ^ n + 1) := by
  sorry
end RyserCoveringCounterexample
end
DEFS(10): abbrev Hypergraph, def IsCover, def Intersecting, def matchings, def matchingNumber, def coverCardinalities, def coverNumber, def PartiteUniform, def RPartiteUniform, def CounterexampleRank
## CHALLENGE RyserOddExtensions  targets=['OAI.RyserOdd.eventualOddFailures_and_infinite'] defs=[]
theorem eventualOddFailures_and_infinite :
    (∃ primeThreshold : ℕ, ∀ prime : ℕ, primeThreshold ≤ prime →
      prime.Prime → prime % 3 = 2 →
      ∃ degreeThreshold : ℕ, 3 ≤ degreeThreshold ∧
        ∀ degree : ℕ, degreeThreshold ≤ degree → Odd degree →
          Specification.ExplicitFailureAt (prime ^ degree + 1)) ∧
    Set.Infinite {rank : ℕ | Specification.ExplicitFailureAt rank} := by
  sorry
end RyserOdd
end
DEFS(11): abbrev Hypergraph, def IsCover, def Intersecting, def matchings, def matchingNumber, def coverCardinalities, def coverNumber, def Uniform, def PartiteUniform, def RPartiteUniform, def Specification.ExplicitFailureAt
## PAPER Balanced-Counterexamples-to-Rysers-Conjecture-at-Prime-Orders-September-27-2026
ABSTRACT: For every sufficiently large prime $q$, we construct a finite intersecting $(q+1)$-partite $(q+1)$-uniform hypergraph with covering number $q+1$ and exactly $q+1$ nonisolated vertices in each part. This disproves Ryser's covering conjecture, even for intersecting hypergraphs with equally sized parts.
[theorem] \label{thm:main} There exists $q_0$ such that, for every prime $q\ge q_0$, there is a finite intersecting $(q+1)$-partite $(q+1)$-uniform hypergraph $H$ with \[ |V_1|=\cdots=|V_{q+1}|=q+1, \qquad \tau(H)=q+1. \] Every vertex belongs to an edge.
## PAPER A-Counterexample-to-Rysers-Covering-Conjecture-September-23-2026
ABSTRACT: For every sufficiently large prime $s\equiv2\pmod3$ and every sufficiently large odd integer $n$, with the threshold depending on $s$, we construct an intersecting $(s^n+1)$-partite $(s^n+1)$-uniform hypergraph with covering number $s^n+1$. This disproves Ryser's covering conjecture in its intersecting case.
[theorem] \label{thm:main} There exists $s_0$ such that, for every prime $s\ge s_0$ with $s\equiv2\pmod3$, there is an integer $n_0(s)\ge3$ with the following property. For every odd integer $n\ge n_0(s)$, put $q=s^n$. There is a finite intersecting $(q+1)$-partite $(q+1)$-uniform hypergraph $H$ satisfying \[ \tau(H)=q+1. \] In particular, the intersecting case of~\eqref{eq:ryser} is false.
==================
# FAMILY 165: The Harary–Hill and Zarankiewicz crossing-number formulas
SCOPE: The formalized result proves Hill's proposed formula for the crossing number of the complete graph: for every $n\ge3$, $\mathrm{cr}(K_n)=\frac14\lfloor n/2\rfloor\lfloor(n-1)/2\rfloor\lfloor(n-2)/2\rfloor\lfloor(n-3)/2\rfloor$. It proves the lower bound and constructs a matching two-page drawing. Crossings are spatial points, so repeated crossings of one edge pair count separately. Zarankiewicz's crossing-number conjecture predicts $\mathrm{cr}(K_{m,n})=\lfloor m/2\rfloor\lfloor(m-1)/2\rfloor\lfloor n/2\rfloor\lfloor(n-1)/2\rfloor$. The formalized result proves this equality for every positive $m,n$ and constructs a drawing attaining it. Crossings are counted as spatial points for continuous simple edge paths, including repeated crossings between the same pair of edges.
## CHALLENGE CompleteCrossing  targets=['OAI.Paper170.complete_graph_crossing_number'] defs=[]
theorem complete_graph_crossing_number (order : ℕ) (at_least_three : 3 ≤ order) :
    ordinaryCrossingNumber (completeGraph order) = hill order := by
  sorry
end Paper170
end
DEFS(12): abbrev Plane, structure Graph, abbrev CompleteEdge, def completeGraph, structure ContinuousDrawing, def edgeInterior, structure ProperCrossing, def crossingPoints, structure AdmissibleDrawing, def crossingCount, def ordinaryCrossingNumber, def hill
## CHALLENGE BipartiteCrossing  targets=['OAI.Zarankiewicz.mainTarget_proof'] defs=[]
theorem mainTarget_proof : MainTarget := by
  sorry
end Zarankiewicz
end
DEFS(11): def axisPairs, abbrev Plane, abbrev BipartiteVertex, abbrev BipartiteEdge, structure ContinuousDrawing, def edgeInterior, def ProperCrossing, def crossingPoints, structure AdmissibleDrawing, def crossingCount, def MainTarget
## PAPER The-crossing-number-of-complete-graphs-September-23-2026
ABSTRACT: We prove the Harary--Hill conjecture: for every positive integer $n$, the ordinary crossing number of the complete graph $K_n$ is \[ \frac14\left\lfloor\frac n2\right\rfloor \left\lfloor\frac{n-1}{2}\right\rfloor \left\lfloor\frac{n-2}{2}\right\rfloor \left\lfloor\frac{n-3}{2}\right\rfloor. \]
[theorem] \label{thm:main} For every integer \(n\ge3\), \[ \crn(K_n)=Z(n):= \frac14\left\lfloor\frac n2\right\rfloor \left\lfloor\frac{n-1}2\right\rfloor \left\lfloor\frac{n-2}2\right\rfloor \left\lfloor\frac{n-3}2\right\rfloor. \]
## PAPER The-crossing-number-of-complete-bipartite-graphs-September-23-2026
ABSTRACT: We prove the Zarankiewicz crossing-number conjecture, resolving Tur\'an's brickyard problem. For all positive integers $m,n$, the ordinary crossing number of the complete bipartite graph $K_{m,n}$ is \[ \left\lfloor\frac m2\right\rfloor \left\lfloor\frac{m-1}{2}\right\rfloor \left\lfloor\frac n2\right\rfloor \left\lfloor\frac{n-1}{2}\right\rfloor. \]
[theorem] \label{thm:main} For all positive integers $m,n$, \[ \crn(K_{m,n})=d_m d_n. \]
==================
# FAMILY 167: Planar distinct distances and unit-distance bounds
SCOPE: The formalized result shows that large repeated distance fibers are rare in arbitrary finite planar point sets. For each fixed $s>0$, the largest possible fraction of ordered distinct pairs $(x,y)$ whose distance from the pin $x$ occurs at least $n^s$ times tends to zero as the set size $n$ grows. Consequently, for every $\varepsilon>0$, the fraction of pins determining fewer than $n^{1-\varepsilon}$ distances tends uniformly to zero. The separate unit-distance power-saving theorem is not included. The planar unit-distance problem asks how many pairs at distance one can occur among $n$ points. The formalization proves that there are absolute constants $C>0$ and $1\le\beta<4/3$ such that every finite planar point set of size $n$ determines at most $Cn^\beta$ unordered unit-distance pairs. The same constants work for every $n$, giving a fixed power improvement over the classical exponent $
## CHALLENGE PinnedDistances  targets=['OAI.WeakPinned.main'] defs=None
theorem main (s : ℝ) (hs : 0<s) : Tendsto (fun n : ℕ => F n s) atTop (𝓝 0) := by
  sorry
end WeakPinned
end
DEFS(6): abbrev Plane, def distanceFiber, def k, def richPairs, def pairFraction, def F
## CHALLENGE PlanarUnitDistances  targets=['OAI.PlanarUnitDistances.main'] defs=[]
theorem main : ∃ C β : ℝ, 0 < C ∧ 1 ≤ β ∧ β < (4 : ℝ) / 3 ∧
    ∀ n : ℕ, (u n : ℝ) ≤ C * (n : ℝ) ^ β := by
  sorry
end PlanarUnitDistances
DEFS(4): abbrev Plane, def IsUnitPair, def unitPairCount, def u
## PAPER The-weak-pinned-planar-distance-theorem-September-23-2026
ABSTRACT: We prove the weak pinned Erd\H{o}s distinct-distance conjecture. For every fixed $\varepsilon>0$, all but $o(n)$ points of any $n$-point planar set determine at least $n^{1-\varepsilon}$ distinct nonzero distances.
[theorem] \label{thm:main} For every fixed $s>0$, one has $F_n(s)\longrightarrow0$ as $n\longrightarrow\infty$.
## PAPER A-power-saving-for-planar-unit-distances-September-23-2026
ABSTRACT: We prove a power saving for the planar unit-distance problem: for some absolute \(\beta<4/3\), every set of \(n\) points in the Euclidean plane determines \(O(n^\beta)\) unordered pairs at unit distance.
[theorem] \label{thm:main} There are absolute constants \(0<C<\infty\) and \(1\le\beta<4/3\) such that \(u(n)\le Cn^\beta\) for every nonnegative integer \(n\).
==================
# FAMILY 168: Combinatorial invariance of Kazhdan–Lusztig polynomials
SCOPE: The combinatorial invariance conjecture asks whether a Kazhdan–Lusztig polynomial depends only on its Bruhat interval as an ordered set. The formalization proves that every order isomorphism between Bruhat intervals in arbitrary Coxeter systems preserves the corresponding equal-parameter Kazhdan–Lusztig polynomial. The two intervals may come from different Coxeter systems.
## CHALLENGE KLInvariance  targets=['OAI.KLInvariance.combinatorial_invariance'] defs=[]
theorem combinatorial_invariance
    {B' : Type u'} {W' : Type v'} [Group W'] {M' : CoxeterMatrix B'}
    (cs : CoxeterSystem M W) (cs' : CoxeterSystem M' W')
    {u b : W} {u' b' : W'}
    (hub : BruhatLE cs u b) (hub' : BruhatLE cs' u' b')
    (ι : Interval cs u b ≃o Interval cs' u' b') :
    klPolynomial cs u b = klPolynomial cs' u' b' := by
  sorry
end KLInvariance
DEFS(9): def BruhatStep, def BruhatLE, def Interval, instance intervalOrder, def rankDifference, abbrev PolynomialFamilies, structure NormalizedKL, def klFamilies, def klPolynomial
## PAPER Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026
ABSTRACT: We prove that an isomorphism of Bruhat intervals in arbitrary Coxeter systems preserves their equal-parameter Kazhdan--Lusztig polynomials. This resolves the full combinatorial invariance conjecture positively.
[theorem[Combinatorial invariance]] \label{thm:main} Let $(W,S)$ and $(W',S')$ be arbitrary Coxeter systems, and let $u\le b$ in $W$ and $u'\le b'$ in $W'$. If \[ \iota:[u,b]\longrightarrow[u',b'] \] is an isomorphism of abstract Bruhat interval posets, then their equal-parameter Kazhdan--Lusztig polynomials satisfy \[ P^W_{u,b}(q)=P^{W'}_{u',b'}(q). \]
==================
# FAMILY 169: Shareshian–Wachs elementary positivity
SCOPE: The elementary-positivity part of the Shareshian–Wachs conjecture asks whether the chromatic quasisymmetric function of every natural unit interval graph has nonnegative coefficients in the elementary basis. The formalization proves this over $\mathbb N[q]$. It constructs an explicit elementary-basis expansion indexed by the graph's permitted nondescent permutations, with each term weighted by a nonnegative power of $q$ determined by its graph inversions. The expansion holds for every finite number of color variables.
## CHALLENGE ElementaryPositivity  targets=['OAI.elementaryPositivityExpansion'] defs=['OAI.elementaryPositivityWitness']
theorem elementaryPositivityExpansion (n : ℕ)
    (G : ElementaryPositivity.NaturalUnitIntervalGraph n) (r : ℕ) :
    G.chromatic r =
      ∑ σ : {σ : Equiv.Perm (Fin n) // G.Nondescent σ},
        MvPolynomial.C (Polynomial.X ^ G.graphInversions σ.val) *
          MvPolynomial.esymmPart (Fin r) (Polynomial ℕ)
            ((elementaryPositivityWitness n G).theta σ) := by
  sorry
DEFS(9): structure NaturalUnitIntervalGraph, def Edge, def Nondescent, def graphInversions, def Proper, def coloringAscents, def chromatic, structure PermutationWitness, def elementaryPositivityWitness
## PAPER Elementary-Positivity-of-Chromatic-Quasisymmetric-Functions-September-24-2026
ABSTRACT: We prove that the chromatic quasisymmetric function of every natural unit interval graph is elementary-positive over $\N[q]$. This resolves the elementary-positivity part of the Shareshian--Wachs conjecture.
[theorem[Elementary positivity and a permutation witness]] \label{main:theorem} There is a deterministic terminating procedure which, given a natural unit interval graph $G$ on $[n]$ and $\sigma\in D_G^0$, returns a partition $\theta_G(\sigma)\vdash n$ such that \begin{equation} \chi_G(X;q)=\sum_{\sigma\in D_G^0} q^{\ginv_G(\sigma)}e_{\theta_G(\sigma)}(X). \label{main:witness} \end{equation} In particular every elementary coefficient of $\chi_G(X;q)$ belongs to $\N[q]$. The assertion holds as a formal symmetric-function identity, uniformly in $n$ and $G$.
==================
# FAMILY 170: Sharp logarithmic exponents for off-diagonal Ramsey numbers
SCOPE: The formalization determines the sharp logarithmic exponent of the off-diagonal Ramsey number $r(5,t)$. It proves $r(5,t)=t^4/(\log t)^{3+o(1)}$ as $t\to\infty$. For every $\varepsilon>0$, the lower bound $t^4/(\log t)^{3+\varepsilon}$ holds eventually, while the upper bound is $Ct^4/(\log t)^3$ for an absolute $C>0$. The corresponding logarithmic exponent converges to three along all natural values of $t$. The formalization determines the sharp logarithmic exponent of the off-diagonal Ramsey number for every fixed integer $s\ge6$. It proves $r(s,t)=t^{s-1}/(\log t)^{s-2+o(1)}$ as $t\to\infty$. More explicitly, for each $\varepsilon>0$ the lower bound $t^{s-1}/(\log t)^{s-2+\varepsilon}$ holds eventually, while the upper bound is $C_s t^{s-1}/(\log t)^{s-2}$. The logarithmic exponent limit is taken along all natural values of $t$.
## CHALLENGE RamseyFive  targets=['OAI.SharpRamseyFive.main'] defs=[]
theorem main : SharpBounds ∧ SharpExponent := by
  sorry
end SharpRamseyFive
DEFS(4): def RamseyProperty, def ramsey, def SharpBounds, def SharpExponent
## CHALLENGE SharpLogRamsey  targets=['OAI.SharpLogRamsey.main'] defs=[]
theorem main (s : ℕ) (hs : 6 ≤ s) : MainBounds s ∧ MainLimit s := by
  sorry
end SharpLogRamsey
DEFS(4): def RamseyProperty, def ramsey, def MainBounds, def MainLimit
## PAPER The-Sharp-Logarithmic-Exponent-of-r-5-t-September-24-2026
ABSTRACT: We determine the sharp logarithmic exponent of the off-diagonal Ramsey number \(r(5,t)\): \[ r(5,t)=\frac{t^4}{(\log t)^{3+o(1)}} \qquad (t\longrightarrow\infty). \]
[theorem] \label{thm:main} There is an absolute constant \(C>0\) such that, for every \(\varepsilon>0\), all sufficiently large integers \(t\) satisfy \[ \frac{t^4}{(\log t)^{3+\varepsilon}} \ \le\ r(5,t)\ \le\ C\frac{t^4}{(\log t)^3}. \] The threshold for \(t\) may depend on \(\varepsilon\). Consequently, \[ \lim_{t\to\infty} \frac{4\log t-\log r(5,t)}{\log\log t}=3. \]
## PAPER Sharp-Logarithmic-Exponents-for-Fixed-Off-Diagonal-Ramsey-Numbers-September-24-2026
ABSTRACT: For every fixed integer $s\ge6$, we determine the sharp logarithmic exponent of the off-diagonal Ramsey number: \[ r(s,t)=\frac{t^{s-1}}{(\log t)^{s-2+o(1)}} \qquad (t\longrightarrow\infty). \]
[theorem] \label{intro:main} For every fixed integer $s\ge6$ there is a constant $C_s>0$ such that, for every $\varepsilon>0$ and every sufficiently large integer $t$, \[ \frac{t^{s-1}}{(\log t)^{s-2+\varepsilon}} \le r(s,t) \le C_s\frac{t^{s-1}}{(\log t)^{s-2}}. \] In particular, \[ \lim_{t\to\infty} \frac{(s-1)\log t-\log r(s,t)}{\log\log t}=s-2. \]
==================
# FAMILY 172: Classification of finite Euclidean Ramsey configurations
SCOPE: A finite configuration is Euclidean Ramsey if every finite coloring of some sufficiently high-dimensional Euclidean space contains a monochromatic congruent copy at the original scale. The formalization gives the tensor-field classification for full-affine-span configurations, covers singleton and affine-span reductions, and proves that every Ramsey configuration is cospherical. It also proves that every nonempty subset of a finite transitive configuration and every nonempty set of at most five points on a circle is Ramsey. A further sufficient condition uses linear independence of the quadratic evaluation rows of a spherical configuration. The formalization also gives spherical non-Ramsey examples: the specified twelve-point set on the unit circle has a fifty-color obstruction in every positive dimension, and a nine-point circle configuration built from algebraically independent paramet
## CHALLENGE EuclideanRamsey  targets=['OAI.EuclideanRamsey.classification'] defs=[]
theorem classification {s d : ℕ} (a : Fin s → Space d)
    (hs : 2 ≤ s) (hd : 1 ≤ d) (ha : Function.Injective a)
    (hspan : affineSpan ℝ (Set.range a) = ⊤) :
    Ramsey a ↔ FieldCriterion a := by
  sorry
end EuclideanRamsey
end
DEFS(10): abbrev Space, def Congruent, def Ramsey, def coordinateField, abbrev Coeff, abbrev TensorRing, def coordinate, def augmented, def multiply, def FieldCriterion
## CHALLENGE GrahamSpherical  targets=['OAI.GrahamSpherical.full_main'] defs=[]
theorem full_main : Specification.FullAuthoredResult := by
  sorry
end GrahamSpherical
end
DEFS(12): abbrev Point, abbrev Label, def parameter, def u, def v, def squareCoordinate, def coordinates, def vertex, def witness, def AvoidsCopy, def EuclideanRamsey, def FullAuthoredResult
## CHALLENGE EuclideanRamseyCircle  targets=['OAI.EuclideanRamsey.CircleConsequence.at_most_five_circle_points_ramsey'] defs=[]
theorem at_most_five_circle_points_ramsey {s : ℕ} (a : Fin s → Space 2)
    (hs : 0 < s) (hs5 : s ≤ 5) (ha : Function.Injective a)
    (hsphere : ∃ c : Space 2, ∃ r : ℝ, ∀ i, dist (a i) c = r) : Ramsey a := by
  sorry
end CircleConsequence
end EuclideanRamsey
end
DEFS(3): abbrev Space, def Congruent, def Ramsey
## CHALLENGE EuclideanRamseyNine  targets=['OAI.EuclideanRamsey.NineStatement.nine_circle_configuration'] defs=[]
theorem nine_circle_configuration (t : Fin 9 → ℝ)
    (ht : AlgebraicIndependent ℚ t) :
    Function.Injective (literalCircleConfig t) ∧
      (∀ i, dist (literalCircleConfig t i) 0 = 1) ∧
      ¬ Ramsey (literalCircleConfig t) := by
  sorry
end NineStatement
end EuclideanRamsey
end
DEFS(4): abbrev Space, def Congruent, def Ramsey, def literalCircleConfig
## CHALLENGE EuclideanRamseyQuadratic  targets=['OAI.EuclideanRamsey.spherical_quadraticIndependent_ramsey_all'] defs=[]
theorem spherical_quadraticIndependent_ramsey_all {s d : ℕ}
    (a : Fin s → Space d) (ha : Function.Injective a)
    (hspan : affineSpan ℝ (Set.range a) = ⊤)
    (hsphere : ∃ c : Space d, ∃ r : ℝ, ∀ i, dist (a i) c = r)
    (hrows : LinearIndependent (Coeff a)
      (fun i : Fin s => fun q : Option (Fin d) × Option (Fin d) =>
        augmented a i q.1 * augmented a i q.2)) : Ramsey a := by
  sorry
end EuclideanRamsey
end
DEFS(7): abbrev Space, def Congruent, def Ramsey, def coordinateField, abbrev Coeff, def coordinate, def augmented
## CHALLENGE EuclideanRamseySpherical  targets=['OAI.EuclideanRamsey.ramsey_cospherical'] defs=[]
theorem ramsey_cospherical {s d : ℕ} (a : Fin s → Space d)
    (ha : Function.Injective a) (hR : Ramsey a) :
    EuclideanGeometry.Cospherical (Set.range a) := by
  sorry
end EuclideanRamsey
end
DEFS(3): abbrev Space, def Congruent, def Ramsey
## CHALLENGE EuclideanRamseyTransitive  targets=['OAI.EuclideanRamsey.TransitiveConsequence.subset_of_finite_transitive_ramsey'] defs=[]
theorem subset_of_finite_transitive_ramsey {s t D : ℕ}
    (a : Fin s → Space D) (y : Fin t → Space D)
    (hs : 0 < s) (ha : Function.Injective a) (_hy : Function.Injective y)
    (htrans : ∀ i j : Fin t, ∃ σ : Equiv.Perm (Fin t),
      (∀ k l : Fin t, dist (y (σ k)) (y (σ l)) = dist (y k) (y l)) ∧ σ i = j)
    (hsub : Set.range a ⊆ Set.range y) : Ramsey a := by
  sorry
end TransitiveConsequence
end EuclideanRamsey
DEFS(3): abbrev Space, def Congruent, def Ramsey
## PAPER A-classification-of-finite-Euclidean-Ramsey-configurations-September-23-2026
ABSTRACT: We classify finite Euclidean Ramsey configurations by a necessary and sufficient tensor condition over their coordinate fields. The Ramsey property here concerns monochromatic congruent copies at the original scale under arbitrary finite colorings. The criterion shows that every nonempty subtransitive set and every nonempty set of at most five points on a circle is Ramsey. In particular, some Ramsey cyclic quadrilaterals are not subtransitive, disproving the necessity direction of the Leader--Russell--Walters conjectured characterization.
[theorem[Classification]] \label{thm:classification} Let $A=\{a_1,\ldots,a_s\}\subset\R^d$ be a finite set of at least two points with affine span $\R^d$, and define $p_i,F,B,m_F$ as above. Then $A$ is Ramsey if and only if there is a matrix $P\in\operatorname{Mat}_{d+1}(B)$ such that \begin{align} (p_i\otimes1)^T P(1\otimes p_i)&=0 &&(1\le i\le s),\label{eq:field-evaluations}\\ m_F(P_{\alpha\beta})&=\delta_{\alpha\beta} &&(1\le\alpha,\beta\le d).\label{eq:field-spatial} \end{align} Here the entries of $p_i\otimes1$ and $1\otimes p_i$ are formed componentwise. There are no separate conditions on the multiplied constant row or constant column of $P$.
==================
# FAMILY 173: Seymour’s second-neighborhood conjecture
SCOPE: Seymour's second-neighborhood conjecture asserts that every nonempty finite oriented graph has a vertex with at least as many second out-neighbors as first out-neighbors. The formalized result proves this assertion, where the second neighborhood consists of vertices at directed distance exactly two. The initial vertex and first neighbors are excluded from that count, and sinks are included.
## CHALLENGE SeymourSecondNeighborhood  targets=['OAI.SeymourSecondNeighborhood.exists_goodVertex'] defs=[]
theorem exists_goodVertex (r : V → V → Prop) (hr : IsOriented r) :
    ∃ v, GoodVertex r v := by
  sorry
end SeymourSecondNeighborhood
DEFS(4): structure IsOriented, def firstNeighbors, def secondNeighbors, def GoodVertex
## PAPER A-proof-of-Seymours-second-neighborhood-conjecture-September-23-2026
ABSTRACT: We prove that every nonempty finite oriented graph has a vertex with at least as many vertices at directed distance two as at directed distance one. This resolves Seymour's second neighborhood conjecture positively.
[theorem] \label{thm:main} Every nonempty finite oriented graph has a vertex \(v\) such that \[ \abs{N_1^+(v)}\leq \abs{N_2^+(v)}. \]
==================
# FAMILY 174: Deterministic construction of strong thin spanning trees
SCOPE: The strong thin-tree conjecture asks for spanning trees that cross every cut sparsely relative to the original graph. The formalized result gives one absolute constant $C>0$ such that every finite loopless $k$-edge-connected multigraph with at least two vertices has a spanning tree crossing each nontrivial cut at most $(C/k)$ times the original cut size. Parallel edges remain distinct. No numerical value of $C$ or construction algorithm is asserted. The strong thin-tree problem asks for a spanning tree that crosses every cut sparsely relative to the original graph. The formalization gives one deterministic polynomial-time algorithm and an absolute constant $C>0$ such that a finite $k$-edge-connected loopless multigraph yields a spanning tree using at most a $C/k$ fraction of the edges of every cut. The input may encode parallel-edge multiplicities in binary, and the running time is polyn
## CHALLENGE StrongThinTree  targets=['OAI.StrongThinTree.strongThinTree'] defs=[]
theorem strongThinTree : MainStatement := by
  sorry
end StrongThinTree
DEFS(6): structure MultiGraph, def cut, def Connected, def SpanningTree, def EdgeConnected, def MainStatement
## CHALLENGE AlgorithmicThinTrees  targets=['OAI.AlgorithmicThinTrees.algorithmic_strong_thin_trees'] defs=[]
theorem algorithmic_strong_thin_trees : AlgorithmicStrongThinTrees := by
  sorry
end AlgorithmicThinTrees
DEFS(37): structure MultiGraph, def cut, def Connected, def SpanningTree, def EdgeConnected, def frame, def encodeNat, inductive StackAction, def StackAction.apply, structure Instruction, def Instruction.halt, structure Machine, structure Config, def topCode, def headsCode, def Machine.step, def Machine.init, def Machine.run, structure ExplicitInput, structure BinaryInput, abbrev BinaryInput.Edge, def BinaryInput.edgeEquiv, def BinaryInput.graph, inductive Input, def ExplicitInput.encode, def BinaryInput.encode, def Input.encode, def Input.length, def Input.n, def Valid
## PAPER The-strong-thin-tree-conjecture-September-23-2026
ABSTRACT: We prove that every finite loopless \(k\)-edge-connected multigraph on at least two vertices, with \(k\ge1\), has a spanning tree meeting each cut in at most \(C/k\) times the size of the cut, where \(C\) is a universal constant. This resolves the strong thin tree conjecture.
[theorem] \label{thm:main} There is a universal constant \(C>0\) such that, for every integer \(k\ge1\), every finite \(k\)-edge-connected undirected multigraph without loops and with at least two vertices has a spanning tree \(T\) satisfying \[ |\delta_T(S)|\le\frac Ck\,|\delta_G(S)| \qquad\text{for every }\varnothing\ne S\subsetneq V. \]
## PAPER A-polynomial-time-construction-of-strong-thin-trees-September-23-2026
ABSTRACT: We give a deterministic polynomial-time construction of strong thin trees. Given a finite $k$-edge-connected loopless multigraph on at least one vertex, the algorithm constructs a spanning tree meeting every cut in at most a $C/k$ fraction of its edges, for a universal constant $C$. The running time is polynomial in the binary input length, including when parallel-edge multiplicities are encoded in binary.
[theorem[Hierarchy bound for the metric test cone]] \label{thm:tg-hierarchy} There is an absolute integer $h_0$ such that, for every integer $h\ge h_0$, every locally $h$-connected hierarchy of $G$, and every collection $\mathcal M$ of nonroot nodes satisfying $|O(A)|\ge |P(A)|/h$, there is a matrix $D\succ0$ on $\mathsf E$ with \begin{align} \ip{D}{Z}&\le\ip{L_G}{Z} &&(Z\in\mathcal N),\label{tg:shortcut}\\ \frac1{|O(A)|}\sum_{e\in O(A)}b_e^TD^{-1}b_e &\le h^{-31/40} &&(A\in\mathcal M).\label{tg:hierarchy-resistance} \end{align} The cutoff is independent of the graph and the hierarchy depth.
==================
# FAMILY 175: Talagrand’s expectation thresholds, discrete convexity, and graph decompositions
SCOPE: Talagrand's expectation-threshold conjecture asks whether the fractional and integral expectation thresholds are comparable by an absolute constant. The formalized result proves $q_f(\mathcal F)\le25\cdot512^4 q(\mathcal F)$ for every nonempty proper increasing family on a finite nonempty ground set. Both thresholds use cover budget $1/2$, and fractional covers may assign weights to every subset, including the empty set. The formalized result proves Talagrand's discrete-convexity assertion with $k=2^{75}$. If a family of subsets of a finite nonempty ground set has Bernoulli-$p$ measure at least $1-1/k$, then the sets not contained in a union of $k$ members form a $p$-small family: they have a containment cover of total $p$-cost at most $1/2$. This holds for every $0<p<1$, with repeated members allowed in the union and no monotonicity assumption.
## CHALLENGE TalagrandExpectationThreshold  targets=['OAI.TalagrandThreshold.talagrand_expectation_threshold_equivalence'] defs=[]
theorem talagrand_expectation_threshold_equivalence [Nonempty α]
    (F : Family α) (_hF : F.Nonempty) (hproper : F ≠ Finset.univ)
    (hIncreasing : Increasing F) :
    qf F ≤ ((25 : ℝ) * (512 : ℝ) ^ 4) * q F := by
  sorry
end TalagrandThreshold
DEFS(12): abbrev Family, def cost, def Covers, def Small, def fracCost, def FractionalCover, def FractionalSmall, def Increasing, def integralFeasible, def fractionalFeasible, def q, def qf
## CHALLENGE TalagrandDiscreteConvexity  targets=['OAI.TalagrandDiscreteConvexity.talagrand_discrete_convexity'] defs=[]
theorem talagrand_discrete_convexity (N : ℕ) (_hN : 1 ≤ N)
    (p : ℝ) (hp0 : 0 < p) (hp1 : p < 1) (D : Family (Fin N))
    (hD : 1 - 1 / (2 : ℝ) ^ 75 ≤ familyMeasure p D) :
    Small p (exceptional ((2 : ℕ) ^ 75) D) := by
  sorry
end
end TalagrandDiscreteConvexity
DEFS(8): abbrev Family, def bernoulliMass, def familyMeasure, def cost, def Covers, def Small, def unionTuple, def exceptional
## PAPER Integral-and-fractional-expectation-thresholds-are-equivalent-September-23-2026
ABSTRACT: We prove Talagrand's conjecture that integral and fractional expectation thresholds are within a universal constant factor, with the same covering budget.
[theorem] \label{thm:main} For every finite nonempty $X$ and every nonempty proper increasing family $\F\subseteq2^X$, \[ q_f(\F)\le25\cdot512^4\,q(\F). \] Both thresholds use the budget $1/2$. The constant is independent of $|X|$, the sizes of the minimal members of $\F$, and the support of the fractional cover.
## PAPER Talagrands-discrete-convexity-conjecture-September-23-2026
ABSTRACT: We prove Talagrand's discrete-convexity conjecture. There is a universal integer $k$ such that, whenever an arbitrary family has Bernoulli product measure at least $1-1/k$, the sets not contained in a union of $k$ members admit a cover of total cost at most $1/2$ at the same density.
[theorem] \label{thm:main} Set $k=2^{75}$. For every integer $N\ge1$, every $p\in(0,1)$, and every family $\mathcal D\subseteq2^{[N]}$, \[ \mu_p(\mathcal D)\ge1-\frac1k \quad\Longrightarrow\quad E_k(\mathcal D)\text{ is }p\text{-small}. \]
==================
# FAMILY 176: The second Kahn–Kalai conjecture with an edge-count bound
SCOPE: The second Kahn–Kalai conjecture compares the threshold for a random graph to contain a fixed graph with its expectation threshold. The formalized result proves the comparison up to a universal factor times $1+\log_2|E(H)|$, and hence up to a universal factor times $\log_2 n$, for every graph $H$ with at least one edge and at most $n$ vertices, $n\ge2$. The bounds use the actual containment and expectation thresholds.
## CHALLENGE SecondKahnKalai  targets=['OAI.LeanBlast.SecondKahnKalai.secondKahnKalaiBounds'] defs=[]
theorem secondKahnKalaiBounds (n : ℕ) (V : Type u) [Fintype V]
    (H : SimpleGraph V) (hn : 2 ≤ n) (hcard : Fintype.card V ≤ n)
    (hedge : 1 ≤ edgeCount H) : SecondKahnKalaiBounds n H := by
  sorry
end LeanBlast.SecondKahnKalai
end
DEFS(12): def bernoulliWeight, def bernoulliExpectation, def bernoulliProbability, abbrev Edge, def graphOfEdges, def edgeCount, def expectedCopies, def containmentProbability, def criticalThreshold, def expectationThreshold, def logTwo, def SecondKahnKalaiBounds
## PAPER The-second-Kahn-Kalai-conjecture-September-24-2026
ABSTRACT: We prove the second Kahn--Kalai conjecture. For every finite simple graph $H$ with $h\ge1$ edges and at most $n$ vertices, the threshold for $G(n,p)$ to contain an ordinary copy of $H$ is at most $C p_{\mathrm E}(n,H)(1+\log_2 h)$, where $C$ is universal. Here $p_{\mathrm E}(n,H)$ is the least density at which every subgraph of $H$ has expected copy count at least one half.
[theorem] \label{thm:main} For every $n\ge2$ and every finite simple graph $H$ with $h=e(H)\ge1$ edges and at most $n$ vertices, \begin{equation}\label{eq:stronger} \pc(n,H)\le \min\{1,\;2048\ee^{50}\pE(n,H)(1+\log_2 h)\}. \end{equation} In particular, \[ \pc(n,H)\le6144\ee^{50}\pE(n,H)\log_2 n. \]
==================
# FAMILY 177: Bounded-degree coboundary expanders
SCOPE: The formalization constructs bounded-degree $\mathbb F_2$ coboundary expanders in every dimension $d\ge3$. For each such $d$, it gives finite pure connected $d$-dimensional simplicial complexes with vertex counts tending to infinity, one uniform bound on top-dimensional degree at each vertex, and one positive coboundary-expansion constant in every degree below $d$. The constants may depend on $d$. The graph and two-dimensional cases used for the paper's all-positive-dimensions conclusion are separate.
## CHALLENGE CoboundaryExpanders  targets=['OAI.CoboundaryExpanders.main'] defs=[]
theorem main : MainStatement := by
  sorry
end CoboundaryExpanders
end
DEFS(13): structure Complex, def facesOf, def Face, def Pure, def Connected, abbrev Cochain, def weight, def norm, def coboundary, def coboundaries, def distance, def topDegree, def MainStatement
## PAPER Bounded-degree-coboundary-expanders-in-every-dimension-September-24-2026
ABSTRACT: For every integer $d\ge3$, we construct arbitrarily large finite $d$-dimensional simplicial complexes with uniformly bounded vertex degrees and uniform $\mathbb F_2$ coboundary expansion in every degree below $d$. Together with the known graph and two-dimensional cases, this establishes the existence of bounded-degree $\mathbb F_2$ coboundary expanders in every positive dimension.
[theorem] \label{thm:main} For every integer $d\ge3$, there exist constants $D<\infty$, $\eps>0$, and finite connected pure $d$-dimensional simplicial complexes $X_m$, with $|X_m(0)|\longrightarrow\infty$, such that every vertex belongs to at most $D$ faces of dimension $d$ and, for every $f\in C^i(X_m;\F)$, \begin{equation}\label{eq:goal} \norm{\delta_i f}_{X_m,i+1} \ge \eps\,\dist_{X_m,i}(f,B^i(X_m)) \qquad(0\le i<d). \end{equation} The constants are independent of $m$, $i$, and $f$.
==================
# FAMILY 179: The circulant Hadamard and Barker-sequence conjectures
SCOPE: The formalization proves the circulant Hadamard conjecture in exact form: a real circulant Hadamard matrix of positive order $n$ exists exactly when $n=1$ or $n=4$. Explicit witnesses are supplied for both orders, with no restriction on prime factors. It also proves the even-length part of the Barker-sequence consequence. A positive even-length sign sequence whose nonzero aperiodic autocorrelations have absolute value at most one must have length $2$ or $4$. The paper's classification of odd Barker lengths is outside this selected additional statement.
## CHALLENGE CirculantHadamard  targets=['OAI.CirculantHadamard.exists_iff_order_one_or_four'] defs=[]
theorem exists_iff_order_one_or_four (n : ℕ) (hn : 0 < n) :
    ExistsRealCirculantHadamard n ↔ n = 1 ∨ n = 4 := by
  sorry
end CirculantHadamard
DEFS(5): def IsSign, abbrev RealMatrix, def IsCirculant, def IsSignHadamard, def ExistsRealCirculantHadamard
## CHALLENGE EvenBarker  targets=['OAI.CirculantHadamard.Barker.even_length_eq_two_or_four'] defs=[]
theorem even_length_eq_two_or_four {n : ℕ} (h : Fin n → ℤ)
    (hnpos : 0 < n) (hn : Even n) (hb : IsBarker h) : n = 2 ∨ n = 4 := by
  sorry
end Barker
end CirculantHadamard
DEFS(3): def IsSign, def aperiodic, def IsBarker
## PAPER The-circulant-Hadamard-conjecture-September-23-2026
ABSTRACT: We prove the circulant Hadamard conjecture: a real circulant Hadamard matrix has order $1$ or $4$. As a consequence, Barker sequences of length greater than one exist exactly at lengths $2,3,4,5,7,11,13$, proving the Barker-sequence conjecture.
[theorem] \label{thm:main} For a positive integer \(n\), a real circulant Hadamard matrix of order \(n\) exists if and only if \(n\in\{1,4\}\).
==================
# FAMILY 180: Barnette’s Hamiltonian-cycle conjecture
SCOPE: Barnette's conjecture states that every finite simple cubic bipartite planar graph that is 3-vertex-connected has a Hamiltonian cycle. The formalization proves this statement for every such graph. The selected result is the existence of a cycle visiting every vertex exactly once.
## CHALLENGE BarnetteHamiltonian  targets=['OAI.Barnette.main'] defs=[]
theorem main : MainStatement.{u} := by
  sorry
end Barnette
DEFS(5): structure PlaneEmbedding, def Planar, def ThreeVertexConnected, def HasHamiltonianCycle, def MainStatement
## PAPER Paired-states-and-Hamiltonian-cycles-in-cubic-bipartite-planar-graphs-September-24-2026
ABSTRACT: We prove Barnette's conjecture: every finite simple cubic bipartite planar \(3\)-vertex-connected graph has a Hamiltonian cycle.
[theorem] \label{thm:main} Every finite simple undirected graph that is cubic, bipartite, planar, and \(3\)-vertex-connected has a Hamiltonian cycle.
==================
# FAMILY 181: The Erdős–Gallai cycle-decomposition conjecture
SCOPE: The Erdős–Gallai cycle-decomposition conjecture asks for a linear bound on the number of cycles and single edges needed to partition a graph's edges. The formalized result gives one absolute constant $C>0$ such that every finite simple graph on $n$ vertices has an edge-disjoint decomposition into at most $Cn$ cycles or singleton edges. Edgeless and small graphs are included. The optimal value of $C$ is not determined.
## CHALLENGE CycleDecomposition  targets=['OAI.ErdosGallai.erdos_gallai'] defs=[]
theorem erdos_gallai : MainStatement := by
  sorry
end ErdosGallai
end
DEFS(3): def CycleOrSingleEdge, def EdgeDecomposition, def MainStatement
## PAPER A-linear-cycle-and-edge-decomposition-of-every-graph-September-24-2026
ABSTRACT: We prove that every finite simple undirected graph on \(n\) vertices has an edge partition into at most \(Cn\) simple cycles and single edges, for an absolute constant \(C\). This resolves the Erd\H{o}s--Gallai cycle decomposition conjecture positively.
[theorem] \label{thm:main} There is an absolute constant \(C>0\) such that, for every finite simple undirected graph \(G\) with \(n\) vertices, \(E(G)\) has a partition into at most \(Cn\) parts, each of which is the edge set of a cycle or consists of a single edge.
==================
# FAMILY 182: Power savings for intersective polynomial differences and prime arguments
SCOPE: The formalization proves a fixed power saving for sets with no nonzero square difference. There are absolute constants $c>0$ and $C$ such that every $A\subseteq\{1,\ldots,N\}$ satisfying $a-b\ne m^2$ for all $a,b\in A$ and integers $m\ge1$ has $|A|\le C N^{1-c}$. The bound is uniform for every integer $N\ge1$.
## CHALLENGE SquareDifference  targets=['OAI.SquareDifference.power_saving'] defs=[]
theorem power_saving :
    ∃ c C : ℝ, 0 < c ∧ ∀ N : ℕ, 1 ≤ N → ∀ A : Finset ℤ,
      A ⊆ Finset.Icc 1 (N : ℤ) → SquareDifference.IsSquareDifferenceFree A →
        (A.card : ℝ) ≤ C * (N : ℝ) ^ (1 - c) := by
  sorry
end SquareDifference
DEFS(1): def IsSquareDifferenceFree
## PAPER A-power-saving-for-square-difference-free-sets-September-24-2026
ABSTRACT: We prove that there are absolute constants $c>0$ and $C<\infty$ such that every set $A\subseteq\{1,\ldots,N\}$ with no nonzero square difference satisfies $|A|\le C N^{1-c}$. This answers the fixed-power question posed by Green and Sawhney.
[theorem] \label{thm:main} There are absolute constants $c>0$ and $C<\infty$ such that, for every integer $N\ge1$ and every square-difference-free set $A\subseteq[N]$, \[ |A|\le C N^{1-c}. \] Equivalently, every subset of $[N]$ larger than $C N^{1-c}$ contains distinct elements whose absolute difference is the square of a positive integer.
==================
# FAMILY 183: Power savings for planar halving lines and <i>k</i>-sets
SCOPE: A halving pair in an even planar point set is a pair whose line leaves equally many remaining points on each side. The formalization proves that some absolute $\varepsilon>0$ and $C$ bound the number of halving pairs by $Cn^{4/3-\varepsilon}$ for every sufficiently large even $n$ and every $n$-point set with no three collinear. It also proves a bound of the same form for all level-switch counts under the additional generic-position assumptions in the statement. The constants are existential.
## CHALLENGE HalvingLines  targets=['OAI.PlanarHalving.power_bounds'] defs=[]
theorem power_bounds :
    (∃ ε : ℝ, 0 < ε ∧ ∃ C : ℝ, ∃ n₀ : ℕ,
      ∀ n : ℕ, Even n → n₀ ≤ n → ∀ P : Fin n → Point,
        GeneralPosition P → (halvingCount P : ℝ) ≤ C * (n : ℝ) ^ ((4 : ℝ) / 3 - ε)) ∧
    (∃ ε : ℝ, 0 < ε ∧ ∃ C : ℝ,
      ∀ n : ℕ, 1 ≤ n → ∀ P : Fin n → Point, Generic P →
        ∀ k : ℕ, k ≤ n → (switchCount P k : ℝ) ≤ C * (n : ℝ) ^ ((4 : ℝ) / 3 - ε)) :=
  sorry
end PlanarHalving
DEFS(9): abbrev Point, def orient, def GeneralPosition, def sideCount, def halvingCount, def slope, def Generic, def belowCount, def switchCount
## PAPER A-power-saving-for-planar-halving-lines-September-25-2026
ABSTRACT: There are absolute constants $\varepsilon>0$ and $C$ such that every sufficiently large even $n$-point set in the plane with no three collinear has at most $Cn^{4/3-\varepsilon}$ unordered halving pairs. This gives a power saving over the classical $O(n^{4/3})$ bound for planar halving lines. The proof is nonquantitative and does not supply explicit constants.
[theorem] \label{thm:halving-power} There exist absolute constants $\varepsilon>0$, $C<\infty$, and $n_0$ such that, for every even $n\ge n_0$ and every $n$-point set $P\subset\mathbb R^2$ with no three collinear, \[ h(P)\le C n^{4/3-\varepsilon}. \]
==================
# FAMILY 184: Correspondence coloring with a fixed forbidden subgraph
SCOPE: The formalized result gives a logarithmic improvement in the independence number of clique-free graphs. For every fixed integer $r\ge4$, there is $c_r>0$ such that every finite $K_r$-free simple graph on $n$ vertices with average degree $d\ge2$ has an independent set of size at least $c_r n\log d/d$. The constant depends only on $r$.
## CHALLENGE CliqueFreeLog  targets=['OAI.CliqueFreeLog.logarithmic_independence_bound'] defs=[]
theorem logarithmic_independence_bound (r : ℕ) (hr : 4 ≤ r) :
    ∃ c : ℝ, 0 < c ∧
      ∀ {V : Type} [Fintype V] (G : SimpleGraph V),
        G.CliqueFree r → 2 ≤ averageDegree G →
        c * (Fintype.card V : ℝ) * Real.log (averageDegree G) / averageDegree G ≤
          (G.indepNum : ℝ) := by
  sorry
end CliqueFreeLog
DEFS(1): def averageDegree
## PAPER A-Logarithmic-Independence-Bound-for-Clique-Free-Graphs-September-25-2026
ABSTRACT: For every fixed integer $r\ge4$, every $K_r$-free graph on $n$ vertices with average degree $d\ge2$ has an independent set of size at least $c_r n\log d/d$, where $c_r>0$ depends only on $r$. This proves the fixed-clique-size independence conjecture of Ajtai, Erd\H{o}s, Koml\'os and Szemer\'edi.
[theorem] \label{thm:main} For every integer $r\ge4$, there is a constant $c_r>0$ such that every finite simple $K_r$-free graph $G$ with $n$ vertices and average degree $d\ge2$ satisfies \[ \alpha(G)\ge c_r\frac{n\log d}{d}. \]
==================
# FAMILY 185: Counterexamples to infinite matroid intersection and packing/covering
SCOPE: The infinite matroid packing/covering conjecture predicts a partition of a common ground set into parts admitting the corresponding packing and covering. The formalization constructs two self-dual partitional matroids on one countably infinite ground set that admit neither an independent covering nor a packing/covering partition. The same pair has no intersection witness, so it also refutes the unrestricted infinite matroid intersection conjecture. Separate formalized consequences give counterexamples to the individual covering and packing conjectures. The construction is in ordinary set theory with Choice and assumes no finitary restriction on the matroids.
## CHALLENGE InfiniteMatroid  targets=['OAI.InfiniteMatroidCounterexample.main'] defs=[]
theorem main :
    Countable E ∧ Infinite E ∧
    ∃ M₀ M₁ : Matroid E,
      M₀.E = Set.univ ∧ M₁.E = Set.univ ∧
      M₀.dual = M₀ ∧ M₁.dual = M₁ ∧
      (∀ I₀ I₁ : Set E, M₀.Indep I₀ → M₁.Indep I₁ → I₀ ∪ I₁ ≠ Set.univ) ∧
      ¬ HasPackingCovering M₀ M₁ := by
  sorry
end InfiniteMatroidCounterexample
DEFS(4): abbrev D, abbrev E, def contractOnto, def HasPackingCovering
## CHALLENGE InfiniteMatroidCorollaries  targets=['OAI.InfiniteMatroidCounterexample.partitional_intersection_counterexample', 'OAI.InfiniteMatroidCounterexample.separate_covering_packing_counterexamples'] defs=[]
theorem partitional_intersection_counterexample :
    Countable E ∧ Infinite E ∧
    ∃ Q : Matroid E0, Q.E = univ ∧ Q.dual = Q ∧ IsUniform Q ∧
      let M₀ := rayMatroid Q false
      let M₁ := rayMatroid Q true
      M₀.E = univ ∧ M₁.E = univ ∧ M₀.dual = M₀ ∧ M₁.dual = M₁ ∧
      IsPartitional M₀ ∧ IsPartitional M₁ ∧
      (∀ I₀ I₁ : Set E, M₀.Indep I₀ → M₁.Indep I₁ → I₀ ∪ I₁ ≠ univ) ∧
      ¬ HasPackingCovering M₀ M₁ ∧ ¬ HasIntersection M₀ M₁ := by
  sorry
theorem separate_covering_packing_counterexamples :
    (∃ (F : Set E) (M : Bool → Matroid E),
      (∀ i, (M i).E = F) ∧ ¬ CoveringConjectureFor F M) ∧
    (∃ (F : Set E) (M : Bool → Matroid E),
      (∀ i, (M i).E = F) ∧ ¬ PackingConjectureFor F M) := by
  sorry
end InfiniteMatroidCounterexample
DEFS(19): abbrev D, abbrev E0, abbrev E, def contractOnto, def HasPackingCovering, def bundleAt, def parityBit, abbrev Vertex, def componentMap, def globalComponentMap, def componentEquiv, def rayMatroid, def IsUniform, def IsPartitional, def HasIntersection, def FamilyCovering, def FamilyPacking, def CoveringConjectureFor, def PackingConjectureFor
## PAPER A-Counterexample-to-the-Infinite-Matroid-Packing-Covering-Conjecture-September-24-2026
ABSTRACT: We construct in ZFC two self-dual partitional matroids on a countably infinite common ground set that admit neither a packing/covering partition nor an intersection witness. This disproves the unrestricted infinite matroid packing/covering and intersection conjectures and answers Jo\'o's question for two partitional matroids negatively. The examples are neither finitary nor cofinitary.
[theorem] \label{thm:main} In ZFC, there exist a countably infinite set $E$ and two infinite matroids $M_0,M_1$ on $E$ such that $M_i^*=M_i$ on the same labelled ground set for $i=0,1$, and \[ I_0\cup I_1\ne E \quad\text{for every independent }I_0\text{ in }M_0 \text{ and independent }I_1\text{ in }M_1. \] The pair $(M_0,M_1)$ has no packing/covering partition. Consequently, the infinite matroid packing/covering conjecture is false.
==================
# FAMILY 186: Uniform influence and sharp thresholds for graph and hypergraph properties
SCOPE: The Friedgut–Kalai sharp-threshold conjecture concerns how quickly a nontrivial increasing graph property appears in the independent-edge random graph. For every $n\ge2$, every such property invariant under vertex relabeling, and $0<\varepsilon<1/2$, the formalization proves that the edge-probability interval between probabilities $\varepsilon$ and $1-\varepsilon$ has width at most $2^{19}\log(1/(2\varepsilon))/(\log n)^2$. The constant is uniform over the graph property, $n$, and $\varepsilon$.
## CHALLENGE SharpThreshold  targets=['OAI.Problem313.sharp_threshold_width'] defs=[]
theorem sharp_threshold_width :
    ∀ (n : ℕ) (f : GraphConfig n → Bool) (ε : ℝ),
      2 ≤ n → VertexInvariant f → IncreasingGraphProperty f →
      NontrivialGraphProperty f → 0 < ε → ε < (1 / 2 : ℝ) →
      graphQuantile (1 - ε) f - graphQuantile ε f ≤
        ((2 : ℝ) ^ 19 / (Real.log (n : ℝ)) ^ 2) * Real.log (1 / (2 * ε)) := by
  sorry
end Problem313
end
DEFS(12): abbrev GraphEdge, abbrev GraphConfig, def permEdge, def permuteConfig, def VertexInvariant, def ConfigLE, def IncreasingGraphProperty, def NontrivialGraphProperty, def boolReal, def graphWeight, def graphMean, def graphQuantile
## PAPER A-Sharp-Threshold-Bound-for-Monotone-Graph-Properties-September-25-2026
ABSTRACT: We prove the Friedgut--Kalai sharp-threshold conjecture. For every integer $n\ge2$, every nontrivial increasing family of graphs on $n$ vertices invariant under all vertex permutations, and every $0<\varepsilon<1/2$, the edge probabilities at which its probability equals $\varepsilon$ and $1-\varepsilon$ differ by at most $C\log(1/(2\varepsilon))/(\log n)^2$, for a universal constant $C$.
[theorem[Friedgut--Kalai sharp-threshold conjecture]] \label{thm:threshold} For every integer $n\ge2$, every nontrivial increasing family $\mathcal P$ of graphs on $n$ vertices invariant under all vertex permutations, and every $0<\varepsilon<1/2$, \begin{equation} \label{eq:threshold} p_{1-\varepsilon}(\mathcal P)-p_\varepsilon(\mathcal P) \le \frac{2^{19}}{(\log n)^2}\log\frac1{2\varepsilon}. \end{equation}
==================
# FAMILY 187: Snaky in 21 Maker moves
SCOPE: In the Snaky Maker–Breaker game, the players alternately claim cells of $\mathbb Z^2$, and Maker seeks a translated, rotated, or reflected copy of the six-cell Snaky shape. The formalization gives a legal strategy that wins within $21$ actual Maker moves against every legal Breaker play from the empty infinite board. The selected theorem checks disjointness and the move counts throughout play; it does not impose the paper's smaller finite-board restriction. The linked supplements reconstruct the older $35$-move appendix's finite recursive certificate and prove four conditional winning templates from partial positions, assuming the required Maker cells are present and Breaker avoids the corresponding finite envelope.
## CHALLENGE SnakyCertificate  targets=['OAI.SnakyCertificate.certificate_correct'] defs=[]
theorem certificate_correct :
    TableValid ∧ placementCount = 1837 ∧
    Output 557 (-1, 0) 118 19 {p | p.1 ≤ -3 ∧ p.2 ≤ -2} ∧
    Output 595 (-1, 0) 222 27 {p | p.1 = -2 ∧ p.2 ≤ -2} ∧
    Output 603 (-1, 0) 275 27 {p | p.1 ≤ -3 ∧ p.2 = 0} ∧
    Output 615 (1, 0) 686 34 {(1, -1)} ∧
    AllRows := by
  sorry
end SnakyCertificate
DEFS(670): instance rotationModulus_neZero, instance digitModulus_neZero, abbrev Cell, def origin, def snaky, def orient, def placement, def basePoint, def baseEnvelope, def baseRequired, structure Term, def Term.shift, structure Entry, def emptyEntry, def entry_6, def entry_7, def entry_8, def entry_9, def entry_10, def entry_11, def entry_12, def entry_13, def entry_14, def entry_15, def entry_16, def entry_17, def entry_18, def entry_19, def entry_20, def entry_21
## CHALLENGE SnakyConditional  targets=['OAI.SnakyConditional.snaky_winning_strategy_with_legal_states'] defs=[]
theorem snaky_winning_strategy_with_legal_states :
    ∃ σ : Policy Cell,
      (∀ r M B, σ r M B ∉ M ∧ σ r M B ∉ B) ∧
      ∀ β : ℕ → Cell, LegalRepliesBeforeFinal σ 35 β ∅ ∅ →
        HasSnaky (playState σ 35 β ∅ ∅ 35).1 ∧
        (playState σ 35 β ∅ ∅ 35).1.card = 35 ∧
        Disjoint (playState σ 35 β ∅ ∅ 35).1 (playState σ 35 β ∅ ∅ 34).2 ∧
        ∀ k, k < 35 →
          Disjoint (playState σ 35 β ∅ ∅ k).1 (playState σ 35 β ∅ ∅ k).2 ∧
          (playState σ 35 β ∅ ∅ k).2.card = k := by
  sorry
DEFS(9): abbrev Cell, def snaky, def orient, def placement, def HasSnaky, abbrev Policy, def playState, def makerAt, def LegalRepliesBeforeFinal
## CHALLENGE SnakyTwentyOne  targets=['OAI.SnakyPrototype.snaky_winning_strategy_21_with_legal_states'] defs=[]
theorem snaky_winning_strategy_21_with_legal_states :
    ∃ σ : Policy Cell,
      (∀ r M B, σ r M B ∉ M ∧ σ r M B ∉ B) ∧
      ∀ β : ℕ → Cell, LegalRepliesBeforeFinal σ 21 β ∅ ∅ →
        HasSnaky (playState σ 21 β ∅ ∅ 21).1 ∧
        (playState σ 21 β ∅ ∅ 21).1.card = 21 ∧
        Disjoint (playState σ 21 β ∅ ∅ 21).1 (playState σ 21 β ∅ ∅ 20).2 ∧
        ∀ k, k < 21 →
          Disjoint (playState σ 21 β ∅ ∅ k).1 (playState σ 21 β ∅ ∅ k).2 ∧
          (playState σ 21 β ∅ ∅ k).2.card = k := by
  sorry
end SnakyPrototype
DEFS(9): abbrev Cell, def snaky, def orient, def placement, def HasSnaky, abbrev Policy, def playState, def makerAt, def LegalRepliesBeforeFinal
## PAPER Snaky-in-21-Maker-moves-September-25-2026
ABSTRACT: We prove that Maker can achieve the Snaky hexomino within 21 actual Maker moves against arbitrary legal Breaker play on the initially empty infinite square board. The same bound holds on a $17\times17$ square; in fact, Maker can confine its claims to a fixed $251$-cell board.
[theorem] \label{thm:main} In this game, there is one globally legal Maker policy that completes an allowed copy of $S$ within at most $21$ actual Maker claims against every legal continuation of Breaker. Equivalently, extend the policy by fresh claims after an earlier win: its Maker set after claim $21$ contains a target whenever the first $20$ Breaker replies are legal.
==================
# FAMILY 188: The sharp terminal leave in random triangle removal
SCOPE: Start with the complete graph on $n$ vertices and repeatedly delete the three edges of a uniformly chosen remaining triangle. The formalization proves that the number of edges at termination, divided by $n^{3/2}$, converges in $L^2$ to $1/(2\sqrt2)$. It also states convergence in probability and convergence of the normalized expectation to the same constant. This is the triangle case of the sharp terminal-leave conjecture of Joos and Kühn.
## CHALLENGE TriangleRemoval  targets=['OAI.SharpTerminalLeave.sharp_terminal_leave'] defs=[]
theorem sharp_terminal_leave :
    Tendsto (fun n => expectation n (fun G =>
      (normalizedLeave n G - sharpConstant) ^ 2)) atTop (𝓝 0) ∧
    (∀ ε : ℝ, 0 < ε →
      Tendsto (fun n => probability n (fun G =>
        ε < |normalizedLeave n G - sharpConstant|)) atTop (𝓝 0)) ∧
    Tendsto (fun n => expectation n (fun G => (G.card : ℝ)) / normalization n)
      atTop (𝓝 sharpConstant) := by
  sorry
end SharpTerminalLeave
DEFS(11): abbrev Graph, def completeGraph, def triangles, def step, def evolve, def terminalLaw, def expectation, def probability, def normalization, def normalizedLeave, def sharpConstant
## PAPER The-Sharp-Terminal-Leave-in-Random-Triangle-Removal-September-25-2026
ABSTRACT: Starting from the complete graph on $n$ vertices, repeatedly remove the three edges of a uniformly chosen remaining triangle. We prove that the number of edges left at termination, divided by $n^{3/2}$, converges in $L^2$ to $1/(2\sqrt2)$. This proves the triangle case of the sharp-constant conjecture of Joos and K\"uhn. In particular, the same limit holds in probability and for the normalized expectation.
[theorem] \label{thm:main} For the uniform triangle-removal process starting from $K_n$, \[ \E\left[\left(\frac{F_n}{n^{3/2}}- \frac1{2\sqrt2}\right)^2\right]\longrightarrow0. \] In particular, \[ \frac{F_n}{n^{3/2}}\xrightarrow{\Prb}\frac1{2\sqrt2}, \qquad \frac{\E F_n}{n^{3/2}}\longrightarrow\frac1{2\sqrt2}. \]
==================
# FAMILY 189: Cycle–clique Ramsey numbers
SCOPE: The cycle–clique Ramsey conjecture predicts the exact number of vertices forcing either a cycle $C_m$ or a clique $K_n$ in complementary colors. The formalization proves $R(C_m,K_n)=(m-1)(n-1)+1$ for all integers $m\ge n\ge3$ except $(m,n)=(3,3)$, where it proves $R(C_3,K_3)=6$. This is the complete parameter range of the paper's main theorem.
## CHALLENGE CycleCliqueRamsey  targets=['OAI.CycleClique.thm_main'] defs=[]
theorem thm_main :
    (∀ m n : ℤ, n ≤ m → 3 ≤ n → (m, n) ≠ (3, 3) →
      (cycleCliqueRamsey m.toNat n.toNat : ℤ) = (m - 1) * (n - 1) + 1) ∧
    cycleCliqueRamsey 3 3 = 6 := by
  sorry
end CycleClique
DEFS(2): def RamseyProperty, def cycleCliqueRamsey
## PAPER Cycle-clique-Ramsey-numbers-September-25-2026
ABSTRACT: We prove that $R(C_m,K_n)=(m-1)(n-1)+1$ for every pair of integers $m\ge n\ge3$ other than $(m,n)=(3,3)$, for which $R(C_3,K_3)=6$. This establishes the cycle--clique conjecture of Erd\H{o}s, Faudree, Rousseau and Schelp. The proof combines expansion in a minimal counterexample with a large-clique lemma and an optimization of paths joining clique vertices. These arguments reduce the remaining cases to $3{,}099$ finite parameter-pattern instances, which are excluded by two exact implementations of proved inference rules. Complete programs and deduction traces accompany the paper.
[theorem] \label{thm:main} For all integers $m\ge n\ge3$ with $(m,n)\ne(3,3)$, \[ R(C_m,K_n)=(m-1)(n-1)+1. \] For the excluded pair, $R(C_3,K_3)=6$.
==================
# FAMILY 190: Polynomial removal fails for ordered binary matrices
SCOPE: The formalized result disproves a polynomial removal bound for one explicit $66\times66$ binary pattern. For every $c,C>0$, there is an $n\times n$ binary matrix at normalized edit distance at least $\varepsilon>0$ from being pattern-free but with fewer than $c\varepsilon^C n^{132}$ induced ordered copies. Row and column indices are independently increasing, and every zero and one entry must match. The construction gives an explicit sequence of such matrices, allowing edits in both directions.
## CHALLENGE MatrixRemoval  targets=['OAI.Problem348.no_polynomial_removal_bound'] defs=[]
theorem no_polynomial_removal_bound :
    ∀ c C : ℝ, 0 < c → 0 < C →
  ∃ n : ℕ, 1 ≤ n ∧
    ∃ ε : ℝ, 0 < ε ∧ ε < 1 ∧
      ∃ A : BinaryMatrix n,
        fixedDistance A ≥ ε ∧
        (copyCount fixedH A : ℝ) <
          c * Real.rpow ε C * ((n : ℝ) ^ 132) := by
  sorry
end Problem348
end
DEFS(11): abbrev BinaryMatrix, abbrev IncreasingMap, def orderedCopies, def copyCount, def HFree, def hammingDistance, def etaBit, def anchor64, def fixedH, def fixedMinEdits, def fixedDistance
## PAPER Polynomial-removal-fails-for-ordered-binary-matrices-September-25-2026
ABSTRACT: We construct a fixed $66\times66$ binary matrix for which ordered matrix removal has no polynomial bound. This disproves the polynomial ordered binary matrix-removal conjecture. Ordered copies preserve the separate row and column orders and match both zeros and ones; removal permits changing entries in either direction.
[theorem] \label{thm:main} There is a fixed binary $66\times66$ matrix $H$ with the following property. For every integer $h\ge1$, put \[ n_h=(386h+2)2^h,\qquad \epsilon_h=(386h+2)^{-2}. \] There is a binary $n_h\times n_h$ matrix $A_h$ such that \[ \operatorname{dist}_H(A_h)\ge\epsilon_h, \qquad \frac{N_H(A_h)}{n_h^{132}}\le\epsilon_h2^{-h}. \] Consequently, no positive constants $c,C$ give a polynomial removal bound for this fixed $H$.
==================
# FAMILY 191: A power improvement in the Heilbronn triangle lower bound
SCOPE: Heilbronn's triangle problem asks how large the smallest triangle determined by $n$ points in the unit square can be. The formalization constructs an unbounded sequence of sizes $n$ and point sets for which every triangle has area at least $n^{-2+\eta}$, for one fixed $\eta>0$. It consequently refutes the proposed upper bound of order $n^{-2+\varepsilon}$ for every $\varepsilon>0$. The linked construction is for an unbounded sequence of sizes; the paper's statement for every sufficiently large $n$ is broader.
## CHALLENGE HeilbronnTriangle  targets=['OAI.Problem355.heilbronn_power_lower_bound', 'OAI.Problem355.almost_n_minus_two_refuted'] defs=[]
theorem heilbronn_power_lower_bound :
    0 < heilbronnExponent ∧ ∃ n : ℕ → ℕ, ∃ P : ℕ → Finset Point,
      Filter.Tendsto n Filter.atTop Filter.atTop ∧ ∀ j : ℕ,
        3 ≤ n j ∧ (P j).card = n j ∧ pointsInUnitSquare (P j) ∧
        triangleAreasAtLeast (P j)
          (Real.rpow (n j : ℝ) (-2 + heilbronnExponent)) := by
  sorry
theorem almost_n_minus_two_refuted :
    0 < heilbronnExponent / 2 ∧
      ¬ eventualAlmostUpperBound (heilbronnExponent / 2) := by
  sorry
end Problem355
end
DEFS(12): abbrev Point, def triangleArea, def pointInUnitSquare, def pointsInUnitSquare, def triangleAreasAtLeast, def hasTriangleAreaAtMost, def heilbronnD, def heilbronnM, def heilbronnT, def heilbronnK, def heilbronnExponent, def eventualAlmostUpperBound
## PAPER A-power-improvement-in-the-Heilbronn-triangle-lower-bound-September-25-2026
ABSTRACT: There are absolute constants $\eta,c_1>0$ such that, for every sufficiently large integer $n$, one can choose $n$ points in the unit square so that every triangle they determine has area at least $c_1n^{-2+\eta}$. Thus the almost $n^{-2}$ upper-bound formulation of Heilbronn's triangle problem is false. The exponent $\eta$ is fixed but extremely small.
[theorem] \label{intro:main} There are absolute constants $\eta,c_1>0$ and an integer $n_0\ge3$ such that \[ \Delta(n)\ge c_1n^{-2+\eta} \qquad\text{for every integer }n\ge n_0. \]
==================
# FAMILY 192: Boolean functions violate the square-root degree bound by arbitrary factors
SCOPE: The formalization disproves the Gopalan–Servedio square-root degree conjecture by an unbounded factor. For every $C>0$, it gives a nonconstant Boolean function on a finite sign cube for which the sum of its linear Fourier coefficients exceeds $C\sqrt{\deg f}$, where $\deg f$ is its real multilinear degree. It also proves that the ratio of the sum of the absolute values of those coefficients to $\sqrt{\deg f}$ is unbounded among positive-degree Boolean functions.
## CHALLENGE SquareRootDegree  targets=['OAI.SquareRootDegree.main'] defs=[]
theorem main : SignedViolations ∧ ¬ BddAbove AbsoluteRatios := by
  sorry
end SquareRootDegree
end
DEFS(12): abbrev Cube, def sign, def average, def character, def fourierCoeff, def fourierDegree, def IsBoolean, def Nonconstant, def singletonSum, def absoluteSingletonSum, def SignedViolations, def AbsoluteRatios
## PAPER Unbounded-Violations-of-the-Square-Root-Degree-Bound-September-26-2026
ABSTRACT: We disprove the Gopalan--Servedio square-root conjecture, even up to an arbitrary constant factor. For every real \(C>0\), there is a nonconstant Boolean function \(f:\{-1,1\}^n\to\{-1,1\}\) on a finite sign cube such that \[ \sum_{i=1}^n \widehat f(\{i\})>C\sqrt{\deg(f)}. \] Here \(\widehat f(\{i\})\) is the linear Fourier coefficient associated with the \(i\)th input, and \(\deg(f)\) is the degree of the real multilinear polynomial representing \(f\).
[theorem] \label{thm:main} For every real \(C>0\), there are a positive integer \(n\) and a nonconstant Boolean function \(f:\{-1,1\}^n\to\{-1,1\}\) such that \[ \sum_{i=1}^n\widehat f(\{i\})>C\sqrt{\deg(f)}. \] Consequently, \[ \sup_{\substack{n\ge1,\ f:\{-1,1\}^n\to\{-1,1\}\\\deg(f)>0}} \frac{\sum_i|\widehat f(\{i\})|}{\sqrt{\deg(f)}}=\infty. \]
==================
# FAMILY 194: Lech’s multiplicity conjecture
SCOPE: Lech's multiplicity conjecture compares Hilbert–Samuel multiplicities across flat local maps. The linked formalization covers a supporting characteristic-$p$ comparison over a complete Noetherian local domain $D$: for a complex satisfying the stated short-complex and finite-length homology conditions, its Frobenius multiplicity sequence converges to its Dutta multiplicity, and the Hilbert–Samuel multiplicity of $D$ is at most that Dutta multiplicity. This selected statement is the complete-domain Dutta comparison. The paper's full flat-local result in arbitrary characteristic is outside it.
## CHALLENGE DuttaDomain  targets=['OAI.Lech.dutta_domain'] defs=[]
theorem dutta_domain : DuttaDomainClaim.{u} := by
  sorry
end Lech
end
end
DEFS(10): def dimension, def colength, def normalizedColength, def multiplicity, structure IsShortComplex, def frobeniusComplex, def shortEuler, def duttaSequence, def duttaMultiplicity, def DuttaDomainClaim
## PAPER Lechs-multiplicity-conjecture-September-23-2026
ABSTRACT: We prove Lech's multiplicity conjecture: Hilbert--Samuel multiplicity cannot decrease under a flat local homomorphism of nonzero Noetherian local rings. The result holds in arbitrary dimension, with no restrictions on the residue fields or characteristics.
[theorem[Lech's conjecture]] \label{thm:main} Let $(R,\mathfrak m)\longrightarrow(S,\mathfrak n)$ be a flat local homomorphism of nonzero Noetherian local rings. Then \[ e(R)\leq e(S). \] There is no restriction on the dimensions, the residue fields, or the characteristics of the rings.
==================
# FAMILY 195: A counterexample to the small Cohen–Macaulay module conjecture
SCOPE: The small Cohen–Macaulay module conjecture asks whether every complete Noetherian local domain has a nonzero finitely generated maximal Cohen–Macaulay module. The linked formalization verifies only the ring-theoretic candidate: there exists a three-dimensional complete Noetherian integrally closed local domain over $\mathbb C$ whose residue field is $\mathbb C$. The proof uses a constructed completed surface cone. The resulting existence statement gives only the ring properties above; it does not assert the absence of small Cohen–Macaulay modules. The paper's main counterexample requires that no nonzero finitely generated module over the ring has depth three. That conclusion, the numerical obstruction used to prove it, and the counterexample essentially of finite type are outside this comparison. The candidate's ring properties alone do not establish the counterexample.
## CHALLENGE SurfaceConeCandidateSupport  targets=['OAI.SmallCM.candidate_ring_properties'] defs=[]
theorem candidate_ring_properties :
    ∃ (R : Type) (_ : CommRing R) (_ : IsDomain R) (_ : IsNoetherianRing R)
      (_ : IsIntegrallyClosed R) (_ : IsLocalRing R) (_ : Algebra ℂ R),
      IsAdicComplete (IsLocalRing.maximalIdeal R) R ∧
      ringKrullDim R = 3 ∧
      Function.Bijective (algebraMap ℂ (IsLocalRing.ResidueField R)) := by
  sorry
end SmallCM
DEFS(0): 
## PAPER A-Complete-Local-Domain-Without-a-Small-Cohen-Macaulay-Module-September-23-2026
ABSTRACT: We construct a three-dimensional complete Noetherian normal local domain containing $\C$, with residue field $\C$, that has no nonzero finitely generated maximal Cohen--Macaulay module. This disproves the domain form of the small Cohen--Macaulay module conjecture.
[theorem] \label{thm:main} There exists a three-dimensional complete Noetherian normal local domain $R$ containing $\C$, with residue field $\C$, such that no nonzero finitely generated $R$-module has depth three.
==================
# FAMILY 196: A counterexample to Kaplansky’s zero-divisor conjecture
SCOPE: Kaplansky's zero-divisor conjecture asserts that the group algebra of a torsion-free group over a field has no zero divisors. The formalized result constructs a finitely presented torsion-free group $G$ and nonzero elements $\alpha,\beta\in\mathbb F_2[G]$ with $\alpha\beta=0$, giving a counterexample. The same group admits a finite two-dimensional classifying space $K(G,1)$.
## CHALLENGE TorsionFreeZeroDivisors  targets=['OAI.TorsionFreeZeroDivisors.main'] defs=[]
theorem main : MainTheorem := by
  sorry
end TorsionFreeZeroDivisors
DEFS(3): def TorsionFree, def HasFiniteTwoDimensionalClassifyingSpace, def MainTheorem
## PAPER A-Torsion-Free-Group-Algebra-with-Zero-Divisors-September-23-2026
ABSTRACT: We disprove Kaplansky's zero-divisor conjecture by constructing a finitely presented torsion-free group \(G\) for which \(\mathbb F_2[G]\) has nonzero zero divisors. The group admits a finite two-dimensional classifying space.
[theorem] \label{thm:main} There exist a finitely presented torsion-free group \(G\) and nonzero elements \(\alpha,\beta\in\mathbb F_2[G]\) such that \(\alpha\beta=0\). Moreover, \(G\) admits a finite two-dimensional classifying space.
==================
# FAMILY 197: A torsion-free group algebra that is not directly finite
SCOPE: Kaplansky's direct-finiteness conjecture asserts that $ab=1$ implies $ba=1$ for $a,b\in K[G]$, for every field $K$ and group $G$. The formalized results construct a finite field of characteristic two and a group algebra violating this implication. One statement records the counterexample for a finitely generated group; the more detailed construction gives a finitely presented group with an element of odd prime order. The detailed construction also gives a precise recipe for choosing the data and proves that the required search terminates. The further conclusion that the group is nonsofic is outside these statements. A nonsingular integer matrix has absolute determinant at least $1$. The group-ring Determinant Conjecture extends this bound to matrices over $\mathbb Z[G]$ for every discrete group $G$. If $T_A$ is the operator induced by such a matrix $A$ on finite direct sums of $\ell^2(G)
## CHALLENGE KaplanskyFinitelyPresented  targets=['OAI.KaplanskyCounterexample.finitelyPresented_counterexample'] defs=[]
theorem finitelyPresented_counterexample :
    ∃ (K : Type) (_ : Field K) (_ : Fintype K) (_ : CharP K 2),
      ∃ (G : Type) (_ : Group G) (_ : Group.IsFinitelyPresented G),
        (∃ (ℓ : ℕ) (_ : ℓ.Prime) (_ : Odd ℓ) (g : G), orderOf g = ℓ) ∧
        ∃ a_out b_out : MonoidAlgebra K G, a_out * b_out = 1 ∧ b_out * a_out ≠ 1 := by
  sorry
DEFS(0): 
## CHALLENGE KaplanskyDirectFiniteness  targets=['OAI.KaplanskyCounterexample.main_theorem'] defs=[]
theorem main_theorem : MainClaim := by
  sorry
end KaplanskyCounterexample
DEFS(1): def MainClaim
## CHALLENGE GroupRingDeterminant  targets=['OAI.GroupRingDeterminant.main'] defs=[]
theorem main : MainStatement := by
  sorry
end GroupRingDeterminant
end
DEFS(7): abbrev Hilbert, def identityVector, def groupTrace, def fkDet, def IsRegularOperator, def rationalMatrix, def MainStatement
## CHALLENGE OddKaplansky  targets=['OAI.OddKaplansky.main_theorem'] defs=[]
theorem main_theorem : MainClaim := by
  sorry
end
end OddKaplansky
DEFS(4): def sourceM, def sourcePrime, def cellular, def MainClaim
## PAPER A-Counterexample-to-Kaplanskys-Direct-Finiteness-Conjecture-in-Characteristic-Two-September-23-2026
ABSTRACT: We disprove Kaplansky's direct-finiteness conjecture by constructing a finite field $K$ of characteristic two, a finitely presented group $G$, and finite sums $a,b\in K[G]$ with $ab=1$ but $ba\ne1$. The group $G$ is nonsofic. The same elements define a cellular automaton on $K^G$ that is injective but not surjective, disproving Gottschalk's surjunctivity conjecture.
[theorem] \label{thm:main} There exist a finite field $K$ of characteristic two, a finitely presented group $G$ containing an element of odd prime order, and elements $a_{\mathrm{out}},b_{\mathrm{out}}\in K[G]$ such that \[ a_{\mathrm{out}}b_{\mathrm{out}}=1, \qquad b_{\mathrm{out}}a_{\mathrm{out}}\ne1. \] The field, group, and finite sums are specified by a terminating prescription involving finite sets and finite-field arithmetic.
## PAPER A-Counterexample-to-the-Group-Ring-Determinant-Conjecture-September-23-2026
ABSTRACT: We disprove the unrestricted group-ring Determinant Conjecture. We construct a finitely generated group $G$ and a square matrix over $\mathbb Z[G]$ that is invertible over $\mathbb Q[G]$ and has Fuglede--Kadison determinant strictly between zero and one. The logarithmic integral defining the determinant is finite.
[theorem] \label{thm:main} There are a finitely generated discrete group $G_D$, an integer $n\ge1$, and $A\in\Mat_n(\Z[G_D])$ invertible over $\Q[G_D]$ such that \[ 0<\det_{\N(G_D)}(T_A)<1. \] The integral in Equation~\eqref{eq:conjecture} is finite and strictly negative. Thus the unrestricted group-ring Determinant Conjecture has a negative resolution.
## PAPER A-Counterexample-to-Kaplanskys-Direct-Finiteness-Conjecture-in-Odd-Characteristic-September-26-2026
ABSTRACT: We construct a counterexample to Kaplansky's direct-finiteness conjecture in odd characteristic. For one specified odd prime $p$, we obtain a field $K$ of order $p^4$, a finitely generated group $G$ containing torsion, and finite sums $a,b\in K[G]$ with $ab=1$ but $ba\ne1$. The same elements define a cellular automaton on $K^G$ that is injective but not surjective.
[theorem] \label{op:main} Put \[ m=\binom{1200}{600},\qquad p=\min\{h\in\mathbb Z:h>1,\ h\mid(m!)^2+1\}. \] Then $p$ is an odd prime. There are a specified field $K$ of order $p^4$, a specified finitely generated group $G$ containing torsion, and specified finite sums $a,b\in K[G]$ satisfying $ab=1$ and $ba\ne1$.
==================
# FAMILY 198: A counterexample to finitistic-dimension finiteness
SCOPE: The little finitistic-dimension conjecture predicts that finitely generated modules of finite projective dimension over a fixed finite-dimensional algebra have bounded projective dimensions. The formalized counterexample is a finite-dimensional complex algebra with a finitely generated module of projective dimension at least $2m-2$ and still finite for every $m\ge1$. A separate formalized result gives a finite-dimensional complex algebra whose little and big finitistic dimensions are infinite on the left and zero on the right. Injectives fail to generate its unbounded derived category on the left and generate it on the right.
## CHALLENGE LittleFinitistic  targets=['OAI.LittleFinitistic.Main.exists_counterexample'] defs=[]
theorem exists_counterexample :
    ∃ (A : Type) (_ : Ring A) (_ : Algebra ℂ A),
      FiniteDimensional ℂ A ∧ littleFinitisticDimension A = ⊤ ∧
        ∀ m : ℕ, 0 < m → ∃ N : ModuleCat.{0} A, Module.Finite A N ∧
          ((2*m-2 : ℕ) : WithBot ℕ∞) ≤ projectiveDimension N ∧
            projectiveDimension N < ⊤ := by
  sorry
end Main
end LittleFinitistic
end
DEFS(1): def littleFinitisticDimension
## CHALLENGE FinitisticAsymmetry  targets=['OAI.LittleFinitistic.extreme_left_right_asymmetry'] defs=[]
theorem extreme_left_right_asymmetry :
    ∃ (Λ : Type) (_ : Ring Λ) (_ : Algebra ℂ Λ),
      FiniteDimensional ℂ Λ ∧
      littleFinitisticDimension Λ = ⊤ ∧ bigFinitisticDimension Λ = ⊤ ∧
      littleFinitisticDimension Λᵐᵒᵖ = 0 ∧ bigFinitisticDimension Λᵐᵒᵖ = 0 ∧
      ¬ InjectivesGenerate Λ ∧ InjectivesGenerate Λᵐᵒᵖ := by
  sorry
end LittleFinitistic
end
DEFS(3): def littleFinitisticDimension, def bigFinitisticDimension, def InjectivesGenerate
## PAPER An-algebra-of-infinite-little-finitistic-dimension-September-23-2026
ABSTRACT: We construct a finite-dimensional complex algebra whose finite-dimensional modules have unbounded finite projective dimensions. This disproves the little finitistic-dimension conjecture.
[theorem] \label{thm:main} There is a finite-dimensional unital complex algebra \(A\) such that, for every integer \(m\ge1\), there is a finite-dimensional left \(A\)-module \(N_m\) with \[ 2m-2\le\pd_A N_m<\infty. \] In particular, \(\findim A=\infty\).
==================
# FAMILY 199: Counterexamples to Auslander–Reiten, Tachikawa and related homological conjectures
SCOPE: The Auslander–Reiten conjecture predicts that a finitely generated module $M$ over an Artin algebra $A$ is projective if $\mathrm{Ext}^i_A(M,M\oplus A)=0$ for every $i>0$. The formalized counterexample is a finite-dimensional algebra over $k=\mathbb F_2(q,H_1,H_2)$ and a finite-dimensional nonprojective Gorenstein-projective module with this vanishing. It also establishes $A/\mathrm{rad}\,A\cong k^8$, $(\mathrm{rad}\,A)^4\ne0$, and preservation of the listed properties after every field extension. The Tachikawa companion is separate. Tachikawa's second conjecture predicts that a finite-dimensional module over a finite-dimensional self-injective algebra is projective if all its positive-degree self-Ext groups vanish. The formalized counterexample gives a finite-dimensional symmetric algebra over $\mathbb F_2(q,H_1,H_2)$ and a finite-dimensional nonprojective module $M$ with $\mathrm{Ext}^
## CHALLENGE AuslanderReiten  targets=['OAI.ArExplicit.Statement.main'] defs=[]
theorem main : FullStatement.{v} := by
  sorry
end ArExplicit.Statement
end
DEFS(6): abbrev K, def parameters, def TotallyAcyclicWitness, def Conclusions, structure System, def FullStatement
## CHALLENGE Tachikawa  targets=['OAI.Tachikawa.main_theorem'] defs=[]
theorem main_theorem : Counterexample := by
  sorry
end
end Tachikawa
DEFS(3): abbrev k, def SymmetricOver, def Counterexample
## PAPER An-explicit-counterexample-to-the-Auslander-Reiten-conjecture-September-23-2026
ABSTRACT: We disprove the Auslander--Reiten conjecture for Artin algebras. We construct a finite-dimensional algebra $\Lambda$ over $k=\mathbb F_2(q,H_1,H_2)$ and a finite-dimensional nonprojective left module $Z$ such that $\Ext^i_\Lambda(Z,Z)=\Ext^i_\Lambda(Z,\Lambda)=0$ for every $i>0$. The module is Gorenstein-projective, so the same example also disproves the Gorenstein-projective conjecture. Both counterexamples persist after every extension of $k$.
[theorem] \label{thm:main} Let $\kk=\mathbb F_2(q,H_1,H_2)$, where $q,H_1,H_2$ are algebraically independent. There exist a finite-dimensional $\kk$-algebra $\Lambda$ and a finite-dimensional nonprojective left $\Lambda$-module $Z$ such that \[ \Ext^i_\Lambda(Z,Z)=0=\Ext^i_\Lambda(Z,\Lambda) \qquad\text{for every integer }i\geq1. \] The module $Z$ is Gorenstein-projective. The semisimple quotient is $\Lambda/\rad\Lambda\simeq\kk^8$, so the algebra is split with eight isomorphism classes of simple modules; also $\rad(\Lambda)^4\ne0$. These conclusions persist after every field extension of $\kk$.
## PAPER A-counterexample-to-Tachikawas-second-conjecture-September-23-2026
ABSTRACT: We disprove Tachikawa's second conjecture by constructing a finite-dimensional symmetric algebra over $k=\mathbb F_2(q,H_1,H_2)$ with a finite-dimensional nonprojective module whose self-extension groups vanish in every positive degree. The associated endomorphism algebra also gives counterexamples to the classical, generalized, and strong Nakayama conjectures, the Auslander--Gorenstein conjecture, and the Wakamatsu tilting conjecture. These conclusions persist after every extension of $k$.
[theorem] \label{thm:main} Let \[ k=\mathbb F_2(q,H_1,H_2), \] where $q,H_1,H_2$ are algebraically independent. There exist a finite-dimensional associative unital symmetric $k$-algebra $A$ and a finite-dimensional unital left $A$-module $M$ such that $M$ is nonprojective and \[ \Ext_A^i(M,M)=0\qquad\text{for every integer }i>0. \] In particular, Tachikawa's second conjecture is false.
==================
# FAMILY 205: Saxl’s conjecture and universal tensor squares
SCOPE: The formalization proves the universal tensor-square conjecture for symmetric groups in the stated range. For every positive integer $n\notin\{2,4,9\}$, it constructs an irreducible complex representation of $S_n$ whose tensor square contains every irreducible complex representation of $S_n$. Equivalently, all corresponding Kronecker coefficients are positive. The statement also supplies injective intertwining maps for arbitrary finite-dimensional irreducible representations. Saxl's conjecture asserts that the tensor square of each staircase Specht module contains every irreducible representation of the corresponding symmetric group. The formalization establishes this for every $m\ge1$: if $\rho_m=(m,m-1,\ldots,1)$, then $g(\rho_m,\rho_m,\mu)>0$ for every partition $\mu$ of $m(m+1)/2$. The stronger claim that every constituent appears in the orbit span of one prescribed tensor is not inc
## CHALLENGE UniversalTensorSquares  targets=['OAI.UniversalTensorSquares.universal_tensor_square'] defs=[]
theorem universal_tensor_square
    (n : ℕ) (hn : 0 < n) (h2 : n ≠ 2) (h4 : n ≠ 4) (h9 : n ≠ 9) :
    ∃ (lam : YoungDiagram) (hlam : lam.card = n),
      (∀ (ν : YoungDiagram) (hν : ν.card = n),
        0 < Saxl.kronecker (Saxl.canonicalTableau lam hlam)
          (Saxl.canonicalTableau lam hlam) (Saxl.canonicalTableau ν hν)) ∧
      Representation.IsIrreducible (Saxl.spechtRep (Saxl.canonicalTableau lam hlam)) ∧
      ∀ (V : Type u) [AddCommGroup V] [Module ℂ V] [Module.Finite ℂ V]
        (ρ : Representation ℂ (Equiv.Perm (Fin n)) V) [Representation.IsIrreducible ρ],
        ∃ F : Representation.IntertwiningMap ρ
          ((Saxl.spechtRep (Saxl.canonicalTableau lam hlam)).tprod
            (Saxl.spechtRep (Saxl.canonicalTableau lam hlam))),
          Function.Injective F := by
  sorry
end UniversalTensorSquares
end
DEFS(12): abbrev WordSpace, def wordRep, def cyclic, abbrev Tableau, def canonicalTableau, def rowWord, def columnGroup, def polytabloid, def spechtSub, abbrev Specht, def spechtRep, def kronecker
## CHALLENGE Saxl  targets=['OAI.Saxl.saxl_conjecture'] defs=[]
theorem saxl_conjecture : SaxlConjecture := by
  sorry
end Saxl
end
DEFS(14): abbrev WordSpace, def wordRep, def cyclic, abbrev Tableau, def canonicalTableau, def rowWord, def columnGroup, def polytabloid, def spechtSub, abbrev Specht, def spechtRep, def kronecker, def staircase, def SaxlConjecture
## PAPER Universal-Tensor-Squares-for-Symmetric-Groups-September-24-2026
ABSTRACT: For every positive integer $n$ other than $2$, $4$, and $9$, we prove that some irreducible complex representation of $S_n$ has a tensor square containing every irreducible representation. This resolves the tensor square conjecture for symmetric groups affirmatively.
[theorem] \label{thm:main} For every positive integer $n\notin\{2,4,9\}$ there is a partition $\lambda\vdash n$ such that \[ g(\lambda,\lambda,\nu)>0\qquad\text{for every }\nu\vdash n. \] Thus one irreducible representation has a tensor square containing every irreducible representation of $S_n$.
## PAPER A-Cyclic-Polytabloid-Proof-of-Saxls-Conjecture-September-24-2026
ABSTRACT: For every staircase partition, we prove that the tensor square of the corresponding irreducible complex representation of the symmetric group contains every irreducible representation of that group. This proves Saxl's conjecture.
[theorem[Saxl's conjecture]] \label{thm:saxl} For every integer $m\ge1$ and every partition $\lambda\vdash N_m$, \[ g(\rho_m,\rho_m,\lambda)>0. \] Equivalently, $S^{\rho_m}\otimes S^{\rho_m}$ contains every irreducible complex representation of $S_{N_m}$.
==================
# FAMILY 206: Finite lattice representation and undecidability
SCOPE: The finite lattice representation problem asks which finite lattices occur as the full congruence lattice of a finite algebra. The formalization proves the paper's colored-graph characterization: a finite nonempty lattice is representable exactly when it admits the specified finite nonempty graph witness, whose edge colors encode the required congruence relations. This selected theorem is the equivalence with the graph criterion; the paper's undecidability and subgroup-interval conclusions are outside it.
## CHALLENGE FiniteCongruenceGraph  targets=['OAI.FiniteCongruence.graph_criterion'] defs=None
theorem graph_criterion (Lat : Type) [Fintype Lat] [Lattice Lat] [OrderBot Lat] :
    Representable Lat ↔ HasGraphWitness Lat := by
  sorry
end FiniteCongruence
DEFS(9): structure Algebra, def Compatible, def Congruence, def Representable, def Admissible, def Marked, def Connected, def IsGraphWitness, def HasGraphWitness
## PAPER Finite-Congruence-Lattices-Characterization-and-Undecidability-September-24-2026
ABSTRACT: We give an explicit colored-graph characterization of the finite nonempty lattices that occur as full congruence lattices of finite algebras, and prove that deciding this representation property is undecidable. In particular, the finite lattice representation problem has a negative answer. We also prove that recognition of full subgroup intervals in finite groups is undecidable.
[theorem] \label{m:main} The following statements hold. \begin{enumerate}[label=\textup{(\roman*)}] \item A finite nonempty lattice is representable if and only if it satisfies the finite colored-graph criterion in \Cref{f:criterion}. For each candidate graph size the criterion is decidable by a finite test. \item There is no deterministic Turing machine that, given the order table of a finite nonempty lattice, always halts and decides \(\mathcal R(L)\). \item There is a nonrepresentable finite lattice \(L_0\) of minimum cardinality, specified by the finite formulas in \Cref{sec:minimum}. Every finite lattice of smaller cardinality is representable, and \(\lvert L_0\rvert>7\). \item Given the order ta
==================
# FAMILY 207: The ℓ¹-Bass conjecture for all discrete groups
SCOPE: The formalization proves the complex Bass trace conjecture for every group: the Hattori–Stallings trace of each virtual class of finitely generated projective right $\mathbb C[G]$-modules vanishes on conjugacy classes of infinite-order elements. No finiteness, countability, or geometric hypothesis on $G$ is imposed. For torsion-free $G$, it identifies the trace on $K_0(\mathbb C[G])$ with the integral augmentation rank and proves the characteristic-zero Kaplansky idempotent conjecture: for every commutative unital domain $R$ of characteristic zero, an idempotent in $R[G]$ is $0$ or $1$.
## CHALLENGE BassTrace  targets=['OAI.BassTrace.RightProjective.bassTraceModules_vanishing_and_support'] defs=[]
theorem bassTraceModules_vanishing_and_support {G : Type u} [_root_.Group G]
    (x : ModuleK0.{u,v} (MonoidAlgebra ℂ G)) :
    (∀ g : G, ¬IsOfFinOrder g → HattoriStallings x (ConjClasses.mk g) = 0) ∧
      ↑(HattoriStallings x).support ⊆
        {c | ∃ g : G, IsOfFinOrder g ∧ ConjClasses.mk g = c} :=
  by sorry
end RightProjective
end BassTrace
end
DEFS(31): def classCoefficient, structure Idempotent, def directSum, def relationGenerators, def relations, instance relations_normal, abbrev Group, def classOf, instance groupRingRelations_normal, def rawCoefficient, def classTrace, def rawTrace, def HattoriStallings, instance rightModuleIdentityRingHomInvPair, def unopTranspose, def rightMatrix, structure Retraction, def Retraction.idempotent, def Retraction.transport, def freeSplit, def Retraction.prod, structure Object, def Object.prod, def Object.retraction, def Object.presentationClass, def moduleRelationGenerators, def moduleRelations, abbrev ModuleK0, def rawPresentation, def presentation
## CHALLENGE BassTorsionFree  targets=['OAI.TorsionFreeBass.torsion_free_corollary'] defs=[]
theorem torsion_free_corollary (G : Type*) [Group G] (hG : TorsionFree G) :
    ((∀ (q : ℕ), 1 ≤ q →
      ∀ e : Matrix (Fin q) (Fin q) (MonoidAlgebra ℂ G), e ^ 2 = e →
        matrixTrace e = ((augmentedMatrix e).rank : ℂ)) ∧
      traceK0 (G := G) = (Int.castAddHom ℂ).comp augmentationRank ∧
      Set.range (traceK0 (G := G)) = Set.range (fun z : ℤ => (z : ℂ))) ∧
    (∀ (R : Type*) [CommRing R] [IsDomain R] [CharZero R]
      (e : MonoidAlgebra R G), e ^ 2 = e → e = 0 ∨ e = 1) := by
  sorry
end TorsionFreeBass
end
DEFS(34): def classCoefficient, theorem classCoefficient_zero, theorem classCoefficient_single, theorem classCoefficient_add, theorem classCoefficient_smul, theorem classCoefficient_sum, theorem classCoefficient_mul_comm, theorem classCoefficient_matrix_mul_comm, structure Idempotent, def directSum, def relationGenerators, def relations, instance relations_normal, abbrev Group, instance groupRingRelations_normal, def rawCoefficient, lemma trace_reindex, lemma trace_directSum, lemma relations_in_kernel, def hsCoefficient, def TorsionFree, def augmentation, def canonicalTrace, def matrixTrace, def augmentedMatrix, lemma augmentedMatrix_mul, lemma augmentedMatrix_trace, lemma idempotent_matrix_trace_eq_rank, def rawAugmentationRank, lemma rawAugmentationRank_of
## PAPER The-Bass-trace-conjecture-for-complex-group-rings-September-24-2026
ABSTRACT: We prove the complex group-ring Bass trace conjecture for every discrete group: the Hattori--Stallings trace of a finitely generated projective module over its complex group ring is supported on conjugacy classes of finite-order elements. As a consequence, for every torsion-free group $G$ and every commutative unital domain $R$ of characteristic zero, the only idempotents in $RG$ are $0$ and $1$. This proves Kaplansky's idempotent conjecture in characteristic zero.
[theorem] \label{thm:bass} Let $G$ be any discrete group. For every $x\in K_0(\C G)$ and every infinite-order element $g\in G$, \[ \HS_G(x)([g]_G)=0. \] Equivalently, if $\con_{\mathrm{fin}}(G)$ denotes the conjugacy classes of finite-order elements, then \[ \HS_G\bigl(K_0(\C G)\bigr) \subseteq\bigoplus_{C\in\con_{\mathrm{fin}}(G)}\C C. \]
==================
# FAMILY 210: Foulkes' conjecture for sixth powers and quadratic stabilization
SCOPE: The formalized result proves surjectivity of the canonical averaged Foulkes–Howe map $\mathrm{Sym}^b(\mathrm{Sym}^a\,V)\to\mathrm{Sym}^a(\mathrm{Sym}^b\,V)$ for every finite-dimensional complex vector space, $a\ge2$, and $b\ge a(a-1)$. It also covers the bijective $a=1$ case, the vanishing-on-products consequence, and the corresponding equivariant embedding in the reverse direction. The sixth-power specialization is covered for $b\ge30$; the companion's full range $b\ge6$ is not included.
## CHALLENGE FoulkesHowe  targets=['OAI.Problem346.canonical_foulkes_howe_surjective'] defs=[]
theorem canonical_foulkes_howe_surjective :
    ∀ (V : Type u) [AddCommGroup V] [Module ℂ V] [FiniteDimensional ℂ V] (a b : ℕ), 2 ≤ a → a * (a - 1) ≤ b → ∃ μ : SymPow b (SymPow a V) →ₗ[ℂ] SymPow a (SymPow b V), IsFoulkesMap a b V μ ∧ Function.Surjective μ ∧ ∀ ν : SymPow b (SymPow a V) →ₗ[ℂ] SymPow a (SymPow b V), IsFoulkesMap a b V ν → ν = μ := by
  sorry
end Problem346
end
DEFS(6): def symMonomialRaw, def symPowSubmodule, abbrev SymPow, def symMonomial, def foulkesFormula, def IsFoulkesMap
## PAPER Quadratic-Stabilization-of-the-Canonical-Foulkes-Howe-Map-September-25-2026
ABSTRACT: For every finite-dimensional complex vector space $V$, we prove that the canonical Foulkes--Howe map $\Sym^b(\Sym^a V)\longrightarrow\Sym^a(\Sym^b V)$ is surjective whenever $a\ge2$ and $b\ge a(a-1)$. This gives a quadratic stabilization bound independent of $\dim V$.
[theorem] \label{thm:main} For every integer $a\ge2$, every integer $b\ge a(a-1)$, and every finite-dimensional complex vector space $V$, the map $\mu_{a,b,V}$ in \eqref{eq:map} is surjective. Equivalently, $A_b=R_b$.
==================
# FAMILY 211: The geometric phase diagram, diffusion, and spectra of random planar maps
SCOPE: For every fixed $q>4$, the formalization proves the Brownian continuum-random-tree limit for critical finite Fortuin–Kasteleyn planar maps. After rescaling graph distances in an $n$-edge map by a constant depending on $q$ times $n^{-1/2}$ and using normalized degree measure, the metric-measure space converges in distribution to the Brownian continuum random tree in the Gromov–Hausdorff–Prokhorov topology. The convergence holds through all positive integer sizes.
## CHALLENGE FKCRT  targets=['OAI.FKCRT.finite_fk_maps_converge_to_brownian_crt'] defs=[]
theorem finite_fk_maps_converge_to_brownian_crt : MainStatement := by
  sorry
end FKCRT
end
DEFS(32): abbrev Dart, abbrev Orbit, def orbit, def spanningGraph, def MapConditions, abbrev LabelledMap, def MapIso, abbrev RootedMap, def reversal, def rotation, abbrev Vertex, abbrev Edge, def graph, def clusterCount, def fkWeight, def partition, structure MetricMeasureData, def MetricMeasureData.Valid, def degreeMass, def mapSpace, def Amalgamates, def ambientCost, def ghpEDist, def IsGHPTest, def excursionDist, abbrev ExcursionTree, def treeProjection, def treeSpace, def standardExcursion, def finiteExpectation
## PAPER Brownian-continuum-random-tree-limits-of-finite-Fortuin-Kasteleyn-maps-above-four-September-24-2026
ABSTRACT: We prove the finite-volume continuum-random-tree prediction for critical Fortuin--Kasteleyn planar maps at every fixed $q>4$. After rescaling graph distances by a constant times $n^{-1/2}$, an $n$-edge map with normalized degree measure converges to the Brownian continuum random tree in the Gromov--Hausdorff--Prokhorov topology. The convergence holds through all positive integer sizes.
[theorem] \label{thm:main} For every fixed real $q>4$, there is a deterministic constant $c(q)\in(0,\infty)$ such that, as $n\to\infty$ through all positive integers, \[ \big(V(M_n),c(q)n^{-1/2}d_n,\mu_n\big) \ \Longrightarrow\ (\mathcal T_e,d_e,\mu_e) \] in the Gromov--Hausdorff--Prokhorov topology on compact metric probability spaces modulo measure-preserving isometry.
==================
# FAMILY 212: Planar first-passage geometry and the absence of bigeodesics
SCOPE: The formalization proves differentiability of the planar first-passage time-constant norm for independent Gamma edge weights of every positive shape and rate. The norm is differentiable away from the origin, and its unit sphere has a $C^1$ boundary. This includes the exponential model, for which the linked statement also gives a unique supporting line at every boundary point. The paper also claims strict convexity for the exponential limit shape. Strict convexity is outside these selected differentiability statements.
## CHALLENGE PlanarFirstPassage  targets=['OAI.PlanarFPP.manuscriptMain'] defs=[]
theorem manuscriptMain (Ω : Type) [MeasurableSpace Ω] (P : Measure Ω) (τ : Edge → Ω → ℝ)
    (henv : ExponentialEnvironment P τ) :
    ∃ μ : Plane → ℝ, TimeConstantNorm μ ∧ IsTimeConstant P τ μ ∧
      DifferentiableAwayFromOrigin μ ∧ UniqueNormalizedSupports μ ∧ C1UnitSphere μ ∧
      (∀ v ∈ frontier {z | μ z ≤ 1}, ∃! L : Set Plane,
        ∃ g : Plane →L[ℝ] ℝ, g ≠ 0 ∧ (∀ z, μ z ≤ 1 → g z ≤ g v) ∧ L={z | g z=g v}) ∧
      (∀ v ∈ frontier {z | μ z ≤ 1}, HasC1CurveChart (frontier {z | μ z ≤ 1}) v) := by
  sorry
end PlanarFPP
DEFS(17): abbrev Vertex, abbrev Edge, inductive Step, def Step.delta, def Step.edge, def displacement, def pathCost, abbrev Plane, def latticeFloor, def passageTime, structure TimeConstantNorm, structure ExponentialEnvironment, def IsTimeConstant, def DifferentiableAwayFromOrigin, def UniqueNormalizedSupports, def C1UnitSphere, def HasC1CurveChart
## CHALLENGE GammaPassage  targets=['OAI.GammaFPP.gamma_differentiability'] defs=[]
theorem gamma_differentiability : GammaDifferentiabilityTarget := by
  sorry
end GammaFPP
DEFS(17): abbrev Vertex, abbrev Edge, inductive Step, def Step.delta, def Step.edge, def displacement, def pathCost, abbrev Plane, def latticeFloor, def passageTime, structure TimeConstantNorm, def IsTimeConstant, def DifferentiableAwayFromOrigin, structure IidEnvironment, abbrev GammaEnvironment, def HasC1CurveChart, def GammaDifferentiabilityTarget
## PAPER Strict-convexity-and-differentiability-of-the-planar-exponential-first-passage-limit-shape-September-24-2026
ABSTRACT: We prove that the limit shape of undirected nearest-neighbor first-passage percolation on $\Z^2$ with independent exponential edge weights is strictly convex and has a $C^1$ boundary. This resolves the strict convexity and differentiability conjectures for the planar exponential model. More generally, we prove differentiability of the time-constant norm for every Gamma edge-weight law with positive shape and rate.
[theorem[The exponential limit shape]] \label{thm:exponential-shape} For independent exponential edge weights of any rate $\lambda>0$, the norm $\mu$ is Fr\'echet differentiable on $\R^2\setminus\{0\}$, and its unit ball is strictly convex. In particular, \[ \mu((1-t)x+ty)<1 \quad\text{if }x,y\in\partial\Bcal,\ x\ne y,\ 0<t<1, \] and $\partial\Bcal$ is a $C^1$ curve with a unique supporting line at every point.
==================
# FAMILY 213: Critical percolation on every quasi-transitive graph
SCOPE: The critical-percolation question asks whether an infinite cluster can remain at the threshold. The formalized result proves that, at their respective critical probabilities, nearest-neighbor bond and site percolation on $\mathbb Z^3$ almost surely have no infinite cluster. Equivalently, almost surely every vertex belongs to a finite cluster in each model. The formalization proves absence of an infinite cluster at criticality for Bernoulli bond percolation on every infinite connected locally finite quasi-transitive graph with critical probability $p_c<1$. At $p=p_c$, the probability that any infinite cluster exists is zero. The graph model permits bond multiplicities.
## CHALLENGE CriticalZ3  targets=['OAI.CriticalZ3.critical_no_infinite'] defs=[]
theorem critical_no_infinite :
    (∀ᵐ ω ∂bondLaw bondCritical, ∀ x : Vertex, (bondCluster ω x).Finite) ∧
    (∀ᵐ ω ∂siteLaw siteCritical, ∀ x : Vertex, (siteCluster ω x).Finite) := by
  sorry
end CriticalZ3
DEFS(19): abbrev Vertex, abbrev Bond, abbrev BondConfig, abbrev SiteConfig, def step, def NearestNeighbor, def BondOpen, def SiteOpen, def BondConnected, def SiteConnected, def bondCluster, def siteCluster, def bondInfiniteAt, def siteInfiniteAt, def parameter, def bondLaw, def siteLaw, def bondCritical, def siteCritical
## CHALLENGE CriticalPercolation  targets=['OAI.CriticalPercolation.BondGraph.no_percolation_at_criticality'] defs=[]
theorem no_percolation_at_criticality [Infinite V]
    (hconnected : G.fullGraph.Connected)
    (hlocal : G.LocallyFinite)
    (hquasi : G.QuasiTransitive)
    (hpc : G.criticalProbability < 1) :
    G.law G.criticalProbability G.percolates = 0 := by
  sorry
end BondGraph
end CriticalPercolation
DEFS(10): structure BondGraph, def openGraph, def fullGraph, def LocallyFinite, structure Aut, def QuasiTransitive, def cluster, def percolates, def law, def criticalProbability
## PAPER Critical-bond-and-site-percolation-on-the-cubic-lattice-September-24-2026
ABSTRACT: We prove that nearest-neighbor Bernoulli bond and site percolation on $\mathbb Z^3$ have no infinite cluster at their respective critical parameters. The proof combines a finite connection inequality for independent hyperedges with a finite-scale extension estimate and an adaptive exploration.
[theorem] \label{thm:main} For nearest-neighbor Bernoulli bond percolation on $\mathbb Z^3$, there is almost surely no infinite open cluster at the bond critical parameter. The same assertion holds for nearest-neighbor Bernoulli site percolation at the site critical parameter.
## PAPER No-percolation-at-criticality-on-quasi-transitive-graphs-September-24-2026
ABSTRACT: We prove that critical Bernoulli bond percolation has no infinite cluster on any infinite connected locally finite quasi-transitive graph with critical probability less than one. This resolves the bond form of the criticality conjecture of Benjamini and Schramm.
[theorem] \label{thm:main} Let $G$ be an infinite connected locally finite quasi-transitive undirected graph. If $\pc(G)<1$, then \[ \PP_{\pc(G)}(\text{there is an infinite open cluster})=0. \] Equivalently, $\PP_{\pc(G)}(|C_x|=\infty)=0$ for every vertex $x$.
==================
# FAMILY 214: The Benjamini–Schramm nonuniqueness conjecture
SCOPE: The formalization proves the nonuniqueness phase conjecture for Bernoulli bond percolation on infinite connected locally finite nonamenable quasi-transitive graphs. It establishes $p_c<p_{2\to2}\le p_u$ and a common nonempty coupled interval with infinitely many infinite clusters almost surely. For Cayley graphs, the result holds for every finite symmetric generating set of a nonamenable finitely generated group and every $p\in(p_c,p_u)$. The selected critical estimates include a finite triangle diagram, susceptibility of order $(p_c-p)^{-1}$, percolation probability of order $p-p_c$, cluster-volume tail of order $n^{-1/2}$, and intrinsic and extrinsic radius tails of order $n^{-1}$. Connection probabilities decay exponentially below $p_{2\to2}$.
## CHALLENGE BenjaminiSchramm  targets=['OAI.Percolation.BenjaminiSchramm.full_main', 'OAI.Percolation.BenjaminiSchramm.cayley_main', 'OAI.Percolation.BenjaminiSchramm.critical_laws'] defs=[]
theorem full_main {V : Type u} {E : Type v} [Infinite V]
    (G : BondGraph V E) (hc : Connected G) (hl : LocallyFinite G)
    (hq : QuasiTransitive G) (hh : 0 < hV G) : MainConclusion G := by
  sorry
/-- Critical mean-field laws and uniform exponential connectivity below the operator threshold. -/
theorem critical_laws {V : Type u} {E : Type v} [Infinite V]
    (G : BondGraph V E) (hc : Connected G) (hl : LocallyFinite G)
    (hq : QuasiTransitive G) (hh : 0 < hV G) : CriticalLawsConclusion G := by
  sorry
/-- Nonuniqueness for every prescribed finite symmetric Cayley generating set. -/
theorem cayley_main {Λ : Type u} [Group Λ]
    (S : Finset Λ) (hsym : ∀ s ∈ S, s⁻¹ ∈ S) (_hone : 1 ∉ S)
    (hgen : Subgroup.closure (S : Set Λ) = ⊤) (hna : ¬ FolnerAmenable Λ) :
    OperatorBounded (cayleyBond S) (pc (cayleyBond S)) ∧
      MainConclusion (cayleyBond S) ∧
      ∀ p : unitInterval, pc (cayleyBond S) < p → p < pu (cayleyBond S) →
        ∀ᵐ ω ∂law p, (infiniteClusters (cayleyBond S) ω).Infinite := by
  sorry
end Percolation.BenjaminiSchramm
DEFS(42): abbrev BondGraph, def Adj, def LocallyFinite, def Connected, def IsAut, def QuasiTransitive, def vertexBoundary, def hV, def Conn, def cluster, def infiniteClusters, def law, def pc, def pu, def twoPoint, abbrev Hilbert, def HasKernel, def OperatorBounded, def operatorNorm, def ptwo, def labelLaw, def openEdges, def MainConclusion, def openSimpleGraph, def susceptibility, def triangleDiagram, def graphDistance, def ExponentialDecay, def pexp, def PowerTail
## CHALLENGE CayleyPercolation  targets=['OAI.Percolation.arbitrary_cayley'] defs=[]
theorem arbitrary_cayley {Λ : Type u} [Group Λ] [Group.FG Λ]
    (hna : ¬ AmenableGroup Λ) (S : Finset Λ)
    (hsym : ∀ s ∈ S, s⁻¹ ∈ S) (hgen : Subgroup.closure (S : Set Λ) = ⊤)
    (h1 : 1 ∉ S) :
    OperatorBounded (cayleyGraph S) (pc (cayleyGraph S)) ∧
    pc (cayleyGraph S) < ptwo (cayleyGraph S) ∧
    ptwo (cayleyGraph S) ≤ pu (cayleyGraph S) ∧
    (∃ p₁ p₂ : unitInterval, pc (cayleyGraph S) < p₁ ∧ p₁ < p₂ ∧ p₂ < 1 ∧
      ∀ᵐ labels ∂(labelLaw : Measure (CayleyEdge S → unitInterval)),
        ∀ p ∈ Set.Icc p₁ p₂, (infiniteClusters (cayleyGraph S) (openEdges labels p)).Infinite) ∧
    (∀ p : unitInterval, pc (cayleyGraph S) < p → p < pu (cayleyGraph S) →
      ∀ᵐ ω ∂law p, (infiniteClusters (cayleyGraph S) ω).Infinite) := by
  sorry
end Percolation
DEFS(17): abbrev BondGraph, def Conn, def cluster, def infiniteClusters, def law, def pc, def pu, def twoPoint, abbrev Hilbert, def HasKernel, def OperatorBounded, def ptwo, def labelLaw, def openEdges, def AmenableGroup, def CayleyEdge, def cayleyGraph
## PAPER Nonuniqueness-of-percolation-on-nonamenable-quasi-transitive-graphs-September-24-2026
ABSTRACT: We prove the bond-percolation nonuniqueness conjecture of Benjamini and Schramm: every infinite connected, locally finite, nonamenable quasi-transitive graph has a nonempty interval of parameters for which Bernoulli bond percolation almost surely has infinitely many infinite clusters. We also prove Hutchcroft's stronger operator-threshold conjecture, establishing $p_c<p_{2\to2}\le p_u$.
[theorem] \label{thm:main} Let $G$ be an infinite connected locally finite quasi-transitive graph with $h_V(G)>0$. For Bernoulli bond percolation on $G$, \[ \sup_{0\le p<\pc}\norm{T_p}_{2\to2} =\norm{T_{\pc}}_{2\to2}<\infty, \qquad \pc(G)<\ptwo(G)\le\pu(G). \] There exist $\pc<p_1<p_2<1$ such that, in the coupling obtained from independent uniform edge labels, almost surely there are infinitely many infinite open clusters simultaneously for every $p\in[p_1,p_2]$.
==================
# FAMILY 215: Canonical $`O(3)`$ continuum limit and exact $`O(4)`$ mass asymptotics
SCOPE: The formalized result proves exponential decay of spin correlations for the two-dimensional classical $O(n)$ model at every temperature when $n\ge3$. For each interaction bound $\beta>0$, constants $A$ and $m>0$ work for every finite square-lattice subgraph with free boundary and nonnegative edge strengths at most $\beta$: the correlation between sites $x,y$ is at most $Ae^{-m|x-y|}$. The infinite-volume limit and the separate $O(4)$ spectral-gap claim are not included.
## CHALLENGE ClassicalON  targets=['OAI.ClassicalON.main'] defs=[]
theorem main : ExponentialDecay := by
  sorry
end ClassicalON
end
DEFS(12): abbrev Site, def PositiveNeighbor, structure LatticeGraph, abbrev Spin, abbrev Configuration, def sphereProbability, def referenceLaw, def interaction, def partition, def correlation, def siteDistance, def ExponentialDecay
## PAPER Exponential-decay-in-two-dimensional-classical-On-models-September-23-2026
ABSTRACT: We prove exponential decay of two-point correlations for the classical nearest-neighbor $O(n)$ model on the square lattice, for every $n\ge3$ and every finite positive inverse temperature. The estimate is uniform over finite free-boundary subgraphs and bounded nonnegative edge strengths. This resolves positively the all-temperature exponential spin-decay conjecture for these models.
[theorem] \label{thm:main} For every integer $n\ge3$ and every finite $\beta>0$, there are constants $A=A(n,\beta)<\infty$ and $m=m(n,\beta)>0$ such that, for every finite nearest-neighbor square-lattice subgraph $G$, every strength array $b\in[0,\beta]^E$, and all $x,y\in V$, \begin{equation} 0\le \langle\sigma_x\cdot\sigma_y\rangle_{G,b}^{(n)} \le A\exp(-m\|x-y\|_2). \label{eq:main-bound} \end{equation}
==================
# FAMILY 218: Conformal universality for weakly interacting and random-bond Ising models
SCOPE: The formalized result compares conditional Ising probabilities on finite graphs when two boundary mixtures differ but a common set of spins is pinned. If $q_0$ is the associated zero-field Fortuin–Kasteleyn connection probability after deleting the pinned vertices, the likelihood ratio lies between $\exp(-4\mathrm{artanh}\,q_0)$ and $\exp(4\mathrm{artanh}\,q_0)$. The statement allows arbitrary external fields and arbitrary probability mixtures satisfying the stated disjointness conditions. The paper's finite stopping-band approximation theorem is outside this selected statement.
## CHALLENGE BufferedIsing  targets=['OAI.BufferedIsing.finite_graph_comparison'] defs=[]
theorem finite_graph_comparison {n m : ℕ} (G : FiniteGraph n m)
    (h : Fin n → ℝ) (I J F : Finset (Fin n))
    (hIJ : Disjoint I J) (hIF : Disjoint I F) (hJF : Disjoint J F)
    (i j : KeptVertex F) (hi : i.val ∈ I) (hj : j.val ∈ J)
    (a τ : Spins n) (mix mix' : Spins n → ℝ)
    (hmix : ∀ b, 0 ≤ mix b) (hmix' : ∀ b, 0 ≤ mix' b)
    (hmixsum : ∑ b, mix b = 1) (hmix'sum : ∑ b, mix' b = 1) :
    Real.exp (-4 * Real.artanh (qZero G I J F i j)) ≤
        mixtureProb G h I J F a τ mix / mixtureProb G h I J F a τ mix' ∧
      mixtureProb G h I J F a τ mix / mixtureProb G h I J F a τ mix' ≤
        Real.exp (4 * Real.artanh (qZero G I J F i j)) := by
  sorry
end BufferedIsing
DEFS(16): structure FiniteGraph, abbrev Spins, def spin, def energy, def weight, def AgreesOn, def constrainedSum, def conditionalProb, def keptEdges, abbrev KeptVertex, def comparisonRel, def comparisonSetoid, def clusterCount, def fkWeight, def qZero, def mixtureProb
## PAPER Buffered-comparison-and-stopping-band-resolution-in-critical-Ising-September-23-2026
ABSTRACT: We prove pointwise comparison and finite stopping-band approximation theorems for the critical nearest-neighbor Ising model on the square lattice. Arbitrary common pinned spins are allowed in the comparison: the likelihood ratio is controlled by a zero-field FK connection probability on the graph with those vertices deleted. For an interface exploration across a band of fixed positive width, finitely many regular signed barriers approximate every good conditional target law in total variation, uniformly over bounded observables and sufficiently fine meshes.
[theorem[Finite-graph comparison]] \label{in:comparison} For every two configurations $b,b'$ on $J$ and every configuration $a$ on $I$, \[ e^{-4\operatorname{arctanh}q_0} \leq \frac{\mu(\sigma_I=a\mid\sigma_J=b,\sigma_F)} {\mu(\sigma_I=a\mid\sigma_J=b',\sigma_F)} \leq e^{4\operatorname{arctanh}q_0}. \] Either conditional law may be replaced by an arbitrary mixture of these laws. The bound is symmetric in the two terminal sets.
==================
# FAMILY 220: Directional zero–one laws beyond iid environments and iid ballisticity
SCOPE: The directional zero–one conjecture asks whether a random walk's probability of escape in a fixed direction must be zero or one. The formalization proves this for nearest-neighbor walks in independent identically distributed strictly elliptic environments on $\mathbb Z^d$, for every $d\ge3$ and every nonzero real direction. Strict ellipticity means that every allowed transition probability is positive almost surely; no uniform positive lower bound or moment condition is assumed. The probability is the annealed law from the origin. For an i.i.d. uniformly elliptic nearest-neighbor random environment on $\mathbb Z^d$, the formalization proves that almost-sure directional transience implies convergence of $X_n/n$ to a deterministic velocity with positive projection in that direction for every $d\ge2$. For $d\ge3$, positive probability of transience in any nonzero direction already suffices.
## CHALLENGE DirectionalWalk  targets=['OAI.DirectionalZeroOne.directional_zero_one'] defs=[]
theorem directional_zero_one (d : ℕ) (hd : 3 ≤ d)
    (μ : Measure (Row d)) [IsProbabilityMeasure μ]
    (hell : StrictEllipticity μ) (ℓ : Fin d → ℝ) (hℓ : ℓ ≠ 0) :
    annealed μ 0 (escape ℓ) = 0 ∨ annealed μ 0 (escape ℓ) = 1 := by sorry
end DirectionalZeroOne
DEFS(14): abbrev Site, abbrev Step, def stepVector, def Row, abbrev Environment, abbrev Path, abbrev State, def StrictEllipticity, def environmentLaw, def transition, def historyKernel, def initialLaw, def annealed, def escape
## CHALLENGE DirectionalBallisticity  targets=['OAI.DirectionalTransience.directional_transience_implies_ballisticity'] defs=[]
theorem directional_transience_implies_ballisticity : MainStatement := by
  sorry
end DirectionalTransience
DEFS(22): abbrev Lattice, abbrev Direction, abbrev Vector, abbrev Row, abbrev Environment, abbrev State, abbrev Path, def step, def environmentLaw, def UniformElliptic, lemma measurable_current_row, def transition, instance transition_markov, def historyTransition, instance historyTransition_markov, def initialLaw, def annealedLaw, def dot, def realPosition, def DirectionallyTransient, def HasVelocity, def MainStatement
## CHALLENGE VelocityHemisphere  targets=['OAI.DirectionalTransience.positive_probability_transience_velocity_hemisphere'] defs=[]
theorem positive_probability_transience_velocity_hemisphere
    {d : ℕ} (hd : 3 ≤ d) (ν : Measure (Row d)) [IsProbabilityMeasure ν]
    (hue : UniformElliptic ν) (ℓ : Vector d) (hℓ : ℓ ≠ 0)
    (hpos : 0 < annealedLaw ν (TransientPaths ℓ)) :
    ∃ v : Vector d,
      v ≠ 0 ∧ 0 < dot v ℓ ∧ annealedLaw ν (VelocityPaths v) = 1 ∧
      (∀ w : Vector d, annealedLaw ν (VelocityPaths w) = 1 → w = v) ∧
      {u : Vector d | dot u u = 1 ∧ annealedLaw ν (TransientPaths u) = 1} =
        {u : Vector d | dot u u = 1 ∧ 0 < annealedLaw ν (TransientPaths u)} ∧
      {u : Vector d | dot u u = 1 ∧ 0 < annealedLaw ν (TransientPaths u)} =
        {u : Vector d | dot u u = 1 ∧ 0 < dot v u} ∧
      (∀ u : Vector d, dot u u = 1 → dot v u ≤ 0 →
        annealedLaw ν (TransientPaths u) = 0) := by
  sorry
end DirectionalTransience
DEFS(21): abbrev Lattice, abbrev Direction, abbrev Vector, abbrev Row, abbrev Environment, abbrev State, abbrev Path, def step, def environmentLaw, def UniformElliptic, lemma measurable_current_row, def transition, instance transition_markov, def historyTransition, instance historyTransition_markov, def initialLaw, def annealedLaw, def dot, def realPosition, def TransientPaths, def VelocityPaths
## PAPER A-directional-zero-one-law-under-strict-ellipticity-September-23-2026
ABSTRACT: We prove the directional zero--one conjecture for nearest-neighbor random walks in independent and identically distributed strictly elliptic environments on $\ZZ^d$, $d\ge3$: the probability of escape in each fixed nonzero real direction is zero or one. Only strict positivity of the transition probabilities is required; no uniform lower bound or moment assumption is imposed.
[theorem] \label{thm:main} Let $d\ge3$, let $\PP$ be an independent and identically distributed law of nearest-neighbor transition rows on $\ZZ^d$ satisfying \eqref{eq:ellipticity}, and let $\ell\in\RR^d\setminus\{0\}$. Then \[ P_0(A_\ell)\in\{0,1\}. \]
## PAPER Directional-transience-implies-ballisticity-September-23-2026
ABSTRACT: We prove that almost-sure transience in a fixed direction implies a deterministic limiting velocity with positive projection in that direction for nearest-neighbor random walks in independent and identically distributed uniformly elliptic environments on $\mathbb Z^d$, $d\ge2$. This resolves the ballisticity conjecture positively.
[theorem[Directional transience implies ballisticity]] \label{thm:main} Let $d\ge2$ and let $P=\nu^{\otimes\mathbb Z^d}$ be an iid law of nearest-neighbor transition rows satisfying uniform ellipticity. If $\ell\in S^{d-1}$ and $P_0(A_\ell)=1$, then there exists a deterministic vector $v=v(\nu)\in\mathbb R^d$ such that \[ v\cdot\ell>0, \qquad P_0\!\left(\lim_{n\to\infty}\frac{X_n}{n}=v\right)=1. \] In particular, the walk is ballistic in the same direction $\ell$.
==================
# FAMILY 221: The Mézard–Parisi formula for diluted spin glasses
SCOPE: The formalization proves the Mézard–Parisi hierarchical cavity formula for diluted even-arity Ising models in the Panchenko–Talagrand class. Under the class's factorization, independence, integrability, and positivity assumptions, the finite-system pressure converges to the infimum of the trial functional over all finite hierarchy depths and trial laws. The arity is any even integer at least two and the interaction density is positive.
## CHALLENGE DilutedSpin  targets=['OAI.DilutedSpinGlass.mezard_parisi'] defs=[]
theorem mezard_parisi {p : ℕ} (M : Model p) (hM : Admissible M) :
    Tendsto (pressure M) atTop (𝓝 (variationalValue M)) := by
  sorry
end DilutedSpinGlass
DEFS(21): abbrev Spin, def spin, abbrev Interaction, abbrev InteractionSample, structure Model, structure Admissible, def logWeight, def logPartition, def pressure, def q, def edge, def appendSpin, def message, def siteLog, def Hierarchy, def logMean, def trialLog, def Exponents, def functional, def phi, def variationalValue
## PAPER The-Mezard-Parisi-formula-for-diluted-spin-glasses-September-23-2026
ABSTRACT: We prove the M\'ezard--Parisi hierarchical cavity formula for diluted even-arity Ising models in the Panchenko--Talagrand class. This resolves the variational equality conjecture for that class: the limiting pressure equals the infimum of the trial functional over all finite hierarchy depths and trial laws. Only first moments of the interaction and external field are required.
[theorem] \label{main:theorem} Under \eqref{model:integrability}--\eqref{model:positivity}, the thermodynamic limit exists and \begin{equation}\label{main:formula} \lim_{N\to\infty}F_N=\inf_{r\ge0}\Phi_r. \end{equation}
==================
# FAMILY 222: Perceptron free energies and microscopic jamming exponents
SCOPE: The linked formalization proves finiteness of the variational value used for the Ising random perceptron. For every nonnegative pattern density and every bounded continuous log-potential, the infimum over admissible overlap paths is a finite real number. This is a supporting well-definedness result. It does not assert convergence of the finite-system pressure or the paper's extension to all bounded Borel log-potentials. The formalization proves the variational formula for the spherical random perceptron's limiting pressure for every positive pattern density and inverse temperature and every bounded continuous single-pattern potential. It shows that the variational value is finite and that the pressure converges to it both in expectation and in probability. The linked spherical-field result supplies a supporting dual formula: finite hierarchy field values converge uniformly on compact par
## CHALLENGE IsingFiniteness  targets=['OAI.IsingPerceptron.variationalValue_real_of_continuous'] defs=[]
theorem variationalValue_real_of_continuous {α : ℝ} (hα : 0 ≤ α)
    {f : ℝ → ℝ} (hf : Continuous f) (hbounded : ∃ K : ℝ, ∀ x, |f x| ≤ K) :
    ∃ p : ℝ, variationalValue α f = (p : EReal) := by
  sorry
end IsingPerceptron
end
DEFS(13): def gaussianTransform, structure Partition, structure FieldStep, def stepAt, def stepFunction, def fieldRecursion, def pathMeasure, structure OverlapPath, def cellAverage, def uniformPattern, def patternFunctional, def isingEntropy, def variationalValue
## CHALLENGE PerceptronFreeEnergy  targets=['OAI.SphericalPerceptronFreeEnergy.main'] defs=[]
theorem main (P : Measure BrownianPath) [IsProbabilityMeasure P]
    (hB : IsBrownianReal brownianEval P)
    (α β : ℝ) (hα : 0 < α) (hβ : 0 < β) (φ : ℝ →ᵇ ℝ) :
    ∃ p : ℝ, variationalValue P α β φ = (p : EReal) ∧
      Tendsto (fun N : ℕ => expectedPressure α β φ (N + 1)) atTop (𝓝 p) ∧
      ∀ ε : ℝ, 0 < ε →
        Tendsto (fun N : ℕ => patternLaw α (N + 1)
          {g | ε < |pressure α β φ (N + 1) g - p|}) atTop (𝓝 0) := by
  sorry
end SphericalPerceptronFreeEnergy
end
DEFS(24): abbrev Time, abbrev BrownianPath, abbrev Spin, def patternCount, abbrev Patterns, def patternLaw, def unitSphereLaw, def sphereLaw, def patternField, def hamiltonian, def pressure, def expectedPressure, structure Trial, def timeLaw, def tailIntegral, def entropy, def brownianEval, def nullSigma, def usualBrownianSigma, def Progressive, def controlCost, def controlPayoff, def controlValue, def variationalValue
## CHALLENGE SphericalField  targets=['OAI.SphericalPerceptron.spherical_linear_field_formula'] defs=[]
theorem spherical_linear_field_formula : SphericalLinearFieldFormula := by
  sorry
end SphericalPerceptron
DEFS(85): abbrev Time, abbrev Spin, def unitSphereLaw, structure Trial, def timeLaw, def tailIntegral, def entropy, theorem timeLaw_eq_volume, def finitePointMeasure, lemma finitePointMeasure_measurable, def finitePoissonLaw, instance finitePoissonLaw_probability, lemma measureSum_measurable, def countablePoissonLaw, instance countablePoissonLaw_probability, def finiteIntensityMarks, instance finiteIntensityMarks_probability, def poissonRandomMeasureLaw, instance poissonRandomMeasureLaw_probability, def stableLogIntensity, instance stableLogIntensity_sigmaFinite, def normalizedMeasure, lemma measurable_measure_withDensity_fixed, lemma normalizedMeasure_measurable, def markedStableTotalE, lemma markedStableTotalE_measurable, def markedStableTotal, lemma markedStableTotal_measurable, def markedStableMassKernel, instance markedStableMassKernel_finite
## PAPER The-free-energy-of-the-Ising-random-perceptron-September-24-2026
ABSTRACT: We determine the limiting free energy of the Ising perceptron with independent Gaussian patterns for every bounded Borel log-potential, at every fixed positive temperature and pattern density. We give an explicit variational formula for the limit and prove convergence in expectation and probability.
[theorem[Gaussian Ising perceptron]] \label{thm:main} For every $\alpha>0$ and every bounded Borel $f:\mathbb R\to\mathbb R$, \begin{equation}\label{thm:formula} \lim_{N\to\infty}\mathbb E p_N(f) =\mathcal P_f(\alpha) :=\inf_{q\in\mathcal Q}\{\alpha V_f(q)+S_{\mathrm I}(q)\}. \end{equation} Moreover, $p_N(f)$ converges to $\mathcal P_f(\alpha)$ in probability. The variational value is finite. In particular, the conclusion holds for $f=\beta\phi$ at every $\beta>0$ and every bounded continuous activation $\phi$, without symmetry, concavity, or a smallness restriction.
## PAPER The-free-energy-of-the-spherical-random-perceptron-September-24-2026
ABSTRACT: We prove an exact variational formula for the limiting pressure of the spherical random perceptron with an arbitrary bounded continuous single-pattern potential. The formula holds at every fixed positive density and inverse temperature, with convergence in expectation and in probability.
[theorem] \label{thm:main} For every $\alpha,\beta>0$ and every $\phi\in C_b(\R;\R)$, \[ \lim_{N\to\infty}\E p_N =\inf_{m\in\U}\{\alpha V_{\beta\phi}(m)+S(m)\} =:\mathcal P(\alpha,\beta,\phi), \qquad p_N\xrightarrow{\mathbb P}\mathcal P(\alpha,\beta,\phi). \] Trials of infinite entropy have value $+\infty$. No condition that $m=1$ near $1$ is imposed.
==================
# FAMILY 227: Critical SK autocorrelation processes and dynamics across the temperature transition
SCOPE: For every fixed inverse temperature $0<\beta<1$, the formalization proves a dimension-independent Poincaré inequality for the zero-field Gaussian Sherrington–Kirkpatrick model with probability tending to one over the disorder. Equivalently, the unscaled single-site heat-bath spectral gap stays bounded away from zero. For dynamics that choose one site uniformly at each discrete step, the spectral gap is at least $1/(Cn)$ with probability tending to one, for a constant $C$ depending on $\beta$. The formalized supporting result proves ratio cutoff for discrete single-site heat-bath dynamics in the zero-field Gaussian Sherrington–Kirkpatrick model for $0\le\beta<1/2$. For every $0<\varepsilon<1/2$ and $\eta>0$, the probability over the disorder that $t_{\mathrm{mix}}(\varepsilon)/t_{\mathrm{mix}}(1-\varepsilon)>1+\eta$ tends to zero as $n\to\infty$. The denominator is positive for all suffic
## CHALLENGE SKHighTemperature  targets=['OAI.SKGap.sk_main'] defs=[]
theorem sk_main (β : ℝ) (hβ0 : 0 < β) (hβ1 : β < 1) : MainStatement β := by
  sorry
end SKGap
end
DEFS(18): abbrev Spin, abbrev Edge, abbrev Disorder, def spinValue, def coupling, def hamiltonian, def weight, def partition, def mass, def expectation, def variance, def flip, def conditionalExpectation, def dirichlet, def disorderLaw, def poincareEvent, def discreteGap, def MainStatement
## CHALLENGE SKRatio  targets=['OAI.SKRatio.ratio_cutoff'] defs=[]
theorem ratio_cutoff (β ε η : ℝ)
    (hβ0 : 0 ≤ β) (hβhalf : β < 1 / 2)
    (hε0 : 0 < ε) (hεhalf : ε < 1 / 2) (hη : 0 < η) :
    Tendsto
      (fun n : ℕ => disorderLaw β n
        {g : Disorder n | 1 + η <
          (mixingTime g ε : ℝ) / (mixingTime g (1 - ε) : ℝ)})
      atTop (𝓝 0) ∧
    (∀ᶠ n : ℕ in atTop, ∀ g : Disorder n, 0 < mixingTime g (1 - ε)) := by
  sorry
end SKRatio
end
DEFS(16): abbrev Spin, abbrev Edge, abbrev Disorder, def spinValue, def coupling, def hamiltonian, def weight, def partition, def mass, def flip, def disorderLaw, def siteKernel, def transition, def totalVariation, def discreteDistance, def mixingTime
## CHALLENGE CriticalSKMixing  targets=['OAI.CriticalSK.critical_mixing_bounds'] defs=[]
theorem critical_mixing_bounds (ε : ℝ) (hε : 0 < ε) :
    Tendsto (fun n : ℕ => (disorderLaw n {W |
      (n : ℝ) ^ ((2 : ℝ) / 3 - ε) ≤ continuousMixingTime W ∧
      continuousMixingTime W ≤ Real.exp (ε * n)}).toReal) atTop (𝓝 1) ∧
    Tendsto (fun n : ℕ => (disorderLaw n {W |
      (n : ℝ) ^ ((5 : ℝ) / 3 - ε) ≤ (discreteMixingTime W : ℝ) ∧
      (discreteMixingTime W : ℝ) ≤ Real.exp (ε * n)}).toReal) atTop (𝓝 1) := by
  sorry
end CriticalSK
end
DEFS(18): abbrev Spin, abbrev Edge, abbrev Disorder, def spinValue, def hamiltonian, def partition, def gibbs, def disorderLaw, def sameExcept, def siteKernel, def discreteKernel, def generator, def continuousKernel, def totalVariation, def continuousDistance, def discreteDistance, def continuousMixingTime, def discreteMixingTime
## CHALLENGE CriticalSK  targets=['OAI.CriticalSK.realized_equilibrium_initial_states', 'OAI.CriticalSK.covariance_and_linear_tests', 'OAI.CriticalSK.critical_mixing_lower_bounds'] defs=[]
theorem realized_equilibrium_initial_states :
    (∀ t : ℕ → ℝ, (∀ n, 0 ≤ t n) →
      Tendsto (fun n => t n / (n : ℝ) ^ ((2 : ℝ) / 3)) atTop (𝓝 0) →
      ∀ δ : ℝ, 0 < δ →
        Tendsto (fun n => (disorderLaw n {W |
          δ ≤ |continuousGoodMass W (t n) - 1|}).toReal) atTop (𝓝 0)) ∧
    (∀ k : ℕ → ℕ,
      Tendsto (fun n => (k n : ℝ) / (n : ℝ) ^ ((5 : ℝ) / 3)) atTop (𝓝 0) →
      ∀ δ : ℝ, 0 < δ →
        Tendsto (fun n => (disorderLaw n {W |
          δ ≤ |discreteGoodMass W (k n) - 1|}).toReal) atTop (𝓝 0)) := by
  sorry
/-- Both the covariance operator norm and the linear inverse-Rayleigh supremum lie
between `n^(2/3) / M n` and `M n * n^(2/3)` with probability tending to one. -/
theorem covariance_and_linear_tests (M : ℕ → ℝ)
    (hMpos : ∀ n, 0 < M n) (hM : Tendsto M atTop atTop) :
    Tendsto (fun n : ℕ => (disorderLaw n {W |
      (n : ℝ) ^ ((2 : ℝ) / 3) / M n ≤ covarianceNorm W ∧
      covarianceNorm W ≤ M n * (n : ℝ) ^ ((2 : ℝ) / 3) ∧
      (n : ℝ) ^ ((2 : ℝ) / 3) / M n ≤ linearRayleigh W ∧
      linearRayleigh W ≤ M n * (n : ℝ) ^ ((2 : ℝ) / 3)}).toReal) atTop (𝓝 1) := by
  sorry
/-- Worst-start mixing takes at least `n^(2/3-ε)` continuous time and
`n^(5/3-ε)` discrete attempts with probability tending to one. -/
theorem critical_mixing_lower_bounds (ε : ℝ) (hε : 0 < ε) :
    Tendsto (fun n => (disorderLaw n).real {W |
      (n : ℝ) ^ (2 / 3 - ε) ≤ continuousMixingTime W}) atTop (𝓝 1) ∧
    Tendsto (fun n => (disorderLaw n).real {W |
      (n : ℝ) ^ (5 / 3 - ε) ≤ (discreteMixingTime W : ℝ)}) atTop (𝓝 1) := by
  sorry
end CriticalSK
end
DEFS(27): abbrev Spin, abbrev Edge, abbrev Disorder, def spinValue, def hamiltonian, def partition, def gibbs, def disorderLaw, def sameExcept, def siteKernel, def discreteKernel, def generator, def continuousKernel, def totalVariation, def continuousDistance, def discreteDistance, def continuousMixingTime, def discreteMixingTime, def mean, def variance, def dirichlet, def linearObservable, def covariance, def covarianceNorm, def linearRayleigh, def continuousGoodMass, def discreteGoodMass
## CHALLENGE SKBarriers  targets=['OAI.SK.main'] defs=[]
theorem main (β : ℝ) (hβ : 1 < β) :
    Tendsto (continuousBadMass β) atTop (𝓝 1) ∧
    Tendsto (discreteBadMass β) atTop (𝓝 1) := by
  sorry
end SK
end
DEFS(19): abbrev Config, abbrev Edge, abbrev Disorder, def spin, def hamiltonian, def partition, def gibbs, def coupling, def localField, def heatBath, def discreteKernel, def continuousKernel, def discreteDistance, def continuousDistance, def disorderLaw, def kappa, def timeScale, def continuousBadMass, def discreteBadMass
## PAPER A-spectral-gap-throughout-the-high-temperature-Sherrington-Kirkpatrick-phase-September-24-2026
ABSTRACT: For every fixed inverse temperature $0<\beta<1$, we prove that the unscaled spectral gap of single-site heat-bath dynamics for the zero-field Gaussian Sherrington--Kirkpatrick model is bounded away from zero with probability tending to one over the disorder. Equivalently, the Gibbs law satisfies a dimension-free Poincar\'e inequality for all functions.
[theorem] \label{thm:main} There is a finite constant $C_\beta$, depending only on $\beta$, such that \[ \Prob_J\left\{\Var_{\mu_0}(f)\le C_\beta\D_0(f) \text{ for every }f:\{-1,1\}^n\longrightarrow\R\right\} \longrightarrow1. \] Consequently, the discrete-time heat-bath chain that chooses a uniform site has spectral gap at least $1/(C_\beta n)$ with probability tending to one.
## PAPER Cutoff-throughout-the-high-temperature-Sherrington-Kirkpatrick-phase-September-24-2026
ABSTRACT: We prove worst-case total-variation cutoff for the zero-field Gaussian Sherrington--Kirkpatrick heat-bath dynamics at every fixed inverse temperature \(0\leq\beta<1\). With rate-one refresh at each spin, the cutoff location is \(\log n/(2\lambda(\beta))\) for a positive deterministic rate \(\lambda(\beta)\). The location for uniformly chosen single-site update attempts is \(n\) times as large. Convergence is in probability over the disorder.
[theorem] \label{thm:main} For every fixed \(0\leq\beta<1\), there is a deterministic \(\lambda(\beta)>0\) such that, with \[ t_n=\frac{\log n}{2\lambda(\beta)}, \] for every \(\epsilon\in(0,1)\), \begin{align*} d_n((1-\epsilon)t_n)&\longrightarrow1, & d_n((1+\epsilon)t_n)&\longrightarrow0,\\ d_n^{\rm disc}(\lfloor(1-\epsilon)nt_n\rfloor)&\longrightarrow1, & d_n^{\rm disc}(\lceil(1+\epsilon)nt_n\rceil)&\longrightarrow0. \end{align*} All convergences are in probability over the disorder. For \(\beta=0\), \(\lambda(0)=1\). For \(0<\beta<1\), \(\lambda(\beta)\) is the equilibrium-operator constant defined in \eqref{eq:exact-lambda}; it satisfies \[ 0<\lambda(\beta)\leq(1-\beta)^2. \]
## PAPER Critical-slowing-down-in-the-Sherrington-Kirkpatrick-model-September-24-2026
ABSTRACT: At the critical inverse temperature $\beta=1$, we prove slow mixing for zero-field Gaussian Sherrington--Kirkpatrick heat-bath dynamics from typical equilibrium configurations held fixed as initial states. For every deterministic sequence $t_n=o(n^{2/3})$ in rate-one-per-site time, the Gibbs mass of initial states whose time-$t_n$ total-variation distance from equilibrium exceeds $1/4$ tends to one in probability over the disorder. The same statement holds for every deterministic integer sequence $k_n=o(n^{5/3})$ of uniform-site update attempts.
[theorem[Realized equilibrium initial states]] \label{thm:gibbs-start} For every deterministic sequence $t_n\ge0$ with $t_n=o(n^{2/3})$, \[ \mu_W\{x:d_{t_n}^{\rm ct}(W,x)>1/4\} \xrightarrow{\Prob}1. \] For every deterministic integer sequence $k_n\ge0$ with $k_n=o(n^{5/3})$, \[ \mu_W\{x:d_{k_n}^{\rm dt}(W,x)>1/4\} \xrightarrow{\Prob}1. \] The convergence is in probability over the disorder.
## PAPER Stretched-exponential-barriers-for-typical-SK-initial-states-September-24-2026
ABSTRACT: At every fixed inverse temperature $\beta>1$, we prove a stretched-exponential obstruction to mixing for the zero-field Sherrington--Kirkpatrick model from typical equilibrium configurations held fixed as initial states. The Gibbs mass of states whose total-variation distance from equilibrium at time $\exp(n^{1/10000})$ exceeds $1/4$ tends to one in probability over the disorder. This holds for rate-one-per-site heat-bath dynamics and after the same stated number of discrete update attempts.
[theorem] \label{thm:main} Set $\kap=1/10000$. For every fixed $\beta>1$, \begin{align*} \PP_{J,\,x_0\sim\pi^J} \left\{d^J\bigl(x_0,\exp(n^\kap)\bigr)>\frac14\right\} &\longrightarrow1,\\ \PP_{J,\,x_0\sim\pi^J} \left\{d_{\mathrm{disc}}^J \bigl(x_0,\lfloor\exp(n^\kap)\rfloor\bigr)>\frac14\right\} &\longrightarrow1. \end{align*}
==================
# FAMILY 228: Continuum phase transitions for radial pair potentials
SCOPE: The formalization constructs one stable radial pair potential in three-dimensional continuum space with a divergent repulsive core and an integrable tail that is $o(r^{-3})$. Its canonical free energy exists for every positive inverse temperature and density. At one inverse temperature $\beta_c\in(1/2,3/2)$, the free energy has a strict finite jump between its one-sided derivatives with respect to inverse temperature, for every density in one nonempty open interval. The formalization constructs a bounded continuous stable radial pair potential in $\mathbb R^3$ satisfying $|\phi(r)|\le Cr^{-3-1/32}$ for $r\ge1$. There is a nonempty open interval of positive densities around $5p/3$, where $p$ is the unit-separated packing-density limit, on which the canonical free energy exists at every positive inverse temperature and has a strict downward derivative jump at one common $\beta_c\in[7/8,9/8
## CHALLENGE ContinuumTransition  targets=['OAI.ContinuumTemperature.main_theorem'] defs=[]
theorem main_theorem : MainStatement := by
  sorry
end ContinuumTemperature
DEFS(9): abbrev Space, def radialPotential, def energy, def Admissible, def cube, def boltzmann, def partition, def HasCanonicalFreeEnergy, def MainStatement
## CHALLENGE RadialTransition  targets=['OAI.RadialTransition.main'] defs=[]
theorem main :
    ∃ (p : ℝ) (φ : Potential) (B C : ℝ) (f : ℝ → ℝ) (βc : ℝ),
      0 < p ∧ IsPackingDensity p ∧
      IsBoundedPotential φ ∧ Continuous φ ∧
      0 < B ∧ 0 < C ∧ StableWith φ B ∧ AlgebraicDecayWith φ C ∧
      IsCanonicalFreeEnergy φ (5*p/3) f ∧
      βc ∈ Icc (7/8:ℝ) (9/8) ∧ StrictTemperatureCorner f βc := by
  sorry
end RadialTransition
end
DEFS(13): abbrev Position, abbrev Potential, def cube, def configurationCube, def energy, def partition, def packingNumber, def IsPackingDensity, def IsBoundedPotential, def StableWith, def AlgebraicDecayWith, def IsCanonicalFreeEnergy, def StrictTemperatureCorner
## CHALLENGE RadialDensityInterval  targets=['OAI.RadialTransition.densityInterval'] defs=[]
theorem densityInterval :
    ∃ (p : ℝ) (φ : Potential) (B C η βc : ℝ) (f : ℝ → ℝ → ℝ),
      0 < p ∧ IsPackingDensity p ∧
      IsBoundedPotential φ ∧ Continuous φ ∧
      0 < B ∧ 0 < C ∧ StableWith φ B ∧ AlgebraicDecayWith φ C ∧
      0 < η ∧ Ioo (5*p/3 - η) (5*p/3 + η) ⊆ Ioi 0 ∧
      βc ∈ Icc (7/8:ℝ) (9/8) ∧
      ∀ ρ ∈ Ioo (5*p/3 - η) (5*p/3 + η),
        IsCanonicalFreeEnergy φ ρ (fun β => f β ρ) ∧
        StrictTemperatureCorner (fun β => f β ρ) βc := by
  sorry
end RadialTransition
end
DEFS(13): abbrev Position, abbrev Potential, def cube, def configurationCube, def energy, def partition, def packingNumber, def IsPackingDensity, def IsBoundedPotential, def StableWith, def AlgebraicDecayWith, def IsCanonicalFreeEnergy, def StrictTemperatureCorner
## PAPER A-continuum-temperature-singularity-for-a-radial-pair-potential-September-24-2026
ABSTRACT: We construct a stable radial pair potential in three dimensions whose canonical free energy has a strict downward derivative jump at one common finite positive inverse temperature throughout an open interval of positive densities. The potential has a divergent repulsive core, a nontrivial attractive interval, and an integrable tail satisfying $\phi(r)=o(r^{-3})$. Its free-cube canonical free energy is finite at every positive inverse temperature and density.
[theorem] \label{thm:main} There exist an admissible radial difference-only pair potential $\Phi(x)=\phi(|x|)$ on $\R^3$, a nonempty open interval $I\subset(0,\infty)$, and one $\beta_c\in(1/2,3/2)$ with the following properties. The potential satisfies $\phi(r)=o(r^{-3})$ as $r\to\infty$. The free-cube limit \eqref{eq:free-energy-definition} exists and is finite for every $\beta>0$ and every density $\rho>0$. For every $\rho\in I$, the finite one-sided derivatives at the same critical point satisfy \[ D_\beta^- f_\Phi(\beta_c,\rho) >D_\beta^+ f_\Phi(\beta_c,\rho). \] Thus one potential and one critical inverse temperature give a strict canonical temperature singularity throughout $I$.
## PAPER A-radial-continuum-phase-transition-with-algebraic-decay-September-24-2026
ABSTRACT: We construct a bounded, continuous, stable radial pair potential in three dimensions with \(|\phi(r)|\le Cr^{-3-1/32}\) for \(r\ge1\). Throughout an open interval of positive densities, its canonical thermodynamic free energy is finite at every positive inverse temperature and has a strict downward derivative jump at one common finite positive inverse temperature.
[theorem] \label{thm:main} There is a bounded continuous function \(\phi:[0,\infty)\to\R\) and finite constants \(B,C>0\) such that \[ \sum_{i<j}\phi(\abs{x_i-x_j})\ge-BN, \qquad \abs{\phi(r)}\le C r^{-3-1/32}\quad(r\ge1). \] There are an open interval \(I\subset(0,\infty)\) centered at \(5p/3\) and a common inverse temperature \(\beta_c\in[7/8,9/8]\) such that, for every \(\rho\in I\), the canonical free energy \[ f(\beta,\rho)= -\lim_{L\to\infty}\frac1{\beta L^3} \log Z^\phi_{L,\lfloor\rho L^3\rfloor}(\beta) \] exists and is finite for every \(\beta>0\). Its finite one-sided derivatives at \(\beta_c\) satisfy \[ f'_-(\beta_c,\rho)>f'_+(\beta_c,\rho). \] In particular, \(f(\,\cdot\,,\rho)\) is not di
==================
# FAMILY 229: Exact three- and four-state reconstruction thresholds and four-state tree capacity
SCOPE: The formalization proves the supercritical direction of reconstruction for the symmetric three-state broadcast channel, whose parameter satisfies $-1/2\le\lambda\le1$. On a regular $b$-ary tree, reconstruction holds when $b\lambda^2>1$; on an observed Poisson Galton–Watson tree of mean $d$, it holds when $d\lambda^2>1$. In each case the root-estimation advantage converges to a positive limit, with the Poisson advantage averaged over trees and spins. The selected statements cover reconstruction above the Kesten–Stigum threshold. Non-reconstruction at or below the threshold and the stochastic-block-model consequences in the paper are outside them.
## CHALLENGE ThreeStateSupercritical  targets=['OAI.ThreeState.regular_supercritical', 'OAI.ThreeState.poisson_supercritical'] defs=[]
theorem regular_supercritical (b : ℕ) (hb : 2 ≤ b) (lam : ℝ) (h : Admissible lam)
    (hcrit : 1 < (b : ℝ) * lam ^ 2) : Reconstructs (regularAdvantage b lam h) := by
  sorry
theorem poisson_supercritical (d : ℝ) (hd : 1 < d) (lam : ℝ) (h : Admissible lam)
    (hcrit : 1 < d * lam ^ 2) : Reconstructs (poissonAdvantage d hd lam h) := by
  sorry
end ThreeState
DEFS(19): abbrev Spin, def Admissible, def channel, def Observation, theorem channel_nonneg, theorem channel_sum, def channelPMF, def iidList, def observedLaw, def uniformSpin, def marginal, def posterior, def advantage, def regularLaw, def poissonOffspring, def poissonLaw, def regularAdvantage, def poissonAdvantage, def Reconstructs
## CHALLENGE ThreeStateTreeClauses  targets=['OAI.ThreeState.TreeClauses.Tree.regular_reconstructs_above_KS', 'OAI.ThreeState.TreeClauses.Tree.poisson_reconstructs_above_KS'] defs=[]
theorem regular_reconstructs_above_KS (b : ℕ) (lam : ℝ) (hlam : Admissible lam)
    (hKS : 1 < (b:ℝ)*lam^2) : Reconstructs lam hlam (PMF.pure b) := by
  sorry
theorem poisson_reconstructs_above_KS (d : ℝ≥0) (lam : ℝ) (hlam : Admissible lam)
    (hKS : 1 < (d:ℝ)*lam^2) : Reconstructs lam hlam (poissonPMF d) := by
  sorry
end ThreeState.TreeClauses.Tree
end
DEFS(18): abbrev Spin, def Admissible, def channelWeight, lemma channelWeight_nonneg, lemma channelWeight_sum, def channel, def Observation, def iidList, def observationLaw, def jointWeight, def marginalWeight, def posterior, def advantage, def Reconstructs, def poissonWeight, lemma poissonWeight_nonneg, lemma poissonWeight_mass, def _root_.OAI.ThreeState.TreeClauses.poissonPMF
## PAPER The-exact-reconstruction-threshold-for-the-three-state-symmetric-channel-September-25-2026
ABSTRACT: We determine the exact reconstruction threshold for the symmetric three-state broadcast process on every regular $b$-ary tree, $b\ge2$, and every observed Poisson Galton--Watson tree of mean $d>1$. Reconstruction occurs exactly when $d\lambda^2>1$, with $d=b$ in the regular model; there is non-reconstruction at equality for either sign of the channel parameter. The Poisson advantage is averaged over trees and spins without conditioning on survival. This resolves the all-degree three-state regular-tree prediction. Combining the Poisson theorem with known tree-to-graph and algorithmic results gives the exact weak-recovery threshold for the symmetric three-community sparse stochastic block mode
[theorem[Exact threshold]] \label{thm:threshold} For every integer $b\ge2$ in the regular model and every real $d>1$ in the Poisson model, reconstruction occurs if and only if \[ d\lambda^2>1, \] with $d=b$ in the regular case. At every admissible equality $d\lambda^2=1$, there is non-reconstruction.
==================
# FAMILY 230: Exact Hausdorff gauges for SLE
SCOPE: For $0<\kappa<8$, put $d=1+\kappa/8$. The formalization proves that every continuous nondecreasing Hausdorff gauge agreeing with $h(r)=r^d(\log\log(1/r))^{(2-d)/2}$ at sufficiently small positive radii almost surely assigns positive measure to every nontrivial compact positive-time segment of ordinary chordal $\mathrm{SLE}_\kappa$.
## CHALLENGE SLELowerPositivity  targets=['OAI.SLEExactGauge.sourceLowerMain_proved'] defs=[]
theorem sourceLowerMain_proved : SourceLowerMainTarget := by
  sorry
end SLEExactGauge
end
DEFS(14): def dimension, def codimension, def upperHalfPlane, def survivingDomain, def IsCapacityTwoWitness, def IsCapacityTwoTrace, def IsOrdinaryChordalSLE, structure IsGauge, def hFormula, def HasSmallRadiusFormula, def extendedGauge, def hausdorffGauge, def segment, def SourceLowerMainTarget
## PAPER An-exact-Hausdorff-gauge-for-SLE-September-25-2026
ABSTRACT: For each \(0<\kappa<8\), we construct a deterministic Hausdorff gauge that almost surely assigns positive finite measure to every nontrivial compact positive-time segment of chordal Schramm--Loewner evolution. This answers Schramm's Hausdorff-measure existence problem in this parameter range. The entire trace has finite expected gauge measure in each bounded box.
[theorem[An exact moment gauge]] \label{thm:main} Fix $0<\kappa<8$, and let $\gamma$ be chordal $\SLE_\kappa$ from $0$ to $\infty$ in the upper half-plane $\HH$, parametrized by half-plane capacity $2t$. There is a deterministic Hausdorff gauge $h_\kappa$, depending only on $\kappa$, such that almost surely, simultaneously for every real $0<s<t<\infty$, \[ 0<\Haus^{h_\kappa}(\gamma([s,t]))<\infty. \]
## PAPER An-explicit-exact-Hausdorff-gauge-for-SLE-September-26-2026
ABSTRACT: For each fixed $0<\kappa<8$, let $d=1+\kappa/8$. The gauge $h(r)=r^d(\log\log(1/r))^{(2-d)/2}$ at sufficiently small radii almost surely gives positive finite Hausdorff measure to every nontrivial positive-time compact segment of chordal $\mathrm{SLE}_\kappa$. This gives an explicit solution to Schramm's Hausdorff-measure problem in this parameter range. The entire trace has finite expected measure in every bounded disk. The exponent-one iterated-logarithm gauge suggested by Schramm is not sigma-finite on any such segment.
[theorem] \label{thm:main} Let $\gamma$ be ordinary chordal $\mathrm{SLE}_\kappa$ from $0$ to $\infty$ in $\mathbb H$, parametrized by half-plane capacity $2t$, and set $\Gamma=\gamma([0,\infty))$. For each fixed $0<\kappa<8$, on one event of probability one, \[ 0<\mathcal H^h(\gamma([s,t]))<\infty \qquad\text{for every real }0<s<t<\infty. \] For every deterministic $0<R<\infty$, \[ \mathbb E\mathcal H^h(\Gamma\cap\overline B(0,R)) \le C_{\kappa,R}<\infty. \] In particular, on the same probability-one event, \[ \mathcal H^h\bigl(\Gamma\cap([-m,m]+i[0,m])\bigr)<\infty \qquad(m=1,2,\ldots). \]
==================
# FAMILY 231: The free uniform spanning forest is a factor of IID
SCOPE: The formalization proves that the free uniform spanning forest is a factor of independent identically distributed vertex labels on every infinite connected locally finite simple unweighted graph. One Borel equivariant rule works for all such graphs and uses no distinguished root. The linked supplements also give equivariant IID sampling for invariant strongly Rayleigh laws on countable groups and existence, uniqueness, and IID-factor results for determinantal laws with Hermitian positive-contraction kernels on countable index sets. These group results require neither amenability nor finite generation, and the kernels need not be trace class.
## CHALLENGE StronglyRayleighDPP  targets=['OAI.Problem336AdditiveD139.finite_strongly_rayleigh_response', 'OAI.Problem336AdditiveD139.strongly_rayleigh_group_factor', 'OAI.Problem336AdditiveD139.finite_positive_contraction_dpp_is_strongly_rayleigh', 'OAI.Problem336AdditiveD139.countable_positive_contraction_dpp_exists_unique', 'OAI.Problem336AdditiveD139.invariant_positive_contraction_dpp_factor', 'OAI.Problem336AdditiveD139.translation_invariant_kernel_dpp_factor'] defs=[]
theorem finite_strongly_rayleigh_response :
    ∀ (F : Type u_1) [Fintype F] [Nonempty F] (μ : ProbabilityMeasure (F → Bool)),
      StronglyRayleighFinite μ →
        (∀ (i j : F) (h : F → ℝ),
          HasDerivAt (fun r : ℝ => tiltMean μ (coordinatePerturb h j r) i)
            (tiltCovariance μ h i j) 0) ∧
        (∀ (i : F) (h : F → ℝ),
          (∑ j : F, |tiltCovariance μ h i j|) ≤
              2 * tiltMean μ h i * (1 - tiltMean μ h i) ∧
            2 * tiltMean μ h i * (1 - tiltMean μ h i) ≤ (1 : ℝ) / 2) ∧
        (∀ (i : F) (h h' : F → ℝ) (D : ℝ),
          0 ≤ D → (∀ j : F, |h j - h' j| ≤ D) →
            |tiltMean μ h i - tiltMean μ h' i| ≤ D / 2) := by
  sorry
theorem strongly_rayleigh_group_factor :
    ∀ (Γ : Type u_2) [Group Γ] [Countable Γ] [MeasurableSpace Γ],
      ∀ μ : ProbabilityMeasure (Γ → Bool),
        StronglyRayleighCountable μ → InvariantBinaryLaw μ → HasEquivariantIIDFactor μ := by
  sorry
theorem finite_positive_contraction_dpp_is_strongly_rayleigh :
    ∀ (F : Type u_3) [Fintype F] [Nonempty F] (K : F → F → ℂ),
      PositiveContractionFinite K →
        (∃ μ : ProbabilityMeasure (F → Bool), IsFiniteDeterminantalLaw μ K) ∧
          ∀ μ : ProbabilityMeasure (F → Bool), IsFiniteDeterminantalLaw μ K →
            StronglyRayleighFinite μ := by
  sorry
theorem countable_positive_contraction_dpp_exists_unique :
    ∀ (I : Type u_4) [Countable I] (K : I → I → ℂ),
      PositiveContractionKernel K →
        ∃! μ : ProbabilityMeasure (I → Bool), IsDeterminantalLaw μ K := by
  sorry
theorem invariant_positive_contraction_dpp_factor :
    ∀ (Γ : Type u_5) [Group Γ] [Countable Γ] [MeasurableSpace Γ]
      (K : Γ → Γ → ℂ) (μ : ProbabilityMeasure (Γ → Bool)),
      PositiveContractionKernel K → IsDeterminantalLaw μ K →
        InvariantBinaryLaw μ → HasEquivariantIIDFactor μ := by
  sorry
theorem translation_invariant_kernel_dpp_factor :
    ∀ (Γ : Type u_6) [Group Γ] [Countable Γ] [MeasurableSpace Γ] (K : Γ → Γ → ℂ),
      PositiveContractionKernel K → TranslationInvariantKernel K →
        ∃ μ : ProbabilityMeasure (Γ → Bool),
          IsDeterminantalLaw μ K ∧ InvariantBinaryLaw μ ∧ HasEquivariantIIDFactor μ := by
  sorry
end Problem336AdditiveD139
end
DEFS(21): abbrev UnitLabel, def leftTranslate, def iidUnitLabels, def InvariantBinaryLaw, def HasEquivariantIIDFactor, def finiteGeneratingValue, def StronglyRayleighFinite, def marginalMass, def marginalGeneratingValue, def StronglyRayleighCountable, def boolReal, def tiltPartition, def tiltMean, def tiltSecondMoment, def tiltCovariance, def coordinatePerturb, def PositiveContractionFinite, def IsFiniteDeterminantalLaw, def PositiveContractionKernel, def IsDeterminantalLaw, def TranslationInvariantKernel
## CHALLENGE FreeUniformSpanningForest  targets=['OAI.Problem336.fusf_is_factor_iid'] defs=[]
theorem fusf_is_factor_iid :
    ∃ Phi : FactorRule, RuleBorel Phi ∧ RuleEquivariant Phi ∧ ∀ G : GraphCode, WorksOnGraph Phi G := by
  sorry
end Problem336
end
DEFS(26): abbrev GraphCode, abbrev EdgeCode, abbrev EdgeConfiguration, abbrev FactorRule, abbrev FiniteSubgraphCode, def Adj, def GraphConnected, def GraphLocallyFinite, def mkEdge, def rawPair, def relabelGraph, def relabelLabels, def mapEdge, def RuleBorel, def RuleEquivariant, def TreeAdj, def SubgraphAdj, def TreeOn, def spanningTrees, def ustCylinder, def IsFiniteConnectedSubgraph, def IsConnectedExhaustion, def uniform01, def IsVertexIID, def HasFUSFLaw, def WorksOnGraph
## PAPER The-free-uniform-spanning-forest-is-a-factor-of-IID-September-25-2026
ABSTRACT: We prove that the free uniform spanning forest is a factor of IID on every infinite connected locally finite simple unweighted graph. One Borel rule works for all such graphs and uses no root, answering affirmatively the general factor question for unimodular random graphs. We also show that every translation-invariant strongly Rayleigh process indexed by a countable group is a factor of IID, including invariant determinantal processes with Hermitian positive-contraction kernels. This group-action conclusion requires no amenability.
[theorem] \label{thm:main} There is one Borel, root-independent, equivariant rule \[ \Phi(G,U,e)\in\{0,1\} \] such that, for every infinite connected locally finite simple undirected unweighted graph $G$ and independent $\operatorname{Uniform}[0,1]$ vertex labels $U=(U_v)_{v\in V(G)}$, the entire edge set \[ \{e\in E(G):\Phi(G,U,e)=1\} \] has law $\FUSF_G$.
==================
# FAMILY 234: All-temperature pressure of orthogonally invariant Ising spin glasses
SCOPE: The formalization gives variational limits for orthogonally invariant Ising spin glasses whose eigenvectors have Haar law and whose empirical eigenvalue distributions converge to a compactly supported law with the stated control of extreme eigenvalues. The pressure converges both in expectation and almost surely to an explicit functional of the limiting spectral law. A version with external fields assumes convergence of their empirical laws in Wasserstein distance and gives the corresponding magnetic-field functional. The formalization also covers every positive temperature, a ground-state limit, random spectral data with the stated conditional Haar law, and Gaussian-pattern specializations. These hypotheses identify the invariant models to which the limits apply.
## CHALLENGE InvariantIsing  targets=['OAI.InvariantIsing.limiting_pressure_of_extreme_limits_unconditional', 'OAI.InvariantIsing.limiting_wasserstein_field_pressure_of_extreme_limits_unconditional', 'OAI.InvariantIsing.positive_temperature_pressure_unconditional', 'OAI.InvariantIsing.ground_state_limit_unconditional', 'OAI.InvariantIsing.random_pressure_tendsto_in_measure_unconditional', 'OAI.InvariantIsing.random_pressure_limit_unconditional', 'OAI.InvariantIsing.random_pressure_tendsto_ae_unconditional', 'OAI.InvariantIsing.random_field_pressure_tendsto_ae_unconditional', 'OAI.InvariantIsing.gaussianPattern_pressure_limit_unconditional', 'OAI.InvariantIsing.gaussianPattern_ground_limit_unconditional', 'OAI.InvariantIsing.gaussianPattern_norm_limits_unconditional'] defs=[]
theorem limiting_pressure_of_extreme_limits_unconditional :
  ∀ {Ω : Type*} [MeasurableSpace Ω] (P : Measure Ω) [IsProbabilityMeasure P]
    (U : (N : ℕ) → Ω → Orthogonal N) (_hU : ∀ N, Measurable (U N))
    (_hHaar : ∀ N, (P.map (U N)).IsMulRightInvariant)
    (eig : (N : ℕ) → Fin N → ℝ) (ν : ProbabilityMeasure ℝ) (a b : ℝ)
    (_hcompact : IsCompact (ν : Measure ℝ).support)
    (_hbound : (ν : Measure ℝ).support ⊆ Icc a b)
    (_ha : a∈(ν : Measure ℝ).support) (_hb : b∈(ν : Measure ℝ).support)
    (_hmin : Tendsto (fun k => spectralMinimum (eig (k+1))) atTop (𝓝 a))
    (_hmax : Tendsto (fun k => spectralMaximum (eig (k+1))) atTop (𝓝 b))
    (_hweak : Tendsto (fun k => empiricalSpectralLaw (Nat.succ_pos k) (eig (k+1)))
      atTop (𝓝 ν)),
    Tendsto (fun N => ∫ ω, rotatedPressure (eig N) (matrixRotation (U N ω)⁻¹) (fun _ => 0) ∂P)
      atTop (𝓝 (variationalFunctional (measureR (ν : Measure ℝ) b)).toReal) ∧
    ∀ᵐ ω ∂P, Tendsto (fun N => rotatedPressure (eig N) (matrixRotation (U N ω)⁻¹) (fun _ => 0))
      atTop (𝓝 (variationalFunctional (measureR (ν : Measure ℝ) b)).toReal) := by
  sorry
theorem limiting_wasserstein_field_pressure_of_extreme_limits_unconditional :
  ∀ {Ω : Type*} [MeasurableSpace Ω] (P : Measure Ω) [IsProbabilityMeasure P]
    (U : (N : ℕ) → Ω → Orthogonal N) (_hU : ∀ N, Measurable (U N))
    (_hHaar : ∀ N, (P.map (U N)).IsMulRightInvariant)
    (eig : (N : ℕ) → Fin N → ℝ) (ν : ProbabilityMeasure ℝ) (a b : ℝ)
    (_hcompact : IsCompact (ν : Measure ℝ).support)
    (_hbound : (ν : Measure ℝ).support ⊆ Icc a b)
    (_ha : a∈(ν : Measure ℝ).support) (_hb : b∈(ν : Measure ℝ).support)
    (_hmin : Tendsto (fun k => spectralMinimum (eig (k+1))) atTop (𝓝 a))
    (_hmax : Tendsto (fun k => spectralMaximum (eig (k+1))) atTop (𝓝 b))
    (_hweak : Tendsto (fun k => empiricalSpectralLaw (Nat.succ_pos k) (eig (k+1)))
      atTop (𝓝 ν))
    (field : (N : ℕ) → Fin N → ℝ) (ξ : ProbabilityMeasure ℝ)
    (_hξ : Integrable (fun x : ℝ => x) (ξ : Measure ℝ))
    (_hw : Tendsto (fun k => fieldWassersteinOne (empiricalSpectralLaw (Nat.succ_pos k) (field (k+1))) ξ)
      atTop (𝓝 0)),
    Tendsto (fun N => ∫ ω, rotatedPressure (eig N) (matrixRotation (U N ω)⁻¹) (field N) ∂P)
      atTop (𝓝 (magneticFieldFunctional (ν : Measure ℝ) b ξ)) ∧
    ∀ᵐ ω ∂P, Tendsto (fun N => rotatedPressure (eig N) (matrixRotation (U N ω)⁻¹) (field N))
      atTop (𝓝 (magneticFieldFunctional (ν : Measure ℝ) b ξ)) := by
  sorry
theorem positive_temperature_pressure_unconditional :
  ∀ {Ω : Type*} [MeasurableSpace Ω] (P : Measure Ω) [IsProbabilityMeasure P]
    (U : (N : ℕ) → Ω → Orthogonal N) (_hU : ∀ N, Measurable (U N))
    (_hHaar : ∀ N, (P.map (U N)).IsMulRightInvariant)
    (eig : (N : ℕ) → Fin N → ℝ) (ν : ProbabilityMeasure ℝ) (a b : ℝ)
    (_hbound : (ν : Measure ℝ).support ⊆ Icc a b)
    (_ha : a∈(ν : Measure ℝ).support) (_hb : b∈(ν : Measure ℝ).support)
    (_hno : ∀ ε : ℝ, 0 < ε → ∀ᶠ N in atTop, ∀ i, a-ε ≤ eig N i ∧ eig N i ≤ b+ε)
    (β : ℝ) (_hβ : 0 < β)
    (_hweak : Tendsto (fun k => empiricalSpectralLaw (Nat.succ_pos k) (eig (k+1)))
      atTop (𝓝 ν)),
    Tendsto (fun N => ∫ ω, rotatedPressure (fun i => β*eig N i) (matrixRotation (U N ω)⁻¹) (fun _ => 0) ∂P)
      atTop (𝓝 (variationalFunctional (measureR (scaledSpectralLaw ν β : Measure ℝ) (β*b))).toReal) ∧
    ∀ᵐ ω ∂P, Tendsto (fun N => rotatedPressure (fun i => β*eig N i) (matrixRotation (U N ω)⁻¹) (fun _ => 0))
      atTop (𝓝 (variationalFunctional (measureR (scaledSpectralLaw ν β : Measure ℝ) (β*b))).toReal) := by
  sorry
theorem ground_state_limit_unconditional :
  ∀ {Ω : Type*} [MeasurableSpace Ω] (P : Measure Ω) [IsProbabilityMeasure P]
    (U : (N : ℕ) → Ω → Orthogonal N) (_hU : ∀ N, Measurable (U N))
    (_hHaar : ∀ N, (P.map (U N)).IsMulRightInvariant)
    (eig : (N : ℕ) → Fin N → ℝ) (ν : ProbabilityMeasure ℝ) (a b : ℝ)
    (_hbound : (ν : Measure ℝ).support ⊆ Icc a b)
    (_ha : a∈(ν : Measure ℝ).support) (_hb : b∈(ν : Measure ℝ).support)
    (_hno : ∀ ε : ℝ, 0 < ε → ∀ᶠ N in atTop, ∀ i, a-ε ≤ eig N i ∧ eig N i ≤ b+ε)
    (_hweak : Tendsto (fun k => empiricalSpectralLaw (Nat.succ_pos k) (eig (k+1)))
      atTop (𝓝 ν)),
    ∃ M : ℝ,
      Tendsto (fun N => ∫ ω, groundStateEnergy (eig N) (matrixRotation (U N ω)⁻¹) ∂P)
        atTop (𝓝 M) ∧
      (∀ᵐ ω ∂P, Tendsto (fun N => groundStateEnergy (eig N) (matrixRotation (U N ω)⁻¹))
        atTop (𝓝 M)) ∧
      Tendsto (thermalVariationalValue ν b) atTop (𝓝 M) := by
  sorry
theorem random_pressure_tendsto_in_measure_unconditional
    {Ω : Type*} [MeasurableSpace Ω] (P : Measure Ω) [IsProbabilityMeasure P]
    (eig : (N : ℕ) → Ω → Fin N → ℝ) (Y : ℕ → Ω → ℝ)
    (heig : ∀ N, Measurable (eig N)) (hY : ∀ N, Measurable (Y N))
    (H : (N : ℕ) → Measure (Orthogonal N)) [∀ N, IsProbabilityMeasure (H N)]
    [∀ N, (H N).IsMulRightInvariant]
    (hlaw : ∀ N, ConditionalFieldOrbitLaw P (fun ω => (eig N ω,fun _ => 0)) (Y N) (H N))
    (ν : ProbabilityMeasure ℝ) (a b : ℝ)
    (hcompact : IsCompact (ν : Measure ℝ).support)
    (hbound : (ν : Measure ℝ).support ⊆ Icc a b)
    (ha : a∈(ν : Measure ℝ).support) (hb : b∈(ν : Measure ℝ).support)
    (hweak : TendstoInMeasure P (fun k ω => LevyProkhorov.ofMeasure
      (empiricalSpectralLaw (Nat.succ_pos k) (eig (k+1) ω))) atTop
      (fun _ => LevyProkhorov.ofMeasure ν))
    (hexcess : TendstoInMeasure P (fun k ω => spectralExcess (eig (k+1) ω) a b)
      atTop (fun _ => 0)) :
    TendstoInMeasure P (fun k => Y (k+1)) atTop
      (fun _ => (variationalFunctional (measureR (ν : Measure ℝ) b)).toReal) := by
  sorry
theorem random_pressure_limit_unconditional :
  ∀ {Ω : Type*} [MeasurableSpace Ω] (P : Measure Ω) [IsProbabilityMeasure P]
    (eig : (N : ℕ) → Ω → Fin N → ℝ) (Y : ℕ → Ω → ℝ)
    (_heig : ∀ N, Measurable (eig N)) (_hY : ∀ N, Measurable (Y N))
    (H : (N : ℕ) → Measure (Orthogonal N)) [∀ N, IsProbabilityMeasure (H N)]
    [∀ N, (H N).IsMulRightInvariant]
    (_hlaw : ∀ N, ConditionalFieldOrbitLaw P (fun ω => (eig N ω,fun _ => 0)) (Y N) (H N))
    (ν : ProbabilityMeasure ℝ) (a b : ℝ)
    (_hcompact : IsCompact (ν : Measure ℝ).support)
    (_hbound : (ν : Measure ℝ).support ⊆ Icc a b)
    (_ha : a∈(ν : Measure ℝ).support) (_hb : b∈(ν : Measure ℝ).support)
    (_hweak : TendstoInMeasure P (fun k ω => LevyProkhorov.ofMeasure
      (empiricalSpectralLaw (Nat.succ_pos k) (eig (k+1) ω))) atTop
      (fun _ => LevyProkhorov.ofMeasure ν))
    (_hexcess : TendstoInMeasure P (fun k ω => spectralExcess (eig (k+1) ω) a b)
      atTop (fun _ => 0))
    (_hUI : UniformIntegrable (fun k => Y (k+1)) 1 P),
    TendstoInMeasure P (fun k => Y (k+1)) atTop
      (fun _ => (variationalFunctional (measureR (ν : Measure ℝ) b)).toReal) ∧
    Tendsto (fun k => eLpNorm (fun ω => Y (k+1) ω-
      (variationalFunctional (measureR (ν : Measure ℝ) b)).toReal) 1 P) atTop (𝓝 0) ∧
    Tendsto (fun k => ∫ ω, Y (k+1) ω ∂P) atTop
      (𝓝 (variationalFunctional (measureR (ν : Measure ℝ) b)).toReal) := by
  sorry
theorem random_pressure_tendsto_ae_unconditional :
  ∀ {Ω : Type*} [MeasurableSpace Ω] (P : Measure Ω) [IsProbabilityMeasure P]
    (eig : (N : ℕ) → Ω → Fin N → ℝ) (Y : ℕ → Ω → ℝ)
    (_heig : ∀ N, Measurable (eig N)) (_hY : ∀ N, Measurable (Y N))
    (H : (N : ℕ) → Measure (Orthogonal N)) [∀ N, IsProbabilityMeasure (H N)]
    [∀ N, (H N).IsMulRightInvariant]
    (_hlaw : ∀ N, ConditionalFieldOrbitLaw P (fun ω => (eig N ω,fun _ => 0)) (Y N) (H N))
    (ν : ProbabilityMeasure ℝ) (a b : ℝ)
    (_hcompact : IsCompact (ν : Measure ℝ).support)
    (_hbound : (ν : Measure ℝ).support ⊆ Icc a b)
    (_ha : a∈(ν : Measure ℝ).support) (_hb : b∈(ν : Measure ℝ).support)
    (_hno : ∀ᵐ ω ∂P, ∀ ε : ℝ, 0 < ε → ∀ᶠ N in atTop,
      ∀ i, a-ε ≤ eig N ω i ∧ eig N ω i ≤ b+ε)
    (_hweak : ∀ᵐ ω ∂P, Tendsto (fun k =>
      empiricalSpectralLaw (Nat.succ_pos k) (eig (k+1) ω)) atTop (𝓝 ν)),
    ∀ᵐ ω ∂P, Tendsto (fun N => Y N ω) atTop
      (𝓝 (variationalFunctional (measureR (ν : Measure ℝ) b)).toReal) := by
  sorry
theorem random_field_pressure_tendsto_ae_unconditional :
  ∀ {Ω : Type*} [MeasurableSpace Ω] (P : Measure Ω) [IsProbabilityMeasure P]
    (d : (N : ℕ) → Ω → FieldSpectralData N) (Y : ℕ → Ω → ℝ)
    (_hd : ∀ N, Measurable (d N)) (_hY : ∀ N, Measurable (Y N))
    (H : (N : ℕ) → Measure (Orthogonal N)) [∀ N, IsProbabilityMeasure (H N)]
    [∀ N, (H N).IsMulRightInvariant]
    (_hlaw : ∀ N, ConditionalFieldOrbitLaw P (d N) (Y N) (H N))
    (ν : ProbabilityMeasure ℝ) (a b : ℝ)
    (_hcompact : IsCompact (ν : Measure ℝ).support)
    (_hbound : (ν : Measure ℝ).support ⊆ Icc a b)
    (_ha : a∈(ν : Measure ℝ).support) (_hb : b∈(ν : Measure ℝ).support)
    (_hno : ∀ᵐ ω ∂P, ∀ ε : ℝ, 0 < ε → ∀ᶠ N in atTop,
      ∀ i, a-ε ≤ (d N ω).1 i ∧ (d N ω).1 i ≤ b+ε)
    (_hweak : ∀ᵐ ω ∂P, Tendsto (fun k =>
      empiricalSpectralLaw (Nat.succ_pos k) (d (k+1) ω).1) atTop (𝓝 ν))
    (ξ : ProbabilityMeasure ℝ) (_hξ : Integrable (fun x : ℝ => x) (ξ : Measure ℝ))
    (_hw : ∀ᵐ ω ∂P, Tendsto (fun k => fieldWassersteinOne
      (empiricalSpectralLaw (Nat.succ_pos k) (d (k+1) ω).2) ξ) atTop (𝓝 0)),
    ∀ᵐ ω ∂P, Tendsto (fun N => Y N ω) atTop
      (𝓝 (magneticFieldFunctional (ν : Measure ℝ) b ξ)) := by
  sorry
theorem gaussianPattern_pressure_limit_unconditional :
  ∀ (α : ℝ) (_hα : 0 < α)
    {Ω : Type u} [MeasurableSpace Ω] (P : Measure Ω) [IsProbabilityMeasure P]
    (Z : (N : ℕ) → Ω → EuclideanSpace ℝ (Fin N × Fin (gaussianPatternCount α N)))
    (_hZ : ∀ N, Measurable (Z N)) (_hlaw : ∀ N, HasLaw (Z N) (stdGaussian _) P)
    (c : ℝ),
    TendstoInMeasure P (fun k ω => gaussianPatternPressure (N := k+1) (m := gaussianPatternCount α (k+1)) c (Z (k+1) ω)) atTop
      (fun _ => gaussianPatternLimit α c) ∧
    Tendsto (fun k => eLpNorm (fun ω => gaussianPatternPressure (N := k+1) (m := gaussianPatternCount α (k+1)) c (Z (k+1) ω)-
      gaussianPatternLimit α c) 1 P) atTop (𝓝 0) ∧
    Tendsto (fun k => ∫ ω, gaussianPatternPressure (N := k+1) (m := gaussianPatternCount α (k+1)) c (Z (k+1) ω) ∂P) atTop
      (𝓝 (gaussianPatternLimit α c)) := by
  sorry
theorem gaussianPattern_ground_limit_unconditional :
  ∀ (α : ℝ) (_hα : 0 < α)
    {Ω : Type u} [MeasurableSpace Ω] (P : Measure Ω) [IsProbabilityMeasure P]
    (Z : (N : ℕ) → Ω → EuclideanSpace ℝ (Fin N × Fin (gaussianPatternCount α N)))
    (_hZ : ∀ N, Measurable (Z N)) (_hlaw : ∀ N, HasLaw (Z N) (stdGaussian _) P)
    (ε : ℝ),
    ∃ e : ℝ,
      TendstoInMeasure P (fun k ω => gaussianPatternGroundEnergy ε (Z (k+1) ω)) atTop (fun _ => e) ∧
      Tendsto (fun k => eLpNorm (fun ω => gaussianPatternGroundEnergy ε (Z (k+1) ω)-e) 1 P)
        atTop (𝓝 0) ∧
      Tendsto (fun k => ∫ ω, gaussianPatternGroundEnergy ε (Z (k+1) ω) ∂P) atTop (𝓝 e) ∧
      Tendsto (fun β => gaussianPatternLimit α (ε*β)/β) atTop (𝓝 e) := by
  sorry
theorem gaussianPattern_norm_limits_unconditional :
  ∀ (α : ℝ) (_hα : 0 < α)
    {Ω : Type u} [MeasurableSpace Ω] (P : Measure Ω) [IsProbabilityMeasure P]
    (Z : (N : ℕ) → Ω → EuclideanSpace ℝ (Fin N × Fin (gaussianPatternCount α N)))
    (_hZ : ∀ N, Measurable (Z N)) (_hlaw : ∀ N, HasLaw (Z N) (stdGaussian _) P),
    ∃ eplus eminus : ℝ, 0 ≤ eplus ∧ eminus ≤ 0 ∧
      Tendsto (fun β => gaussianPatternLimit α β/β) atTop (𝓝 eplus) ∧
      Tendsto (fun β => gaussianPatternLimit α (-β)/β) atTop (𝓝 eminus) ∧
      (TendstoInMeasure P (fun k ω => ‖gaussianPatternOperator (Z (k+1) ω)‖/(k+1)) atTop
        (fun _ => Real.sqrt (2*eplus)) ∧
       Tendsto (fun k => eLpNorm (fun ω => ‖gaussianPatternOperator (Z (k+1) ω)‖/(k+1)-
        Real.sqrt (2*eplus)) 1 P) atTop (𝓝 0)) ∧
      (TendstoInMeasure P (fun k ω =>
        (Finset.univ.inf' Finset.univ_nonempty (fun σ : Spin (k+1) => ‖gaussianPatternSum (Z (k+1) ω) σ‖))/(k+1))
        atTop (fun _ => Real.sqrt (-2*eminus)) ∧
       Tendsto (fun k => eLpNorm (fun ω =>
        (Finset.univ.inf' Finset.univ_nonempty (fun σ : Spin (k+1) => ‖gaussianPatternSum (Z (k+1) ω) σ‖))/(k+1)-
          Real.sqrt (-2*eminus)) 1 P) atTop (𝓝 0)) := by
  sorry
end InvariantIsing
end
DEFS(68): abbrev Spin, def spinValue, def logPartition, def fieldEnergy, abbrev Rotation, abbrev Orthogonal, def spinVector, def rotatedEnergy, def rotatedPressure, lemma orthogonal_mulVec_norm_sq, def matrixRotation, structure OverlapPath, def pathMeasure, def deficit, def gaussianOperator, structure FieldStep, def fieldFunction, def fieldIncrement, def fieldValue, def fieldPairing, def entropyFunctional, def spectralFunctional, def variationalFunctional, def measureResolvent, def measureInverse, def measureR, def finiteSpectralMeasure, theorem finiteSpectralMeasure_probability, lemma empiricalSpectralWeight_sum, def empiricalSpectralLaw
## PAPER All-temperature-pressure-for-orthogonally-invariant-Ising-spin-glasses-September-25-2026
ABSTRACT: We determine the limiting pressure of an Ising spin glass with Haar orthogonal eigenvectors, a compact limiting spectral law, and no asymptotic outliers, at every fixed temperature. The pressure converges in expectation and almost surely to a variational formula. We also give the limiting pressure with deterministic external fields whose empirical laws converge in first-moment transport distance, and derive a formula for the zero-field ground-state energy by taking temperature to zero.
[theorem[Limiting pressure]] \label{thm:main} Let $\Lambda_N$ be deterministic real diagonal matrices whose empirical spectral measures converge weakly to a compactly supported probability law $\mu$. Assume that their smallest and largest eigenvalues converge to the respective edges of $\supp\mu$. Let $U_N$ be Haar distributed on $O(N)$, and define $P_N$ using the uniform spin probability in Equation~\eqref{eq:pressure}. With $S$ and $G_1$ as in Equations~\eqref{eq:S}--\eqref{eq:G}, \begin{equation} \lim_{N\to\infty}\E P_N =\lim_{N\to\infty}P_N =\mathcal F(\mu) :=\inf_{p\in\cP}\{S(p)+G_1(p)\}, \label{eq:variational} \end{equation} where the second limit holds almost surely. No independence of the matrices $U_N$ across d
==================
# FAMILY 235: Limiting random SAT thresholds, sharp variance and computability
SCOPE: The random $k$-SAT threshold problem asks whether satisfiability changes at one limiting clause density. The formalization proves that every fixed integer $k\ge3$ has a finite positive threshold $\alpha_k$: for every fixed density $c<\alpha_k$, the satisfiability probability tends to one as the number of variables grows, while for every $c>\alpha_k$ it tends to zero. Clauses use distinct variables with independent uniform signs and are sampled independently with replacement. The statement makes no assertion at the threshold itself. Let $H_n$ be the first unsatisfiable prefix length in random $k$-SAT with independent uniformly signed clauses on $k$ distinct variables, sampled with replacement. The formalization proves $\mathrm{Var}(H_n)=\Theta_k(n)$ for every fixed $k\ge4$. For $k=3$, it proves a positive linear lower bound and an $O(n\log n)$ upper bound. The same upper bounds hold after
## CHALLENGE FixedClauseThreshold  targets=['OAI.FixedClauseThreshold.main'] defs=[]
theorem main (k : ℕ) (hk : 3 ≤ k) : HasLimitingThreshold k := by
  sorry
end FixedClauseThreshold
DEFS(8): abbrev Assignment, abbrev ProperClause, abbrev Formula, def SatisfiesClause, def Satisfies, def Satisfiable, def properSATProbability, def HasLimitingThreshold
## CHALLENGE SATSharpness  targets=['OAI.RandomKSAT.sharpness'] defs=[]
theorem sharpness (k : ℕ) (hk : 3 ≤ k) :
    (∀ γ D A : ℝ, γ < (k : ℝ) / ((k-1 : ℕ) : ℝ) → 0 < D → 0 < A →
      ∀ N : ℕ, ∃ u : ℕ, N ≤ u ∧ k ≤ u ∧ ∃ S : Finset (Assignment u),
        S.Nonempty ∧ A * (u : ℝ) ^ (-((k-1 : ℕ) : ℝ)) ≤ blockKill u (k-1) S 1 ∧
        D * (blockKill u (k-1) S 1) ^ (-γ) < lifetime u k S) ∧
    (∃ u : ℕ → ℕ, ∃ S : ∀ g, Finset (Assignment (u g)),
      (∀ g, 2 ≤ g → k ≤ u g ∧ (S g).Nonempty) ∧
      Asymptotics.IsEquivalent Filter.atTop
        (fun g => blockKill (u g) (k-1) (S g) 1 - blockKill (u g) k (S g) g)
        (fun g => ((2 : ℝ)^k)⁻¹ * (g : ℝ)^(-((k-1 : ℕ) : ℝ)))) ∧
    (¬ ∃ e : ℕ → ℝ,
      Asymptotics.IsLittleO Filter.atTop e (fun g => (g : ℝ)^(-((k-1 : ℕ) : ℝ))) ∧
      ∀ u, k ≤ u → ∀ S : Finset (Assignment u), S.Nonempty → ∀ g, 2 ≤ g →
        blockKill u (k-1) S 1 - e g ≤ blockKill u k S g) := by
  sorry
end RandomKSAT
end
DEFS(16): abbrev Assignment, def Clause, instance clauseFintype, instance clauseMeasurableSpace, instance clauseMeasurableSingletonClass, def Satisfies, abbrev Stream, def clauseLaw, def streamLaw, def SetSAT, def blockKill, def favg., def clauseStep, def alive, def survival, def lifetime
## CHALLENGE SATVariance  targets=['OAI.RandomKSAT.variance_main'] defs=[]
theorem variance_main (k : ℕ) (hk : 3 ≤ k) :
    (∃ C : ℝ, 0 ≤ C ∧ ∀ n : ℕ, k ≤ n →
      variance (H : Stream n k → ℝ) (streamLaw n k) ≤ C * n * ell k n) ∧
    (∀ B : ℝ, 0 < B → ∃ C : ℝ, 0 ≤ C ∧ ∀ n : ℕ, k ≤ n →
      variance (T B : Stream n k → ℝ) (streamLaw n k) ≤ C * n * ell k n) ∧
    (∃ c : ℝ, 0 < c ∧
      (∃ N : ℕ, ∀ n : ℕ, N ≤ n → k ≤ n →
        c * n ≤ variance (H : Stream n k → ℝ) (streamLaw n k)) ∧
      (∀ B : ℝ, U k < B → ∃ N : ℕ, ∀ n : ℕ, N ≤ n → k ≤ n →
        c * n ≤ variance (T B : Stream n k → ℝ) (streamLaw n k))) := by
  sorry
end RandomKSAT
end
DEFS(16): abbrev Assignment, def Clause, instance clauseFintype, instance clauseMeasurableSpace, instance clauseMeasurableSingletonClass, def Satisfies, abbrev Stream, def clauseLaw, def streamLaw, def PrefixSAT, def firstFailure, def H, def cap, def T, def ell, def U
## CHALLENGE SATComputability  targets=['OAI.FixedClauseThreshold.Computability.main'] defs=[]
theorem main : MainStatement := by
  sorry
end FixedClauseThreshold.Computability
DEFS(8): abbrev Assignment, abbrev ProperClause, abbrev Formula, def SatisfiesClause, def Satisfies, def Satisfiable, def properSATProbability, def MainStatement
## PAPER A-Limiting-Satisfiability-Threshold-for-Every-Fixed-Clause-Size-September-25-2026
ABSTRACT: For every fixed integer \(k\ge3\), random \(k\)-SAT with independent uniformly signed clauses on distinct variables, sampled with replacement, has a finite positive limiting satisfiability threshold. We credit Gaia Carenini~\cite{Carenini2026Polynomial} with priority for resolving the satisfiability conjecture. This paper gives an alternative proof, using concentration of a capped last satisfiable index and a comparison between different system sizes.
[theorem] \label{thm:main} For every fixed integer \(k\ge3\), there is a constant \(\alpha_k\in(0,\infty)\) such that, for independent proper uniformly signed \(k\)-clauses sampled with replacement, \[ \lim_{n\to\infty}P_n(\lfloor cn\rfloor) = \begin{cases} 1,&0\le c<\alpha_k,\\ 0,&c>\alpha_k. \end{cases} \]
## PAPER Variance-of-the-Random-k-SAT-Hitting-Time-September-27-2026
ABSTRACT: Let $H_n$ be the index of the first unsatisfiable prefix in random $k$-SAT on $n$ variables, with independent uniformly signed clauses using $k$ distinct variables and sampled with replacement. For every fixed $k\ge4$, we prove $\Var(H_n)=\Theta_k(n)$. For $k=3$, the variance is bounded below by a positive multiple of $n$ and above by a constant multiple of $n\log n$; the companion paper on random 3-SAT sharpens this to $\Theta(n)$. The same upper bounds proved here hold after clipping at any fixed positive multiple of $n$.
[theorem] \label{thm:variance} Fix an integer $k\ge3$, and write \[ \ell_k(n)=\begin{cases}\log(en),&k=3,\\1,&k\ge4,\end{cases} \qquad U_k=\frac{\log2}{-\log(1-2^{-k})}. \] There are constants $C_k,c_k>0$ such that \[ \Var(H_n)\le C_kn\ell_k(n)\quad(n\ge k),\qquad \Var(H_n)\ge c_kn\quad\text{for all sufficiently large }n. \] For every fixed $B>0$ there is $C_{k,B}<\infty$ such that \[ \Var(T_{n,B})\le C_{k,B}n\ell_k(n)\quad(n\ge k). \] If $B>U_k$, then also $\Var(T_{n,B})\ge c_kn$ for all sufficiently large $n$, with the size cutoff allowed to depend on $k$ and $B$.
## PAPER Computing-the-Random-3-SAT-Threshold-September-27-2026
ABSTRACT: The limiting satisfiability threshold of uniform random 3-SAT is a computable real. We credit Gaia Carenini~\cite{Carenini2026Polynomial} with priority for resolving the satisfiability conjecture, which establishes the threshold's existence. We prove that one finite deterministic machine can approximate it to any prescribed accuracy. A deletion estimate gives explicit lower certificates, while a finite hierarchical approximation of the soft pressure gives upper certificates at every larger rational density. A fair search through these certificates halts without requiring a computable rate of finite-size convergence.
[theorem] \label{thm:main} There is a real number $\alpha_3\in(0,\infty)$ such that, for every fixed real $a\ge0$, \[ \lim_{n\to\infty}p(n,\lfloor an\rfloor)= \begin{cases}1,&a<\alpha_3,\\0,&a>\alpha_3.\end{cases} \] There is one finite deterministic Turing machine which, on input $1^r$ for any integer $r\ge1$, halts with a rational number $q_r$ satisfying $|q_r-\alpha_3|\le2^{-r}$. Its only input is the unary precision $1^r$; it uses no oracle, advice, or noncomputable real constant.
==================
# FAMILY 236: The exact factor-of-IID threshold for free Ising spins on trees
SCOPE: The formalized result determines the factor-of-IID threshold for the free zero-field Ising law on the infinite $d$-regular tree. For every $d\ge3$ and $\beta\ge0$, the law is a factor of IID exactly when $\tanh\beta\le1/\sqrt{d-1}$, including equality. The factor uses independent uniform vertex labels and is almost surely equivariant for each fixed tree automorphism. Finitary coding and coding-radius bounds are not included.
## CHALLENGE FreeIsing  targets=['OAI.Problem367.free_ising_factor_iff_threshold'] defs=[]
theorem free_ising_factor_iff_threshold :
    ∀ (d : ℕ) (beta : ℝ), 3 ≤ d → 0 ≤ beta → (IsFactorOfIID d (Real.tanh beta) ↔ Real.tanh beta ≤ 1 / Real.sqrt ((d : ℝ) - 1)) := by
  sorry
end Problem367
end
DEFS(17): abbrev TreeVertex, def treeAdj, structure TreeAut, def relabel, inductive IsingSpin, abbrev IsingSpin.enumList, theorem IsingSpin.enumList_getElem?_ctorIdx_eq, theorem IsingSpin.enumList_nodup, instance isingSpinMeasurable, def uniform01, instance uniform01Probability, def labelMeasure, def ConnectedFinset, def inducedEdges, def freeCylinderWeight, def HasFreeIsingLaw, def IsFactorOfIID
## PAPER The-sharp-factor-of-IID-threshold-for-the-free-Ising-model-on-regular-trees-September-26-2026
ABSTRACT: For every integer \(d\ge3\) and inverse temperature \(\beta\ge0\), the free zero-field ferromagnetic Ising measure on the infinite \(d\)-regular tree is a factor of IID exactly when \(\tanh\beta\le(d-1)^{-1/2}\). We prove the positive implication, including equality, resolving the conjecture of Nam, Sly and Zhang; the strict converse is known. The spin factor can be chosen to commute with every tree automorphism on every label input.
[theorem] \label{thm:main}\label{thm:sharp} For every integer $d\ge3$ and every $\beta\ge0$, the free zero-field Ising law $\mu_{d,\beta}$ is a factor of IID in the sense of \eqref{eq:equivariance} if and only if \[ \tanh\beta\le(d-1)^{-1/2}. \] In this range the factor can be chosen to commute with every automorphism on every label input.
==================
# FAMILY 237: The three-quarter exponent for honeycomb self-avoiding walk
SCOPE: The linked formalization establishes finiteness of the critical bridge measures used in the paper. For every strip height $h\ge1$, the total weight and first length moment of self-avoiding honeycomb bridges from a fixed initial port to a free terminal port are finite. The corresponding sums are also finite when the bridge is confined to the corridor of horizontal width $h(\log h)^2$, including the normalized first-moment sums. These are supporting summability statements. The paper's $h^{4/3+o(1)}$ mean-length law and its central-visit and hexagonal-chord exponents are outside them. The linked formalization proves existence of the infinite-length free energy for the critical honeycomb self-avoiding-walk partition function. For every starting vertex, force direction, and real force parameter, the logarithm of the length-$n$ partition function divided by $n$ converges to its stated free-ene
## CHALLENGE HoneycombBridgeFiniteness  targets=['OAI.PolynomialVacuumBridge.Corridor.finite_bridge_sums'] defs=[]
theorem finite_bridge_sums : FiniteBridgeSums := by
  sorry
end PolynomialVacuumBridge.Corridor
DEFS(13): inductive Vertex, def position, def adjacent, def criticalActivity, def layer, structure BridgePath, def weight, def firstLengthWeight, def bridgeMass, def InLogCorridor, def ConfinedBridgePath, def confinedMass, def FiniteBridgeSums
## CHALLENGE HoneycombFreeEnergy  targets=['OAI.HoneycombForce.logPartition_tendsto'] defs=[]
theorem logPartition_tendsto (o : Vertex) (e : ℂ) (s : ℝ) :
    Tendsto (logPartition o e s) atTop (𝓝 (freeEnergy o e s)) := by
  sorry
end HoneycombForce
end
DEFS(15): structure Vertex, def up, def down, def rowSpacing, def position, def rho, def neighbors, def walkLists, def saws, def endpoint, def displacement, def projection, def partition, def logPartition, def freeEnergy
## CHALLENGE CriticalStripMass  targets=['OAI.CriticalStrip.critical_strip_mass'] defs=[]
theorem critical_strip_mass : CriticalStripMass := by
  sorry
end
end CriticalStrip
DEFS(22): def rho, def c, def lambda, def d, def C, def eta, abbrev Triangle, def up, def down, def upDownAdjacent, def adjacent, def IsPath, def archWeight, def bridgeWeight, def K, def bridgeKernel, def archMass, def bridgeMass, def moment, def StripSumsFinite, def Comparable, def CriticalStripMass
## CHALLENGE HoneycombBridgeMassSupport  targets=['OAI.CriticalHoneycomb.finiteBridgeMassEstimate'] defs=[]
theorem finiteBridgeMassEstimate : FiniteBridgeMassEstimate := by
  sorry
end CriticalHoneycomb
DEFS(15): abbrev Center, def up, def down, def Adj, def rowSpacing, def centerPosition, structure Port, def Port.position, def IsTrace, def kappa, def weight, def strip, def StrictBridge, def bridgeMass, def FiniteBridgeMassEstimate
## PAPER Polynomial-vacuum-representations-and-bridge-mass-for-honeycomb-walks-September-26-2026
ABSTRACT: We prove that, under the all-length critical measure, a honeycomb bridge crossing a strip of $h$ layers, with its initial port fixed and its terminal port free, has mean length $h^{4/3+o(1)}$. We also obtain central visit probability $R^{-2/3+o(1)}$ and mean length $R^{4/3+o(1)}$ for macroscopic free-boundary chords in a regular hexagon.
[theorem[Strip mass and bridge length]] \label{thm:pv:bridge} As the integer layer height $h$ tends to infinity, \[ b_h=h^{-1/4+o(1)},\qquad \ell_h=h^{13/12+o(1)},\qquad \mathbb E_h|\gamma|=h^{4/3+o(1)}. \] All three sums are finite. These exponents are unchanged if the paths are also confined to horizontal distance $h\log^2h$ from their initial port.
## PAPER Renewal-and-changes-of-law-for-critical-honeycomb-walks-September-26-2026
ABSTRACT: For critical honeycomb self-avoiding walk, we prove spatial exponent $3/4$ for the infinite irreducible-bridge law and for bridges of every sufficiently large compatible even length. We establish the corresponding thermal laws at every large discount scale, including all positive length and spatial moments. For unrestricted uniform walks, the endpoint lower law holds on a common set of lengths of natural density one. We also determine the near-critical exponential correlation scale and small-force free-energy exponent, and prove spatial local lower bounds that permit conditioning on a prescribed terminal vertex.
[theorem[Finite bridge estimates]] \label{R:renew:finite-input} There are constants $c,C>0$ such that, for every sufficiently large integer $h$, \[ c h^{-1/4}\le B_h\le C h^{-1/4},\qquad M_h\le C h^{13/12},\qquad B_h\{L\ge c h^{4/3}\}\ge c h^{-1/4}. \] For all $h\ge1$ and $x\ge1$, one also has \[ B_h\{D>x\}\le C x^{-1/4}. \] The same estimates hold in the symmetry-related pure directions.
## PAPER Critical-strip-crossing-mass-on-the-honeycomb-lattice-September-26-2026
ABSTRACT: At the critical weight of the regular honeycomb lattice, the total weight of self-avoiding paths crossing a strip of height $N$ is comparable to $N^{-1/4}$. The first horizontal-displacement moment of return paths is comparable to $N^{3/4}$.
[theorem[Critical strip mass]] \label{thm:strip} For every integer $N\ge1$, all sums in \eqref{eq:01-strip-quantities} are finite. With constants independent of $N$, \begin{equation}\label{eq:01-strip-result} c\mathcal A_N+\mathcal B_N=1,\qquad m_{N+1}-m_N\asymp\mathcal B_N,\qquad m_N\asymp N^{3/4},\qquad \mathcal B_N\asymp N^{-1/4}. \end{equation} Moreover, $\mathcal B_N$ is nonincreasing in $N$.
## PAPER Critical-honeycomb-chords-with-prescribed-boundary-endpoints-September-26-2026
ABSTRACT: Critical self-avoiding walks between prescribed, macroscopically separated boundary ports of a regular honeycomb hexagon have length $R^{4/3+o(1)}$ in probability, where $R$ is the scale of the hexagon. We prove the corresponding statements for half-plane arches, parallel cuts and nonparallel pure cuts. The half-plane law also has mean length $R^{4/3+o(1)}$. A separate strip argument gives endpoint mean laws on one density-one set of heights and in an aligned, critically weighted mixture of all even heights in a macroscopic interval.
[theorem[Prescribed boundary endpoints]] \label{c:main} Let $D_R$ be convex pure lattice hexagons which, after scaling by $R$, converge to a regular hexagon. Let $a_R,b_R$ be boundary ports whose scaled limits are distinct points in the relative interiors of sides. Then, for every $\varepsilon>0$, the critical chord law satisfies \[ \mathbb P_{D_R;a_R,b_R} \{R^{4/3-\varepsilon}\le L(\gamma)\le R^{4/3+\varepsilon}\} \longrightarrow1. \] The same conclusion holds in a full half-plane for prescribed boundary ports at distance $R$, in a strip of height comparable to $R$ for one prescribed port on each of the two opposite boundary cuts, at mutual distance $O(R)$, and in a wedge of angle $\pi/3$ or $2\pi/3$ formed by two nonparallel pure
==================
# FAMILY 238: Optimal logarithmic mixing of the Thorp shuffle
SCOPE: The formalization proves optimal-order mixing of the Thorp shuffle on $2^d$ cards. After $1600d$ complete shuffles, the full permutation law converges in total variation to uniform as $d\to\infty$, uniformly over initial decks. Together with the support lower bound of $2d-O(1)$, this gives mixing time $\Theta(d)=\Theta(\log(2^d))$. The linked supporting results include frame and conditional-list estimates, regular trace and spectral bounds, signed moments, and full-density $L^2$ control. They also bound reciprocal Specht-dimension sums and give the eight-block Fourier estimate used in the mixing argument. The formalized supporting result turns bounds on partial-permutation cosets into Fourier bounds. Partition a finite set into $b\ge1$ nonempty blocks, and let $f\ge0$ be a subprobability weight on its symmetric group whose left-coset masses for each block subgroup are at most $B$. For ev
## CHALLENGE ThorpFirstReciprocal  targets=['OAI.Thorp.Current.first_reciprocal_main'] defs=[]
theorem first_reciprocal_main :
    (BddAbove (Set.range (fun n : {n : ℕ // 1 ≤ n} => reciprocalFirst n.val)) ∧
    (∀ n : ℕ, 1 ≤ n → reciprocalFirst n ≤ C1) ∧
    Tendsto exceptionalFirst atTop (nhds 0)) ∧
    (∀ (d : ℕ) (_hd : 3 ≤ d)
    (e : Position d ≃ Fin 8 × Fin (2 ^ (d - 3)))
    {E : Type uE} [NormedAddCommGroup E] [InnerProductSpace ℂ E]
    [FiniteDimensional ℂ E]
    (ρ : Representation ℂ (Equiv.Perm (Position d)) E)
    [Representation.IsIrreducible ρ]
    (_ : ∀ g x y, ⟪ρ g x, ρ g y⟫_ℂ = ⟪x, y⟫_ℂ)
    (ν : Equiv.Perm (Position d) → ℝ)
    (_ : ∀ g, 0 ≤ ν g) (_ : ∑ g, ν g = 1)
    (_ : ∀ (i : Fin 8) (g : Equiv.Perm (Position d)),
      ∑ h : Equiv.Perm (Fin (2 ^ (d - 3))),
          ν (g * Block.embedding e (Pi.mulSingle i h)) ≤
        4 * (Fintype.card (Equiv.Perm (Fin (2 ^ (d - 3)))) : ℝ) /
          Fintype.card (Equiv.Perm (Position d))),
    ‖LinearMap.toContinuousLinearMap (Fourier.integrated ρ (fun g => (ν g : ℂ)))‖ ≤
      Real.sqrt (32 * C1) * (Module.finrank ℂ E : ℝ) ^ (-5 / 16 : ℝ)) := by
  sorry
end Current
end Thorp
end
DEFS(34): abbrev Position, def perm, def hom, def embedding, def integrated, abbrev Cells, def rowCellsEquiv, def ofPartition, def longest, def cyclic, def rep, def alternator, def Tabloid, instance tabloidFinite, instance tabloidFintype, instance tabloidAction, def baseTabloid, def fiberGroup, def complexSign, def tableauRow, def tableauCol, def tabloidRep, def columnAlternator, def polytabloid, def module, abbrev Shape, def canonicalTableau, abbrev Space, def degree, abbrev NShape
## CHALLENGE ThorpRemaining  targets=['OAI.ThorpResults.remaining_main'] defs=[]
theorem remaining_main :
    FrameMain ∧ InformationMain ∧ SpectrumMain ∧ SignedMain ∧
      DegreeSavingMain ∧ FullDensityMain ∧ ForwardMixingMain ∧ OptimalOrderMain := by
  sorry
end ThorpResults
end
DEFS(94): abbrev Position, abbrev State, def Coins, instance coinsFintype, instance coinsInhabited, def pairSwitch, def rotate, def step, abbrev History, def run, def fairMass, def law, def uniform, def tv, def distance, def lawFrom, abbrev LabelList, def coordinateRun, def images, def listTV, def mixingTime, abbrev Card, def switchFun, theorem switchFun_involutive, def pairSwitch, def Coins, def rotate, def step, def run, def law
## CHALLENGE PartialPermutation  targets=['OAI.PartialPermutation.complementaryCosets_finite'] defs=[]
theorem complementaryCosets_finite : ComplementaryCosetsFiniteStatement := by
  sorry
end
end PartialPermutation
DEFS(17): def IsUnitary, def hsNormSq, def complexFourier, def componentSimple, instance components_finite, def regularRep, abbrev IrreducibleIndex, instance irreducibleIndex_fintype, abbrev irreducibleSpace, abbrev irreducibleDegree, def mass, def LeftCosetCap, def blockSubgroup, def inverseDegreeSum, def symmetricInverseDegreeSum, def symmetricDegreeConstant, def ComplementaryCosetsFiniteStatement
## CHALLENGE ThorpRouting  targets=['OAI.ThorpNine.main'] defs=[]
DEFS(382): abbrev Card, def switchFun, theorem switchFun_involutive, def pairSwitch, def Butterfly, def childLift, def butterflyPerm, def SwitchIndex, def decodeButterfly, abbrev Cell, def row, def col, lemma row_lt_colLen, def rowIndex, abbrev Tabloid, def baseTabloid, def tabloidAct, lemma tabloidAct_apply, lemma tabloidAct_one, lemma tabloidAct_mul, def tabloidRep, def delta, def colGroup, def permSign, def alternator, def polytabloid, def space, lemma orbit_mem_space, lemma action_mem_space, def subrepresentation
## CHALLENGE OccupiedOverlap  targets=['OAI.RowColumn.occupied_overlap_endpoint', 'OAI.RowColumn.occupied_overlap'] defs=[]
DEFS(42): abbrev Cell, def row, def col, lemma row_lt_colLen, def rowIndex, abbrev Tabloid, def baseTabloid, def tabloidAct, lemma tabloidAct_apply, lemma tabloidAct_one, lemma tabloidAct_mul, lemma tabloidAct_inv, def tabloidRep, lemma tabloidRep_apply, def delta, def colGroup, def permSign, def alternator, def polytabloid, def space, lemma orbit_mem_space, lemma action_mem_space, def subrepresentation, def representation, abbrev H, def hilbertEquiv, def hilbertSpace, def spaceHilbertEquiv, def unitaryRepresentation, def relabelledUnitary
## CHALLENGE WeightedSweepMoments  targets=['OAI.CubeShuffle.WeightedSweep.weighted_sweep_moments'] defs=[]
theorem weighted_sweep_moments :
    ∃ (W : YoungDiagram → ℝ) (pStar : ℝ) (p : ℕ → ℝ),
      (∀ μ : YoungDiagram, 0 < W μ) ∧
      2 ≤ pStar ∧
      (∀ d : ℕ, 1 ≤ d → 2 ≤ p d ∧ p d ≤ pStar) ∧
      ∀ d : ℕ, 1 ≤ d → ∀ μ : Shapes (2 ^ d),
        dimension μ.1 ^ (3 / 4 : ℝ) ≤ W μ.1 ∧
        W μ.1 ≤ dimension μ.1 ∧
        W μ.1 *
          schattenNorm (V := hilbertSpace μ.1) (fourierSweep d μ) (p d) ^ (p d) ≤ 1 ∧
        ‖fourierSweep d μ‖ ≤ dimension μ.1 ^ (-3 / (4 * pStar)) := by
  sorry
end CubeShuffle.WeightedSweep
end
DEFS(50): abbrev Cell, def row, def col, lemma row_lt_colLen, def rowIndex, abbrev Tabloid, def baseTabloid, def tabloidAct, lemma tabloidAct_apply, lemma tabloidAct_one, lemma tabloidAct_mul, lemma tabloidAct_inv, def tabloidRep, lemma tabloidRep_apply, def delta, def colGroup, def permSign, def alternator, def polytabloid, def space, lemma orbit_mem_space, lemma action_mem_space, def subrepresentation, def representation, abbrev H, def hilbertEquiv, def hilbertSpace, def spaceHilbertEquiv, def unitaryRepresentation, def relabelledUnitary
## CHALLENGE CoordinateTrace  targets=['OAI.ThorpNine.Harmonic.Thorp.LowPlanes.regular_trace_smoothing'] defs=[]
theorem regular_trace_smoothing : MainStatement := by
  sorry
end Thorp.LowPlanes
end ThorpNine.Harmonic
DEFS(59): abbrev Card, def switchFun, theorem switchFun_involutive, def pairSwitch, def Coins, def rotate, def step, def run, def law, lemma card_positions, abbrev Cell, def row, def col, lemma row_lt_colLen, def rowIndex, abbrev Tabloid, def baseTabloid, def tabloidAct, lemma tabloidAct_apply, lemma tabloidAct_one, lemma tabloidAct_mul, def tabloidRep, def delta, def colGroup, def permSign, def alternator, def polytabloid, def space, lemma orbit_mem_space, lemma action_mem_space
## CHALLENGE ThorpWeightedCompatibility  targets=['OAI.ThorpCompatibility.weightedCompatibility_main'] defs=[]
theorem weightedCompatibility_main : WeightedCompatibilityTheorem := by
  sorry
end ThorpCompatibility
DEFS(7): abbrev Rows, abbrev Cols, def Compatible, def uniformMean, def marginalFactor, def weightedCompatibility, def WeightedCompatibilityTheorem
## CHALLENGE SpinAngle  targets=['OAI.SpinAngle.TypeAngle.one_sided_type_angle'] defs=[]
theorem one_sided_type_angle (W : Finset (R × C))
    (D : TypeLabel q) (H : C → TypeLabel q) (K : R → TypeLabel q)
    (hD : D.size = W.card)
    (hH : ∀ j, (H j).size = Fintype.card (TypeBlocks.Fiber (column W) j))
    (hK : ∀ i, (K i).size = Fintype.card (TypeBlocks.Fiber (row W) i)) :
    (‖TypeBlocks.projection (column W) H * TypeBlocks.projection (row W) K * D.projection W‖ ^ 2 ≤
      min 1 (Real.exp (TypeBlocks.entropy H + TypeBlocks.entropy K - D.entropy) *
        (TypeBlocks.dimension H : ℝ) * (TypeBlocks.dimension K : ℝ) * phi W)) ∧
    (min 1 (Real.exp (TypeBlocks.entropy H + TypeBlocks.entropy K - D.entropy) *
        (TypeBlocks.dimension H : ℝ) * (TypeBlocks.dimension K : ℝ) * phi W) ≤
      min 1 (Real.exp (TypeBlocks.entropy H + TypeBlocks.entropy K - D.entropy +
        (Fintype.card R * Fintype.card C - W.card : ℕ)) *
        (TypeBlocks.dimension H : ℝ) * (TypeBlocks.dimension K : ℝ))) ∧
    TypeBlocks.dimension H * TypeBlocks.dimension K ≤
      (W.card + 1) ^ ((Fintype.card R + Fintype.card C) * q * (q - 1)) := by
  sorry
end SpinAngle.TypeAngle
end
DEFS(72): def cyclic, def tensor, lemma tensor_mul, lemma tensor_one, lemma toEuclideanLin_mul, lemma toEuclideanLin_one, def action, def rep, lemma tensor_reindex, def rep, def alternator, lemma alternator_apply, lemma rep_alternator, def complexSign, lemma complexSign_inv, abbrev Cells, instance coloringAction, def reindex, lemma action_site_commute, def columnGroup, abbrev TensorSpace, def alternating, def rowColor, def highest, lemma highest_mem, def ordinary, abbrev Carrier, instance carrierInner, def rep, abbrev Spin
## CHALLENGE SignedSweepMoment  targets=['OAI.SignedSweeps.signed_occurrence_moment_bound'] defs=[]
theorem signed_occurrence_moment_bound :
    ∃ η₀ : ℝ, 0 < η₀ ∧
      ∀ η : ℝ, 0 < η → η < η₀ →
        ∃ κ₀ : ℝ, 0 < κ₀ ∧ κ₀ < η / 256 ∧
          ∀ κ : ℝ, 0 < κ → κ < κ₀ →
            ∃ r : ℕ, 1 ≤ r ∧
              ∀ d : ℕ, 1 ≤ d →
                ∀ lam : Partition (2 ^ d),
                  ∀ (u v l : ℕ) (h : u + v + l = 2 ^ d)
                    (α : Partition u) (β : Partition v) (γ : Partition l),
                    SignedOccurrence h α β γ lam →
                      logMoment (weightedMoment lam r) ≤
                        ((coefficient η d * signedEntropy α β +
                            remainderBudget κ d l : ℝ) : EReal) := by
  sorry
end SignedSweeps
end
DEFS(36): abbrev Partition, abbrev SymmetricGroup, def transpose, def tableau, def rowOf, def colOf, def fiberSubgroup, def rowSubgroup, def colSubgroup, abbrev RegularSpace, def regularIsometry, lemma regularIsometry_apply, def regularRepresentation, lemma regularRepresentation_apply, def polytabloid, def spechtSubrepresentation, def Specht, instance spechtNormedAddCommGroup, instance spechtInnerProductSpace, instance spechtFiniteDimensional, def spechtRepresentation, def spechtDimension, def blockEmbedding, def SignedOccurrence, abbrev BinaryPositions, def positionsEquiv, def coordinateSubgroup, def layerOperator, def sweepOperator, def positiveSquare
## CHALLENGE BinarySweep  targets=['OAI.binary_sweep_contraction_and_mixing'] defs=[]
theorem binary_sweep_contraction_and_mixing :
    BinaryCoordinateSweeps.BinaryContractionTarget ∧
    (∀ d : ℕ, 0 < d → ∑ g : Equiv.Perm (BinaryCoordinateSweeps.Slot d),
      BinaryCoordinateSweeps.binaryLaw d g * BinaryCoordinateSweeps.realSign g = 0) ∧
    BinaryCoordinateSweeps.UniformSweepMixingTarget := by
  sorry
DEFS(18): abbrev Slot, def coordinateLayer, abbrev SweepCoins, def binarySweep, def finiteLaw, def totalVariation, def uniformLaw, def binaryLaw, abbrev RepSpace, def IsUnitaryRep, def averageOperator, def BinaryContractionTarget, def realSign, def convolution, def pointMassOne, def convolutionPower, def sweepLaw, def UniformSweepMixingTarget
## CHALLENGE CoordinateSweeps  targets=['OAI.CoordinateSweeps.conditional_main', 'OAI.CoordinateSweeps.all_grid_moment'] defs=[]
theorem all_grid_moment {r : ℕ} (hr : ScaleLarge r) (hrS : SparseScalar.ScaleReady r)
    (hS : ∀ G : Grid, G.Allowed r → ScalarInduction.MainSizeReady SparseScalar.q G.size)
    {zStar : ℝ} (hζ : SparsePerturb r zStar) {z : ℝ} (hz : z∈Set.Icc 0 zStar) :
    ∀ G : Grid, G.Allowed r → MomentBound G SparseScalar.q z := by
  sorry
/-- One global choice of scale, moment order, and positive perturbation interval. -/
theorem conditional_main : ConditionalMain := by
  sorry
end CoordinateSweeps
end
DEFS(60): structure FiniteLaw, theorem ext, theorem sum_mass, def uniform, def map, abbrev Cube, def pairSwitch, def binaryLayer, def orderedProduct, abbrev BinaryChoices, def binarySweep, def binaryLaw, structure Grid, def size, abbrev Slot, abbrev Line, abbrev Choices, def fiberPerm, def stage, def boundary, def sweep, def Allowed, structure Holes, def Compatible, def Feasible, def lineCount, def cost, def stabilizer, def reference, theorem reference_compatible
## CHALLENGE FourRowPermanent  targets=['OAI.FourRow.robust_permanent'] defs=[]
theorem robust_permanent :
  ∃ p₀ : ℝ, 4 / 3 < p₀ ∧ p₀ < 2 ∧
    ∃ ε : ℝ, 0 < ε ∧ ∀ ν : Law,
      IsProbability ν → totalVariation ν < ε → UniformMarginals ν →
      ∀ f : Functions, (∀ i j, 0 ≤ f i j) →
        permanentExpectation ν f ≤ ∏ i, lpNorm p₀ (f i) := by
  sorry
end FourRow
end
DEFS(9): abbrev Site, abbrev Perm, abbrev Law, abbrev Functions, def IsProbability, def UniformMarginals, def totalVariation, def lpNorm, def permanentExpectation
## PAPER Optimal-order-mixing-of-the-Thorp-shuffle-September-26-2026
ABSTRACT: We prove that the Thorp shuffle on $2^d$ cards mixes in $\Theta(d)$ complete shuffles. The full permutation law after $1600d$ shuffles converges to uniform in total variation as $d\to\infty$, uniformly over the initial deck, while a support count gives a lower bound of $2d-O(1)$.
[theorem[Optimal-order mixing]] \label{thm:mixing} As $d\to\infty$, \[ \|q_d^{*(1600d)}-U_n\|_{\mathrm{TV}}\longrightarrow0. \] For every integer $t\ge0$, \[ \|q_d^{*t}-U_n\|_{\mathrm{TV}} \ge 1-\frac{2^{tn/2}}{n!}. \] Consequently the mixing time at distance $1/4$ satisfies \[ t_{\mathrm{mix}}(d)\ge \left\lceil\frac2n\log_2\frac{3n!}{4}\right\rceil =2d-O(1), \qquad t_{\mathrm{mix}}(d)=\Theta(d). \]
## PAPER From-partial-permutation-information-to-Fourier-bounds-September-26-2026
ABSTRACT: We show how information about partial permutations controls full permutation laws. Let $n$ tend to infinity through multiples of eight. If the images of a uniformly chosen $7n/8$ labels approach the uniform injection law in average total variation, and the sign mean tends to zero, then the product of two independent permutations with the given law converges to uniform on $S_n$.
[theorem[Complementary cosets control Fourier matrices]] \label{l:main} Partition $X$ into $b$ nonempty sets $M_1,\ldots,M_b$. Put $H_i=H_{M_i}$. Suppose $f$ is a nonnegative measure on $G$ of mass at most one and, for every $g\in G$ and $i$, \begin{equation}\label{l:main-cap} f(gH_i)\le \frac{B}{[G:H_i]}. \end{equation} For every $u>0$ and every irreducible $\rho$ of degree $D$, \begin{equation}\label{l:main-hs} \|\widehat f(\rho)\|_{\HS}^2 \le bBC_uD^{-1+(u+2)/b}. \end{equation} There is also an independent orbit-span proof of the bound \begin{equation}\label{l:main-orbit} \|\widehat f(\rho)\|_{\op}^2 \le bBC_uD^{-1+(u+2)/b}. \end{equation} No restriction is imposed on block sizes or on the multiplicities in $\rho|_{H_1\times\cdots\times H_b}$.
## PAPER Conditional-permutations-in-a-revealed-switching-environment-September-26-2026
ABSTRACT: Fix half the labels in a Thorp shuffle on $2^d$ positions and reveal their complete trajectories. We prove that, after an explicit absolute number of coordinate sweeps, the conditional permutation of the remaining labels approaches uniform in expected total variation as $d\to\infty$, uniformly in the initial layout. The resulting constructions give full-deck mixing in a constant multiple of $d$ physical shuffles.
[theorem[Conditional permutation and full-deck mixing]] \label{thm:methods} Let $n=2^d$, and start the shuffle from any deterministic deck. After $J(s_0+1)$ sweeps, where $s_0=400$ and $J=40000$, the conditional free-slot law defined above satisfies \[ \sup_{\text{initial layouts}}\E_{\mathcal E} \|\nu_{\mathcal E}-U_{n/2}\|_{\TV}\longrightarrow0 \qquad(d\longrightarrow\infty). \] Consequently the full-deck law approaches uniform, uniformly in the starting deck, after $16\,040\,400d$ physical shuffles. For every integer $t\ge0$, after $t$ physical shuffles the full-deck distance from uniform is at least $1-2^{tn/2}/n!$. Thus the full-deck mixing time is of order $d$.
## PAPER Routing-densities-and-representation-contraction-for-Thorp-sweeps-September-26-2026
ABSTRACT: For $N=2^d$ cards, we prove that an absolute number of coordinate sweeps of the Thorp shuffle brings the full permutation law to total-variation distance tending to zero from uniform. The mixing time therefore has optimal order $\Theta(\log N)$ in physical shuffles.
[theorem[Routing density and representation contraction]] \label{fac:main} There are absolute constants $\eta,c,C>0$ such that, with $a=1/1000$, \[ \log\E_{y\sim u_{N,k}}R_x(y)^{1+a} \le Ck(k/N)^\eta \qquad(1\le k\le N), \] uniformly over every starting injection $x$. For every sufficiently large dyadic $N$ and every nontrivial irreducible representation, \[ T_N(\lambda)=0\quad\hbox{or}\quad \|T_N(\lambda)\|_{\op}\le D_\lambda^{-c}. \] Consequently an absolute number of forward sweeps has worst-start total-variation distance from uniform tending to zero as $d\to\infty$.
## PAPER Row-column-symmetry-and-contraction-of-coordinate-sweeps-September-26-2026
ABSTRACT: We prove that the Thorp shuffle on $N=2^d$ labeled cards has full-permutation total-variation mixing time $\Theta(\log N)$ in physical shuffles. An absolute number of coordinate sweeps suffices for the upper bound.
[theorem[Weighted sweep moments]] \label{thm:weighted} There are positive weights $W_\lambda$, an absolute finite $p_*$, and real exponents $2\le p_d\le p_*$ such that, for every $d\ge1$ and every $\lambda\vdash2^d$, \begin{equation}\label{eq:weighted-main} D_\lambda^{3/4}\le W_\lambda\le D_\lambda, \qquad W_\lambda\|K_d(\lambda)\|_{p_d}^{p_d}\le1. \end{equation} Consequently $\|K_d(\lambda)\|_{\rm op}\le D_\lambda^{-3/(4p_*)}$.
## PAPER Random-subspace-tests-and-trace-smoothing-for-coordinate-sweeps-September-26-2026
ABSTRACT: We prove that an absolute number of coordinate sweeps of the Thorp shuffle on $n=2^d$ positions brings the full permutation to total-variation distance at most $\frac12n^{-5}$ from uniform, uniformly over the initial deck. Thus $O(d)$ physical shuffles suffice, which is optimal in order.
[theorem[Regular-trace smoothing]] \label{ten:lowplanes:main} There is an absolute $P\ge2$ such that for every dyadic $n\ge2$, \begin{equation}\label{ten:lowplanes:eq:1} \operatorname{Tr}_{\rm reg}|Q_n|^P\le1+n^{-10}. \end{equation} If $v$ is an integer with $2v\ge P$, then $v$ independent sweeps have total-variation distance at most $\frac12n^{-5}$ from uniform, from every deterministic initial deck. Here $\|\mu-\nu\|_{\rm TV}=\tfrac12\sum_g|\mu(g)-\nu(g)|$.
## PAPER Compatibility-entropy-and-the-spectrum-of-a-Thorp-sweep-September-26-2026
ABSTRACT: We prove that the Thorp shuffle on $n=2^d$ cards mixes in $\Theta(d)$ physical shuffles. After a sufficiently large fixed number of coordinate sweeps, the total-variation distance of the full permutation from uniform tends to zero as $d\to\infty$.
[theorem[Weighted compatibility]] \label{tra:duality:weighted}\label{tra:duality:weighted-statement} There are absolute constants $L,C_0>0$ such that the following holds. Put $m=\sqrt n$, assume $m/2\le A,D\le2m$, and take $m$ sufficiently large that $\theta=1-L/\log m>0$. For all nonnegative functions $w_i:S_D\to[0,\infty)$ and $v_k:S_A\to[0,\infty)$, \begin{equation}\label{tra:duality:eq5} \frac{n!}{|R||C|}\, \mathbb E_U\!\left[\mathbf1_{\mathcal I} \prod_{i=1}^A w_i(r_i)\prod_{k=1}^D v_k(c_k)\right] \le e^{C_0n^{.54}} \prod_{i=1}^A(\mathbb E w_i^{1/\theta})^\theta \prod_{k=1}^D(\mathbb E v_k^{1/\theta})^\theta . \end{equation} The expectations on the right are uniform on the indicated symmetric groups, and logarithms are 
## PAPER Signed-tensor-densities-and-diagram-budgets-for-coordinate-sweeps-September-26-2026
ABSTRACT: We prove that a fixed number of coordinate sweeps of the Thorp shuffle on $2^d$ cards makes the squared $L^2$ distance of the full permutation density from uniform tend to zero as $d\to\infty$. In particular, the total-variation mixing time is $\Theta(d)$ physical shuffles.
[theorem[A moment bound for every signed occurrence]] \label{ten:spin:main}\label{s:spin-moment} For each sufficiently small fixed $\bar\eta>0$, choose a sufficiently small $\bar\kappa>0$ with $\bar\kappa<\bar\eta/256$. There is an integer $r\ge1$, depending only on these fixed constants, such that for every $d\ge1$, every $\lambda\vdash n=2^d$, and every occurrence~\eqref{ten:spin:eq:1}, \begin{equation}\label{ten:spin:eq:3} \log\!\left(D_\lambda\operatorname{Tr}_{V_\lambda}(B_n^*B_n)^r\right) \le\eta_d F(\alpha,\beta)+g_n(l), \end{equation} where \[ \eta_d=\bar\eta\left(1-\frac1{2\sqrt d}\right),\qquad \kappa_d=\bar\kappa\left(1-\frac1{2\sqrt d}\right),\qquad g_n(l)=\max\{0,\kappa_d l\log n-l\log(n/l)\}. \] Set $g_n(0)=0$ and interpret the lo
## PAPER Conditional-coordinate-sweeps-and-analytic-transfer-September-26-2026
ABSTRACT: For coordinate sweeps with near-uniform line laws and line sizes among powers of two in a suitable fixed interval, we prove a Schatten-moment bound after conditioning on any feasible collection of prescribed card trajectories. An analytic transfer to binary sweeps then shows that a fixed number of sweeps mixes the Thorp shuffle on $2^d$ cards in $O(d)$ physical steps, matching the order of the support lower bound.
[theorem[Binary sweep contraction]] \label{thm:binary} There are absolute constants \(g>0\) and \(d_0\) such that, for \(d\ge d_0\) and every \(\lambda\vdash 2^d\), \[ \|K_\lambda\|_{\op}\le D_\lambda^{-g}. \] The sign representation is annihilated. There is an absolute positive integer \(w\) such that the law after \(w\) independent sweeps converges to uniform in total variation as \(d\to\infty\), uniformly over deterministic initial decks.
## PAPER A-strict-four-row-permanent-inequality-and-permutation-moments-September-26-2026
ABSTRACT: We prove a permanent inequality with exponent strictly below two for laws on $S_4$ sufficiently close to uniform and with exactly uniform coordinate marginals. Applied to a four-row recursion, it shows that an absolute number of coordinate sweeps brings the full permutation of the Thorp shuffle on $N=2^d$ cards to total-variation distance tending to zero from uniform as $N\to\infty$. Thus the mixing time has the optimal order $O(\log N)$ in physical shuffles.
[theorem[A robust four-row inequality]] There are absolute constants $p_0\in(4/3,2)$ and $\varepsilon>0$ with the following property.\label{thm:permanent} Let $\nu$ be a probability measure on $S_4$ such that \[ \|\nu-u\|_{\TV}<\varepsilon, \qquad \nu\{\pi:\pi(i)=j\}=\frac14\quad(1\le i,j\le4). \] Then every four nonnegative functions on $\{1,2,3,4\}$ satisfy \begin{equation}\label{eq:permanent} \E_\nu\prod_{i=1}^4f_i(\pi(i))\le\prod_{i=1}^4\|f_i\|_{p_0}. \end{equation}
==================
# FAMILY 240: Shelah's eventual categoricity and the prescribed-threshold obstruction
SCOPE: Under the continuum hypothesis, the formalized result refutes the proposed transfer of categoricity down to the Hanf threshold. It gives an abstract elementary class in a countable relational language, with Löwenheim–Skolem number $\aleph_0$, that has two nonisomorphic models at $\beth_{\omega_2}=h(\aleph_0)$ but is categorical in every cardinal at least $\beth_{(2^{\aleph_1})^+}$. No amalgamation, joint embedding, tameness, or absence-of-maximal-models assumption is imposed. The later canonical-point obstruction and the separate eventual-categoricity theorem are not included.
## CHALLENGE CHObstruction  targets=['OAI.CHObstruction.main'] defs=[]
theorem main (hCH : CH.{u}) :
    ∃ (L : ℕ → Type), Countable (Σ n, L n) ∧
      ∃ K : ClassData.{u} L, K.IsAEC ∧ K.HasLSNumber ℵ₀ ∧
        endpoint = hanf (ℵ₀ : Cardinal.{u}) ∧ K.TwoModels endpoint ∧
        ∀ μ, tailThreshold ≤ μ → K.Categorical μ := by
  sorry
end CHObstruction
end
DEFS(14): structure RelModel, structure IsSubstructure, structure Iso, def IsUnion, structure ClassData, def LSBound, def HasLSNumber, structure IsAEC, def Categorical, def TwoModels, def CH, def hanf, def endpoint, def tailThreshold
## PAPER A-CH-Obstruction-to-a-Prescribed-Categoricity-Threshold-September-24-2026
ABSTRACT: Assuming the continuum hypothesis, we construct an abstract elementary class with L\"owenheim--Skolem number \(\aleph_0\) that is categorical in every sufficiently large cardinal but has at least two nonisomorphic models of cardinality \(\beth_{\omega_2}\). Thus categoricity does not transfer down to the proposed bound \(\beth_{(2^{\aleph_0})^+}\), which equals \(\beth_{\omega_2}\) under CH. Consequently, if ZFC is consistent, the prescribed-threshold form of Shelah's categoricity conjecture is not provable in ZFC.
[theorem] \label{thm:main} Assume the continuum hypothesis. There is an abstract elementary class \(K\) in a countable finitary relational language such that \begin{enumerate}[label=\textup{(\roman*)}] \item \(\LS(K)=\aleph_0\); \item \(K\) has at least two nonisomorphic models of cardinality \(\beth_{\omega_2}=H(K)\); \item putting \(\Lambda=\beth_{(2^{\aleph_1})^+}\), the class \(K\) is categorical in every cardinal \(\mu\ge\Lambda\). \end{enumerate} In particular, \(\lambda=\Lambda^+>H(K)\) is a categoricity cardinal from which downward transfer to \(H(K)\) fails.
==================
# FAMILY 241: Rigidity of the Turing degrees
SCOPE: The rigidity problem asks whether the ordering of Turing degrees by relative computability has any nontrivial automorphism. The formalized result gives a negative answer: every order automorphism of the full Turing degrees of subsets of $\mathbb N$ fixes every degree, with no definability or genericity assumption. The additional representation corollaries are not included.
## CHALLENGE DegreeRigidity  targets=['OAI.TuringRigidity.ManuscriptMain.rigidity'] defs=[]
theorem rigidity : MainTheorem := by
  sorry
end ManuscriptMain
end TuringRigidity
DEFS(6): abbrev Oracle, def oracleFunction, def Reduces, def Degree, instance oraclePreorder, def MainTheorem
## PAPER Rigidity-of-the-Turing-degrees-September-24-2026
ABSTRACT: We prove that every order automorphism of the full partial order of Turing degrees is the identity, resolving the rigidity conjecture for the Turing degrees positively.
[theorem] \label{thm:rigidity} Every order automorphism of the full Turing-degree structure is the identity: \[ \forall\pi\in\Aut(\DT,\leT)\ \forall\mathbf a\in\DT \qquad \pi(\mathbf a)=\mathbf a. \]
==================
# FAMILY 242: Single-fold Diophantine representations and undecidability under an at-most-one-solution promise
SCOPE: The single-fold Diophantine conjecture asks whether every recursively enumerable set has a polynomial representation with a unique auxiliary witness for each member. The formalization establishes this for every recursively enumerable subset of $\mathbb N^n$, $n\ge1$: an integer polynomial has exactly one complete natural-number witness tuple for members and none for nonmembers. The consequence that solvability remains undecidable under an at-most-one-solution promise is not separately formalized.
## CHALLENGE SingleFold  targets=['OAI.SingleFold.main'] defs=[]
theorem main : MainStatement := by
  sorry
end SingleFold
DEFS(3): def evalNat, def Represents, def MainStatement
## PAPER Single-fold-Diophantine-representations-September-24-2026
ABSTRACT: Every recursively enumerable set of natural-number tuples has a polynomial Diophantine representation with exactly one complete auxiliary tuple for each member. This proves the single-fold conjecture and, consequently, the finite-fold conjecture.
[theorem] \label{thm:main} For every integer $n\ge1$ and every recursively enumerable set $S\subseteq\NN^n$, there are an integer $m\ge1$ and a polynomial $P\in\ZZ[A_1,\ldots,A_n,W_1,\ldots,W_m]$ such that, for every $a\in\NN^n$, \[ \#\{w\in\NN^m:P(a,w)=0\}= \begin{cases}1,&a\in S,\\0,&a\notin S.\end{cases} \]
==================
# FAMILY 243: Separating choiceless counting from polynomial time and witnessed choice
SCOPE: The formalized result separates polynomial time from choiceless polynomial time with counting. It gives an explicit query on finite structures with eight relations that is invariant under isomorphism and decidable in polynomial time, but is not definable in the stated hereditarily finite-set language with cardinality and polynomial bounds on stages and intermediate objects. The query applies to all finite inputs without a promise. The separate witnessed-symmetric-choice result is not included. The formalization proves that witnessed symmetric choice strictly increases the expressive power of choiceless polynomial time with counting. It constructs one fixed sentence with exactly one witnessed-choice occurrence that gives a Boolean answer on every finite input, while no sentence of the original counting formalism defines the same class of inputs.
## CHALLENGE ChoicelessPolynomialTime  targets=['OAI.CPTSeparation.main'] defs=[]
theorem main :
    (∀ (A B : Type) [Fintype A] [Fintype B] (S : Input A) (T : Input B),
      S.Iso T → (S.query ↔ T.query)) ∧
    OrdinaryPolynomialTime ∧
    ¬ FullCPT.EvaluationDefinable (fun {_} [_] I => I.query) := by
  sorry
end CPTSeparation
end
DEFS(74): abbrev Scalar, inductive Symbol, structure Input, abbrev Edge, abbrev Config, def coefficient, def incident, def normalized, def consistent, def query, structure Iso, abbrev HF, def mk, def atom, def isSet, def rawElements, def elements, def ofFinset, def rawRank', def rawRank, def rank, def double, def ordinal, abbrev empty, abbrev truth, def boolean, def inputRelation, def allAtoms, def unionHF, def uniqueHF
## CHALLENGE WitnessedChoice  targets=['OAI.WitnessedChoice.main'] defs=[]
DEFS(55): abbrev HF, def mk, def atom, def isSet, def rawElements, def elements, def ofFinset, def rawRank', def rawRank, def rank, def rawMap', def rawMap, def map, def singleton, def double, def pair, def ordinal, def closure, abbrev Scalar, inductive Symbol, structure Input, inductive Term, def dropFree, def Term.free, def Term.wscCount, abbrev Result, def emptyHF, def TC, def unionHF, def uniqueHF
## PAPER Choiceless-polynomial-time-with-counting-does-not-capture-polynomial-time-September-23-2026
ABSTRACT: We prove that choiceless polynomial time with counting does not capture polynomial time on unordered finite structures, confirming the noncapture conjecture of Blass, Gurevich and Shelah. A linear-consistency query over $\mathbb F_3$ in a fixed binary vocabulary is decidable in polynomial time but not in the full counting formalism.
[theorem] \label{thm:main} The query $Q$ on all finite structures in the fixed vocabulary $\tau$ of eight binary relations is isomorphism-invariant and decidable in deterministic polynomial time, but is not definable in full choiceless polynomial time with counting.
## PAPER Witnessed-symmetric-choice-is-strictly-stronger-than-choiceless-polynomial-time-with-counting-September-24-2026
ABSTRACT: We prove that witnessed symmetric choice strictly increases the expressive power of choiceless polynomial time with counting. A fixed sentence with one witnessed-choice occurrence defines a Boolean query on every finite input that is not definable in the original counting formalism.
[theorem] \label{thm:main} There exist a vocabulary \(\tau\) of eight binary relations, a fixed polynomial \(p\), and a \(\CPT+\WSC\) sentence \((\Phi,p)\) with one occurrence of a WSC operator such that: \begin{enumerate}[label=\textup{(\roman*)}] \item \((\Phi,p)\) has a Boolean value on every finite \(\tau\)-structure; \item no \(\CPT\) sentence over \(\tau\) has the same true-model class. \end{enumerate} The \(\CPT\) sentences in \textup{(ii)} may use counting and hereditarily finite sets of unrestricted finite rank.
==================
# FAMILY 244: The Partition Principle does not imply Choice
SCOPE: The Partition Principle says that every surjection admits an injection in the reverse direction. The formalization proves the relative-consistency implication: if ZF is consistent, then so is ZF with the Partition Principle, Choice for ordinal-indexed families, and failure of the Axiom of Choice. The linked model-construction result also constructs a transitive model of the Partition Principle without Choice from an externally countable transitive ground model satisfying the stated axioms, including Choice, and containing an internal strongly inaccessible cardinal. The paper's stronger transitive-model preservation assertions are outside that selected construction.
## CHALLENGE PartitionPrinciple  targets=['OAI.PartitionPilot.Forcing.TransitiveGround.exists_model_partitionPrinciple_without_choice'] defs=[]
theorem exists_model_partitionPrinciple_without_choice
    (pairing : Realize M.sets SetFormula.pairing Fin.elim0)
    (unions : Realize M.sets SetFormula.union Fin.elim0)
    (powers : Realize M.sets powerSet Fin.elim0) (separation : SeparationSchema M.sets)
    (collection : CollectionSchema M.sets) (infinite : Realize M.sets infinity Fin.elim0)
    (choice : Realize M.sets SetFormula.choice Fin.elim0)
    (small : M.sets.Countable)
    {K : ZFSet.{u}} (hK : K ∈ M.sets) (standard : GroundStandardInaccessible M K) :
    ∃ N : TransitiveGround.{u}, M.sets ⊆ N.sets ∧ ZFRealization N.sets ∧
      Realize N.sets partitionPrinciple Fin.elim0 ∧
      ¬ Realize N.sets SetFormula.choice Fin.elim0 := by
  sorry
end PartitionPilot.Forcing.TransitiveGround
DEFS(50): inductive SetFormula, def extend, def Realize, def ex, def disj, def imp, inductive BoundedFormula, def imp, def disj, def exMem, def toFormula, def singletonFormula, def unorderedPairFormula, def orderedPairFormula, def pairMembershipFormula, def relationBetweenFormula, def functionFormula, def nonemptyFormula, def choiceFunctionFormula, structure TransitiveGround, structure InjectionCode, def groundEmbeddable, def setTransitive, def ordinalSetProperty, def groundPower, def GroundBelow, def GroundCardinal, def CofinalFunctionCode, def GroundCofinalRegular, def GroundCardinalStrongLimit
## CHALLENGE PartitionConsistency  targets=['OAI.PartitionConsistency.main_consistency'] defs=[]
theorem main_consistency :
    Consistent SetLanguage.ZF → Consistent SetLanguage.targetTheory := by
  sorry
end PartitionConsistency
DEFS(47): inductive Formula, abbrev neg, abbrev iff, def liftRen, def rename, abbrev raise, def instantiate, def close, abbrev Sentence, abbrev Theory, inductive Derives, def Theory.at, def Consistent, def subset, def empty, def nonempty, def unorderedPair, def successor, def orderedPair, def edge, def functionOn, def mapsTo, def surjection, def injection, def transitiveSet, def membershipLinear, def membershipWellFounded, def ordinal, def choiceOn, def nonemptyFamily
## PAPER The-Partition-Principle-does-not-imply-Choice-September-24-2026
ABSTRACT: We prove that the Partition Principle does not imply the Axiom of Choice: if ZF is consistent, then so is ZF with the Partition Principle, Choice for ordinal-indexed families, and the negation of the Axiom of Choice. Separately, over every countable transitive model of ZFC, we construct a transitive symmetric model of this theory with the same ordinals and no new countable sequences of ground elements.
[theorem] \label{thm:main-consistency} If $\ZF$ is consistent, then so is $\ZF+\PP+\ACwo+\neg\AC$.
==================
# FAMILY 245: Weak normalization implies strong normalization in pure type systems
SCOPE: The formalization proves the $\beta$-Barendregt–Geuvers–Klop conjecture for pure type systems: if every legal expression in every valid context has some terminating $\beta$-reduction sequence, then every $\beta$-reduction sequence from every such expression terminates. Reduction is allowed inside type annotations, and the specification may have arbitrary sorts and nonfunctional axioms or rules.
## CHALLENGE TypeSystemNormalization  targets=['OAI.PureTypeSystem.weak_implies_strong'] defs=[]
theorem weak_implies_strong {S : Type u} (P : Specification S)
    (h : SystemWeaklyNormalizing P) : SystemStronglyNormalizing P := by
  sorry
end PureTypeSystem
DEFS(18): inductive Expr, def liftRen, def rename, def liftSub, def subst, def single, def instantiate, structure Specification, inductive Beta, def Converts, def Normal, def WeaklyNormalizing, def StronglyNormalizing, inductive HasType, inductive ValidContext, def Legal, def SystemWeaklyNormalizing, def SystemStronglyNormalizing
## PAPER Weak-and-strong-normalization-in-pure-type-systems-September-25-2026
ABSTRACT: We prove that every weakly $\beta$-normalizing pure type system is strongly $\beta$-normalizing. Both properties quantify over all legal expressions in all valid contexts, and reduction acts inside type annotations. No functionality hypothesis is required. This resolves the $\beta$-Barendregt--Geuvers--Klop conjecture.
[theorem[The $\beta$-Barendregt--Geuvers--Klop conjecture]] \label{thm:main} Let $\mathcal P=(\mathcal S,\mathcal A,\mathcal R)$ be any pure type system. If every legal expression of $\mathcal P$, in every valid context, is weakly $\beta$-normalizing, then every such expression is strongly $\beta$-normalizing. No functionality assumption is imposed on $\mathcal A$ or $\mathcal R$.
==================
# FAMILY 246: Cannon's conjecture
SCOPE: Cannon's conjecture asks whether a hyperbolic group with boundary homeomorphic to the two-sphere acts geometrically on hyperbolic three-space. The formalization proves that such a group admits an isometric action on $\mathbb H^3$ that is proper and cocompact and has finite kernel. Hyperbolicity is expressed through uniformly thin geodesic triangles in a Cayley graph, and the boundary hypothesis is a homeomorphism with $S^2$.
## CHALLENGE CannonGeometricAction  targets=['OAI.CannonRelease.cannon'] defs=[]
theorem cannon (G : Type u) [Group G] [TopologicalSpace G] [DiscreteTopology G]
    (D : CayleyData G) (hthin : D.ThinTriangles)
    (hsphere : Nonempty (Boundary D ≃ₜ SphereTwo)) :
    ∃ ρ : G →* H3Isom, ProperAction ρ ∧ CocompactAction ρ ∧
      (ρ.ker : Set G).Finite := by
  sorry
end CannonRelease
end
DEFS(13): structure CayleyData, def CayleyData.graph, def CayleyData.ThinTriangles, def BasedRay, def raySetoid, def Boundary, abbrev SphereTwo, def HyperbolicThree, def hyperbolicDist, def hyperbolicIsometries, abbrev H3Isom, def ProperAction, def CocompactAction
## PAPER A-Modulus-Proof-of-Cannons-Conjecture-September-23-2026
ABSTRACT: We prove that every hyperbolic group whose boundary is homeomorphic to the two-sphere admits a proper cocompact isometric action on hyperbolic three-space with finite kernel. This resolves Cannon's conjecture positively.
[theorem[Cannon's conjecture]] \label{thm:main} Let $G$ be a hyperbolic group with $\partial G$ homeomorphic to $\Sphere$. There is a homomorphism $\rho:G\to\Isom(\HH^3)$ for which the action on $\HH^3$ is proper and cocompact. Its kernel is finite.
==================
# FAMILY 247: An infinite finitely presented residually finite 2-group and a finitely presented nil algebra
SCOPE: The finitely presented Burnside question asks whether a finitely presented group in which every element has finite order must be finite. The formalization gives a negative answer by constructing an infinite finitely presented periodic group, including a witness realized as a Steinberg group over an algebra of characteristic two. Periodicity means that each element has some finite order; no common exponent is asserted. The paper's separate nil-algebra and radical-algebra conclusions are outside these selected statements.
## CHALLENGE PeriodicGroup  targets=['OAI.SourceBurnside.thm_main'] defs=[]
theorem thm_main : MainStatement ∧ BurnsideStatement := by
  sorry
end SourceBurnside
DEFS(9): structure Root, abbrev Generator, def bracket, def letter, inductive SteinbergRel, def Steinberg, def Periodic, def MainStatement, def BurnsideStatement
## PAPER An-infinite-finitely-presented-periodic-group-September-23-2026
ABSTRACT: We construct an infinite group with an ordinary finite presentation in which every element has finite order, answering the finitely presented Burnside question negatively. We also construct an infinite-dimensional finitely presented nonunital nil associative algebra over $\F_2$ that is Jacobson radical but not nilpotent. Its unitization is finitely presented, algebraic, and infinite-dimensional. These algebras answer the finitely presented nil- and radical-algebra nilpotence questions and the finite-presentation version of Kurosh's algebraic finiteness question negatively.
[theorem] \label{thm:main} There is an infinite periodic group with an ordinary finite presentation. More precisely, the construction below gives a unital associative $\F_2$-algebra $R$ for which $\St_{12}(R)$ is infinite, finitely presented, and periodic.
==================
# FAMILY 248: Thompson's group <i>F</i> is nonamenable
SCOPE: The amenability problem for Thompson's group $F$ asks whether it admits a positive normalized left-invariant mean on bounded real functions. The formalized result rules out such a mean for the standard group of dyadic piecewise-linear homeomorphisms of the interval, proving nonamenability. No explicit boundary constant or prescribed generating set is given.
## CHALLENGE ThompsonNonamenability  targets=['OAI.ThompsonNonamenability.thompson_F_nonamenable_composition'] defs=[]
theorem thompson_F_nonamenable_composition :
    ∃ group : Group F, letI := group;
      (∀ (h g : F) (x : UnitInterval),
        (h * g).val.toHomeomorph x = h.val.toHomeomorph (g.val.toHomeomorph x)) ∧
      ¬ Nonempty (InvariantMean F) := by
  sorry
end ThompsonNonamenability
end
DEFS(11): abbrev UnitInterval, def unitIntervalZero, def unitIntervalOne, structure IntervalHomeomorph, def IsDyadic, structure DyadicPLWitness, def HasDyadicPLPieces, def F, abbrev BoundedReal, def leftPull, structure InvariantMean
## PAPER Thompsons-group-F-is-nonamenable-September-23-2026
ABSTRACT: We prove that Thompson's group \(F\) is nonamenable. This confirms Geoghegan's conjecture and resolves the amenability problem for \(F\).
[theorem] \label{thm:main} Thompson's group \(F\) is not amenable.
==================
# FAMILY 249: A finitely generated Eilenberg–Ganea counterexample
SCOPE: The Eilenberg–Ganea conjecture predicts that a group of integral cohomological dimension two has a two-dimensional classifying space. The formalization constructs a finitely generated residually finite group of cohomological dimension two that has a three-dimensional classifying space but no two-dimensional one. Thus its geometric dimension is three, contradicting the conjecture.
## CHALLENGE EilenbergGanea  targets=['OAI.EilenbergGanea.source_main'] defs=[]
theorem source_main :
    Group.FG SourceGroup ∧ Group.ResiduallyFinite SourceGroup ∧
    cohomologicalDimension SourceGroup = 2 ∧
    HasClassifyingSpace.{0} SourceGroup 3 ∧
    ¬ HasClassifyingSpace.{u} SourceGroup 2 := by
  sorry
end EilenbergGanea
end
DEFS(25): def seedWord, def boundaryLength, abbrev RoseVertex, abbrev SeedVertex, abbrev CircleEdge, abbrev Sector, abbrev SeedEdge, abbrev SeedCell, def circleStart, def circleEnd, def sectorLetter, def sectorCircleEdge, def sectorStart, def nextSector, def edgeVertices, def sectorEdges, def sectorVertices, def properFace, def seedGraph, def artinRelations, abbrev ArtinGroup, def height, abbrev SourceGroup, def cohomologicalDimension, def HasClassifyingSpace
## PAPER A-finitely-generated-counterexample-to-the-Eilenberg-Ganea-conjecture-September-23-2026
ABSTRACT: We construct a finitely generated residually finite group of integral cohomological dimension two and geometric dimension three, disproving the Eilenberg--Ganea conjecture.
[theorem] \label{thm:main} There is a finitely generated residually finite group $G$ such that \[ \cdim G=2,\qquad \gdim G=3. \] One may take $G$ to be the height kernel in the right-angled Artin group associated to a finite acyclic flag triangulation of the presentation complex \begin{equation} \label{eq:seed-presentation-intro} \langle x,y\mid x^2=y^5,\ x^2=(xy^{-1})^3\rangle. \end{equation} No two-dimensional classifying space for this $G$ exists, regardless of the number of its cells.
==================
# FAMILY 250: Boone–Higman embeddings with higher finiteness
SCOPE: The Boone–Higman conjecture characterizes finitely generated groups with decidable word problem by embeddings into finitely presented simple groups. The formalization proves the equivalence in full: a finitely generated group has a computable word problem for a finite generating set exactly when it embeds by an injective homomorphism into a finitely presented simple group. The formalization proves the higher-finiteness strengthening of the Boone–Higman conjecture: every finitely generated group with decidable word problem embeds by an injective homomorphism into a nontrivial simple group of type $F_\infty$. Here type $F_\infty$ means that the group has a classifying CW complex with finitely many cells in each dimension. No additional finiteness property of the original group is assumed. The formalized result constructs one group $H$ of type $F_\infty$ containing every finitely presented 
## CHALLENGE BooneHigman  targets=['OAI.FiniteAlgebraicEnvelopes.main'] defs=[]
theorem main (GroupType : Type u) [Group GroupType] [Group.FG GroupType] :
    HasDecidableWordProblem GroupType ↔ EmbedsInFinitelyPresentedSimpleGroup GroupType := by
  sorry
end FiniteAlgebraicEnvelopes
DEFS(4): abbrev Word, def evalWord, def HasDecidableWordProblem, def EmbedsInFinitelyPresentedSimpleGroup
## CHALLENGE SimpleOvergroups  targets=['OAI.SimpleFInftyOvergroups.main'] defs=[]
theorem main (G : Type u) [Group G] [Group.FG G]
    (hG : HasDecidableWordProblem G) :
    ∃ (H : Type u) (_ : Group H), Nontrivial H ∧ IsSimpleGroup H ∧
      HasTypeFInfty H ∧ ∃ f : G →* H, Function.Injective f := by
  sorry
end SimpleFInftyOvergroups
DEFS(3): def evalWord, def HasDecidableWordProblem, def HasTypeFInfty
## CHALLENGE UniversalFInfinity  targets=['OAI.UniversalFInfinity.universal_group_of_type_FInfinity'] defs=[]
theorem universal_group_of_type_FInfinity :
    ∃ (H : Type u) (groupH : Group H),
      @HasTypeFInfinity H groupH ∧
      ∀ (G : Type u) [Group G] [Group.IsFinitelyPresented G],
        ∃ φ : G →* H, Function.Injective φ := by
  sorry
end UniversalFInfinity
DEFS(1): def HasTypeFInfinity
## PAPER Finite-algebraic-envelopes-and-the-Boone-Higman-conjecture-September-23-2026
ABSTRACT: We prove the Boone--Higman conjecture. A finitely generated group has decidable word problem if and only if it embeds in a finitely presented simple group.
[theorem] \label{thm:main} For every finitely generated group \(G\), the following are equivalent: \begin{enumerate}[label=\textup{(\roman*)}] \item \(G\) has decidable word problem. \item \(G\) embeds in a finitely presented simple group. \end{enumerate}
## PAPER Simple-F-infinity-overgroups-of-groups-with-decidable-word-problem-September-23-2026
ABSTRACT: Every finitely generated group with decidable word problem embeds in a simple group of type \(F_\infty\). This resolves the higher-finiteness strengthening of the Boone--Higman conjecture.
[theorem] \label{thm:main} Every finitely generated group \(G\) with decidable word problem admits an injective homomorphism into a nontrivial simple group \(H\) of type \(\Finfty\).
## PAPER A-universal-group-of-type-F-infinity-September-23-2026
ABSTRACT: We construct a single group of type $\Finfty$ containing every finitely presented group. Its finitely generated subgroups, up to isomorphism, are exactly the finitely generated recursively presented groups. This answers the $\Finfty$ form of the higher-dimensional Higman embedding question.
[theorem] \label{thm:main} There exists a group $H$ of type $\Finfty$ such that every finitely presented group admits an injective homomorphism into $H$.
==================
# FAMILY 251: Amenability, unitarizability, and strong Ulam stability
SCOPE: Dixmier's unitarizability problem asks whether a discrete group is amenable exactly when every uniformly bounded Hilbert-space representation is similar to a unitary one. The formalization establishes this equivalence for every discrete group. For every nonamenable group and every $\varepsilon>0$, it also gives a nonunitarizable representation with uniform operator bound at most $1+\varepsilon$. The Hilbert space can be chosen separable for countable groups; a separate linked statement records a separable witness with uniform bound $101$ in that case.
## CHALLENGE DixmierAllDiscrete  targets=['OAI.Dixmier.current_main_theorem'] defs=[]
theorem current_main_theorem : CurrentMainTheorem.{u,v} := by
  sorry
end Dixmier
end
DEFS(5): def leftTranslate, def Amenable, def SimilarToUnitary, def Unitarizable, def CurrentMainTheorem
## CHALLENGE Dixmier  targets=['OAI.Dixmier.main_theorem_all_universes'] defs=[]
theorem main_theorem_all_universes : MainTheorem.{u,v} := by
  sorry
end Dixmier
end
DEFS(5): def leftTranslate, def Amenable, def SimilarToUnitary, def NonamenableWitness, def MainTheorem
## PAPER Unitarizability-Implies-Amenability-for-Countable-Groups-September-23-2026
ABSTRACT: We prove that a discrete group is amenable if and only if every uniformly bounded representation on a complex Hilbert space is similar to a unitary representation. This resolves Dixmier's unitarizability problem affirmatively for discrete groups.
[theorem] \label{thm:main} A discrete group is amenable if and only if it is unitarizable. For every discrete nonamenable group \(G\) and every \(\varepsilon>0\), there are a complex Hilbert space \(\mathcal K\) and a representation \(\pi:G\to\mathrm{GL}(\mathcal K)\) with \(|\pi|\le1+\varepsilon\) that is not similar to a unitary representation. If \(G\) is countable, \(\mathcal K\) may be chosen separable.
==================
# FAMILY 252: A torsion-free hyperbolic group that is neither residually finite nor linear over any field
SCOPE: The residual-finiteness question for hyperbolic groups asks whether every nonidentity element survives in some finite quotient. The formalized result gives a negative answer by constructing a torsion-free word-hyperbolic group that is not residually finite. Nonlinearity over every field is not a separate conclusion of the statement linked below.
## CHALLENGE TorsionFreeHyperbolic  targets=['OAI.Release075.main'] defs=[]
theorem main : ∃ (G : Type) (_ : Group G),
    TorsionFree G ∧ WordHyperbolic G ∧ ¬ Group.ResiduallyFinite G := by
  sorry
end Release075
DEFS(4): def TorsionFree, def Geodesic, def SideThin, def WordHyperbolic
## PAPER a-torsion-free-hyperbolic-group-that-is-not-residually-finite-September-23-2026
ABSTRACT: We construct a torsion-free word-hyperbolic group that is not residually finite, answering the residual-finiteness question for hyperbolic groups negatively.
[theorem] \label{thm:main} There exists a torsion-free word-hyperbolic group that is not residually finite.
==================
# FAMILY 253: An infinite finitely presented simple amenable group
SCOPE: The formalized result answers the existence question affirmatively: there is one group that is infinite, finitely presented, simple, and amenable. Amenability is expressed by the Følner condition. The later general claims about central kernels and enlargements across families are not included.
## CHALLENGE SimpleAmenable  targets=['OAI.SimpleAmenable.main'] defs=[]
theorem main : ∃ (G : Type) (_ : Group G),
    Infinite G ∧ Group.IsFinitelyPresented G ∧ IsSimpleGroup G ∧ FolnerAmenable G := by
  sorry
end SimpleAmenable
DEFS(1): def FolnerAmenable
## PAPER An-Infinite-Finitely-Presented-Simple-Amenable-Group-September-23-2026
ABSTRACT: We construct an infinite finitely presented simple amenable group, giving a positive answer to the finite-presentation existence question for simple amenable groups.
[theorem] \label{thm:main} There exists an infinite finitely presented simple amenable group.
==================
# FAMILY 254: Classifying spaces and geometric obstructions for Artin groups
SCOPE: The Artin $K(\pi,1)$ conjecture asserts that the standard Salvetti complex of every finite-rank Artin group is aspherical. The formalized result proves the equivalent statement that its universal cover is contractible. It applies to every Coxeter matrix on a finite generating set, including empty and disconnected diagrams and infinite edge labels. The associated Coxeter and Artin groups may be infinite. Later corollaries in the manuscript are not included. The geometric-action question asks whether every Artin group acts properly and cocompactly by isometries on a proper CAT(0) space. The formalized result gives a counterexample: an Artin group defined by a symmetric matrix on $116$ generators, with diagonal entries $1$ and off-diagonal entries in $\{2,3,\infty\}$. It admits no such action on any nonempty proper CAT(0) space, in any dimension. The formalization proves that the intersecti
## CHALLENGE HarmonicArtin  targets=['OAI.HarmonicArtin.salvetti_cover_contractible'] defs=[]
theorem salvetti_cover_contractible [Finite S] (M : CoxeterMatrix S) :
    ContractibleSpace (SalvettiCover M) := by
  sorry
end HarmonicArtin
DEFS(12): def alternating, def braidRelators, abbrev Artin, def generator, def coxeterParabolic, def IsSpherical, abbrev SphericalType, abbrev LiftedCell, def wordArtin, def wordCoxeter, def LiftedFace, def SalvettiCover
## CHALLENGE ArtinCAT0  targets=['OAI.ArtinCAT0.main'] defs=[]
theorem main :
    (∀ s t : Letters, explicitMatrix s t = explicitMatrix t s) ∧
    (∀ s : Letters, explicitMatrix s s = 1) ∧
    (∀ s t : Letters, s ≠ t →
      explicitMatrix s t = 2 ∨ explicitMatrix s t = 3 ∨ explicitMatrix s t = ⊤) ∧
    (∀ (X : Type u) [MetricSpace X] [ProperSpace X] [Nonempty X]
      [MulAction (ArtinGroup explicitMatrix) X],
      ¬ GeometricAction (ArtinGroup explicitMatrix) X) := by
  sorry
end ArtinCAT0
DEFS(13): abbrev Letters, abbrev Label, def blockLetter, def Adjacent, def Distant, def Sentinel, def explicitMatrix, def alternating, def artinRelators, abbrev ArtinGroup, def Segment, def CAT0, def GeometricAction
## CHALLENGE ArtinParabolicIntersections  targets=['OAI.HarmonicArtin.ParabolicIntersections.unconditional_parabolic_intersections', 'OAI.HarmonicArtin.ParabolicIntersections.unconditional_arbitrary_intersections', 'OAI.HarmonicArtin.ParabolicIntersections.unconditional_parabolic_closure', 'OAI.HarmonicArtin.ParabolicIntersections.unconditional_nonclique_dynamics'] defs=[]
theorem unconditional_parabolic_intersections
    (X Y : Set S) (g h : Artin M) :
    ∃ (Z : Set S) (k : Artin M),
      conjugate g (artinParabolic M X) ⊓ conjugate h (artinParabolic M Y) =
        conjugate k (artinParabolic M Z) := by
  sorry
/-- An arbitrary parabolic intersection is obtained from at most the rank many members. -/
theorem unconditional_arbitrary_intersections
    (F : Set (Subgroup (Artin M))) (hF : ∀ P ∈ F, IsParabolic M P) :
    (∃ F₀ : Finset (Subgroup (Artin M)),
      (↑F₀ : Set (Subgroup (Artin M))) ⊆ F ∧ F₀.card ≤ Nat.card S ∧
        sInf F = sInf (↑F₀ : Set (Subgroup (Artin M)))) ∧ IsParabolic M (sInf F) := by
  sorry
/-- Every subset is contained in a unique smallest parabolic subgroup. -/
theorem unconditional_parabolic_closure (E : Set (Artin M)) :
    ∃! P : Subgroup (Artin M), IsParabolic M P ∧ E ⊆ P ∧
      ∀ Q : Subgroup (Artin M), IsParabolic M Q → E ⊆ Q → P ≤ Q := by
  sorry
/-- An irreducible non-clique Artin group has an acylindrical non-elementary
hyperbolic action and all its proper parabolics are weakly malnormal. -/
theorem unconditional_nonclique_dynamics
    (hIrred : IsIrreducible M) (hInf : ∃ s t : S, s ≠ t ∧ M s t = 0) :
    AcylindricallyHyperbolic (Artin M) ∧
      ∀ P : Subgroup (Artin M), IsParabolic M P → P ≠ ⊤ → WeaklyMalnormal P := by
  sorry
end HarmonicArtin.ParabolicIntersections
DEFS(16): def alternating, def braidRelators, abbrev Artin, def generator, def artinParabolic, def conjugate, def IsParabolic, def gromovProduct, def IsGromovHyperbolic, def IsGeodesicMetric, def IsGromovSequence, def IsAcylindrical, def HasThreeOrbitLimitPoints, def AcylindricallyHyperbolic, def WeaklyMalnormal, def IsIrreducible
## PAPER Harmonic-heights-and-the-Artin-K-pi-1-conjecture-September-23-2026
ABSTRACT: We prove that the standard Salvetti complex of every Artin group with finitely many standard generators is aspherical. This resolves the Artin \(K(\pi,1)\) conjecture in finite rank.
[theorem] \label{thm:main} For every Coxeter matrix on a finite set \(S\), the universal cover of \(X(W,S)\) is contractible. Equivalently, \[ \pi_n\bigl(X(W,S)\bigr)=0\qquad(n\ge2). \] The conclusion allows arbitrary finite labels, infinite labels, and connected or disconnected diagrams.
## PAPER An-Artin-group-with-no-geometric-CAT-0-action-September-23-2026
ABSTRACT: We construct an Artin group on 116 generators that admits no proper, cocompact isometric action on a nonempty proper CAT(0) space. This refutes the CAT(0) conjecture for Artin groups.
[theorem] \label{thm:main} There is an Artin matrix \(M\) on 116 generators, with every off-diagonal label in \(\{2,3,\infty\}\), such that \(A_M\) admits no geometric action. One explicit matrix is given in Definition~\ref{def:matrix}.
## PAPER Parabolic-intersections-in-Artin-groups-September-23-2026
ABSTRACT: We prove that every intersection of parabolic subgroups of any finite-rank Artin group, with arbitrary finite or infinite Coxeter labels, is parabolic. This resolves the Parabolic Intersection Conjecture affirmatively.
[theorem[Parabolic intersections]] \label{thm:main} For every Coxeter matrix $M$ on a finite set $S$, subsets $X,Y\subseteq S$, and $g,h\in A_M$, there are $Z\subseteq S$ and $k\in A_M$ such that \[ gA_Xg^{-1}\cap hA_Yh^{-1}=kA_Zk^{-1}. \]
==================
# FAMILY 255: Quasi-isometric recognition of virtually polycyclic groups
SCOPE: The formalization proves quasi-isometric recognition of virtually polycyclic groups: every finitely generated group quasi-isometric to a finitely generated virtually polycyclic group is itself virtually polycyclic. It also realizes a finite-index subgroup of the recognized group as a uniform lattice in a simply connected solvable Lie group, which may differ from the original ambient group. The linked structural estimate controls the height-coordinate behavior of self quasi-isometries of the stated unimodular solvable Lie models, up to bounded error and one of finitely many linear height symmetries.
## CHALLENGE PolycyclicRecognition  targets=['OAI.PolycyclicRecognition.group_recognition', 'OAI.PolycyclicRecognition.main_uniform_bounded_height', 'OAI.PolycyclicRecognition.lattice_recognition'] defs=[]
theorem group_recognition
    {P J : Type} [Group P] [Group J] [Group.FG P] [Group.FG J]
    (e : GroupCoarseEquivalence P J) (hP : IsVirtuallyPolycyclic P) :
    IsVirtuallyPolycyclic J ∧
      ∃ Γ : Subgroup J, Γ.FiniteIndex ∧
        ∃ (S : SimplyConnectedSolvableLieModel) (Λ : Subgroup S.carrier),
          IsUniformLattice Λ ∧ Nonempty (Γ ≃* Λ) := by
  sorry
/-- One finite slope group controls the height of every self quasi-isometry. -/
theorem main_uniform_bounded_height
    (R : SimplyConnectedSolvableLieModel) (d : ProperChainMetric R.carrier)
    {a : ℕ} (T : TriangularAdjoint (GroupLieAlgebra (𝓘(ℝ, R.modelSpace)) R.carrier) a)
    (huni : ModelIsUnimodular R)
    {W : Type} [NormedAddCommGroup W] [NormedSpace ℝ W] [FiniteDimensional ℝ W]
    (q : HeightSpace T.character ≃ₗ[ℝ] W)
    (Exp : GroupLieAlgebra (𝓘(ℝ, R.modelSpace)) R.carrier → R.carrier)
    (hExp : IsGroupExponential Exp) (π : R.carrier →* Multiplicative W)
    (hπExp : ∀ x, (π (Exp x)).toAdd = q (heightProjection T.character x)) :
    letI := d.compatibleMetric
    ∃ A : Subgroup (W ≃ₗ[ℝ] W), Set.Finite (A : Set (W ≃ₗ[ℝ] W)) ∧
      ∀ K C : ℝ, 1 ≤ K → 0 ≤ C → ∃ B : ℝ, 0 ≤ B ∧
        ∀ F : SelfQuasiIsometry R.carrier K C, ∃ AF : A, ∀ g,
          ‖(π (F.toFun g)).toAdd - ((π (F.toFun 1)).toAdd + AF.val (π g).toAdd)‖ ≤ B := by
  sorry
/-- Finite-covolume lattice recognition, allowing a different ambient Lie group. -/
theorem lattice_recognition
    (S : SimplyConnectedSolvableLieModel) (Λ : Subgroup S.carrier)
    (hΛ : IsFiniteCovolumeLattice Λ)
    {J : Type} [Group J] [Group.FG J] (e : GroupCoarseEquivalence Λ J) :
    ∃ Γ : Subgroup J, Γ.FiniteIndex ∧
      ∃ (R : SimplyConnectedSolvableLieModel) (Δ : Subgroup R.carrier),
        IsUniformLattice Δ ∧ Nonempty (Γ ≃* Δ) := by
  sorry
end PolycyclicRecognition
end
DEFS(20): structure CyclicStep, structure CyclicSeries, def GroupBornologous, structure GroupCoarseEquivalence, def IsPolycyclic, def IsVirtuallyPolycyclic, def IsUniformLattice, structure SimplyConnectedSolvableLieModel, def IsFiniteCovolumeLattice, structure LinearMetricChains, structure ProperChainMetric, abbrev ProperChainMetric.compatibleMetric, def heightKernel, abbrev HeightSpace, def heightProjection, structure TriangularAdjoint, def character, structure IsGroupExponential, def ModelIsUnimodular, structure SelfQuasiIsometry
## PAPER quasi-isometric-recognition-of-virtually-polycyclic-groups-September-24-2026
ABSTRACT: We prove that every finitely generated group quasi-isometric to a finitely generated virtually polycyclic group is virtually polycyclic. This resolves the lattice-recognition conjecture of Eskin, Fisher and Whyte, which allows the ambient solvable Lie group in the conclusion to differ from the one in the hypothesis.
[theorem] \label{thm:recognition} Let $P$ be a finitely generated virtually polycyclic group, and let $H$ be any finitely generated group. If $H$ and $P$ are quasi-isometric, then $H$ is virtually polycyclic.
==================
# FAMILY 256: Nonsingular systems of equations over arbitrary groups
SCOPE: Kervaire's conjecture states that the free product of a nontrivial group with an infinite cyclic group cannot be normally generated by one element. The linked formalization proves the stronger coefficient-injectivity statement used in the paper: for any group $A$ and any relator in $A*\mathbb Z$ whose exponent sum in the cyclic generator is $1$ or $-1$, the natural map from $A$ into the quotient by that relator is injective. This is the selected unimodular-relator result underlying the conjecture.
## CHALLENGE Kervaire  targets=['OAI.Kervaire.coefficient_injective'] defs=[]
theorem coefficient_injective (A : Type u) [Group A] (w : WordGroup A)
    (hw : Unimodular w) : Function.Injective (coefficientMap w) := by
  sorry
end Kervaire
end
DEFS(6): abbrev WordGroup, def exponentSum, def Unimodular, def relatorClosure, abbrev RelatorQuotient, def coefficientMap
## PAPER The-Kervaire-Theorem-for-Groups-September-24-2026
ABSTRACT: We prove that no free product of a nontrivial group with an infinite cyclic group is normally generated by one element. This resolves the Kervaire conjecture positively.
[theorem] \label{thm:main} For every group $A$ and every unimodular word $w\in A*\langle t\rangle$, the canonical homomorphism \[ A\longrightarrow (A*\langle t\rangle)/\langle\!\langle w\rangle\!\rangle_H \] is injective.
==================
# FAMILY 257: A hyperbolic group without a geometric CAT(0) action
SCOPE: The formalized result constructs a finite connected aspherical complex with a linear disk-filling bound whose fundamental group is word-hyperbolic but admits no geometric action on a nonempty proper complete $\mathrm{CAT}(0)$ space. It also excludes locally $\mathrm{CAT}(-1)$ geodesic metrics on every finite complex homotopy equivalent to the witness. The stronger claims that the witness is two-dimensional and that those models admit no locally $\mathrm{CAT}(0)$ metric are not included.
## CHALLENGE HyperbolicObstruction  targets=['OAI.HyperbolicObstruction.main'] defs=[]
theorem main : MainStatement.{u} := by sorry
end HyperbolicObstruction
end
end
end
DEFS(22): structure FiniteComplex, abbrev Vertex, def Carrier, def Edge, def EdgePath, def Closed, inductive DiskMove, inductive DiskHomotopy, def Disk, def LinearDiskFilling, def Aspherical, def IsSegment, def IsGeodesic, def CATZero, def CATNegOne, structure GeometricAction, def NoGeometricCATZeroAction, def WordLength, def WordDistance, def WordHyperbolic, def CompatibleLocallyCATNegOne, def MainStatement
## PAPER A-hyperbolic-group-with-no-geometric-CAT0-action-September-25-2026
ABSTRACT: We construct a hyperbolic group with a finite classifying space that admits no geometric action on a proper complete CAT(0) space. Consequently, a finite aspherical simplicial complex with a linear combinatorial disk-filling inequality need not have a finite locally CAT(0) homotopy model, and hence need not have a finite locally CAT($-1$) model. Here metric models carry geodesic length metrics inducing the given complex topology.
[theorem] \label{thm:main} There exist a finite connected two-dimensional aspherical simplicial complex $K$ and a constant $C<\infty$ with the following properties. \begin{enumerate}[label=\textup{(\roman*)}] \item Every combinatorial edge loop of length $\ell$ in the universal cover of $K$ bounds a disk diagram with at most $C\ell$ triangular faces. \item The group $\pi_1K$ admits no geometric action on a proper complete $\CAT(0)$ space. \end{enumerate} In particular, $\pi_1K$ is word-hyperbolic, and no finite simplicial complex homotopy equivalent to $K$ admits a locally $\CAT(0)$ geodesic length metric inducing its given topology. Consequently, no such model admits a compatible locally $\CAT(-1)$ g
==================
# FAMILY 260: Spacetime Penrose inequalities: enclosing area, charge, rotation, and anti-de Sitter extensions
SCOPE: The formalization replaces a three-dimensional Cha–Khuri–Sakovich hyperboloidal end by asymptotically flat ends while preserving each fixed compact interior, completeness, and the dominant energy condition. For strictly future-timelike initial-data charge, the ADM masses approach the invariant Bondi mass and the loss of enclosing area tends to zero. The Comparator also includes canonical Schwarzschild equality examples at every positive mass, with $m_{\mathrm{Bondi}}=m$ and enclosing area $16\pi m^2$. The paper's general Bondi–Penrose inequality for possibly disconnected weakly trapped boundaries remains unformalized. The implementation retains a conditional inequality for the connected marginal-boundary case, assuming the asymptotically flat exterior Penrose inequality. This supporting result is not selected as a substitute for the paper's main inequality.
## CHALLENGE CKSBondiPenrose  targets=['OAI.CKSSourceExterior.area_controlled_end_replacement', 'OAI.CKSMain.schwarzschild_equality_examples'] defs=[]
theorem area_controlled_end_replacement
    (g : OAI.CKSMetricGluing.SmoothMetric OAI.CKSGeometricCuts.I3 (M := N)) (K : OAI.CKSMetricGluing.InnerField OAI.CKSGeometricCuts.I3 (M := N))
    (hK : ContMDiff OAI.CKSGeometricCuts.I3 (OAI.CKSGeometricCuts.I3.prod 𝓘(ℝ,OAI.CKSLorentz.SpatialBilinear)) ∞ (OAI.CKSMetricGluing.innerSection OAI.CKSGeometricCuts.I3 K))
    (hKsym : ∀ x v w, K x v w = K x w v)
    (hOrient : OAI.CKSSourceExterior.Orientable (N := N))
    (hScompact : IsCompact (OAI.CKSGeometricCuts.I3.boundary N)) (hSnonempty : (OAI.CKSGeometricCuts.I3.boundary N).Nonempty)
    (hcomplete : OAI.CKSReplacementCompleteness.IsComplete OAI.CKSGeometricCuts.I3 g.toContinuousRiemannianMetric)
    (hDEC : OAI.CKSSpatialManifold.PhysicalDEC OAI.CKSGeometricCuts.I3 g.inner K)
    (d : OAI.CKSSourceExterior.CKSData g K)
    (ht : ‖(OAI.CKSLorentz.bondiCharge d.massAspect).2‖ < (OAI.CKSLorentz.bondiCharge d.massAspect).1) :
    ∃ (d' : OAI.CKSSourceExterior.CKSData g K) (R₀ : ℝ) (ε : ℝ → ℝ),
      OAI.CKSLorentz.bondiCharge d'.massAspect =
        (Real.sqrt ((OAI.CKSLorentz.bondiCharge d.massAspect).1^2 - ‖(OAI.CKSLorentz.bondiCharge d.massAspect).2‖^2),0) ∧
      d'.chart.radius < R₀ ∧ 12 ≤ R₀ ∧ Tendsto ε atTop (𝓝 0) ∧
      OAI.CKSFullCutArea.minEnclosingArea g < ⊤ ∧
      ∀ R ≥ R₀, (0 ≤ ε R ∧ ε R < 1) ∧
        ∃ (gR : OAI.CKSMetricGluing.SmoothMetric OAI.CKSGeometricCuts.I3 (M := N)) (kR : OAI.CKSMetricGluing.InnerField OAI.CKSGeometricCuts.I3 (M := N))
          (G k : OAI.CKSLorentz.SpatialTensor) (η : ℝ),
          ContMDiff OAI.CKSGeometricCuts.I3 (OAI.CKSGeometricCuts.I3.prod 𝓘(ℝ,OAI.CKSLorentz.SpatialBilinear)) ∞ (OAI.CKSMetricGluing.innerSection OAI.CKSGeometricCuts.I3 kR) ∧
          (∀ x v w, kR x v w = kR x w v) ∧
          (∀ x, x ∉ d'.chart.domain ∨ ‖d'.chart
theorem schwarzschild_equality_examples (m : ℝ) (hm : 0 < m) :
    SchwarzschildExample.{v} m hm := by
  sorry
end OAI.CKSMain
DEFS(235): abbrev InnerField, abbrev SmoothMetric, def innerSection, abbrev I, def D, abbrev Idx, abbrev Mat, structure MetricJet, def gamma, def dInv, def dGamma, def ricci, def scalar, structure TensorJet, def trace, def normSq, def dTrace, def tensorDivergence, def energy, def momentum, abbrev Point, def basis, def momentumSq, def DEC, abbrev Point, def basis, abbrev AmbientMat, abbrev PhysicalPoint, abbrev I, abbrev A
## PAPER Area-controlled-end-replacement-and-the-Bondi-Penrose-inequality-in-the-CKS-class-September-27-2026
ABSTRACT: We replace a three-dimensional Cha--Khuri--Sakovich hyperboloidal end by an asymptotically flat end while preserving the dominant energy condition and each fixed compact interior. For strictly future-timelike CKS initial-data charge, the replacements lose asymptotically no enclosing area and their ADM masses tend to the invariant Bondi mass. Combining this construction with the companion numerical spacetime Penrose theorem yields the sharp Bondi bound for possibly disconnected weakly future trapped boundaries in this class. Horizon-regular Schwarzschild exteriors attain equality at every positive mass.
[theorem[Area-controlled end replacement]] \label{prop:replacement} Let $(\Omega,g,K)$ be a smooth connected orientable three-dimensional exterior, complete including its nonempty compact smooth boundary, with exactly one end of class \eqref{eq:cks}. Suppose DEC holds and $E_B>|P_B|$. There is a balanced chart such that, for every sufficiently large $R$, smooth data $(G_R,k_R)$ on the same exterior have the following properties: \begin{enumerate} \item They agree with $(g,K)$ on the compact side of $r=R$ and satisfy DEC. \item For numbers $0\leq\varepsilon_R<1$ with $\varepsilon_R\to0$, $G_R\geq(1-\varepsilon_R)g$ everywhere on $\Omega$. \item The end is asymptotically flat, with $G_R-\delta=O_j(r^{-1})$ for every fixed finite $j$, a
==================
# FAMILY 261: Localization and delocalization in the Anderson model
SCOPE: The linked formalization proves a supporting spectral statement for the nearest-neighbor Anderson operator on $\mathbb Z^2$. For every disorder strength $h>0$ with independent site potentials uniform on $[-h,h]$, it constructs the bounded self-adjoint operator almost surely and identifies its spectrum as the real interval $[-4-h,4+h]$. This selected statement identifies the spectral set. It does not assert the pure-point spectral type claimed in the accompanying paper.
## CHALLENGE PlanarAndersonSpectrum  targets=['OAI.PlanarAnderson.anderson_spectrum_ae'] defs=[]
theorem anderson_spectrum_ae {h : ℝ} (hh : 0 < h) :
    ∀ᵐ v ∂disorderLaw h, ∃ H : Hilbert →L[ℂ] Hilbert,
      IsAndersonOperator v H ∧ IsSelfAdjoint H ∧ spectrum ℂ H = spectralInterval h := by
  sorry
end PlanarAnderson
end
DEFS(6): abbrev Site, abbrev Configuration, abbrev Hilbert, def disorderLaw, def IsAndersonOperator, def spectralInterval
## PAPER Pure-Point-Spectrum-for-the-Two-Dimensional-Anderson-Model-at-Every-Positive-Disorder-September-23-2026
ABSTRACT: For each fixed positive disorder strength, we prove that the nearest-neighbor Anderson operator on the square lattice with independent uniform site potentials almost surely has pure-point spectral type throughout its spectrum. This resolves the pure-point assertion of the two-dimensional Anderson localization conjecture for the uniform single-site law.
[theorem] \label{main:theorem} For each fixed $h>0$, almost surely $H_v$ has pure-point spectral type, admits a complete orthonormal eigenbasis, and has spectrum \[ \sigma(H_v)=[-4-h,4+h]. \] Its eigenvalues are dense in this interval. The probability-one event in this statement is allowed to depend on $h$.
==================
# FAMILY 262: Sharp finite-matrix Lieb–Thirring inequalities and all equality cases
SCOPE: The formalized result determines the sharp one-dimensional Lieb–Thirring constant for $1/2<\gamma<3/2$. For every nonnegative $W\in L^{\gamma+1/2}(\mathbb R)$, it bounds the full negative-eigenvalue moment of $-d^2/dx^2-W$ by the one-bound-state constant times the potential integral. This constant is optimal and is attained by $(r+1)\mathrm{sech}^2(rx)$, where $r=(\gamma-1/2)^{-1}$. No finite spectral cutoff is imposed.
## CHALLENGE LiebThirring  targets=['OAI.SharpLiebThirring.sharp_lieb_thirring'] defs=[]
theorem sharp_lieb_thirring : MainClaim := by
  sorry
end SharpLiebThirring
end
DEFS(15): structure H1, def l2Pairing, def schrodingerForm, def IsNegativeEigenfunction, def IsOrthonormalFamily, def negativeMoment, def oneStateMoment, def Admissible, def potentialMass, def semiclassicalConstant, def sharpConstant, def optimalConstant, def oneStateConstant, def equalityPotential, def MainClaim
## PAPER Sharp-One-Dimensional-Lieb-Thirring-Constants-September-23-2026
ABSTRACT: We resolve affirmatively the remaining cases of the scalar one-dimensional Lieb--Thirring conjecture: for every $\frac12<\gamma<\frac32$, the optimal constant is the one-bound-state constant. The estimate holds for every nonnegative potential in $L^{\gamma+1/2}(\mathbb R)$, with all negative eigenvalues included.
[theorem] \label{thm:main} For every $1/2<\gamma<3/2$ and every nonnegative $W\in L^{\gamma+1/2}(\R)$, \begin{equation}\label{eq:main} \Tr(H_{-W})_-^\gamma \le 2\left(\frac{\gamma-1/2}{\gamma+1/2}\right)^{\gamma-1/2} L_{\gamma,1}^{\cl}\int_\R W^{\gamma+1/2}. \end{equation} The constant is optimal and equals $L_{\gamma,1}^{(1)}$. More precisely, if $r=(\gamma-1/2)^{-1}$, equality is attained by $W(x)=(r+1)\sech^2(rx)$.
==================
# FAMILY 263: The ionization and generalized ionization conjectures
SCOPE: The formalization gives the large-ionization asymptotics for the full nonrelativistic two-spin Coulomb atom. Let $I_m(Z)$ be the energy needed to remove $m$ electrons from a neutral atom of nuclear charge $Z$. There is a positive coefficient $a_{\mathrm{TF}}$ with the Thomas–Fermi variational characterization such that $I_m(Z)/m^{7/3}\to a_{\mathrm{TF}}$ whenever $m\to\infty$ and $Z/m\to\infty$, with integers $Z>m\ge1$. The corresponding iterated limsup and liminf limits hold with $Z\to\infty$ first. The energy uses the full antisymmetric Sobolev form domain; fixed-$m$ convergence and ground-state attainment are outside this statement. For neutral Coulomb atoms with two electron spin states, the formalization proves the asymptotic law for generalized outer-electron radii defined by an expected exterior electron mass $m$. For every choice of normalized ground states, both the upper and lo
## CHALLENGE CoulombIonization  targets=['OAI.CoulombAtom.generalized_ionization'] defs=[]
theorem generalized_ionization : MainStatement := by
  sorry
end CoulombAtom
end
DEFS(19): abbrev Space, abbrev Configuration, abbrev Spins, structure FormVector, def direction, def FormAdmissible, def formEnergy, def energy, def ionization, def tfKinetic, def directIntegrand, def TFAdmissible, def tfFunctional, def tfEnergy, def tfIonization, def TFCharacterization, def JointLimit, def IteratedLimits, def MainStatement
## CHALLENGE CoulombRadii  targets=['OAI.NeutralAtom.generalized_outer_radii'] defs=[]
theorem generalized_outer_radii
    (Ψ : ∀ N : ℕ, Wavefunction (N + 1))
    (hΨ : ∀ N : ℕ, IsNormalizedGroundState (N + 1) (Ψ N)) :
    Tendsto (fun m : ℕ => (((m : ℝ) ^ (1 / 3 : ℝ) : ℝ) : EReal) * upperRadius Ψ m)
      atTop (𝓝 (bTF : EReal)) ∧
    Tendsto (fun m : ℕ => (((m : ℝ) ^ (1 / 3 : ℝ) : ℝ) : EReal) * lowerRadius Ψ m)
      atTop (𝓝 (bTF : EReal)) := by
  sorry
end NeutralAtom
end
DEFS(20): abbrev Position, abbrev Configuration, abbrev Spins, abbrev Wavefunction, abbrev Gradient, def coordinateDirection, def HasWeakGradient, def IsAntisymmetric, def FormDomain, def normSquared, def coulombPotential, def energy, def IsNormalizedGroundState, def density, def exteriorMass, def radius, def bTF, def largeCharge, def upperRadius, def lowerRadius
## PAPER Generalized-ionization-energies-for-full-Coulomb-atoms-September-24-2026
ABSTRACT: We prove the energy part of the generalized ionization conjecture for full nonrelativistic Coulomb atoms with two electron spin states. The energy needed to remove $m$ electrons is asymptotic to $a_{\TF}m^{7/3}$ whenever $m\to\infty$ and $Z/m\to\infty$, with the Thomas--Fermi constant in atomic units. We also obtain both conjectured iterated limits.
[theorem[Generalized ionization energy]] \label{thm:main} For full nonrelativistic Coulomb atoms with two electron spin states, \begin{equation}\label{eq:joint-limit} \frac{I_m(Z)}{m^{7/3}}\longrightarrow a_{\TF}>0 \quad\text{whenever}\quad m\longrightarrow\infty, \qquad \frac Zm\longrightarrow\infty, \end{equation} where $Z>m\ge1$ are integers. In particular, \begin{align} \lim_{m\to\infty} \frac{\limsup_{Z\to\infty} I_m(Z)}{m^{7/3}} &=a_{\TF},\label{eq:iterated-upper}\\ \lim_{m\to\infty} \frac{\liminf_{Z\to\infty} I_m(Z)}{m^{7/3}} &=a_{\TF}.\label{eq:iterated-lower} \end{align} The inner limits are taken over integer $Z$ with $m$ fixed. No convergence of $I_m(Z)$ at a fixed $m$ is asserted or assumed.
## PAPER Generalized-outer-electron-radii-of-neutral-Coulomb-atoms-September-24-2026
ABSTRACT: We prove the radius part of the generalized ionization conjecture for neutral nonrelativistic Coulomb atoms with two spin states. For every choice of ground states, the upper and lower large-nuclear-charge limits of the radius defined by an expected exterior electron mass $m$ are both asymptotic to $(81\pi^2/2)^{1/3}m^{-1/3}$ as $m$ tends to infinity.
[theorem[Generalized ionization conjecture: radii]] \label{intro:main} Set $b_{\mathrm{TF}}=(81\pi^2/2)^{1/3}$. For every choice of normalized neutral ground states $(\Psi_Z)_{Z\ge1}$ of \eqref{intro:hamiltonian}, \begin{align} \lim_{m\to\infty}m^{1/3} \left[\limsup_{\substack{Z\to\infty\\ Z>m}}R_m(\Psi_Z)\right] &=b_{\mathrm{TF}},\label{intro:limsup}\\ \lim_{m\to\infty}m^{1/3} \left[\liminf_{\substack{Z\to\infty\\ Z>m}}R_m(\Psi_Z)\right] &=b_{\mathrm{TF}}.\label{intro:liminf} \end{align} All limits are over integers. The inner limits hold $m$ fixed; no convergence in $Z$ at a fixed $m$ is assumed.
==================
# FAMILY 266: Exactly three mutually unbiased bases in dimension six
SCOPE: The paper claims that at most three mutually unbiased orthonormal bases exist in $\mathbb C^6$. The linked formalization proves a weaker family bound: every family in its mutually unbiased bases model has at most five members. It also proves a Fourier character-sum vanishing statement for order-six complex Hadamard matrices not equivalent to the Tao matrix, uniformly over coordinate permutations. The selected statement does not establish the paper's upper bound of three or its computer-assisted exclusion of four arbitrary bases. The linked formalization proves a cancellation lemma used in the order-six complex Hadamard analysis. Let $H$ and its entrywise square both be complex Hadamard matrices, and fix two distinct rows. If the cubes of their six entrywise ratios take only two distinct values, then the sum of the row-ratio terms over either specified cube fiber is zero. This is a suppor
## CHALLENGE MUBSix  targets=['OAI.MUB6.fourier_and_family_bound'] defs=[]
theorem fourier_and_family_bound :
    (∀ H : CMatrix, IsHadamard H → ¬Equivalent H tao →
      ∀ π : Equiv.Perm Coord, g H (permuteCharge π alpha) = 0) ∧
    (∀ n : ℕ, Attainable n → n ≤ 5) := by
  sorry
end MUB6
end
DEFS(16): abbrev Coord, abbrev CMatrix, abbrev Charge, def IsHadamard, def character, def g, def alpha, def permuteCharge, def Equivalent, def omega, def taoExponent, def tao, abbrev Space, abbrev Basis, def IsMUBFamily, def Attainable
## CHALLENGE HadamardCubeFiber  targets=['OAI.HadamardSix.rowRatio_cubeFiber_sum_zero'] defs=[]
lemma rowRatio_cubeFiber_sum_zero {H : Matrix6} (hH : IsComplexHadamard H)
    (hs : IsComplexHadamard (entrywiseSquare H)) {i j : Index} (hij : i ≠ j)
    (a b : ℂ) (hne : a ≠ b)
    (hab : ∀ k, rowRatio H i j k ^ 3 = a ∨ rowRatio H i j k ^ 3 = b) :
    ∑ k ∈ cubeFiber (rowRatio H i j) a, H i k * star (H j k) = 0 := by
  sorry
end HadamardSix
DEFS(7): abbrev Index, abbrev Matrix6, def Unimodular, def IsComplexHadamard, def entrywiseSquare, def cubeFiber, def rowRatio
## PAPER The-maximum-number-of-mutually-unbiased-bases-in-dimension-six-September-24-2026
ABSTRACT: We prove that the maximum number of mutually unbiased orthonormal bases in $\C^6$ is three, resolving Zauner's dimension-six MUB conjecture. The upper bound is computer-assisted: under the stated binary64 arithmetic and compiler conditions, a complete execution of the documented verification pipeline excludes four arbitrary complex bases.
[theorem[Computer-assisted]] \label{thm:main} Under the arithmetic and compiler conditions in Appendix~\ref{sec:rounding}, the fresh complete execution documented in Section~\ref{execute:observed} certifies that there are no four pairwise mutually unbiased orthonormal bases in $\C^6$. Consequently, $N(6)=3$.
## PAPER Exact-Fourier-certificates-for-complex-Hadamard-matrices-of-order-six-September-24-2026
ABSTRACT: We prove the Fourier-vanishing conjecture of Matolcsi, Ruzsa, and Weiner: every complex Hadamard matrix of order six outside Tao's cubic equivalence class has a vanishing character sum at every permutation of $(1,1,1,-1,-1,-1)$. We also give an exact certificate excluding seven mutually unbiased bases in $\C^6$; by Weiner's completion theorem, this yields an upper bound of five. Both certificates use only integer and rational arithmetic, and the complete verifier is included.
[theorem[Fourier vanishing]] \label{thm:fourier} Let $H$ be a complex Hadamard matrix of order six. If $H$ is not equivalent to the cubic matrix $T$ in \eqref{eq:cubic-matrix}, then \[ g_H(\pi\alpha)=0\qquad\text{for every coordinate permutation }\pi. \]
==================
# FAMILY 267: Positive-temperature Bose–Einstein condensation and exact quantum depletion
SCOPE: The formalization proves ground-state Bose–Einstein condensation in the dilute hard-sphere gas. There are absolute constants $\varepsilon_0,c_0>0$ such that, whenever the density $\rho$ and hard-sphere radius $a$ satisfy $\rho a^3<\varepsilon_0$, the condensate occupation fraction has limit inferior at least $c_0$ along every thermodynamic sequence with $N/L^3\to\rho$. The bound covers every pure ground state, every mixed state supported on the ground space, and the normalized ground-space projection. It is uniform in the gas parameter within this range and concerns ground states, without a positive-temperature assertion.
## CHALLENGE HardSphere  targets=['OAI.HardSphere.condensation_with_mixed'] defs=[]
theorem condensation_with_mixed :
    ∃ε₀ c₀ : ℝ,0<ε₀ ∧ 0<c₀ ∧
    ∀a ρ : ℝ,0<a → 0<ρ → ρ*a^3<ε₀ →
    ∀(N : ℕ→ℕ) (L : ℕ→Length) (hN : ∀k,0<N k),
      Tendsto N atTop atTop → Tendsto (fun k ↦ (L k).val) atTop atTop →
      Tendsto (fun k ↦ (N k:ℝ)/(L k).val^3) atTop (𝓝 ρ) →
      (∀Ψ : (k : ℕ)→Jet (N k) (L k),
        (∀k,IsGroundVector (N k) (L k) a (Ψ k)) →
        c₀≤liminf (fun k ↦ occupation (hN k) (Ψ k).1) atTop) ∧
      (∀T : (k : ℕ)→Density.Operator (ScalarL2 (N k) (L k)),
        (∀k,GroundSupported a (T k)) →
        c₀≤liminf (fun k ↦ mixedOccupation (hN k) (T k)) atTop) := by
  sorry
DEFS(30): abbrev Length, instance lengthPositive, abbrev Torus, abbrev Configuration, abbrev LiftedConfiguration, abbrev Direction, def torusDistance, def allowed, def project, def representative, def coordDerivative, abbrev ScalarL2, abbrev Jet, structure SmoothTest, def SmoothTest.jet, def dirichletDomain, def energy, def bosonic, def IsGroundVector, def insertFirst, def occupation, def basisSet, def basis, structure Operator, def Operator.compressionTrace, def sliceIntegral, def map, def continuous, def GroundSupported, def mixedOccupation
## PAPER Ground-state-condensation-in-the-dilute-hard-sphere-gas-September-24-2026
ABSTRACT: We prove Bose--Einstein condensation in every ground state of a dilute three-dimensional hard-sphere Bose gas. At every sufficiently small fixed gas parameter, the constant orbital contains a positive fraction of the particles in the thermodynamic limit. The fraction can be chosen independently of the gas parameter, and the conclusion holds for arbitrary complex ground states.
[theorem[Condensation in every ground state]] \label{main:theorem} There are absolute constants $\varepsilon_0,c_0>0$ with the following property. Fix $a,\rho>0$ satisfying $\rho a^3<\varepsilon_0$. For every sequence of particle numbers $N_k$ and lengths $L_k$ such that \[ N_k\longrightarrow\infty,\qquad L_k\longrightarrow\infty, \qquad \frac{N_k}{L_k^3}\longrightarrow\rho, \] and every choice of normalized, possibly complex, bosonic ground eigenvectors $\Psi_k$ of the hard-sphere Hamiltonians, \begin{equation}\label{main:limit} \liminf_{k\to\infty} B(\Psi_k)\ge c_0. \end{equation}
==================
# FAMILY 269: Uniform Laughlin gap and stability under bounded scalar disorder
SCOPE: The linked formalization proves the uniform unperturbed gap estimate used in the paper's stability argument for the fermionic Laughlin state at filling $1/3$ on the sphere. At flux $q=3(N-1)$ and all sufficiently large particle numbers $N$, every antisymmetric state has $V_1$ energy at least $1/25$ times its squared distance from the Laughlin ground-state line. This selected statement is the unperturbed Fock-space inequality. Stability under projected one-body potentials and uniqueness of the perturbed ground state are outside it. The Laughlin spectral-gap problem asks for a positive gap that remains uniform as the system grows. The formalization includes the finite spherical $V_1$ bound of $1/100$ above the Laughlin state at flux $3(N-1)$ for all sufficiently large particle numbers $N$. It also proves the stronger Fock-space inequality $H_Q^2\ge\gamma H_Q$ for every fixed $0<\gamma<\gam
## CHALLENGE LaughlinGap  targets=['OAI.LaughlinGap.thm_main'] defs=[]
theorem thm_main : MainTarget := by
  sorry
end LaughlinGap
DEFS(13): abbrev Configuration, abbrev State, def Antisymmetric, def pairCoefficient, def pairAmplitude, def energy, abbrev SpinorVariables, def bracket, def laughlinPolynomial, def monomialExponent, def laughlinVector, def distanceToLaughlinSq, def MainTarget
## CHALLENGE Laughlin  targets=['OAI.Laughlin.mainTarget_proved'] defs=[]
theorem mainTarget_proved : MainTarget := by
  sorry
end Laughlin
DEFS(13): abbrev Configuration, abbrev State, def Antisymmetric, def pairCoefficient, def pairAmplitude, def energy, abbrev SpinorVariables, def bracket, def laughlinPolynomial, def monomialExponent, def laughlinVector, def distanceToLaughlinSq, def MainTarget
## CHALLENGE LaughlinFock  targets=['OAI.LaughlinFock.thm_fock'] defs=[]
theorem thm_fock (γ : ℝ) (hγ : 0 < γ) (hγStar : γ < gammaStar) :
    ∃ Qγ : ℤ, 1 ≤ Qγ ∧ ∀ Q : ℤ, Qγ ≤ Q → FockInequality Q.toNat γ := by
  sorry
end LaughlinFock
end
DEFS(11): def pairCoefficient, abbrev Orbital, abbrev Occupation, abbrev FockMatrix, def tensorPairCoefficient, def pairCoefficient, def annihilator, def pairAnnihilator, def hamiltonian, def gammaStar, def FockInequality
## CHALLENGE LaughlinPlanar  targets=['OAI.Laughlin.planar_gap'] defs=[]
theorem planar_gap {N : ℕ} (ψ : Planar.HomogeneousState N) :
    ENNReal.ofReal gammaStar * Planar.fullEnergy ψ ≤ Planar.fullSquareNorm ψ := by
  sorry
end Laughlin
DEFS(17): def gammaStar, def pairLimitCoefficient, abbrev Orbital, abbrev Space, def annihilate, def occupationBasis, def OccupationBidegree, abbrev Occupations, def pairMatrix, def planarCoefficient, def planarPairMatrix, def planarHamiltonian, def pairEnergy, def squareNorm, structure HomogeneousState, def fullEnergy, def fullSquareNorm
## PAPER Uniform-Stability-of-the-Spherical-Laughlin-Gap-October-5-2026
ABSTRACT: We prove that the fermionic Laughlin $V_1$ Hamiltonian at filling $1/3$ on expanding round spheres retains a unique ground state and a uniform spectral gap under sufficiently weak bounded real scalar one-body potentials projected to the lowest Landau level. With coefficient one for each pair projector and Laughlin flux $q=3(N-1)$, the gap and perturbation threshold are uniform for all sufficiently large particle numbers and all potential profiles of supremum norm at most one. The result uses the uniform unperturbed Fock-space gap and gives existential constants.
[theorem[Uniform scalar-disorder stability]] \label{thm:main} There are constants $\lambda_*>0$, $\Delta_*>0$, and $N_*<\infty$ such that, for every $N\ge N_*$, every real bounded measurable $\varphi$ on $S_{3(N-1)}$ with $\|\varphi\|_\infty\le1$, and every real $|\lambda|\le\lambda_*$, \begin{equation}\label{eq:intro-stability} E_1(N,\lambda,\varphi)-E_0(N,\lambda,\varphi)\ge\Delta_*. \end{equation} In particular the perturbed ground state is unique.
## PAPER A-Fock-space-inequality-and-the-Laughlin-spectral-gap-September-24-2026
ABSTRACT: We prove the spherical fermionic Laughlin spectral-gap conjecture for the full \(V_1\) interaction. With coefficient one for each pair projector, the gap above the Laughlin state at filling \(1/3\) on the round sphere is at least \(1/25\) for all sufficiently large systems. More generally, \(H_Q^2\ge\gamma H_Q\) for some fixed \(\gamma>1/25\) on the entire lowest-Landau-level Fock space for all sufficiently large flux \(Q\), independently of particle number.
[theorem] \label{thm:fock} For every \(0<\gamma<\gamma_*\), there is an integer \(Q_\gamma\) such that for every integer \(Q\ge Q_\gamma\), \begin{equation}\label{eq:architecture} H_Q^2\ge\gamma H_Q\qquad\text{on }\FF_Q. \end{equation} The threshold \(Q_\gamma\) is independent of particle number.
==================
# FAMILY 271: Bloch's law, its lattice correction, and the spherical magnetization law
SCOPE: The formalization proves spontaneous magnetization for the nearest-neighbor isotropic quantum Heisenberg ferromagnet on $\mathbb Z^d$ for every $d\ge3$ and every spin $S\in\{\tfrac12,1,\tfrac32,\ldots\}$. At every sufficiently low positive temperature, it constructs a translation-invariant equilibrium state satisfying the KMS condition for the zero-field dynamics and having magnetization at least $S/4$. It also proves convergence of the finite-volume dynamics to the infinite-volume dynamics used in the KMS statement.
## CHALLENGE Heisenberg  targets=['OAI.Heisenberg.spontaneous_magnetization'] defs=[]
theorem spontaneous_magnetization (d ℓ : ℕ) (hd : 3≤d) (hℓ : 1≤ℓ) :
    DynamicsConverges d ℓ ∧
      ∃ β₀ : ℝ,0<β₀ ∧ ∀ β : ℝ,β₀≤β →
        ∃ ω : State d ℓ,TranslationInvariant ω ∧ IsKMS β ω ∧
          (ω.functional (spinZ d ℓ 0)).im=0 ∧
          (ℓ:ℝ)/8≤(ω.functional (spinZ d ℓ 0)).re := by
  sorry
end Heisenberg
end
DEFS(31): abbrev L2, def l2Reindex, def l2Projection, abbrev Site, abbrev Level, abbrev Configuration, abbrev SpinHilbert, abbrev SpinOperator, def configPerm, def matrixUnit, def operatorRelabel, def quasiLocalAlgebra, abbrev QuasiLocal, def localUnit, def translation, def magneticLevel, def spinZ, def spinPlus, def spinMinus, def spinX, def spinY, def NearestNeighbor, def volumeEdges, def hamiltonian, def box, def finiteDynamics, def dynamics, def DynamicsConverges, structure State, def TranslationInvariant
## PAPER Spontaneous-magnetization-in-the-quantum-Heisenberg-ferromagnet-September-24-2026
ABSTRACT: For every dimension $d\geq3$ and every spin $S\in\{\frac12,1,\frac32,\ldots\}$, we prove that the nearest-neighbor isotropic quantum Heisenberg ferromagnet has a translation-invariant, spontaneously magnetized equilibrium state at every sufficiently low positive temperature. The same state satisfies the KMS condition for the zero-field dynamics and has magnetization at least $S/4$. This resolves the low-temperature ordering problem in the spontaneous-magnetization formulation.
[theorem] \label{thm:main} For every integer $d\geq3$ and every $S\in\{\frac12,1,\frac32,\ldots\}$, there is a finite $\beta_0(d,S)>0$ such that, for every finite $\beta\geq\beta_0(d,S)$, the dynamics associated with \eqref{eq:hamiltonian} has a translation-invariant $\beta$-KMS state $\omega$ satisfying \[ \omega(S_0^z)\ge S/4. \]
==================
# FAMILY 272: Entanglement without distillable secret key
SCOPE: The paper's entanglement construction yields counterexamples to PPT-composition claims. The linked formalization covers these consequences: two explicitly specified PPT maps on $10\times10$ complex matrices have a composition that is not entanglement breaking, and the nonzero Choi matrix of that composition has no nonzero product vector in its range. A separate trace-preserving PPT channel on $21\times21$ matrices has a square that is not entanglement breaking. The paper's zero-distillable-secret-key statement is outside these two selected Comparator statements.
## CHALLENGE DimensionTenChannel  targets=['OAI.DimensionTen.exists_channel_fin21'] defs=[]
theorem exists_channel_fin21 :
    ∃ Θ : ChannelCompletion.Map (Fin 21) (Fin 21),
      ChannelCompletion.PPT Θ ∧ ChannelCompletion.TracePreserving Θ ∧
        ¬ ChannelCompletion.EntanglementBreaking (Θ.comp Θ) := by
  sorry
end DimensionTen
end
DEFS(9): abbrev Mat, abbrev Map, def amplify, def CP, def transposeMap, def PPT, def TracePreserving, def Separable, def EntanglementBreaking
## CHALLENGE DimensionTenPair  targets=['OAI.DimensionTen.main_pair'] defs=[]
theorem main_pair :
    ∃ Φ₁ Φ₂ : Mat 10 → Mat 10,
      Φ₁ = phiOne ∧ Φ₂ = phiTwo ∧ PPT Φ₁ ∧ PPT Φ₂ ∧
      (let Z := choi (Φ₂ ∘ Φ₁)
       Z ≠ 0 ∧
       (∀ u v : Fin 10 → ℂ, ∀ w : Fin 10 × Fin 10 → ℂ,
         Z *ᵥ w = productVector u v → u = 0 ∨ v = 0) ∧
       ¬ EntanglementBreaking (Φ₂ ∘ Φ₁)) := by
  sorry
end DimensionTen
end
DEFS(25): def blocksZ, def blocks, def pencilMap, abbrev Mat, def IsComplexLinear, def amplify, def CompletelyPositive, def PPT, def separable, def EntanglementBreaking, def choi, def tensorMap, def hsAdjoint, def symmetricPairs, def exteriorPairs, def symmetricIsometry, def exteriorIsometry, def hodgeComplement, def firstSix, def exteriorMap, def complementaryMap, def phiOne, def phiTwo, def compositeChoi, def productVector
## PAPER Entanglement-with-zero-distillable-secret-key-in-local-dimension-ten-September-27-2026
ABSTRACT: We construct an entangled state on $\C^{10}\otimes\C^{10}$ with zero distillable secret key for the local-instrument protocols specified here. They allow joint processing of all copies and unlimited two-way public communication, with the input as the only shared private resource and an eavesdropper holding a purification and the complete public record. The construction also disproves the unrestricted two-map PPT-composition conjecture. A separate trace-preserving PPT channel on $\Mat{21}$ has a square that is not entanglement breaking.
[theorem] \label{thm:main-state} There is an explicitly specified entangled density operator $\rho$ on $\C^{10}\otimes\C^{10}$ whose range contains no nonzero product vector and for which $K_D(\rho)=0$. More precisely, let $n\geq1$ and let $\tau_{K_AK_BE'}$ be the normalized output of any admitted completed bit-output protocol of Definition~\ref{def:protocol} on $\rho^{\otimes n}$, where $E'$ retains an initial purification and the complete public transcript. For every state $\sigma_{E'}$, \begin{equation}\label{eq:main-gap} \left\lVert \tau_{K_AK_BE'}- \frac12\sum_{i=0}^1|i,i\rangle\langle i,i|\otimes\sigma_{E'} \right\rVert_1\geq\frac15. \end{equation} Thus the corresponding trace distance, with its
==================
# FAMILY 273: The entropy photon-number inequality
SCOPE: The formalization proves the entropy photon-number inequality for two independent bosonic inputs with finite mean energy and any finite positive number $n$ of modes. Write $N(\rho)=g^{-1}(S(\rho)/n)$, where $S$ is von Neumann entropy and $g(x)=(x+1)\log(x+1)-x\log x$ is the thermal entropy per mode. For a beam splitter of transmissivity $0\le\eta\le1$, its output satisfies $N(\rho_C)\ge\eta N(\rho_A)+(1-\eta)N(\rho_B)$. Entanglement among modes within either input is allowed. The thermal-attenuator minimum-output-entropy and broadcast-capacity consequences in the paper are outside this selected inequality.
## CHALLENGE EntropyPhotonNumber  targets=['OAI.EntropyPhotonNumber.entropy_photon_number_inequality'] defs=[]
theorem entropy_photon_number_inequality
    (n : ℕ) (hn : 1 ≤ n) (ρA ρB ρC : State n)
    (hA : FiniteEnergy ρA) (hB : FiniteEnergy ρB)
    (η : ℝ) (hη : η ∈ Set.Icc 0 1)
    (hC : IsBeamSplitterOutput η ρA ρB ρC) :
    η * gInv (entropy ρA / n) + (1 - η) * gInv (entropy ρB / n) ≤
      gInv (entropy ρC / n) := by
  sorry
end EntropyPhotonNumber
end
DEFS(17): abbrev NumberIndex, abbrev Fock, def numberKet, def entry, structure State, def totalNumber, def FiniteEnergy, def entropy, def g, def gInv, def oneModeBeamCoefficient, def beamCoefficient, abbrev SectorSplit, def splitLeft, def splitRight, def outputBlock, def IsBeamSplitterOutput
## PAPER The-entropy-photon-number-inequality-September-24-2026
ABSTRACT: We prove the entropy photon-number inequality for two independent bosonic inputs with finite mean energy, for every finite number of modes. This resolves the entropy photon-number conjecture in this finite-energy setting while allowing arbitrary entanglement among the modes within either input. As a consequence, we determine the exact minimum output entropy at fixed input entropy for every finite tensor power of an identical thermal attenuator, over finite-energy inputs that may be entangled across modes. We also obtain the exact classical capacity region of the degraded two-receiver pure-loss bosonic broadcast channel under a mean photon constraint.
[theorem[Entropy photon-number inequality]] \label{thm:epni} Let \(n\ge1\) be finite, and let \(\rho_A,\rho_B\) be states on \(n\) bosonic modes, with annihilation operators \(a_1,\ldots,a_n\) and \(b_1,\ldots,b_n\), respectively, satisfying \[ \Tr\rho_A\sum_{j=1}^n a_j^\dagger a_j<\infty, \qquad \Tr\rho_B\sum_{j=1}^n b_j^\dagger b_j<\infty. \] The joint input is \(\rho_A\otimes\rho_B\); no independence assumption is made among the modes within either state. For \(0\le\eta\le1\), let \(\rho_C\) be the reduced state of the modes \[ c_j=\sqrt\eta\,a_j+\sqrt{1-\eta}\,b_j,\qquad 1\le j\le n, \] after passive beam-splitter mixing. Then \begin{equation}\label{eq:epni} g^{-1}\!\left(\frac{S(\rho_C)}n\right) \ge \eta\,g^{-1}\!\left(\frac{S(\r
==================
# FAMILY 274: Parity is not in QAC<sup>0</sup>
SCOPE: The formalization rules out bounded-error parity computation by constant-depth quantum circuits with polynomially many zero-initialized ancillary qubits. For every fixed depth, polynomial bound on the total number of qubits, and $0<\varepsilon\le1/2$, every sufficiently large input length has an input on which the measured-output parity success probability is less than $1/2+\varepsilon$. A companion specialization gives success strictly below $2/3$. The formalization also includes the product-projection localization estimate supporting this bound. The formalized result supplies the polynomial-size parity consequence of the paper. For every fixed circuit depth and polynomial bound on the number of qubits, all sufficiently large input lengths have an input on which any such circuit computes measured-output parity with probability strictly below $2/3$. Ancillary qubits start at zero. The fo
## CHALLENGE QACParity  targets=['OAI.QAC.parity_lower_bound'] defs=[]
DEFS(17): abbrev Bit, abbrev Word, abbrev Operator, abbrev QubitOperator, def tensorMatrix, inductive Gate, def support, def toffoliWord, def matrix, structure PhysicalLayer, def physicalLayerMatrix, def physicalCircuitMatrix, def inputWord, def parity, def successProbability, def ParityStatement, theorem QAC.parity_lower_bound
## CHALLENGE RegularParity  targets=['OAI.QAC.parity_lower_bound_polynomial_size'] defs=[]
theorem parity_lower_bound_polynomial_size (d k C : ℕ)
    (_hd : 0 < d) (_hk : 0 < k) (_hC : 0 < C) :
    ∃ n₀ : ℕ, ∀ n ≥ n₀, ∀ N : ℕ, n ≤ N → N ≤ C * (n + 1) ^ k →
      ∀ layers : List (PhysicalLayer N), layers.length ≤ d →
        ∀ out : Fin N, ∃ x : Word n,
          successProbability (physicalCircuitMatrix layers) out x < (2 : ℝ) / 3 := by
  sorry
end QAC
end
DEFS(15): abbrev Bit, abbrev Word, abbrev Operator, abbrev QubitOperator, def tensorMatrix, inductive Gate, def support, def toffoliWord, def matrix, structure PhysicalLayer, def physicalLayerMatrix, def physicalCircuitMatrix, def inputWord, def parity, def successProbability
## CHALLENGE RegularParity  targets=['OAI.QAC.parity_lower_bound_polynomial_size'] defs=[]
theorem parity_lower_bound_polynomial_size (d k C : ℕ)
    (_hd : 0 < d) (_hk : 0 < k) (_hC : 0 < C) :
    ∃ n₀ : ℕ, ∀ n ≥ n₀, ∀ N : ℕ, n ≤ N → N ≤ C * (n + 1) ^ k →
      ∀ layers : List (PhysicalLayer N), layers.length ≤ d →
        ∀ out : Fin N, ∃ x : Word n,
          successProbability (physicalCircuitMatrix layers) out x < (2 : ℝ) / 3 := by
  sorry
end QAC
end
DEFS(15): abbrev Bit, abbrev Word, abbrev Operator, abbrev QubitOperator, def tensorMatrix, inductive Gate, def support, def toffoliWord, def matrix, structure PhysicalLayer, def physicalLayerMatrix, def physicalCircuitMatrix, def inputWord, def parity, def successProbability
## CHALLENGE QACParity  targets=['OAI.QAC.parity_lower_bound'] defs=[]
DEFS(17): abbrev Bit, abbrev Word, abbrev Operator, abbrev QubitOperator, def tensorMatrix, inductive Gate, def support, def toffoliWord, def matrix, structure PhysicalLayer, def physicalLayerMatrix, def physicalCircuitMatrix, def inputWord, def parity, def successProbability, def ParityStatement, theorem QAC.parity_lower_bound
## PAPER Product-projection-localization-and-the-QAC0-parity-lower-bound-September-24-2026
ABSTRACT: We prove that constant-depth quantum circuits with arbitrary one-qubit and unbounded-arity Toffoli gates cannot compute parity with any fixed positive worst-case advantage using polynomially many qubits. Ancillas start in zero, only one output qubit is measured, and all final garbage is unrestricted. This resolves Moore's parity conjecture in the measured-output model.
[theorem[Parity lower bound]] \label{thm:parity} Fix a nonnegative integer \(d\), a real number \(c\ge1\), and \(0<\varepsilon\le1/2\). For all sufficiently large \(n\), no circuit of depth at most \(d\) on \(n\) input qubits and at most \(n^c\) total qubits, using arbitrary one-qubit unitaries and unbounded-arity Toffoli gates, computes \(\parity(x)\) with probability at least \(1/2+\varepsilon\) for every \(x\in\{0,1\}^n\). Gates in each layer have disjoint supports, ancillas start in \(\ket0\), and one output qubit is measured; the other qubits may be discarded.
## PAPER Regular-trajectories-pruning-and-quantum-parity-September-24-2026
ABSTRACT: We prove that constant-depth quantum circuits with arbitrary one-qubit gates and unbounded-arity Toffoli gates cannot compute parity with any fixed positive worst-case advantage using polynomially many total qubits. Ancillary qubits are initialized to $|0\rangle$, one output qubit is measured, and all other final registers may be discarded without restriction. This resolves Moore's parity conjecture in the measured-output model.
[theorem] \label{thm:parity} Fix positive integers $d,k,C$ and a real $0<\varepsilon\le1/2$. There is an integer $n_0=n_0(d,k,C,\varepsilon)$ such that, for every $n\ge n_0$, every allowed circuit of depth at most $d$ on at most $C(n+1)^k$ total qubits has an input $x\in\{0,1\}^{n}$ on which its answer equals $\Parity_n(x)$ with probability strictly less than $1/2+\varepsilon$.
==================
# FAMILY 275: QMA-hardness of continuum Coulomb energy
SCOPE: The formalization proves QMA-hardness of approximating the electronic Coulomb spectral infimum in three-dimensional continuum space when positive integer nuclear charges are encoded in binary. The instances have distinct rational nuclear positions and a unary electron count, and the energy ranges over antisymmetric continuum states and all spin sectors. A deterministic polynomial-time many-one reduction produces the promise gap with threshold separation at least one, while keeping the complete output length polynomial. The same Comparator file also contains the companion unit-charge result. The formalization proves QMA-hardness of approximating the electronic ground-energy infimum for clamped unit-charge nuclei in the full spinful fermionic continuum. The reduction is deterministic and polynomial time, with rational nuclear positions and separated rational energy thresholds. No orbital b
## CHALLENGE ContinuumCoulombHardness  targets=['OAI.ContinuumCoulomb.unit_coulomb_qmaHard', 'OAI.ContinuumCoulomb.binary_coulomb_qmaHard'] defs=[]
theorem unit_coulomb_qmaHard : QMAHard unitCoulombCodec.encode unitCoulombPromise := by
  sorry
theorem binary_coulomb_qmaHard : QMAHard binaryCoulombCodec.encode binaryCoulombPromise := by
  sorry
end ContinuumCoulomb
end
DEFS(99): abbrev BitString, structure Codec, def encodeDigits, def readDigits, theorem readDigits_encode, def decodeDigits, theorem decodeDigits_bits, def natural, def encodeUnary, def readUnary, theorem readUnary_encode, def unary, def integer, def pair, def readCount, theorem readCount_encode, def list, def equiv, def sum, abbrev Space, abbrev Configuration, abbrev Spins, structure Nuclei, def position, def coulombKernel, def attraction, def permute, structure H1Vector, def Antisymmetric, def mass
## CHALLENGE ContinuumCoulombHardness  targets=['OAI.ContinuumCoulomb.unit_coulomb_qmaHard', 'OAI.ContinuumCoulomb.binary_coulomb_qmaHard'] defs=[]
theorem unit_coulomb_qmaHard : QMAHard unitCoulombCodec.encode unitCoulombPromise := by
  sorry
theorem binary_coulomb_qmaHard : QMAHard binaryCoulombCodec.encode binaryCoulombPromise := by
  sorry
end ContinuumCoulomb
end
DEFS(99): abbrev BitString, structure Codec, def encodeDigits, def readDigits, theorem readDigits_encode, def decodeDigits, theorem decodeDigits_bits, def natural, def encodeUnary, def readUnary, theorem readUnary_encode, def unary, def integer, def pair, def readCount, theorem readCount_encode, def list, def equiv, def sum, abbrev Space, abbrev Configuration, abbrev Spins, structure Nuclei, def position, def coulombKernel, def attraction, def permute, structure H1Vector, def Antisymmetric, def mass
## PAPER Continuum-Coulomb-hardness-with-binary-nuclear-charges-September-24-2026
ABSTRACT: We prove that approximating the electronic Coulomb spectral infimum in three-dimensional space is QMA-hard when positive integer nuclear charges are encoded in binary. The nuclei have distinct rational positions, the electron number is unary, and the energy is minimized over all antisymmetric continuum states and spin sectors. A deterministic classical polynomial-time reduction produces instances with threshold separation at least one. The nuclear charges may be exponentially large, but every output has polynomial bit length.
[theorem] \label{thm:main} The promise problem above is QMA-hard under deterministic classical polynomial-time many-one reductions for $c=1$. The reduction can produce instances with $b-a\ge1$.
## PAPER QMA-hardness-of-continuum-Coulomb-energy-with-unit-nuclear-charges-September-24-2026
ABSTRACT: We prove that approximating the electronic ground-energy infimum for clamped unit-charge nuclei is QMA-hard on the full spinful fermionic continuum space. A deterministic classical polynomial-time reduction produces polynomially many nuclei at distinct rational positions and polynomially many electrons, with polynomial rational bit lengths and threshold separation at least one. No orbital basis, magnetic field, or additional external potential is supplied, and no binding assumption is imposed.
[theorem[Unit-charge Coulomb hardness]] \label{thm:main} The electronic promise problem for~\eqref{eq:electronic-H} on $\mathcal H_N$, with distinct rational nuclear positions, all nuclear charges equal to one, unary electron number, and rational thresholds separated by at least $L^{-1}$, is QMA-hard under deterministic classical polynomial-time many-one reductions. The reduction produces polynomially many nuclei and electrons, polynomial rational bit lengths, and threshold separation at least one. The only output data are the nuclear positions, electron number, and thresholds.
==================
# FAMILY 276: Classical capacity of generalized amplitude damping
SCOPE: The formalized result determines the unassisted classical capacity of every generalized amplitude-damping channel with parameters in $[0,1]^2$. Its unrestricted Holevo information is additive across every number of repeated uses, equals an attained scalar maximum, and agrees with the operational capacity per use. Every maximizing equiprobable phase-pair product ensemble attains the corresponding block value. Additivity with an arbitrary different partner channel and decoding by separate measurements are not included.
## CHALLENGE AmplitudeDamping  targets=['OAI.GAD.main'] defs=[]
theorem main (γ ν : ℝ) (hγ : γ ∈ Set.Icc (0 : ℝ) 1)
    (hν : ν ∈ Set.Icc (0 : ℝ) 1) :
    (∀ n : ℕ, 1 ≤ n → holevo γ ν n = (n : ℝ) * holevo γ ν 1) ∧
    (∃ p : ℝ, Maximizes γ ν p ∧
      ∀ n : ℕ, 1 ≤ n → holevo γ ν n = (n : ℝ) / Real.log 2 * objective γ ν p) ∧
    capacity γ ν = holevo γ ν 1 ∧
    (∀ p : ℝ, Maximizes γ ν p → ∀ n : ℕ, 1 ≤ n →
      (∀ s : Basis n, IsState (phaseState p s)) ∧
      holevo γ ν n = phaseValue γ ν p n) := by
  sorry
end GAD
end
DEFS(22): abbrev Basis, abbrev QMatrix, def entropy, def IsState, def kraus, def tensorKraus, def channel, structure Ensemble, def ensembleValue, def holevo, structure Code, def averageError, def Achievable, def capacity, def g, def v, def objective, def Maximizes, def phaseSignal, def phaseProduct, def phaseState, def phaseValue
## PAPER Classical-capacity-and-entropy-inequalities-for-generalized-amplitude-damping-September-24-2026
ABSTRACT: We determine the unassisted classical capacity of every qubit generalized amplitude-damping channel, for all damping strengths and thermal occupations. It equals the one-shot Holevo capacity and is given by a one-variable maximum. A binary pure-state ensemble attains the one-use optimum, and its independent products attain the optimum at every block length. We also prove that one-shot Holevo capacity, minimum output entropy, and regularized unassisted classical capacity are additive under tensor product with every finite-dimensional completely positive trace-preserving partner channel.
[theorem] \label{thm:main} For all $\gamma,\nu\in[0,1]$ and every integer $n\ge1$, \begin{equation}\label{eq:main} \chi(\A_{\gamma,\nu}^{\otimes n}) =n\chi(\A_{\gamma,\nu}) =\frac n{\ln2}\max_{0\le p\le1} \{h((1-\gamma)p+\gamma\nu)-g(v_{\gamma,\nu}(p))\}, \end{equation} where \begin{equation}\label{eq:v-main} v_{\gamma,\nu}(p) =\gamma\nu(1-\nu)+\gamma(1-\gamma)(p-\nu)^2. \end{equation} In particular, $C(\A_{\gamma,\nu})=\chi(\A_{\gamma,\nu})$. If $p$ maximizes \eqref{eq:main}, independent products of the two equiprobable signals \begin{equation}\label{eq:pair} \phi_\pm=\sqrt{1-p}\,\ket0\ \pm\sqrt p\,\ket1 \end{equation} attain the Holevo information at every block length.
==================
# FAMILY 277: Threshold repetition for entangled games
SCOPE: The formalization gives exponential threshold parallel repetition for every finite two-player game with arbitrary correlated questions. If its finite-dimensional entangled value is $v<1$, its answer sets are $A,B$, and $0<\delta<1-v$, then the probability of winning at least the fraction $v+\delta$ of $k$ repetitions is at most $\exp(-\kappa\delta^{13}k/(1+\log(|A||B|)))$ for one universal $\kappa>0$. The bound applies to every joint finite-dimensional strategy and to their supremum, without assuming attainment. The separate distribution-dependent cubic bound is outside this scope.
## CHALLENGE EntangledGames  targets=['OAI.ThresholdParallelRepetition.threshold_parallel_repetition'] defs=[]
theorem threshold_parallel_repetition :
    ∃ κ₀ : ℝ, 0 < κ₀ ∧
      ∀ (x y a b : ℕ) (G : Game x y a b), entangledValue G < 1 →
      ∀ (δ : ℝ), 0 < δ → δ < 1 - entangledValue G →
      ∀ (k : ℕ), 1 ≤ k →
        (∀ S : RepeatedStrategy x y a b k,
          thresholdProbability G δ S ≤
            Real.exp (-κ₀ * δ ^ 13 / (1 + Real.log (((a + 1) * (b + 1) : ℕ) : ℝ)) * k)) ∧
        thresholdValue (k := k) G δ ≤
          Real.exp (-κ₀ * δ ^ 13 / (1 + Real.log (((a + 1) * (b + 1) : ℕ) : ℝ)) * k) := by
  sorry
end ThresholdParallelRepetition
end
DEFS(10): structure Game, structure Strategy, def Strategy.born, abbrev SingleStrategy, def successProbability, def entangledValue, abbrev RepeatedStrategy, def wins, def thresholdProbability, def thresholdValue
## PAPER Threshold-parallel-repetition-for-finite-dimensional-entangled-games-September-25-2026
ABSTRACT: For every finite two-player game with entangled value $v<1$, we prove exponential decay for the probability of winning at least a $v+\delta$ fraction of $k$ independent repetitions, uniformly over all finite-dimensional joint strategies. The result allows arbitrary correlated question distributions and holds for every $0<\delta<1-v$ and $k\ge1$. Its universal rate is proportional to $\delta^5/(1+\log(|\mathcal A||\mathcal B|))$, where $\mathcal A,\mathcal B$ are the answer alphabets. For each fixed question distribution, we also obtain an explicit cubic rate in $\delta$.
[theorem[Threshold parallel repetition]] \label{thm:main} There is a universal constant $\kappa_0>0$ such that the following holds. Let $G$ be any finite two-player one-round game with Boolean acceptance predicate and entangled value $v=\omega^*(G)<1$. For every $0<\delta<1-v$, every integer $k\ge1$, and every finite-dimensional joint strategy for $k$ repetitions, \begin{equation}\label{eq:main} \Pr\!\left[W_k\ge\lceil(v+\delta)k\rceil\right] \le \exp\!\left(-\frac{\kappa_0\delta^5} {1+\log d}\,k\right). \end{equation} The same inequality holds for the supremum over those strategies.
==================
# FAMILY 279: Exact quantum factoring over a fixed finite gate set
SCOPE: The formalization constructs a polynomial-time uniform quantum circuit family that outputs the complete prime factorization of every integer $N\ge2$ with probability exactly one. The circuits use one fixed finite set of bounded-arity gates, and both the gate count and number of qubits have polynomial worst-case bounds in the bit length of $N$. The probability-one conclusion is exact, rather than an asymptotic or bounded-error guarantee.
## CHALLENGE ExactQuantumFactoring  targets=['OAI.ExactQuantumFactoring.exact_quantum_factoring'] defs=[]
theorem exact_quantum_factoring : MainTheorem := by
  sorry
end ExactQuantumFactoring
DEFS(27): inductive Primitive, def Primitive.arity, def Primitive.code, structure Gate, def Gate.arity, def Primitive.matrix, def Gate.baseMatrix, def Gate.matrix, structure Instruction, abbrev Basis, abbrev State, def Instruction.matrix, structure Circuit, def Circuit.apply, def inputBasis, def Circuit.outputState, def paddedLength, def readBit, def outputList, def CorrectEncoding, def Circuit.correctProbability, def natWord, def Instruction.encode, def Circuit.encode, def Uniform, def PolynomialResources, def MainTheorem
## PAPER Exact-quantum-factoring-over-a-fixed-finite-gate-set-September-25-2026
ABSTRACT: We give a polynomial-time uniform quantum circuit family that outputs the complete prime factorization of every integer $N\ge2$ with probability one. A fixed finite set of bounded-arity gates suffices, and both the gate count and the number of qubits have polynomial worst-case bounds in the input length.
[theorem] \label{thm:main} There is a polynomial-time uniform family of polynomial-size quantum circuits that outputs the complete prime factorization of every input integer $N\ge2$ with probability one. The number of gates and qubits is bounded by a fixed polynomial in the bit length of $N$. One fixed finite gate set suffices: NOT, CNOT, Toffoli, Hadamard, $\operatorname{diag}(1,i)$, their inverses, and their singly controlled versions.
==================
# FAMILY 280: Unitary vertex operator algebras and conformal nets
SCOPE: The linked formalization proves the first construction step relating strongly rational unitary vertex operator algebras to conformal nets. For a simple unitary strongly rational vertex operator algebra, it establishes polynomial energy bounds and strong locality and constructs an irreducible conformal net with the stated covariance, vacuum, and positive-energy properties. The selected statement does not include complete rationality of the net, unitarizability of all simple modules, the braided tensor equivalence, or the classification of local extensions described in the paper.
## CHALLENGE VertexAlgebraNet  targets=['OAI.MinimalVertex.main'] defs=[]
theorem main (_hSimple : A.toVertexAlgebra.IsSimple)
    (hSR : A.IsStronglyRational.{u,v}) :
    A.PolynomialEnergyBounds ∧ OAI.MinimalVertex.CKLWStrongLocal U hSR.2.2 ∧
      Nonempty (OAI.MinimalVertex.IrreducibleConformalNetStructure (OAI.MinimalVertex.intervalAlgebra U hSR.2.2)) := by
  sorry
end OAI.MinimalVertex
DEFS(85): abbrev StateField, def mode, def JacobiIdentity, structure VertexAlgebra, def translation, def c2, def C2Cofinite, def IsIdeal, def IsSimple, def ModuleJacobiIdentity, structure WeakModule, def IsInvariant, def CompletelyReducible, structure CFTTypeVOA, def virasoroMode, def physicalMode, def energyShift, def gradingEquiv, def IsAdmissible, def IsRational, def PolynomialEnergyBound, def PolynomialEnergyBounds, structure UnitaryStructure, def _root_.OAI.MinimalVertex.Code.StronglyRationalVOA.HilbertCore.space, def _root_.OAI.MinimalVertex.Code.StronglyRationalVOA.HilbertCore.equiv, def _root_.OAI.MinimalVertex.Code.StronglyRationalVOA.HilbertCore.operator, def RapidCoefficients, def tsumMap, structure SmoothCircleFunction, def _root_.OAI.MinimalVertex.Code.StronglyRationalVOA.SmoothCircleFunction.coefficient
## PAPER Strongly-rational-unitary-vertex-operator-algebras-and-conformal-nets-September-25-2026
ABSTRACT: Every simple unitary strongly rational vertex operator algebra generates a completely rational conformal net. All its simple grading-restricted modules are unitarizable, its canonical fusion forms are positive, and the Carpi--Weiner--Xu functor gives a braided unitary tensor equivalence from its grading-restricted finite-length module category onto the finite-index sectors of the net. Gui's extension theorems then identify normalized irreducible finite-index local extensions of these nets with simple CFT-type conformal extensions of the vertex operator algebras.
[theorem] \label{thm:main} Let $V$ be a simple unitary strongly rational vertex operator algebra over $\mathbb C$. Then: \begin{enumerate}[label=\textup{(\arabic*)}] \item $V$ has polynomial energy bounds and is CKLW-strongly local. The algebras \eqref{eq:intro-net} form an irreducible conformal net $A_V$. \item $V$ is completely unitary: every simple grading-restricted module is unitarizable, and all canonical invariant Hermitian fusion forms are positive definite. \item Every unitary grading-restricted finite-length module is strongly integrable, with the closed-field equality \eqref{eq:intro-cwx}. \item The net $A_V$ is completely rational. \item After choosing invariant positive forms on the simpl
==================
# FAMILY 281: QAOA attains the SK optimum in the thermodynamic-first limit
SCOPE: The linked formalization supplies variational identities for the Gaussian zero-field Sherrington–Kirkpatrick ground-state energy used in the paper's QAOA argument. Conditional on an admissible Parisi minimizer and its associated diffusion, it proves convergence of the finite-system ground-state energy, identifies its limit with the Parisi value, and gives equivalent terminal-martingale and integrated-curvature formulas. It also proves convergence of finite Gaussian coefficient sums to the curvature integral, which approaches the ground-state value as the terminal time tends to one. The selected statement covers these value and approximation results; it does not itself assert convergence of QAOA circuit energies. The formalization proves that every admissible integrable minimizer of the zero-temperature Parisi functional for the pure zero-field Sherrington–Kirkpatrick model has full relat
## CHALLENGE SKValue  targets=['OAI.SKValue.value_consequences'] defs=[]
theorem value_consequences :
    (∀ (W : BrownianSpace) (γ : OrderParameter) (X : ℝ → W.Ω → ℝ),
      IsMinimizer W γ → IsDiffusion W γ X → ScalarValueConclusion W γ X) ∧
    (∀ (W : BrownianSpace) (γ : OrderParameter) (X : ℝ → W.Ω → ℝ) (T : ℝ),
      0 < T → T < 1 → IsMinimizer W γ → IsDiffusion W γ X →
      FiniteGaussianConclusion W γ X T) ∧
    (∀ (W : BrownianSpace) (γ : OrderParameter),
      IsMinimizer W γ → groundStateValue = parisi W γ) := by
  sorry
end SKValue
DEFS(34): def standardGaussian, def gaussianProduct, instance gaussianProduct_probability, def coordinate, def stepSize, def meshTime, def euler, structure OrderParameter, structure BrownianSpace, def BrownianSpace.filtration, def shiftedFiltration, def Admissible, def controlPayoff, def phi, def gradient, def curvature, def parisi, def IsMinimizer, def IsDiffusion, def spin, def hamiltonian, def groundStateSequence, def groundStateValue, def gradientStopped, def ScalarValueConclusion, def eulerPath, def rawCoefficient, def normalizer, def gaussianIncrement, def roundedSign
## CHALLENGE SKFullSupport  targets=['OAI.ZeroTemperatureSK.full_support'] defs=[]
theorem full_support (W : BrownianSystem Ω) (γ : OrderParameter)
    (hmin : IsMinimizer W γ) : FullSupportConclusion W γ := by
  sorry
end ZeroTemperatureSK
end
DEFS(16): abbrev Time, def extend, structure OrderParameter, structure BrownianSystem, def incrementFiltration, structure Control, def controlPayoff, def value, def gradient, def curvature, def parisi, def IsMinimizer, def IsStieltjesMeasure, def IsDiffusion, def squareMoment, def FullSupportConclusion
## PAPER QAOA-attains-the-SK-ground-state-energy-in-the-thermodynamic-first-limit-September-25-2026
ABSTRACT: We prove that the Quantum Approximate Optimization Algorithm (QAOA) approaches the ground-state energy per spin of the Gaussian zero-field Sherrington--Kirkpatrick model when system size tends to infinity first and circuit depth then increases. For every accuracy, some finite depth and deterministic angles, independent of system size and disorder, achieve that accuracy in the limiting expected energy per spin using the standard cost Hamiltonian and transverse-field mixer. This proves the eventual Parisi-optimality conjecture of Basso, Farhi, Marwaha, Villalonga, and Zhou in its fixed-parameter thermodynamic formulation. We give no quantitative bound on the required depth or efficient angle-s
[theorem] \label{thm:main} For the zero-field SK model~\eqref{eq:sk-model}, \begin{equation}\label{eq:main-result} \lim_{p\to\infty}Q_p=\Pstar. \end{equation} Equivalently, for every $\varepsilon>0$ there exist a finite integer $p$ and deterministic real vectors $\gamma,\beta\in\R^p$, independent of $n$ and $J$, such that $v_p(\gamma,\beta)\ge\Pstar-\varepsilon$.
## PAPER Full-support-of-the-zero-temperature-Sherrington-Kirkpatrick-order-parameter-September-27-2026
ABSTRACT: We prove that every admissible integrable minimizer of the zero-temperature Parisi functional for the pure, zero-field Sherrington--Kirkpatrick model has full relative Stieltjes support on $[0,1)$. Thus its support has no gaps at any overlap scale below one. We use the covariance normalization $\xi(t)=t^2/2$.
[theorem[Full support at zero temperature]] \label{thm:full-support} If $\gamma\in\mathcal U$ minimizes $\mathcal P$, then \[ \supp\mu_\gamma=[0,1). \] In particular $\gamma(b)>\gamma(a)$ whenever $0\leq a<b<1$. For the solution of~\eqref{eq:model-diffusion}, \begin{equation}\label{eq:main-consistency} \E[u_\gamma(t,X_t)^2]=t,\qquad \E[\Phi_{\gamma,xx}(t,X_t)^2]=1, \qquad 0\leq t<1. \end{equation}
==================
# FAMILY 287: Isomorphism of the free group factors
SCOPE: The free group factor problem asks whether the von Neumann algebras of free groups of different ranks are isomorphic. The formalization proves that interpolated free group factors with any parameters $r,s>1$, including the infinite parameter, are normally trace-preservingly isomorphic. The paper's fundamental-group conclusion is a further consequence rather than a separate selected statement here.
## CHALLENGE InterpolatedFactors  targets=['OAI.FreeGroupFactorMain.Interpolation.allInterpolatedIsomorphic'] defs=[]
theorem allInterpolatedIsomorphic (r s : ℝ≥0∞) (hr : 1<r) (hs : 1<s) :
    Nonempty (NormalTracialEquiv (interpolatedTrace r) (interpolatedTrace s)
      (interpolatedTopology r) (interpolatedTopology s)) := by
  sorry
end FreeGroupFactorMain.Interpolation
end
DEFS(41): abbrev GroupHilbert, abbrev GroupOperator, def leftTranslations, def groupVonNeumann, def canonicalTrace, def ultraweakOperatorTopology, def groupUltraweakTopology, abbrev FreeGroupRank, instance groupVN_isClosed, instance groupVN_CStarAlgebra, def cornerSubalgebra, abbrev Corner, instance cornerClosed, instance cornerSemiring, instance cornerRing, instance cornerAlgebra, instance cornerNormedRing, instance cornerCStarAlgebra, def cornerTopology, def normalizedCornerTrace, def stabilizedRightTranslations, def stabilization, instance stabilization_isClosed, instance stabilization_CStarAlgebra, def stabilizedProjectionTrace, def stabilizedTrace, def stabilizationTopology, structure NormalTracialEquiv, abbrev RankTwoProjection, instance rankTwoProjectionInhabited
## PAPER An-isomorphism-of-the-free-group-factors-September-23-2026
ABSTRACT: We solve the free group factor isomorphism problem affirmatively by proving that $L(\F_2)$ and $L(\F_3)$ are isomorphic as tracial von Neumann algebras. The classical free group factor alternative then implies that all interpolated free group factors, including $L(\F_\infty)$, are isomorphic and have fundamental group $\R_{>0}$.
[theorem[Isomorphism of consecutive ranks]] \label{thm:rank-step} For every integer $n\geq3$ there is a unital trace-preserving normal $*$-isomorphism \[ L(\F_n)\cong L(\F_{n+1}). \]
==================
# FAMILY 288: Kadison's similarity conjecture
SCOPE: Kadison's similarity problem asks whether every bounded unital homomorphism from a unital complex $C^*$-algebra into operators on a Hilbert space is similar to a $*$-homomorphism. The formalization proves this for arbitrary Hilbert spaces. It also gives one universal hyperreflexivity constant for all unital von Neumann algebras. The linked commutator estimate is uniform over all finite matrix amplifications: its constant is independent of the algebra, Hilbert space, and amplification size. This is the quantitative derivation estimate supporting the similarity result.
## CHALLENGE KadisonSimilarity  targets=['OAI.KadisonSimilarity.universalCommutatorTheorem', 'OAI.KadisonSimilarity.universalHyperreflexivity', 'OAI.KadisonSimilarity.similarityTheorem'] defs=[]
theorem universalCommutatorTheorem : UniversalCommutatorTheorem.{u} := by
  sorry
/-- Every von Neumann algebra has hyperreflexivity constant at most `2 * universalConstant`. -/
theorem universalHyperreflexivity : UniversalHyperreflexivity.{u} universalConstant := by
  sorry
/-- Every bounded unital representation is similar to a star representation. -/
theorem similarityTheorem : SimilarityTheorem.{u,v} := by
  sorry
end KadisonSimilarity
end
DEFS(20): abbrev BoundedUnitalHom, def SimilarToStar, def commutator, abbrev HilbertCopies, def matrixOperator, def amplify, def innerDerivation, def scalarCommutatorNorm, def CommutatorEstimate, def UniformCommutatorEstimate, def UniversalCommutatorTheorem, def SimilarityTheorem, abbrev CommutantProjection, def offDiagonalSeminorm, def UniversalHyperreflexivity, def rowConstant, def cyclicConstant, def cornerConstant, def factorConstant, def universalConstant
## CHALLENGE UniformCommutator  targets=['OAI.Kadison.uniform_commutator'] defs=[]
theorem uniform_commutator :
    ∃ C : ℝ, 0 ≤ C ∧ ∀ (K : Type u) [NormedAddCommGroup K] [InnerProductSpace ℂ K]
      [CompleteSpace K] (P : VonNeumannAlgebra K) (Y : K →L[ℂ] K)
      (h : ℕ), 1 ≤ h → ∀ (X : Matrix (Fin h) (Fin h) (K →L[ℂ] K)),
      (∀ i j, X i j ∈ P) →
      ‖diagonalAmplification h Y * matrixOperator h X -
        matrixOperator h X * diagonalAmplification h Y‖ ≤
        C * commutatorSeminorm P Y * ‖matrixOperator h X‖ := by
  sorry
end Kadison
end
DEFS(3): def commutatorSeminorm, def matrixOperator, def diagonalAmplification
## PAPER Kadisons-similarity-theorem-through-uniform-derivation-estimates-September-23-2026
ABSTRACT: We prove that every bounded complex-linear unital algebra homomorphism from a unital complex $C^*$-algebra into the bounded operators on an arbitrary Hilbert space is similar to a $*$-homomorphism. This resolves Kadison's similarity conjecture positively. We also obtain one universal hyperreflexivity constant for all unital von Neumann algebras on arbitrary complex Hilbert spaces.
[theorem[Similarity]] \label{thm:similarity} Let \(A\) be any unital complex \(C^*\)-algebra, let \(H\) be any complex Hilbert space, and let \(\pi:A\to\mathcal B(H)\) be a bounded, complex-linear, unital algebra homomorphism. There exists an operator \(S\in\mathcal B(H)\), invertible with bounded inverse, such that \[ \rho(a)=S\pi(a)S^{-1}\qquad(a\in A) \] is a \(*\)-homomorphism. In particular, \(\rho(a^*)=\rho(a)^*\) for every \(a\in A\).
==================
# FAMILY 289: Strong Kadison–Kastler stability and its spatial boundaries
SCOPE: The formalization proves the strong Kadison–Kastler conjecture uniformly. For every $\varepsilon>0$, there is a $\delta>0$ such that any two unital von Neumann algebras on the same complex Hilbert space at Kadison–Kastler distance below $\delta$ are conjugate by a unitary $u$ with $\lVert u-1\rVert<\varepsilon$. The tolerance depends only on $\varepsilon$, uniformly over the algebras, their representations, and the Hilbert space.
## CHALLENGE StrongKadisonKastler  targets=['OAI.KadisonKastler.universal_strong_stability'] defs=[]
theorem universal_strong_stability : UniversalStrongStability.{u} := by
  sorry
end
end KadisonKastler
DEFS(6): def unitBall, def kkDistance, def unitaryConj, def Conjugates, def NearConjugacy, def UniversalStrongStability
## PAPER Universal-strong-Kadison-Kastler-stability-September-23-2026
ABSTRACT: We prove that sufficiently close unital von Neumann algebras are conjugate by a unitary arbitrarily close to the identity. The tolerance depends only on the prescribed distance of that unitary from the identity, uniformly over all algebras, representations, and Hilbert spaces. This resolves the strong Kadison--Kastler conjecture.
[theorem[Strong Kadison--Kastler stability]] \label{thm:main} For every $\eps>0$ there is $\delta=\delta(\eps)>0$ such that the following holds. If $H$ is any complex Hilbert space and $M,N\subseteq\B(H)$ are unital von Neumann algebras with identity $I_H$ and $d(M,N)<\delta$, there is a unitary $u\in\B(H)$ satisfying \[ uMu^*=N,\qquad \norm{u-I_H}<\eps. \]
==================
# FAMILY 290: Relative bicentralizers and modular spectral recovery
SCOPE: For a faithful normal state with scalar centralizer in the stated standard-space representation, the formalized result converts positive modular spectral averages into uniformly bounded algebra elements. Given unit vectors in shrinking spectral bands around a real number $s$ and a positive limiting symmetric average for a bounded operator $T$, it finds a subsequence of bounded algebra elements whose images under $T$ stay uniformly nonzero and whose spectral bands have four times the original widths. The absolute bicentralizer conjecture is not included.
## CHALLENGE BoundedRecovery  targets=['OAI.BoundedRecovery.bounded_recovery'] defs=[]
theorem bounded_recovery (S : StandardModularData H) (hscalar : S.ScalarCentralizer)
    (omega : Ultrafilter ℕ) (hfree : (omega : Filter ℕ) ≤ Filter.atTop)
    (T : H →L[ℂ] H) (s : ℝ) (delta : ℕ → ℝ) (hdelta : ∀ n, 0 < delta n)
    (hdelta0 : Tendsto delta atTop (𝓝 0)) (h : ℕ → H) (hunit : ∀ n, ‖h n‖ = 1)
    (hband : ∀ n, S.D.HasSpectralSupport (Icc (s - delta n) (s + delta n)) (h n))
    (hpositive : 0 < Filter.limsup
      (fun n => fixedMean omega (fun t => ‖T (S.D.unitary t (h n))‖ ^ 2)) atTop) :
    RecoveryConclusion S T s delta := by
  sorry
end BoundedRecovery
end
DEFS(12): def spectralCharacter, def halfExponentialCutoff, structure RealSpectralCalculus, def unitary, def halfGraph, def HasSpectralSupport, structure StandardModularData, def sigma, def ScalarCentralizer, def symmetricAverage, def fixedMean, def RecoveryConclusion
## PAPER Bounded-recovery-for-modular-spectral-averages-September-23-2026
ABSTRACT: We prove a bounded spectral recovery theorem for a von Neumann algebra with a faithful normal state whose centralizer consists only of scalars. A positive averaged squared norm for an arbitrary bounded Hilbert-space operator on shrinking modular spectral bands can be recovered on uniformly bounded algebra elements with shrinking spectral support. We apply this theorem to spectral intertwining rigidity and obtain an alternative proof of bicentralizer triviality for type $\mathrm{III}_1$ factors with separable predual.
[theorem] \label{thm:main} Let $M$ be a type $\mathrm{III}_1$ factor with separable predual and let $\phi$ be any faithful normal state on $M$. Then \[ \BC(M,\phi)=\C1. \]
==================
# FAMILY 291: Cuntz comparison, nuclear dimension, and equivariant Jiang–Su stability
SCOPE: The formalization proves that real rank zero of the uniform tracial ultrapower of the uniform tracial completion implies uniform property $\Gamma$ for a simple separable unital infinite-dimensional nuclear stably finite $C^*$-algebra with traces. The conclusion holds at every specified free ultrafilter under the corresponding real-rank-zero hypothesis. The linked comparison results also prove Jiang–Su absorption and uniform property $\Gamma$ for simple separable unital infinite-dimensional nuclear algebras with strict comparison, and for the stated stably projectionless nuclear algebras with bounded densely finite traces, a nonempty compact normalized trace base, and the prescribed finite-target-rank comparison condition.
## CHALLENGE UniformGamma  targets=['OAI.ComparatorModel.CurrentMain.main'] defs=[]
DEFS(68): structure CStarAlgebraNorm, structure TracialState, structure ClosedStarIdeal, abbrev CStarAlgebraNorm, def IsNuclear, abbrev TracialState, def RealRankZero, def traceTwoNorm, abbrev Pureness.ClosedStarIdeal, abbrev Quotient, def quotientMap, instance quotientStar, instance quotientStarRing, instance quotientStarModule, abbrev idealSubmodule, instance idealSubmodule_closed, def quotientLinearEquiv, instance quotientNormedAddCommGroup, instance quotientNormedSpace, def quotientNormEquiv, instance quotientCompleteSpace, class NormConstruction, instance quotientNormedRing, instance quotientNormedAlgebra, instance quotientNormedStarGroup, instance quotientCStarAlgebra, def CurrentMain.familyTwoNorm, instance CurrentMain.boundedFamilyProductCStar, def CurrentMain.IsFamilyNull, class CurrentMain.NullConstruction
## PAPER Tracial-projection-methods-and-uniform-property-Gamma-September-23-2026
ABSTRACT: For a simple, separable, unital, infinite-dimensional, nuclear, stably finite $C^*$-algebra with traces, real rank zero of the uniform tracial ultrapower of its uniform tracial completion implies uniform property $\Gamma$. This answers Problem XXI of Schafhauser, Tikuisis and White affirmatively. Independently, strict comparison implies Jiang--Su absorption for simple, separable, unital, infinite-dimensional nuclear algebras, resolving the unital Toms--Winter conjecture. Under comparison tested on traces of finite target rank, we also obtain uniform property $\Gamma$ and absorption for simple, separable, nuclear, stably projectionless algebras whose densely finite traces are all bounded and 
[theorem[Real rank zero and uniform property $\Gamma$]] \label{r:thm:main} Let $A$ be a unital, separable, simple, infinite-dimensional, nuclear, stably finite $C^*$-algebra with $T(A)\ne\varnothing$, and let $B=\overline A^{T(A)}$. Fix any free ultrafilter $\omega$ on $\N$. If $B^\omega$ has real rank zero in its quotient $C^*$-norm, then there is a projection $p\in B^\omega\cap B'$ such that \[ \lambda(px)=\tfrac12\lambda(x) \qquad(x\in B,\ \lambda\in\Lambda_\omega). \] In particular, $A$ has uniform property $\Gamma$.
==================
# FAMILY 292: Kirchberg's $`\mathcal O_2`$ norm-ultrapower embedding problem
SCOPE: Kirchberg's norm-ultrapower embedding problem asks whether separable $C^*$-algebras embed into norm ultrapowers of nuclear algebras. The formalization constructs an explicit separable unital full group $C^*$-algebra that has no unital embedding into $B^\omega$ for any nonzero unital nuclear $C^*$-algebra $B$ and any free ultrafilter $\omega$ on $\mathbb N$. In particular, it does not embed unitally into an ultrapower of the Cuntz algebra $\mathcal O_2$.
## CHALLENGE NuclearUltrapower  targets=['OAI.NuclearUltrapower.main_no_embedding'] defs=[]
theorem main_no_embedding : MainStatementWithCuntzCorollary.{0} := by
  sorry
end NuclearUltrapower
DEFS(24): abbrev Dyadic, abbrev Vector3, abbrev SL3Z, def dyadicTwo, def matrixAction, def dilationAction, def groupAction, abbrev G, abbrev BoundedSeq, def ultraRel, def ultraCon, abbrev NormUltrapower, def IsFree, structure ComplexHilbert, def spatialEval, def commutingEval, def minTensorNorm, def maxTensorNorm, def IsNuclear, structure UnitalCStar, def IsFullGroupAlgebra, def CuntzTwoRelations, def IsCuntzTwoAlgebra, def MainStatementWithCuntzCorollary
## PAPER An-explicit-obstruction-to-nuclear-norm-ultrapower-embeddings-September-23-2026
ABSTRACT: We give a negative answer to Kirchberg's norm-ultrapower embedding problem. We construct an explicit separable unital full group $C^*$-algebra that admits no unital embedding into $B^\omega$, for any nonzero unital nuclear $C^*$-algebra $B$ and any free ultrafilter $\omega$ on $\mathbb N$. In particular, it does not embed unitally into $\mathcal O_2^\omega$.
[theorem] \label{thm:main} Let \[ G=\Z[1/2]^3\rtimes\bigl(\SL_3(\Z)\times\Z\bigr), \qquad (M,k)\cdot v=2^kMv, \] and let $A=C^*(G)$ be its full group $C^*$-algebra. Then $A$ is separable and unital. For every nonzero unital nuclear $C^*$-algebra $B$ and every free ultrafilter $\omega$ on $\N$, there is no unital embedding \[ A\longrightarrow B^\omega. \] In particular, $A$ does not embed unitally into $\Otwo^\omega$.
==================
# FAMILY 293: Invariant projections, hyperinvariant subspaces, and transitive algebras
SCOPE: For every irrational rotation angle $\theta\in(0,1)$, the formalization constructs a continuous nonnegative circle weight with a single zero and logarithmic integral $-\infty$ whose weighted rotation is nonzero and quasinilpotent. In its associated hyperfinite type $\mathrm{II}_1$ factor, the operator has no nontrivial invariant projection: $(1-p)Tp=0$ forces $p=0$ or $p=1$. The linked statements also include an earlier existence construction, a product realization, and the selected product model's Brown measure $\delta_0$. The formalization for the companion paper [Backward intertwiners and a transitive commutant](../../preprints/Backward-intertwiners-and-a-transitive-commutant-September-27-2026/paper.pdf) gives, on every separable infinite-dimensional complex Hilbert space, a nonzero quasinilpotent operator whose commutant is transitive, proper, and closed in the strong operator topolo
## CHALLENGE FiniteFactor  targets=['OAI.FiniteFactor.main_theorem'] defs=[]
theorem main_theorem : MainTarget.{0} := by
  sorry
end FiniteFactor
DEFS(5): def HasScalarCenter, def IsFiniteAlgebra, def HasNoMinimalProjection, def HasSeparablePredual, def MainTarget
## CHALLENGE BackwardIntertwiners  targets=['OAI.BackwardIntertwiners.direct_algebra_corollary'] defs=[]
theorem direct_algebra_corollary (H : Type*) [NormedAddCommGroup H] [InnerProductSpace ℂ H]
    [CompleteSpace H] [TopologicalSpace.SeparableSpace H] (hInf : ¬FiniteDimensional ℂ H) :
    Hyperinvariant233.FullClaim (H:=H) := by
  sorry
end
end BackwardIntertwiners
DEFS(4): def commutant, def TransitiveCommutant, def strongOperatorTopology, def FullClaim
## CHALLENGE ContinuousCircleWeight  targets=['OAI.ContinuousCircleWeight.main_theorem'] defs=[]
theorem main_theorem : MainStatement := by
  sorry
end ContinuousCircleWeight
end
DEFS(10): abbrev CircleX, abbrev TracialHilbert, abbrev Operator, def circleIdentification, def circleFunction, def negativeLog, structure IsTracialRotation, def rotationAlgebra, def weightedRotation, def MainStatement
## CHALLENGE HyperinvariantSubspaces  targets=['OAI.Hyperinvariant.main_theorem'] defs=[]
theorem main_theorem (hInf : ¬FiniteDimensional ℂ H) : FullClaim (H := H) := by
  sorry
end Hyperinvariant
DEFS(4): def commutant, def TransitiveCommutant, def strongOperatorTopology, def FullClaim
## CHALLENGE IrrationalRotation  targets=['OAI.Invariant233.Results.prescribed_irrational_counterexample', 'OAI.Invariant233.Results.product_realization'] defs=[]
theorem prescribed_irrational_counterexample (θ : ℝ)
    (hθ0 : 0 < θ) (hθ1 : θ < 1) (hθ : Irrational θ) :
    ∃ f : C(Circle, ℝ), Rotation.IsContinuousCounterexample θ f := by
  sorry
theorem product_realization :
    ∃ θ c : ℕ → ℝ, ProductModel.IsCounterexampleRealization θ c := by
  sorry
end Invariant233.Results
DEFS(115): abbrev Circle, def circleMeasure, def negLogCost, def HasNegInfiniteLogIntegral, def scalarWeightDeterminant, def NormQuasinilpotent, def IsContinuousCircleWeight, abbrev Hilbert, abbrev Weight, def reindex, def shift, def diagonal, def diagonalAlgHom, def translate, def operator, def orbitProduct, def tailWeight, def tailProjection, def vonNeumannGenerated, theorem diagonal_value, theorem diagonal_bound, theorem diagonal_aestronglyMeasurable, def fieldDiagonalVec, theorem fieldDiagonalVec_ae, def fieldDiagonalLinear, def fieldDiagonal, instance circleMeasure_probability, abbrev Fiber, abbrev Hilbert, def action
## CHALLENGE ProductBrown  targets=['OAI.FiniteFactor.productBrown'] defs=[]
theorem productBrown : ProductBrownClaim := by
  sorry
end FiniteFactor
DEFS(64): theorem product_has_low_nonzero_coeff, abbrev Coefficients, def coefficientPolynomial, theorem coefficientPolynomial_coeff, def productCoefficient, theorem productCoefficient_eq, theorem continuous_productCoefficient, def lowCoefficients, theorem continuous_lowCoefficients, theorem lowCoefficients_ne_zero, def admissibleCoefficients, theorem isCompact_admissibleCoefficients, theorem uniform_product_coefficient_bound, def unitIntervalMeasure, def sourceKappa, def sourceNextCutoff, theorem sourceNextCutoff_large, theorem exists_source_block_length, structure SourceStageState, def SourceStageState.D, structure SourceStageChoice, theorem exists_sourceStageChoice, def selectedSourceStage, def SourceStageChoice.C, def SourceStageChoice.next, def sourceStageState, def sourceStage, def coordinateFloor, def coordinateRotate, def sourceLog
## CHALLENGE HyperinvariantSubspaces  targets=['OAI.Hyperinvariant.main_theorem'] defs=[]
theorem main_theorem (hInf : ¬FiniteDimensional ℂ H) : FullClaim (H := H) := by
  sorry
end Hyperinvariant
DEFS(4): def commutant, def TransitiveCommutant, def strongOperatorTopology, def FullClaim
## PAPER Invariant-projection-counterexamples-for-every-irrational-rotation-September-27-2026
ABSTRACT: For every irrational angle, we construct a continuous nonnegative circle weight with exactly one zero and logarithmic integral $-\infty$ whose weighted rotation has no nontrivial invariant projection in the associated hyperfinite type $\mathrm{II}_1$ factor. This answers negatively the question of Zhu, Fang, and Shi, with the angle prescribed in advance. The resulting operator is nonzero and norm-quasinilpotent.
[theorem] \label{thm:main} For every irrational $\theta\in(0,1)$ there exists a continuous function $f:\T\to[0,1]$ such that \[ f^{-1}(\{0\})=\{1\},\qquad \int_\T\log f\,dm=-\infty, \] and every projection $p\in R_\theta$ satisfying $(1-p)Uf(V)p=0$ is either $0$ or $1$.
## PAPER Backward-intertwiners-and-a-transitive-commutant-September-27-2026
ABSTRACT: We give a negative answer to the hyperinvariant-subspace problem by constructing, on every infinite-dimensional separable complex Hilbert space, a nonzero bounded norm-quasinilpotent operator with no nonzero proper closed hyperinvariant subspace. Its commutant is a proper strongly closed unital transitive complex operator algebra.
[theorem] \label{thm:direct-model} There are measurable positive weights $\beta_j:X\to(0,\infty)$, $j\in\Z$, and a contraction $V\in\B(H_0)$ with the following properties. The shifts \[ S_xe_j=\beta_j(x)e_{j+1},\qquad (Sf)(x)=S_xf(x), \] define a bounded operator $S$ on $H_0$, and: \begin{enumerate} \item For every $x\in X$, the closed invariant subspaces of $S_x$ are exactly $\Ktail{h}$, $h\in\Z\cup\{-\infty,+\infty\}$. \item The operator $S$ is nonzero, $\|S\|=e^{-10}$, and for every integer $n\ge1$, \begin{equation}\label{eq:main-power-bound} \|S^n\|\le \exp\left(-10\left\lfloor\frac{(n+1)^2}{4}\right\rfloor\right). \end{equation} \item The operator $V$ commutes with $S$ and has the form \[ (Vf)(\t
## PAPER Backward-intertwiners-and-a-transitive-commutant-September-27-2026
ABSTRACT: We give a negative answer to the hyperinvariant-subspace problem by constructing, on every infinite-dimensional separable complex Hilbert space, a nonzero bounded norm-quasinilpotent operator with no nonzero proper closed hyperinvariant subspace. Its commutant is a proper strongly closed unital transitive complex operator algebra.
[theorem] \label{thm:direct-model} There are measurable positive weights $\beta_j:X\to(0,\infty)$, $j\in\Z$, and a contraction $V\in\B(H_0)$ with the following properties. The shifts \[ S_xe_j=\beta_j(x)e_{j+1},\qquad (Sf)(x)=S_xf(x), \] define a bounded operator $S$ on $H_0$, and: \begin{enumerate} \item For every $x\in X$, the closed invariant subspaces of $S_x$ are exactly $\Ktail{h}$, $h\in\Z\cup\{-\infty,+\infty\}$. \item The operator $S$ is nonzero, $\|S\|=e^{-10}$, and for every integer $n\ge1$, \begin{equation}\label{eq:main-power-bound} \|S^n\|\le \exp\left(-10\left\lfloor\frac{(n+1)^2}{4}\right\rfloor\right). \end{equation} \item The operator $V$ commutes with $S$ and has the form \[ (Vf)(\t
==================
# FAMILY 294: Kaplansky's quasitrace conjecture and failure of tensor-product stable finiteness
SCOPE: Kaplansky's quasitrace conjecture predicts that every $2$-quasitrace on a $C^*$-algebra is a trace. The formalization constructs a separable $C^*$-algebra with normalized $2$-quasitraces and fixed positive contractions $a,b$ for which every such quasitrace satisfies $\mathrm{Re}(\tau(a+b)-\tau(a)-\tau(b))\ge1/144$. Thus none is additive on this pair. The formalization also gives simple stably finite $C^*$-algebras whose spatial tensor product is properly infinite, a separable stably finite algebra with no tracial state, and a tensor-product example in which normalized $2$-quasitraces are lost. These are the stable-finiteness consequences named in the paper's title.
## CHALLENGE KaplanskyQuasitrace  targets=['OAI.Kaplansky.kaplansky_quasitrace_counterexample'] defs=[]
theorem kaplansky_quasitrace_counterexample : MainTarget := by
  sorry
end Kaplansky
end
DEFS(6): structure OneQuasitrace, def OneQuasitrace.Normalized, def upperLeft, def OneQuasitrace.IsTwo, def PositiveContraction, def MainTarget
## CHALLENGE KaplanskyStableFiniteness  targets=['OAI.KaplanskyConsequences.stable_finiteness_bundle'] defs=[]
theorem stable_finiteness_bundle : StableFinitenessBundle := by
  sorry
end KaplanskyConsequences
end
DEFS(27): abbrev HilbertSum, lemma reindex_mem, def reindex, lemma reindex_apply, def left, lemma left_apply, lemma left_one, lemma left_mul, lemma left_star, def Algebra, def generator, abbrev F2, def diagonal, structure OneQuasitrace, def OneQuasitrace.Normalized, def ProperlyInfinite, def upperLeft, def OneQuasitrace.IsTwo, structure ClosedStarIdeal, def StablyFinite, structure TracialState, def TraceFreeStablyFinite, def tensorAlgebra, def ReducedQuasitraceLoss, def CStarSimple, def SimpleStableTensorCounterexample, def StableFinitenessBundle
## PAPER A-counterexample-to-Kaplanskys-quasitrace-conjecture-September-23-2026
ABSTRACT: We refute Kaplansky's quasitrace conjecture by constructing a separable unital complex \(C^*\)-algebra that admits normalized \(2\)-quasitraces but has no tracial state. As a consequence, we show that the minimal tensor product of two unital simple stably finite complex \(C^*\)-algebras can be properly infinite, even when one factor is the reduced free-group algebra \(C_r^*(\mathbb F_2)\).
[theorem] \label{thm:main} There exist a separable unital complex \(C^*\)-algebra \(A\), admitting a normalized \(2\)-quasitrace, and positive contractions \(a,b\in A\) such that every normalized \(2\)-quasitrace \(\tau\) on \(A\) satisfies \[ \tau(a+b)-\tau(a)-\tau(b)\ge\frac1{144}. \]
==================
# FAMILY 295: The Kadison–Ringrose cohomology conjecture
SCOPE: The formalization proves vanishing of bounded Hochschild cohomology in every degree at least two for a complex von Neumann algebra with coefficients in itself. Every bounded multilinear cocycle of such a degree is the Hochschild differential of a bounded multilinear cochain one degree lower. No separability or type restriction is imposed. The degree-one inner-derivation theorem is outside this selected statement.
## CHALLENGE KadisonRingrose  targets=['OAI.BoundedHochschild.KadisonRingrose.main_result'] defs=[]
theorem main_result
    {M : Type u} [CStarAlgebra M] [PartialOrder M] [StarOrderedRing M] [WStarAlgebra M]
    (n : ℕ) (f : Cochain M (n + 2))
    (hf : ∀ x : Fin (n + 3) → M, differentialValue f x = 0) :
    ∃ g : Cochain M (n + 1), ∀ x : Fin (n + 2) → M,
      differentialValue g x = f x := by
  sorry
end KadisonRingrose
end BoundedHochschild
end
DEFS(3): abbrev Cochain, def mergeInputs, def differentialValue
## PAPER Vanishing-of-higher-bounded-Hochschild-cohomology-September-23-2026
ABSTRACT: We prove that every bounded Hochschild cocycle of degree at least two on a complex von Neumann algebra, with values in the algebra itself, has a bounded primitive. Together with the established degree-one inner-derivation theorem, this resolves the Kadison--Ringrose cohomology conjecture positively.
[theorem] \label{thm:main} Let \(M\) be a complex von Neumann algebra and let \(k\geq2\). Every \(f\in C_b^k(M,M)\) satisfying \(df=0\) has the form \(f=dg\) for some \(g\in C_b^{k-1}(M,M)\). Consequently \(H_b^k(M,M)=0\).
==================
# FAMILY 296: The generator problem for finite factors
SCOPE: The formalization answers the generator problem affirmatively for type $\mathrm{II}_1$ factors with separable predual: one bounded operator generates the factor under adjoints and weak-operator closure. It imposes no separability assumption on the representing Hilbert space or on the operator-norm topology. It also proves the paper's relative-generation result. For an irreducible inclusion of type $\mathrm{II}_1$ factors with separable predual for the larger factor, the unitaries that generate the larger factor together with the smaller one form a dense $G_\delta$ set in the normalized trace two-norm topology. The normalized faithful normal trace is included in the assertion.
## CHALLENGE FactorGeneration  targets=['OAI.Generator.single_generation_of_II1_separable_predual'] defs=[]
theorem single_generation_of_II1_separable_predual
    (S : StarSubalgebra ℂ (H →L[ℂ] H)) (hS : IsII1Factor S)
    (hsep : HasSeparablePredual S) : SinglyGenerated S := by
  sorry
end Generator
end
DEFS(5): def WOTClosed, def wstar, structure IsII1Factor, def HasSeparablePredual, def SinglyGenerated
## CHALLENGE RelativeGeneration  targets=['OAI.RelativeGeneration.main_theorem'] defs=[]
theorem main_theorem : MainTarget.{level} := by
  sorry
end RelativeGeneration
end
DEFS(11): def WOTClosed, def wstar, structure IsII1Factor, def HasSeparablePredual, abbrev ultraweakTopology, abbrev algebraUltraweakTopology, structure IsNormalizedTrace, def traceDistance, abbrev traceTopology, def relativeGeneratorLocus, def MainTarget
## PAPER Relative-generation-and-the-generator-problem-for-finite-factors-September-23-2026
ABSTRACT: We prove that every type $\mathrm{II}_1$ factor with separable predual is generated by one operator, equivalently by two self-adjoint operators. Combined with the established direct-integral reduction to this case, this gives an affirmative solution of the generator problem for von Neumann algebras with separable predual.
[theorem] \label{thm:relative-generation} Let $P\subset M$ be an irreducible inclusion of type $\mathrm{II}_1$ factors, with $M$ of separable predual. The set \[ \{u\in\mathcal U(M):W^*(P,u)=M\} \] is a dense $G_\delta$ subset of the unitary group $\mathcal U(M)$ for the trace $2$-norm topology.
==================
# FAMILY 297: A ZFC counterexample to Naimark's problem
SCOPE: Naimark's problem asks whether a $C^*$-algebra whose nonzero irreducible representations are all unitarily equivalent must be an algebra of compact operators. The formalization gives a counterexample in ZFC: a unital infinite-dimensional simple complex $C^*$-algebra with a faithful tracial state has that uniqueness property for irreducible representations but is not isomorphic to the compact operators on any Hilbert space. No additional set-theoretic assumption is used.
## CHALLENGE Naimark  targets=['OAI.NaimarkZFC.main'] defs=[]
theorem main :
    ∃ (A : Type u) (_ : CStarAlgebra A),
      IsSimpleCStar A ∧ ¬ FiniteDimensional ℂ A ∧
      (∃ τ : A →L[ℂ] ℂ, IsFaithfulTracialState τ) ∧
      HasUniqueIrreducibleRepresentation.{u, v, w} A ∧
      ∀ (H : Type v) [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H],
        ¬ IsIsomorphicToCompacts A H := by
  sorry
end NaimarkZFC
end
DEFS(7): def IsSimpleCStar, def IsState, def IsFaithfulTracialState, def IsIrreducible, def UnitarilyEquivalent, def HasUniqueIrreducibleRepresentation, def IsIsomorphicToCompacts
## PAPER A-counterexample-to-Naimarks-problem-in-ZFC-September-24-2026
ABSTRACT: We construct in ZFC a unital infinite-dimensional simple complex $C^*$-algebra with a faithful tracial state whose nonzero irreducible representations are all unitarily equivalent. This gives a negative answer to Naimark's problem without additional set-theoretic assumptions.
[theorem] \label{na:main} There exists a unital infinite-dimensional simple complex $C^*$-algebra $A$ with a faithful tracial state such that all its nonzero irreducible representations are unitarily equivalent. In particular, $A$ is not isomorphic to $K(H)$ for any complex Hilbert space $H$.
==================
# FAMILY 298: Two notions of free entropy differ even when both are finite
SCOPE: The formalization disproves equality of microstates and nonmicrostates free entropy even when both quantities are finite. It constructs a bounded self-adjoint tuple $X$ in a von Neumann algebra with a faithful normal tracial state such that $-\infty<\chi(X)\le\chi^*(X)-1/2<\infty$. Here $\chi$ is the microstates entropy with an operator-norm cutoff and a limsup over matrix sizes, and $\chi^*$ is the nonmicrostates entropy defined using free semicircular noise. The example has a fixed finite number of variables.
## CHALLENGE FiniteEntropySeparation  targets=['OAI.FiniteEntropySeparation.main'] defs=[]
theorem main :
    ∃ (H : Type) (_ : NormedAddCommGroup H) (_ : InnerProductSpace ℂ H)
      (_ : CompleteSpace H) (M : VonNeumannAlgebra H) (τ : TracialVector M)
      (n : ℕ) (X S : Fin n → H →L[ℂ] H),
      2 ≤ n ∧
      (∀ i, X i ∈ M ∧ IsSelfAdjoint (X i)) ∧
      (∀ i, S i ∈ M ∧ IsSelfAdjoint (S i)) ∧
      FreeStandardNoise τ X S ∧
      (⊥ : EReal) < chi τ X ∧
      chi τ X ≤ chiStar τ X S - (1 / 2 : EReal) ∧
      chiStar τ X S - (1 / 2 : EReal) < (⊤ : EReal) := by
  sorry
end FiniteEntropySeparation
end
DEFS(19): structure TracialVector, def trace, def wordEval, def wordMoment, def FreeSubalgebras, def FreeStandardNoise, def polynomialL2, def derivativeMoment, def ConjugateSystem, def freeFisher, def heatTuple, def chiStar, abbrev MatrixCoordinates, def hermitianMatrix, def matrixOpNorm, def matrixMoment, def microstates, def chiCutoff, def chi
## PAPER A-finite-entropy-separation-of-microstates-and-nonmicrostates-free-entropy-September-25-2026
ABSTRACT: We answer the finite-entropy equality question for microstates and nonmicrostates free entropy negatively. We construct a bounded self-adjoint tuple $X$ in a von Neumann algebra with faithful normal tracial state such that $-\infty<\chi(X)\leq\chi^*(X)-\tfrac12<\infty$. Here $\chi$ is the original microstates entropy with an operator-norm cutoff and a limsup over matrix sizes. The counterexample uses a large but fixed number of variables.
[theorem] \label{thm:main} There exist an integer $n\geq2$ and a bounded self-adjoint tuple $X=(X_1,\ldots,X_n)$ in a von Neumann algebra with faithful normal tracial state such that \[ -\infty<\chi(X)\leq\chi^*(X)-\tfrac12<\infty. \] Here $\chi$ is the original microstates entropy using an operator-norm cutoff and a limsup over matrix sizes.
==================
# FAMILY 299: The Kirchberg–Rørdam character criterion and infinite tensor-power Jiang–Su stability
SCOPE: The Kirchberg–Rørdam criterion relates Jiang–Su absorption to characters of the central-sequence algebra. The formalized result proves that, for every nonzero unital separable complex $C^*$-algebra $A$ and every free ultrafilter on $\mathbb N$, the norm central-sequence algebra has no nonzero character exactly when $A\cong A\otimes_{\min}\mathcal Z$. No nuclearity, simplicity, trace, or comparison hypothesis is imposed.
## CHALLENGE CharacterCriterion  targets=['OAI.KirchbergRordam.character_criterion'] defs=[]
theorem character_criterion
    (A : Type) [CStarAlgebra A] [Nontrivial A] [TopologicalSpace.SeparableSpace A]
    (ω : Ultrafilter ℕ) (hω : (ω : Filter ℕ)≤Filter.cofinite) :
    OAI.KirchbergRordam.HasNoCharacters (NormUltrapower.CentralAlgebra A ω) ↔
      Nonempty (A ≃⋆ₐ[ℂ] MinTensor.Algebra A JiangSu.Algebra) := by sorry
end KirchbergRordam
end
DEFS(121): def normedRing, abbrev BoundedSeq, def normLimit, def nullIdeal, instance nullIdeal_twoSided, instance nullIdeal_closed, abbrev Algebra, instance quotientNormedRing, instance quotientNormedAlgebra, instance quotientStar, instance quotientStarRing, instance quotientStarModule, def cutRepresentative, instance quotientCStarRing, instance quotientCStarAlgebra, def quotientMap, def constantSeq, def diagonal, def centralSubalgebra, instance centralSubalgebra_closed, abbrev CentralAlgebra, instance centralSubringClass, instance centralCStarAlgebra, instance completionStar, instance completionContinuousStar, instance completionStarRing, instance completionNormedAlgebra, instance completionStarModule, structure System, def Raw
## PAPER The-Kirchberg-Rordam-character-criterion-September-25-2026
ABSTRACT: We prove the Kirchberg--R\o rdam character criterion: for every free ultrafilter on $\N$, a nonzero unital separable complex $C^*$-algebra absorbs the Jiang--Su algebra if and only if its norm central-sequence algebra has no characters. We also prove that the infinite minimal tensor power of every nonzero unital separable complex $C^*$-algebra without characters is $\Z$-stable and contains a unital copy of $\Z$.
[theorem] \label{thm:main} Let $A$ be a nonzero unital separable complex $C^*$-algebra, and let $\omega$ be any free ultrafilter on $\N$. Then \[ F_\omega(A)\text{ has no characters} \quad\Longleftrightarrow\quad A\cong A\otmin\Z. \]
==================
# FAMILY 301: Trace cones and Razak–Jacelon stabilization
SCOPE: The paper classifies separable nuclear complex $C^*$-algebras after tensoring with the Razak–Jacelon algebra and the compact operators, using their cones of extended lower-semicontinuous traces. The linked formalization proves the supporting ideal-transport result from Section 2: a trace-cone equivalence induces an order isomorphism of closed two-sided ideals, carrying the ideals determined by finiteness and vanishing of each trace to those of its image. Here a trace-cone equivalence preserves addition, zero, positive scalar multiplication, and canonical convergence in both directions. The finite ideal is the norm closure of $\{x : \tau(x^*x)<\infty\}$; the zero ideal is characterized on positive elements by $\tau(a)=0$. For each closed ideal $I$, it also constructs the trace that is zero on positive elements of $I$ and infinite elsewhere. These traces are exactly the additive idempotent
## CHALLENGE TraceIdealTransportSupport  targets=['OAI.TraceConeClassification.TraceConeEquiv.idealOrderIso_finIdeal', 'OAI.TraceConeClassification.TraceConeEquiv.idealOrderIso_zeroIdeal', 'OAI.TraceConeClassification.closed_ideal_weight_exists', 'OAI.TraceConeClassification.ExtendedTrace.zero_mem_finiteSquareSet', 'OAI.TraceConeClassification.ExtendedTrace.star_mem_finiteSquareSet', 'OAI.TraceConeClassification.ExtendedTrace.smul_mem_finiteSquareSet', 'OAI.TraceConeClassification.ExtendedTrace.add_mem_finiteSquareSet', 'OAI.TraceConeClassification.ExtendedTrace.mul_mem_finiteSquareSet_left', 'OAI.TraceConeClassification.ExtendedTrace.isClosed_finiteIdeal', 'OAI.TraceConeClassification.ExtendedTrace.mul_mem_finiteIdeal_left', 'OAI.TraceConeClassification.ExtendedTrace.mul_mem_finiteIdeal_right', 'OAI.TraceConeClassification.ExtendedTrace.lowerSemicontinuous_supportWeight', 'OAI.TraceConeClassification.ClosedIdeal.weight_idempotent', 'OAI.TraceConeClassification.ClosedIdeal.finiteIdeal_weight', 'OAI.TraceConeClassification.ClosedIdeal.le_iff_add_weight', 'OAI.TraceConeClassification.ExtendedTrace.idempotent_eq_weight', 'OAI.TraceConeClassification.closedIdealEquivOfAdditive_weight'] defs=[]
theorem closed_ideal_weight_exists
    (I : NonUnitalStarSubalgebra ℂ A) (hI : IsClosed (I : Set A))
    (hleft : ∀ (x y : A), y ∈ I → x * y ∈ I)
    (hright : ∀ (x y : A), x ∈ I → x * y ∈ I) :
    ∃ τ : ExtendedTrace A, ∀ a : Positive A, τ a = if a.1 ∈ I then 0 else ∞ := by
  sorry
namespace ExtendedTrace
lemma zero_mem_finiteSquareSet : (0 : A) ∈ τ.finiteSquareSet := by sorry
lemma star_mem_finiteSquareSet {x : A} (hx : x ∈ τ.finiteSquareSet) :
    star x ∈ τ.finiteSquareSet := by sorry
lemma smul_mem_finiteSquareSet (c : ℂ) {x : A} (hx : x ∈ τ.finiteSquareSet) :
    c • x ∈ τ.finiteSquareSet := by sorry
lemma add_mem_finiteSquareSet {x y : A}
    (hx : x ∈ τ.finiteSquareSet) (hy : y ∈ τ.finiteSquareSet) :
    x + y ∈ τ.finiteSquareSet := by sorry
lemma mul_mem_finiteSquareSet_left (x : A) {y : A} (hy : y ∈ τ.finiteSquareSet) :
    x * y ∈ τ.finiteSquareSet := by sorry
lemma isClosed_finiteIdeal : IsClosed (τ.finiteIdeal : Set A) := by sorry
lemma mul_mem_finiteIdeal_left (x : A) {y : A} (hy : y ∈ τ.finiteIdeal) :
    x * y ∈ τ.finiteIdeal := by sorry
lemma mul_mem_finiteIdeal_right {x : A} (hx : x ∈ τ.finiteIdeal) (y : A) :
    x * y ∈ τ.finiteIdeal := by sorry
end ExtendedTrace
end TraceConeClassification
namespace TraceConeClassification
universe u v
variable {A : Type u} [NonUnitalCStarAlgebra A] [PartialOrder A] [StarOrderedRing A]
lemma lowerSemicontinuous_supportWeight (τ : ExtendedTrace A) :
    LowerSemicontinuous (fun a : Positive A => if τ a = 0 then (0 : ℝ≥0∞) else ∞) := by sorry
theorem weight_idempotent (I : ClosedIdeal A) : I.weight.add I.weight = I.weight := by sorry
theorem finiteIdeal_weight (I : ClosedIdeal A) : I.weight.finiteIdeal = I.1 := by sorry
theorem le_iff_add_weight (I J : ClosedIdeal A) :
    I ≤ J ↔ I.weight.add J.weight = I.weight := by sorry
end ClosedIdeal
theorem idempotent_eq_weight {τ : ExtendedTrace A} (hτ : τ.add τ = τ) :
    τ.finIdeal.weight = τ := by sorry
lemma closedIdealEquivOfAdditive_weight (e : ExtendedTrace A ≃ ExtendedTrace B)
    (he : ∀ τ σ, e (τ.add σ) = (e τ).add (e σ)) (I : ClosedIdeal A) :
    (closedIdealEquivOfAdditive e he I).weight = e I.weight := by sorry
theorem idealOrderIso_finIdeal (τ : ExtendedTrace A) :
    F.idealOrderIso τ.finIdeal = (F.toEquiv τ).finIdeal := by
  sorry
theorem idealOrderIso_zeroIdeal (τ : ExtendedTrace A) :
    F.idealOrderIso τ.zeroIdeal = (F.toEquiv τ).zeroIdeal := by
  sorry
end TraceConeEquiv
end TraceConeClassification
end
DEFS(28): abbrev Positive, def zero, def add, def scale, def starMul, def mulStar, def cut, structure ExtendedTrace, def CanonicalConvergence, def scale, def finiteSquareSet, def finiteSquareAlgebra, def finiteIdeal, def add, def zero, def ClosedIdeal, def finIdeal, def supportWeight, def zeroIdeal, def weight, def IdempotentTrace, def closedIdealEquivIdempotent, def idempotentTraceEquiv, def closedIdealEquivOfAdditive, def closedIdealOrderEquivOfAdditive, def PreservesCanonicalConvergence, structure TraceConeEquiv, def idealOrderIso
## PAPER The-trace-cone-classifies-Razak-Jacelon-stabilizations-September-25-2026
ABSTRACT: We prove that the canonical topological cone of all extended lower-semicontinuous tracial weights determines a separable nuclear \(C^*\)-algebra after tensoring with the Razak--Jacelon algebra and the compact operators, answering Robert's trace-cone classification question positively. The isomorphism realizes the prescribed cone map, with arbitrary ideal structure and without a density assumption on the finite domains of the weights.
[theorem] \label{thm:main} Let \(A\) and \(B\) be separable nuclear complex \(C^*\)-algebras. If \(T(A)\) and \(T(B)\) are isomorphic as topological cones, then \[ A\otimes\W\otimes\K\ \cong\ B\otimes\W\otimes\K, \] where \(\K=\K(\ell^2(\N))\) and all tensor products are spatial.
==================
# FAMILY 303: Weak pure infiniteness and Cuntz-algebra absorption
SCOPE: The formalization proves that a complex $C^*$-algebra in which every positive element is properly infinite is strongly purely infinite, with the full positive-element diagonalization property. No exactness, nuclearity, unitality, or simplicity assumption is needed for this implication. For exact algebras, proper infiniteness of one fixed finite amplification of every positive element already implies individual proper infiniteness and strong pure infiniteness.
## CHALLENGE ExactInfiniteness  targets=['OAI.WeakPureInfiniteness.exact_weaklyPurelyInfinite_individuallyProperlyInfinite_any', 'OAI.WeakPureInfiniteness.exact_weaklyPurelyInfinite_stronglyPurelyInfinite'] defs=[]
theorem exact_weaklyPurelyInfinite_individuallyProperlyInfinite_any
    {A : Type u} [NonUnitalCStarAlgebra A] [PartialOrder A] [StarOrderedRing A]
    (hA : Exact A) (hW : WeaklyPurelyInfinite A) {a : A} (ha : 0 ≤ a) :
    ProperlyInfinite (diagonalCopies 1 a) := by
  sorry
theorem exact_weaklyPurelyInfinite_stronglyPurelyInfinite
    (A : Type u) [NonUnitalCStarAlgebra A] [PartialOrder A] [StarOrderedRing A]
    (hExact : Exact A) (hWeak : WeaklyPurelyInfinite A) : StronglyPurelyInfinite A := by
  sorry
end WeakPureInfiniteness
end
DEFS(23): lemma norm_completion_le, lemma norm_completion, structure ComplexHilbert, instance completedTensorCStar, instance hilbertOperatorsCStar, structure SpatialRepresentation, abbrev SpatialRepresentation.hilbert, abbrev SpatialRepresentation.space, def SpatialAmbient, instance spatialAmbientCStar, instance spatialAmbientCoeFun, def spatialElementary, def minimalTensorSubalgebra, abbrev MinimalTensor, def SpatialRepresentation.precompRight, def tensorKernelIdeal, def Exact, def CuntzSubequiv, def blockSum, def ProperlyInfinite, def diagonalCopies, def WeaklyPurelyInfinite, def StronglyPurelyInfinite
## CHALLENGE IndividualStrongInfiniteness  targets=['OAI.MainGap.Manuscript.individual_to_strong_main'] defs=[]
theorem individual_to_strong_main (hP : PropertyP A) :
    (∀ a b : A, 0 ≤ a → 0 ≤ b → ∀ c : A, ∀ ε : ℝ, 0 < ε →
      ∃ s t : A,
        ‖star s * a * s - a‖ < ε ∧
        ‖star t * b * t - b‖ < ε ∧
        ‖star s * c * t‖ < ε) ∧
    MainGap.StronglyPurelyInfinite A := by
  sorry
end MainGap.Manuscript
end
end
DEFS(35): def scalarCorner, def doubleCorner, def Diagonalization, def UnrestrictedDiagonalization, def StronglyPurelyInfinite, abbrev Mat, def pad, lemma pad_entry, lemma pad_apply, lemma sum_pad, lemma pad_mul, def padHom, lemma pad_injective, lemma norm_pad, lemma pad_self, lemma pad_pad, instance pad_directedSystem, abbrev Algebraic, lemma norm_mk, lemma normedCore, def cornerAlg, lemma cornerAlg_apply, lemma cornerAlg_isometry, abbrev Stabilization, lemma coe_mul_stable, lemma coe_star_stable, def stabilizationCStarAlgebra, def corner, lemma corner_apply, lemma norm_corner
## PAPER Weak-pure-infiniteness-and-O-infinity-absorption-September-25-2026
ABSTRACT: We prove that every complex \(C^*\)-algebra in which each positive element is properly infinite is strongly purely infinite. This answers the ordinary-to-strong part of Kirchberg--R{\o}rdam's comparison question. For exact algebras, we also prove that proper infiniteness of one fixed finite amplification of every positive element implies proper infiniteness of each positive element. Consequently, every separable nuclear algebra with this fixed-amplification property absorbs \(\Oinf\), without assumptions of unitality or simplicity.
[theorem] \label{thm:individual-to-strong} Let \(C\) be a complex \(C^*\)-algebra satisfying \(\propP\). For all \(a,b\in C_+\), \(c\in C\), and \(\varepsilon>0\), there are \(s,t\in C\) such that \begin{equation}\label{eq:main-diagonalization} \|s^*as-a\|<\varepsilon,\qquad \|t^*bt-b\|<\varepsilon,\qquad \|s^*ct\|<\varepsilon. \end{equation} Consequently \(C\) is strongly purely infinite.
==================
# FAMILY 307: Failure of rational injectivity for maximal coarse assembly
SCOPE: The coarse Novikov conjecture predicts rational injectivity of the ordinary coarse assembly map for uniformly discrete spaces of bounded geometry. The formalization constructs a counterexample from a coarse disjoint union of finite connected graphs with uniformly bounded degree. Its degree-one coarse $K$-homology contains an infinite-order class whose image under ordinary coarse assembly into the reduced locally compact Roe algebra vanishes. The class remains nonzero after tensoring with $\mathbb Q$, so rational injectivity fails.
## CHALLENGE CoarseAssembly  targets=['OAI.CoarseAssembly.bounded_geometry_graph_counterexample_unconditional'] defs=[]
theorem bounded_geometry_graph_counterexample_unconditional :
    (∀ j, Finite (FiberVertex j) ∧
      (fiberedGraph elementaryMoves chosenHolonomyUnit j).Connected) ∧
    (∃ D : ℕ, ∀ j (x : FiberVertex j),
      Nat.card {y // (fiberedGraph elementaryMoves chosenHolonomyUnit j).Adj x y} ≤ D) ∧
    ProperSpace VertexUnion ∧ UniformFiniteBalls VertexUnion ∧
      (∀ x y : VertexUnion, x ≠ y → 1 ≤ dist x y) ∧
      ∃ α : KX1 VertexUnion,
        (∀ n : ℤ, n ≠ 0 → n • α ≠ 0) ∧ constructedCoarseAssembly α = 0 ∧
        (1 : ℚ) ⊗ₜ[ℤ] α ≠ 0 ∧
        ¬ Function.Injective constructedCoarseAssembly ∧
        ¬ Function.Injective (constructedCoarseAssembly.toIntLinearMap.lTensor ℚ) := by
  sorry
end CoarseAssembly
end
end
DEFS(189): def blockLinear, def blockOperator, def blockIsometry, def flattenVector, def rowVector, def unflattenVector, def flattenEquiv, def operatorConjugation, def operatorConjugationHom, abbrev ArithmeticGroup, abbrev Quotient, def reduce, def diagonal, def holonomy, def residueMap, def quotientMap, def flattenOperator, def discreteGraphMetric, def connectedGraphMetric, def graphMetricOrDiscrete, def separatedDist, def separatedMetric, abbrev Module, abbrev Operator, def insert, def coordinate, def entry, def CompactEntries, def PropagationLE, def Generator
## PAPER A-counterexample-to-the-coarse-Novikov-conjecture-September-23-2026
ABSTRACT: We disprove the coarse Novikov conjecture: ordinary coarse assembly need not be rationally injective for uniformly discrete spaces of bounded geometry. We construct a coarse disjoint union of finite graphs of uniformly bounded degree and an infinite-order class in its degree-one coarse K-homology whose image under ordinary coarse assembly in the K-theory of the reduced, locally compact Roe algebra vanishes.
[theorem] \label{thm:main} There is a uniformly discrete bounded-geometry metric space $X$, which is a coarse disjoint union of finite connected graphs of uniformly bounded degree, and an infinite-order element $\alpha\in KX_1(X)$ such that \[ \mu_X(\alpha)=0\quad\text{in }K_1(C^*(X)). \] Consequently, ordinary coarse assembly for $X$ fails to be injective both integrally and after tensoring its domain and target with $\Q$.
==================
# FAMILY 312: The Grothendieck homotopy hypothesis
SCOPE: The Grothendieck homotopy hypothesis asks whether algebraic $\infty$-groupoids recover the homotopy theory of spaces. The formalized result is the elementary-expansion theorem used in this approach: for every Grothendieck coherator in the Ara–Henry convention and every boundary-cellular model, attaching an $(n+1)$-disk along its source $n$-face induces a weak equivalence. The later semi-model structure and full comparison with the homotopy theory of spaces are not included.
## CHALLENGE GrothendieckElementaryExpansion  targets=['OAI.Grothendieck.elementary_expansion'] defs=[]
theorem elementary_expansion (C : GlobularTheory.{v}) (hC : C.IsCoherator)
    (X : C.Model) (hX : X.IsCellular) (n : ℕ)
    (a : GlobularTheory.Model.disk C n ⟶ X)
    (Y : C.Model) (i : X ⟶ Y)
    (b : GlobularTheory.Model.disk C (n + 1) ⟶ Y)
    (square : IsPushout a (GlobularTheory.Model.J C n) i b) :
    GlobularTheory.Model.WeakEquivalence hC i := by
  sorry
end Grothendieck
DEFS(72): structure GlobularSet, structure Hom, def Parallel, def Joined, def Boundary, def boundary, def Hom.boundaryMap, structure Globe, inductive Face, def comp, def face, def source, def target, abbrev GlobularPresheaf, def underlying, def underlyingMap, def disk, def face, inductive Table, def height, def realizeWithLast, def realize, def lastInclusion, abbrev Shape, def realize, def height, def globe, def face, def source, def target
## PAPER The-Grothendieck-homotopy-hypothesis-via-elementary-expansions-September-24-2026
ABSTRACT: We prove the Grothendieck homotopy hypothesis for every Grothendieck coherator in the Ara--Henry convention: its weak globular infinity-groupoids recover the homotopy theory of spaces. We also resolve Henry's pushout conjecture, showing that elementary expansions preserve components and all homotopy groups of cellular infinity-groupoids.
[theorem] \label{thm:main} Fix any Grothendieck coherator \(\mathcal C\). Let \(X\) be a cellular \(\mathcal C\)-infinity-groupoid, let \(n\ge0\), and let \(a:D_n\to X\) be any cell. In the pushout square \[ \begin{tikzpicture}[baseline=(current bounding box.center), node distance=1.25cm and 2.2cm,>=Stealth] \node (a) {\(D_n\)}; \node (b) [right=of a] {\(D_{n+1}\)}; \node (c) [below=of a] {\(X\)}; \node (d) at (b |- c) {\(X^+\)}; \draw[->] (a) -- node[above] {\(s_n\)} (b); \draw[->] (a) -- node[left] {\(a\)} (c); \draw[->] (b) -- (d); \draw[->] (c) -- node[below] {\(i\)} (d); \end{tikzpicture} \] where \(s_n\) is the source inclusion, the map \(i:X\to X^+\) is a weak equivalence.
==================
# FAMILY 317: Thomason model structures in all strict higher dimensions
SCOPE: The formalization proves the higher-dimensional Thomason model-structure theorem for small strict globular $n$-categories in every positive finite dimension and in dimension $\omega$. Each category has the stated proper combinatorial model structure, Quillen equivalent to simplicial sets through the twice-subdivided categorification and twice-extended Street nerve adjunction. The selected statements also identify weak equivalences by the Street nerve in all these dimensions. Thus the constructions model the homotopy theory of spaces throughout the stated range.
## CHALLENGE ThomasonModelStructures  targets=['OAI.Thomason.main', 'OAI.Thomason.nerveDetection_allDimensions'] defs=[]
DEFS(109): structure OmegaCategory, structure Functor, def id, def comp, def IsTruncated, def NCategory, structure DirectedComplex, structure Hom, def id, def comp, structure Table, def truncate, def comp, def nu, def table, def nu, def nuFunctor, abbrev Word, abbrev Chains, def bracket, def prepend, def wordBoundary, def boundary, def faces, def grade, def emptyWord, def emptyCoefficient, def Positive, def positiveGrade, def complex
## PAPER Thomason-Model-Structures-in-Every-Strict-Higher-Dimension-September-25-2026
ABSTRACT: We prove the higher-dimensional Thomason model-structure conjecture of Ara and Maltsiniotis. For every $1\le n\le\infty$, the category of small strict globular $n$-categories admits a proper combinatorial model structure that is Quillen equivalent to simplicial sets. Its weak equivalences and fibrations are detected by the twice-extended Street nerve $\Ex^2N_n$, and the Quillen equivalence is given by $c_n\Sd^2\dashv\Ex^2N_n$. Thus strict higher categories model the homotopy theory of spaces in every positive finite dimension and in dimension $\omega$.
[theorem] \label{thm:main} For every $n\in\{1,2,3,\ldots\}\cup\{\infty\}$, the classes $(C_n,W_n,F_n)$ in \eqref{eq:prescribed-classes} form a proper combinatorial model structure on $\nCat$. It is cofibrantly generated by $(L_nI,L_nJ)$, where \[ I=\{\partial\Delta[m]\hookrightarrow\Delta[m]:m\ge0\},\qquad J=\{\Lambda^k[m]\hookrightarrow\Delta[m]:m\ge1,\ 0\le k\le m\}. \] Moreover, \[ L_n:\sSet_{\KQ}\rightleftarrows(\nCat,C_n,W_n,F_n):R_n \] is a Quillen equivalence.
==================
# FAMILY 322: Tingley’s sphere-isometry problem
SCOPE: Tingley's problem asks whether a surjective isometry between the unit spheres of Banach spaces extends to a linear isometry of the spaces. The formalized result gives a unique surjective real-linear isometric extension for arbitrary nonzero real Banach spaces, with no finite-dimensionality, separability, reflexivity, or convexity assumptions. For complex spaces viewed as real spaces, the conclusion is real linearity rather than complex linearity.
## CHALLENGE TingleySphereIsometry  targets=['OAI.Tingley.tingley_sphere_isometry_full'] defs=[]
theorem tingley_sphere_isometry_full
    {X : Type u} {Y : Type v}
    [NormedAddCommGroup X] [NormedSpace ℝ X] [CompleteSpace X]
    [NormedAddCommGroup Y] [NormedSpace ℝ Y] [CompleteSpace Y]
    [Nontrivial X] [Nontrivial Y]
    (f : UnitSphere X → UnitSphere Y) (hf : Isometry f) (hs : Function.Surjective f) :
    ∃ T : X ≃ₗᵢ[ℝ] Y,
      (∀ u : UnitSphere X, T (u : X) = (f u : Y)) ∧
      T 0 = 0 ∧
      (∀ x : X, ∀ hx : x ≠ 0, T x = ‖x‖ • (f (normalize x hx) : Y)) ∧
      Function.Surjective T ∧
      (∀ L : X →ₗ[ℝ] Y, (∀ u : UnitSphere X, L (u : X) = (f u : Y)) →
        L = T.toLinearEquiv.toLinearMap) := by
  sorry
end Tingley
end
DEFS(2): abbrev UnitSphere, def normalize
## PAPER A-positive-solution-to-Tingleys-problem-September-23-2026
ABSTRACT: Every surjective isometry between the unit spheres of real Banach spaces extends uniquely to a surjective real-linear isometry, giving an affirmative solution to Tingley's problem. If distances between different radii are not preserved, we realize the positive maximal defect in a possibly enlarged pair of Banach spaces. We then align extremal chords using common supports and Darbo's fixed-point theorem and obtain a contradiction from support and convexity estimates.
[theorem] \label{thm:main} Let $X,Y$ be nonzero real Banach spaces and let $f:S_X\to S_Y$ be a surjective isometry. Then \[ T(0)=0,\qquad T(x)=\norm{x}f\left(\frac{x}{\norm{x}}\right)\quad(x\ne0) \] is a surjective real-linear isometry. It is the unique linear extension of $f$.
==================
# FAMILY 323: Independence of the separable quotient problem
SCOPE: The separable quotient problem asks whether every infinite-dimensional Banach space has an infinite-dimensional separable quotient. The linked formalization proves the negative direction under the continuum hypothesis: over both the real and complex fields, there is an infinite-dimensional Banach space admitting no bounded linear surjection onto an infinite-dimensional separable Banach space. This is the conditional counterexample direction. The positive consistency direction and the paper's full relative-independence conclusions are outside the selected statement.
## CHALLENGE SeparableQuotientNegative  targets=['OAI.SeparableQuotient.negative_main'] defs=[]
theorem negative_main (hCH : CH) : ¬ SQ.{u} ℝ ∧ ¬ SQ.{u} ℂ := by
  sorry
end SeparableQuotient
DEFS(3): def CH, def HasSeparableQuotient, def SQ
## PAPER Relative-independence-of-the-separable-quotient-problem-September-23-2026
ABSTRACT: The separable quotient problem asks whether every infinite-dimensional Banach space has a separable infinite-dimensional quotient. We prove that this statement is independent of ZFC, relative to the consistency of ZFC with a measurable cardinal. This holds over both the real and complex fields. For spaces of norm density $\aleph_1$, we obtain independence relative to the consistency of ZFC alone.
[theorem] \label{intro:main} For each $\mathbb F\in\{\R,\C\}$, ZFC proves the following implications. \begin{enumerate}[label=\textup{(\roman*)}] \item If $\mathfrak c$ is real-valued measurable, then $\SQ_{\mathbb F}$ holds. \item If the continuum hypothesis holds, then $\SQ_{\mathbb F}$ fails. \end{enumerate} Consequently, if ZFC with a measurable cardinal is consistent, then $\SQ_{\mathbb F}$ is independent of ZFC. Consistency of its failure requires only consistency of ZFC.
==================
# FAMILY 324: Lipschitz equivalent Banach spaces need not be linearly isomorphic
SCOPE: The formalized counterexample gives separable real Banach spaces $X,Y$ that are bi-Lipschitz equivalent but not linearly isomorphic. The bijection has lower Lipschitz bound $4/21$ and upper bound $76/25$. The linear obstruction is explicit: $X$ contains a linear isometric copy of $c_0(\ell_2)$, whereas $Y$ contains no bounded linear copy of that space. The formalized result constructs one separable real Banach space $X$ that is bi-Lipschitz equivalent to $X\times c_0$ but contains no closed linear subspace isomorphic to $c_0$. The same space contains a bi-Lipschitz copy of $c_0$, is bi-Lipschitz universal for separable metric spaces, and is not linearly isomorphic to $X\times c_0$. Thus nonlinear absorption of $c_0$ does not force a linear copy of it.
## CHALLENGE LipschitzEquivalence  targets=['OAI.LipschitzCounterexample.main'] defs=[]
theorem main : MainClaim := by
  sorry
end LipschitzCounterexample
end
DEFS(5): abbrev RealL2, abbrev C0L2, structure SeparableRealBanach, def ContainsLinearCopy, def MainClaim
## CHALLENGE C0Absorption  targets=['OAI.C0Absorption.main_result'] defs=[]
theorem main_result : MainConclusion := by sorry
end C0Absorption
DEFS(5): abbrev C0, def BiLip, def NoLinearC0, def MetricUniversal, def MainConclusion
## PAPER Lipschitz-Equivalent-Separable-Banach-Spaces-Need-Not-Be-Linearly-Isomorphic-September-24-2026
ABSTRACT: There are separable real Banach spaces that are globally bi-Lipschitz equivalent but not linearly isomorphic. This gives a negative answer to the separable Banach-space Lipschitz-isomorphism problem.
[theorem] \label{thm:main} There are separable real Banach spaces \(X,Y\) and a bijection \(\Psi:X\to Y\) such that, for every \(s,t\in X\), \begin{equation} \label{eq:main-bounds} \frac4{21}\|s-t\|_X \le \|\Psi(s)-\Psi(t)\|_Y \le \frac{76}{25}\|s-t\|_X. \end{equation} The space \(X\) contains a linearly isometric copy of \(c_0(\ell_2)\), while \(Y\) contains no closed subspace linearly isomorphic to \(c_0(\ell_2)\). In particular, \(X\) and \(Y\) are not linearly isomorphic.
## PAPER Bi-Lipschitz-Absorption-of-c0-Without-a-Linear-Copy-of-c0-September-26-2026
ABSTRACT: We construct a separable real Banach space \(Z\) that contains no linear copy of \(c_0\), yet is bi-Lipschitz equivalent to \(Z\oplus_\infty c_0\). The same space contains a bi-Lipschitz image of every separable metric space.
[theorem] \label{thm:main} There is a separable real Banach space \(Z\) containing no closed linear subspace isomorphic to \(c_0\), and an onto bi-Lipschitz map \[ F:Z\oplus_\infty c_0\longrightarrow Z. \]
==================
# FAMILY 325: The complete Crouzeix conjecture
SCOPE: The complete Crouzeix inequality bounds a matrix-valued polynomial evaluated at a matrix by its maximum norm on the numerical range. The formalized result proves the bound with constant $2$ for every positive matrix and coefficient size, every polynomial degree, and arbitrary complex coefficients. It also proves that no smaller universal constant works. Normality of the matrix and nonempty interior of its numerical range are not assumed. The formalization proves the complete Crouzeix inequality with sharp constant two for every bounded operator on an arbitrary complex Hilbert space. For every matrix-valued polynomial, its operator evaluation has norm at most twice its supremum norm on the numerical range. The same bound holds for finite matrix-valued functions holomorphic near the closure of the numerical range and for rational functions with poles outside that closure. No separability a
## CHALLENGE DirectCrouzeix  targets=['OAI.DirectCrouzeix.complete_crouzeix', 'OAI.DirectCrouzeix.uniform_sharpness'] defs=[]
theorem complete_crouzeix : UniversalBound 2 := by
  sorry
theorem uniform_sharpness (c : ℝ) (hc : UniversalBound c) : 2 ≤ c := by
  sorry
end DirectCrouzeix
end
DEFS(5): def numericalRange, def polynomialValue, def tensorEvaluation, def rangeMaximum, def UniversalBound
## CHALLENGE CompleteCrouzeix  targets=['OAI.CompleteCrouzeix.main'] defs=[]
theorem main : UniversalBound 2 ∧ ∀ C : ℝ, UniversalBound C → 2 ≤ C := by
  sorry
end CompleteCrouzeix
end
DEFS(5): def numericalRange, def polynomialValue, def polynomialAt, def rangeMaximum, def UniversalBound
## CHALLENGE StructuralCrouzeix  targets=['OAI.StructuralCrouzeixReference.challenge'] defs=[]
theorem challenge : StructuralCrouzeix.FullEndpoint ∧
    StructuralCrouzeix.IsAdmissible (Metric.ball (0 : ℂ) 1) := by
  sorry
end StructuralCrouzeixReference
DEFS(18): def numericalRange, structure DiskCoordinate, def exteriorMap, structure ExteriorCoordinate, def scalarJetEval, def primaryEquiv, def primaryNilpotent, def primaryEval, def matrixAnalyticEval, def completeAnalyticEval, def MetricFeasible, def RegularAnalyticBoundaryAt, structure IsAdmissible, def IsMinimizing, def StrictlyFeasible, def analyticSupNorm, def boundaryPoint, def FullEndpoint
## CHALLENGE CrouzeixHilbert  targets=['OAI.CrouzeixHilbert.hilbert'] defs=[]
theorem hilbert (H : Type u) [NormedAddCommGroup H] [InnerProductSpace ℂ H]
    [CompleteSpace H] (A : Operator H) :
    (Nontrivial H → NonzeroConclusion A) ∧
    (Subsingleton H → ZeroConclusion A) ∧ SharpConstant := by
  sorry
end CrouzeixHilbert
end
DEFS(24): abbrev Operator, abbrev Coeff, def numericalRange, def numericalClosure, def supNorm, abbrev Amplification, def tensorOperator, def matrixPolynomial, def polynomialEval, structure SmoothContour, def SmoothContour.index, structure CalculusContour, def contourEval, def holomorphicEval, def matrixHolomorphicEval, def EntrywiseHolomorphic, abbrev RationalMatrix, def PolesOutside, def matrixRationalFunction, def rationalEval, def matrixRationalEval, def NonzeroConclusion, def ZeroConclusion, def SharpConstant
## CHALLENGE HilbertCrouzeix  targets=['OAI.HilbertCrouzeix.numericalClosure_geometry', 'OAI.HilbertCrouzeix.exists_finite_compression', 'OAI.HilbertCrouzeix.rational_denominator_isUnit', 'OAI.HilbertCrouzeix.zeroConclusion'] defs=[]
theorem numericalClosure_geometry (A : H →L[ℂ] H) :
    IsCompact (numericalClosure A) ∧ Convex ℝ (numericalClosure A) ∧
      spectrum ℂ A ⊆ numericalClosure A := by
  sorry
omit [CompleteSpace H] in
theorem exists_finite_compression {m d : ℕ} (A : H →L[ℂ] H)
    (B : Fin (d + 1) → Coeff m) (ξ : H ⊗[ℂ] CoeffSpace m) :
    ∃ (E : Submodule ℂ H) (hE : FiniteDimensional ℂ E),
      letI : FiniteDimensional ℂ E := hE
      ∃ η : Amplification E m,
        tensorInclusion E m η = (↑ξ : Amplification H m) ∧
        tensorInclusion E m (polynomialEval (compression A E) B η) =
          polynomialEval A B (↑ξ) := by
  sorry
theorem rational_denominator_isUnit [Nontrivial H] (A : H →L[ℂ] H)
    {m : ℕ} (R : RationalMatrix m) (hR : numericalClosure A ⊆ poleFreeSet R)
    (i j : Fin m) : IsUnit (Polynomial.aeval A (R i j).denom) := by
  sorry
theorem zeroConclusion [Subsingleton H] (A : H →L[ℂ] H) : ZeroConclusion A := by
  sorry
end HilbertCrouzeix
end
DEFS(26): abbrev Coeff, abbrev CoeffSpace, def numericalRange, def numericalClosure, abbrev Amplification, def tensorOp, def matrixPolynomial, def polynomialEval, def normSup, def contourIntegral, def contourIndex, def IsCauchyContour, def chosenContour, def dunfordIntegral, def holomorphicCalculus, def matrixUnit, def holomorphicEval, abbrev RationalMatrix, def poleFreeSet, def rationalFunction, def rationalCalculus, def rationalEval, def ZeroConclusion, def compression, def completedIsometry, def tensorInclusion
## PAPER A-direct-proof-of-the-complete-Crouzeix-inequality-September-26-2026
ABSTRACT: We give a direct proof of the sharp constant-two numerical-range inequality for matrix-valued polynomials in all finite base and coefficient dimensions. This resolves the complete Crouzeix conjecture in its matrix formulation, including matrices whose numerical ranges are points or line segments.
[theorem] \label{thm:main} For every pair of positive integers $n,m$, every $A\in M_n(\C)$, every nonnegative integer $d$, and every polynomial $P(z)=\sum_{k=0}^d B_kz^k$ with $B_k\in M_m(\C)$, \begin{equation}\label{eq:main} \|P[A]\|\le2\max_{z\in W(A)}\|P(z)\|. \end{equation} The constant two cannot be decreased uniformly over $n,m$, and $d$.
## PAPER The-complete-Crouzeix-theorem-September-23-2026
ABSTRACT: We resolve the complete Crouzeix conjecture by proving the sharp constant-two numerical-range inequality for every bounded operator on a complex Hilbert space and every matrix-valued polynomial. No separability assumption is needed. The closure of the numerical range is a complete $2$-spectral set, and the bound extends to finite matrix-valued functions holomorphic near that closure. For a finite matrix and a bounded convex domain containing its numerical range with regular real-analytic Jordan boundary, the optimal similarity making its conformal disk image contractive is attained with condition number at most two. For the similar matrix, one continuous positive boundary density of mass the
[theorem[The optimal metric]] \label{thm:structural} For every admissible $\Omega$, every finite $n\ge1$, every $A\in M_n(\C)$ with $W(A)\subset\Omega$, and the interior conformal coordinate $f$ above, the problem \eqref{eq:minimum} is strictly feasible and has an attained minimum $1\le\kappa^2\le4$. If $H$ is a minimizing metric, then \[ S=H^{1/2},\qquad A'=SAS^{-1},\qquad D=Sf(A)S^{-1}=f(A') \] satisfy \[ D^*D\preceq I,\qquad \rho(D)<1, \qquad \|S\|\|S^{-1}\|=\kappa\le2. \]
==================
# FAMILY 326: The cotype–cotype conjecture under the approximation property
SCOPE: The cotype–cotype problem asks whether finite cotype of a Banach space and its dual characterizes $K$-convexity. The formalized result establishes this equivalence for every nonzero real Banach space with the approximation property: $X$ is $K$-convex exactly when both $X$ and $X^*$ have finite cotype.
## CHALLENGE Cotype  targets=['OAI.Cotype.mainTarget_proved'] defs=[]
theorem mainTarget_proved [Nontrivial X] : MainTarget X := by
  sorry
end Cotype
end
DEFS(12): abbrev Cube, def sign, def average, def cubeL2, def rademacherSum, def moment, def radProjection, def KConvex, def HasCotype, def FiniteCotype, def ApproximationProperty, def MainTarget
## PAPER The-cotype-cotype-conjecture-under-the-approximation-property-September-23-2026
ABSTRACT: We prove the cotype--cotype conjecture under the ordinary approximation property. A nonzero real Banach space with this property is \(K\)-convex if and only if both the space and its dual have finite Rademacher cotype, possibly with different exponents.
[theorem] \label{thm:main} Let \(X\) be a nonzero real Banach space with the ordinary approximation property. Then \(X\) is \(K\)-convex if and only if \[ C_q(X)<\infty \quad\hbox{and}\quad C_r(X^*)<\infty \qquad\text{for some }q,r\in[2,\infty). \] The exponents \(q\) and \(r\) may differ. The forward implication holds for every real Banach space, without an approximation hypothesis.
==================
# FAMILY 327: Markov type characterizes superreflexivity
SCOPE: The formalized result proves that a real Banach space has nontrivial Markov type exactly when it admits an equivalent uniformly convex norm, hence exactly when it is superreflexive. Nontrivial Markov type means a uniform Markov-type bound for some exponent $p>1$ over all finite stationary reversible chains and all positive times. The exponent and equivalent norm may depend on the space, and the zero space is included. Additional formalized consequences concern uniformly smooth renormings and reflexivity of finitely representable spaces.
## CHALLENGE MarkovType  targets=['OAI.MarkovSuperreflexivity.hasNontrivialMarkovType_iff_hasEquivalentUCNorm'] defs=[]
theorem hasNontrivialMarkovType_iff_hasEquivalentUCNorm [CompleteSpace X] :
    HasNontrivialMarkovType X ↔ HasEquivalentUCNorm X := by
  sorry
end MarkovSuperreflexivity
end
DEFS(10): structure FiniteReversibleChain, abbrev StatePath, def pathWeight, def stateCost, def MarkovTypeWith, def HasMarkovType, def HasNontrivialMarkovType, structure EquivalentNorm, def UniformConvex, def HasEquivalentUCNorm
## PAPER Nontrivial-Markov-Type-Forces-Superreflexivity-September-23-2026
ABSTRACT: We prove that every real Banach space with Markov type $p>1$ is superreflexive. Together with the known converse, this characterizes superreflexivity by nontrivial Markov type. This answers Naor's question: every real Banach space with nontrivial Markov type admits an equivalent uniformly smooth norm.
[theorem] \label{thm:main} Every real Banach space with Markov type $p$ for at least one $p>1$ is superreflexive.
==================
# FAMILY 328: Nonexpansive fixed points in reflexive Banach spaces
SCOPE: The fixed-point question asks whether reflexivity suffices for nonexpansive maps on bounded convex sets. The formalized result gives an affirmative answer: every nonexpansive self-map of a nonempty closed bounded convex subset of a real reflexive Banach space has a fixed point in the original norm. Zero and nonseparable spaces are included, with no uniform convexity, normal structure, or weak-continuity assumption.
## CHALLENGE ReflexiveFixedPoints  targets=['OAI.ReflexiveFixedPoints.exists_fixedPoint_of_canonicallyReflexive'] defs=[]
theorem exists_fixedPoint_of_canonicallyReflexive
    {X : Type u} [NormedAddCommGroup X] [NormedSpace ℝ X] [CompleteSpace X]
    (hX : CanonicallyReflexive X) (C : Set X)
    (hne : C.Nonempty) (hclosed : IsClosed C)
    (hbounded : Bornology.IsBounded C) (hconvex : Convex ℝ C)
    (F : C → C)
    (hF : ∀ a b : C, ‖(F a : X) - (F b : X)‖ ≤ ‖(a : X) - (b : X)‖) :
    ∃ a : C, F a = a := by
  sorry
end ReflexiveFixedPoints
end
DEFS(1): def CanonicallyReflexive
## PAPER Fixed-Points-of-Nonexpansive-Maps-in-Reflexive-Banach-Spaces-September-24-2026
ABSTRACT: Every nonexpansive selfmap of a nonempty closed bounded convex subset of a real reflexive Banach space has a fixed point. This resolves the reflexive-space fixed point problem for the given norm.
[theorem] \label{thm:main} Let $X$ be a real reflexive Banach space, and let $C\subseteq X$ be nonempty, norm closed, bounded, and convex. If $F:C\to C$ satisfies \[ \norm{F(a)-F(b)}\le \norm{a-b}\qquad(a,b\in C), \] then $F$ has a fixed point.
==================
# FAMILY 329: A counterexample to metric-entropy duality
SCOPE: Metric-entropy duality predicts a universal comparison between covering numbers of convex bodies and their polars. The formalized result disproves such a comparison: for every $a,b\ge1$, there is an origin-symmetric convex body $K$ in a positive finite dimension with $\log N(K,B_\infty)>b\log N(B_\infty^\circ,a^{-1}K^\circ)$, where $N$ is the least number of translates in a finite cover. A further construction makes the dual-to-primal logarithmic entropy ratio tend to zero as the dimension grows.
## CHALLENGE MetricEntropyDuality  targets=['OAI.MetricEntropyDuality.exists_entropy_duality_counterexample_with_covers'] defs=[]
theorem exists_entropy_duality_counterexample_with_covers
    (a b : ℝ) (ha : 1 ≤ a) (hb : 1 ≤ b) :
    ∃ n : ℕ, 0 < n ∧ ∃ K : Set (RealSpace (Fin n)),
      IsSymmetricConvexBody K ∧
      Coverable K (cube (Fin n)) ∧
      Coverable (polar (cube (Fin n))) (a⁻¹ • polar K) ∧
      b * Real.log (coveringNumber (polar (cube (Fin n))) (a⁻¹ • polar K) : ℝ) <
        Real.log (coveringNumber K (cube (Fin n)) : ℝ) := by
  sorry
end MetricEntropyDuality
end
DEFS(8): abbrev RealSpace, def pairing, def cube, def polar, def Covers, def Coverable, def coveringNumber, structure IsSymmetricConvexBody
## PAPER Counterexamples-to-the-duality-conjecture-for-metric-entropy-September-24-2026
ABSTRACT: We disprove Pietsch's dimension-free duality conjecture for metric entropy. For every proposed pair of universal constants, we construct origin-symmetric convex bodies that violate the corresponding covering-entropy inequality, already when the covering body is a cube.
[theorem] \label{thm:main} For every $a,b\ge1$, there are a positive integer $n$ and an origin-symmetric convex body $K\subset\R^n$ such that, with $L=[-1,1]^n$, \[ \log N(K,L)>b\log N(L^\circ,a^{-1}K^\circ). \]
==================
# FAMILY 330: A uniformly discrete counterexample to bounded approximation in Lipschitz-free spaces
SCOPE: Kalton's question asks whether uniform discreteness of a metric space forces its Lipschitz-free space to have the bounded approximation property. The formalization constructs a countable metric space with all distinct points at distance at least one whose real Lipschitz-free space has the approximation property but fails every bounded approximation bound. The metric space is unbounded and not proper. The earlier quantitative renorming result for real $\ell_1$ is retained: for each integer $p\ge1$, an equivalent complete norm has the $2B_p$-bounded approximation property but fails the $p$-bounded approximation property, where $B_p=300p^2+150p+5$.
## CHALLENGE RealL1Renorming  targets=['OAI.DiscreteFree.real_l1_quantitative_renorming'] defs=[]
theorem real_l1_quantitative_renorming : RealL1RenormingStatement := by
  sorry
end DiscreteFree
end
DEFS(4): def HasBAP, def blockBound, def RealL1, def RealL1RenormingStatement
## CHALLENGE DiscreteLipschitzFree  targets=['OAI.DiscreteFree.source_endpoints'] defs=[]
theorem source_endpoints : BlockStatement ∧ MainStatement := by
  sorry
end DiscreteFree
end
DEFS(12): def lipSubmodule, def Lip0, def slope, def evaluation, def freeSubmodule, def FreeSpace, def delta, def HasAP, def HasBAP, def blockBound, def BlockStatement, def MainStatement
## PAPER Failure-of-Bounded-Approximation-in-a-Lipschitz-Free-Space-over-a-Uniformly-Discrete-Metric-Space-September-26-2026
==================
# FAMILY 331: Reflexive midpoint convexity and diamond distortion
SCOPE: The paper constructs a Banach space whose midpoint geometry is asymptotically uniformly convex even though no equivalent norm is asymptotically uniformly convex in the usual one-sided sense. The formalization proves that the full dual of the specified segment-norm completion is infinite-dimensional, separable, and reflexive; its averaged midpoint modulus is at least $\sqrt{1+t^2/12}-1$ for every $t>0$, while every equivalent norm fails asymptotic uniform convexity. It also proves that an embedding of a depth-$k$ countably branching diamond has distortion at least $\sqrt{1+k/12}$. The general-forest and word-forest results use the closed span of the coordinate functionals. Their conclusions retain the finite-ancestor and equivalent-norm hypotheses, including the scale $\alpha/(2\beta)$ when $0<\alpha\le\beta$ and the new norm lies between $\alpha$ and $\beta$ times the original norm; they
## CHALLENGE ForestSpace  targets=['OAI.ForestSpace.main_theorem'] defs=[]
theorem main_theorem :
    (¬FiniteDimensional ℝ (FullDual Vertex)) ∧
    TopologicalSpace.SeparableSpace (FullDual Vertex) ∧
    Reflexive (FullDual Vertex) ∧
    (∀ (α β : ℝ) (R : EquivalentNorm (FullDual Vertex) α β), ¬IsAUC R.N) ∧
    (∀ t : ℝ, 0 < t →
      Real.sqrt (1+t^2/12)-1 ≤ averageModulus (FullDual Vertex) norm t) ∧
    (∀ (k : ℕ) (f : (Diamond.diamond k).V → FullDual Vertex) (C : ℝ),
      Diamond.EmbeddingBound k f C → Real.sqrt (1+(k:ℝ)/12) ≤ C) := by
  sorry
end ForestSpace
end
DEFS(35): def Cofinite, def aucValues, def aucInner, def aucCenter, def aucModulus, def averageValues, def averageInner, def averageCenter, def averageModulus, structure EquivalentNorm, def Reflexive, def IsAUC, def IsSegment, def segSum, def TestBound, def testValues, def squareSup, def rho, def l1size, def segmentSeminorm, def TestVector, def toFinsupp, abbrev J, abbrev FullDual, instance fullDualAddCommGroup, structure Word, structure Vertex, structure Network, def graph, def refine
## CHALLENGE MidpointLenses  targets=['OAI.SegmentLenses.midpoint_lens_main'] defs=[]
theorem midpoint_lens_main :
    (∀ (H : Finset ForestVertex) (_ : Ancestral ForestAncestor H)
      (x y : X) (_ : x = head H x) (R : ℝ) (_ : 0 ≤ R)
      (_ : ‖x + y‖ ≤ R) (_ : ‖x - y‖ ≤ R),
      ‖tail H y‖ ≤ 2 * Real.sqrt (R ^ 2 - ‖x‖ ^ 2)) ∧
    (∀ (H : Finset InfiniteVertex) (_ : Ancestral List.IsPrefix H)
      (x y : BInfinite) (_ : x.val = head H x.val) (R : ℝ) (_ : 0 ≤ R)
      (_ : ‖x + y‖ ≤ R) (_ : ‖x - y‖ ≤ R),
      ‖tail H y.val‖ ≤ 2 * Real.sqrt (R ^ 2 - ‖x‖ ^ 2)) :=
  sorry
end SegmentLenses
end
DEFS(30): abbrev InfiniteVertex, def ForestVertex, def ForestAncestor, def IsInterval, def Ancestral, class SegmentSystem, structure SegmentFamily, def column, def test, def seminorm, def singleton, def segmentSeminorm, def Test, def coeff, def ofFinsupp, def evaluation, abbrev Primal, abbrev FullDual, def unitVector, def coordinate, def coordinateSpan, abbrev CoordinatePredual, def head, def tail, instance infiniteSegments, instance forestSegments, abbrev J, abbrev X, abbrev JInfinite, abbrev BInfinite
## CHALLENGE DiamondDistortion  targets=['OAI.DiamondDistortion.headline_all_pairs'] defs=[]
theorem headline_all_pairs :
    (∀ (k : ℕ) (f : Diamond.Vertex k → ForestDual) (D s : ℝ),
      0 < s → (∀ u v,s*Diamond.distance k u v ≤ ‖f u-f v‖ ∧
        ‖f u-f v‖ ≤ D*s*Diamond.distance k u v) → 1+(k:ℝ)/4 ≤ D^2) ∧
    (∀ (k : ℕ) (f : Diamond.Vertex k → InfinitePredual) (D s : ℝ),
      0 < s → (∀ u v,s*Diamond.distance k u v ≤ ‖f u-f v‖ ∧
        ‖f u-f v‖ ≤ D*s*Diamond.distance k u v) → 1+(k:ℝ)/4 ≤ D^2) := by
  sorry
end DiamondDistortion
end
DEFS(31): structure SegmentSystem, structure Family, def Family.test, def Family.seminorm, def primalSeminorm, def singletonFamily, def Primal, abbrev JamesSpace, abbrev Dual, def coordinateFinite, def coordinate, def unitFinite, def unitVector, def headDual, def CoordinatePredual, def intervalSystem, class Ancestry, def segments, def ForestNode, def ForestAncestor, def forestAncestry, def forestSegments, def infiniteAncestry, def infiniteSegments, abbrev ForestDual, abbrev InfinitePredual, def Edge, def Vertex, def endpoint, def graph
## CHALLENGE DaugavetModuli  targets=['OAI.ExactModuli.exact_main', 'OAI.ExactModuli.kadets_werner_existence', 'OAI.ExactModuli.exact_example'] defs=[]
theorem exact_main {Ω : Type u_1} [MeasurableSpace Ω] (μ : Measure Ω)
    [IsProbabilityMeasure μ] (E : Submodule ℝ (Lp ℝ 1 μ))
    (_hclosed : IsClosed (E : Set (Lp ℝ 1 μ))) (hdim : ¬ FiniteDimensional ℝ E)
    (hprecompact : MeasurePrecompactBall μ E) (hdaugavet : Daugavet E) :
    (∀ (x : E), ‖x‖ = 1 → ∀ t : ℝ, 0 < t →
      H (normSeminorm ℝ E) x t = max (t / 2) (t - 1) ∧
      D (normSeminorm ℝ E) x t = max 0 (t - 2)) ∧
    (∀ t : ℝ, 0 < t →
      averagedModulus (normSeminorm ℝ E) t = max (t / 2) (t - 1) ∧
      oneSidedModulus (normSeminorm ℝ E) t = max 0 (t - 2)) ∧
    (∀ N : Seminorm ℝ E, EquivalentNorm N → ¬ AUC N) := by
  sorry
theorem kadets_werner_existence :
    ∃ E : Submodule ℝ (Lp ℝ 1 kwMeasure),
      IsClosed (E : Set (Lp ℝ 1 kwMeasure)) ∧ (¬ FiniteDimensional ℝ E) ∧
      MeasurePrecompactBall kwMeasure E ∧ UnitSliceProperty E ∧ Daugavet E := by
  sorry
theorem exact_example :
    ∃ E : Submodule ℝ (Lp ℝ 1 kwMeasure),
      IsClosed (E : Set (Lp ℝ 1 kwMeasure)) ∧ (¬ FiniteDimensional ℝ E) ∧
      MeasurePrecompactBall kwMeasure E ∧ UnitSliceProperty E ∧ Daugavet E ∧
      (∀ (x : E), ‖x‖ = 1 → ∀ t : ℝ, 0 < t →
        H (normSeminorm ℝ E) x t = max (t / 2) (t - 1) ∧
        D (normSeminorm ℝ E) x t = max 0 (t - 2)) ∧
      (∀ t : ℝ, 0 < t →
        averagedModulus (normSeminorm ℝ E) t = max (t / 2) (t - 1) ∧
        oneSidedModulus (normSeminorm ℝ E) t = max 0 (t - 2)) ∧
      (∀ N : Seminorm ℝ E, EquivalentNorm N → ¬ AUC N) := by
  sorry
end ExactModuli
end
DEFS(14): def Cofinite, def averagedIncrement, def H, def D, def averagedModulus, def oneSidedModulus, def EquivalentNorm, def AUC, def Daugavet, def measureDistance, def MeasurePrecompactBall, def UnitSliceProperty, abbrev KWOmega, def kwMeasure
## CHALLENGE BoundedTreePotentials  targets=['OAI.BoundedTreePotentials.TreeCalculus.main_counterexample'] defs=[]
DEFS(21): structure TestFamily, def finitePairing, def testNorm, def testSeminorm, def TestVector, abbrev TestCompletion, abbrev Node, def potential, inductive QuadraticKind, def QuadraticGroup, def QuadraticBudget, def CoefficientSupport, structure IsTreeTest, abbrev TreeCoordinate, def liftCoefficients, def treeTestFamily, structure ClosedFiniteCodim, def averagedModulusReal, def oneSidedModulusReal, def IsAUCReal, theorem TreeCalculus.main_counterexample
## CHALLENGE IndependentProducts  targets=['OAI.IndependentProducts.main_general', 'OAI.IndependentProducts.main_exponential', 'OAI.IndependentProducts.main_gaussian_24', 'OAI.IndependentProducts.main_gaussian_12'] defs=[]
theorem main_general (μ : Measure ℝ) (hμ : MultiplierHypotheses μ) :
    ¬ FiniteDimensional ℝ (productSpan μ) ∧
    ∀ N : Seminorm ℝ (productSpan μ),
      IsEquivalentNorm (productSpan μ) N → ¬ IsAUC (productSpan μ) N := by
  sorry
theorem main_exponential (t : ℝ) (ht : 0 < t) :
    (7 * t / 30) * excessConstant (10 / t) ≤
      averagedMidpointModulus (productSpan exponentialLaw)
        (normSeminorm ℝ (productSpan exponentialLaw)) t ∧
    0 < (7 * t / 30) * excessConstant (10 / t) := by
  sorry
theorem main_gaussian_24 (t : ℝ) (ht : 0 < t) :
    gaussianTail (4 * Real.sqrt 2 * (2 + Real.sqrt 2) / t) / 8 ≤
      averagedMidpointModulus (productSpan gaussianSquareLaw)
        (normSeminorm ℝ (productSpan gaussianSquareLaw)) t ∧
    0 < gaussianTail (4 * Real.sqrt 2 * (2 + Real.sqrt 2) / t) / 8 := by
  sorry
theorem main_gaussian_12 (t : ℝ) (ht : 0 < t) :
    gaussianTail (8 * Real.sqrt 6 / t) / 4 ≤
      averagedMidpointModulus (productSpan gaussianSquareLaw)
        (normSeminorm ℝ (productSpan gaussianSquareLaw)) t ∧
    0 < gaussianTail (8 * Real.sqrt 6 / t) / 4 := by
  sorry
end IndependentProducts
end
DEFS(17): abbrev Vertex, abbrev Edge, abbrev Sample, def productMeasure, def pathPrefix, def pathProduct, def productSpan, structure MultiplierHypotheses, def CofiniteSubspaces, def averagedMidpointModulus, def oneSidedModulus, def IsEquivalentNorm, def IsAUC, def gaussianTail, def excessConstant, def exponentialLaw, def gaussianSquareLaw
## CHALLENGE RecursivePotentials  targets=['OAI.ComparatorModel.RecursivePotentials.main'] defs=[]
theorem main : MainClaim := by
  sorry
end RecursivePotentials
end ComparatorModel
end
DEFS(141): def leastPair, structure FiniteRootedTree, def children, def maxDepth, def fields, def Initial, def ancestors, def ancestorClosure, def restrict, def extend, def head, def projectHead, structure CofiniteSubspace, def averagedGain, def averagedInner, def averagedModulus, def sequenceTree, abbrev ComponentNode, abbrev JoinedNode, def joinedTree, def WeaklyNull, structure EquivalentNorm, def inner, def modulus, def AUC, def IsReflexive, abbrev Space, def completionEquivOfDense, def componentTree, def logarithmicGamma
## PAPER Asymptotic-midpoint-uniform-convexity-and-unbounded-diamond-distortion-in-a-reflexive-tree-space-September-27-2026
## PAPER Midpoint-lenses-in-segment-spaces-September-27-2026
## PAPER Diamond-distortion-from-midpoint-and-tree-energies-September-27-2026
## PAPER Exact-asymptotic-moduli-in-a-Daugavet-subspace-of-L1-September-27-2026
ABSTRACT: For an infinite-dimensional real subspace of $L^1$ whose unit ball is totally bounded in measure and whose norm has the Daugavet property, we compute the averaged midpoint and one-sided asymptotic moduli at every unit center. They are $\max\{t/2,t-1\}$ and $\max\{0,t-2\}$, respectively. The same weak-neighborhood geometry excludes every equivalent asymptotically uniformly convex norm. A quantitative realization of the Kadets--Werner construction supplies a space with both hypotheses.
[theorem] \label{thm:exact} Let $E$ be an infinite-dimensional closed real subspace of $L^1(\Omega,\mathbb P)$, where $\mathbb P$ is a probability measure. Suppose its closed unit ball is totally bounded for convergence in measure and its inherited norm has the Daugavet property. Then every $x\in S_E$ and $t>0$ satisfy \[ H_E(x,t)=\max\{t/2,t-1\},\qquad D_E(x,t)=\max\{0,t-2\}. \] Consequently these are also the formulas for $\widehat\delta_E(t)$ and $\overline\delta_E(t)$. The space $E$ admits no equivalent AUC norm.
## PAPER Midpoint-convexity-from-bounded-tree-potentials-and-path-costs-September-27-2026
ABSTRACT: Four real Banach spaces defined by bounded tree potentials satisfy the averaged asymptotic midpoint bound $\widehat\delta(t)\ge\sqrt{1+t^2/4}-1$ for $0<t<1$, while none admits an asymptotically uniformly convex (AUC) renorming. On finite-height trees, the globally constrained norm equals the least additive cost of a Hilbert vector and root paths. The quadratic path and segment-start outer Hilbert sums are reflexive and asymptotically midpoint uniformly convex, and admit no equivalent AUC norm.
[theorem] \label{thm:four} Each of the four completed spaces $X_K$ is a separable infinite-dimensional real Banach space. For $K\in\{K_{\rm s},K_{\rm p},K_{\rm a},K_{\rm g}\}$ and $0<t<1$, \begin{equation}\label{eq:common-bound} \widehat\delta_{X_K}(t)\ge\sqrt{1+t^2/4}-1. \end{equation} None of these spaces admits an equivalent AUC norm.
## PAPER Independent-products-in-real-L1-asymptotic-midpoint-convexity-without-AUC-renormings-September-27-2026
ABSTRACT: For a countably branching tree, the closed real $L^1$ spans of products of independent exponential or Gaussian-square multipliers along its paths have positive averaged asymptotic midpoint moduli and admit no equivalent asymptotically uniformly convex norm. The renorming obstruction holds for every positive nonconstant mean-one multiplier with finite second moment.
[theorem] \label{thm:main} For every multiplier $W$ as above, the Banach space $X_W$ is infinite dimensional and has no equivalent AUC norm. For the exponential and Gaussian-square laws, the inherited norms satisfy \begin{align} \whdelta_{X_{\mathrm{exp}}}(t) &\ge \frac{7t}{30}c(10/t)>0 &&(t>0),\label{eq:main-exp}\\ \whdelta_{X_{\mathrm{sq}}}(t) &\ge\frac{\PP\bigl(|G|\ge4\sqrt2(2+\sqrt2)/t\bigr)}{8}>0 &&(t>0),\label{eq:main-sq24}\\ \whdelta_{X_{\mathrm{sq}}}(t) &\ge\frac{\PP\bigl(|G|\ge8\sqrt6/t\bigr)}{4}>0 &&(t>0).\label{eq:main-sq12} \end{align}
## PAPER Midpoint-convexity-from-two-recursive-potentials-September-27-2026
ABSTRACT: We study tree norms computed by two least nonnegative fields whose difference is the vector. For Euclidean child aggregation, two root-sum spaces have an averaged asymptotic midpoint modulus of at least $t^3/128$ for $0<t<1$, including a reflexive joining-root space. A reflexive construction with a fixed zero root also satisfies a homogeneous cubic estimate. These spaces admit no equivalent asymptotically uniformly convex norm. We also obtain sixth-power and cubic estimates when the aggregation exponent depends on the height of a finite component.
[theorem] \label{rec:main}\label{rec:joined-root-stability} For $N=N_\Sigma$ on $X_\Sigma$, or $N=N_J$ on $X_J$, one has \begin{equation}\label{rec:sum-modulus} \widehat\delta_N(t)\ge t^3/128\qquad(0<t<1). \end{equation} For $X_0$, a finite initial set $H$, a vector $x$ supported in $H$, and $z\in F_H\setminus\{0\}$, one has \begin{equation}\label{rec:equal-estimate} \frac{N_0(x+z)+N_0(x-z)}2\ge N_0(x) +\frac{N_0(z)^3}{8(2N_0(x)+N_0(z))^2}. \end{equation} Each of $X_\Sigma,X_0,X_J$ admits no equivalent AUC norm.
==================
# FAMILY 333: Smooth isometric immersions of surfaces into ℝ<sup>4</sup>
SCOPE: The formalization proves that every closed smooth Riemannian surface admits a smooth isometric immersion into $\mathbb R^4$. The differential preserves the Riemannian inner product on every tangent space. No orientability assumption is imposed, and the statement asks for an immersion rather than an embedding.
## CHALLENGE SurfaceImmersion  targets=['OAI.ClosedSurfaceR4.FiniteOrderSmoothing.smooth_isometric_immersion'] defs=[]
theorem smooth_isometric_immersion (g : SmoothMetric M) :
    ∃ F : M → Space, IsSmoothIsometricImmersion M g F := by
  sorry
end FiniteOrderSmoothing
end ClosedSurfaceR4
end
DEFS(6): abbrev Plane, abbrev Space, abbrev planeModel, abbrev spaceModel, abbrev SmoothMetric, def IsSmoothIsometricImmersion
## PAPER Smooth-isometric-immersions-of-closed-surfaces-into-Euclidean-four-space-September-23-2026
ABSTRACT: Every closed smooth Riemannian surface admits a smooth isometric immersion into Euclidean four-space, without an orientability assumption. This resolves the closed-surface form of the classical four-dimensional isometric-immersion problem.
[theorem] \label{thm:main} Every closed smooth Riemannian surface $(M,g)$ admits a $C^\infty$ isometric immersion into $(\R^4,\delta_4)$, where $\delta_4=\sum_{i=1}^4 dx_i^2$.
==================
# FAMILY 334: A smooth surface metric with no local isometric immersion in ℝ<sup>3</sup>
SCOPE: The local isometric-immersion problem asks whether every smooth surface metric can be realized locally in Euclidean three-space. The formalized counterexample is a smooth positive-definite metric on $(-1,1)^2$ for which no neighborhood of the origin admits a smooth isometric immersion into $\mathbb R^3$. The obstruction applies to every smooth candidate map on every such neighborhood.
## CHALLENGE IsometricImmersion  targets=['OAI.SmoothLocal.Geometry.exists_local_metric_without_local_immersion'] defs=[]
theorem exists_local_metric_without_local_immersion :
    ∃ g : coordinateSquareOpen → Matrix (Fin 2) (Fin 2) ℝ,
      LocalSmoothPositive coordinateSquareOpen g ∧
      ∀ U : Opens Coord, ∀ hUS : (U : Set Coord) ⊆ square,
        (0 : Coord) ∈ U → ∀ F : U → Ambient,
          ¬ (ContMDiff 𝓘(ℝ, Coord) 𝓘(ℝ, Ambient) ∞ F ∧
            ∀ p : U, ∀ v w : Coord,
              (inner ℝ : Ambient → Ambient → ℝ) (mfderiv 𝓘(ℝ, Coord) 𝓘(ℝ, Ambient) F p v)
                (mfderiv 𝓘(ℝ, Coord) 𝓘(ℝ, Ambient) F p w) =
                  v ⬝ᵥ (g ⟨p, hUS p.property⟩ *ᵥ w)) := by
  sorry
end SmoothLocal.Geometry
end
DEFS(6): abbrev Coord, abbrev Ambient, def square, def LocalSmoothPositive, theorem coordinate_square_isOpen, def coordinateSquareOpen
## PAPER A-Smooth-Metric-with-No-Local-Isometric-Immersion-into-Three-Space-September-24-2026
ABSTRACT: We construct a smooth positive-definite Riemannian metric on \((-1,1)^2\) that agrees with the Euclidean metric to every order at the origin, yet no neighborhood of the origin admits a smooth isometric immersion into Euclidean three-space. This gives a negative answer to the unrestricted smooth local isometric realization problem for surfaces.
[maintheorem] There is a \(C^\infty\) positive definite Riemannian metric \(g\) on \((-1,1)^2\) such that no open neighborhood \(U\) of the origin admits a \(C^\infty\) isometric immersion \[ F:(U,g)\longrightarrow\R^3. \] In particular, no such neighborhood admits a smooth isometric embedding.
==================
# FAMILY 337: Sharp Cartan–Hadamard isoperimetry and rigidity
SCOPE: The formalization proves the sharp Euclidean filling inequality for every compactly supported integral $n$-cycle in a proper $\mathrm{CAT}(0)$ space, for $n\ge2$. It constructs a compactly supported integral filling whose mass is at most $C_n$ times the boundary mass to the power $(n+1)/n$, where $C_n$ is the Euclidean isoperimetric coefficient. Integer multiplicities and the ambient dimension are unrestricted. A second statement proves that this coefficient is optimal by giving, in Euclidean space, a cycle for which every compactly supported integral filling has at least that mass. This yields the selected integral-current form of the Cartan–Hadamard isoperimetric conjecture.
## CHALLENGE FillingCoefficient  targets=['OAI.SharpIntegralFillings.coefficient_optimal'] defs=[]
theorem coefficient_optimal (n : ℕ) (hn : 2 ≤ n) :
    ∃ T : IntegralCurrent (Euc (n + 1)) n,
      CompactlySupported T.val ∧ IsCycle T.val ∧ 0 < mass T.val ∧
      ∀ S : IntegralCurrent (Euc (n + 1)) (n + 1),
        CompactlySupported S.val → boundarySucc S.val = T.val →
        fillingCoefficient n * (mass T.val) ^ fillingPower n ≤ mass S.val := by
  sorry
end SharpIntegralFillings
DEFS(23): abbrev Euc, abbrev Functional, def BoundedLip, def Admissible, def Controls, def mass, structure IsMetricCurrent, def boundarySucc, def boundary, structure IntegerChart, def scalar, def jacobian, def action, def image, def IntegerRectifiable, def IsIntegral, abbrev IntegralCurrent, def CompactlySupported, def IsCycle, def omega, def sphereArea, def fillingCoefficient, def fillingPower
## CHALLENGE SharpCAT0Filling  targets=['OAI.CAT0Fillings.sharp_integral_filling'] defs=[]
theorem sharp_integral_filling
    (X : Type u) [MetricSpace X] [MeasurableSpace X] [BorelSpace X] [ProperSpace X]
    (hX : IsCAT0 X) (n : ℕ) (hn : 2 ≤ n) (T : IntegralCurrent X n)
    (hTc : CompactlySupported T.val) (hTz : IsCycle T.val) :
    ∃ S : IntegralCurrent X (n + 1), CompactlySupported S.val ∧
      boundarySucc S.val = T.val ∧
      mass S.val ≤ fillingCoefficient n * (mass T.val) ^ fillingPower n := by
  sorry
end CAT0Fillings
DEFS(24): abbrev Euc, abbrev Functional, def BoundedLip, def Admissible, def Controls, def mass, structure IsMetricCurrent, def boundarySucc, def boundary, structure IntegerChart, def scalar, def jacobian, def action, def image, def IntegerRectifiable, def IsIntegral, abbrev IntegralCurrent, def CompactlySupported, def IsCycle, def IsCAT0, def omega, def sphereArea, def fillingCoefficient, def fillingPower
==================
# FAMILY 342: Donaldson's tamed-to-compatible conjecture
SCOPE: Donaldson's tamed-to-compatible conjecture asks whether an almost-complex structure tamed by a symplectic form also admits a compatible symplectic form. The formalized result establishes this for every closed connected smooth four-manifold, keeping the almost-complex structure fixed. No integrability assumption or prescribed cohomology class for the compatible form is required.
## CHALLENGE TamingCompatibility  targets=['OAI.TamingCompatibility.taming_implies_compatibility'] defs=[]
theorem taming_implies_compatibility
    [T2Space X] [SecondCountableTopology X] [CompactSpace X] [ConnectedSpace X]
    (J : AlmostComplexStructure X)
    (h : ∃ α : TwoForm X, IsSymplectic α ∧ Tames α J) :
    ∃ η : TwoForm X, IsSymplectic η ∧ Compatible η J := by
  sorry
end TamingCompatibility
end
DEFS(13): abbrev Space, abbrev Model, abbrev TwoForm, structure AlmostComplexStructure, def eval, def pullback, def IsSmooth, def IsClosed, def IsNondegenerate, def IsSymplectic, def Tames, def IsInvariant, def Compatible
## PAPER Taming-implies-compatibility-on-four-manifolds-September-23-2026
ABSTRACT: We prove that every smooth almost complex structure on a closed four-manifold which is tamed by a symplectic form is compatible with a symplectic form. This gives a positive solution to Donaldson's tamed-to-compatible conjecture.
[theorem] \label{thm:main} Suppose that a smooth almost complex structure \(J\) on a closed connected smooth real four-manifold \(X\) is tamed by a symplectic form. Then there is a smooth symplectic form compatible with \(J\).
==================
# FAMILY 343: Symplectic ball packing in higher dimensions
SCOPE: The formalization proves Siegel and Yao's ball-packing criterion in every symplectic dimension $2n$ with $n\ge3$. For $k\ge1$ closed standard balls of positive capacities $R_1,\ldots,R_k$, disjoint symplectic embeddings into the interior of a ball of capacity $R$ exist exactly when $\sum_i R_i^n<R^n$ and $R_i+R_j<R$ for all $i\ne j$. Capacity is $\pi$ times squared Euclidean radius, and each embedding is defined on a neighborhood of its closed source ball. The linked statements include both the full equivalence and the necessity direction.
## CHALLENGE BallPacking  targets=['OAI.HigherDimensionalBallPacking.main_theorem'] defs=[]
theorem main_theorem (n k : ℕ) (hn : 3 ≤ n) (hk : 1 ≤ k)
    (R : ℝ) (r : Fin k → ℝ) (hR : 0 < R) (hr : ∀ i, 0 < r i) :
    HasPacking n k R r ↔ PackingInequalities n k R r := by
  sorry
end HigherDimensionalBallPacking
DEFS(8): abbrev Phase, def capacity, def closedBall, def openBall, def standardForm, def SymplecticOn, def HasPacking, def PackingInequalities
## CHALLENGE BallPackingNecessity  targets=['OAI.HigherDimensionalBallPacking.packing_necessity'] defs=[]
theorem packing_necessity (n k : ℕ) (hn : 3 ≤ n) (hk : 1 ≤ k)
    (R : ℝ) (r : Fin k → ℝ) (hR : 0 < R) (hr : ∀ i, 0 < r i)
    (hp : HasPacking n k R r) : PackingInequalities n k R r := by
  sorry
end HigherDimensionalBallPacking
DEFS(8): abbrev Phase, def capacity, def closedBall, def openBall, def standardForm, def SymplecticOn, def HasPacking, def PackingInequalities
## PAPER Symplectic-Ball-Packings-in-Higher-Dimensions-September-23-2026
ABSTRACT: We prove that, for all integers \(n\ge3\) and \(k\ge1\) and all positive real capacities \(R_1,\ldots,R_k\), the closed standard symplectic \(2n\)-balls of these capacities embed disjointly into the interior of a ball of capacity \(R>0\) if and only if \[ \sum_{i=1}^k R_i^n<R^n, \qquad R_i+R_j<R\quad(i\ne j). \] Capacity is \(\pi\) times the squared Euclidean radius, and each embedding is defined on a neighborhood of its closed source ball. This proves Siegel and Yao's Conjecture~A.
[theorem] \label{intro:main} Let \(n\ge3\) and \(k\ge1\) be integers. For positive real numbers \(R,R_1,\ldots,R_k\), there exists a symplectic embedding \[ \bigsqcup_{i=1}^k B^{2n}(R_i) \hookrightarrow \Int B^{2n}(R) \] if and only if \begin{equation}\label{intro:inequalities} \sum_{i=1}^k R_i^n<R^n, \qquad R_i+R_j<R\quad (1\le i<j\le k). \end{equation}
==================
# FAMILY 347: Counterexamples to stable-Morse and strong Arnold fixed-point bounds
SCOPE: The critical-number form of Arnold's fixed-point conjecture predicts at least as many fixed points as the minimum number of critical points of a smooth function. The formalized counterexample is a Hamiltonian diffeomorphism of the complex quadric threefold with exactly three fixed points, while every smooth function on that manifold has at least four critical points. At least one fixed point is degenerate. The separate nondegenerate Morse-number construction is not included.
## CHALLENGE ArnoldCounterexample  targets=['OAI.ArnoldCounterexample.main'] defs=[]
theorem main :
    ∃ φ : Q3 ≃ Q3, IsHamiltonian φ ∧ (fixedSet φ).encard = 3 ∧
      (3 : ℕ∞) < 4 ∧ 4 ≤ criticalNumber ∧ HasDegenerateFixedPoint φ := by
  sorry
end ArnoldCounterexample
end
DEFS(19): abbrev CV, def quadricPolynomial, def normSquared, def IsUnitQuadric, abbrev UnitQuadric, def Q3, def project, def Horizontal, def omega, def LocalFunctionLift, def IsSmoothFunction, structure SmoothFunction, def IsCritical, def criticalSet, def criticalNumber, structure HamiltonianPath, def IsHamiltonian, def fixedSet, def HasDegenerateFixedPoint
## PAPER A-degenerate-counterexample-to-the-critical-number-Arnold-bound-September-23-2026
ABSTRACT: We construct a smooth Hamiltonian diffeomorphism of the complex quadric threefold with exactly three fixed points, at least one of which is degenerate. The critical number and the unit-inclusive rational cup length of this manifold are both four. Thus the example disproves the unrestricted critical-number and rational cup-length forms of the Arnold conjecture.
[theorem] \label{thm:counterexample} There is a smooth Hamiltonian diffeomorphism $\phi$ of the closed connected symplectic six-manifold $Q^3$ such that \begin{equation}\label{eq:counterexample} \#\Fix(\phi)=3<4=\Crit(Q^3) =\operatorname{cuplength}(Q^3;\mathbb Q). \end{equation} At least one fixed point of $\phi$ is degenerate.
==================
# FAMILY 348: Nonnegative-curvature Einstein classification and an <i>L</i><sup>2</sup> topological gap
SCOPE: The formalization classifies connected smooth closed Einstein four-manifolds with strictly positive sectional curvature. Up to positive scaling and isometry, every such manifold is the round four-sphere, the complex projective plane with its Fubini–Study metric, or round real projective four-space. No orientability hypothesis is required. In the oriented case, only the sphere and complex projective plane occur.
## CHALLENGE EinsteinFour  targets=['OAI.PositiveEinsteinFour.orientedClassification', 'OAI.PositiveEinsteinFour.classificationOn', 'OAI.PositiveEinsteinFour.classification'] defs=[]
theorem orientedClassification (X : ClosedOrientedMetricFour.{u})
    (hEinstein : IsEinstein X.metric) (hpositive : HasPositiveSectionalCurvature X.metric) :
    ∃ a : ℝ, 0 < a ∧ (ScaledIsometricTo X.metric a roundDistance ∨
      ScaledIsometricTo X.metric a fubiniStudyDistance) := by
  sorry
section
variable (M : Type u) [TopologicalSpace M] [ChartedSpace FourSpace M]
  [IsManifold I4 ∞ M] [T2Space M] [SecondCountableTopology M]
  [CompactSpace M] [ConnectedSpace M]
theorem classificationOn : ClassificationOn M := by
  sorry
end
/-- The connected closed classification includes the real projective quotient. -/
theorem classification (M : Type*) [TopologicalSpace M] [ChartedSpace FourSpace M]
    [IsManifold I4 ∞ M] [T2Space M] [SecondCountableTopology M]
    [CompactSpace M] [ConnectedSpace M] (g : SmoothMetric M)
    (hEinstein : IsEinstein g) (hpositive : HasPositiveSectionalCurvature g) :
    ∃ a : ℝ, 0 < a ∧
      (ScaledIsometricTo g a roundDistance ∨
        ScaledIsometricTo g a fubiniStudyDistance ∨
        ScaledIsometricTo g a realProjectiveDistance) := by
  sorry
end PositiveEinsteinFour
end
DEFS(31): abbrev FourSpace, abbrev I4, def coordinateVector, abbrev RoundSphere4, abbrev ComplexProjective2, abbrev RealProjective4, def roundDistance, def fubiniStudyDistance, def realProjectiveDistance, abbrev SmoothMetric, def metricInChart, def partialDeriv, def christoffel, def curvatureComponent, def ricciInChart, def sectionalNumerator, def IsEinstein, def HasPositiveSectionalCurvature, def scaledEDistance, def ScaledIsometricTo, abbrev Mat4, def chartMetric, structure OrthonormalFrame, def OrthonormalFrame.map, def OrthonormalFrame.vector, structure FrameBundle, def frameRealization, structure FrameOrientation, structure ClosedOrientedMetricFour, def Classified
## PAPER Positively-curved-Einstein-four-manifolds-September-23-2026
ABSTRACT: We prove the classification conjecture for connected smooth closed Einstein four-manifolds with strictly positive sectional curvature. Up to positive scaling and isometry, every such manifold is the round four-sphere, the complex projective plane with its Fubini--Study metric, or real projective four-space with its round metric. No orientability assumption is needed.
[theorem] \label{thm:classification} Let $(M,g)$ be a connected smooth closed Einstein four-manifold with strictly positive sectional curvature, without an orientability assumption. There is a constant $a>0$ such that $(M,ag)$ is isometric to the standard round $S^4$, to $\mathbb{CP}^2$ with its Fubini--Study metric, or to $\mathbb{RP}^4$ with its standard round metric.
==================
# FAMILY 350: Yau’s nodal bounds: surfaces and higher dimensions
SCOPE: Yau's nodal-set conjecture predicts nodal size of order $\sqrt\lambda$ for Laplace eigenfunctions of eigenvalue $\lambda$. The formalization proves the upper bound on every fixed smooth closed connected Riemannian surface: there is a surface-dependent constant $C$ such that the one-dimensional Hausdorff measure of the zero set of every nonzero real eigenfunction with $\lambda>0$ is at most $C\sqrt\lambda$. The known lower bound is not part of this selected statement. The formalized results contradict Yau's proposed $O(\sqrt\lambda)$ upper bound for nodal measure in dimensions three and four. On $S^3$, every prescribed smooth neighborhood of the round metric contains one fixed smooth metric with an eigenfunction sequence of unbounded nodal-measure ratio. A second fixed metric on $S^2\times T^2$ has the same property. In both cases the eigenvalues tend to infinity and the intrinsic nodal m
## CHALLENGE NodalLength  targets=['OAI.SharpNodal.Main'] defs=[]
theorem Main [CompactSpace M] [ConnectedSpace M]
    [IsContMDiffRiemannianBundle 𝓘(ℝ,Plane) ∞ Plane
      (fun x:M=>TangentSpace 𝓘(ℝ,Plane) x)]
    [IsRiemannianManifold 𝓘(ℝ,Plane) M] : MainStatement M := by
  sorry
end SharpNodal
end
DEFS(8): abbrev Plane, def coordinateMetric, def coordinateDensity, def coordPartial, def laplaceBeltrami, def nodalSet, def nodalLength, def MainStatement
## CHALLENGE SmoothYau  targets=['OAI.YauCounterexamples.sphere_three', 'OAI.YauCounterexamples.sphere_two_torus_two'] defs=[]
theorem sphere_three (gRound : SmoothMetric (Euclidean 3) (Sphere 3))
    (hRound : IsRound gRound) :
    ∀ N : Set (SmoothMetric (Euclidean 3) (Sphere 3)),
      IsSmoothNeighborhood gRound N →
      ∃ g ∈ N, HasUnboundedNodalRatio g 3 := by
  sorry
theorem sphere_two_torus_two :
    ∃ g : SmoothMetric FourModel FourManifold,
      HasUnboundedNodalRatio g 4 := by
  sorry
end YauCounterexamples
end
DEFS(18): abbrev Euclidean, abbrev Sphere, abbrev FourManifold, abbrev FourModel, instance torusChartedSpace, instance torusIsManifold, instance fourChartedSpace, instance fourIsManifold, abbrev SmoothMetric, abbrev CoordIndex, def coordinateVector, def metricCoefficients, def laplaceBeltrami, structure CoordinateTest, def IsSmoothNeighborhood, def nodalMeasure, def HasUnboundedNodalRatio, def IsRound
## CHALLENGE YauCounterexample  targets=['OAI.Yau.Target.yau_nodal_set_upper_bound_counterexample'] defs=[]
theorem yau_nodal_set_upper_bound_counterexample : MainTarget := by
  sorry
end
end Target
end Yau
DEFS(12): abbrev Base, abbrev Manifold5, abbrev Model, abbrev modelWithCorners, abbrev SmoothMetric, abbrev Index, def frame, def metricMatrix, def volumeFactor, def chartLaplacian, def nodalMeasure, def MainTarget
## PAPER Sharp-nodal-length-on-smooth-surfaces-September-23-2026
ABSTRACT: We prove that a nonzero real Laplace eigenfunction with eigenvalue $\lambda>0$ on a fixed smooth closed connected Riemannian surface has nodal length at most $C\sqrt\lambda$. Together with the known lower bound, this proves Yau's conjecture in this setting.
[theorem] \label{thm:main} Let $(M,g)$ be a closed connected $C^\infty$ Riemannian surface. There is a finite constant $C=C(M,g)$ such that every nonzero real Laplace eigenfunction satisfying \[ -\Delta_g u=\lambda u,\qquad \lambda>0, \] obeys \[ \mathcal H_g^1(Z_u)\le C\sqrt\lambda. \] Here $\mathcal H_g^1$ is Hausdorff measure for the Riemannian distance. The same constant applies to every eigenfunction in every positive eigenspace.
## PAPER Smooth-counterexamples-to-Yaus-nodal-upper-bound-in-dimensions-three-and-four-September-23-2026
ABSTRACT: We construct a smooth metric on the three-sphere, arbitrarily close to the round metric in the smooth topology, and a smooth metric on $S^2\times\T^2$ for which sequences of exact real Laplace eigenfunctions have unbounded nodal measure divided by the square root of the eigenvalue. Each sequence belongs to one fixed metric. Thus the upper-bound part of Yau's nodal conjecture fails for smooth metrics in dimensions three and four.
[theorem] \label{thm:main} Let $g_*$ be the round metric on $\Sph^3$. Every neighborhood of $g_*$ in the $C^\infty$ topology contains a smooth Riemannian metric $g_\infty$ for which there are nonzero smooth real functions $u_j$ and positive numbers $\lambda_j$ satisfying \[ -\Delta_{g_\infty}u_j=\lambda_j u_j,\qquad \lambda_j\longrightarrow\infty,\qquad \frac{\HH^2_{g_\infty}(Z_{u_j})}{\sqrt{\lambda_j}} \longrightarrow\infty. \]
## PAPER Power-law-violations-of-Yaus-nodal-upper-bound-September-23-2026
ABSTRACT: We construct a smooth Riemannian metric on $S^4\times S^1$ and a sequence of real Laplace eigenfunctions whose nodal four-volume grows faster than $\lambda^{1/2+\epsilon_0}$ for one fixed $\epsilon_0>0$. This disproves the smooth upper-bound assertion in Yau's nodal-set conjecture and the proposed bound with an arbitrarily small positive power loss.
[theorem] \label{thm:main} There exist a smooth Riemannian metric $g$ on $S^4\times S^1$, a number $\epsilon_0>0$, and nonzero real smooth functions $u_j$ with positive eigenvalues $\lambda_j$ such that \[ -\Delta_g u_j=\lambda_j u_j,\qquad \lambda_j\longrightarrow\infty,\qquad \frac{\Hh_g^4(\Z(u_j))} {\lambda_j^{1/2+\epsilon_0}}\longrightarrow\infty. \] The metric and $\epsilon_0$ are fixed throughout the sequence.
==================
# FAMILY 353: Affine Bernstein rigidity through dimension nine and a smooth dimension-ten counterexample
SCOPE: The formalization proves the Euclidean-complete affine Bernstein theorem for graph dimensions $3\le n\le9$. If a smooth function on a nonempty open convex domain has positive-definite Hessian, satisfies the affine maximal equation, and its graph is complete in the induced Euclidean metric, then the domain is all of $\mathbb R^n$ and the function is a positive-definite quadratic polynomial plus an affine term. Its graph is therefore an elliptic paraboloid. The paper's extension to immersed hypersurfaces without an initial graph assumption is outside this selected statement.
## CHALLENGE AffineBernstein  targets=['OAI.AffineBernstein.affine_bernstein'] defs=[]
theorem affine_bernstein
    (n : ℕ) (hn₃ : 3 ≤ n) (hn₉ : n ≤ 9)
    (Ω : Set (Space n)) (hΩne : Ω.Nonempty) (hΩopen : IsOpen Ω)
    (hΩconvex : Convex ℝ Ω) (u : Space n → ℝ)
    (hu : ContDiffOn ℝ ∞ u Ω)
    (hpos : ∀ x ∈ Ω, (hessian u x).PosDef)
    (hmax : AffineMaximalOn Ω u)
    (hcomplete : EuclideanGraphComplete Ω u) :
    Ω = univ ∧
      (∃ (A : Matrix (Fin n) (Fin n) ℝ) (b : Space n) (c : ℝ),
        A.IsSymm ∧ A.PosDef ∧
        ∀ x, u x = (1 / 2 : ℝ) * (∑ i : Fin n, ∑ j : Fin n, x i * A i j * x j)
          + (∑ i : Fin n, b i * x i) + c) ∧
      (∃ e : (Space n × ℝ) ≃ᵃ[ℝ] (Space n × ℝ),
        e '' standardParaboloid n = graph Ω u) := by
  sorry
end AffineBernstein
end
DEFS(11): abbrev Space, def coordinateVector, def hessian, def cofactorHessian, def affineWeight, def AffineMaximalOn, def graphPathLength, def graphEDist, def EuclideanGraphComplete, def graph, def standardParaboloid
## PAPER The-affine-Bernstein-theorem-in-dimensions-three-through-nine-September-24-2026
ABSTRACT: We prove the Euclidean-complete affine Bernstein conjecture in dimensions three through nine: a smooth locally uniformly convex affine maximal graph is an elliptic paraboloid whenever its induced Euclidean metric is complete. The same conclusion holds, without an initial graph assumption, for connected smooth open (noncompact and without boundary) affine-complete locally uniformly convex immersed hypersurfaces that are classically affine maximal in these dimensions.
[theorem] \label{thm:main} Let \(3\le n\le9\). Suppose \(u\in C^\infty(\Omega)\) has positive-definite Hessian and satisfies \eqref{eq:affine-maximal}. If its graph is complete for the induced Euclidean metric \[ g_{ij}=\delta_{ij}+u_i u_j, \] then \(\Omega=\R^n\) and \[ u(x)=\tfrac12 x^{\mathsf T}Ax+b\cdot x+c \] for a positive-definite symmetric matrix \(A\), a vector \(b\), and a constant \(c\). In particular, the graph is an invertible affine image of the standard elliptic paraboloid.
==================
# FAMILY 354: The isoperimetric profile of the cubic three-torus
SCOPE: The formalization determines the isoperimetric profile and all minimizers in the unit cubic flat three-torus. At every volume $0<V<1$, a minimizer exists, and the minimizers, up to null-set changes, are exactly balls, circular tubes about shortest closed geodesics, coordinate slabs, and their complements in the appropriate volume ranges. The classification includes all equality cases at the transition volumes $4\pi/81$ and $1/\pi$, and every minimizer has the stated candidate-profile perimeter.
## CHALLENGE CubicTorus  targets=['OAI.CubicTorus.unit_cubic_isoperimetric'] defs=[]
theorem unit_cubic_isoperimetric (V : ℝ) (hV : V ∈ Ioo 0 1) :
    (∃ E : Set Torus, IsMinimizerAt V E) ∧
    (∀ E : Set Torus, IsMinimizerAt V E →
      perimeter E = ENNReal.ofReal (candidateProfile V)) ∧
    (∀ E : Set Torus, IsMinimizerAt V E ↔ StandardRegionAt V E) := by
  sorry
end CubicTorus
end
DEFS(18): abbrev Cover, abbrev Torus, def quotientMap, def fundamentalCube, def torusVolume, def latticeVector, def AdmissibleField, def divergence, def perimeter, def FinitePerimeter, def IsMinimizerAt, def candidateProfile, def canonicalBall, def canonicalTube, def canonicalSlab, def CongruentAE, def SmallStandardRegion, def StandardRegionAt
## PAPER The-Isoperimetric-Conjecture-for-the-Cubic-Flat-Three-Torus-September-24-2026
ABSTRACT: We prove the isoperimetric conjecture for the cubic flat three-torus and classify all minimizers, including the equality cases at the transition volumes $4\pi/81$ and $1/\pi$. The minimizing regions are balls, circular tubes about shortest closed geodesics, coordinate slabs, and their complements.
[theorem] \label{intro:main} For \(V\in(0,1)\), put \(v=\min(V,1-V)\). Among finite-perimeter subsets of \(\mathbb R^3/\mathbb Z^3\) of volume \(V\), the minimum perimeter is \begin{equation} I_{\rm unit}(V)= \min\left\{(36\pi)^{1/3}v^{2/3},\ 2\sqrt{\pi v},\ 2\right\}. \label{intro:profile} \end{equation} For \(0<V\le1/2\), every minimizing region is, up to an ambient isometry and a null set, one of the following: \[ \begin{array}{c|c} \text{volume range}&\text{region}\\ \hline 0<V\le 4\pi/81 & \text{a ball of radius }(3V/(4\pi))^{1/3}\\[2pt] 4\pi/81\le V\le1/\pi &\text{a solid circular tube of radius }\sqrt{V/\pi}\\ &\text{about a shortest closed geodesic}\\[2pt] 1/\pi\le V\le1/2 &\text{a slab of wid
==================
# FAMILY 356: Gigli’s characterization of Alexandrov curvature
SCOPE: The formalization transfers a weak Hessian upper bound to every prescribed minimizing geodesic in an $\mathrm{RCD}(K,N)$ space with finite $N>1$. If a bounded globally Lipschitz function $F$ has weak Hessian bounded above by $G$ times the metric, where $G$ is bounded and continuous, then every constant-speed geodesic $\gamma:[0,1]\to X$ satisfies $(F\circ\gamma)''\le G(\gamma)\,d(\gamma(0),\gamma(1))^2$ in the distributional sense. Constant geodesics are included. The space is complete and separable with full support and measure finite on bounded sets; compactness and metric nonbranching are not assumed.
## CHALLENGE WeakHessian  targets=['OAI.WeakHessian.every_geodesic'] defs=[]
theorem every_geodesic [CompleteSpace X] [TopologicalSpace.SeparableSpace X]
    (m : Measure X) (K N : ℝ) (hN : 1 < N)
    (hfull : FullSupport m) (hfinite : FiniteOnBoundedSets m) (hrcd : RCD m K N)
    (F G : X → ℝ) (hFbound : BoundedFunction F) (hFlip : GloballyLipschitz F)
    (hGbound : BoundedFunction G) (hGcont : Continuous G)
    (hHess : WeakHessianUpperBound m F G)
    (σ : Curve X) (hσ : IsGeodesic σ) : CurveSecondDerivativeBound F G σ := by
  sorry
end WeakHessian
end
DEFS(45): abbrev Time, def timeZero, def timeOne, def clampTime, abbrev Curve, instance curveMeasurableSpace, instance curveBorelSpace, def evalReal, def IsGeodesic, def metricSpeed, def IsAC2, def IsTestPlan, def BoundedTracks, def LocallyL2, def IsLocalWeakUpperGradient, def IsMinimalLocalWeakUpperGradient, def weakGradient, def LocalSobolev, def Sobolev, def gamma, def IsLaplacian, def InLaplacianDomain, def laplacian, def BoundedFunction, def GloballyLipschitz, def IsTestFunction, def weakHessian, def WeakHessianUpperBound, def localSlope, def cheegerEnergy
## PAPER Weak-Hessian-bounds-along-every-geodesic-in-RCD-spaces-September-24-2026
ABSTRACT: On a full-support \(\RCD(K,N)\) space with \(1<N<\infty\), we prove that a bounded globally Lipschitz function whose distributional Hessian is bounded above by a bounded continuous function satisfies the corresponding second-derivative inequality along every minimizing geodesic.
[theorem[Weak Hessian bounds along every geodesic]] \label{weight:every-geodesic} Let \((M,d,m)\) be a full-support \(\RCD(K,N)\) space, where \(K\in\mathbb R\) and \(1<N<\infty\). Let \(F\colon M\to\mathbb R\) be bounded and globally Lipschitz, and let \(G\colon M\to\mathbb R\) be bounded and continuous. Suppose that for every compactly supported \(g\in\Test(M)\) and every nonnegative \(h\in\Lip_c(M)\), \begin{equation} \label{weight:hessian-assumption} H_F(\nabla g,\nabla g)(h) \le\int_M hG\Gamma(g)\dd m. \end{equation} Then every constant-speed minimizing geodesic \(\sigma\colon[0,1]\to M\), of length \(\ell\), satisfies \begin{equation} \label{weight:curve-hessian} (F\circ\sigma)''\le\ell^2G\circ\sigma \qquad\text{in distributions on }(0,
==================
# FAMILY 358: A three-manifold without conjugate points or nonpositive curvature
SCOPE: The formalized result separates absence of conjugate points from nonpositive sectional curvature. It constructs a closed connected orientable smooth three-manifold with a smooth Riemannian metric having no conjugate points, while the same manifold admits no smooth metric of everywhere nonpositive sectional curvature. The no-conjugate-points assertion ranges over all geodesics and tangent-bundle Jacobi fields, including constant geodesics and unbounded time intervals. The separate no-focal-points and CAT(0) consequences are not included.
## CHALLENGE ConjugatePoints  targets=['OAI.ThreeManifold.main_theorem'] defs=[]
theorem main_theorem : MainStatement := by
  sorry
end ThreeManifold
end
DEFS(18): abbrev E3, abbrev I3, def OrientedAtlas, abbrev SmoothMetric, def basisVector, def metricMatrix, def coordPartial, def christoffel, def connectionTerm, def curvatureCoefficient, def curvatureTerm, def NonpositiveSectionalCurvature, def alongDerivative, def IsGeodesicOn, def fieldCoordinates, def IsJacobiFieldOn, def NoConjugatePoints, def MainStatement
## PAPER A-Three-Manifold-Without-Conjugate-Points-and-Without-a-Nonpositively-Curved-Metric-September-24-2026
ABSTRACT: We construct a closed connected orientable smooth three-manifold that admits a smooth Riemannian metric without conjugate points but admits no smooth Riemannian metric of nonpositive sectional curvature.
[theorem] \label{thm:main} There exists a closed connected orientable smooth three-manifold $M$ with a $C^\infty$ Riemannian metric without conjugate points, such that $M$ admits no $C^\infty$ Riemannian metric whose sectional curvature is everywhere at most zero.
==================
# FAMILY 359: Negative Kähler curvature without bounded holomorphic coordinates
SCOPE: The formalized result constructs a nonempty contractible complex threefold with a complete Kähler metric whose real sectional curvatures lie between two fixed negative constants. Nevertheless, it has no system of bounded holomorphic coordinates and is not biholomorphic to a bounded domain. The metric is obtained from an explicitly controlled potential. This is the negatively pinched construction; the different companion with only one-sided curvature control is separate.
## CHALLENGE PinchedKahler  targets=['OAI.PinchedHartogs.main_theorem', 'OAI.PinchedHartogs.controlled_potential', 'OAI.PinchedHartogs.metric_transfer'] defs=[]
theorem main_theorem : MainTheorem := by
  sorry
theorem controlled_potential : ControlledPotential := by
  sorry
theorem metric_transfer : MetricTransfer := by
  sorry
end PinchedHartogs
end
DEFS(37): abbrev Base, abbrev Ambient, abbrev Target, def ball, def hartogs, def noMinorant, def coordVector, def jacobian, abbrev CMatrix, abbrev CurvatureTensor, def coordinates, def dz, def dbar, def hermitianValue, def realArea, def tensorValue, def curvature, def sectional, def IsKahlerMetric, def christoffel, def GeodesicallyComplete, def IsNegativelyPinched, def NoBoundedCoordinates, def BiholomorphicToBoundedDomain, def MainTheorem, def psi, def metricPotential, def complexHessian, def hartogsMetric, def dzBase
## PAPER A-negatively-pinched-Kahler-threefold-without-bounded-holomorphic-coordinates-September-25-2026
ABSTRACT: We construct a contractible domain in complex dimension three with a complete K\"ahler metric whose real sectional curvatures lie between two finite negative constants. It admits no bounded holomorphic map to $\mathbb C^3$ with nowhere-vanishing Jacobian and is therefore not biholomorphic to a bounded domain. This gives a negative answer to the negatively pinched K\"ahler uniformization question.
[theorem] \label{main:theorem} There exist a contractible domain $M\subset\C^3$, a smooth complete K\"ahler metric $g$ on $M$, and finite constants $0<A\le B$ such that \[ -B\le K_g(\sigma)\le -A<0 \] for every real two-plane $\sigma\subset T_pM$ and every $p\in M$. No bounded holomorphic map $F:M\to\C^3$ has a nowhere-vanishing Jacobian determinant. In particular, $M$ is not biholomorphic to a bounded domain in $\C^3$.
==================
# FAMILY 360: Weak MTW curvature gives convexity and regular optimal transport
SCOPE: On a compact connected smooth Riemannian manifold of dimension at least two, the formalized result proves that weak MTW curvature implies convexity of every open tangent injectivity domain. Prior convexity or nonfocality is not assumed. Additional formalized results give global support at ordinary subgradients, compact convex lifted gap sections with the stated diameter bound, and scale and local-injectivity estimates for finite target families. The latter finite-family result does not cover the paper's arbitrary-potential local-injectivity assertion. The formalized result gives uniform bi-Hölder optimal transport for squared-distance cost on each fixed compact connected smooth Riemannian manifold of dimension at least two satisfying weak MTW. For probability densities between fixed positive lower and finite upper bounds, one exponent and constant work for every pair of densities. The op
## CHALLENGE WeakMTWGlobalSupport  targets=['OAI.WeakMTWGlobalSupport.current_main_convexity'] defs=[]
theorem current_main_convexity
    {n : ℕ} (hn : 2 ≤ n) {M : Type*}
    [MetricSpace M] [ChartedSpace (WeakMTW.Model n) M]
    [IsManifold (WeakMTW.model n) ∞ M]
    [CompactSpace M] [ConnectedSpace M]
    [RiemannianBundle (fun x : M => TangentSpace (WeakMTW.model n) x)]
    [IsContMDiffRiemannianBundle (WeakMTW.model n) ∞ (WeakMTW.Model n)
      (fun x : M => TangentSpace (WeakMTW.model n) x)]
    [IsRiemannianManifold (WeakMTW.model n) M]
    (hmtw : WeakMTW.HasWeakMTW (n := n) (M := M)) :
    WeakMTW.MainConvexity (n := n) (M := M) :=
  by
    sorry
end WeakMTWGlobalSupport
DEFS(10): abbrev Model, abbrev model, def CompleteGeodesicWithInitialData, def ExpEndpoint, def exp, def injectivityDomain, def cost, def mtw, def HasWeakMTW, def MainConvexity
## CHALLENGE BiholderTransport  targets=['OAI.WeakMTWTransport.uniform_biHolder_transport'] defs=[]
theorem uniform_biHolder_transport
    {n : ℕ} (hn : 2 ≤ n) {M : Type*}
    [MetricSpace M] [CompactSpace M] [ConnectedSpace M]
    [ChartedSpace (Model n) M] [IsManifold 𝓘(ℝ, Model n) ∞ M]
    [RiemannianBundle (fun x : M => TangentSpace 𝓘(ℝ, Model n) x)]
    [IsContMDiffRiemannianBundle 𝓘(ℝ, Model n) ∞ (Model n)
      (fun x : M => TangentSpace 𝓘(ℝ, Model n) x)]
    [IsRiemannianManifold 𝓘(ℝ, Model n) M]
    [MeasurableSpace M] [BorelSpace M]
    (hmtw : WeakMTW (n := n) (M := M))
    (lam cap : ℝ) (hlam : 0 < lam) (hcap : lam ≤ cap)
    (hclass : ∃ rho : M → ℝ, AdmissibleDensity (metricVolume n) lam cap rho) :
    ∃ alpha C : ℝ, 0 < alpha ∧ alpha ≤ 1 ∧ 0 ≤ C ∧
      ∀ rho0 rho1 : M → ℝ,
        AdmissibleDensity (metricVolume n) lam cap rho0 →
        AdmissibleDensity (metricVolume n) lam cap rho1 →
        ∃ T : M ≃ₜ M,
          IsOptimalMap (metricVolume n) rho0 rho1 T ∧
          (∀ S : M → M, IsOptimalMap (metricVolume n) rho0 rho1 S →
            S =ᵐ[densityMeasure (metricVolume n) rho0] T) ∧
          BiHolderEstimate alpha C T := by
  sorry
end WeakMTWTransport
end
DEFS(13): abbrev Model, def cost, def euclideanVolumeFactor, def metricVolume, def AdmissibleDensity, def densityMeasure, def IsOptimalMap, def BiHolderEstimate, def IsGeodesicWithInitialData, def riemannianExp, def injectivityDomain, def mtw, def WeakMTW
## PAPER Global-Support-and-Convex-Injectivity-Domains-under-Weak-MTW-September-25-2026
ABSTRACT: We prove that weak Ma--Trudinger--Wang curvature on a smooth, connected, compact Riemannian manifold of dimension at least two without boundary implies convexity of every tangent injectivity domain, resolving Villani's conjecture in this setting. Conjugate cut points are allowed. More generally, every ordinary subgradient of a squared-distance cost potential is a minimizing velocity with a global supporting mountain. No density hypothesis is used.
[theorem[Convexity of injectivity domains]] \label{thm:main} If $(M,g)$ satisfies \eqref{eq:weak-mtw}, then $I(x)$ is convex for every $x\in M$. More precisely, for every $v_0,v_1\in I(x)$ and $\theta\in[0,1]$, \[ (1-\theta)v_0+\theta v_1\in I(x). \]
## PAPER Uniform-Bi-Holder-Transport-from-Weak-MTW-September-25-2026
ABSTRACT: We prove that the weak Ma--Trudinger--Wang condition on a fixed smooth connected compact boundaryless Riemannian manifold of dimension at least two implies a common H\"older estimate for optimal transport maps and their inverses over the entire class of probability densities with fixed positive upper and lower bounds. The maps have homeomorphic representatives, conjugate cut points are allowed, and no density regularity is assumed.
[theorem[Uniform bi-H\"older transport]] \label{thm:main} Fix $(M,g)$ as above and $0<\lambda\leq\Lambda<\infty$ for which the following density class is nonempty. There are $\alpha\in(0,1]$ and $C<\infty$, depending only on $(M,g),\lambda,\Lambda$, such that the following holds for every pair of measurable densities satisfying \[ \int_M\rho_i\,d\vol=1,\qquad \lambda\leq\rho_i\leq\Lambda\quad\vol\text{-almost everywhere}, \qquad i=0,1. \] The almost-everywhere unique optimal map from $\rho_0\vol$ to $\rho_1\vol$ for the cost $c$ has a homeomorphic representative $\widetilde T:M\to M$, and \[ d(\widetilde T(x),\widetilde T(x'))\leq C d(x,x')^\alpha, \qquad d(\widetilde T^{-1}(y),\widetilde T^{-1}(y')) \leq C d(y,y')^\alpha \] for al
==================
# FAMILY 361: Failure of integer-degree harmonic dimension comparison
SCOPE: The formalized result disproves the proposed Euclidean upper comparison for dimensions of harmonic functions with integer polynomial growth. It constructs one complete smooth metric with nonnegative Ricci curvature on an even-dimensional Euclidean space, Euclidean near the origin and with asymptotic volume ratio strictly between zero and one, admitting more independent harmonic functions of the prescribed growth degree than the Euclidean count. The construction uses dimension $16$ and degree $50000$. Separate tangent-cone and cone-spectrum conclusions are not included.
## CHALLENGE HarmonicGrowth  targets=['OAI.HarmonicCounterexample.main'] defs=[]
theorem main : MainClaim := by sorry
end HarmonicCounterexample
end
DEFS(18): abbrev Space, abbrev Mat, structure SmoothMetric, def coordDeriv, def christoffel, def ricci, def RicciNonnegative, def laplaceBeltrami, def pathLength, def distance, def Complete, def EuclideanNearOrigin, def ballVolume, def omega, def PositiveSubunitAVR, def HarmonicGrowth, def euclideanDimension, def MainClaim
## PAPER A-counterexample-to-integer-degree-harmonic-dimension-comparison-September-25-2026
ABSTRACT: For some even $n\ge8$ and integer $k\ge2$, we construct a complete smooth metric on $\mathbb R^n$ with nonnegative Ricci curvature whose space of real harmonic functions of pointwise polynomial growth at most $k$ has dimension larger than the Euclidean harmonic-polynomial dimension. The metric is Euclidean near the origin, has asymptotic volume ratio strictly between zero and one, and has nonunique tangent cones at infinity. This answers the integer-degree form of Yau's dimension comparison question in the negative.
[theorem] \label{thm:main} There are an even integer $n\geq8$, an integer $k\geq2$, and a complete smooth metric $g$ on $\mathbb R^n$ such that $\operatorname{Ric}_g\geq0$ and \[ h_k(\mathbb R^n,g)>h_k(\mathbb R^n,g_{\mathrm E}). \] The metric is Euclidean near the origin, and its asymptotic volume ratio satisfies \[ 0<\lim_{R\to\infty} \frac{\operatorname{vol}_g B_g(0,R)}{\omega_nR^n}<1, \] where $\omega_n$ is the volume of the Euclidean unit ball.
==================
# FAMILY 362: Global smoothness for relativistic Vlasov–Maxwell
SCOPE: The formalized result gives global existence and uniqueness for the three-dimensional one-species relativistic Vlasov–Maxwell system. The initial particle density is nonnegative, smooth, and compactly supported; the initial fields have bounded derivatives of all orders, finite energy, and satisfy both Gauss constraints. The solution is smooth on every finite time interval, has compact particle phase support there, and is unique among classical solutions. No smallness, symmetry, or neutrality assumption is imposed.
## CHALLENGE VlasovMaxwell  targets=['OAI.RVM.global_classical_solution'] defs=[]
theorem global_classical_solution (d : Datum) (hd : Admissible d) :
    ∃ s : Solution, Classical d s ∧ SmoothOnFiniteHorizons s ∧
      ∀ s' : Solution, Classical d s' → SameNonnegativeTime s s' := by
  sorry
end RVM
end
DEFS(28): abbrev Vec, abbrev Phase, abbrev Particle, abbrev Field, def q, def velocity, def basis, def dot, def cross, def spatialPartial, def divergence, def curl, def rho, def current, structure Datum, def BoundedSmooth, def Admissible, structure Solution, def particleHalfSpace, def fieldHalfSpace, def particleSlab, def fieldSlab, def TimeContinuousL2, def Equations, def CompactOnFiniteHorizons, def Classical, def SmoothOnFiniteHorizons, def SameNonnegativeTime
## PAPER Global-classical-solutions-of-the-three-dimensional-relativistic-Vlasov-Maxwell-system-September-23-2026
ABSTRACT: We prove global existence and uniqueness for arbitrary smooth admissible initial data in the three-dimensional, one-species relativistic Vlasov--Maxwell system. The particle density is initially compactly supported, and the electromagnetic fields have finite energy and bounded derivatives of all orders. The solution remains smooth on every finite time interval. This resolves the large-data global classical regularity problem for this model, without size or symmetry restrictions on the data.
[theorem] \label{thm:global} Every smooth admissible datum \eqref{eq:data} generates a unique global classical solution of \eqref{eq:rvm}. For every finite $T$, this solution satisfies \[ f\in C^\infty([0,T]\times\R^3_x\times\R^3_v),\qquad E,B\in C^\infty([0,T]\times\R^3_x;\R^3), \] and $f$ has compact phase-space support on $[0,T]$. The two divergence constraints hold for all time.
==================
# FAMILY 363: Nonuniqueness with local conservation for the hard-sphere Boltzmann equation
SCOPE: The formalization proves nonuniqueness for the periodic hard-sphere Boltzmann equation by constructing two distinct global renormalized solutions on $\mathbb T^3\times\mathbb R^3$ with the same nonnegative initial density. The data have bounded velocity support and finite mass, energy, and absolute entropy. Both solutions conserve local mass and total momentum and satisfy the global energy and entropy-dissipation inequalities. On a common initial interval they are strongly continuous in $L^1$, with integrable collision gains and losses. These are the conditions of the selected periodic result; later local-conservation refinements are outside it.
## CHALLENGE BoltzmannNonuniqueness  targets=['OAI.BoltzmannNonuniqueness.nonuniqueness'] defs=[]
theorem nonuniqueness :
    ∃ f₀ : Density, BoundedVelocitySupport f₀ ∧
      ∃ (F G : Evolution) (T : ℝ), AdmissibleGlobal f₀ F ∧ AdmissibleGlobal f₀ G ∧
        StrongEarly T F ∧ StrongEarly T G ∧
        ∃ t ∈ Set.Icc 0 T, ¬(F t =ᵐ[MeasureTheory.volume] G t) :=
  sorry
end BoltzmannNonuniqueness
end
DEFS(38): abbrev Velocity, abbrev Position, abbrev Phase, abbrev Density, abbrev Sphere, def sphereArea, def normalComponent, def scatterLeft, def scatterRight, def collisionKernel, def gain, def loss, def collision, abbrev Evolution, abbrev SpaceTimePhase, abbrev LiftedSpaceTimePhase, def torusProjection, def torusRepresentative, def maxwellian, def entropyMoment, def FiniteEntropyDatum, def BoundedVelocitySupport, def energy, def momentum, def relativeEntropy, def extendedEntropyProduction, def entropyDissipation, structure Renormalization, structure KineticTest, def KineticTest.transportDerivative
## PAPER Nonuniqueness-for-the-periodic-hard-sphere-Boltzmann-equation-September-23-2026
ABSTRACT: We prove nonuniqueness for the periodic hard-sphere Boltzmann equation by constructing two distinct global renormalized solutions with the same nonnegative initial density on \(\T^3\times\R^3\). This density has bounded velocity support and finite mass, energy, and absolute entropy. Both solutions conserve local mass and total momentum and satisfy the global energy and entropy-dissipation inequalities. On a common initial interval, they are strongly continuous in \(L^1\), and their collision gains and losses are integrable.
[theorem] \label{thm:main} There is a nonnegative density \(F_0\) on \(\T^3\times\R^3\), with bounded velocity support and \[ \int_{\T^3\times\R^3} F_0(1+|v|^2+|\log F_0|)\dd x\dd v<\infty, \] for which the hard-sphere Boltzmann equation has two distinct global admissible solutions, in the sense of Definition~\ref{def:admissible}, with initial datum \(F_0\). On some common initial interval both solutions are strongly continuous in \(L^1\), and their collision gains and losses are integrable in space-time-velocity.
==================
# FAMILY 365: Joint metric and connection recovery from one boundary patch
SCOPE: The Calderón inverse problem asks whether boundary measurements determine an interior conductivity. The formalized result gives nonuniqueness for bounded measurable scalar conductivities on the ball $B(0,3)\subset\mathbb R^3$: two uniformly positive conductivities differ on a set of positive volume, equal $1$ near the boundary, and have the same full weak Dirichlet-to-Neumann operator. Weak solutions exist uniquely for every boundary trace.
## CHALLENGE Conductivity  targets=['OAI.ScalarConductivity.main_nonuniqueness'] defs=[]
theorem main_nonuniqueness : MainStatement := by
  sorry
end ScalarConductivity
end
DEFS(23): abbrev R3, abbrev JetFiber, def ball, def ballMeasure, abbrev JetSpace, def smoothJet, def smoothJets, def compactSmoothJets, def H1Space, abbrev H1, def zeroTraceAmbient, def H10, instance H10_isClosed, abbrev TraceSpace, abbrev TraceDual, abbrev DNOperator, def trace, def weakGradient, def energy, def Harmonic, def IsDirichletToNeumann, def EqualOneNearBoundary, def MainStatement
## PAPER Nonuniqueness-for-Bounded-Measurable-Scalar-Conductivities-in-Three-Dimensions-September-23-2026
ABSTRACT: We construct two distinct uniformly positive bounded measurable scalar conductivities on a ball in $\R^3$ with the same full Dirichlet-to-Neumann operator. Both conductivities equal one near the boundary. This gives nonuniqueness in the scalar Calder\'on problem at bounded measurable regularity.
[theorem] \label{thm:main} There exist real scalar functions $\gamma_0,\gamma_1\in L^\infty(B(0,3);\R)$ and constants $0<c<C<\infty$ such that \begin{enumerate}[label=\textup{(\roman*)},itemsep=2pt] \item $c\leq\gamma_j\leq C$ almost everywhere, for $j=0,1$; \item both conductivities equal $1$ in a neighborhood of the boundary; \item $\abs{\{x:\gamma_0(x)\ne\gamma_1(x)\}}>0$; \item $\Lambda_{\gamma_0}=\Lambda_{\gamma_1}$ as bounded operators from $H^{1/2}(\partial B(0,3))$ to $H^{-1/2}(\partial B(0,3))$. \end{enumerate}
==================
# FAMILY 367: The critical dimension for the one-phase Bernoulli problem
SCOPE: The paper identifies seven as the critical dimension for nonflat one-homogeneous global minimizers of the one-phase Bernoulli problem. The linked formalization proves the existence side: in dimension seven there is a nonzero one-homogeneous global minimizer that is not a half-space solution. The flatness classification in dimensions at most six and the resulting regularity and singular-set bounds are outside this selected statement.
## CHALLENGE BernoulliNonflatInSeven  targets=['OAI.Bernoulli.nonflat_in_seven'] defs=[]
theorem nonflat_in_seven : ∃ u : Space 7 → ℝ,
    GlobalMinimizer u ∧ Nonzero u ∧ OneHomogeneous u ∧ ¬ Flat u := by
  sorry
end Bernoulli
end
DEFS(12): abbrev Space, def Test, def WeakGradient, def H1, def H10, def H1Loc, def energy, def LocalMinimizer, def GlobalMinimizer, def OneHomogeneous, def Nonzero, def Flat
## PAPER The-critical-dimension-for-one-phase-Bernoulli-minimizers-September-24-2026
ABSTRACT: We prove that seven is the critical dimension for the one-phase Bernoulli problem: every nonzero one-homogeneous global minimizer in dimensions at most six is flat, while a nonflat one-homogeneous global minimizer exists in dimension seven. It follows that the interior free boundary of a local minimizer is smooth in dimensions at most six. In dimension $n\ge7$, its singular set has Hausdorff dimension at most $n-7$, and this bound is sharp. In dimension seven, the singular set is locally finite.
[theorem] \label{thm:main} Every nonzero one-homogeneous global minimizer of \eqref{eq:energy} in \(\R^d\), \(1\leq d\leq6\), is flat. There is a nonflat one-homogeneous global minimizer in \(\R^7\). Consequently, \[ d_*=7. \]
==================
# FAMILY 369: The hot spots conjecture for simply connected planar domains
SCOPE: The strict hot-spots conjecture asks whether extrema of a first nonconstant Neumann eigenfunction occur only on the boundary. The formalization proves the stronger interior statement on every nonempty smooth bounded simply connected planar domain: every nonzero eigenfunction in the first positive Neumann eigenspace has nonvanishing gradient throughout the interior. Consequently all global maxima and minima lie on the boundary. The conclusion applies to every eigenfunction even when the eigenvalue is multiple.
## CHALLENGE HotSpots  targets=['OAI.StrictHotSpots.main_theorem'] defs=[]
theorem main_theorem (Ω : Set Plane) (hΩ : AdmissibleDomain Ω)
    (u : Plane → ℝ) (hu : InFirstNeumannEigenspace Ω u)
    (hne : ∃ x ∈ Ω, u x ≠ 0) : MainConclusion Ω u := by
  sorry
end StrictHotSpots
end
DEFS(8): abbrev Plane, def SmoothBoundary, def AdmissibleDomain, def HasH1Gradient, def rayleighValues, def firstPositiveNeumannValue, def InFirstNeumannEigenspace, def MainConclusion
## PAPER Strict-hot-spots-and-absence-of-interior-critical-points-on-smooth-simply-connected-planar-domains-September-24-2026
ABSTRACT: We prove the strict hot spots conjecture for smooth bounded simply connected planar domains. More precisely, every nonzero eigenfunction for the first positive Neumann eigenvalue has nonvanishing gradient in the interior, so all its global maxima and minima lie on the boundary. This holds even when the eigenvalue is multiple.
[theorem] \label{thm:main} For every $0\ne u\in\V$, \[ \grad u(x)\ne0\qquad(x\in\Omega). \] In particular, \begin{equation}\label{eq:hotspots} \min_{y\in\partial\Omega}u(y)<u(x)<\max_{y\in\partial\Omega}u(y) \qquad(x\in\Omega). \end{equation}
==================
# FAMILY 370: The Lane–Emden and Hénon–Lane–Emden conjectures
SCOPE: The formalized result proves nonexistence of positive entire solutions to the subcritical Hénon–Lane–Emden system. For $n\ge2$, $p,q>0$, and real $A,B$ with $(n+A)/(p+1)+(n+B)/(q+1)>n-2$, there are no positive functions, continuous everywhere and $C^2$ off the origin, satisfying $-\Delta u=|x|^A v^p$ and $-\Delta v=|x|^B u^q$ away from the origin. It includes the globally $C^2$ unweighted case for $n\ge3$. The critical equality case is not included.
## CHALLENGE HenonEmden  targets=['OAI.HenonLaneEmden.main_nonexistence'] defs=[]
theorem main_nonexistence (n : ℕ) (hn : 2 ≤ n) (p q A B : ℝ)
    (hp : 0 < p) (hq : 0 < q) (hsub : Subcritical n p q A B) :
    ¬ ∃ u v : Space n → ℝ, IsSolution n p q A B u v := by
  sorry
end HenonLaneEmden
DEFS(3): abbrev Space, structure IsSolution, def Subcritical
## PAPER The-Subcritical-Henon-Lane-Emden-Conjecture-September-24-2026
ABSTRACT: We prove the subcritical H\'enon--Lane--Emden conjecture: for every dimension $n\ge2$, positive powers $p,q$, and real weights $A,B$, the system has no strictly positive entire solution when $(n+A)/(p+1)+(n+B)/(q+1)>n-2$. Solutions need only be continuous at the origin and classical elsewhere, without a condition at infinity. For \(n\ge3\) and \(A,B>-2\), combining this result with the radial existence theorem of Bidaut-V\'eron and Giacomini proves Phan's Conjecture~C in full: a positive radial entire solution exists whenever the strict inequality fails.
[theorem] \label{thm:main} Let \(n\ge2\) be an integer, let \(p,q>0\), and let \(A,B\in\R\). Suppose that \begin{equation}\label{eq:subcritical} \frac{n+A}{p+1}+\frac{n+B}{q+1}>n-2. \end{equation} There are no functions \[ u,v\in C^2(\R^n\setminus\{0\})\cap C(\R^n), \qquad u(x)>0,\quad v(x)>0\quad(x\in\R^n), \] satisfying Equation~\eqref{eq:system} at every \(x\ne0\).
==================
# FAMILY 371: Stable blowup for the defocusing Schrödinger equation
SCOPE: The formalization constructs stable self-similar finite-time blowup for defocusing nonlinear Schrödinger equations on the twelve-dimensional torus. For every prescribed lower bound on the power, it selects an odd power at least that large and a Sobolev index $k>8$ for which a nonempty open set of $H^k$ initial data has the stated classical blowup behavior. The selected quantifier gives arbitrarily large odd powers, rather than every sufficiently large odd power. For each such construction, Gaussian Fourier data with decay exponent $\alpha>k+6$ assign positive probability to the blowup set, and almost-sure global existence fails. The exponent $\alpha$ may be arbitrarily large.
## CHALLENGE DefocusingNLS  targets=['OAI.DefocusingNLS.stable_blowup', 'OAI.DefocusingNLS.gaussian_blowup', 'OAI.DefocusingNLS.gaussian_not_almost_sure_global'] defs=[]
theorem stable_blowup (p₀ : ℕ) :
    ∃ p k : ℕ, p₀ ≤ p ∧ Odd p ∧ 3 ≤ p ∧ ∃ hk : 8 < (k : ℝ),
      ∃ U : Set FourierL2, U.Nonempty ∧ IsOpen U ∧ ∀ f ∈ U,
        IsClassicalDefocusingFlow k (by linarith) ((p - 1) / 2) f ∧
        HasFiniteTimeSelfSimilarBlowup k (by linarith) ((p - 1) / 2)
          (1 / ((p : ℝ) - 1)) f := by
  sorry
/-- Corollary 1.2: for every permitted Gaussian Fourier decay exponent,
the same open blowup family has positive Gaussian probability. -/
theorem gaussian_blowup (p₀ : ℕ) :
    ∃ p k : ℕ, p₀ ≤ p ∧ Odd p ∧ 3 ≤ p ∧ ∃ hk : 8 < (k : ℝ),
      ∃ U : Set FourierL2, U.Nonempty ∧ IsOpen U ∧
      (∀ f ∈ U, IsClassicalDefocusingFlow k (by linarith) ((p - 1) / 2) f ∧
        HasFiniteTimeSelfSimilarBlowup k (by linarith) ((p - 1) / 2)
          (1 / ((p : ℝ) - 1)) f) ∧
      ∀ α : ℝ, (k : ℝ) + 6 < α →
        (∀ᵐ g ∂fourierGaussianLaw, Memℓp (weightedGaussianCoefficient k α g) 2) ∧
        (∀ᵐ g ∂fourierGaussianLaw, ∀ n,
          sobolevFourierCoefficient k (weightedGaussianVector k α g) n =
            (1 + ‖n‖ ^ 2) ^ (-α / 2) • g n) ∧
        0 < weightedGaussianLaw k α U := by
  sorry
/-- In particular, Gaussian data are not almost surely globally continuable. -/
theorem gaussian_not_almost_sure_global (p₀ : ℕ) :
    ∃ p k : ℕ, p₀ ≤ p ∧ Odd p ∧ 3 ≤ p ∧ ∃ hk : 8 < (k : ℝ),
      ∀ α : ℝ, (k : ℝ) + 6 < α →
        ¬ ∀ᵐ f ∂weightedGaussianLaw k α,
          maximalSobolevInteractionDomain k (by linarith) ((p - 1) / 2) f = univ := by
  sorry
end DefocusingNLS
end
DEFS(32): def frequencyLattice, def complexGaussian, instance complexGaussian_isProbabilityMeasure, def fourierGaussianLaw, def sobolevVariance, def weightedGaussianCoefficient, abbrev FourierL2, def weightedGaussianVector, def sobolevFourierCoefficient, def weightedGaussianLaw, abbrev SchrodingerTorus, def frequencyCoordinates, def torusCharacter, def sobolevTorusTerm, def sobolevTorusFunction, def sobolevProductWeight, def sobolevProductCoefficient, def sobolevProduct, def fourierConjugate, def sobolevOddPower, def schrodingerMultiplier, def schrodingerFlow, def fourierContraction, def lowerSobolevInclusion, def lowerSobolevGenerator, def schrodingerInteractionField, structure SobolevInteractionPatch, def maximalSobolevInteractionDomain, def maximalSobolevInteractionFlow, def maximalSobolevSchrodingerFlow
## PAPER Stable-Self-Similar-Blowup-for-a-Supercritical-Defocusing-Schrodinger-Equation-on-the-Torus-September-24-2026
ABSTRACT: We prove stable self-similar finite-time blowup for a supercritical defocusing nonlinear Schr\"odinger equation on the twelve-dimensional torus. For a sufficiently large odd power, the blowup initial data contain a nonempty open set in a high Sobolev space. As a consequence, Gaussian Fourier initial data of arbitrarily high Sobolev regularity can have positive probability of finite-time blowup.
[theorem[An open set of blowup data]] \label{thm:blowup} There exist an odd integer $p\geq3$, a finite integer $k>8$, and a nonempty open set $\mathcal U\subset H^k(\mathbb T^{12};\mathbb C)$ with the following property. For every $u_0\in\mathcal U$, the unique local solution of \eqref{eq:nls} extends to \[ u\in C([0,T);H^k)\cap C^1([0,T);H^{k-2}) \] for some finite $T>0$, but has no continuous $H^k$ extension through $T$. More precisely, there are $x_*\in\mathbb T^{12}$ and $c_0>0$ such that \[ \lim_{t\uparrow T}(T-t)^{1/(p-1)}|u(t,x_*)|=c_0. \] The power can be chosen sufficiently large, and $k$ is then fixed after that choice.
==================
# FAMILY 372: Global uniqueness in smooth isotropic elasticity
SCOPE: The formalization proves global uniqueness in the three-dimensional static isotropic elasticity inverse problem. On a bounded connected smooth domain, let two pairs of smooth real Lamé moduli satisfy $\mu>0$ and $3\lambda+2\mu>0$ on the closure. If their full displacement-to-traction maps agree, then both Lamé moduli agree throughout the domain. The selected statement is uniqueness; it does not supply a reconstruction algorithm.
## CHALLENGE ElasticityUniqueness  targets=['OAI.Elasticity.global_uniqueness'] defs=[]
theorem global_uniqueness : MainClaim := by
  sorry
end Elasticity
end
DEFS(23): abbrev X, abbrev V, def coordVector, def SmoothBoundary, def Domain, def SmoothUpTo, def Admissible, abbrev Ambient, def coordDeriv, def SmoothJets, def TestJets, abbrev H1, def HasZeroTrace, def SameTrace, abbrev BoundaryData, def trace, def div, def strain, def energy, def WeakSolution, def dirichletSolution, def DN, def MainClaim
## PAPER Global-Uniqueness-for-the-Smooth-Isotropic-Elasticity-Inverse-Problem-September-24-2026
ABSTRACT: We prove that the full static displacement-to-traction map uniquely determines both real smooth Lam\'e moduli on every bounded connected smooth domain in $\R^3$, provided $\mu>0$ and $3\lambda+2\mu>0$ on the closure. This resolves the smooth three-dimensional isotropic elastic Calder\'on uniqueness problem under these positivity assumptions.
[theorem] \label{thm:main} Let $\Omega\subset\R^3$ be any bounded connected domain with $C^\infty$ boundary. For $j=1,2$, let $\lambda_j,\mu_j\in C^\infty(\overline\Omega;\R)$ satisfy $\mu_j>0$ and $3\lambda_j+2\mu_j>0$ on $\overline\Omega$. If \[ \Lambda_{\lambda_1,\mu_1} =\Lambda_{\lambda_2,\mu_2} \colon H^{1/2}(\partial\Omega;\R^3) \longrightarrow H^{-1/2}(\partial\Omega;\R^3), \] then $\lambda_1=\lambda_2$ and $\mu_1=\mu_2$ throughout $\Omega$.
==================
# FAMILY 373: Nonattainment of the three-marginal Coulomb Monge problem
SCOPE: The Monge ansatz asks whether an optimal multi-marginal transport plan can be induced by maps from one marginal. For the three-marginal Coulomb cost in $\mathbb R^3$, the formalization constructs a smooth compactly supported probability density, with smooth compactly supported square root, for which no pair of measure-preserving Borel maps attains the Kantorovich minimum. Nevertheless, the Monge and Kantorovich infima are equal: preserving maps with finite costs approach the minimum. This is the three-dimensional Coulomb result; the paper's inverse-power extensions in every dimension are outside this statement.
## CHALLENGE CoulombCounterexample  targets=['OAI.Problem356.coulomb_counterexample_and_equal_infima'] defs=[]
theorem coulomb_counterexample_and_equal_infima :
    ∃ rho : E3 → ℝ, HasFullCoulombConclusion rho := by
  sorry
end Problem356
end
DEFS(19): abbrev E3, abbrev Triple, def tripleFst, def tripleSnd, def tripleThd, def invDistance, def coulombCost, def IsThreeCoupling, def densityMeasure, def Preserves, def graphCost, def kantorovichValue, def mongeValue, def IsSmoothCompactProbabilityDensity, def KantorovichAttained, def NoMongeOptimizer, def FiniteMongeApproximation, def HasCoulombCounterexample, def HasFullCoulombConclusion
## PAPER A-counterexample-to-the-Monge-ansatz-for-the-three-marginal-Coulomb-cost-September-25-2026
ABSTRACT: We construct a smooth compactly supported probability density on \(\R^3\), with a smooth compactly supported square root, for which the three-marginal Coulomb transport minimum is not attained by any pair of measure-preserving Borel maps. Nevertheless, the Monge and Kantorovich infima agree: we construct preserving maps whose costs approach the Kantorovich minimum. For every \(d\ge2\) and \(s>0\), we also construct a smooth identical marginal with the same nonattainment and equality-of-infima properties for the inverse-power interaction \(\sum_{i<j}|x_i-x_j|^{-s}\) on \(\R^d\).
[theorem] \label{thm:main} There is a nonnegative density \(\rho\) on \(\R^3\) such that \[ \int_{\R^3}\rho(x)\dd x=1,\qquad \rho\in C_c^\infty(\R^3),\qquad \sqrt{\rho}\in C_c^\infty(\R^3), \] with the following properties. For \(\mu=\rho\dd x\), the value \(\E(\mu)\) is finite and is attained by a coupling in \(\Pi(\mu,\mu,\mu)\), but every pair of Borel maps \(T_2,T_3:\R^3\to\R^3\) satisfying \((T_2)_\#\mu=(T_3)_\#\mu=\mu\) obeys \[ \int_{\R^3}c\bigl(x,T_2(x),T_3(x)\bigr)\dd\mu(x)>\E(\mu). \] The inequality permits the left-hand side to be infinite.
==================
# FAMILY 374: Sharp one-third stability of Brenier maps
SCOPE: The formalization proves one-third Hölder stability of Brenier maps from the uniform measure on a compact convex body with nonempty interior in $\mathbb R^d$, for every $d\ge2$. For targets supported in one fixed nonempty compact set, the $L^2$ distance between the unique quadratic optimal maps is at most a constant times the one-third power of the targets' $2$-Wasserstein distance. The constant is uniform over those targets. It also proves optimality of the exponent: on a fixed cube, pairs of three-atom target measures violate every analogous bound with exponent greater than $1/3$. In particular, the conjectured uniform square-root estimate fails.
## CHALLENGE Brenier  targets=['OAI.Problem358.one_third_stability', 'OAI.Problem358.one_third_exponent_is_sharp'] defs=[]
theorem one_third_stability :
    ∀ (dimension : ℕ) (source container : Set (E dimension)),
      2 ≤ dimension → IsCompact source → Convex ℝ source → (interior source).Nonempty →
      IsCompact container → container.Nonempty →
      ∃ constant : ℝ, 0 ≤ constant ∧
        ∀ (first second : Measure (E dimension)),
          IsProbabilityMeasure first → IsProbabilityMeasure second →
          IsSupported first container → IsSupported second container →
          ∃ firstMap secondMap : E dimension → E dimension,
            IsUniqueQuadraticOptimalMap (uniformMeasure source) first firstMap ∧
            IsUniqueQuadraticOptimalMap (uniformMeasure source) second secondMap ∧
            mapL2Dist (uniformMeasure source) firstMap secondMap ≤
              constant * Real.rpow (wasserstein2 first second) (1 / 3 : ℝ) := by
  sorry
theorem one_third_exponent_is_sharp :
    ∀ (dimension : ℕ), 2 ≤ dimension → ∀ exponent : ℝ, (1 / 3 : ℝ) < exponent →
      ∀ constant : ℝ, 0 < constant →
        ∃ (first second : Measure (E dimension)) (firstMap secondMap : E dimension → E dimension),
          IsProbabilityMeasure first ∧ IsProbabilityMeasure second ∧
          IsSupported first (cube dimension) ∧ IsSupported second (cube dimension) ∧
          HasExactlyThreeAtoms first (cube dimension) ∧
          HasExactlyThreeAtoms second (cube dimension) ∧
          first ≠ second ∧
          IsUniqueQuadraticOptimalMap (uniformMeasure (cube dimension)) first firstMap ∧
          IsUniqueQuadraticOptimalMap (uniformMeasure (cube dimension)) second secondMap ∧
          0 < wasserstein2 first second ∧
          constant * Real.rpow (wasserstein2 first second) exponent <
            mapL2Dist (uniformMeasure (cube dimension)) firstMap secondMap := by
  sorry
end Problem358
end
DEFS(12): abbrev E, def uniformMeasure, def IsSupported, def IsCoupling, def quadraticPlanCost, def wasserstein2, def graphPlan, def IsQuadraticOptimalMap, def IsUniqueQuadraticOptimalMap, def mapL2Dist, def cube, def HasExactlyThreeAtoms
## PAPER Sharp-One-Third-Stability-of-Brenier-Maps-September-25-2026
ABSTRACT: For the uniform probability measure \(\rho\) on a compact convex body in \(\R^d\), \(d\ge2\), quadratic optimal transport maps are one-third H\"older continuous in \(L^2(\rho)\) with respect to the target's \(2\)-Wasserstein distance. The constant is uniform over all targets supported in a fixed compact set, and the exponent is optimal. A three-atom family on a fixed cube disproves Letrouit's conjectured uniform square-root estimate.
[theorem] \label{main:stability} For every \(K,Y\) as above there is a finite constant \(C(K,Y)\) such that \[ \|T_\mu-T_\nu\|_{L^2(\rho)} \le C(K,Y)\,W_2(\mu,\nu)^{1/3} \qquad\bigl(\mu,\nu\in\Prob(Y)\bigr). \] The targets may be atomic, singular, or absolutely continuous. The exponent \(1/3\) cannot be replaced by any larger exponent in general, even for \(K=Y=[-1,1]^d\) and targets with exactly three atoms.
==================
# FAMILY 376: Universal computation in forced Navier–Stokes flows
SCOPE: The formalization realizes finite families of prescribed positive diagonal maps on coding sheets by smooth incompressible flows on a flat three-torus. At every positive computable viscosity, it supplies a solution starting from rest with zero pressure and a force that is divergence free, has spatial mean zero, and is one-periodic from time zero. Each map acts on every point of its source sheet, and the construction provides effective bounds for all mixed derivatives. This selected statement covers the sheet programs. The paper's fixed-particle halting detector and its reciprocal maps on solid boxes are outside its scope. The formalization proves that a fluid particle can detect arbitrary finite-machine halting using alternating-coordinate memory in smooth incompressible Navier–Stokes flows whose velocity and force decay faster than every inverse power of time, including every mixed deriv
## CHALLENGE SolenoidalSheetPrograms  targets=['OAI.Solenoidal.sheet_theorem'] defs=[]
theorem sheet_theorem {N : ℕ} (D : SheetData N) (ν : ℝ)
    (hν : 0 < ν) (hνcomp : ComputableReal ν) :
    ∃ f u : Field, ∃ X : ℝ → Space → Space,
      SpatiallyPeriodic f ∧ SpatiallyPeriodic u ∧
      Smooth f ∧ Smooth u ∧ Effective f ∧
      MeanZero f ∧ DivergenceFree f ∧ OnePeriodic f ∧
      ClassicalSolution ν f u (fun _ _ => 0) ∧
      (∀ v : Field, ∀ p : Pressure, ClassicalSolution ν f v p →
        ∀ t, 0 ≤ t → ∀ x, v t x = u t x ∧ p t x = 0) ∧
      MaterialFlow u X ∧
      (∀ i : Fin N, ∀ y ∈ (D.source i).carrier,
        toTorus (X 1 (sheet y)) =
          toTorus (sheet (diagonalMap (D.source i) (D.target i) (D.ratio i) y))) ∧
      IntegerCollars u ∧ (∀ t x, advection u t x = 0) ∧
      EffectiveBounds f ∧ EffectiveBounds u ∧
      (N = 0 → f = 0 ∧ u = 0) := by
  sorry
end Solenoidal
end
DEFS(42): abbrev Plane, abbrev Space, abbrev SpaceTime, abbrev Field, abbrev Pressure, abbrev Torus, def toTorus, def sheet, structure Rectangle, def carrier, def center, def halfWidth, def inCodingSquare, def SeparatelySeparated, def diagonalMap, structure SheetData, def deck, def SpatiallyPeriodic, def fundamentalCell, def basis, def spatialPartial, def timePartial, def divergence, def laplacian, def advection, def gradient, def DivergenceFree, def MeanZero, def Smooth, def OnePeriodic
## CHALLENGE NavierStokesAlternating  targets=['OAI.AlternatingNS.alternating'] defs=[]
theorem alternating (ν : ℝ) (hν : 0 < ν) (hc : ComputableReal ν) :
    AlternatingConclusion ν := by
  sorry
end AlternatingNS
DEFS(56): abbrev Rule, abbrev Machine, def states, def alphabet, def initialState, def haltingStates, def table, def instruction, def WellFormed, def ValidInput, structure Configuration, def isHalting, def initial, def step, def run, def Halts, abbrev Space, abbrev Field, abbrev Velocity, abbrev Pressure, abbrev MultiIndex, def e, def dx, def dt, def spatial, def mixed, def div, def grad, def laplacian, def advection
## CHALLENGE NavierStokesVelocity  targets=['OAI.VelocityDetection.main_result'] defs=[]
theorem main_result :
    ∃ B : ℕ, 0 < B ∧
      (∀ s : ℝ, |deriv (deriv SmoothBump.profile) s| ≤ (B:ℝ)) ∧
    ∀ (ν : ℝ), 0 < ν → ComputableReal ν →
    ∀ (b N : ℕ) [NeZero b] [NeZero N]
      (M : TM0.Machine (Fin b) (Fin N)) (w : List (Fin b)),
    ∃ (Ftor Fcyl : ℝ → VectorField 3),
      (compile B M w).Represents .torus Ftor ∧
      (compile B M w).Represents .cylinder Fcyl ∧
      (ContDiff ℝ ∞ (uncurry (Ftor ν)) ∧
        (∀ t, FactorsThrough (Ftor ν t) PeriodicSpace.cover) ∧
        (∃ K : Set (Coord 2), IsCompact K ∧ (∀ X ∈ K, ∀ i, X i ∈ Ioo (0:ℝ) 1) ∧
          ∀ t X, PeriodicSpace.cover (horizontal X) ∉ PeriodicSpace.cover '' K → Ftor ν t X = 0) ∧
        (∀ T d, ∃ C : ℝ, 0 ≤ C ∧ ∀ t ∈ Icc (0:ℝ) T, ∀ X,
          ‖iteratedFDeriv ℝ d (uncurry (Ftor ν)) (t,X)‖ ≤ C) ∧
        ∃ u : VectorField 3,
          ContDiff ℝ ∞ (uncurry u) ∧ TorusClass.ComparisonClass u (fun _ _ => 0) ∧
          NavierStokes ν u (fun _ _ => 0) (Ftor ν) ∧
          (Observation.torusEvent u ↔ (TM0.eval M w).Dom) ∧
          ∀ (v : VectorField 3) (p : ScalarField 3), TorusClass.ComparisonClass v p →
            NavierStokes ν v p (Ftor ν) →
            ∀ t ≥ 0, (∀ X, v t X = u t X) ∧ (∀ X, p t X = 0)) ∧
      (ContDiff ℝ ∞ (uncurry (Fcyl ν)) ∧
        UniformDerivatives.Bounded (fun _ : Unit => uncurry (Fcyl ν)) ∧
        (∀ t X z, Fcyl ν t (update X 2 z) = Fcyl ν t X) ∧
        (∀ T : ℝ, ∃ K : Set (Coord 2), IsCompact K ∧ ∀ t ∈ Icc (0:ℝ) T,
          ∀ X : Coord 3, horizontal X ∉ K → Fcyl ν t X = 0) ∧
        ∃ u : VectorField 3,
          ContDiff ℝ ∞ (uncurry u) ∧
          Cylinder.ComparisonClass (fun t x => u t (Cylinder.join x)) (fun _ _ => 0) ∧
          NavierStokes ν u (fun _ _ => 0) (Fcyl ν) ∧
          (∀ t ≥ 0, (∀ x, 0 ≤ u t (Cylinder.join x) 2) ∧
            Integrable (fun x
DEFS(194): abbrev Coord, abbrev ScalarField, abbrev VectorField, theorem neZeroTwo, theorem neZeroThree, theorem neZeroFive, def spatialD, def timeD, def laplacian, def advection, def divergence, def NavierStokes, def horizontal, inductive Move, def update, structure Rule, structure Configuration, def applyRule, def address, def capacity, def lambda, def initialRadius, def radius, def join, def torusEvent, def upperHalfPlane, def planeMass, def planeEvent, abbrev step, def window
## CHALLENGE BalancedBoxRouting  targets=['OAI.BoxTransport.Routing.balanced_box_routing'] defs=[]
theorem balanced_box_routing
    (n : ℕ) (a b h k : Fin n → RationalSpace)
    (hh : ∀ i j, 0 < h i j) (hk : ∀ i j, 0 < k i j)
    (ha : Pairwise fun i j => Disjoint (solidBox (a i) (h i)) (solidBox (a j) (h j)))
    (hb : Pairwise fun i j => Disjoint (solidBox (b i) (k i)) (solidBox (b j) (k j)))
    (hvol : ∀ i, ∏ j : Fin 3, k i j / h i j = 1) :
    ∃ U : Field, ∃ Φ : ℝ → Space → Space,
      AdmissibleField U ∧ IsGlobalFlow U Φ ∧ Delivers a b h k Φ := by
  sorry
end BoxTransport.Routing
DEFS(24): abbrev Space, abbrev RationalSpace, abbrev SpaceTime, abbrev RationalSpaceTime, abbrev Field, abbrev Axis, def coordinateVector, def coordinateDirection, def realPoint, def realSpaceTime, def realBox, def solidBox, def prescribedAffine, def mixedDerivative, abbrev RationalCode, def rationalValue, abbrev RationalPointCode, def codeSpaceTime, abbrev EvaluationRequest, def Effective, def spatialDivergence, def AdmissibleField, def IsGlobalFlow, def Delivers
## CHALLENGE BalancedThreeStack  targets=['OAI.BalancedTransport.balanced_three_stack_realization'] defs=[]
theorem balanced_three_stack_realization :
    ∃ U f₀ f₁ : Family Velocity,
    ∃ X : Family MaterialFlow,
    ∃ repeated : FiniteMachine → Velocity,
      EffectiveFamily U ∧ EffectiveFamily f₀ ∧ EffectiveFamily f₁ ∧
      (∀ M, Function.Periodic (repeated M) 1) ∧
      ∀ (M : FiniteMachine) (w : Input M),
        Smooth (U M w) ∧ Smooth (f₀ M w) ∧ Smooth (f₁ M w) ∧
        f₀ M w = inertialCoefficient (U M w) ∧
        f₁ M w = viscousCoefficient (U M w) ∧
        CommonCompactSupport (U M w) (f₀ M w) (f₁ M w) ∧
        BoundedMixed (U M w) ∧
        PeriodicAfterOne (U M w) ∧
        (∀ t, 1 ≤ t → ∀ x, U M w t x = repeated M t x) ∧
        ComparisonClass (U M w) (fun _ _ => 0) ∧
        IsMaterialFlow (U M w) (X M w) ∧
        ((∃ t : ℝ, 0 ≤ t ∧ X M w t fixedLabel ∈ observer) ↔ Halts M w) ∧
        ∀ ν : ℝ, 0 < ν →
          let f := affineForce (f₀ M w) (f₁ M w) ν
          ZeroDataSolution ν f (U M w) (fun _ _ => 0) ∧
          Smooth f ∧ BoundedMixed f ∧ PeriodicAfterOne f ∧
          UniqueInComparison ν f (U M w) ∧
          (ComputableReal ν → EffectiveFieldIn ∅ f) ∧
          (∀ name : ℕ → ℚ, RealName name ν → EffectiveFieldIn {nameOracle name} f) := by
  sorry
end BalancedTransport
DEFS(50): inductive Direction, structure Transition, structure FiniteMachine, abbrev Input, structure TapeConfiguration, def initialConfiguration, def machineStep, def Halts, def Recorder.Direction.number, def FiniteMachine.code, def inputCode, abbrev Space, abbrev Field, abbrev Velocity, abbrev Pressure, abbrev Family, abbrev MaterialFlow, abbrev MultiIndex, abbrev RationalPoint, def timeD, def spaceD, def mixedD, def spatialD, def Smooth, def BoundedMixed, def CH, def C1L2, def div, def laplacian, def convection
## CHALLENGE ForcedNavierStokesComputation  targets=['OAI.BalancedTransport.balanced_three_stack_realization'] defs=[]
theorem balanced_three_stack_realization :
    ∃ U f₀ f₁ : Family Velocity,
    ∃ X : Family MaterialFlow,
    ∃ repeated : FiniteMachine → Velocity,
      EffectiveFamily U ∧ EffectiveFamily f₀ ∧ EffectiveFamily f₁ ∧
      (∀ M, Function.Periodic (repeated M) 1) ∧
      ∀ (M : FiniteMachine) (w : Input M),
        Smooth (U M w) ∧ Smooth (f₀ M w) ∧ Smooth (f₁ M w) ∧
        f₀ M w = inertialCoefficient (U M w) ∧
        f₁ M w = viscousCoefficient (U M w) ∧
        CommonCompactSupport (U M w) (f₀ M w) (f₁ M w) ∧
        BoundedMixed (U M w) ∧
        PeriodicAfterOne (U M w) ∧
        (∀ t, 1 ≤ t → ∀ x, U M w t x = repeated M t x) ∧
        ComparisonClass (U M w) (fun _ _ => 0) ∧
        IsMaterialFlow (U M w) (X M w) ∧
        ((∃ t : ℝ, 0 ≤ t ∧ X M w t fixedLabel ∈ observer) ↔ Halts M w) ∧
        ∀ ν : ℝ, 0 < ν →
          let f := affineForce (f₀ M w) (f₁ M w) ν
          ZeroDataSolution ν f (U M w) (fun _ _ => 0) ∧
          Smooth f ∧ BoundedMixed f ∧ PeriodicAfterOne f ∧
          UniqueInComparison ν f (U M w) ∧
          (ComputableReal ν → EffectiveFieldIn ∅ f) ∧
          (∀ name : ℕ → ℚ, RealName name ν → EffectiveFieldIn {nameOracle name} f) := by
  sorry
DEFS(50): inductive Direction, structure Transition, structure FiniteMachine, abbrev Input, structure TapeConfiguration, def initialConfiguration, def machineStep, def Halts, def Recorder.Direction.number, def FiniteMachine.code, def inputCode, abbrev Space, abbrev Field, abbrev Velocity, abbrev Pressure, abbrev Family, abbrev MaterialFlow, abbrev MultiIndex, abbrev RationalPoint, def timeD, def spaceD, def mixedD, def spatialD, def Smooth, def BoundedMixed, def CH, def C1L2, def div, def laplacian, def convection
## PAPER Geometric-Programs-for-Solenoidal-Forcing-September-27-2026
ABSTRACT: We construct smooth solenoidal mean-zero forces, periodic from time zero, for which a fixed particle on a flat three-torus reaches a fixed open strip exactly when a given machine halts. The initial fluid velocity and the pressure are zero. We also realize positive diagonal maps on coding sheets by incompressible shears, with explicit normal compensation for changes of planar area, and reciprocal maps on whole boxes of positive thickness. Complete local inverses, initialization rules, and intermediate trajectory bounds connect these geometric constructions to finite computations.
[theorem[Periodic initialization]] \label{sv:periodic-theorem} Fix a computable viscosity $\nu>0$. From a deterministic one-tape machine, with head moves in $\{-1,0,1\}$, and a finite input, one can effectively construct a smooth force on $\mathbb T_1^3$ such that: \begin{enumerate}[label=(\roman*),itemsep=2pt] \item The force is divergence free, has zero spatial mean, and is one-periodic from time zero. Equation~\eqref{sv:NS} has a global smooth solution with pressure zero, unique in the stated classical class. \item The velocity is one-periodic, vanishes near every integer time, has zero instantaneous self-advection, and has uniformly bounded kinetic energy. Every mixed derivative of force and velocity is globally bounded. 
## PAPER Computation-under-Rapidly-Vanishing-Navier-Stokes-Forcing-September-27-2026
ABSTRACT: At any fixed positive computable viscosity, smooth forces can make a fixed fluid particle detect the halting of an arbitrary machine, starting from rest, while every mixed derivative of the force and velocity decreases faster than every inverse power of time. We give three complete memory constructions: compact moving curls, alternating fractional coordinates, and a periodic lattice on the flat three-torus. Each machine step takes one unit of physical time. The constructions retain earlier records at separated spatial scales and use an exact open detector with a shrinking signal.
[theorem[Compact support and rapid decay]] \label{thm:rapid} Fix a positive computable viscosity $\nu$. From a deterministic Turing machine $M$ and a finite input $w$ one can effectively construct a smooth force on $[0,\infty)\times\R^3$, supported for all times in the fixed compact set \[ K=[-2,1]\times[-1,2]\times[-1,1], \] such that, for every pair of nonnegative integers $J,l$ and spatial multi-index $\alpha$, \begin{equation} \sup_{t\geq0,\,x\in\R^3} (1+t)^J\bigl|\partial_t^l\partial_x^\alpha f(t,x)\bigr|<\infty. \label{eq:rapid-force-bound} \end{equation} The Navier--Stokes equation with this force and zero initial velocity has an explicit global smooth solution, unique in the finite-interval class \eqref{eq:energy-class}. Its 
## PAPER Velocity-Field-Detection-of-Computation-in-Forced-Navier-Stokes-Flows-September-27-2026
ABSTRACT: We construct smooth forces for three-dimensional incompressible Navier--Stokes flow, from rest at any fixed positive computable viscosity, whose velocity field detects whether a prescribed machine halts. On the unit flat torus, a pointwise test of the third velocity component uses successively shorter stirring intervals in a fixed spatial region. On $\R^2\times\T$, an integral test uses an expanding array of translation regions and a force with globally bounded mixed derivatives. The vertical velocity solves an advection--diffusion equation: short bursts control its pointwise error in the first construction, and a moving cutoff controls the total escaped mass in the second.
[theorem] \label{thm:main} For each positive computable $\nu$, a machine and a finite input effectively determine each of the following two forces. \begin{enumerate} \item On $\T^3$, a smooth force has a unique global smooth solution in the torus class above, with pressure zero, for which \eqref{eq:torus-event} holds exactly when the machine halts. The force is supported in $K\times\T$ for a compact $K\subset(0,1)^2$ independent of time. Its derivatives are bounded on every finite time interval; their bounds may grow with that interval. \item On $\R^2\times\T$, a smooth force and all its mixed derivatives are globally bounded. On each finite time interval its horizontal support is compact. It has a un
## PAPER Incompressible-Box-Transport-and-Finite-Computation-September-27-2026
ABSTRACT: We realize finite positive diagonal affine maps of determinant one by effective smooth incompressible flows on neighborhoods of entire closed rational solid boxes. The source and target families are each disjoint, but may overlap each other. The construction uses localized curls, evacuation to storage and obstacle detours. A balanced three-stack recorder then assigns every machine and finite input a smooth Navier--Stokes force with one compact spatial support, periodic after a loading interval, at any fixed positive computable viscosity. The fluid starts at rest, and one fixed particle enters one fixed open cube exactly when the machine halts. Further constructions give fixed torus charts, p
[proposition[Projection on a flat torus]] \label{prop:projection-l2} An effective smooth mean-zero force $g$ on $\T_L^3$ has an effective mean-zero potential $\phi$ satisfying $\Delta\phi=\operatorname{div}g$. Replacing $(g,p)$ by $(g-\nabla\phi,p-\phi)$ preserves velocity and makes the force solenoidal. Uniform mixed-derivative bounds, temporal $L^2$ bounds of their spatial suprema, and separately imposed time periodicity, eventual stationarity, or orderwise decay bounds are preserved.
==================
# FAMILY 378: The Exponential Time Hypothesis is False
SCOPE: For fixed $k\ge2$, Lean proves that a deterministic machine exactly counts satisfying assignments of a canonically encoded $k$-CNF on $n$ variables in time $(L+1)^{O_k(1)}2^{O_k(n(\log\log n)^2/\sqrt{\log n})}$, where $L$ is the encoding's bit length. At every step, the machine has visited at most $(L+1)^{O_k(1)}$ tape cells in total. For $m$ clauses, the October 25 manuscript gives the sharper time bound $(n+m)^{O_k(1)}2^{O_k(n\log\log n/\sqrt{\log n})}$. When $m\le Dn$ for fixed $D>0$, this improves to $(n+m)^{O_{k,D}(1)}2^{O_{k,D}(n/\sqrt{\log n})}$.
## CHALLENGE SubexponentialSAT  targets=['OAI.Algorithms.SubexponentialSAT.SqrtLogSpace.exact_count_and_sat'] defs=[]
theorem exact_count_and_sat (k : ℕ) (hk : 2 ≤ k) :
    ∃ (machine : Computation.PrimitiveMachine)
      (countTape answerTape : Fin machine.tapeCount)
      (C A S : ℝ) (d e : ℕ),
      0 < C ∧ 0 < A ∧ 0 < S ∧ 0 < d ∧ 0 < e ∧
      ∀ (n : ℕ) (F : SAT.CNF (Fin n)), SAT.WidthAtMost k F →
        ∃ (time : ℕ) (final : LocatedCfg machine),
          Computation.Trace (locatedStep machine) time
            (locatedInit machine (Encoding.encodeCNF F)) final ∧
          final.config.tapes countTape =
            Turing.Tape.mk₁ ((countWord (SAT.count F)).map some) ∧
          final.config.tapes answerTape =
            Turing.Tape.mk₁ [some (decide (0 < SAT.count F))] ∧
          final.config.state = Sum.inl (decide (0 < SAT.count F)) ∧
          BinaryArithmetic.toNat (countWord (SAT.count F)) = SAT.count F ∧
          (countWord (SAT.count F)).length ≤ n + 1 ∧
          (time : ℝ) ≤ OAI.Algorithms.SubexponentialSAT.SqrtLog.Statement.runtimeBound C A d
            (Encoding.formulaBitLength F) n ∧
          ∀ (prefixSteps : ℕ) (intermediate : LocatedCfg machine),
            prefixSteps ≤ time →
            Computation.Trace (locatedStep machine) prefixSteps
              (locatedInit machine (Encoding.encodeCNF F)) intermediate →
            (visitedSpace intermediate : ℝ) ≤
              S * ((Encoding.formulaBitLength F : ℝ) + 1) ^ e := by
  sorry
DEFS(35): def bitVal, def toNat, abbrev Assignment, structure Literal, abbrev Clause, abbrev CNF, def Literal.eval, def Clause.eval, def CNF.eval, def WidthAtMost, def satisfyingAssignments, def count, def encodeNat, def frame, def encodeList, def literalCode, def clauseNumbers, def cnfNumbers, def encodeCNFBody, def encodeCNF, def formulaBitLength, inductive Trace, structure PrimitiveMachine, structure Cfg, def step, def init, def runtimeScale, def runtimeBound, def countWord, structure LocatedCfg
## PAPER The-Exponential-Time-Hypothesis-is-False-October-25-2026
ABSTRACT: We give a deterministic algorithm for exactly counting the satisfying assignments of an arbitrary $k$-CNF formula. For every fixed $k\ge2$, on a formula with $n$ variables and $m$ clauses, our algorithm uses $\poly_k(n,m)$ space and runs in time $(n+m)^{O_k(1)}2^{\,n/(\log n)^{\frac12+o(1)}}$. Our algorithm refutes the Exponential Time Hypothesis (ETH), which postulates that deciding $3$-SAT on $n$ variables requires $2^{\Omega(n)}$ time in the worst case.
[theorem] \label{thm:main} For each fixed $k\ge2$, there exists a deterministic algorithm that, given a $k$-CNF $F$ on $n\ge20$ declared variables with $m$ clauses, computes $\#F$ as defined in \eqref{eq:solution-count} in \[ (n+m)^{O_k(1)}2^{O_k(n\log\log n/\sqrt{\log n})} \] bit operations and $(n+m)^{O_k(1)}$ bits of space. For each fixed $D>0$, its running time on inputs with $m\le Dn$ is \[ (n+m)^{O_{k,D}(1)}2^{O_{k,D}(n/\sqrt{\log n})}. \]
==================
