# Akande and Lee (2022): plasma steam methane reforming in a 915 MHz microwave torch, 15-50 kW

## Source and review

- Source ID: **SRC008**. Olugbenga Akande and BongJu Lee, "Plasma steam methane reforming (PSMR) using a microwave torch for commercial-scale distributed hydrogen production," International Journal of Hydrogen Energy 47(5) (2022) 2874-2884. DOI: https://doi.org/10.1016/j.ijhydene.2021.10.258. Corrigendum: Int. J. Hydrogen Energy 47 (2022) 25876, https://doi.org/10.1016/j.ijhydene.2022.06.004.
- Documents: [manuscript.pdf](../manuscript.pdf), 13 pages (PDF pp. 1-11 = printed pp. 2874-2884; pp. 12-13 reproduce the corrigendum). [erratum.pdf](../erratum.pdf), 1 page (the corrigendum alone). No ESI. Retrieval date unknown.
- SHA-256: manuscript.pdf `c573b98c7c5199ef221ee826df66c889064907ff7c7d66b494cd86aa865f2798`; erratum.pdf `7157aecec222d0f093ef2aa727da1187627826bacd08ec9426cc7c188614fb16`.
- Protocol 0.1 (with 2026-11-04 amendment). Extractor/reviewer: Claude (AI), 2026-11-05, same-extractor checks. Status: **ai_checked; partial human check by BB, 2026-11-26: headline OP003 (E012, E014, E015, E022, E041) confirmed: 96.6% at 32 kW, 60 lpm, S/C 3; H2 rate above the stoichiometric ceiling and the Fig. 10 conflict agreed; no changes (human_checks/summary.csv). Other records human verification pending.**
- Coverage: full text, corrigendum and Figs. 6-10 read. ASPEN Plus simulations (Figs. 4, 6-9) are modelling and excluded. Table 2 is a literature comparison and is not extracted.
- Records: [evidence.csv](evidence.csv), 38 records (SRC008-E001-E030 source; E041-E048 reviewer calculations). Calculations C001-C007 in [calculations.py](calculations.py). E001 = SRC008-E001 below.
- Selection: record R002 in [search_and_selection_log.md](../../logs/search_and_selection_log.md).

**Headline caution.** The paper's main results are internally inconsistent and the corrigendum does not resolve this (section "Consistency checks"). The reported H2 production rate (2247 g/h) and energy yield (70 g H2/kWh) exceed the stoichiometric maximum for the stated methane feed by a factor of 1.7. Use the author's H2 and energy-yield values only with that flag.

## Electricity supply

**Classification: microwave plasma torch (915 MHz, electrode-free), steam as the plasma/swirl gas, no catalyst.** Steam comes from a separate steam generator; methane enters downstream at the reformer gas inlet (E005-E007). The authors describe microwave plasma generally as "warm plasma" (~3000 K gas temperature); no measurement in this study (E028).

| Quantity | Extraction | Evidence |
|---|---|---|
| Plasma scale | 15-50 kW absorbed microwave power (tests at 17, 27, 32, 37, 42, 47 kW) | E003, E012-E017 |
| Power measurement | Absorbed = incident - reflected, directional coupler with bolometric head and HP power meter | E002 |
| Generator | 915 MHz, rated 75 kW (rating, not operating power); WR975 waveguide, 3-stub tuner | E001 |
| Total process energy scale | Not reported: generator wall power (magnetron efficiency), steam-generator duty and auxiliaries missing | E004, E006 |

The authors' energy yield uses absorbed microwave power only (E004). The steam generator is an external heat input of unreported duty. An indicative reviewer estimate for raising 180 lpm of steam from 25 degC water is 4.3-6.2 kW, 13-19% of the 32 kW absorbed (C005); this is not a reported value.

## Reactor configuration

Quartz discharge tube 79 mm ID / 85 mm OD with metal igniter, fed by the waveguide through an E-bend and tapered section (E005). Downstream "plug flow" reformer 0.28 m ID x 2.27 m (about 140 L, C007) with thermocouples along its length; no catalyst (E009). Then heat exchanger, and in the schematic a vapour-liquid separator, compressor and PSA; the PSA was not used, and results are for gas after the reformer and heat exchanger (E025).

