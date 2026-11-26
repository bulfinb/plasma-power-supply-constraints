# Source extraction: SRC016

## Source and review

- Source ID / citation / DOI: SRC016. Kiefer, C.K., Antunes, R., Hecimovic, A., Meindl, A., Fantz, U. (2024). CO2 dissociation using a lab-scale microwave plasma torch: an experimental study in view of industrial application. Chem. Eng. J. 481, 148326. https://doi.org/10.1016/j.cej.2023.148326
- Source filenames and document versions: manuscript.pdf, published version (CC BY 4.0) from the University of Augsburg repository (OPUS docId 110559), SHA-256 `ef2d75a234e020e0ccd58a4e711e871a8bc3c94e6b6982ada4f16a188bb9a3f2`. PDF page 1 is the repository cover sheet; the article is PDF pages 2-15 (printed pages 1-14, so printed = PDF - 1). The supplementary files (nozzle photo; durability-test data) were not obtained.
- Retrieval date: 2026-11-11 (downloaded by Claude from the repository).
- Protocol version: workflow.md 0.7, with the CO2-splitting metrics of [../../literature_review_objectives.md](../../literature_review_objectives.md).
- Extractor / date: Claude (AI), 2026-11-11.
- Coverage: full manuscript, Sections 1-7, Figs. 1-19, Tables 1-2. Figs. 11, 14 and 15 read from rendered pages.
- Reviewer / date / checks: Claude (AI), 2026-11-11; arithmetic reproduced in outputs/calculations.py (reported EPC 19.6 kWh/Nm3 and eta_p 16.4% reproduced).
- Review status: ai_checked; partial human check by BB, 2026-11-25: the figure points OP001 and OP003 (E003, E004, E010, E015, E018, E019, E021, E022) confirmed, no corrections (human_checks/summary.csv). Other records: no human check.

## Electricity supply

- 2.45 GHz magnetron microwave source (Muegge MH3000S head, ML3000D supply), maximum forward power 3 kW; WR340 waveguides, manual 3-stub tuner (E001).
- Two power boundaries, both measured:
  - **Absorbed microwave power** P_abs = P_in - P_ref (E002). How forward and reflected power were read is not described. Reflected power is small: 27 W at 2.7 kW (E023); coupling efficiency close to 100% (E017).
  - **Wall-plug active power** of the microwave supply and the vacuum pump, measured on all three phases with two Weidmüller Energy Meter 525 units (class 1) and inductive current transformers (E003). Error 1.4% (conservative) (E005). Chiller, gauges and mass flow controllers excluded (E004).
- Microwave source efficiency P_in/P_active,MW rises with power: about 53% at 0.9 kW and 72% at 2.7 kW (E013, E017). This is the largest loss after the plasma itself (E022).
- Vacuum pump: about 400-600 W active, rising with flow, plus 1 kVAr reactive (E014). Needed only for sub-atmospheric runs and for ignition.
- Plasma scale: P_abs 0.6-2.7 kW. Total process input: wall-plug power of the microwave supply and pump, 3.3-4.2 kW at the selected points (E044). No external heating.

## Reactor configuration

- Microwave plasma torch: combined cylindrical (TE10) and coaxial resonator, quartz tube ID 26 mm; tangential injection for a swirl flow (E006).
- Three configurations (E009, Table 1, Fig. 2):
  - standard: four tangential inlets at the bottom, 16 cm quartz tube;
  - nozzle: water-cooled Cu nozzle (10, 5 or 2.5 mm) on an 84 mm tube;
  - cooling channels and reverse vortex: 1.5 mm tangential inlets at the top, water-cooled Cu piece with a 5 mm constriction splitting into four 4 mm channels, on an 84 mm tube.
- Effluent cooled to room temperature in a 2 m double-pipe heat exchanger before analysis (E007). Heat is not recovered.

## Operating conditions

Pure CO2 (grade 3.5, at least 99.95%) except in the impurity tests (E028). Flows in slm at 0 degC, 1013 hPa (E006). "Atmospheric" means the outlet goes straight to the exhaust; "900 mbar" means the pump holds the resonator at 900 mbar (E010).

