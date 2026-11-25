# Source extraction: SRC020

## Source and review

- Source ID / citation / DOI: SRC020. O'Modhrain, C., Trenchev, G., Gorbanev, Y., Bogaerts, A. (2024). Upscaling plasma-based CO2 conversion: case study of a multi-reactor gliding arc plasmatron. ACS Eng. Au 4, 333-344. https://doi.org/10.1021/acsengineeringau.3c00067
- Source filenames and document versions: manuscript.pdf, published version (CC BY-NC-ND 4.0), SHA-256 `5c2a2c08094372e9b68d51fcd5292350ed3ed5dfa80e05d7e43b310ce07f4b61`; ESI.pdf (Supporting Information, 9 pp.), SHA-256 `ac09d5bb3899c0957b59e9340cc7f54e9523a38e5d7b1b80d9fe62d383f23972`. Printed page = PDF page + 332.
- Retrieval date: 2026-11-11 (downloaded by BB).
- Protocol version: workflow.md 0.7, with the CO2-splitting metrics of [../../literature_review_objectives.md](../../literature_review_objectives.md).
- Extractor / date: Claude (AI), 2026-11-12.
- Coverage: full manuscript and ESI; Figs. 3-5 read from rendered pages. Economics (Section 7) recorded in one line per the workflow.
- Reviewer / date / checks: Claude (AI), 2026-11-12; efficiency, SEI and EC recalculated (C001-C003).
- Review status: ai_checked; partial human check by BB, 2026-11-25: OP001 (E010, E011) confirmed, no changes (human_checks/summary.csv). Other records human verification pending.

## Electricity supply

- One PSU per node: GAD-1000 (Micro-Arc), DC switching-type HV generator, current-regulated without a ballast resistor, ~1 kW each (E003).
- **Power boundary: plug.** A three-phase meter (Schneider iEM3150) measures "the overall power consumed by the process"; all metrics use plug power (E006, E009). Whether the chiller, PLC and fan are on the metered circuit is not stated.
- **Measured PSU efficiency (plug to plasma): 77-83%** (~80%) (E010). Authors' targets: >90% and ~150 EUR/kW (now ~400 EUR/kW) (E004).
- Plasma scale: 1.5-7.1 kW plug (5 nodes at up to ~1.4 kW). No external heat. Post-plasma chamber water-cooled (E002).

## Reactor configuration

- Multi-reactor gliding arc plasmatron (MRGAP): five reverse-vortex GAP nodes on one anode plate in one housing; per node 3.2 mm tangential inlet and 9 mm outlet into a common water-jacketed post-plasma chamber (E002). Built by D-CRBN (E001).
- Integrated plug-and-play unit with PLC, gas sensors, interlocks and Faraday cage (Section 4).

## Operating conditions

CO2 99.7 vol%, 30-80 L/min total, always split over all five nodes; 23.6 L/mol (17 C) (E007). Atmospheric outlet. Triplicates (E008).

| OP | Active nodes | Q (L/min) | P plug (kW) | SEI (kJ/L) | Evidence |
|---|---|---|---|---|---|
| OP001 | 5 | 80 | 7.1 | 5.33 | E011 |
| OP002 | 3 | 60 | ~4.2-4.3 | ~4.2-4.3 | E012, E013, C002 |
| OP003 | 1 (central) | 80 | ~1.48 | 1.11 (C002) | E014 |

## Performance indicators

- **Power boundary:** plug (three-phase meter); plasma basis estimated with the measured PSU efficiency.
- **External heat:** no.
- Product: CO2/CO/O2, unseparated; CO not measured directly (stoichiometry assumed) (E008).

| OP | X_CO2 (%) | eta plug (%) | eta plasma, est. (%) | EC_CO2 plug (MJ/mol) | EC_CO plug (kWh/Nm3) | EC_CO plasma est. (kWh/Nm3) | CO2 converted (g/h) |
|---|---|---|---|---|---|---|---|
| OP001 | 8.7 | 19.6 (reported ~20) | 23.6-25.4 (authors 24) | 1.44 | 17.9 | 13.8-14.9 | 779 |
| OP002 | ~7.6 | 21.2 (reported ~21) | 25.5-27.5 | 1.34 | 16.5 | 12.7-13.7 | 510 |
| OP003 | ~2.1 | 22.7 (reported 23) | 27.3-29.5 | 1.25 | 15.5 | 11.9-12.9 | 188 |

