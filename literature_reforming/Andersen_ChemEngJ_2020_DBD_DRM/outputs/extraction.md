# Andersen et al. (2020): plasma-catalytic dry reforming of methane in a coaxial packed-bed DBD, 45 W

## Source and review

- Source ID: **SRC013**. J.A. Andersen, J.M. Christensen, M. Østberg, A. Bogaerts and A.D. Jensen, "Plasma-catalytic dry reforming of methane: Screening of catalytic materials in a coaxial packed-bed DBD reactor," Chemical Engineering Journal 397 (2020) 125519. DOI: https://doi.org/10.1016/j.cej.2020.125519 (Crossref-confirmed). DTU, Haldor Topsøe and University of Antwerp.
- Documents: [manuscript.pdf](../manuscript.pdf), 8 pages (printed page = PDF page); [ESI.pdf](../ESI.pdf), 8 pages, saved by the user from ESI.docx (same content; ESI.pdf used for locators). Retrieval date unknown.
- SHA-256: manuscript.pdf `f6743c10942e865c9d2362771b00a00012a0f0bc61f960e68c8fa3e8db9ec737`; ESI.pdf `2c843efb30c64ca10efc0fb92a43bac0d70d4d8b9d906b392426396a3b153ecf`; ESI.docx `56574129bf55e2abe15d584f20d076c259de811e0f09121e86284b3e7f3c5ab5`.
- Protocol 0.1 (with 2026-11-04 amendment). Extractor/reviewer: Claude (AI), 2026-11-05, same-extractor checks. Status: **ai_checked; human check: none**.
- Coverage: full manuscript and ESI read. Values from Table 3 and ESI Table S.2; Fig. 1(b) catalyst-only bars read approximately. XRD/SEM details recorded briefly. Table 4 literature comparison noted as context only.
- Records: [evidence.csv](evidence.csv), 32 records (SRC013-E001-E026 source; E041-E046 reviewer calculations). Calculations C001-C005 in [calculations.py](calculations.py).
- Selection: record R020 in [search_and_selection_log.md](../../logs/search_and_selection_log.md).

## Electricity supply

**Classification: non-thermal, atmospheric-pressure coaxial dielectric barrier discharge (DBD), packed with catalyst beads in the discharge (in-plasma catalysis), no external heating.**

| Quantity | Extraction | Evidence |
|---|---|---|
| Plasma scale | 45 W plasma power, fixed for all runs; 3 kHz | E002 |
| Power measurement | TREK HV amplifier; HV probe, Rogowski coil and 10 nF charge capacitor logged on an oscilloscope for continuous power measurement. Exact formula (V-I integral or Lissajous) not stated | E001 |
| Applied voltage / waveform | Not reported | E025 |
| Total process energy | Amplifier wall power not reported. No furnace, steam or preheat, so plasma power is the only process energy input apart from supply losses | E006 |

## Reactor configuration

Alumina tube (ID 17 mm, 2.4 mm wall) as dielectric barrier; stainless-steel mesh outer HV electrode, 10 cm long; 8 mm grounded steel rod inside; 4.5 mm gap; discharge volume 17.7 cm3 (E003). Packed runs fill the discharge volume with ~11 g of 3.5-4.4 mm gamma-Al2O3 spheres, bare or with 10 wt% Ag, 10 wt% Cu or 1 wt% Pt, pre-reduced in an Ar/H2 plasma (E018).

## Operating conditions

Feed 25 Nml/min CH4 + 25 Nml/min CO2 (1:1, no diluent); ~1.16 atm; no external heating; SEI 54 J/ml (E004-E006, E009). The reference state of "Nml" is not stated; the authors' Eq. (7) uses 24.46 L/mol (25 degC), which reproduces their E values (C001), so that basis is used here: F_CH4 = 1.022 mmol/min. Gas or bed temperature under plasma not measured (E026).

| OP | Configuration | Duration before sampling | Evidence |
|---|---|---|---|
| OP001 | Plasma only (empty gap) | 1 h | E013 |
| OP002 | Plasma + Al2O3 | 5 h (5 x 1 h on/off) | E014 |
| OP003 | Plasma + Ag/Al2O3 | 5 h | E015 |
| OP004 | Plasma + Pt/Al2O3 | 5 h | E016 |
| OP005 | Plasma + Cu/Al2O3 | 5 h | E017 |
| OP006 | Catalyst only, plasma off (ambient) | 1 h | E010 |

