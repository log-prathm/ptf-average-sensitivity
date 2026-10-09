# An elementary improvement of the average sensitivity bound for polynomial threshold functions

**Prathmesh Lagdive, Vaibhav Aglave, Suraj Damre**  
M. S. Bidve Engineering College, Latur

**Published preprint:** [Zenodo record](https://zenodo.org/records/23269472) · [DOI: 10.5281/zenodo.23269472](https://doi.org/10.5281/zenodo.23269472).

This research note refines the probability step in [OpenAI's weighted-grading proof](https://github.com/openai/math/blob/main/preprints/Average-Sensitivity-of-Polynomial-Threshold-Functions-September-25-2026/main.pdf). For every real polynomial threshold function of degree at most $d$ on the uniform Boolean cube $`\{-1,1\}^n`$, it derives

```math
\mathrm{AS}(f) \le 3.83\,d\sqrt{n}.
```

The estimate is uniform in dimension and degree and uses $\mathrm{sgn}(0)=1$. It improves the coefficient $8$ in the cited argument. The weighted grading and edge-recovery construction remain attributed to OpenAI.

If $b_n=\mathbb{E}|B_n-n/2|$, where $B_n\sim\mathrm{Bin}(n,1/2)$, the more precise estimate is

```math
\mathrm{AS}(f) \le \min\{n,\;8d\,b_n+2d^2,\;10d\,b_n\}.
```

For $d=o(\sqrt n)$, this gives an asymptotic coefficient $8/\sqrt{2\pi}$. The value $3.83$ is a sufficient uniform coefficient; optimality is not claimed.

## Read the result

- [Six-page published manuscript](paper/manuscript.pdf) and [LaTeX source](paper/main.tex).
- [Proof notes](127-improved-bound.md).
- [Literature comparison](docs/literature-review.md) and [GitHub search report](docs/github-search-review.md).
- [Separate AI proof audit](docs/proof-review.md).

The derivation and review used OpenAI Codex. Exact finite checks and supplemental numerical experiments accompany the analytic proof. The refinement has not received independent human peer review or a Lean formalization. The searches did not establish exhaustive priority.

The public research records are included as [supporting evidence](evidence/README.md).

## Reproduce the checks

The exact checks use only the Python standard library:

```bash
python3 checks/verify_127.py
```

The script checks the rational constant certificate, binomial identities, a central-binomial induction inequality, and finite instances through dimension 2000. It writes `checks/127-exact-verification.json`. The universal theorem rests on the analytic proof, rather than the finite checks.

The optional coupling LP and matrix experiments require NumPy and SciPy:

```bash
python3 -m venv .venv
.venv/bin/pip install -r checks/requirements-optional.txt
.venv/bin/python checks/explore_127.py
```

Their previously recorded output is [127-numerical-checks.json](checks/127-numerical-checks.json). Floating-point LP results are supplemental evidence.

## Build the paper

With a standard TeX installation providing pdfLaTeX:

```bash
make paper
```

The output is `build/main.pdf`. The manuscript uses standard packages, an inline bibliography, and no shell escape.

## Attribution and license

The published manuscript and its LaTeX source use [CC BY 4.0](paper/LICENSE-CC-BY-4.0), matching the Zenodo paper. Verification code, recorded check outputs, proof notes, and repository documentation use [Apache License 2.0](LICENSE). [NOTICE](NOTICE) records the original argument and the scope of the refinement. [PROVENANCE.json](PROVENANCE.json) identifies the original argument and the Zenodo files by checksums.

Use [CITATION.cff](CITATION.cff) for the authors and title, and cite the original OpenAI argument when describing the weighted-grading construction.