## Operating conditions

Atmospheric pressure. H2O/CH4 3-6; total flow 240-420 lpm; reference conditions for lpm not stated (0 degC, 1 atm assumed; +9% in energy metrics at 25 degC) (E011). Reformer temperature gradient 500-650 degC along its length, not point-specific (E010).

| OP | P_abs (kW) | CH4 (lpm) | H2O (lpm) | S/C | Source of results | Evidence |
|---|---|---|---|---|---|---|
| OP001 | 17 | 60 | 180 | 3 | Fig. 6 | E012-E013 |
| OP002 | 27 | 60 | 180 | 3 | Figs. 6-8, 10 | E012-E017, E022 |
| OP003 | 32 | 60 | 180 | 3 | Figs. 7-10; author optimum | E014-E017, E022 |
| OP004 | 37 | 60 | 180 | 3 | Figs. 6-8, 10 | E013, E015, E017, E022 |
| OP005 | 42 | 60 | 180 | 3 | Figs. 7-8, 10 | E015, E017, E022 |
| OP006 | 47 | 60 | 180 | 3 | Fig. 6 | E013 |
| OP007 | 32 | 60 | 300 | 5 | Fig. 9 | E014 |
| OP008 | 32 | 62 | 180 | 2.9 | "Best" outlet composition (Conclusion + corrigendum) | E019-E020 |

Duration: not reported. "Steady plasma flame" under all settings and start-up under 10 min are qualitative claims (E024). No soot observed (E021).

## Performance indicators

### As reported

- CH4 conversion vs absorbed power (S/C 3): 74.6% (17 kW), 85.7% (27), 97.3% (37), 97.7% (47) (E013).
- CH4 conversion vs S/C at 32 kW: 96.6% (3), 98.8% (4), 99.8% (5), ~99.9% (6) (E014).
- H2 production rate: 1532 g/h (27 kW), 2247 g/h (32 kW), ~2230 g/h (37 and 42 kW, Fig. 7) (E015).
- Energy yield (absorbed MW basis): 56, 70, 54 (Fig. 8 ~56), 46 g H2/kWh at 27, 32, 37, 42 kW (E017).
- Outlet composition, "best" case (corrigendum, wet basis): CH4 3.4, H2 63.4, CO 10.4, CO2 6.3, H2O 16.5 mol% at 62 lpm CH4, 180 lpm steam, 32 kW (E019-E020).
- Fig. 10 outlet mole fractions: CH4 0.26/0.14/0.09/0.02 and H2 0.45/0.63/0.58/0.58 at 27/32/37/42 kW (E022).
- Corrigendum: conversion = converted/initial CH4 (mass basis); other corrections are wording only (E018, E029).

### Consistency checks (reviewer calculations)

1. **H2 rate exceeds the stoichiometric ceiling (C001, E041).** 60 lpm CH4 can give at most 4 x 60 = 240 lpm H2, i.e. 1295 g/h at 0 degC (1187 g/h at 25 degC), and at most 40.5 g/kWh at 32 kW, even with complete conversion and complete shift. The reported 2247 g/h and 70 g/kWh are 1.73 times these limits. Coincidentally, 2247 g/h equals 416 lpm of H2 at 0 degC, close to the 420 lpm maximum total inlet flow; we cannot tell whether this reflects a flow-basis error.
2. **Fig. 7 and Fig. 8 disagree at 37 and 42 kW (C001, E042).** Energy yield x power gives 1998 and 1932 g/h; Fig. 7 shows about 2230 g/h at both. At 27 and 32 kW they agree, so the two quantities are not independent: both depend on the same H2 rate.
3. **The corrigendum's "best" composition implies 83% conversion (C002, E043).** CH4/(CH4 + CO + CO2) = 3.4/20.1 means 17% of the carbon leaves as CH4, i.e. X_CH4 = 83.1% (no soot), against 96.6% reported for 32 kW, S/C 3. With carbon-balance flows, H closes to 88% and O to 68%.
4. **Fig. 10 implies much lower conversion than Fig. 6 (C003, E045).** With 3-4 mol H2 per mol CH4 converted, Fig. 10 implies X_CH4 of about 30-37% (27 kW), 53-60% (32 kW), 62-68% (37 kW) and 88-91% (42 kW), against 85.7/96.6/97.3% reported. Fig. 10's CH4 at 32 kW (14%) also contradicts the corrigendum's 3.4%.
5. Minor: the S/C paragraph is printed twice (pp. 7-8); the 37 kW energy yield is 54 in the text and about 56 in Fig. 8; Fig. 7's axis label reads g(H2)kWh; the 32 kW, S/C 3 conversion (96.6%) is above the Fig. 6 trend (~91% by interpolation).

