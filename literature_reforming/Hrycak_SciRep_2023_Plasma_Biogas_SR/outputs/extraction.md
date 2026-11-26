# Hrycak et al. (2023): steam reforming of synthetic biogas in a 915 MHz microwave plasma, 4.5-6.5 kW

## Source and review

- Source ID: **SRC010**. Bartosz Hrycak, J. Mizeraczyk, D. Czylkowski, M. Dors, M. Budnarowska and M. Jasinski, "Hydrogen production by the steam reforming of synthetic biogas in atmospheric-pressure microwave (915 MHz) plasma," Scientific Reports 13 (2023) 2204. DOI: https://doi.org/10.1038/s41598-023-29433-y. Open access. Institute of Fluid Flow Machinery PAS (Gdansk) and Gdynia Maritime University.
- Documents: [manuscript.pdf](../manuscript.pdf), 15 pages (printed page = PDF page for pp. 1-13). No ESI located; data "available on reasonable request" (E026). Retrieval date unknown.
- SHA-256 manuscript.pdf: `97b3dba7e1dba374b1cd2cbb88aa1d8055bdab7ed809c7cde2f41a3d6755792a`
- Protocol 0.1 (with 2026-11-04 amendment). Extractor/reviewer: Claude (AI), 2026-11-05, same-extractor checks. Status: **ai_checked** (human_verified withdrawn 2026-11-10). Partial human check by BB, 2026-11-26: headline OP001-OP002 (Table 1 rows 1-2, E010, E011) and the carbon gap (E045) confirmed; NL reference conditions not found in the paper (E044 stays a reviewer inference); no changes (human_checks/summary.csv). Other records human verification pending.
- Coverage: full text, Tables 1-4 and Figs. 4-9. Table 1 (three tabulated points) and Fig. 9 (power sweep) extracted as operating points; Figs. 4, 6-8 used for trends. Table 4 is a literature comparison (not extracted). The setup and power measurement are described in more detail in the authors' ref. 44 (Hrycak et al., Plasma Chem. Plasma Process. 39 (2019) 695), not obtained.
- Records: [evidence.csv](evidence.csv), 34 records (SRC010-E001-E026 source; E041-E048 reviewer calculations). Calculations C001-C005 in [calculations.py](calculations.py).
- Selection: record R004 in [search_and_selection_log.md](../../logs/search_and_selection_log.md).

## Electricity supply

**Classification: atmospheric-pressure microwave (915 MHz) plasma in a waveguide-supplied metal-cylinder source; no catalyst.** Steam is produced separately in an electric induction vaporizer (E001, E004-E005).

| Quantity | Extraction | Evidence |
|---|---|---|
| Plasma scale | 4.5-6.5 kW absorbed microwave power | E002 |
| Power measurement | "Microwave power measuring system" with tuner and plunger; method details in ref. 44 | E001 |
| Steam generation | Induction vaporizer, 0.5-3 kg/h at 250-350 degC; energy not reported | E004 |
| Total process energy scale | Not reported: generator wall power and vaporizer electricity missing | E002, E004 |

Indicative reviewer estimate of the steam duty (20 degC water to 300 degC steam): 1.65 kW at 2 kg/h and 2.48 kW at 3 kg/h, i.e. 25-38% of the absorbed microwave power (C004). The energy yield and our power-basis metrics exclude it.

## Reactor configuration

Metal-cylinder microwave plasma source with a quartz discharge tube; four tangential inlets create a swirl (CH4:CO2 through three, steam through one). A water-cooled centrifuge gas-soot separator sits at the tube outlet (E005, E023). Dimensions are in Fig. 2(a). No catalyst.

## Operating conditions

Atmospheric pressure. Synthetic biogas = CH4 + CO2 only, 40-100% CH4, 3000-12,000 NL/h; steam 0.5-3 kg/h (E006). NL reference not stated; 24.25 L/mol (about 22 degC, 1 atm) is used because it reproduces the authors' own H2 rates and conversions in all three Table 1 rows (C002; XR008). Steam/CH4 molar ratio 0.9-1.8 at the extracted points (C001). 3000 NL/h is the minimum flow for safe operation at 6.5 kW (swirl cooling) (E018). No gas or wall temperatures reported apart from the steam temperature.

Route: mixed (steam + CO2) reforming, except OP002 (100% CH4 + steam = SMR).

| OP | P_abs (kW) | CH4:CO2 (NL/h) | CH4 (%) | Steam (kg/h) | Source | Evidence |
|---|---|---|---|---|---|---|
| OP001 | 6.5 | 6000 | 75 | 3 | Table 1, row 1 (best H2 rate and EY) | E010 |
| OP002 | 6.5 | 3000 | 100 | 3 | Table 1, row 2 (pure CH4, SMR) | E011 |
| OP003 | 6.5 | 3000 | 50 | 2 | Table 1, row 3 (best conversion) | E012 |
| OP004-OP006 | 4.5 / 5.5 / 6.5 | 6000 | 50 | 2 | Fig. 9 power sweep | E020 |

