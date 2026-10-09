# Literature comparison for the uniform sensitivity constant

Checked: **9 October 2026**. The theorem under comparison is

\[
 \operatorname{AS}(f)\le C\,d\sqrt n
\]

for every real polynomial threshold function on the **uniform Boolean cube**, uniformly over every dimension $n\ge1$ and degree $1\le d\le n$. The constant must be independent of both parameters. This matches family 127's stated scope. Gaussian bounds, fixed-degree bounds with dimension-dependent logarithms, lower bounds, and stronger estimates on special classes do not supply a smaller constant for this theorem.

| Primary source | Result relevant to the comparison | Does it provide a smaller uniform constant? |
| --- | --- | --- |
| [Harsha, Klivans, Meka, 2009 / Theory of Computing 2014](https://arxiv.org/abs/0909.5175) | Upper bounds with dimension exponent larger than $1/2$ for fixed degree; an alternative recursive estimate | No all-degree, all-dimension $C d\sqrt n$ bound |
| [Diakonikolas, Raghavendra, Servedio, Tan, 2009 / SIAM J. Computing 2014](https://arxiv.org/abs/0909.5011) | Early Boolean sensitivity bounds with additional degree and dimension factors; Gaussian results and learning applications | No smaller constant for the theorem under comparison |
| [Kane, 2012 / Computational Complexity 2014](https://arxiv.org/abs/1210.1283) | $\sqrt n(\log n)^{O(d\log d)}2^{O(d^2\log d)}$ | No: logarithmic and nonlinear degree factors remain |
| [Kabanets, Kane, Lu, STOC 2017](https://www.cs.sfu.ca/~kabanets/Research/PTF-restriction.html) | Another proof of Kane's dimension-exponent bound using a polynomial restriction lemma | The logarithmic factors remain |
| [Moore and Russell, 2014](https://arxiv.org/abs/1408.5425) | An average-case sensitivity bound after random rotation | Random-rotation averaging differs from a bound for every fixed polynomial |
| [Kim, Maldonado, Wellens, 2017](https://arxiv.org/abs/1709.06650) | Quadratic counterexamples to exact symmetric extremality; bounds for restricted support graphs | The upper bounds concern special classes |
| [Chapman, SODA 2018; arXiv upload 2021](https://arxiv.org/abs/2108.02288) | Counterexamples to the exact-maximizer conjecture | A constraint on candidate extremizers, not a stronger universal upper bound |
| [Chang, Slote, Volberg, Zhang, April 2026, version 2](https://arxiv.org/html/2604.08095v2) | Polylogarithmic bounds on $\mathbb E\sqrt{s_f(X)}$, the Boolean surface area | Different moment. Its introduction still identifies Kane's result as the strongest step toward the weaker influence conjectures |
| [Tseng, Volberg, June 2026, version 2](https://arxiv.org/html/2606.16004v2) | Bounds on sensitivity moments. Section 2.5, equation (11), retains a factor $(\log n)^{C d\log d}$ at moment order one | No smaller uniform $C$ |
| [Pavlov, May 2026](https://arxiv.org/html/2605.01637v1) | An influence-dependent Walsh invariant and finite ternary-threshold computations | No universal degree-versus-influence theorem of the target form |
| [Grebennikov, October 7, 2026, version 2](https://arxiv.org/html/2610.08708v2) | Influence bounds for bounded-degree rational functions and nonvanishing indicators; its update cites OpenAI's Gotsman–Linial proof | These are different classes. The paper explicitly states that its rational-function result does not imply the full Gotsman–Linial bound |
| [OpenAI, September 25 manuscript, released October 6, 2026](https://github.com/openai/math/blob/main/preprints/Average-Sensitivity-of-Polynomial-Threshold-Functions-September-25-2026/main.pdf) | $\operatorname{AS}(f)\le8d\sqrt n$ | **Best comparable numerical constant located: 8** |
| [This derivation](../127-improved-bound.md) | $\operatorname{AS}(f)\le(383/100)d\sqrt n$; exact deviation bound also supplied | 3.83 is below 8, under the same theorem assumptions |

The OpenAI [formalization scope](https://github.com/openai/math/blob/main/lean/docs/127.md) also states the constant 8 and distinguishes the uniform bound from the conjecture about exact extremizers. That page was read; its Lean proof library was not rebuilt.

The review included searches using the exact manuscript title, the Gotsman–Linial name, “average sensitivity”, “polynomial threshold”, “constant”, “improvement”, “OpenAI”, and combinations with 2026 and the proposed numerical constants. Searches for post-release improvements returned explanations and catalogues of the 8 bound, without locating a smaller comparable theorem. Primary sources above were used for the actual comparison; secondary catalogue pages were not treated as independent proofs.

Public arXiv API inventories were also queried and saved. The broad inventory, using `(all:"polynomial threshold" OR all:PTF) AND (all:sensitivity OR all:influence)`, returned all 30 reported matches, including unrelated uses of PTF. The first 100 of 150 matches for the Gotsman/title inventory were sorted newest first; its recent relevant entries agree with the primary papers checked above. These queries added the random-rotation and Banach-Butterfly papers to the review. [Kane's current publication list](https://cseweb.ucsd.edu/~dakane/papers.html) was also inspected for additional sensitivity results. None of these inventories is a complete census of the literature.

**Supported conclusion:** 3.83 improves every comparable bound identified in this review. The analytic proof establishes the mathematical improvement over 8. Literature searching does not prove that no unindexed competing result exists; an absolute priority claim is not established here. The new proof has not been externally peer reviewed or formally checked in Lean.

The subsequent citation review queried Semantic Scholar's citing-paper inventory for Kane's paper and received 51 entries, with no additional page. It also queried Crossref for 100 title matches. The October 7 Littlewood–Offord preprint was discovered through this citation search and checked in its revised version. Its real-valued influence is defined as a sum of squared changes, equal to four times our average sensitivity for a sign-valued function. Its nonvanishing-indicator theorem applies to $\mathbf1_{p\ne0}$, not arbitrary $\mathbf1_{p>0}$, so its numerical coefficient cannot be substituted into the target theorem. This check illustrates why matching function classes and normalizations is necessary.
