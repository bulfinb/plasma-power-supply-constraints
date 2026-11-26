# Song et al. (2020): dry reforming of methane with a 20-30 kW, 400 kHz inductively coupled plasma torch

## Source and review

- Source ID: **SRC009**. Hohyun Song, Yun-Seong Lee, Geunjae Kwak and Hong-Young Chang, "Study on CH4 dry reforming process by high power inductively coupled plasma torch at atmospheric pressure," Current Applied Physics 20 (2020) 196-204. DOI: https://doi.org/10.1016/j.cap.2019.10.023. KIMM, EN2CORE Technology, KRICT and KAIST.
- Documents: [manuscript.pdf](../manuscript.pdf), 9 pages (PDF page = printed page - 195). No ESI located (search by BB, 2026-11-05). A related KAIST PhD thesis (2019) was not obtained. Retrieval date unknown.
- SHA-256 manuscript.pdf: `052178b73a97cbf541fb012a5f3ccfecd5471da34345ac9f85195fa95a2e2556`
- Protocol 0.1 (with 2026-11-04 amendment). Extractor/reviewer: Claude (AI), 2026-11-05, same-extractor checks. Status: **ai_checked; partial human check by BB, 2026-11-26: headline OP013 (E016-E019) confirmed; BB reads the 22 kW as power-supply (generator) output, as assumed here (E003); no changes (human_checks/summary.csv). Other records human verification pending.**
- Coverage: full text and Figs. 1-9 read; CHEMKIN-PRO simulations (Section 3.4, Figs. 10-11) are modelling and excluded. Fig. 7 (selectivities) not digitised; selectivities can be recomputed from Fig. 6.
- Records: [evidence.csv](evidence.csv), 34 records (SRC009-E001-E027 source; E041-E047 reviewer calculations). Calculations C001-C006 in [calculations.py](calculations.py). E001 = SRC009-E001 below.
- Selection: record R003 in [../../search_and_selection_log.md](../../search_and_selection_log.md).

## Electricity supply

**Classification: atmospheric-pressure inductively coupled (RF) plasma torch, 400 kHz, CO2 (with Ar) as plasma gas; CH4 injected downstream into the plasma tail; no catalyst, no external heating.** The authors do not state a plasma regime or temperature; atmospheric-pressure ICP torches at tens of kW are normally thermal plasmas (reviewer note, not a source claim).

| Quantity | Extraction | Evidence |
|---|---|---|
| Plasma scale | 17-27 kW in the experiments (generator maximum 30 kW) | E001, E012-E020 |
| Supply | 400 kHz RF generator; 21-turn copper coil antenna, L = 25 uH, R = 310 mOhm | E001, E004 |
| Power definitions | "Applied/input power" = generator output; "absorbed power" = from antenna V and I via a circuit model, excluding antenna loss | E002 |
| Boundary actually plotted | **Unclear.** Text p. 8 says plotted experimental power is "delivered power, not the actual power absorbed"; Fig. 8-9 captions say "absorbed power = 22 kW"; Section 3.3 and Eq. (5) use "input power" | E002-E003 |
| Total process energy scale | Generator wall power, cooling and gas supply not reported | - |

We treat P as the generator input/applied (delivered) power. Our recalculation of the authors' ECE and SED reproduces their values with P = 22 kW (C002), confirming that the same nominal P is used throughout, whatever its boundary. Absorbed-power values from the circuit model are never given.

## Reactor configuration

Quartz reaction tube D = 80 mm, L = 267 mm, inside the coil; Ar and CO2 enter with 30 degree swirl through centre, middle and side inlets at the bottom; CH4 enters through an additional inlet above the tube into the plasma tail, because CH4 in the main inlet makes the discharge unstable (E005-E006). Downstream reaction chamber dimensions not given. No catalyst.

## Operating conditions

