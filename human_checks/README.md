# Human checks

Checks by the author (BB) of AI-extracted values against the source documents.

- `summary.csv`: one row per source and check: date, scope, records checked against total, findings, and status after the check.
- `findings.csv`: one row per error found (so far one: HC001, a boundary description; value unchanged).

Scope: the values behind the plotted operating points of the reforming and CO2-splitting studies, and the evidence behind each adopted power-supply efficiency range plus the extreme points in the power-supply figure (47 values). Checks are partial, covering the values used in the manuscript, not whole papers.

Judgements on subjective cases are recorded in each topic's `logs/processing_log.md`, and decisions on differences found in the independent AI cross-check in `logs/cross_check_log.md` (marked "BB").
