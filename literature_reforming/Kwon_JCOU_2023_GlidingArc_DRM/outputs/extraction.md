# Kwon, Kim & Song (2023): dry reforming of methane in a rotating gliding arc with product quenching, ~1.7 kW

## Source and review

- Source ID: **SRC014**. Hyoungjoon Kwon, Taewoo Kim and Soonho Song, "Dry reforming of methane in a rotating gliding arc plasma: Improving efficiency and syngas cost by quenching product gas," Journal of CO2 Utilization 70 (2023) 102448 (open access, CC BY). DOI: https://doi.org/10.1016/j.jcou.2023.102448. Yonsei University and University of Illinois.
- Documents: [manuscript.pdf](../manuscript.pdf), 13 pages (printed page = PDF page); [ESI.pdf](../ESI.pdf), 2 pages (section S1, H2O calculation). ESI.docx has the same content; ESI.pdf used for locators. Retrieval date unknown.
- SHA-256: manuscript.pdf `dd4b950d32cf6b36d95f281478c50568c5182ce6fec1170f34dae8db4482c0c0`; ESI.pdf `ada936305e0f66e58a03f7ac3a8e2ea96975a8a6c415c43c7243eba634532bec`; ESI.docx `0cf52bf5c5338934034b57549ebc93a77ac564b7faa041bd78e7b0c6bc5d49e5`.
- Protocol 0.1 (with 2026-11-04 amendment). Extractor/reviewer: Claude (AI), 2026-11-05, same-extractor checks. Status: **ai_checked; human check: none**.
- Coverage: full manuscript and ESI read. Values from text and Table 1 where given; Figs. 2, 6, 9 and 11 read by eye from 250 dpi renders (~0.5 points, ~10 degC). Equilibrium modelling (Figs. 4-5) recorded as context only.
- Records: [evidence.csv](evidence.csv), 28 records (SRC014-E001-E022 source; E041-E046 reviewer calculations). Calculations C001-C005 in [calculations.py](calculations.py).
- Selection: record R008 in [search_and_selection_log.md](../../logs/search_and_selection_log.md).

## Electricity supply

**Classification: AC rotating gliding arc (RGA), described by the authors as "warm plasma", atmospheric pressure, no catalyst, no external heating; water-cooled quenching rod (QR) downstream.**

| Quantity | Extraction | Evidence |
|---|---|---|
| Plasma scale | 0.92-1.67 kW discharge power (measured SEI 2.3-4.2 kJ/L at 24 SLPM); set values 1000-1800 W | E002-E003, E011 |
| Power measurement | Time-averaged V x I from HV and current probes on an oscilloscope; ~20 kHz AC, several kV, hundreds of mA | E002 |
| Total process energy | Supply wall power not reported. No furnace or steam. Heat removed by cooling water (inner electrode ~20 degC, QR ~7 degC) not reported | E001, E022 |

## Reactor configuration

Conical water-cooled copper inner electrode (32 mm) inside a stainless-steel outer electrode (ID 36.2 mm), minimum gap ~2.1 mm; four 2 mm tangential inlets give a swirling flow; nozzle and 16 mm tubular outlet; water-cooled QR 20 mm after the outlet (E001). Off-axis thermocouples before (TC1) and after (TC2) the QR.

## Operating conditions

Feed CH4 + CO2 + 12 SLPM N2, total 24 SLPM; CH4/CO2 1/3, 1/2, 5/7 and 1 (E004). The SLPM reference is not stated; 0 degC is used here because it reproduces the authors' efficiency (C003). Pressure not stated; taken as atmospheric (E021). Each condition: 10 min stabilisation, sampling, then 3 min of CO2 with the arc on to burn carbon off the electrodes; three repeats (E005).

| OP | CH4/CO2/N2 (SLPM) | SEI (kJ/L) | P (kW) | Quench | TC1 / TC2 (degC) | Evidence |
|---|---|---|---|---|---|---|
| OP001 | 5/7/12 | 4.18 | 1.672 | no | 536 / 246 | E008, E011, E013 |
| OP002 | 5/7/12 | 4.18 | 1.672 | yes (headline) | ~360 / ~101 | E008, E011-E012 |
| OP003 | 6/6/12 | 4.17 | 1.668 | yes | ~370 / ~105 | E008, E014 |
| OP004 | 5/7/12 | 2.3 | 0.92 | yes (low power) | ~233 / ~80 | E008, E013, E016 |

