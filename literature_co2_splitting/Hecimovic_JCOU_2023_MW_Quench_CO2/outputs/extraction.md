# Source extraction: SRC017

## Source and review

- Source ID / citation / DOI: SRC017. Hecimovic, A., Kiefer, C.K., Meindl, A., Antunes, R., Fantz, U. (2023). Fast gas quenching of microwave plasma effluent for enhanced CO2 conversion. J. CO2 Util. 71, 102473. https://doi.org/10.1016/j.jcou.2023.102473
- Source filenames and document versions: manuscript.pdf, published version (CC BY-NC-ND 4.0), SHA-256 `006cc945c8a63fc31b286a2e4a85c72fb7fefd42753e69fbfe670c0a0ef33a12`; ESI.pdf (1 page, derivation of the conversion equation), SHA-256 `93374f9d12943b461f63236d68f8be55a15d683ab888fa3852538cd230e135d3`. Printed page = PDF page.
- Retrieval date: 2026-11-11 (downloaded by BB).
- Protocol version: workflow.md 0.7, with the CO2-splitting metrics of [../../literature_review_objectives.md](../../literature_review_objectives.md).
- Extractor / date: Claude (AI), 2026-11-12.
- Coverage: full manuscript and ESI; Figs. 2, 6-10 read from rendered pages.
- Reviewer / date / checks: Claude (AI), 2026-11-12; efficiency recalculated from conversion and SEI (C002); flows cross-matched with SRC016 (C005).
- Review status: ai_checked. Human verification pending (efficiency-basis finding E019 in particular).

## Relation to SRC016 (same group, same torch)

Kiefer et al. 2024 (SRC016) reports the same cooled-channel reverse-vortex torch. This paper's 4, 10 and 15 ls/min (20 C) are SRC016's 3.7, 9.3 and 14.0 slm (0 C) (C005), and the conversions match (34.4-34.5% at 10 ls/min, 2.7 kW; 56.6% at ~4 ls/min, 2.7 kW). In the synthesis, count these as one torch: this paper is the primary source for the configuration study and conversion maps; SRC016 for wall-plug energy and for efficiencies on a consistent flow basis.

## Electricity supply

- 2.45 GHz microwave source, up to 3 kW, manual 3-stub tuner (E001). Power is the microwave power coupled to the plasma; its measurement is not described here (E002; SRC016: forward minus reflected).
- Supply efficiency and auxiliary power are out of scope (E003). Wall-plug values for this torch are in SRC016.
- Plasma scale: 0.8-2.7 kW absorbed. Total process energy: not reported here. No external heat.

## Reactor configuration

- E010 cylindrical resonator with coaxial ignition pin; quartz tube ID 26 mm; 2 m heat exchanger to the analysis point (E004).
- Configurations: standard (bottom tangential inlets, no constriction); reverse vortex with a 5 mm constriction into one 5 mm channel (1eff) or four 4 mm off-axis channels (4eff); water-cooled Cu channels, 73 mm long, 11.5 vs 27.3 cm2 gas-exposed surface (E004). Narrow 1.5 mm inlets (NGI) raise inlet velocity eightfold and stabilise the plasma at low flow (E005).
- No carbon deposits in the channels (E004).

## Operating conditions

Pure CO2 (purity not stated here; SRC016: grade 3.5). Flows in ls/min at 20 C, 1 atm (E006). Most runs at 900-950 mbar with the pump; the pump-off runs are at atmospheric pressure with <20-30 mbar drop (E009, E010).

| OP | Configuration | p | CO2 (ls/min) | P_abs (W) | Evidence |
|---|---|---|---|---|---|
| OP001 | 4effNGI | atmospheric, no pump | 10 | ~2700 | E011 |
| OP002 | 4effNGI | 900 mbar | 5 | 2700 | E013, E014 |
| OP003 | 4effNGI | 900 mbar | ~4 (from SEI 10.1 eV) | 2700 | E015 |
| OP004 | 4effNGI | 900 mbar | NR (high flow, SEI ~1.2 eV) | NR | E016 |

## Performance indicators

- **Power boundary:** absorbed microwave power (method referenced, not described).
- **External heat:** no.
- Product: CO2/CO/O2, unseparated.

