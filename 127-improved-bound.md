# A uniform 3.83 bound for polynomial threshold functions

Date: 9 October 2026. This is a research derivation extending family 127 of the OpenAI mathematics release. It has been checked here as an informal proof, with exact arithmetic for its numerical constants. It has not been independently reviewed or formalized in Lean. Attribution for the weighted-grading reduction belongs to [OpenAI's manuscript](https://github.com/openai/math/blob/main/preprints/Average-Sensitivity-of-Polynomial-Threshold-Functions-September-25-2026/main.pdf), Lemma 3 and Section 5. The probability estimate below supplies the improvement.

**Theorem.** Let $n\ge1$ and $0\le d\le n$ be integers. Let $p$ be a real polynomial of degree at most $d$, evaluated on $\{-1,1\}^n$, and put $f=\operatorname{sgn}p$ with $\operatorname{sgn}(0)=1$. Under the uniform distribution on the cube, define

\[
 I(f)=\sum_{i=1}^n\Pr\{f(X)\ne f(X^{\oplus i})\}.
\]

Then

\[
 \boxed{I(f)\le\frac{383}{100}\,d\sqrt n.}
\]

A more informative estimate, before choosing a single constant, is

\[
 I(f)\le\min\{n,\;8d\,b_n+2d^2,\;10d\,b_n\},
 \qquad
 b_n=\mathbb E|B_n-n/2|
 =\frac{n}{2^n}\binom{n-1}{\lfloor(n-1)/2\rfloor},
 \quad B_n\sim\operatorname{Bin}(n,1/2).
\]

In particular, for $d=o(\sqrt n)$ its coefficient is at most

\[
 \frac{8}{\sqrt{2\pi}}+o(1)=3.19153824\ldots+o(1).
\]

The comparison target is the all-degree, all-dimension bound $8d\sqrt n$ in the accompanying OpenAI manuscript. The literature review is in [127-literature.md](docs/literature-review.md). Smaller constants for restricted classes, such as linear thresholds, are different theorems.

**Probability lemma.** Suppose $U$ and $V$ have the same distribution, finite variance, common mean $m$, and $V-U\le a$ almost surely for some $a\ge0$. Set $b=\mathbb E|U-m|$. Then

\[
 \mathbb E(U-V)^2\le\min\{4ab+a^2,\;5ab\}.
\]

**Proof.** Write $D=V-U$ and choose

\[
 g(t)=\tfrac12(t-m)|t-m|=\int_m^t|z-m|\,dz.
\]

It is increasing and integrable under either marginal. For $u<v$,

\[
 \frac{(v-u)^2}{4}\le g(v)-g(u)
 \le\frac{v-u}{2}\bigl(|u-m|+|v-m|\bigr).
\]

The lower inequality follows by minimizing the integral over intervals of a given length; the minimum occurs when the interval is centered at $m$. The upper inequality follows by integrating the chord bound for the convex function $|z-m|$.

Equal marginals imply $\mathbb E[g(V)-g(U)]=0$. Consequently the expected positive and negative parts of this difference agree. On the event $D<0$, the lower interval inequality gives

\[
 D^2\le4(g(U)-g(V)).
\]

On the event $D>0$, the upper interval inequality and $D\le a$ give

\[
 g(V)-g(U)\le\frac a2\bigl(|U-m|+|V-m|\bigr).
\]

Combining these statements,

\[
 \begin{aligned}
 \mathbb E[D^2\mathbf1_{D<0}]
 &\le4\mathbb E[(g(U)-g(V))\mathbf1_{D<0}]\\
 &=4\mathbb E[(g(V)-g(U))\mathbf1_{D>0}]\\
 &\le2a\mathbb E[(|U-m|+|V-m|)\mathbf1_{D>0}]\\
 &\le4ab.
 \end{aligned}
\]

Meanwhile, $\mathbb E[D^2\mathbf1_{D>0}]\le a^2$. This proves the first bound. For the second, $\mathbb ED=0$ implies

\[
 \mathbb E D_+=\tfrac12\mathbb E|U-V|
 \le\tfrac12\mathbb E(|U-m|+|V-m|)=b.
\]

Therefore $\mathbb E[D^2\mathbf1_{D>0}]\le a\mathbb ED_+\le ab$, proving the second bound. Neither independence nor exchangeability is assumed. This distinction between bounded positive displacements and potentially large negative displacements avoids applying the original coarse interval bound to both events.

**Applying the grading reduction.** The source's Lemma 3 and Section 5 construct equal-binomial-marginal random variables $U,V$ such that

\[
 V-U\le d,\qquad I(f)\le2\mathbb E(U-V)^2,
 \qquad U,V\sim\operatorname{Bin}(n,1/2).
\]

These implications precede the source's final use of its coupling estimate; thus substituting the probability lemma above does not assume the desired improved theorem. Applying it with $a=d$, and also using $I(f)\le n$, proves the displayed estimate involving $b_n$. A polynomial with zeros can first be shifted by a sufficiently small positive constant to preserve the stated sign convention; reducing powers by $x_i^2=1$ does not increase degree. Degree zero gives $I(f)=0$.

**An elementary bound for $b_n$.** Put

\[
 c_k=4^{-k}\binom{2k}{k}.
\]

The binomial deviation formula gives $b_{2k}=kc_k$ and $b_{2k+1}=(2k+1)c_k/2$. These identities also follow by summing the upper half of the binomial law and using $j\binom nj=n\binom{n-1}{j-1}$; the two resulting binomial tails cancel except at their boundary.

We have

\[
 c_k\le(3k+1)^{-1/2}\quad(k\ge0).
\]

Indeed, the base case is equality, $c_{k+1}/c_k=(2k+1)/(2k+2)$, and

\[
 (2k+2)^2(3k+1)-(2k+1)^2(3k+4)=k\ge0.
\]

This proves the inequality by induction without an asymptotic approximation. For even $n=2k$,

\[
 \frac{8b_n}{\sqrt n}\le4\sqrt{\frac{2k}{3k+1}}
 \le4\sqrt{\frac23}<4\sqrt{\frac{15}{22}}.
\]

For odd $n=2k+1\ge15$, we have $k\ge7$. Since $(2k+1)/(3k+1)$ is decreasing,

\[
 \frac{8b_n}{\sqrt n}\le4\sqrt{\frac{2k+1}{3k+1}}
 \le4\sqrt{\frac{15}{22}}.
\]

Thus $8b_n/\sqrt n\le K:=4\sqrt{15/22}$ for every $n\ge15$.

**A constant valid for every $n,d$.** Let $C=383/100$. If $n\le C^2d^2$, then $I(f)\le n\le Cd\sqrt n$. Otherwise $d\ge1$ and $n>C^2d^2\ge14.6689$, so $n\ge15$ and $d/\sqrt n<1/C$. The sharper estimate gives

\[
 \frac{I(f)}{d\sqrt n}
 \le\frac{8b_n}{\sqrt n}+\frac{2d}{\sqrt n}
 <K+\frac2C<C.
\]

The last comparison is an exact algebraic statement. Since $C-2/C>0$ and $K^2=120/11$, it follows from

\[
 (C^2-2)^2-\frac{120}{11}C^2
 =\frac{524329931}{1100000000}>0.
\]

This completes the all-dimension, all-degree proof. The constant 3.83 is a convenient sufficient value, not a claim of optimality.

The full reduction and current declarations are in the [published manuscript](paper/manuscript.pdf), archived at [Zenodo](https://doi.org/10.5281/zenodo.23269472).

**Verification scope.** [verify_127.py](checks/verify_127.py) checks the rational certificate, the binomial identities, the central-binomial induction inequality, and the resulting bound exactly in a finite range. The proof above supplies the extension to all dimensions. [explore_127.py](checks/explore_127.py) checks coupling and grading calculations numerically on finite instances; those experiments are supplemental and do not establish the theorem. No result here depends on a floating-point LP optimum. The borrowed operator reduction was inspected in the original PDF; its Lean library was not rebuilt.