## Performance indicators

| OP | X_CH4 (%) | X_CO2 (%) | H2/CO | S_H2 (H-based, %) | S_CO (C-based, %) | Unknown C species (%) | Evidence |
|---|---|---|---|---|---|---|---|
| OP001 | 32.6 | 22.4 | 0.899 | 30.6 | 39.8 | 41.8 | E013, E019 |
| OP002 | 27.2 | 21.8 | 0.879 | 33.3 | 41.0 | 40.5 | E014, E019 |
| OP003 | 27.3 | 21.4 | 0.852 | 32.5 | 42.3 | 39.2 | E015, E019 |
| OP004 | 32.5 | 22.1 | 0.840 | 26.3 | 36.7 | 45.4 | E016, E019 |
| OP005 | 32.6 | 16.1 | 1.04 | 25.6 | 32.2 | 48.3 | E017, E019 |
| OP006 | ~1.5 | ~1 | NR | NR | NR | NR | E010 |

- Packing does not raise conversion: Al2O3 and Ag lower CH4 conversion (shorter residence time), Pt matches plasma only, and Cu lowers CO2 conversion because CO reduces residual CuO (E012, E017). No plasma-catalyst synergy.
- By-products: ethane ~11-12%, propane ~3.5-3.9%, methanol 0.7-3.2% (Cu highest), plus traces of C2H4, C2H2, C4, DME, formic acid and ethanol (E019).
- Balances: C 88-90%, H 83-88%, O 88-92%; 39-48% of converted carbon is unidentified. The N2 internal standard shows no gas expansion, so the missing carbon is probably heavier products or solid carbon + H2O (E020-E021).
- Carbon deposits on all metal-containing packings; Fe/Cr/Ni from the inner electrode found on spent Al2O3 (E022).

### Energy metrics

- **Power-basis metrics (plasma power; no external heat; C002-C003, 25 degC molar volume):**

| OP | SEI_CH4 (kJ/mol) | EC_CH4 (kJ/mol) | per CH4+CO2 conv. (eV) | EC_H2 (kJ/mol) | EY_H2 (g/kWh) | eta_P,LHV (%) |
|---|---|---|---|---|---|---|
| OP001 | 2642 | 8103 | 49.8 | 13,241 | 0.55 | 3.8 |
| OP002 | 2642 | 9712 | 55.9 | 14,583 | 0.50 | 3.5 |
| OP003 | 2642 | 9676 | 56.2 | 14,887 | 0.49 | 3.5 |
| OP004 | 2642 | 8128 | 50.1 | 15,453 | 0.47 | 3.4 |
| OP005 | 2642 | 8103 | 56.2 | 15,827 | 0.46 | 2.9 |

  H2 and CO flows are from Table S.2 selectivities x converted moles; recalculated H2/CO 0.85-1.06 matches the authors' 0.84-1.04. At 0 degC molar volume all EC values fall ~9% (OP001 EC_CH4 7425 kJ/mol). EC_CH4 is ~33 times the 247 kJ/mol DRM enthalpy (C005).
- **Author metrics:** E = (CH4 + CO2 converted)/P = 0.183-0.206 mmol/kJ; eta = [X_CO2 x 247 + (X_CH4 - X_CO2) x 65.9/2] / (SEI x 24.46) = 3.43-4.44%, assuming excess CH4 forms ethane (E009, E013-E017). Both reproduced within 0.003 mmol/kJ and 0.05 points (C001). The authors conclude only ~4% of the plasma power goes into conversion (E023).
- **eta_HHV (partial):** 2.6-3.4%, f_electric 0.75; amplifier losses excluded (C004).
- **Energy completeness:** included: plasma power. Omitted: amplifier/supply losses. No external heat or steam (none used).

## Reporting quality

