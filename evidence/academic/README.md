# Academic evidence

## What was verified, and how

`refs_verified.json` is the raw output of `validate_references.py`, which for each
candidate DOI:

1. resolves it against the Crossref REST API (`https://api.crossref.org/works/<doi>`),
2. rejects the record unless Crossref returns a complete record whose title matches the
   expected title (token-overlap similarity >= 0.80),
3. queries Unpaywall (`https://api.unpaywall.org/v2/<doi>`) for a legal open-access location.

`reference_validation.md` is the human-readable validation table used in the report.

## What was NOT verified

**Scopus indexing, Scopus quartile, and SINTA rank are not verified.** There is no free,
authoritative, machine-readable source for either index available in this environment, so
every record carries the literal value `Not independently verified`. The report never
claims a quartile or a SINTA rank.

## Counts at verification time (2026-10-03)

- candidates submitted: 40
- DOI resolved and title matched: 40
- open-access location confirmed: 35
- kept after topical screening and de-duplication: 34
- additionally excluded from the report: 7 off-topic records (biomedical/criminology) that
  passed the technical checks but are irrelevant to the report subject matter.

`refs_candidates.json` is retained so any reviewer can re-run the validator and reproduce
the same set.
