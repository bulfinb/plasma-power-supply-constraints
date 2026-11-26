# Source extraction: SRC028

## Source and review

- Source ID / citation / DOI: SRC028. Kim, S.C., Lim, M.S., Chun, Y.N. (2014). Reduction characteristics of carbon dioxide using a plasmatron. Plasma Chem. Plasma Process. 34, 125-143. https://doi.org/10.1007/s11090-013-9499-8
- Source files and document versions: manuscript.pdf, published version (Springer, 19 pp.), SHA-256 `8593d8a8eeffe0aae472b8d34ce59571343381dc1a4035e13fe0f44d74c95e06`. Printed page = PDF page + 124. No supplement.
- Retrieval date: 2026-11-26 (added by BB).
- Protocol version: workflow.md 1.2.
- Extractor / date: Claude (AI), 2026-11-26.
- Coverage: full paper. Case 1 (pure CO2, Fig. 2) extracted; Fig. 2 read from the embedded 150 ppi image. Cases 2-4 and Refs. 1-2 (CH4 and/or H2O co-feed) are out of scope and only noted (E010).
- Reviewer / date / checks: Claude (AI), 2026-11-26; EDE reproduced from CR, flow and power; carbon-based conversion, O2/CO ratio and SEI, efficiency and energy per CO recalculated (C001-C005). Blind GPT cross-check 2026-11-26 (cross_check_log.md XC016-XC020).
- Review status: ai_checked; partial human check by BB, 2026-11-26: Eq. (1) without expansion factor (E008), Fig. 2b CO2 and CO readings (E012) and the feed preheat in Fig. 1 (E017) confirmed; low O2 queried and explained (E042); no value changes (human_checks/summary.csv). Other records human verification pending.

## Electricity supply

- 3-phase AC gliding arc ("plasmatron"); supply Unicon Tech. UAP-15K1A, up to 15 kW (15 kV, 1 A). Frequency and waveform not stated (E002).
- Diagnostics listed: HV probe, current probe and oscilloscope "for measuring the electric characteristics" (E002). No voltage, current or power traces are shown.
- Power: "constant plasma input power of 0.6 kW" for every experiment; Eq. (2) calls it the "supplied electric power". How it was set or measured is not stated; the identical value at every flow suggests a setpoint (E004).
- Scale: 0.6 kW, one reactor. No supply efficiency or wall-plug data.

## Reactor configuration

- Three blade electrodes (2 x 95 x 2 mm) at 120 deg, 3 mm gap, Al2O3 support; gas injected through a 3 mm nozzle at the top centre; quartz shell 55 mm x 200 mm (E003).
- No quench section, packing, catalyst or carbon bed.

## Operating conditions

Pure CO2 from a cylinder through an MFC, 6-32 L/min (reference conditions not stated; 22.414 L/mol used, C003). Pressure not stated (downstream suction pump; presumably ~1 atm). Reactor temperature 532 degC at 6 L/min falling to 290 degC at 32 L/min, thermocouple at the reactor top outlet (Fig. 1) (E005, E006). In Fig. 1 the gas line passes through the steam generator (kept at 400 degC) before the plasmatron; whether its heater was on in Case 1 is not stated (E017).

| OP | CO2 (L/min) | P (kW) | SEI (kJ/mol; eV) | Why chosen | Evidence |
|---|---|---|---|---|---|
| OP001 | 14 | 0.6 | 57.6; 0.60 | maximum reported conversion | E011-E013 |
| OP002 | 20 | 0.6 | 40.3; 0.42 | highest EDE and highest carbon-based efficiency | E011, E012, E014 |

## Performance indicators

- **Power boundary:** "plasma input power" 0.6 kW; supply output or discharge power unclear; method not stated.
- **External heat:** yes, on BB's reading of Fig. 1: the CO2 line passes through the steam generator kept at 400 degC; not stated in the text for Case 1 and not counted by the authors (E017). Value not reported; ~16 kJ/mol indicative, which would lower eta on X_C to 30-32% (C005, E045). By BB's decision the headline eta and EC_CO stay on electricity only, with the preheat noted. Heat recovery could not supply it: the products need quenching and the outlet is 290-532 degC. No pumping (other than sampling) or quench gas.
- **Product:** CO2/CO/O2, unseparated. GC-TCD on dry gas (E007).

**Reported conversion is concentration-based.** The authors' CR (Eq. 1) is the drop in CO2 concentration, so for pure CO2 CR = 100 - y_CO2 (dry %) (E008). Fig. 2b confirms this within reading error. No correction is made for gas expansion (CO2 -> CO + 1/2 O2) or for dilution. The authors' own CO selectivity is only ~55-59% (Fig. 2b; CO selectivity = y_CO / CR): about 40% of the CO2 counted as converted does not appear as CO. Fig. 2b also leaves ~2-2.7% of the dry gas unidentified (N2 is among the analysed species) and gives O2/CO = 0.29-0.41 instead of 0.5 (C002, E042). No carbon black is reported for pure CO2 (E009).

We therefore take the carbon-based conversion X_C = y_CO / (y_CO + y_CO2), which uses the measured CO and is unaffected by expansion or dilution (assumes no solid carbon; none reported).

| OP | CR reported (%) | X_C (%) | X from y_CO2, expansion only (%) | eta on CR (%) | eta on X_C (%) | EC_CO on X_C (kJ/mol; kWh/Nm3) |
|---|---|---|---|---|---|---|
| OP001 | 12.3 (Fig. ~12.4) | 7.8 | 8.8 | 60.4 | 38.4 | 738; 9.1 |
| OP002 | ~10.3 | 6.4 | 7.5 | 72.2 | 44.9 | 630; 7.8 |

