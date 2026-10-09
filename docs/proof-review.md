# Separate proof audit of the submission draft

Reviewed against the earlier five-page manuscript on 9 October 2026. Its analytic proof and bibliography are retained unchanged in the current six-page `paper/main.tex`, whose PDF and source match the published Zenodo record. This was a fresh adversarial audit by Codex, reconstructing the argument from its assumptions and the original source. It is AI review, not an external referee report, and does not claim independent confirmation of priority.

**Mathematical finding:** no gap was identified in the analytic derivation of the uniform coefficient $383/100$. The complete grading-to-coupling argument is included in the draft and explicitly attributed to OpenAI. The new probability step and the finite-dimension coefficient extraction are proved in the draft.

| Item challenged | Resolution |
| --- | --- |
| Could the new coupling lemma accidentally require independence or a lower displacement bound? | It uses equality of marginal expectations of an integrable potential. Only $V-U\le a$ is required; negative displacements remain unrestricted. |
| Is the balancing of positive and negative increments valid? | The potential has quadratic growth and the marginals have finite second moment, so both expectations exist and agree. |
| Does the factor four apply on the correct event? | On $V-U<0$ the squared displacement is at most four times the decreasing potential increment. On the positive event the increment is controlled by the upper displacement bound. |
| Is the $a^2$ addition valid at every outcome? | The positive displacement lies in $(0,a]$; its restricted second moment is at most $a^2$. |
| Does the alternative $5ab$ bound use an unjustified equality? | Equal means imply $\mathbb E D_+=\mathbb E|D|/2\le b$, making the positive second moment at most $ab$. |
| Is the weighted grading defined for every polynomial? | Cube multilinearization preserves values and degree. A small positive shift removes zeros while preserving the chosen sign convention. The resulting positive weight gives an invertible multiplier. |
| Could coordinate multiplication jump more than one grade? | It raises polynomial degree by at most one; self-adjointness gives the reverse triangular zero blocks. |
| Is the commutator norm estimate justified? | The grading-parity average retains only adjacent blocks; conjugation by grading phases converts it to the commutator without changing its norm. |
| Are edges counted with the same normalization as average sensitivity? | The draft uses ordered neighboring pairs; dividing by $2^n$ gives the sum of flip probabilities in the theorem. |
| Are both constructed marginals really binomial? | Row and column sums of squared blocks of a unitary are the corresponding projection dimensions, namely $\binom nk$. |
| Is the coupling support inequality reversed? | $R+S\ge n-d$ becomes $V-U\le d$ under $U=S,V=n-R$. |
| Does the scalar second moment equal the normalized anticommutator energy? | Orthogonal blocks have coefficient $r+s-n$, yielding exactly the stated second-moment sum. |
| Could the result fail when $d$ grows with $n$ or $n$ is small? | The exact case split uses the trivial bound when $n\le C^2d^2$. Its complementary branch forces $n\ge15$. No fixed-degree assumption is used. |
| Is the central-binomial inequality just numerical evidence? | It is proved by induction using a polynomial identity whose difference is $k\ge0$. |
| Is the comparison $K+2/C<C$ affected by rounding? | The draft gives the exact positive rational certificate $524329931/1100000000$. |
| Does the proof rely on a floating-point solver? | No. LPs and matrix experiments are supplemental; neither appears as an assumption in the theorem proof. |

**Bibliographic correction made during review:** the Kabanets–Kane–Lu STOC 2017 pagination was verified against the public DOI metadata and corrected to 615–628.

**Priority finding:** the review did not locate a published all-degree, all-dimension bound with a coefficient at most 3.83. The October 7 Grebennikov preprint was checked explicitly: its rational-function and nonvanishing-indicator theorems have different assumptions and influence conventions. The draft claims an improvement over OpenAI's coefficient 8; it does not claim an optimal constant, an exhaustive census, or an externally confirmed priority date.

**Validation:** exact checks of the numerical certificate and binomial identities passed; 14,584 nontrivial dimension-degree pairs and 1,986,416 pairs covered by the trivial branch were checked through dimension 2000. Eight coupling LPs and 63 weighted-gradings checks passed. These finite checks support the audit; the universal claims rest on the analytic proof.
