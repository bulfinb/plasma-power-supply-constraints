# From et al. (2025): eSMR of biogas with feed-forward control, pilot plant

## Source and review

- Source ID: **SRC006**. Thomas N. From, Marené Rautenbach, Behzad Partoon, Martin Østberg, Sebastian T. Wismann, Anders Bentien and Peter M. Mortensen, "Understanding the dynamic interplay of CH4/CO2 ratio in electrified reforming of biogas to renewable methanol production: A pilot plant story," Chemical Engineering Journal 518 (2025) 164662. DOI: https://doi.org/10.1016/j.cej.2025.164662. Not open access.
- Documents (user-supplied, 2026-11-04): [Manuscript.pdf](../Manuscript.pdf), 9 pages, publisher version; printed page numbers equal PDF page numbers. [ESI.docx](../ESI.docx), Supporting Information sections S1-S5 (normalized-gas method, S/HC, simulations, carbon formation, sensitivity); no pages, cited by section.
- SHA-256:
  - Manuscript.pdf: `f2017566703ceecf2c86719f69c8627ce3b1722e52f0ab6d5e83c257c2f4c088`
  - ESI.docx: `300d5197c47ebc8d7dee33d876908f8b176d8ae750ce817092c4f3991516f3f6`
- Protocol: 0.1. Extractor/reviewer: Claude (AI), 2026-11-04, same-extractor checks. Status: **ai_checked; human verification pending**.
- Coverage: full manuscript and ESI read; Fig. 5 inspected and graph-read for the CH4/CO2 ratio and flow ranges. Thermodynamic simulations (Figs. 1, S1-S3) recorded only as modelling.
- Relation to other sources: same Topsoe/Aarhus eSMR pilot plant as From et al. (2024), SRC005. This paper adds point-matched feed flows and an outlet composition, but no energy data.
- Records: [evidence.csv](evidence.csv), 25 records (E001-E021, E041-E044); [calculations.py](calculations.py); [short_summary.txt](../short_summary.txt). Evidence IDs below abbreviated E001 = SRC006-E001.

## Electricity supply

The exit gas temperature is held by feedback control of the power from a PSU (E004). **No electrical power, energy efficiency or energy consumption is reported** in the manuscript or ESI (E005). The authors state that the data are confidential (E003).

## Reactor configuration

Same pilot plant as SRC005: sulfur removal, compressors, steam generator, heaters, prereformer, eSMR (Topsoe eREACT), waste heat boiler, condensate separation and flare (E001). New in this paper: H2 is co-fed, and steam and H2 flows are set by a feed-forward controller using a real-time CH4 analyser (Endress+Hauser Prosonic Flow 200) to hold the inlet O/C and H/C ratios (E006). Reactor and catalyst size are not reported (E020).

## Operating conditions

The feed is raw biogas plus steam and **co-fed H2**; in OP002, CO2 was also added to simulate composition swings. This is mixed steam/CO2 reforming with hydrogen in the feed, aimed at a methanol syngas module (H2−CO2)/(CO+CO2) of 2.

| OP | Test | Exit T (degC) | p (barg) | Biogas (Nm3/h) | Steam / H2 (Nm3/h) | Ratios | Duration | Evidence |
|---|---|---|---|---|---|---|---|---|
| OP001 | Unregulated (Fig. 4) | 950 | 10 | 6.3 | 7.9 / 4.4 | CH4/CO2 1.33 at TOS 0; S/HC 2.1-2.3 | 20 h | E008-E009 |
| OP002 | Feed-forward, CO2 disturbances (Fig. 5, Table 1) | 900 ± 1 | 6 | 6.4 (+ added CO2, NR) | ~7.7-8.6 / ~5.2-10.1, controlled | O/C 2.22, H/C 6.46, S/HC 2.3 | 80 h | E010-E014 |
| OP003-OP005 | Table 2 Exp. 1-3 | 950 / 1000 / 1050 | 10 | 6 | NR | O/C ~2.0; S/HC ~2.0 | NR | E015 |
| OP006-OP008 | Table 2 Exp. 4-6 | 950 | 10 | 6 | NR | S/HC 1.87 / 1.62 / 1.31 | NR | E015-E016 |

Overall envelope: 900-1050 degC, 6-10 barg, normalized S/HC 1.3-2.3; approximately 1000 h of operation in this work (E017). How this relates to the ~2000 h in SRC005 is not stated.

## Performance indicators

- **Syngas composition (OP002, 80 h average; E013):** H2 53.0, H2O 23.0, CO 17.3, CO2 6.2, CH4 0.24 mol% wet, all within 0.4 points of equilibrium.
- **Conversion (reviewer calculation, C002, E042):** X_CH4 about 97.7-98.2% and X_CO2 about 42-54% at OP002. The range comes from the inlet CH4/CO2 ratio, which varied from about 0.78 to 1.22 because of added CO2 (graph-read, E011). The authors do not report conversion.
- **Elemental consistency (C003, E043):** outlet O/C 2.22 and H/C 6.44 versus inlet 2.22 and 6.46, so the Table 1 composition is consistent with the feed ratios.
- **Syngas module:** 1.99 ± 0.01 with control (OP002, E014); 1.93-2.06 without control (OP001, E009). The authors' main result is control quality, not conversion or energy.
- **Scale:** CH4 feed about 2.5-2.7 mol/min (C001, E041), roughly a third of the SRC005 energy-test flows.
- **Low S/HC:** stable operation down to S/HC 1.31 (OP008), with more variable control at that point (E016).
- **Modelling (excluded):** thermodynamic H/C-O/C model and unregulated simulations (E021).

