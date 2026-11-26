# Source extraction: SRC027

## Source and review

- Source ID / citation / DOI: SRC027. Kaufmann, S.J., Quade, J., Buschmann, J., Chinnaraj, H., Birke, K.P., Rößner, P. (2026). CO2 and CH4 conversion in a rotating DC glow to arc plasma with big discharge gap. J. CO2 Util. 105, 103347. https://doi.org/10.1016/j.jcou.2026.103347 (open access, CC BY).
- Source filenames, document versions and SHA-256 hashes: manuscript.pdf, published version (19 pp., Elsevier, created 23 Feb 2026), SHA-256 `4451d74ce0a578bde37b699de88e5b36d102c1b21e9e03cf6e8a57074dc5c38d`. No supplement (BB: no ESI). Printed page = PDF page.
- Retrieval date: 2026-11-26 (downloaded by BB; identified by BB, search log R030).
- Protocol version: 0.9
- Extractor / date: Claude (AI), 2026-11-26.
- Coverage: full paper; Fig. 13a/b read from a 400 dpi render of p. 14. Pure-CO2 and pure-CH4 experiments noted but not extracted (out of scope, E020).
- Reviewer / date / checks: Claude (AI), 2026-11-26; Fig. 13b groups matched to Fig. 13a and text values; author EC range and power checked (C001-C004).
- Review status: ai_checked; partial human check by BB, 2026-11-26: headline OP002 (E011, E014, E043) confirmed, no changes (human_checks/summary.csv). Other records human verification pending.

## Electricity supply

- DC plasma driver (Cyclize, customised; development of the Renninger et al. driver, SRC022) with voltage-controlled current limitation, fed by an AC-DC supply of max. 5 kW. No ballast resistor (E003).
- Two measured boundaries (E004-E005):
  - **Plasma power** P_P = U_P x I_P at the reactor (HV differential probe, current probe, oscilloscope).
  - **Supply power** P_in = U_supply x I_supply at the power supply feeding the driver. eta_ps,pp = P_P / P_in = 88-94% (E006). Whether the mains-side AC-DC loss is inside P_in is unclear; read as DC supply output, **not wall plug**.
- Plasma scale: 400-1750 W at the supply; abstract 400-1700 W; highest P_P quoted 1660 W at 40 mm (E006, E022). At the selected points, P from SEI x 6 SLM is 540-1430 W plasma (C002, C004).
- No external heat. Resonance of the driver output filter can switch the discharge into a pulsed arc mode at the same mean current, with lower conversion and efficiency (E024).

## Reactor configuration

Pin anode and ring cathode in a stainless-steel ISO-K casing lined with vermiculite; gap 10-40 mm set by cathode size and axial anode position; permanent magnets (21 mT) rotate the cathode spot around the ring; axial (vertical) flow; no catalyst in the performance runs (E002). Ceramic foam above the electrodes in some voltage tests (Fig. 7) only.

## Operating conditions

6 SLM total, CO2/CH4 50/50 or 60/40 molar, no diluent in the main runs (N2 10% only to fit the expansion factor alpha) (E007, E009). Atmospheric pressure, value not stated; no temperature measured (E021). Each biogas run lasted 2-5 min (E017).

| OP | Mixture CO2/CH4 | Gap / mean current | SEI_supply (kJ/L) | SEI_P (kJ/L) | P plasma / supply (W) | Evidence |
|---|---|---|---|---|---|---|
| OP001 | 50/50 | 20 mm / 0.24 A | ~6.0 | ~5.4 (C001) | ~540 / ~600 | E012, E013, E041 |
| OP002 | 50/50 | 40 mm / 0.4 A | 15.9 | 14.3 | ~1430 / ~1590 (C004) | E011, E014 |
| OP003 | 60/40 | 40 mm / 0.4 A | ~12.3 | ~11.0 (C001) | ~1100 / ~1230 | E012, E015, E041 |

OP001 is the lowest EC_CH4 in the paper; OP002 the highest power and conversion; OP003 the 60/40 high-power point with little solid carbon.

## Performance indicators

- **Power boundary:** plasma (U x I at the reactor) and supply (DC supply output feeding the driver); both measured. Not wall plug.
- **External heat:** no.
- Products: CO, H2 (dry gas, IR/TCD analyser after cold trap); H2O not measured; solid carbon at 50/50 (E008, E018).

| OP | X_CH4 (%) | X_CO2 (%) | X_tot (%) | S_C,CO (%) | eta_BGs supply basis (%) | SEI_CH4 plasma (kJ/mol) | EC_CH4 plasma / supply (kJ/mol) | EC_tot plasma (eV) |
|---|---|---|---|---|---|---|---|---|
| OP001 | ~42 | ~38.5 | 40.2 | ~81 | ~57 | 241 | 574 / 640 | 3.11 |
| OP002 | ~66 | ~70 | 68 (text) | ~81 | ~44.5 | 641 | 971 / 1080 | 4.89 |
| OP003 | ~52.5 | ~56 | 54.6 (text 55) | ~93 | ~52.5 | 618 | 1178 / 1313 | 4.69 |