Atmospheric pressure (E025). Feeds in SLM; reference conditions not stated (0 degC, 1 atm assumed; this reproduces the authors' ECE, C002). Argon (30 SLM) is used for ignition; its flow during the reforming measurements is not stated (E008). No temperature measurement is reported; "900-1000 degC" is a general statement about DRM conditions (E006).

| OP | P (kW) | CO2 (SLM) | CH4 (SLM) | Source of results | Evidence |
|---|---|---|---|---|---|
| OP001-OP003 | 17 / 18.5 / 20 | 20 | 20 | Figs. 4(A), 5(A) | E012, E015 |
| OP004-OP006 | 18 / 20 / 23 | 25 | 25 | Figs. 4(B), 5(B) | E013, E015 |
| OP007-OP009 | 21 / 23 / 27 | 30 | 30 | Figs. 4(C), 5(C), 9(C) | E014-E015, E020 |
| OP010-OP013 | 22 | 30 | 20 / 32 / 34 / 36 | Figs. 6, 8, 9(A,B) | E016-E019 |

Duration: not reported; GC analysis took 10 min per sample (E026).

## Performance indicators

Figure values were read visually from the embedded 300 dpi images (+/-1 point for Fig. 4 conversions; +/-0.3-1 SLM for products). For OP010-OP013 our readings reproduce the authors' Fig. 8 ECE, Fig. 9(B) carbon balance and SED to within 0.2 points (C002), and for OP007-OP009 power / syngas reproduces the Fig. 9(C) SED to within 0.2 kJ/L.

| OP | P (kW) | CO2/CH4 (SLM) | X_CO2 / X_CH4 (%) | H2 / CO (SLM) | C2H2 (SLM) | C balance (%) | Evidence |
|---|---|---|---|---|---|---|---|
| OP001 | 17 | 20/20 | 70 / 77 | 20.0 / 27.0 | NR | NR | E012, E015 |
| OP003 | 20 | 20/20 | 91 / 94 | 35.2 / 29.6 | NR | NR | E012, E015 |
| OP007 | 21 | 30/30 | 86 / 82 | 42.3 / 45.1 | NR | 96.7 | E014-E015, E020 |
| OP009 | 27 | 30/30 | 94 / 94 | 58.8 / 55.5 | NR | 99.9 (text 98.9) | E014-E015, E020 |
| OP010 | 22 | 30/20 | 88.7 / 98.0 | 33.3 / 44.4 | 0.32 | 98.0 | E016-E017, E019 |
| OP013 | 22 | 30/36 | 87.1 / 79.3 | 48.8 / 45.7 | 3.32 | 98.3 | E016-E017, E019 |

All OPs are in calculations.py. The abstract's "95% for both" matches OP009 (94/94%) most closely; it is **not** the condition of the 57% ECE (OP013, CH4 79%) (E021). Increasing CH4 at 22 kW lowers CH4 conversion (98 to 79%) and raises C2 hydrocarbons (C2H2 up to 3.3 SLM; selectivity 1.2 to 10.1%) (E016-E017). Water is not measured; the oxygen balance implies 6.6-8.8 SLM of unmeasured O at OP010-OP013, probably H2O (C002, E046). Coke is inferred from the carbon balance, not measured (E022). At OP009 the H2 reading is 4% above the hydrogen available from converted CH4, within reading error (E015).

### Energy metrics

- **Power-basis metrics (P = generator input/applied power, boundary unclear; no external heat reported; 0 degC SLM; C001):**

| OP | SEI (kJ/L) | SEI_CH4 (kJ/mol) | EC_CH4 (kJ/mol) | EC per mol CH4+CO2 converted | EC_H2 (kJ/mol) | EY_H2 (g/kWh) | eta_P,LHV (%) |
|---|---|---|---|---|---|---|---|
| OP001 | 25.5 | 1143 | 1485 | 778 | 1143 | 6.3 | 35.4 |
| OP003 | 30.0 | 1345 | 1431 | 727 | 764 | 9.5 | 40.2 |
| OP007 | 21.0 | 941 | 1148 | 560 | 668 | 10.9 | 47.9 |
| OP009 | 27.0 | 1210 | 1288 | 644 | 618 | 11.8 | 50.8 |
| OP010 | 26.4 | 1479 | 1510 | 640 | 888 | 8.2 | 45.5 |
| OP013 | 20.0 | 822 | 1036 | 541 | 606 | 12.0 | 47.1 |

  EC_CH4 is 4-6 times the DRM reaction enthalpy (247 kJ/mol). Per mol of CH4 + CO2 converted (the usual DRM energy-cost convention) it is 541-778 kJ/mol (5.6-8.1 eV/molecule). +7% at 20 degC SLM (C006).
- **Author metric:** ECE, Eq. (5) = sum(products x LHV, including C2H2, C2H4, C2H6) / (input power + CH4 converted x LHV CH4); 46.6-56.7% at 22 kW, rising with CH4 flow because C2 products carry more LHV (E010, E018). Our eta_P,LHV counts only H2 and CO, so it is lower (45.5-47.1%) at the same points. LHV of CO printed as 285 kJ/mol.
- **eta_HHV (partial):** 26.8-51.6% (H2 + CO only; generator losses, cooling and gas supply excluded); OP009 51.6%, f_electric 0.58; OP013 43.6% (E047).
- **Energy completeness:** included: RF power at the generator/antenna (boundary unclear). Omitted: generator wall losses, coil and torch cooling, argon supply. No external heat, so no heat-included variant is needed.

## Reporting quality

| Item | Answer | Reason and evidence IDs |
|---|---|---|
| Q1 Power measurement | partly | Generator power given per point; absorbed power method described but values not reported, and the plotted boundary is contradicted in the text (E002-E003). |
| Q2 Feed definition | partly | CO2 and CH4 flows per point in SLM; reference conditions and Ar flow during reforming not stated (E007-E008). |
| Q3 Product analysis | partly | GC with TCD and FID named; calibration and method to obtain product flows in SLM not described; water not measured (E009). |
| Q4 Balance closure | yes | Carbon balance defined and reported (96-99.9%) (E011, E019-E020). O and H balances not reported. |
| Q5 Temperature | no | No temperature measured or reported; 900-1000 degC is a general statement (E006). |
| Q6 Controls | partly | CHEMKIN-PRO simulation comparison only; no thermal-equilibrium or non-plasma control (E023). |
| Q7 Repeatability | no | No repeats or error bars. |
| Q8 Stability | no | No time on stream or stability data (E026). |
| Q9 Energy completeness | partly | No external heating used, so RF power is the main input; generator losses, cooling and auxiliaries not reported. |

- **Confidence in conversion/product results: moderate.** Carbon balance reported and our readings reproduce the authors' derived quantities, but feeds lack reference conditions and Ar flow, water is unmeasured, and there are no repeats or temperatures.
- **Confidence in energy results: moderate.** Power is point-matched and the authors' ECE is reproducible, but the power boundary is internally contradictory and wall power is missing.

## Reported system information

- **Boundary:** ICP torch and reaction tube; GC sampling downstream. Downstream equipment, cooling and generator not described in energy terms.
- **Mass flows:** CO2 and CH4 in; H2, CO, C2 products and residual CO2/CH4 in SLM; water and any Ar not reported; carbon balance 96-99.9%.
- **Energy flows:** RF power only; no energy balance, cooling or heat losses reported.
- **Hardware:** 30 kW, 400 kHz generator; 21-turn coil; 80 mm x 267 mm quartz tube. CO2 throughput capacity rises with power to about 42 SLM at 26 kW (E024). No lifetime, maintenance or costs. Co-author and funder EN2CORE Technology Inc. (E027).

## Missing information and comparison limits

| Field | Status |
|---|---|
| SLM reference conditions | not_reported (0 degC assumed; reproduces author ECE) |
| Power boundary of plotted P; absorbed power values | unclear / not_reported |
| Ar flow during reforming | unclear |
| Gas temperature anywhere | not_reported |
| Water in product; O/H balance | not_reported |
| Product flow measurement method | not_reported |
| Time on stream; repeats | not_reported |
| Generator efficiency; cooling duty | not_reported |
| ESI | none located |

Comparison limits: DRM route, no catalyst; CO2 is the plasma gas, so CO2 conversion is partly plasma dissociation. Significant C2 hydrocarbons (mainly C2H2) at high CH4 flows mean that the author's ECE is not a syngas efficiency. Headline 95% conversion and 57% ECE are different conditions.

## Calculations

All in [calculations.py](calculations.py).

| ID | Inputs | Method | Result |
|---|---|---|---|
| C001 | E012-E017 | SEI, SEI_CH4, EC_CH4, EC per CH4+CO2 converted, EC_H2, EY_H2, eta_P,LHV, partial eta_HHV | Tables above |
| C002 | E010-E011, E016-E020 | Recalculate author ECE (Eq. 5), carbon balance (Eq. 12) and SED (Eq. 15); O deficit | Within 0.2 points of the authors; O deficit 6.6-8.8 SLM |
| C006 | C001 | 20 degC SLM sensitivity | EC_CH4 +7%; ECE 56.7 to 54.5% |

## Revisions

None.

## Plasma characteristics

| Characteristic | Reported |
|---|---|
| Regime | Atmospheric-pressure ICP torch, continuous 400 kHz RF; regime not stated by the authors (normally thermal for this class; reviewer note) |
| Gas temperature | not reported (900-1000 degC quoted only as typical DRM conditions) |
| Electron temperature/density, E/N, ionization | not reported experimentally; CHEMKIN-PRO electron energy balance is a model (E023) |
| Diagnostic basis | Antenna voltage/current for the absorbed-power circuit model (values not given) |
