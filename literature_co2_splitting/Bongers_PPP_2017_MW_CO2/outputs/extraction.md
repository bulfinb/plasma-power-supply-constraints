# Source extraction: SRC018

## Source and review

- Source ID / citation / DOI: SRC018. Bongers, W., Bouwmeester, H., Wolf, B., Peeters, F., Welzel, S., van den Bekerom, D., den Harder, N., Goede, A., Graswinckel, M., Groen, P.W., Kopecki, J., Leins, M., van Rooij, G., Schulz, A., Walker, M., van de Sanden, R. (2017). Plasma-driven dissociation of CO2 for fuel synthesis. Plasma Process. Polym. 14, e1600126. https://doi.org/10.1002/ppap.201600126
- Source filenames and document versions: manuscript.pdf, Wiley **Early View** typeset version (page footer "Plasma Process Polym 2016; 9999: 1-8"; final pagination differs), University of Twente repository, SHA-256 `2cbc559513744bdb1b0436bd8d2212ed48973a5d1cd351a5cc16f2fd59e8ab98`. Printed page = PDF page. No supplement.
- Retrieval date: 2026-11-11 (downloaded by Claude).
- Protocol version: workflow.md 0.7, with the CO2-splitting metrics of [../../literature_review_objectives.md](../../literature_review_objectives.md).
- Extractor / date: Claude (AI), 2026-11-12.
- Coverage: full paper; Figs. 3, 6, 7 read from rendered pages.
- Reviewer / date / checks: Claude (AI), 2026-11-12; SEI and efficiency recalculated from power, flow and conversion (C001-C004).
- Review status: ai_checked; partial human check by BB, 2026-11-25: OP001 (E009) and OP003 (E010-E011) confirmed, Fig. 3b point at 3.1 kW nearer 10% than the text's 11% (human_checks/summary.csv). Other records human verification pending.

## Electricity supply

- IGVP (Stuttgart): 915 MHz magnetron system rated 3-30 kW (circulator, 3-stub tuner, WR-975), TM010 cavity, used up to 10 kW (E002).
- DIFFER: 2.45 GHz, 1 kW (InitSF), TE101 cavity with optional coaxial pin (E004).
- Power basis: "MW power"; whether forward or absorbed is not stated; at DIFFER the tuner minimised reflection (E003). No supply efficiency or wall-plug data.
- Plasma scale: up to 10 kW (915 MHz), the largest microwave CO2 data in the set so far. Vacuum pump power (sub-atmospheric operation) not reported. No external heat.

## Reactor configuration

- 915 MHz: quartz tube ID 30 mm in a TM010 cavity, single 4 mm tangential inlet (forward vortex). Quenching: nozzle after the cavity, exhaust expanding supersonically into a vacuum vessel (E002, E009).
- 2.45 GHz: quartz tube ID 27 mm, double 1 mm tangential inlets; configurations A/B/C (full or half-height waveguide; water-cooled brass quencher with ~5 mm nozzle; ~2 cm Cu quench tube in reverse vortex) (E004, E012).

## Operating conditions

Pure CO2; flows in slm (reference not stated; 0 C reproduces the SEI values, C001).

| OP | Setup | p (mbar) | CO2 (slm) | P (kW, MW) | SEI (eV) | Evidence |
|---|---|---|---|---|---|---|
| OP001 | 915 MHz, FV + nozzle quench | 200 | 11 | 8.1 | 10.3 | E009 |
| OP002 | 915 MHz, FV + nozzle quench | 200 | 11 | 3.1 | 3.9 | E009 |
| OP003 | 915 MHz, FV + nozzle quench | 200 | 75 | 3.1 | 0.6 | E010, E011 |
| OP004 | 915 MHz, FV + nozzle quench | 200 | 75 | 10 | 1.9 | E010, E011 |
| OP005 | 2.45 GHz, RV, convective quench (Exp. 7) | ~400-600 | NR | NR | 0.8 | E013 |

## Performance indicators

- **Power boundary:** microwave power (forward/absorbed unclear). Sub-atmospheric: vacuum pumping excluded.
- **External heat:** no.
- Product: CO2/CO/O2, unseparated.

| OP | alpha = X_CO2 (%) | eta reported (%) | eta = alpha x 2.9/SEI (%) | EC_CO2 (kJ/mol) | EC_CO, MW basis (kWh/Nm3) |
|---|---|---|---|---|---|
| OP001 | 83 | 24 | 23.5 | 1193 | 14.8 |
| OP002 | 47 | 35 | 34.7 | 806 | 10.0 |
| OP003 | ~10 (text 11) | 51 | 50.3 | 556 | 6.9 |
| OP004 | ~22.5 (text 23) | ~36 (Fig.; text 40) | 35.1 | 797 | 9.9 |
| OP005 | ~12.5 | ~46.5 | 45.3 | 618 | 7.7 |