- Core metrics at 22.414 L/mol (SLM reference not stated). At 24.46 L/mol EC_CH4 is 9% higher: 627, 1060, 1285 kJ/mol (plasma) (E042-E044).
- Author's metrics: eta_BGs = alpha(LHV_H2 x_H2 + LHV_CO x_CO) / (SEI + LHV_CH4 chi_CH4 x_CH4,in), LHV basis, plotted on SEI_supply; maxima 68% (60/40) and 60% (50/50) quoted on the plasma basis (x ~1.06). EC = 3.3-4.7 eV per CO2 + CH4 converted on SEI_P (E010, E011, E016).
- EC_CH4 penalises the 60/40 feed (less CH4 per kJ); on EC_tot or eta_BGs the 60/40 runs are better.
- Duration 2-5 min per CO2/CH4 run; no long-term test (E017).

## Reporting quality

| Item | Answer (yes/partly/no/NA) | Reason and evidence IDs |
|---|---|---|
| Q1 Power measurement | yes | Plasma U x I with HV and current probes; supply power also measured (E004-E006). |
| Q2 Feed definition | partly | 6 SLM and molar ratios stated; SLM reference conditions and pressure value not stated (E007). |
| Q3 Product analysis | partly | Calibrated IR/TCD analyser; volume change from an alpha correlation fitted in N2-tracer runs, not measured per run (E008, E009). |
| Q4 Balance closure | no | Only the carbon selectivity to CO is reported (81-96%), which is not a closure; no C/H/O balance; solid carbon not quantified (E013-E015, E018). Changed from partly after GPT cross-check XR015. |
| Q5 Temperature | no | No gas, wall or electrode temperature (E021). |
| Q6 Controls | NA | No catalyst; geometry and mixture varied. |
| Q7 Repeatability | partly | +-5% deviation estimated from sensor and probe accuracy; no repeats or error bars (E011). |
| Q8 Stability | no | 2-5 min runs; carbon deposits at 50/50 (E017, E018). |
| Q9 Energy completeness | yes | No external heat; supply-side power measured (E005, E006). |

- Confidence in conversion/product results: moderate. Calibrated analyser and consistent text/figure values, but per-run conversions are bar-chart readings, alpha is a correlation and runs last minutes.
- Confidence in energy results: moderate. Both boundaries measured with probes, but the SLM reference is not stated, the author EC range is only roughly reproduced (C003) and the quoted 1660 W is ~14% above SEI x flow (C004).

## Gaps and comparison limits

- Conversions and SEI for individual runs only in Fig. 13 (no tables; data on request).
- SLM reference not stated: +-9% on EC_CH4 between 0 degC and 25 degC litres (E042-E044).
- Supply boundary probably excludes the mains-side AC-DC stage; not wall plug.
- 1660 W (text) vs ~1430 W (SEI x 6 SLM) at the highest-SEI point, unresolved (C004); EC uses SEI and is not affected.
- Short runs (2-5 min); carbon deposition at 50/50 not quantified.
- Hardware note: current-controlled power-electronic driver at 88-94% plasma/supply efficiency, no ballast (E006); driver-load resonance can force a pulsed arc mode (E024).

## Calculations

All in outputs/calculations.py (22.414 L/mol main basis; 24.46 printed).

- SRC027-C001 SEI_P / SEI_supply from the text endpoints (5.1/5.7, 14.3/15.9): 0.897; used for OP001 and OP003. Inputs E011. Result E041.
- SRC027-C002 SEI_CH4 = SEI x Vm / x_CH4,in; EC_CH4 = SEI_CH4 / X_CH4, plasma and supply; CH4 feed = 6 SLM x x_CH4 / Vm. Inputs E007, E011, E013-E015, E041. Results E042-E044, E047.
- SRC027-C003 Author EC check: SEI_P x Vm / X_tot over the Fig. 13a points gives 3.10-4.87 eV (22.414) or 3.39-5.32 eV (24.46) against the reported 3.3-4.7. Inputs E012, E016. Result E045.
- SRC027-C004 Power check: SEI x 0.1 L/s at OP002 = 1430 W plasma, 1590 W supply vs text 1660 W and 1750 W. Inputs E006, E011. Result E046.

## Revisions, if any

- 2026-11-26, after GPT cross-check (../../cross_check_log.md XR011-XR015): Q4 changed from partly to no (XR015). No values changed; evidence IDs kept.

## Plasma characteristics, when reported

- Regime: rotating glow / glow-to-arc transition at atmospheric pressure; mean currents 0.24-0.4 A, 1.5-4 kV; rotation 4-5 Hz at 40 mm; short arcs with arc chopping above ~0.42 A in 60/40 (E022).
- Gas temperature: not measured (E021).
- Other diagnostics: high-speed imaging, U-I and P-I mappings, current PSD, SEM of carbon (E023).