## Performance indicators

| OP | X_CH4 (%) | X_CO2 (%) | X_tot (%; incl. N2) | H2/CO | S_H2 / S_H2O (H-based, %) | Evidence |
|---|---|---|---|---|---|---|
| OP001 | ~52.0 | ~40.6 | 22.4 | 0.91 | 81 / 13.9 | E011, E013, E015 |
| OP002 | 51.1 | 40.2 | 21.9 | 0.95 | 85.4 / 8.6 | E011, E013, E015 |
| OP003 | 50.5 | 40.3 | 22.5 | 1.26 | 87.4 / 4.6 | E014 |
| OP004 | ~26.1 | ~20.0 | 11.1 | NR | NR | E013 |

- Quenching slightly lowers conversion (51.1 vs ~52% CH4) but raises H2 selectivity and yield by suppressing the reverse water-gas shift downstream; water selectivity falls from 13.9 to 8.6% (E015). An uncooled rod gives the same selectivities as no rod, so the effect is due to cooling, not geometry (E017).
- C-based CO selectivity ~90% at 5/7, C2H2 ~5%; C2H2 rises to ~16% at CH4/CO2 = 1 (E015, E009).
- Balances: H and O sums ~100% (water is calculated by atom balance, so these are partly enforced); C sum 97-100%, lowest at CH4/CO2 = 1 where carbon deposits (E009). Gas expansion corrected with an N2 internal standard (E006).
- Conversion rises roughly in proportion to SEI, so EC_CH4 changes little with power (E013).

### Energy metrics

- **Power-basis metrics (discharge power; no external heat; 0 degC SLPM; C002-C003):**

| OP | SEI_CH4 (kJ/mol) | EC_CH4 (kJ/mol) | per CH4+CO2 conv. (eV) | EC_H2 (kJ/mol) | EY_H2 (g/kWh) | eta_P,LHV (%) |
|---|---|---|---|---|---|---|
| OP001 | 450 | 865 | 4.28 | 533 | 13.6 | 53.8 |
| OP002 | 450 | 880 | 4.34 | 516 | 14.1 | 54.7 |
| OP003 | 374 | 740 | 4.27 | 425 | 17.1 | 52.7 |
| OP004 | 247 | 948 | 4.74 | NR | NR | NR (author ~51.5) |

  H2 from the H-based yield (x 2 x CH4 fed); CO from the measured H2/CO. The OP001 H2 yield (42.2%) is inferred: the reported +3.4% increase on quenching is relative, as shown by the H2O change (13.9 to 8.6%) being stated as -38%. At 20 degC SLPM all EC values rise ~7% and eta falls 2-3 points.
- **Author metrics:** eta (Eq. E8) = LHV of H2 + CO out / (SEI + LHV of CH4 converted). This is the same definition as our eta_P,LHV and is reproduced within ~0.6 points: 55.3% (OP002), 53.2% (OP003). Conversion cost = SEI / total conversion including N2 (18.5-20.4 kJ/L) and syngas cost (10.2-11.9 kJ/L) are per litre of total flow, so they include the N2 dilution (E007, E012, E016). The abstract gives 55.3% and Section 3.2 gives 55.6% for the same point (E012).
- **eta_HHV (partial):** 35.5-38.0%, f_electric 0.30-0.34; supply losses and cooling excluded (C004).
- **Energy completeness:** included: discharge power. Omitted: supply losses and wall power. Heat removed by electrode and QR cooling water not reported. Half the feed is N2, which absorbs part of the plasma energy as sensible heat (indicatively ~130 W, ~8% of P, to reach the TC1 temperature; C005).

## Reporting quality

