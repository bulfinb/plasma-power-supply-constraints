# Source extraction: SRC024

## Source and review

- Source ID / citation / DOI: SRC024. Van Laer, K., Bogaerts, A. (2015). Improving the conversion and energy efficiency of carbon dioxide splitting in a zirconia-packed dielectric barrier discharge reactor. Energy Technol. 3, 1038-1044. https://doi.org/10.1002/ente.201500127
- Source filenames and document versions: manuscript.pdf, published version (Wiley typeset), University of Antwerp repository, SHA-256 `8bb54c87724d300c58a602e7fe427c713c7e7ccef7ebfcf86992841bd925395a`. Printed page = PDF page + 1037. No supplement.
- Retrieval date: 2026-11-11 (downloaded by Claude).
- Protocol version: workflow.md 0.7, with the CO2-splitting metrics of [../../literature_review_objectives.md](../../literature_review_objectives.md).
- Extractor / date: Claude (AI), 2026-11-12.
- Coverage: experimental results and methods; the 2D helium fluid model recorded only as the authors' interpretation. Fig. 1 not digitised (headline values given in the text).
- Reviewer / date / checks: Claude (AI), 2026-11-12; plasma power implied by the reported values, expansion correction and energy per CO calculated (C001-C004).
- Review status: ai_checked. Human check: none.

## Role in the review

Included to represent the DBD class (objectives: span plasma types), not as a scale-up candidate. The Wang et al. (2012) packed-DBD claim (record CR021) remains unchecked.

## Electricity supply

- AC HV power supply (AFS); experiments labelled by "applied power" 60, 80, 100 W, whose meaning (supply input or setpoint) is not defined (E004).
- Plasma power from the V(t) I(t) integral (HV probe, Rogowski coil) (E007) is used for SEI and efficiency but not reported per point. Backing it out of the reported X and eta gives ~20-37 W, i.e. **33-46% of the applied power** (E041).
- Plasma scale: ~20-37 W. No external heat.

## Reactor configuration

Coaxial DBD: 8 mm grounded steel rod, Al2O3 tube (17/22 mm) with Ni foil HV electrode, 90 mm long, 4.5 mm gap, 15.9 cm3 discharge volume; packed with ZrO2 beads (dielectric constant 22-25) of five size ranges, or empty (E002, E003).

## Operating conditions

Pure CO2 (purity NR), 20, 50, 100 mL/min, atmospheric pressure; plasma on 20 min before GC (E005).

| OP | Packing | Applied power (W) | Flow (mL/min) | Evidence |
|---|---|---|---|---|
| OP001 | ZrO2 1.60-1.80 mm | 60 | 20 | E011 |
| OP002 | ZrO2 2.00-2.24 mm | 80 | 20 | E009 |
| OP003 | ZrO2 1.60-1.80 mm | 60 | 100 | E010 |
| OP004 | empty | 60 | 20 | E011 (via improvement factors) |

## Performance indicators

- **Power boundary:** plasma power (V x I) for the reported efficiency; "applied power" otherwise.
- **External heat:** no.
- Product: CO2/CO/O2, unseparated; CO and O2 selectivities ~50% each; no carbon deposits (E006).

| OP | X_CO2 reported (%) | eta reported (%) | X if expansion-corrected (%) | P_plasma implied (W) | EC_CO plasma (kWh/Nm3) | eta on applied power (%) |
|---|---|---|---|---|---|---|
| OP001 | 37.8 | 6.4 | 28.8 | 22.5-24.6 | 54 | 2.4 |
| OP002 | 42.0 | 4.7 | 32.6 | 34.0-37.2 | 74 | 2.0 |
| OP003 | 10.0 | 9.6 | 6.9 | 19.8-21.7 | 36 | 3.2 |
| OP004 | ~19.9 | ~3.6 | 14.2 | 21.3-23.3 | 98 | 1.3 |

- Author's metric: eta = dH X / (SEI Vm), dH 279.8 kJ/mol, plasma power (E008). Molar volume not stated.
- Packing raises conversion and efficiency together by up to ~1.9x; larger beads work best; performance falls above 80 W applied (E009-E012).
- Energy per CO: 36-98 kWh/Nm3 on plasma power, 3-5x the microwave and gliding-arc results in the set; ~2-3% efficiency on applied power.
- Conversion: computed from the drop in the GC CO2 signal against a no-plasma reference (E006); no expansion correction is stated, so reported conversions are likely high by ~25-45% relative (E043).
- Duration: steady state after 20 min; total run time NR.

## Reporting quality

| Item | Answer | Reason and evidence IDs |
|---|---|---|
| Q1 Power measurement | partly | Plasma power method stated but values not reported; 'applied power' undefined (E004, E007). |
| Q2 Feed definition | partly | Flows stated; purity, flow reference and molar volume not (E005, E008). |
| Q3 Product analysis | partly | Calibrated GC, but conversion from CO2 signal ratio without stated expansion correction (E006, E043). |
| Q4 Balance closure | partly | CO and O2 selectivities ~50% and no carbon deposits; no numerical closure (E006). |
| Q5 Temperature | no | Not measured. |
| Q6 Controls | yes | Empty reactor at matched conditions (E011). |
| Q7 Repeatability | no | Repeats and error bars not stated. |
| Q8 Stability | partly | 20 min to steady state; no long test (E005). |
| Q9 Energy completeness | no | Supply losses not reported beyond the undefined applied power. |

- Confidence in conversion/product results: moderate to lower. Calibrated GC, but likely uncorrected for gas expansion.
- Confidence in energy results: lower. Plasma power not reported per point, molar volume not stated; efficiency on applied power ~2-3%.

## Gaps and comparison limits

- Small lab DBD (~20-37 W plasma, 20-100 mL/min); represents the DBD class only.
- Likely uncorrected conversion (E043) and undefined applied power (E004).
- Wang et al. (2012) packed DBD (48.7% at 44.6%, CR021) not yet checked; if confirmed it would change the DBD picture.

## Calculations

All in outputs/calculations.py.

- SRC024-C001 Plasma power implied by reported X and eta at Vm 24.5 and 22.414 L/mol. Inputs E009-E011. Result E041.
- SRC024-C002 EC_CO2 = dH/eta (plasma basis), in kWh/Nm3 CO. Result E042.
- SRC024-C003 Expansion-corrected conversion if X = 1 - y_CO2,out. Result E043.
- SRC024-C004 Efficiency on applied power. Result E042.
- SRC024-C005 EC_CO on the expansion-corrected conversion: EC_CO2 x X_reported / X_corrected. Result E044 (OP001 71, OP002 95, OP003 52, OP004 137 kWh/Nm3 CO, plasma power).

## Revisions

- 2026-11-26 (BB decision): the synthesis and manuscript figure use the expansion-corrected conversion and EC_CO (C005, E044), for consistency with Kim 2014 (SRC028); reported values kept in the tables here. Evidence IDs kept.

## Plasma characteristics

- Regime: filamentary DBD with surface discharges at bead contact points; transition suggested above 80 W (authors) (E012).
- Gas temperature: not measured (model fixed at 300 K, helium).
- Other diagnostics: charge from external capacitor; 2D He fluid model of field enhancement at contact points (model only).
