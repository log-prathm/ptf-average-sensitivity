# Supporting research records

These records accompany the probability refinement and the related-work review. The published paper is archived at [Zenodo](https://zenodo.org/records/23269472), DOI [10.5281/zenodo.23269472](https://doi.org/10.5281/zenodo.23269472).

- `original-source.json` identifies the OpenAI family-127 source and its PDF checksum.
- The two `127-arxiv-*-inventory.json` files retain the queried bibliographic metadata and result totals.
- `semantic-scholar-citation-metadata.json` records the returned citing-paper metadata.
- `crossref-citation-metadata.json` retains title-query metadata; matches require relevance screening.
- `github-search-summary.json` records query totals, fork comparisons, and access limits.
- `github-fork-metadata.json` records the 189 sampled public forks used for candidate selection.
- `zenodo-record.json` records the published authors, ORCIDs, DOI, and file checksums.

The raw third-party abstracts, issue bodies, and unrelated correspondence are not redistributed. These bibliographic records and bounded searches do not establish exhaustive priority. The reviews in `docs/` describe the actual comparison and the limits of the proof audit.

The initial, superseded absolute-deviation idea is preserved in [earlier-refinement.md](../docs/earlier-refinement.md). The final coupling estimate and uniform coefficient 3.83 are in the [proof notes](../127-improved-bound.md) and [published manuscript](../paper/manuscript.pdf).
