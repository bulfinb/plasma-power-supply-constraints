# Wanten et al. (2022): dry reforming of methane in a confined atmospheric pressure glow discharge, ~0.1-0.15 kW

## Source and review

- Source ID: **SRC015**. Bart Wanten, Stein Maerivoet, Christine Vantomme, Joachim Slaets, Georgi Trenchev and Annemie Bogaerts, "Dry reforming of methane in an atmospheric pressure glow discharge: Confining the plasma to expand the performance," Journal of CO2 Utilization 56 (2022) 101869. DOI: https://doi.org/10.1016/j.jcou.2021.101869 (Crossref-confirmed; online 23 Dec 2021). PLASMANT, University of Antwerp.
- Documents: [manuscript.pdf](../manuscript.pdf), 11 pages (printed page = PDF page); [ESI.pdf](../ESI.pdf), 19 pages (experimental analysis, quasi-1D model, extra selectivity results). ESI.docx has the same content; ESI.pdf used for locators. Retrieval date unknown.
- SHA-256: manuscript.pdf `095f470a66a355cc17dad2094b6c62b73df2cc773f785149504e0b10cad34f39`; ESI.pdf `0c44ae539e58e0d12b85cd46a7817702673810d8d4ccdb5b294f0f8545379462`; ESI.docx `d793870cfe27000fea165419f8623b8a2ebf0857e9d6cd6eccf14e18c97286ab`.
- Protocol 0.1 (with 2026-11-04 amendment). Extractor/reviewer: Claude (AI), 2026-11-05, same-extractor checks. Status: **ai_checked; partial human check by BB, 2026-11-26: headline OP006 Fig. 3 conversions (~73% CH4, ~55% CO2; E010) confirmed approximately; paper confirmed silent on the power method and ballast boundary (E004; exclusion inferred, C005); no changes (human_checks/summary.csv). Other records human verification pending.**
- Coverage: full manuscript and ESI read. Most results are in figures only: Figs. 3, 4, 6 and 7 read by eye from the embedded 300 ppi images (~0.5-1 point for conversions, ~0.2-0.3 kJ/L for SEI, ~0.01 for H2/CO). The kinetic model (Sections 2.2, 3.5; ESI Section 2) is recorded as context only.
- Records: [evidence.csv](evidence.csv), 33 records (SRC015-E001-E027 source; E041-E046 reviewer calculations). Calculations C001-C006 in [calculations.py](calculations.py).
- Selection: record R009 in [search_and_selection_log.md](../../logs/search_and_selection_log.md).

## Electricity supply

**Classification: DC atmospheric pressure glow discharge (APGD), "warm" plasma (model gas temperature 2000-3000 K, E/N ~45 Td), confined in a ceramic tube; no catalyst, no external heating.**

| Quantity | Extraction | Evidence |
|---|---|---|
| Plasma scale | 97-145 W plasma power (reviewer: SEI x flow; SEI 3.4-12.5 kJ/L read from Fig. 4); 20-35 mA | E012, E042 |
| Supply | Technix HV DC supply, up to 30 kV / 40 mA, with a **300 kOhm series ballast resistor**; supply voltage after ignition ~10-15 kV, read from the supply | E002-E003 |
| Power measurement | Not described. SEI = "plasma power" / inlet flow; no power values tabulated. The implied plasma voltages (3.9-4.7 kV) plus the ballast drop (7.5-10.5 kV) give 11.4-14.6 kV, matching the reported supply voltage, so plasma power appears to exclude the ballast (C005) | E004, E045 |
| Total process energy | Wall power not reported. Ballast dissipation I^2R = 188 W at 25 mA and 368 W at 35 mA, i.e. 1.6-2.6x the plasma power; the plasma receives only 28-39% of the supply output (C005) | E003, E045 |

## Reactor configuration

Stainless-steel (310S) cathode pin and anode plate. The cathode and discharge region sit inside a Macor ceramic tube of 2.5 mm inner radius, which confines the ~4 mm wide glow so that most of the gas passes through it. Gas enters through a ~1 mm groove in the cathode (vortex flow, cools the cathode); the anode plate is 22 mm from the cathode tip, with a central exit (E001). Products pass a liquid trap before the GC; N2 internal standard (10% of the inlet flow) is added after the reactor (E005).

## Operating conditions

CO2/CH4 feed with 15, 25 or 35% CH4; no diluent. Total flow 0.5, 1 or 2 L/min; current 20-35 mA; atmospheric pressure (E006). Litres converted with the authors' 24.05 L/mol (E007), which reproduces their eV/molecule values. Higher current or lower flow overheated and damaged the ceramic tube, cathode and resistor; CH4 above 35% made the plasma unstable due to carbon (E015).

