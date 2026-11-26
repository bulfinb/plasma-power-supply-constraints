# Zhu et al. (2019): gliding arc plasma catalytic steam methane reforming, ~250 W

## Source and review

- Source ID: **SRC012**. Xiaobing Zhu, Xiaoyu Liu, Hao-Yu Lian, Jing-Lin Liu and Xiao-Song Li, "Plasma catalytic steam methane reforming for distributed hydrogen production," Catalysis Today 337 (2019) 69-75. DOI: https://doi.org/10.1016/j.cattod.2019.05.015. Dalian University of Technology.
- Documents: [manuscript.pdf](../manuscript.pdf), 7 pages (printed page = PDF page + 68); [ESI.pdf](../ESI.pdf), 3 pages (Figs. S1-S3). Retrieval date unknown.
- SHA-256: manuscript.pdf `0a61242d63ad528d080aa7ad2fa1ebf6c746b9c45787fae2e8ec054a85ba7805`; ESI.pdf `c380e29d47bcfbc127d24604e9271bc06478afdd31fb575591dc7e6a93fc8169`.
- Protocol 0.1 (with 2026-11-04 amendment). Extractor/reviewer: Claude (AI), 2026-11-05, same-extractor checks. Status: **ai_checked; partial human check by BB, 2026-11-26: headline OP003-OP004 conditions and conversions (E011, E013; plasma alone and plasma + catalyst) confirmed from the text; author efficiency definition (CO at the H2 LHV) confirmed (E006); no changes (human_checks/summary.csv). Other records human verification pending.**
- Coverage: full manuscript and ESI read. Values taken from text and Table 1 (figures not digitised). Catalyst characterisation (XRD, XPS, EDS) recorded briefly. Table 2 / Fig. 8 literature comparison not extracted.
- Records: [evidence.csv](evidence.csv), 26 records (SRC012-E001-E021 source; E041-E045 reviewer calculations). Calculations C001-C005 in [calculations.py](calculations.py).
- Selection: record R007 in [search_and_selection_log.md](../../logs/search_and_selection_log.md).

## Electricity supply

**Classification: DC gliding arc ("warm plasma") at atmospheric pressure, followed by a post-plasma Ni/CeO2/Al2O3 catalyst bed in an insulated reactor with no extra heating.** The plasma is the only heat source for the reactor; steam is raised in an external vaporizer (E002, E004, E020).

| Quantity | Extraction | Evidence |
|---|---|---|
| Plasma scale | 149-246 W discharge power; 246 W at the optimum | E007, E011 |
| Power measurement | DC: P = (supply voltage - ballast-resistor voltage) x current (built-in ammeter); 2.5-2.8 kV, 53-95 mA | E001, E007 |
| Total process energy scale | Not reported: ballast-resistor dissipation, supply losses and vaporizer duty excluded | E001, E004 |

Indicative steam-raising duty at the optimum (2.25 SLM steam): ~78 W, 32% of the discharge power (C005; reviewer estimate, not reported).

## Reactor configuration

Stainless-steel reactor insulated with ceramic fibre; gliding arc zone, 4 cm gap, then 10 g (3.5 cm) of Ni/CeO2/Al2O3 (11 wt% Ni, 8 wt% Ce on 1-2.5 mm gamma-Al2O3), GHSV 18,000 ml g-1 h-1 (E002-E003). Catalyst reduced in situ, no pre-reduction (E019). Thermocouples along the bed centre and on the wall.

## Operating conditions