Duration: not reported; stability described only as soot-free operation without discharge extinction (E025).

## Performance indicators

| OP | X_CH4 (%) | X_CO2 (%) [ours] | H2 (g/h) | EY_H2 (g/kWh) | Outlet H2 / CO / CO2 / CH4 (vol%) | C closure [ours] | Evidence |
|---|---|---|---|---|---|---|---|
| OP001 | 48.9 | 43.5 | 239 | 36.8 | 40.0 / 14.3 / 11.8 / 32.0 | 74% | E010, E044-E045 |
| OP002 | 66.1 | NA | 234 | 36.1 | 58.4 / 14.4 / 3.2 / 21.1 | 71% | E011, E044-E045 |
| OP003 | 74.3 | 59.7 | 171.5 | 26.4 | 46.8 / 30.0 / 13.7 / 8.7 | 79% | E012, E044-E045 |
| OP004 | 40.5 | NR | 128.5 | 28.6 | H2 25.1% | NR | E020 |
| OP005 | 42.3 | NR | 162.5 | 29.5 | H2 27.2% | NR | E020 |
| OP006 | 49.4 | NR | 191 | 29.4 | H2 33.3% | NR | E020 |

Table 1 compositions exclude the N2 marker and water (they sum to 100%). C2 hydrocarbons are 0.8-2.9% (mostly C2H2).

**Consistency checks (C002-C003).** Taking the authors' H2 rate with the Table 1 composition gives an outlet flow and a CH4 conversion that match the authors' values exactly at 24.25 L/mol (48.9/66.1/74.3%); at 22.414 L/mol they were 2-4 points higher. So H2 rate and conversion agree, and the authors' molar volume is ~24.25 L/mol. **Carbon closes at only 71-79%**, however: about a quarter of the carbon fed is missing from the gas. The paper says operation was soot-free but also describes a separator to clean "soot formed during the methane conversion" (E023); unquantified solid carbon is one possible cause, an analysis or flow error another. The authors report no carbon balance. Water was not measured, so H and O balances cannot be checked.

Trends: steam above the minimum needed for soot-free operation does not change performance (E015-E016); H2 rate and EY are constant between 3000 and 12,000 NL/h while unconverted CH4 rises from 25 to 57% (E017); H2 rate rises with power while EY stays at ~29 g/kWh (E020). Without steam (dry reforming) the source was limited to 40% CH4 by soot (E024).

### Energy metrics

- **Power-basis metrics (absorbed microwave power; steam generation excluded, not reported; C001):**

| OP | SEI_CH4 (kJ/mol) | EC_CH4 (kJ/mol) | EC_CH4 incl. indicative steam duty | EC_H2 (kJ/mol) | EY_H2 (g/kWh) | eta_P,LHV (%) |
|---|---|---|---|---|---|---|
| OP001 | 126 | 258 | ~356 | 197 | 36.8 | 42.3 |
| OP002 | 189 | 286 | ~395 | 202 | 36.0 | 40.6 |
| OP003 | 378 | 509 | ~639 | 275 | 26.4 | 59.7 |
| OP004 | 131 | 323 | ~442 | 254 | 28.6 | NR |
| OP005 | 160 | 378 | ~492 | 246 | 29.5 | NR |
| OP006 | 189 | 383 | ~480 | 247 | 29.4 | NR |

  OP001-OP002 EC_CH4 is close to the 206-247 kJ/mol reaction enthalpies on microwave power alone. Two things make this optimistic: the steam carries unreported vaporizer energy (+25-38%), and the ~25% carbon gap means part of the "converted" CH4 may have gone to solid carbon (pyrolysis needs only ~75 kJ/mol), which is not reforming. Treat these as lower bounds.
- **Author metrics:** energy yield = H2 rate / absorbed microwave power (g/kWh), best 36.8 (E003, E010). New "energy-CH4 feedstock consumption yield" = EY / CH4 feed (kNL/h), 17.6-4.9 (Table 3; caption says 6.5 kW, text says 4.5 kW; values match 6.5 kW) (E021, C005).
- **eta_HHV (partial):** 24.3% (OP001), 30.9% (OP002), 50.6% (OP003); f_electric 0.12-0.30. Low because half the CH4 leaves unconverted; excludes vaporizer and generator losses (E047).
- **Energy completeness:** included: absorbed microwave power. Omitted: induction vaporizer, generator wall losses, cooling water, gas-soot separator.

## Reporting quality