| OP | X_CO2 (%) | SEI (kJ/mol; eV) | eta reported (%) | eta = X x 2.9/SEI, reviewer (%) | EC_CO2 (kJ/mol) | EC_CO absorbed (kWh/Nm3) |
|---|---|---|---|---|---|---|
| OP001 | ~34.5 (Fig. 2) | 390; 4.04 | ~27 (Fig. 2) | 24.8 | 1130 | 14.0 |
| OP002 | 55 | 779; 8.08 | ~21.7 (Fig. 7) | 19.7 | 1417 | 17.6 |
| OP003 | ~56.5 (abstract: up to 57) | 974; 10.1 | ~16.4 (Fig. 9) | 16.3 | 1722 | 21.3 |
| OP004 | 12 | ~1.2 eV (implied) | 30 (text) | ~27 (SRC016) | NR | NR |

- Author's efficiency: eta = X dH/SEI with dH = 2.9 eV/molecule (E008).
- **Efficiency basis (E019, E042):** in Figs. 2, 6, 7, 10 and in the conclusion's "30% at 12%", eta is about 9-10% above X x 2.9/SEI computed with the 20 C flows the paper states; Figs. 8-9 are consistent. Taking the flows at 0 C reproduces the figure values (26.6% and 21.2% vs 27 and 21.7), i.e. a 0 C SEI factor applied to 20 C flows. SRC016 reports the same torch at 27% for X 12.3%. The conclusion's "57% at an energy efficiency of 20%" also disagrees with Fig. 9 (~16.4% at that point). Conversion (from MS mole fractions) is not affected.
- CO outflow: up to ~3.5 ls/min, limited by the 3 kW generator (E012); 2.75 ls/min at OP002 (E013).
- Quenching works only at low flow / high SEI: no gain above 20 ls/min; the single channel saturates above ~2000 W (E018). 4effNGI at 900 mbar matches the standard torch at 200 mbar; no super-ideal quenching (E017).
- Pump removal does not change conversion (E010).
- Duration: not reported (power scans).

## Reporting quality

| Item | Answer | Reason and evidence IDs |
|---|---|---|
| Q1 Power measurement | partly | Absorbed microwave power used; measurement method only referenced (E002). |
| Q2 Feed definition | yes | Pure CO2; flow reference conditions explicitly stated (20 C, 1 atm) (E006). |
| Q3 Product analysis | yes | Relatively calibrated MS; expansion-corrected conversion derived in the ESI (E007). |
| Q4 Balance closure | no | Stoichiometry assumed; no C/O balance reported (E007). |
| Q5 Temperature | no | Gas temperature not measured (E020). |
| Q6 Controls | yes | Standard, nozzle and channel configurations, forward vs reverse inlets, pump on/off compared at matched flow and power (E010, E017). |
| Q7 Repeatability | partly | Error bars shown; repeats not described. |
| Q8 Stability | no | No time on stream; stability refers to plasma position (E005). |
| Q9 Energy completeness | no | Supply efficiency and auxiliaries out of scope (E003). |

- Confidence in conversion/product results: higher. Calibrated MS, expansion handled, results reproduced in SRC016.
- Confidence in energy results: moderate. Absorbed power only, and the reported efficiencies appear to mix flow reference conditions (E019); recalculated values are used.

## Gaps and comparison limits

- Reported efficiencies in Figs. 2, 6, 7, 10 and the conclusion are probably ~8-10% too high (E019). Use the reviewer values (E041) or SRC016.
- No wall-plug energy (see SRC016). No duration.
- Same torch as SRC016: avoid double counting.

## Calculations

All in outputs/calculations.py. 24.055 L/mol (20 C, 1 atm); dH 2.9 eV (authors) and 2.93 eV (review).

- SRC017-C001 SEI = P_abs / F_CO2. Inputs E011, E013, E015. Result E041.
- SRC017-C002 eta = X x dH / SEI, compared with the figure values; ratio, and the value with flows taken at 0 C. Result E041, E042.
- SRC017-C003 SEI implied by the reported 30% at 12% (1.16 eV). Input E016. Result E042.
- SRC017-C004 EC_CO2 = SEI/X; EC_CO in kWh/Nm3 (absorbed basis). Result E041.
- SRC017-C005 ls/min (20 C) to slm (0 C). Result E043.

## Revisions

None.

## Plasma characteristics

- Regime: contracted thermal plasma near 1 bar, ~6000 K cited from literature; thermal dissociation dominant (E020).
- Gas temperature: not measured.
- Other diagnostics: plasma length by ICCD imaging (Fig. 4); pressure in resonator and effluent.