- Author metric: EDE = converted CO2 flow / power (L/min W), ~0.0029 at OP001 and ~0.00347 at OP002 (Fig. 2a). It is CR x F / P exactly (C001, E041), i.e. 1.345/EDE kJ/mol at 0 degC. The authors give no energy efficiency.
- Literature context: reviews quote ~61-65% gliding-arc efficiency for this paper (search log CS017, CR022): Snoeckx & Bogaerts, Chem. Soc. Rev. 46 (2017) 5805, p. 5830-5831 ("the highest experimentally reported and also calculated energy efficiency being 65%", refs. 97, 160; optimum SEI 0.45 eV per molecule attributed to Kim) and Xu et al., Green Chem. 2025 (GAD efficiency "a maximum of 61.55%", ref. 123) (../../literature_reviews/). That matches efficiency computed from the reported CR (60-72% across 14-20 L/min). On the CO actually measured, the efficiency is ~38-45% and the energy per CO 7.8-9.1 kWh/Nm3 (plasma input power, 0 degC flow basis).
- Trend: CR rises with flow to a maximum at 14-17 L/min, then falls; X_C follows the same pattern (2.7-7.8%). EDE peaks at 17-20 L/min (E011-E015).
- Co-feed cases (out of scope): CH4 raises CR to 34.5%, CH4 + H2O to 43%, H2O alone lowers it to 7.8%; carbon black forms with CH4 (E010).
- Duration: not reported.

## Reporting quality

| Item | Answer | Reason and evidence IDs |
|---|---|---|
| Q1 Power measurement | partly | 0.6 kW stated for all points and probes listed, but the method, boundary and supply frequency are not given; likely a setpoint (E002, E004). |
| Q2 Feed definition | partly | Pure CO2 via MFC; flow reference conditions, purity and pressure not stated (E005). |
| Q3 Product analysis | partly | GC-TCD on dry gas; calibration not described; conversion from concentration drop without expansion correction (E007, E008). |
| Q4 Balance closure | no | No C or O balance reported; reviewer O2/CO 0.29-0.41 and ~2-3% unidentified gas (E042). |
| Q5 Temperature | partly | Reactor temperature given per case range, thermocouple at the reactor outlet (Fig. 1); not given per flow (E006). |
| Q6 Controls | no | No reference case for pure CO2 (co-feed cases are not controls). |
| Q7 Repeatability | no | No repeats or error bars. |
| Q8 Stability | no | No time on stream or steady-state criterion. |
| Q9 Energy completeness | no | Only the 0.6 kW; no supply losses or auxiliaries; possible feed preheat in the steam generator not stated (E017). |

- Confidence in conversion/product results: lower. Conversion is concentration-based without expansion correction, and the paper's own CO selectivity (~57%) shows it overstates the CO formed.
- Confidence in energy results: lower. One fixed power of unstated boundary and method; flow reference unknown; efficiency only via the reviewer's carbon-based conversion.

## Gaps and comparison limits

- Reported CR (12.3%) is ~1.6 x the carbon-based conversion (7.8%); efficiencies quoted from this paper in reviews (~61-65%) rest on CR. Use X_C-based values (E042, E043).
- Power boundary and method not stated; frequency of the 3-phase supply not stated.
- Flow reference conditions not stated: 25 degC instead of 0 degC raises EC_CO by 9% (C003).
- Pressure not stated (assumed ~1 atm).
- Possible feed preheat: Fig. 1 routes the gas through the 400 degC steam generator; not stated for Case 1 (E017, C005).
- The text calls Fig. 2b "energy efficiency and the CO selectivity", but the figure shows only CO selectivity and gas concentrations (E018).
- Fig. 2 read from a 150 ppi image; only figure values for OP002.

## Calculations

All in outputs/calculations.py. 22.414 L/mol (0 degC, workflow 4; no author molar value to reproduce); dH 283 kJ/mol; P = 600 W.

- SRC028-C001 EDE check: EDE = CR x F / P. Inputs E004, E011. Result E041.
- SRC028-C002 Carbon-based conversion X_C = y_CO/(y_CO + y_CO2); dry sum; O2/CO. Input E012. Result E042.
- SRC028-C003 SEI = P/F; eta = X x 283/SEI; EC_CO = SEI/X_C (CO = X_C x F); /80.69 for kWh/Nm3; 25 degC sensitivity. Inputs E004, E011, E012. Result E043.
- SRC028-C004 Expansion-only correction X = (1 - y)/(1 + y/2) from y_CO2. Input E012. Result E044.
- SRC028-C005 Feed-preheat sensitivity: eta = X_C x 283 / (SEI + 16 kJ/mol) (CO2 298-673 K). Inputs E012, E017. Result E045.

## Revisions

- 2026-11-26, after GPT cross-check (cross_check_log.md XC016-XC020): OP001 reported-basis values now use the text CR 12.3% (eta 60.4%, was 60.9% from the Fig. 12.4%; XC017); Fig. 2b prose label noted (E018; XC018); thermocouple location from Fig. 1 (E006; XC019); external heat changed from "no" to unknown, as the feed passes the 400 degC steam generator (E017, C005; XC020). Carbon-based conversion and EC_CO kept (XC016). Evidence IDs kept.

## Plasma characteristics

- Regime: 3-phase AC gliding arc; the authors describe gliding arcs as having "both high and low temperature plasma characteristics" (p. 2).
- Gas temperature: not measured in the discharge; reactor temperature 290-532 degC by thermocouple at the reactor outlet (E006).
- Other diagnostics: none reported (probes listed, no data).