| OP | CH4 (%) | I (mA) | Q (L/min) | SEI (kJ/L) | P (W) | Note | Evidence |
|---|---|---|---|---|---|---|---|
| OP001 | 25 | 25 | 1.0 | 7.1 | 118 | reference condition | E010, E012 |
| OP002 | 25 | 35 | 1.0 | 8.6 | 143 | authors' lowest EC | E013 |
| OP003 | 25 | 25 | 0.5 | 11.7 | 97 | headline conversion (94% CH4) | E011 |
| OP004 | 35 | 25 | 0.5 | 12.5 | 104 | authors' highest X_tot | E013 |
| OP005 | 25 | 25 | 2.0 | 3.4 | 113 | lowest SEI | E010, E012 |
| OP006 | 35 | 35 | 1.0 | 8.7 | 145 | highest H2/CO | E010, E016 |

## Performance indicators

| OP | X_CO2 (%) | X_CH4 (%) | X_tot (%) | H2/CO | Y_H2 (H-based, %) | Evidence |
|---|---|---|---|---|---|---|
| OP001 | ~45.5 | ~73.0 | ~52 | ~0.36 | 37 (calc.) | E010, E016, E043 |
| OP002 | ~55.1 | ~85.3 | 62 +- 1 | ~0.33 | 40 (calc.) | E010, E013, E016 |
| OP003 | 63.7 +- 0.4 | 94.28 +- 0.07 | 71 +- 3 | ~0.31 | ~42 (Fig. 7) | E011, E016, E018 |
| OP004 | ~66.4 | ~86.8 | 74 +- 3 | 0.60 +- 0.01 | ~60 (Fig. 7) | E013, E016, E018 |
| OP005 | ~19.6 | ~36.3 | ~23.8 | ~0.475 | 22 (calc.) | E010, E016 |
| OP006 | ~54.8 | ~73.5 | ~61 | 0.628 +- 0.009 | 53 (calc.) | E010, E016 |

- C-based CO selectivity 95-100%; C2 (mainly C2H2) at most 3.75%. Much of the hydrogen leaves as water: H-based S_H2O falls from 71 to 26% and S_H2 rises from 24 to 69% as CH4 rises from 15 to 35% (25 mA, 0.5 L/min; E017). H2/CO stays below 0.65, so the syngas is CO-rich.
- Water is not measured; it is calculated from the O balance (E021). Carbon balance "always very close to 1"; closure values not tabulated; some solid carbon deposits (E019). Liquid contains 24-204 ppm oxygenates (E020).
- Gas expansion and liquid removal corrected with an N2 internal standard (E005). Blank plus three plasma measurements per condition (E022).
- EC (kJ/L) is nearly constant with current and flow (13-16 kJ/L), because conversion rises in proportion to SEI (E014).

### Energy metrics

- **Power-basis metrics (plasma power; no external heat; 24.05 L/mol; C002-C003):**

| OP | SEI_CH4 (kJ/mol) | EC_CH4 (kJ/mol) | per CH4+CO2 conv. (eV) | EC_H2 (kJ/mol) | EY_H2 (g/kWh) | eta_P,LHV (%) |
|---|---|---|---|---|---|---|
| OP001 | 683 | 936 | 3.38 | 934 | 7.8 | 59.3 |
| OP002 | 827 | 970 | 3.42 | 1031 | 7.0 | 58.3 |
| OP003 | 1126 | 1194 | 4.09 | 1339 | 5.4 | 51.6 |
| OP004 | 859 | 990 | 4.24 | 717 | 10.1 | 54.9 |
| OP005 | 327 | 901 | 3.56 | 746 | 9.7 | 59.4 |
| OP006 | 598 | 813 | 3.54 | 560 | 13.0 | 62.3 |

  CO = S_CO,C x carbon converted (0.95 from Fig. 7 at OP003-OP004, 0.97 elsewhere); H2 = H2/CO x CO. This reproduces the Fig. 7 H2 yields (42 and 60%) at OP003-OP004. If the flows are at 0 degC (22.414 L/mol), per-mol energies fall ~7%.
- **Author metrics:** EC = SEI / X_tot, per molecule of CH4+CO2 converted: 13.9-17 kJ/L, 3.5-4.2 eV/molecule, below the 4.27 eV target of Snoeckx and Bogaerts (E008-E009, E013). Reproduced (3.38-4.24 eV). The low per-molecule cost partly reflects CO2-rich feeds (65-85% CO2): EC_CH4 is 2.4-3.5x higher than the per-molecule figure.
- **eta_HHV (partial):** 31.7-53.4%, f_electric 0.27-0.56; supply and ballast losses excluded (C004).
- **Supply-output basis (C005):** including the ballast loss, EC_CH4 rises to 2392-3490 kJ/mol (2.6-3.6x). The ballast is a laboratory stabilisation method; a current-controlled (active) DC supply could replace most of it, but each glow needs its own current limiting, which matters for scale-up by numbering up.
- **Energy completeness:** included: plasma power. Omitted: ballast and supply losses, wall power. Heat lost to the ceramic tube and electrodes not quantified (E025). Outlet gas leaves hot and unrecovered.

## Reporting quality