No outlet flow measurement is described (E008), so the method behind the H2 rate cannot be checked.

### Energy metrics

- **Power-basis EC_CH4 (absorbed microwave power; steam generation excluded, not reported) from the authors' conversions (C004, E046):** 511 (OP001, 17 kW), 706 (OP002), 742 (OP003), 852 (OP004), 1078 (OP006), 719 kJ/mol (OP007). These depend on the reported conversions, which checks 3 and 4 put in doubt. If conversion at 32 kW is nearer the 83% implied by the composition, EC_CH4 is about 835 kJ/mol (C002).
- **EC_H2, EY_H2, eta_P,LHV:** not calculated from the author's H2 rate, which is physically impossible as stated. From the corrigendum composition with carbon-balance flows (OP008): H2 about 1055 g/h, EY_H2 33.0 g/kWh, EC_H2 220 kJ/mol, eta_P,LHV 66.8% (C002, E044). These rest on the no-soot assumption and a composition whose H and O balances do not close.
- **External heat:** steam-generator duty not reported. Indicative 4.3-6.2 kW at 32 kW would raise OP003 EC_CH4 to about 840-890 kJ/mol (C005, E047; reviewer estimate only).
- **Author metric:** energy yield = H2 production rate / absorbed microwave power (g H2/kWh); maximum 70 at 32 kW (E004, E016-E017). Compared by the authors with the DOE 60 g/kWh target; that comparison is not valid if the H2 rate is wrong.
- **eta_HHV (partial):** 66.1% at OP008 on composition-derived flows, f_electric 0.44; excludes steam generation, generator losses and auxiliaries (C006, E048). Lower confidence.
- **Energy completeness:** included: absorbed microwave power. Omitted: steam generator, generator (magnetron) losses, cooling, compressor/auxiliaries. Heat exchanger recovery not quantified.

## Reporting quality

| Item | Answer | Reason and evidence IDs |
|---|---|---|
| Q1 Power measurement | yes | Absorbed microwave power from incident minus reflected power with a directional coupler and power meter (E002). Generator wall power not given (covered by Q9). |
| Q2 Feed definition | partly | CH4 and steam flows in lpm with S/C, but reference conditions not stated and steam flow measured by vortex meter (actual or normal volume unclear); 60 vs 62 lpm at 32 kW (E011-E012, E020). |
| Q3 Product analysis | no | Syngas analyser named only; no calibration, wet/dry basis or outlet-flow measurement, so the H2 rate cannot be traced (E008). |
| Q4 Balance closure | no | No balance reported; reviewer checks show H2 above the stoichiometric limit and conflicting conversions (C001-C003). |
| Q5 Temperature | partly | Thermocouples along the reformer; only a 500-650 degC gradient reported, not per point (E010). |
| Q6 Controls | partly | Compared with ASPEN Plus simulation only; no plasma-off or thermal control (E027). |
| Q7 Repeatability | partly | Error bars in Figs. 6-10 and "repeated several times", but error bars undefined and repeat count not given (E023). |
| Q8 Stability | no | No time on stream; only a qualitative "steady plasma flame" (E024). |
| Q9 Energy completeness | no | Steam-generator duty, generator efficiency and auxiliaries not reported (E004, E006). |

