# GitHub review of the 3.83 average-sensitivity refinement

Checked: **9 October 2026**.

**Finding:** no matching or stronger uniform refinement was identified in the sources checked. This is a bounded search result, not independent confirmation of priority and not proof that no other GitHub artifact exists.

The comparison is for every degree-at-most-$d$ real polynomial threshold function on the uniform $n$-dimensional Boolean cube, with $\mathrm{sgn}(0)=1$, and a coefficient independent of both $n$ and $d$. An equivalent refinement or a coefficient at most $3.83$ would be relevant. A different notion of sensitivity, a result for a restricted class, or an unrelated occurrence of the number 3.83 does not establish the same theorem.

## Sources checked in detail

| Source | Observation | Comparison |
| --- | --- | --- |
| [OpenAI family 127](https://github.com/openai/math/tree/main/preprints/Average-Sensitivity-of-Polynomial-Threshold-Functions-September-25-2026) and [formalization scope](https://github.com/openai/math/blob/main/lean/docs/127.md) | The stated coefficient is 8 | Original argument on which this note builds |
| [Dedicated family-127 discussion](https://github.com/mahrud/openai-math-comments/pull/127) | The issue-comments, review-comments, and reviews endpoints each returned an empty list | No posted refinement was found in that thread |
| [Awesome AI Proofs sensitivity entry](https://github.com/subroy13/awesome-ai-proofs/blob/main/problems/average-sensitivity-of-polynomial-threshold-functions.md) | Describes and links the OpenAI coefficient-8 result | Catalogue of the original proof, rather than another refinement |
| [PvsNP repository](https://github.com/robertocastiglion/PvsNP) | The README's average-sensitivity discussion concerns a circuit-complexity meta-function | It does not state the all-degree polynomial-sign bound under comparison |
| [vivan1992/gotsman](https://github.com/vivan1992/gotsman), [aegis-discovery](https://github.com/ycchiranjeevi/aegis-discovery), and [gcge](https://github.com/drdezarza/gcge) | Their inspected READMEs did not supply the target refinement | Keyword-associated search hits |

## Search coverage

Nine public GitHub REST searches were made: four repository searches and five issue/pull-request searches, including explicit comment searches. They returned **61 distinct repository matches** and **124 distinct issue/pull-request matches**. The returned matches were triaged for relevance; the detailed inspections are described above. Every search reported `incomplete_results: false`, and each returned all its reported matches on the requested page. That flag concerns the individual query, not coverage of all GitHub content.

Queries included `Gotsman`, the exact `Gotsman-Linial` string, `polynomial threshold` with `sensitivity`, `average sensitivity` with `OpenAI`, and `3.83` with `polynomial threshold`. Repository searches included README searches and searches that allowed forks. Additional indexed-web queries targeted GitHub pages, the exact manuscript name, `383/100`, the proposed coefficient, and coupling terminology.

The public API result totals and queries are recorded in [github-search-summary.json](github-search-summary.json). The summary retains query totals and comparison links; full third-party issue bodies are not redistributed in this package.

## Fork comparisons

OpenAI's repository reported **1,379 forks** at the time of the check. The first 100 newest forks and first 100 forks sorted by stars were fetched, giving **189 distinct sampled forks**. Ten of those had a push timestamp later than upstream's reported last push; their default branches were compared with upstream `main`:

- Seven comparisons were identical to upstream.
- [Deicyde/math](https://github.com/openai/math/compare/main...Deicyde:main) changed its README, unrelated comparator challenges, and representation-theory material.
- [Stars1233/math-](https://github.com/openai/math/compare/main...Stars1233:main) added a workflow.
- [2404589803/math](https://github.com/openai/math/compare/main...2404589803:main) added a synchronization workflow.

None of those ten comparisons changed the family-127 sensitivity argument or supplied a competing refinement. The other sampled forks were not content-compared. An older divergent fork could contain relevant work even if its push timestamp precedes upstream's latest push; the timestamp selection does not rule this out. The search also did not inspect all forks or all their branches.

## Access and interpretation limits

The unauthenticated REST code-search request returned **HTTP 401, Requires authentication**. Full GitHub code search was therefore not performed. Repository metadata/README searches and issue searches do not replace full file-content search. PDFs, unindexed files, private repositories, gists missed by indexed search, and unpublished work may contain results outside this review's coverage.

The existing broader literature review remains relevant. The strongest supported wording is: **the 3.83 refinement improves every comparable bound located so far, and no matching GitHub refinement was found in this review.** The mathematical proof and the historical priority question are separate.
