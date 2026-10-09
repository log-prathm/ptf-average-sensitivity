# Audit of the 3.83 derivation

The target is a smaller universal coefficient in family 127, retaining the uniform Boolean distribution, arbitrary real threshold polynomial, all dimensions and degrees, and the positive sign convention at zero.

| Requirement | Evidence | Finding |
| --- | --- | --- |
| Improved coefficient is genuinely below 8 | $383/100<8$ exactly | Proved |
| Coupling estimate uses no independence assumption | Equal marginal expectations balance the positive and negative increments of an integrable potential | Proved in the probability lemma |
| Large negative displacements remain allowed | Their second moment is bounded by the balanced potential increment; only positive displacement is bounded by $a$ | Proved |
| Coupling implies a bound for the same threshold functions | Original Lemma 3 and Section 5 supply $I(f)\le2\mathbb E(U-V)^2$, binomial marginals, and $V-U\le d$ | Checked in the original PDF |
| Both coupling marginals are binomial | Grading blocks have dimensions $\binom nr$; multiplication by a sign is unitary; binomial reflection preserves the law | Checked |
| Coupling support constraint points in the correct direction | $R+S\ge n-d$ becomes $V-U\le d$ for $U=S,V=n-R$ | Checked |
| Polynomial zeros do not invalidate the argument | A sufficiently small positive constant perturbation preserves negative signs and maps zeros to the required positive sign | Checked |
| Nonmultilinear polynomials remain covered | Multilinear reduction by $x_i^2=1$ preserves cube values without raising degree | Checked |
| Coefficient holds at small dimensions and high degree | $n\le C^2d^2$ is covered by $I(f)\le n$ | Proved |
| Coefficient holds in the remaining parameter range | $n\ge15$, central-binomial induction, and $4\sqrt{15/22}+2/C<C$ | Proved |
| Numerical constants do not rely on floating point | Exact rational certificate $524329931/1100000000>0$ | Verified |
| Finite checks exercise the actual inequalities | Exact binomial sums, induction identities, rational interval inequalities, and dimension-degree cases | Passed; see verification output |
| Numerical source-framework check | 8 coupling LPs and 63 weighted gradings, including forbidden blocks and energy identities | Passed; supplemental only |
| Lower than known comparable literature bounds | Primary-source comparison in 127-literature.md identifies 8 as the best located universal coefficient | Supported by the documented review |
| Lower than every result present anywhere in the literature | Search absence cannot rule out an unindexed competing theorem | **Not established exhaustively** |

The source's edge-recovery lemma was inspected rather than assumed from the headline theorem. Its argument bounds each off-diagonal grading entry by $1/2$, compares distance-weighted energy to the fixed grading energy, bounds the total neighbor deficit by twice the diagonal energy, and then detects that diagonal energy in the anticommutator. The resulting factor two agrees with the normalization used here. The mathematical dependency is explicitly attributed in the new proof.

The universal theorem has an informal analytic proof; the numerical checks do not substitute for that proof. No external reviewer or Lean checker has certified the new derivation. The remaining broad uncertainty concerns literature completeness and priority, rather than an unverified floating-point constant.