| Item | Answer | Reason and evidence IDs |
|---|---|---|
| Q1 Power measurement | yes | Plasma power from HV probe, Rogowski coil and charge capacitor on an oscilloscope, continuously; formula not stated; wall power not given (E001). |
| Q2 Feed definition | partly | Flows and composition clear; Nml reference not stated (25 degC implied by Eq. 7) (E004, E009). |
| Q3 Product analysis | yes | GC (TCD + FID), N2 internal standard after the reactor, blank feed measurement; effective-carbon method for uncalibrated C4 (E007, E019). |
| Q4 Balance closure | yes | C, H and O balances reported (83-92%); poor closure acknowledged and quantified as unknown species (E020-E021). |
| Q5 Temperature | no | No gas, bed or wall temperature measured; "ambient" refers to no external heating (E026). |
| Q6 Controls | partly | Catalyst-only (plasma off) and plasma-only controls at the same flow; catalyst-only is at ambient, not at the (unknown) plasma-on bed temperature (E010, E013). |
| Q7 Repeatability | yes | Each experiment repeated three times, >=3 GC injections; error bars in Fig. 1 (definition not stated) (E007, E011). |
| Q8 Stability | partly | 5 h cumulative in 1 h plasma on/off cycles with 1 h stabilisation; plasma only 1 h; no continuous run (E008, E011). |
| Q9 Energy completeness | yes | No external heat or steam; only supply losses missing (E006). |

- **Confidence in conversion/product results: moderate.** Conversions are well controlled (internal standard, triplicates, controls), but 39-48% of converted carbon is unidentified and the H balance closes to only 83-88%.
- **Confidence in energy results: higher.** Plasma power is measured continuously at a fixed setting with no external heat, and the author metrics are reproducible; only the Nml reference (~9%) and supply losses are uncertain.

## Reported system information

- **Boundary:** DBD reactor at ambient temperature with plasma power only; HV amplifier and function generator outside the reported energy.
- **Mass flows:** CH4/CO2 in; dry product by GC with N2 internal standard; C, H, O balances 83-92%; unidentified products and solid carbon not quantified; no water measured.
- **Energy flows:** 45 W plasma power only. No temperature data, so heat release in the bed is unknown.
- **Hardware:** lab scale (17.7 cm3 discharge, 50 Nml/min). Electrode material migration and carbon deposition after 5 h. No costs or lifetime data.

## Missing information and comparison limits

| Field | Status |
|---|---|
| Nml reference state | unclear (24.46 L/mol used in Eq. 7) |
| Applied voltage, waveform, Lissajous figures | not_reported |
| Amplifier wall power / supply efficiency | not_reported |
| Gas or bed temperature under plasma | not_reported |
| Identity of 39-48% of converted carbon; solid carbon; water | not_reported |
| Continuous time on stream > 1 h | not_reported |

Comparison limits: tiny scale (1.0 mmol/min CH4, 45 W). One fixed SEI (54 J/ml), deliberately high; the authors and their Table 4 show DBD efficiency is better at lower power (up to 2.2 mmol/kJ, ~4.7 eV per molecule, at 2 W), so this paper is a representative DBD result rather than the best DBD energy figure. CO takes only 32-42% of the converted carbon (C-based selectivity), so EC_H2 and eta_P,LHV are less meaningful than EC_CH4.

## Calculations

| ID | Inputs | Method | Result |
|---|---|---|---|
| C001 | E004, E009, E013-E017 | Author E and eta recomputed | Reproduced at 24.46 L/mol |
| C002 | E002, E004, E013-E017 | SEI, SEI_CH4, EC_CH4, EC per CH4+CO2 converted | EC_CH4 8103-9712 kJ/mol; 49.8-56.2 eV |
| C003 | C002, E019 | H2, CO from selectivities; EC_H2, EY_H2, eta_P,LHV | 2.9-3.8% |
| C004 | C003 | Partial eta_HHV | 2.6-3.4% |
| C005 | C002, E003 | EC_CH4 / 247; empty-volume residence time | ~33x; ~21 s |

## Revisions

None.

## Plasma characteristics

| Characteristic | Reported |
|---|---|
| Regime | Non-thermal DBD; filamentary/surface discharge behaviour discussed from literature only, not observed here (E012) |
| Gas temperature | Not measured; no external heating |
| Electron temperature/density, E/N, ionization | Not measured; authors cite modelling that packing raises the local field (E012) |
| Diagnostic basis | Voltage, current and transferred charge on an oscilloscope (E001) |