### Energy indicators

- Fired SMR reference metrics: not applicable.
- **Power-basis metrics:** not calculable; no electrical power reported (C004, E044).
- **Author energy metric:** none.
- **Whole-system eta_HHV:** not calculable.
- **Energy completeness:** no energy flows reported.

## Reporting quality

| Item | Answer | Reason and evidence IDs |
|---|---|---|
| Q1 Power measurement | no | No power values reported (E005). |
| Q2 Feed definition | partly | Biogas, steam and H2 flows and ratios given for OP001-OP002 (E008, E010); added CO2 flow and Table 2 steam/H2 flows not reported (E015). |
| Q3 Product analysis | yes | GC with stated relative errors, plus real-time CH4 analyser (E006, E013). |
| Q4 Balance closure | partly | Not reported by the authors (E019); our elemental check closes within 0.3% (C003). |
| Q5 Temperature | partly | Exit gas temperature with stated deviations (E012, E015, E018); no profiles. |
| Q6 Controls | partly | Unregulated run (OP001) and simulated unregulated case as comparisons for the control system (E009, E021). |
| Q7 Repeatability | partly | Standard deviations over time; no repeat runs. |
| Q8 Stability | yes | 80 h controlled test; about 1000 h total (E010, E017). |
| Q9 Energy completeness | no | No energy flows reported (E005). |

- **Conversion/product results: moderate confidence.** Composition at equilibrium with standard deviations, and elemental ratios close; but conversion is our calculation, the inlet carbon split is graph-read and the data are confidential (E003).
- **Energy results: not available.** No energy data.
- **Independence:** Topsoe co-authors develop and promote the technology; one author has a related patent pending (E002).

## Reported system information

- Boundary: pilot plant as in SRC005; no energy boundary.
- Flows: feed flows for OP001-OP002; outlet composition for OP002 only; no outlet flows.
- Energy flows: none.
- Hardware: real-time CH4 analyser and PLC feed-forward control added; reactor size not reported.
- Costs: not reported.

## Missing information and comparison limits

| Status | Gap | Consequence |
|---|---|---|
| not_reported | Electrical power and any energy metric | No EC_CH4, SEI or efficiency |
| not_reported | Added CO2 flow in OP002 | Inlet carbon split only from the Fig. 5C ratio range |
| not_reported | Conversions | Reviewer-calculated for OP002 only |
| not_reported | Table 2 steam and H2 flows; outlet compositions | No conversion for OP003-OP008 |
| not_reported | Outlet flows | No H2 yield; net H2 production unknown because H2 is co-fed |
| not_applicable | Plasma characteristics | Joule-heated source |

Comparison limits:
- Co-fed H2 and added CO2 make OP002 a methanol-syngas condition, not a hydrogen-production benchmark. Net H2 production cannot be calculated.
- Use this source for conversion, conditions and stability at pilot scale; use SRC005 for energy.

## Calculations

All in [calculations.py](calculations.py).

- **SRC006-C001, CH4 feed.** Inputs E008, E010-E011. OP001: 6.3 Nm3/h × 57.1% = 2.67 mol/min. OP002: 6.4 Nm3/h × 52-55% CH4 (biogas CH4/CO2 1.10-1.22 outside CO2-addition periods) = 2.49-2.62 mol/min. Table 2: 2.2-3.3 mol/min for 50-75% CH4. Normal reference assumed 0 degC, 1 atm.
- **SRC006-C002, conversion at OP002.** Inputs E011, E013. Carbon basis from Table 1 (CO + CO2 + CH4 = 23.74 mol%). X_CH4 = 1 − (0.24/23.74)/x_CH4,in; X_CO2 = 1 − (6.2/23.74)/(1 − x_CH4,in), with x_CH4,in = r/(1 + r) for r = 0.78-1.22. Results: X_CH4 97.7-98.2%; X_CO2 53.5-42.0%. Uses 80 h averages, so it is indicative; GC errors (9% relative for CH4) not propagated.
- **SRC006-C003, elemental check.** Input E012-E013. Outlet O/C = (H2O + CO + 2CO2)/C = 2.22; H/C = (2H2 + 2H2O + 4CH4)/C = 6.44.
- **SRC006-C004, EC_CH4.** Not calculated; no power reported.

## Review and revisions

- 2026-11-04: initial extraction (Claude, AI). Human verification pending, especially the Fig. 5C ratio range and the Table 1 caption label swap (E012).

## Plasma characteristics

Not applicable (Joule-heated source).