| Item | Answer | Reason and evidence IDs |
|---|---|---|
| Q1 Power measurement | yes | Discharge power by V x I integration from probes on an oscilloscope; measured SEI reported separately from set values (E002-E003). Wall power not given. |
| Q2 Feed definition | partly | Flows, ratios and N2 dilution clear; SLPM reference and pressure not stated (E004, E021). |
| Q3 Product analysis | yes | Calibrated GC (TCD + FID); N2 internal standard for gas expansion; H2O by atom balance (E006). |
| Q4 Balance closure | partly | C sums 97-100% reported; H and O closures are near 100% partly because water is calculated from the balance (E009). |
| Q5 Temperature | partly | Two off-axis thermocouples before and after the QR; authors state they do not give the true gas temperature (E008). |
| Q6 Controls | yes | Quenched vs not-quenched at matched conditions and an uncooled-rod control (E013, E017). No catalyst, so plasma-off controls not applicable. |
| Q7 Repeatability | yes | Triplicates with error bars on all performance figures (E010). |
| Q8 Stability | no | ~10 min stabilisation per sample; electrodes need a CO2 burn-off between runs; no time-on-stream test (E005). |
| Q9 Energy completeness | partly | No external heat or steam, but cooling-water duties and supply losses not reported (E022). |

- **Confidence in conversion/product results: higher.** Internal-standard expansion correction, calibrated GC, triplicates, matched controls and near-closed balances; figure-read values for some points.
- **Confidence in energy results: higher.** Discharge power is measured at each point, there is no external heat, and the author efficiency matches our definition and is reproduced; SLPM reference (~7%) and supply losses are the main gaps.

## Reported system information

- **Boundary:** RGA reactor with QR; power supply, cooling-water circuits and N2 supply outside the reported energy.
- **Mass flows:** CH4, CO2, N2 in; dry product by GC; water by atom balance; solid carbon not measured but inferred from the C sum (3% at ratio 1).
- **Energy flows:** discharge power only; heat to the electrode and QR cooling water not quantified.
- **Hardware:** lab scale, ~1.7 kW, 24 SLPM. Carbon deposits on the electrodes need periodic CO2 burn-off; discharge becomes unstable at CH4/CO2 = 1. No costs or lifetime data.

## Missing information and comparison limits

| Field | Status |
|---|---|
| SLPM reference state | not_reported (0 degC inferred from eta reproduction) |
| Operating pressure | not_reported (atmospheric assumed) |
| Supply wall power / efficiency | not_reported |
| Cooling-water heat duties (electrode, QR) | not_reported |
| True gas temperature | not_reported (off-axis TCs only) |
| Solid carbon (direct measurement) | not_reported |
| Time on stream beyond ~10 min per sample | not_reported |
| H2 yield at SEI 2.3 (OP004) | not_reported (figure only for selectivity; yield not read) |

Comparison limits: 50% N2 dilution lowers the author's per-litre costs and is not present in the other DRM sources; EC_CH4 per mol CH4 converted is unaffected by the dilution. Lab scale (~0.22 mol/min CH4). No catalyst. Short runs only.

## Calculations

| ID | Inputs | Method | Result |
|---|---|---|---|
| C001 | E004, E011, E013-E014 | Total conversion from nominal feed; conversion cost | Within ~2% relative of author values |
| C002 | E003-E004, E011, E013-E014 | P, SEI_CH4, EC_CH4, EC per CH4+CO2 converted | EC_CH4 740-948 kJ/mol; 4.27-4.74 eV |
| C003 | C002, E011-E012, E014-E016 | H2 from yield, CO from H2/CO; EC_H2, EY_H2, eta_P,LHV vs author eta | 52.7-54.7% vs 53.2-55.3% |
| C004 | C003 | Partial eta_HHV | 35.5-38.0% |
| C005 | E004, E008 | Indicative N2 sensible heat | ~134 W (~8% of P) |

## Revisions

None.

## Plasma characteristics

| Characteristic | Reported |
|---|---|
| Regime | Rotating gliding arc, "warm plasma"; authors cite 1000-3000 K gas temperature for GA plasmas from the literature (general description, not measured here) (E020) |
| Gas temperature | Not measured in the arc; off-axis thermocouples downstream: TC1 233-636 degC, TC2 80-280 degC depending on condition and quenching (E008) |
| Electron temperature/density, E/N, ionization | Not reported |
| Diagnostic basis | Voltage and current waveforms (Fig. 3); thermocouples (E002, E008) |