- **Confidence in conversion/product results: lower.** Conversions, Fig. 10 compositions and the corrected outlet composition contradict each other, and the H2 rate exceeds the stoichiometric limit.
- **Confidence in energy results: lower.** Absorbed power is properly measured, but the energy yield depends on an impossible H2 rate and the steam-generator heat is unreported.

## Reported system information

- **Boundary:** microwave torch and reformer (absorbed power only); gas analysed after the heat exchanger. Schematic shows separator, compressor and PSA, not operated (E025).
- **Mass flows:** CH4 and steam inlet flows; outlet composition at one point (wet) and CH4/H2 fractions in Fig. 10; outlet flow not reported.
- **Energy flows:** absorbed microwave power only. Steam generator and heat exchanger duties not reported.
- **Hardware:** 75 kW, 915 MHz generator; WR975 waveguide; 79 mm quartz tube; 140 L reformer; no catalyst. The "commercial-scale" description is the authors' characterisation; no operating hours, lifetime, maintenance or costs are reported. The corresponding author is also affiliated with Green Science Corporation (E030).

## Missing information and comparison limits

| Field | Status |
|---|---|
| lpm reference conditions; steam flow basis | not_reported |
| Outlet flow measurement / method for H2 rate | not_reported |
| Analyser calibration; wet/dry basis of Fig. 10 | not_reported |
| Carbon/elemental balance | not_reported |
| Steam generator duty and steam temperature | not_reported |
| Generator (wall) power and efficiency | not_reported |
| Gas/plasma temperature; point-specific reformer temperature | not_reported |
| Time on stream, stability, lifetime | not_reported |
| Error-bar definition; number of repeats | not_reported |
| ESI | not_applicable (none published) |

Comparison limits: the headline H2 rate and energy yield should not be plotted or ranked as demonstrated performance. EC_CH4 can be plotted from the reported conversions, but only with a flag and the alternative 835 kJ/mol value from the composition. Steam generation excluded.

## Calculations

All in [calculations.py](calculations.py).

| ID | Inputs | Method | Result |
|---|---|---|---|
| C001 | E012, E015-E017 | H2 ceiling = 4 x CH4 feed; EY x P vs Fig. 7 | 1295 g/h (0 degC); 40.5 g/kWh at 32 kW; Fig. 7/8 mismatch at 37/42 kW |
| C002 | E019-E020 | Carbon-basis conversion and flows from corrigendum composition | X_CH4 83.1%; H2 1055 g/h; EY 33.0 g/kWh; EC_CH4 835 kJ/mol; eta_P,LHV 66.8% |
| C003 | E022 | Implied conversion from Fig. 10, 3-4 H2 per CH4 converted | 30-37 / 53-60 / 62-68 / 88-91% |
| C004 | E003, E012-E014 | SEI_CH4, EC_CH4 on absorbed power | 511-1078 kJ/mol |
| C005 | E006, E012 | Indicative steam-raising duty | 4.3-6.2 kW |
| C006 | C002 | Partial eta_HHV at OP008 | 66.1% |
| C007 | E009 | Reformer volume and nominal space time | 140 L; ~35 s |

## Revisions

- 2026-11-26 (BB decision): the synthesis and manuscript figure use OP008 (carbon-based X_CH4 83.1% from the corrigendum composition, 62 lpm, 32 kW; EC_CH4 835 kJ/mol; E043, E044) in place of OP003 (reported 96.6%), because the reported conversion conflicts with the corrigendum composition and Fig. 10. No soot is assumed (authors report none); the H and O balances of the composition close at 88% and 68%. Evidence IDs kept.

## Plasma characteristics

| Characteristic | Reported |
|---|---|
| Regime | Atmospheric-pressure 915 MHz microwave steam plasma torch, electrode-free; authors' general description of microwave plasma as "warm" (~3000 K), not measured here (E028) |
| Gas temperature | Not reported for the plasma; reformer 500-650 degC gradient (thermocouples; location unclear) (E010) |
| Electron temperature/density, E/N, other temperatures, ionization | not reported |
| Diagnostic basis | None beyond microwave power measurement |