Atmospheric pressure. Feed CH4 + steam only; SLM at 0 degC (reproduces the authors' SEI; C001). SEI is per mol of total feed (CH4 + H2O).

| OP | Configuration | SEI (kJ/mol) | S/C | Ft (SLM) | P (W) | Evidence |
|---|---|---|---|---|---|---|
| OP001 | Plasma alone | 80 | 2 | 2.5 | 149 | E007-E008 |
| OP002 | Plasma alone | 110 | 2 | 2.5 | 206 | E007-E008 |
| OP003 | Plasma alone (optimum conditions) | 110 | 3 | 3.0 | 246 | E011, E013 |
| OP004 | Plasma + Ni catalyst (optimum) | 110 | 3 | 3.0 | 246 | E011-E013, E017 |

Catalyst-bed temperature at OP004: 977 degC at entry, 726 degC after 2 cm, 651 degC at exit; wall ~605 degC (E012). Plasma-zone gas temperature not measured. Duration: 6 h stability test at OP004 (E017-E018).

## Performance indicators

| OP | X_CH4 (%) | X_H2O (%) | Selectivity CO / CO2 / C2Hx (C-based, %) | Balance | Evidence |
|---|---|---|---|---|---|
| OP001 | 40 | 15 | 69 / 4 / 26 | C ~100 +/- 3% | E008 |
| OP002 | 56 | 24 | 74 / 7 / 17 | C ~100 +/- 3% | E008 |
| OP003 | 65 | 21 | 77 / 10 / ~13 | ~100% | E013-E014 |
| OP004 | 90 | 42 | 52 / 46 / 0 | ~100% | E013-E014, E017 |

The catalyst raises CH4 conversion from 65 to 90% at the same power, close to equilibrium at the 651 degC bed-exit temperature, and removes the C2Hx (mainly C2H2) made in the plasma (E013-E014). The shift reaction over the catalyst converts CO to CO2 + H2. Dry product at OP004: H2 76% (t-H2 79%), CO 11%; t-H2 2.7 SLM (E016). Conversion and selectivity were steady over 6 h, with no change in catalyst element distribution (E017, E019).

### Energy metrics

- **Power-basis metrics (discharge power; steam vaporizer and ballast resistor excluded; C002-C003):**

| OP | SEI_CH4 (kJ/mol CH4) | EC_CH4 (kJ/mol) | EC_H2 (kJ/mol) | EY_H2 (g/kWh) | eta_P,LHV (%) |
|---|---|---|---|---|---|
| OP001 | 240 | 601 | NR | NR | NR |
| OP002 | 332 | 594 | NR | NR | NR |
| OP003 | 441 | 679 | ~250 | ~29 | ~59 |
| OP004 | 441 | 490 | ~144 | ~50 | ~75 |

  H2 flows for OP003-OP004 are reconstructed from CO/CO2 selectivities (3 H2 per CO, 4 per CO2; C2Hx neglected), giving t-H2 2.65 SLM at OP004 against the authors' 2.7. With the indicative steam duty, OP004 EC_CH4 rises to ~646 kJ/mol (C005).
- **Author metrics:** eta = (F_H2 + F_CO) LHV_H2 / (F_CH4 X LHV_CH4 + P) and EC = P / (F_H2 + F_CO), both counting CO as potential H2 (t-H2): 59% and 2.3 kWh/Nm3 (plasma alone), 75% and 1.5 kWh/Nm3 (plasma catalysis) (E006, E015). Our reconstruction gives 56.8/73.3% and 2.42/1.55 kWh/Nm3 (C003). Both exclude the vaporizer heat.
- **eta_HHV (partial):** 48.4% (OP003), 75.6% (OP004); f_electric 0.33. Excludes vaporizer, ballast resistor and supply losses (C004).
- **Energy completeness:** included: discharge power. Omitted: steam generation (~1/3 of P by estimate), ballast-resistor and supply losses. No external reactor heating (insulated).

## Reporting quality

| Item | Answer | Reason and evidence IDs |
|---|---|---|
| Q1 Power measurement | yes | DC discharge power from measured current and resistor-corrected voltage, per condition (E001, E007). Wall power not given. |
| Q2 Feed definition | partly | Ft, S/C and SEI given; SLM reference not stated (0 degC inferred from SEI consistency) (E007, C001). |
| Q3 Product analysis | yes | Two GCs with He and N2 internal standards; water conversion from O balance (E005). |
| Q4 Balance closure | yes | Carbon and hydrogen balances ~100 +/- 3% reported (E008). |
| Q5 Temperature | yes | Axial catalyst-bed and wall temperatures by thermocouple for the catalytic case (E012). Plasma-zone gas temperature not measured. |
| Q6 Controls | partly | Plasma alone vs plasma + catalyst at matched conditions, and equilibrium comparison; no catalyst-only control at the same temperature (E013). |
| Q7 Repeatability | no | No repeats or error bars on conversions. |
| Q8 Stability | yes | 6 h time on stream with steady conversion and selectivity; catalyst characterised before and after (E017-E019). |
| Q9 Energy completeness | partly | No external reactor heat; vaporizer duty and ballast/supply losses not reported (E001, E004). |

- **Confidence in conversion/product results: higher.** Internal standards, closed C and H balances, matched controls, equilibrium comparison and a 6 h test; no repeats.
- **Confidence in energy results: moderate.** Discharge power is point-matched and the author metrics are reproducible, but steam generation (~1/3 of P) and ballast/supply losses are omitted, and the author efficiency counts CO as H2.

## Reported system information

- **Boundary:** insulated gliding arc + catalyst reactor; vaporizer, DC supply and ballast resistor outside the reported energy.
- **Mass flows:** CH4 and steam in; dry outlet by GC with internal standards; water from O balance; C and H balances close.
- **Energy flows:** discharge power only; bed temperature profile shows the plasma heat driving SMR + WGS in the bed.
- **Hardware:** lab scale (~0.25 kW, 3 SLM); no costs or electrode lifetime. Authors claim fast response and compactness for distributed H2 but demonstrate only 6 h.

## Missing information and comparison limits

| Field | Status |
|---|---|
| SLM reference | not_reported (0 degC inferred) |
| Vaporizer duty, steam inlet temperature | not_reported |
| Ballast-resistor dissipation; wall power | not_reported |
| Plasma-zone gas temperature | not_reported |
| Catalyst-only control at bed temperature | not_reported |
| Repeats / uncertainties on conversion | not_reported |
| Outlet H2 and CO flows (absolute) | not_reported except t-H2 2.7 SLM |

Comparison limits: lab scale (~250 W, 0.034 mol/min CH4), the smallest SMR source after Geng. S/C 3. The catalyst bed operates as a plasma-heated thermal reformer (bed 977-651 degC, near equilibrium); the plasma-catalysis benefit here is mainly heat and C2Hx clean-up rather than a demonstrated non-thermal synergy. Author efficiency (t-H2, includes CO) is not our eta_P,LHV and excludes steam heat.

## Calculations

| ID | Inputs | Method | Result |
|---|---|---|---|
| C001 | E007, E011 | SEI = P / total molar feed | Reproduces 80-110 kJ/mol at 0 degC SLM |
| C002 | E007-E013 | SEI_CH4, EC_CH4 | 490-679 kJ/mol |
| C003 | E013-E015 | H2/CO from selectivities; EC_H2, EY_H2, eta_P,LHV; author eta/EC check | Author values reproduced within ~2 points |
| C004 | C003 | Partial eta_HHV | 48.4 / 75.6% |
| C005 | E004, E011 | Indicative steam duty | ~78 W (32% of P) |

## Revisions

None.

## Plasma characteristics

| Characteristic | Reported |
|---|---|
| Regime | DC gliding arc, described by the authors as "warm plasma"; arc elongation and rotation increase with flow (E020) |
| Gas temperature | Not measured in the plasma zone; catalyst-bed entry 977 degC (4 cm downstream), bed exit 651 degC, wall ~605 degC (thermocouples) (E012) |
| Electron temperature/density, E/N, ionization | not reported |
| Diagnostic basis | Discharge current and voltage only |
