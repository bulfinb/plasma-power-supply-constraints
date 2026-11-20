# Source extraction

## Source and review

- Source ID / citation / DOI: pending
- Source filenames and document versions: pending
- Retrieval date: unknown
- Protocol version: 0.8
- Extractor / date: pending
- Coverage (documents, conditions, figures): pending
- Reviewer / date / checks: pending
- Review status: unreviewed

## Electricity supply

Core findings with evidence IDs. Specify electrical conventions and measurement boundaries.

For plasma: plasma scale, total process energy (or unknown), thermal background/additional heating, and plasma-on/off distinction.

## Reactor configuration

Core findings with evidence IDs. Define volume basis.

## Operating conditions

Core findings with evidence IDs. Use a small condition table and operating-point IDs where useful. Separate operating_points.csv is optional.

## Performance indicators

Conversion, space time, output and demonstrated scale, with evidence IDs. Label modelling separately.

- Fired SMR reference only: EC_CH4,fired and EC_CH4,abs, reformer or plant boundary, data type: pending
- Power boundary (where and how P is measured): pending
- External heat (furnace/preheat/steam: yes / no / unknown; duty if reported): pending
- Core metrics per OP: SEI as reported, SEI_CH4, EC_CH4 (power basis; external heat excluded or included): pending
- Author's efficiency / energy metric (value, equation, basis): pending
- Optional, if product flows measured: EY_H2, eta_P,LHV: pending
- Benchmarks only (fired SMR, Joule pilots): EC_CH4,fired/abs, eta_HHV, f_electric: pending

## Reporting quality

| Item | Answer (yes/partly/no/NA) | Reason and evidence IDs |
|---|---|---|
| Q1 Power measurement | pending | |
| Q2 Feed definition | pending | |
| Q3 Product analysis | pending | |
| Q4 Balance closure | pending | |
| Q5 Temperature | pending | |
| Q6 Controls | pending | |
| Q7 Repeatability | pending | |
| Q8 Stability | pending | |
| Q9 Energy completeness | pending | |

For fired SMR reference sources, replace Q1-Q9 with R1-R4 from workflow.md section 5.

- Confidence in conversion/product results (higher/moderate/lower, reason): pending
- Confidence in energy results (higher/moderate/lower, reason): pending

## Gaps and comparison limits

Only missing information that blocks comparison (not_reported, unclear or not_applicable), mismatched conditions or boundaries, source conflicts and user-selected assumptions. Note in one line any unusual hardware, lifetime or cost data the paper reports.

## Calculations, if needed

Calculation ID, input evidence IDs, formula/units, assumptions, result and limitations. Separate calculations.md is optional for substantial calculations.

## Revisions, if any

Record corrections/decisions; preserve evidence IDs.

## Outputs

Save this extraction.md and evidence.csv in outputs/. Save short_summary.txt in the source's top folder alongside the manuscript and supplement. Summary: experimental scale, conversion, energy metrics, duration and reporting confidence, with compact evidence references. End the summary with the four comparison tables specified in workflow.md section 6 (route, scale and conditions; mass balance; energy; plasma parameters), using one matched experimental operating point per row. Extra files are optional.

## Plasma characteristics, when reported

For plasma sources (workflow.md section 7): regime; gas temperature with location, method and uncertainty; one line naming other diagnostics reported. For Joule-only sources, not applicable.