| OP | Configuration | p | CO2 (slm) | P_abs (W) | Evidence |
|---|---|---|---|---|---|
| OP001 | cooling channels, reverse vortex | atmospheric, pump off | 9.3 | 2700 | E018, E019 |
| OP002 | standard | 150 mbar, pump on | 9.3 | 2700 | E019, E020 |
| OP003 | cooling channels, reverse vortex | 900 mbar, pump on | 3.7 | 2700 | E015 |
| OP004 | cooling channels, durability test | atmospheric, pump off after ignition | 10.2 | 2250 | E024 |

OP001 is the review's headline point (best wall-plug efficiency at atmospheric pressure). OP003 is the highest conversion. OP004 is the 29 h durability test. OP002 is kept to show the sub-atmospheric alternative with pump power included.

## Performance indicators

- **Power boundary:** absorbed microwave power (forward minus reflected) for SEI_p and eta_p; wall-plug active power of the microwave supply plus vacuum pump (energy meters) for eta_tot and EPC.
- **External heat:** no.
- Product separation and recycle: not included. The product is a CO2/CO/O2 mixture; EPC is per Nm3 CO in that mixture.

Results per OP (reported values, with reviewer calculations from outputs/calculations.py; 22.414 L/mol as used by the authors, E012):

| OP | X_CO2 (%) | eta_p (%) | eta_tot (%) | SEI_p (kJ/mol) | EC_CO2 abs / wall (kJ/mol) | EPC (kWh/Nm3 CO) |
|---|---|---|---|---|---|---|
| OP001 | 34.4 +/- 1.6 | 24.9 (C002) | 17.9 | 390 (4.05 eV) | 1135 / 1579 | 19.6 |
| OP002 | 38.6 +/- 1.6 | 27.9 (C002) | 17.9 | 390 (4.05 eV) | 1011 / 1579 | 19.6 |
| OP003 | 56.6 +/- 1.6 | 16.4 +/- 0.5 | ~10.5 (Fig. 11) | 981 (10.1 eV reported) | 1734 / ~2690 | ~33 (C006) |
| OP004 | ~27 (Fig. 15) | ~26 (Fig. 15) | ~17-18 (Fig. 15) | 297 (3.07 eV) | 1099 / ~1600 | ~20-21 (Fig. 15) |

- Author's metrics: eta_p = X * dH / SEI_p with dH = 2.93 eV/molecule (E011); eta_tot = X * dH * F_CO2 / P_active,tot = eta_p * eta_coupling * eta_MWsource * eta_equipment (E012); EPC = P_active,tot / F_CO,out in kWh/Nm3 CO (E012). eta_p and eta_tot are our eta_dH on the absorbed and wall-plug boundaries.
- Reported EPC 19.6 kWh/Nm3 CO is reproduced (E046). For comparison, the Topsoe SOEC stack figure is 3.44 kWh/Nm3 CO (stack level; plasma_shortlist_2026-11-11.md); not yet extracted.
- EPC breakdown at OP001: plasma ~14, microwave source losses ~5.7, reflected ~0 kWh/Nm3 (E022). At OP002: plasma ~12.5, source losses ~5, vacuum pump ~2.3. The pump cost cancels the plasma gain from 150 mbar operation.
- Other results, not separate OPs: highest eta_p in the cooling-channels configuration 27% at X 12.3% (E016); 5 mm nozzle at 900 mbar eta_p up to 29% and X up to 21.6% at different flows (E026); standard configuration near 1 bar limited to X below 20% (E032); EPC minimum 25.0 kWh/Nm3 at 1950 W in the Fig. 13 power scan (cooling channels; flow and pressure not stated in the text) (E023).
- Impurities (E027): 5% N2 raises eta_p to 33.2% (standard, 200 mbar); 2% compressed air drops X to 10.3% in the 5 mm nozzle at atmospheric pressure, attributed to humidity; authors recommend at most about 100 ppm H2O in the feed.
- Duration: 29 h 20 min durability test in four blocks over several days, stable in all figures of merit, start-up 2-3 min (E024, E025). Other runs: power measured over at least 2 min, usually more than 5 min (E005).