- Author's metrics: eta = X x 283 x Q / (P x 23.6 x 60) on plug power; SEI kJ/L; EC MJ per mol CO2 converted (E009). Reproduced for OP001.
- Conversion peaks at SEI ~5.3 kJ/L (~1.3 eV/molecule on plug power) for 3-5 nodes; more nodes move the peak to higher flow (E011, E012). Low conversion at low flow is attributed to a hot post-plasma chamber (~600 C) promoting recombination; ~450 C or lower is better (E015).
- Efficiency on plug power stays at 20-23% across configurations; the gain from parallel nodes is throughput (188 -> 779 g/h CO2 converted), not efficiency or conversion.
- Inconsistency: the text gives the single-node optimum as 23% at 1.4 kJ/L with 187 g/h; those numbers give 17.9%. Fig. 3a (1.48 kW at 80 L/min) gives 1.11 kJ/L and 22.7%, which is used (E042).
- Fig. 4 efficiency bar at 80 L/min (~22%) is slightly above the recalculated 19.6% (E011).
- Duration: not reported (E017).
- Unusual data (one line): total assembly ~3000 EUR/kW incl. PSU at <=1000 t/y; PSU ~400 EUR/kW; MW generators ~7000 EUR/kW (estimate from Detz & van der Zwaan); separation cost excluded (E004, E005, E016).

## Reporting quality

| Item | Answer | Reason and evidence IDs |
|---|---|---|
| Q1 Power measurement | yes | Plug power from a three-phase meter; PSU efficiency measured (method not described) (E006, E010). |
| Q2 Feed definition | yes | Purity, flow range, split and molar volume stated (E007). |
| Q3 Product analysis | partly | Calibrated O2 and CO2 sensors, expansion-corrected; CO not measured; no GC cross-check (E008). |
| Q4 Balance closure | partly | Two independent conversion estimates (CO2- and O2-based) averaged; agreement not reported (E008). |
| Q5 Temperature | partly | Bulk post-plasma gas temperature by thermocouples; plasma temperature not measured (E015). |
| Q6 Controls | yes | Number and position of active nodes varied at matched flow (Section 6). |
| Q7 Repeatability | yes | Triplicates with standard deviations (E008). |
| Q8 Stability | no | No duration or time on stream (E017). |
| Q9 Energy completeness | partly | Plug power covers PSUs; auxiliaries (chiller, PLC, fan) not stated; no separation (E006, E016). |

- Confidence in conversion/product results: moderate. Calibrated sensors and triplicates, but CO not measured and no GC cross-check.
- Confidence in energy results: higher. Plug power measured and PSU efficiency reported; one text-figure inconsistency at the 1-node point.

## Gaps and comparison limits

- Auxiliary power on the metered circuit not stated.
- Low single-pass conversion (2-9%): separation and recycle energy would dominate a product-CO comparison; not addressed (E016).
- No durability data; electrode lifetime not reported.
- Affiliations: prototype and PSUs from the spin-off and an affiliated company; no competing interest declared (E001).

## Calculations

All in outputs/calculations.py. 23.6 L/mol; dH 283 kJ/mol; kWh/Nm3 per mol CO at 22.414 L/mol.

- SRC020-C001 SEI, eta, EC on plug power; conversion rate. Inputs E011, E013, E014. Result E041.
- SRC020-C002 Conversion and power backed out of the reported SEI and conversion rate; single-node inconsistency. Input E012. Result E042.
- SRC020-C003 Plasma-basis efficiency and EC with PSU efficiency 0.77-0.83. Input E010. Result E043.

## Revisions

None.

## Plasma characteristics

- Regime: "warm" gliding arc plasmatron, reverse vortex, ~1-1.4 kW per node; designed to stay below the thermal regime (Section 3).
- Gas temperature: post-plasma bulk gas 440-600 C (thermocouples) (E015); plasma temperature not measured.
- Other diagnostics: none.
