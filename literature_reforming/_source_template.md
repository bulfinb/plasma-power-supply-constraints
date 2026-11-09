# Source extraction

## Source and review

- Source ID / citation / DOI: pending
- Source filenames and document versions: pending
- Retrieval date: unknown
- Protocol version: 0.1
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
- Power-basis metrics (P and boundary; SEI, EC_CH4, EC_H2/EY_H2, eta_P,LHV; external heat excluded or included): pending
- Author energy metric (value, equation, assumptions, basis/boundary): pending
- Whole-system eta_HHV / electricity fraction (or why unavailable): pending
- Energy completeness (included / omitted / unknown): pending

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

## Reported system information

- Authors' system boundary and included/excluded equipment: pending
- Reported inlet/outlet flows, compositions and mass/elemental balance closure: pending
- Reported energy flows and energy balance closure: pending
- Hardware size, utility requirements, power electronics, lifetime and maintenance: pending
- Reported costs, currency/year, scale and included equipment: pending

Record available evidence and gaps. Whole-system balances and cost estimates belong to the separate scale-up assessment (literature_review_objectives.md), not to the per-source extraction.

## Missing information and comparison limits

One checklist of missing core fields: not_reported, unclear or not_applicable. Record mismatched conditions/boundaries, source conflicts and user-selected assumptions.

## Calculations, if needed

Calculation ID, input evidence IDs, formula/units, assumptions, result and limitations. Separate calculations.md is optional for substantial calculations.

## Revisions, if any

Record corrections/decisions; preserve evidence IDs.

## Outputs

Save this extraction.md and evidence.csv in outputs/. Save short_summary.txt in the source's top folder alongside the manuscript and supplement. Summary: experimental scale, conversion, energy metrics, duration and reporting confidence, with compact evidence references. End the summary with the five comparison tables specified in workflow.md section 6 (route and scale, operating conditions, mass balance, energy balance, plasma parameters), using one matched experimental operating point per row. Extra files are optional.

## Plasma characteristics, when reported

For plasma sources, record the descriptors available in workflow.md section 7: regime, gas temperature, electron temperature/mean energy, electron density, reduced electric field, other diagnostic temperatures and degree of ionization. Include diagnostic method, location, operating conditions and stated uncertainty, with evidence IDs. Keep specific temperature labels and distinguish measurements, inferences and simulations. Do not create a checklist of every absent diagnostic. For Joule-only sources, this section is not applicable.