## Reporting quality

| Item | Answer | Reason and evidence IDs |
|---|---|---|
| Q1 Power measurement | yes | Absorbed power from forward/reflected; wall-plug active power from 3-phase energy meters with a stated 1.4% error (E002, E003, E005). |
| Q2 Feed definition | yes | Pure CO2 with grade, flows in slm with reference conditions (E006, E028). |
| Q3 Product analysis | partly | Mass spectrometry after a heat exchanger; conversion from relative molar flows, but calibration and gas-expansion handling are described only by reference [30] (E007, E008). |
| Q4 Balance closure | no | No C or O balance or CO/O2 ratio reported. |
| Q5 Temperature | no | No gas temperature measured; ~6000 K cited from literature (E031). |
| Q6 Controls | NA | No catalyst; configurations and pump on/off compared at matched flow and power (E019). |
| Q7 Repeatability | yes | Error bars on X and eta_p; durability test reproducible across days (E015, E025). |
| Q8 Stability | yes | 29 h 20 min test, stable (E024, E025). |
| Q9 Energy completeness | partly | Microwave supply and vacuum pump measured; chiller and small devices excluded; cooling-water heat not recovered; no separation or compression (E004). |

- Confidence in conversion/product results: moderate. Error bars and a long stable test support the values, but the MS method and expansion correction are only referenced and no balance is given.
- Confidence in energy results: higher. Both the absorbed and the wall-plug power are measured with stated methods and errors, and the authors' EPC reproduces.

## Gaps and comparison limits

- EPC and eta_tot are for the CO2/CO/O2 mixture: no CO/O2/CO2 separation, so not comparable with SOEC product-CO figures without a separation step.
- OP003 and OP004 wall-plug values come from figure readings (E021, E025); OP003 is at 900 mbar with the pump on.
- Microwave-source efficiency is for a 3 kW magnetron at the lab; the authors expect higher efficiency at 915 MHz and at nominal power (Section 4.1). Our supply analysis (power_systems/) should use the measured 72% as a lab data point only.
- Durability-test raw data are in a supplementary file not obtained.
- Hardware note: atmospheric ignition fails once the ignition pin is blunted (E029).

## Calculations

All in outputs/calculations.py (run to reproduce). Inputs: flows and P_abs (E015, E019, E024), X (E015, E018, E020, E025), eta_tot (E018, E020, E021, E025), dH 2.93 eV (E011), Vm 22.414 L/mol (E012).

- SRC016-C001 SEI_p = P_abs / F_CO2 (kJ/mol). Results E041.
- SRC016-C002 eta_p = X * 282.7 / SEI_p, check against reported eta_p. Results E042; OP003 reproduces 16.4%.
- SRC016-C003 EC_CO2 (absorbed) = SEI_p / X. Results E043.
- SRC016-C004 P_active,tot = X * dH * F_CO2 / eta_tot. Results E044; OP001 equals 2700 W / 0.72 (E013), consistent with no pump.
- SRC016-C005 EC_CO2 (wall) = P_active,tot / (F_CO2 X). Results E045.
- SRC016-C006 EPC = P_active,tot / (CO in Nm3/h). Results E046; reproduces 19.6 kWh/Nm3.

## Revisions

- 2026-11-12: cross-reference added. SRC017 (Hecimovic et al. 2023) reports the same cooled-channel torch in ls/min at 20 C (10, 15, 4 ls/min = 9.3, 14.0, 3.7 slm here); conversions agree. SRC017's reported efficiencies are ~9-10% higher than its own X*dH/SEI (SRC017-E019); the efficiencies in this source are on a consistent 0 C basis and are preferred. Count the torch once in the synthesis.

## Plasma characteristics

- Regime: contracted (filamentary) thermal plasma above about 150 mbar, diffuse below (authors, Section 1); thermal CO2 splitting with recombination limiting near 1 bar.
- Gas temperature: not measured here; ~6000 K in the contracted regime cited from refs. 24 and 26 (E031).
- Other diagnostics: pressure drop across the nozzle (Fig. 6); none other.
