# Source extraction: SRC023

## Source and review

- Source ID / citation / DOI: SRC023. Yong, T., Zhong, H., Pannier, E., Laux, C., Cappelli, M.A. (2023). High-pressure CO2 dissociation with nanosecond pulsed discharges. Plasma Sources Sci. Technol. 32, 115012. https://doi.org/10.1088/1361-6595/ad066e
- Source filenames and document versions: manuscript.pdf, published version (IOP; PDF p. 1 is the IOP cover, printed = PDF - 1), SHA-256 `10b1090a3866cb8d6f81055e4ebe5c7cdd58ac87fff4634b103f75133e86d92e`. Supplementary material (reaction mechanism) not obtained.
- Retrieval date: 2026-11-11 (downloaded by BB).
- Protocol version: workflow.md 0.7, with the CO2-splitting metrics of [../../literature_review_objectives.md](../../literature_review_objectives.md).
- Extractor / date: Claude (AI), 2026-11-12.
- Coverage: full paper; Figs. 8 and 13 read from rendered pages. The 0D kinetic model is recorded only as the authors' interpretation.
- Reviewer / date / checks: Claude (AI), 2026-11-12; SEI and efficiency recalculated from pulse energy, frequency, time, pressure and volume (C001-C003).
- Review status: ai_checked. Human verification pending (volume question E042).

## Electricity supply

- FID F1112 nanosecond pulser: two opposite-polarity 15 kV outputs (30 kV), ~10 ns FWHM, 30 kHz (E002).
- **Power boundary: energy deposited in the gap**, from synchronised HV and Rogowski probes; 300-1000 uJ per pulse, i.e. ~9-30 W average (E005). Pulser efficiency (wall to load) not reported; for the P1 class see power_systems/ (0.45-0.92).
- No external heat.

## Reactor configuration

High-pressure batch chamber (to 125 bar), 400 cm3 reduced to 200 cm3 with resin for higher pressures; tungsten pin (10 um tip) to plane, 150 um gap (E003). Not a flow reactor: SEI is per CO2 molecule initially in the chamber (E009).

## Operating conditions

Pure CO2, 3.5-12.2 bar fill, 300 K, processing time 30-1500 s, 30 kHz (E009, E012).

| OP | p (bar) | E_pulse (uJ) | tau (s) | Evidence |
|---|---|---|---|---|
| OP001 | 5.8 | 700 | 420 | E007 |
| OP002 | 5 | 800 (text: 865) | 120 (text: 420) | E008, E011 |

## Performance indicators

- **Power boundary:** deposited pulse energy (plasma); pulser losses excluded.
- **External heat:** no.
- Product: CO, O2 (N_CO ~ 2 N_O2) and CO2; no other gas-phase carbon species; solid carbon deposits not quantified (E004, E006).

| OP | Phi = X_CO2 (%) | eta reported (%) | eta recalculated, 200 / 400 cm3 (%) | EC_CO deposited (kWh/Nm3) |
|---|---|---|---|---|
| OP001 | 14 | 23 | 21.3 / 42.6 | 15.1 (reported eta); 16.3 (recalc, 200 cm3) |
| OP002 | 3.3 (Fig. 8b; text 4) | ~27 | 13.2 / 26.4 | ~13 (from 27%) |

- Author's metric: eta = dH / E_CO = Phi x 2.9 eV / SEI (E009, E010).
- **Volume question (E041, E042):** the headline (5.8 bar) and the 9 bar data reproduce with V = 200 cm3; the 5 bar time series (Fig. 8b, including the 27% point) reproduces only with V = 400 cm3. The text's best-efficiency statement (Phi 4%, 865 uJ, 420 s) gives 4-8% from its own inputs; Fig. 8b places ~27% at 120 s and Phi 3.3%. The paper does not say which volume applies to each data set.
- Efficiency ~20% for Phi <15%, weakly sensitive to pressure (3.5-12 bar), pulse energy and time (E012-E014). Conversion falls with pressure at fixed energy (8% -> 2% from 3.5 to 12 bar) and saturates at ~18% over long times (E011, E012).
- Scale: ~21 W deposited; ~48 mmol CO2 per 420 s batch (~0.007 mol/min equivalent) (E043).
- **Electrode erosion:** gap grew 150 -> 250 um in 240 s (~25 um/min) with carbon deposition (E006). A major durability issue for this electrode design.
- Duration: batches of 30-1500 s.

## Reporting quality

| Item | Answer | Reason and evidence IDs |
|---|---|---|
| Q1 Power measurement | yes | Deposited energy from synchronised V and I probes with stated uncertainty (E005). |
| Q2 Feed definition | partly | Pure CO2, fill pressure and temperature stated; chamber volume per data set ambiguous (E003, E042). |
| Q3 Product analysis | yes | Calibrated GC with two detectors; compressibility corrected (E004). |
| Q4 Balance closure | partly | GC confirms N_CO ~ 2 N_O2; the carbon balance is assumed (Phi = CO/(CO+CO2)), and carbon deposits on the electrode are observed but not quantified (E004, E006). |
| Q5 Temperature | no | Gas temperature only from the model (E015). |
| Q6 Controls | partly | Pressure, pulse energy and time scanned; no plasma-off control needed (batch). |
| Q7 Repeatability | partly | Error bars on figures; repeat procedure not described. |
| Q8 Stability | partly | Time dependence reported; electrode erosion and energy drift during runs (E006). |
| Q9 Energy completeness | no | Pulser efficiency and auxiliaries not reported. |

- Confidence in conversion/product results: moderate. Calibrated GC and N_CO ~ 2 N_O2, but the carbon balance is assumed and the deposits are not quantified.
- Confidence in energy results: lower. Deposited energy only, and efficiencies depend on an unstated volume per data set; the best-efficiency statement does not match its inputs.

## Gaps and comparison limits

- Batch, not flow: SEI per initial molecule; no throughput at scale.
- Deposited energy only; pulser efficiency needed for a wall basis (P1 class).
- Chamber volume per data set (E042).
- Rapid electrode erosion (E006).
- Supercritical-kernel discussion is model-based (E015).

## Calculations

All in outputs/calculations.py.

- SRC023-C001 N0, E_tot, SEI and eta at V = 200 and 400 cm3 for the headline, the text's best-efficiency statement, Fig. 8b and Fig. 13a points. Inputs E007, E008, E011, E013. Results E041, E042.
- SRC023-C002 EC_CO at OP001 from reported and recalculated efficiency. Result E043.
- SRC023-C003 Average deposited power and CO2 per batch. Result E043.
- SRC023-C004 Electrode gap growth rate. Input E006.

## Revisions

- 2026-11-20, after GPT cross-check (cross_check_log.md XC014): Q4 changed from yes to partly and conversion confidence from higher to moderate: only N_CO ~ 2 N_O2 is checked; the carbon balance is assumed and the electrode carbon deposits are not quantified. Summary table and synthesis confidence updated; no values change.

## Plasma characteristics

- Regime: nanosecond repetitively pulsed spark-like discharge, pin-to-plane, 30 kHz; E/N 660-1100 Td (initial, model) (E015).
- Gas temperature: not measured; ~3000 K peak per pulse from the model (E015).
- Other diagnostics: V-I waveforms and pulse energy (Fig. 3); breakdown voltage vs pressure (Appendix C).
