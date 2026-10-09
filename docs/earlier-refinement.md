# A concrete refinement to investigate in family 127

**Update, 9 October 2026:** a stronger derivation now gives a uniform constant **3.83**. See [the new proof](../127-improved-bound.md) and [literature comparison](literature-review.md). The note below preserves the initial absolute-deviation refinement that motivated the work.

This is an inference from the published argument, conditional on its operator lemmas. It is not an independently audited proof of the main theorem or a claim of research novelty. The starting point is [OpenAI's manuscript](https://github.com/openai/math/blob/main/preprints/Average-Sensitivity-of-Polynomial-Threshold-Functions-September-25-2026/main.pdf), Lemma 2 and Section 5, equations (13)–(17). A [local copy](https://github.com/openai/math/blob/main/preprints/Average-Sensitivity-of-Polynomial-Threshold-Functions-September-25-2026/main.pdf) is retained.

Let $I(f)$ denote average sensitivity. The coupling lemma has equal-law variables $U,V$, common mean $m$, and $V-U\le a$. Its final Cauchy–Schwarz step can be omitted. The preceding inequalities already give

\[
\mathbb E(U-V)^2\le 8a\,\mathbb E|U-m|.
\]

Applying the manuscript's remaining comparison with $a=d$ and $U\sim\operatorname{Bin}(n,1/2)$ gives

\[
I(f)\le
\min\left\{n,\;16d\,\mathbb E|B_n-n/2|\right\},
\qquad B_n\sim\operatorname{Bin}(n,1/2).
\]

The binomial absolute deviation has the exact form

\[
\mathbb E|B_n-n/2|
=\frac{n}{2^n}\binom{n-1}{\lfloor(n-1)/2\rfloor}.
\]

Consequently the coefficient multiplying $d\sqrt n$ approaches

\[
\frac{16}{\sqrt{2\pi}}=6.38307648\ldots
\]

as $n\to\infty$, compared with 8 in the stated bound. This asymptotic coefficient is not an assertion that exactly 6.383 works at every finite dimension. For example, the deviation expression gives coefficients 6.7082 at $n=5$, 6.3671 at $n=100$, and 6.3815 at $n=1000$. The trivial bound $I(f)\le n$ can be stronger in some parameter ranges.

The formula was checked against the direct binomial sum using exact rational arithmetic at dimensions 1, 2, 5, 10, 50, 100, and 1000. This checks the numerical identity in those instances; the combinatorial identity and asymptotic follow analytically. It does not check the operator lemmas.

An initial optimization experiment is the following relaxation. Let $\mu_u=2^{-n}\binom nu$. Maximize

\[
C_{n,d}=\max_{p}\sum_{u,v=0}^n (u-v)^2p_{uv}
\]

subject to

\[
p_{uv}\ge0,\quad
\sum_vp_{uv}=\mu_u,\quad
\sum_up_{uv}=\mu_v,\quad
p_{uv}=0\text{ when }v-u>d.
\]

The manuscript's coupling is feasible, so its operator comparison would yield $I(f)\le\min(n,2C_{n,d})$. The optimization above is an upper-bound relaxation: its extremizers need not arise from polynomial threshold functions. A floating-point optimum is exploratory evidence; rigorous upper bounds need dual feasible certificates with checked arithmetic. This experiment has not yet been run.

The elementary absolute-deviation refinement is a useful starting baseline. A substantive contribution would require further improvement, a useful parameter regime, or a characterization of extremal behavior, followed by a broader novelty check. Known counterexamples to the old exact-maximizer conjecture are supplied by [Kim, Maldonado and Wellens](https://arxiv.org/abs/1709.06650) and [Chapman](https://arxiv.org/abs/2108.02288).