| Item | Answer | Reason and evidence IDs |
|---|---|---|
| Q1 Power measurement | partly | Absorbed power reported per point; measuring system named but method described only in ref. 44 (E001-E002). |
| Q2 Feed definition | yes | CH4:CO2 flow in NL/h, CH4 fraction and steam kg/h stated per point (E006, E010-E012). |
| Q3 Product analysis | partly | Two GCs; N2 flow marker handles volume change; calibration not described; water not measured (E007). |
| Q4 Balance closure | no | No balance reported; reviewer carbon closure 71-79% (E045). |
| Q5 Temperature | no | Only steam temperature (250-350 degC); no plasma, gas or wall temperatures (E004). |
| Q6 Controls | partly | Dry reforming (no steam) at the same power and flows as a comparison; no thermal or equilibrium control (E024). |
| Q7 Repeatability | partly | Error bars and "+/-5% measurement error", but repeat count not stated (E009). |
| Q8 Stability | no | No time on stream (E025). |
| Q9 Energy completeness | no | Vaporizer electricity and generator efficiency not reported (E002, E004). |

- **Confidence in conversion/product results: moderate.** Tabulated matched points with a flow marker, and H2 rate and conversion agree, but the 71-79% carbon closure, unmeasured water and lack of temperatures limit CO/CO2 values.
- **Confidence in energy results: lower.** Absorbed power is per point, but the steam vaporizer (an estimated 25-38% of the microwave power) is unreported, and the carbon gap may flatter EC_CH4.

## Reported system information

- **Boundary:** microwave plasma source and gas-soot separator; vaporizer and generator outside the reported energy boundary.
- **Mass flows:** inlet CH4, CO2, steam; outlet composition (dry, N2-free) and N2-marker flows; water, solid carbon and balances not reported. Example output flows 4860 and 7020 NL/h (E019).
- **Energy flows:** absorbed microwave power only.
- **Hardware:** 915 MHz generator, metal-cylinder MPS, induction vaporizer (max 3 kg/h), centrifuge separator. Minimum 3000 NL/h for cooling at 6.5 kW. No lifetime, maintenance or costs.

## Missing information and comparison limits

| Field | Status |
|---|---|
| Absorbed-power measurement method | not_reported here (ref. 44) |
| Vaporizer power / steam generation energy | not_reported |
| Generator wall power | not_reported |
| Temperatures (plasma, gas, wall) | not_reported |
| Water in product; solid carbon | not_reported |
| Carbon/elemental balance | not_reported (reviewer 71-79%) |
| Time on stream | not_reported |
| Repeats | not_reported |
| ESI | none located |

Comparison limits: mixed (CO2 + steam) route except OP002 (SMR). Headline maxima (239 g/h, 36.8 g/kWh, 74.3%) come from different points. EC_CH4 is on absorbed microwave power without steam heat; the carbon gap means conversion may partly be pyrolysis.

## Calculations

| ID | Inputs | Method | Result |
|---|---|---|---|
| C001 | E010-E012, E020 | SEI_CH4, EC_CH4, EC_H2, EY_H2, S/C | Energy table above |
| C002 | E010-E012 | Outlet flow anchored on author H2 rate; H2-anchored X_CH4 | Equal to the authors' values at 24.25 L/mol |
| C003 | C002 | Carbon closure; X_CO2; eta_P,LHV; partial eta_HHV | C closure 71-79% |
| C004 | E004 | Indicative steam duty (20 degC water to 300 degC steam) | 1.65-2.48 kW |
| C005 | E021 | Back-calculate EY from Table 3 | 26-29 g/kWh, consistent with 6.5 kW |

## Revisions

- 2026-11-05: extraction informally reviewed by BB and marked human_verified. Reviewer agreed the carbon-closure flag (66-73%) is sufficient; possible causes (soot, flow-marker or analysis error) not pursued further. No values changed.
- 2026-11-10: human_verified status withdrawn at BB's request; returned to ai_checked pending a systematic human check. The 2026-11-05 BB review was informal. No values changed.
- 2026-11-20, after GPT cross-check (cross_check_log.md XR008): molar volume changed from 22.414 to 24.25 L/mol, which reproduces the authors' H2 rates and conversions in all three Table 1 rows. Volume-dependent values updated (+8.2% on SEI_CH4 and EC_CH4; carbon closure 71-79%, was 66-73%; X_CO2, eta_P,LHV, partial eta_HHV, S/C). Author-reported values, EC_H2 and EY unchanged. Evidence IDs kept.

## Plasma characteristics

| Characteristic | Reported |
|---|---|
| Regime | Atmospheric-pressure 915 MHz microwave discharge; regime not characterised in this paper |
| Gas, electron and other temperatures, density, E/N | not reported |
| Diagnostic basis | Microwave power measurement only |