- Author's efficiency: eta = alpha dH/SEI, dH = 2.9 eV (E006). Reproduced within reading precision, except the text's 40% at 10 kW, which conflicts with Fig. 3b and with its own alpha and SEI (E042).
- OP001 is the highest single-pass conversion in the set (83%), at 8.1 kW and 200 mbar. OP003 has the lowest energy per CO so far (6.9 kWh/Nm3 on microwave power) but at ~10% conversion.
- Trade-off: on the 915 MHz system, conversion rises from 47% to 83% while efficiency falls from 35% to 24% as power rises at 11 slm; at 75 slm the efficiency is 36-51% for conversion 10-23% (E009-E011).
- Supersonic expansion at ~1 mbar: eta at most 15% (E008).
- 2.45 GHz: efficiency ~40-47% at 0.8-0.9 eV; quenching and reverse vortex shift the optimum to higher pressure (46% at 500 mbar); stronger fields lower eta (E014).
- Mechanism: OES gives Tg 4000-5700 K with Tvib 9000 K; the authors conclude dissociation is mainly thermal and the results sit near the thermal-equilibrium limit (~50% with ideal quenching); Fridman's high efficiencies below 1 eV are not reproduced (E007, E015, E016).
- Authors raise an upper limit on conversion at high efficiency and suggest integrating SOECs with microwave plasma (E017).
- Duration: not reported.

## Reporting quality

| Item | Answer | Reason and evidence IDs |
|---|---|---|
| Q1 Power measurement | partly | "MW power" stated per point; forward vs absorbed not defined (E003). |
| Q2 Feed definition | partly | Pure CO2 and slm given; reference conditions not stated (0 C inferred, C001). |
| Q3 Product analysis | partly | MS against calibrated mixtures; gas-expansion handling not described (E005). |
| Q4 Balance closure | no | Not reported. |
| Q5 Temperature | yes | Tg and Tvib from OES (C2 Swan bands), method stated (E015). |
| Q6 Controls | yes | Configurations compared at matched SEI; FV vs RV; quench vs none (E012, E014). |
| Q7 Repeatability | partly | Standard errors within 3% for the 2.45 GHz data; none for 915 MHz. |
| Q8 Stability | no | No time on stream; plasma not sustained below 3.1 kW at 75 slm (E010). |
| Q9 Energy completeness | no | No supply efficiency or vacuum pump power at 200 mbar. |

- Confidence in conversion/product results: moderate. Calibrated MS, but expansion handling not stated and no balance.
- Confidence in energy results: lower. Power boundary unclear, sub-atmospheric with pump excluded, and one text value conflicts with the figure.

## Gaps and comparison limits

- **Sub-atmospheric flag:** all 915 MHz data at 200 mbar; vacuum pumping (for SRC016, ~0.4-0.6 kW at 3 kW plasma) is excluded. Not directly comparable with the atmospheric points of SRC016/SRC017.
- Power boundary not defined (forward vs absorbed); no wall-plug data.
- 2.45 GHz flows for Exps. 5-8 not stated per point; OP005 power and flow NR.
- Text vs figure: 75 slm, 10 kW efficiency 40% (text) vs ~36% (Fig. 3b) (E042).
- Document is the Early View version; cite by DOI.

## Calculations

All in outputs/calculations.py. 22.414 L/mol (0 C assumed; reproduces the reported SEI); dH 2.9 eV.

- SRC018-C001 SEI = P/F_CO2. Inputs E009-E011. Result E041.
- SRC018-C002 eta = alpha x 2.9/SEI; EC_CO2 = SEI/alpha; EC_CO = EC_CO2/80.69. Result E041.
- SRC018-C003 Text pair check at 10 kW, 75 slm. Inputs E010, E011. Result E042.
- SRC018-C004 SEI of Exp. (1): 1 kW / 14 slm = 1.00 eV vs stated 0.9. Input E012. Result E043.

## Revisions

- 2026-11-19, after GPT cross-check (cross_check_log.md XC001-XC002): OP005 power changed from "~1 kW" to NR (the 1 kW / 14 slm belong to Exps. 1-2, not Exp. 7); 5700 K condition conflict (Fig. 4 caption vs text) noted, temperature no longer assigned to OP001-OP004. Evidence IDs kept.

## Plasma characteristics

- Regime: microwave, forward or reverse vortex; contracted; dissociation mainly thermal (authors) (E015, E016).
- Gas temperature: 5700 K (915 MHz, 200 mbar; conditions conflict: the Fig. 4 caption gives 0.9 eV, 5 kW, 75 slm, the text says the Fig. 2d setup, 3.1 kW, 75 slm, 0.6 eV; not assigned to any OP) and 4000 K (2.45 GHz, Exp. 1, 200 mbar), rotational temperature of C2 Swan bands taken as Tg, OES at the brightest point of the plasma core (E015). Tvib 9000 K in both.
- Other diagnostics: E/n estimated 70-80 Td from HFSS field simulation (E014).