| Item | Answer | Reason and evidence IDs |
|---|---|---|
| Q1 Power measurement | partly | "Plasma power" used for SEI but the method is not described; values only as SEI in a figure. Ballast and supply losses not reported (E004, E012). |
| Q2 Feed definition | partly | CH4 fraction, total flow and current clear; the litre reference is given only via the 24.05 L/mol "normal conditions" in the eV conversion; pressure stated only as atmospheric (E006-E007). |
| Q3 Product analysis | yes | Calibrated GC (TCD), N2 internal standard added after the reactor, liquid analysed by GC and HPLC; H2O by atom balance (E005, E020-E021). |
| Q4 Balance closure | partly | Carbon balance "always very close to 1" and selectivity sums ~100%, but closures not tabulated; H and O closure enforced by the water calculation (E019, E021). |
| Q5 Temperature | no | No temperature measured; 2000-3000 K is a model input taken from a CO2 APGD simulation (E023). |
| Q6 Controls | not_applicable | No catalyst; blank (plasma-off) measurement for each condition used as the inlet reference (E022). |
| Q7 Repeatability | yes | Three plasma measurements per condition, error bars on all figures (E022). |
| Q8 Stability | no | Run duration and time on stream not reported; carbon deposits and component damage at the edges of the operating range (E015). |
| Q9 Energy completeness | partly | No external heat or steam, but ballast and supply losses, wall heat loss and outlet enthalpy not reported (E004, E025). |

- **Confidence in conversion/product results: higher.** Internal-standard expansion correction, calibrated GC, triplicates with small error bars, two headline points stated in the text; other values figure-read.
- **Confidence in energy results: moderate.** Author EC is reproduced and consistent with the reported supply voltage, but the plasma-power method is not described, the litre reference is only implied, and SEI comes from a figure.

## Reported system information

- **Boundary:** confined APGD reactor; supply, ballast resistor, liquid trap and GC outside the energy boundary.
- **Mass flows:** CO2 and CH4 in; dry gas by GC; water by O balance; solid carbon not measured (C balance close to 1).
- **Energy flows:** plasma power only. The ballast resistor dissipates more power than the plasma; heat lost through the ceramic tube and in the hot outlet gas is not quantified.
- **Hardware:** single ~0.1 kW glow, 0.5-2 L/min; operating window limited by overheating of the tube, cathode and resistor and by carbon above 35% CH4 (E015). No costs, lifetime or scale-up data. The authors describe the design as "very simple, inexpensive".

## Missing information and comparison limits

| Field | Status |
|---|---|
| Plasma-power measurement method | not_reported (inferred: supply V minus ballast drop, times I) |
| Point power values | not_reported (from Fig. 4 SEI x flow) |
| Wall power / supply efficiency | not_reported |
| Gas temperature | not_reported (model assumption only) |
| Balance closure values | not_reported (qualitative) |
| Time on stream / run duration | not_reported |
| Outlet temperature, wall heat loss | not_reported |
| Litre reference state | partly (24.05 L/mol in eV conversion) |

Comparison limits: ~0.1 kW, single glow; CO2-rich feeds (H2/CO <= 0.63); much of the H as water. The per-molecule EC favours CO2-rich feeds, so EC_CH4 is the comparable metric. Scale-up would need many parallel discharges, each current-limited.

## Calculations

| ID | Inputs | Method | Result |
|---|---|---|---|
| C001 | E006, E010-E013 | X_tot from X_CO2, X_CH4; SEI read vs EC x X_tot | X_tot within 1 point of author; SEI within 3% |
| C002 | E007, E010-E013 | P = SEI x flow; SEI_CH4, EC_CH4, eV per CH4+CO2 converted | EC_CH4 813-1194 kJ/mol; 3.38-4.24 eV (author 3.5-4.2) |
| C003 | C002, E016-E018 | CO from S_CO,C; H2 from H2/CO; EC_H2, EY_H2, eta_P,LHV | eta_P,LHV 51.6-62.3%; Fig. 7 Y_H2 reproduced |
| C004 | C003 | Partial eta_HHV | 31.7-53.4% |
| C005 | E002-E003, C002 | Ballast I^2R, implied voltages, supply-output EC_CH4 | Plasma 28-39% of supply output; EC_CH4 2392-3490 kJ/mol |
| C006 | E009 | DRM enthalpy per molecule | 2.56 eV per pair; 1.28 eV per reactant molecule |

## Revisions

None.

## Plasma characteristics

| Characteristic | Reported |
|---|---|
| Regime | DC atmospheric pressure glow discharge, confined; "warm plasma" with mainly vibrational excitation (E024) |
| Gas temperature | Not measured; 2000-3000 K assumed in the model from a CO2 APGD fluid simulation (E023) |
| Electron temperature/density, E/N | Model only: Te ~0.8 eV, ne ~3.5e11 cm-3, E/N ~45 Td (25% CH4, 30 mA, 1 L/min) (E024) |
| Diagnostic basis | Supply voltage and current; GC; no optical or electrical diagnostics reported (E003) |
