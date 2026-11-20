# IEAGHG (2017): fired SMR merchant hydrogen plant, Base Case

## Source and review

- Source ID: **SRC004**. IEAGHG, *Techno-Economic Evaluation of SMR Based Standalone (Merchant) Hydrogen Plant with CCS*, Technical Report 2017-02, February 2017. Prepared by Amec Foster Wheeler and IEAGHG; principal researchers G. Collodi, G. Azzaro and N. Ferrari; IEAGHG manager S. Santos.
- Role: **fired SMR reference system**, second of the two benchmark systems (with SRC003). Data type: engineering design study with heat and material balance (E001). Only the **Base Case (SMR without CCS)** is extracted.
- Document: [IEAGHG_2017-02.pdf](../IEAGHG_2017-02.pdf), 286 PDF pages, downloaded 2026-10-30 from https://ieaghg.org/docs/General_Docs/Reports/2017-02.pdf (the publication page was blocked by Cloudflare). SHA-256 `33a3dd61486a7fe748a06be7a61903470f356332e0e8a7be7fde66979b555e44`. Text copying is restricted in the PDF; text was extracted for reading only.
- Page numbering: the main report uses "Sheet N of 112", with sheet N = PDF page N + 22. The Reference Document (Annex I) uses "Sheet N of 24", with sheet N = PDF page N + 246. Heat and material balance and equipment list pages are unnumbered; PDF pages are used.
- Protocol version: 0.1.
- Extractor / date: Claude (AI), 2026-10-30.
- Coverage: IEAGHG overview (PDF pp. 3-21), Base Case sections 2.1-2.9 (PDF pp. 31-58), Reference Document sections 3.1-3.4 (PDF pp. 254-256), economic basis (PDF p. 236). Equipment list pages 53-54 inspected as images. Capture cases 1A-3 not extracted.
- Reviewer / checks: same extractor. Component heating values reproduce the report's natural gas HHV and LHV; the H2 Nm3 flow reproduces the stream 12 molar flow at 0 degC; reformer outlet CH4 (3.36% dry) matches the stated 3.3-4% range (C001, C003).
- Review status: **ai_checked; human verification pending**.

## Electricity supply

Not an electrically heated system. The reformer is fired with PSA tail gas and supplementary natural gas. Surplus HP steam drives a condensing steam turbine (cogen plant, 11.5 MWe gross) that covers the plant's 1.58 MWe consumption (H2 plant 1.216, cogen + utilities + BoP 0.366) and **exports 9.918 MWe** to the grid (E018-E019). There is no grid import, so f_electric = 0. The H2 product leaves the PSA at 2.5 MPa with no H2 compressor (E016).

## Reactor configuration

- Hydrogen plant: feed preheat, sulphur absorber, adiabatic pre-reformer, **Foster Wheeler Terrace Wall** steam reformer, reformer waste heat boiler, high-temperature shift, syngas cooling, PSA (E004-E005).
- Terrace Wall furnace: single row of catalyst tubes per firebox, two rows of burners on two levels firing upward along terraced walls; convective section on top with reformer feed preheat, pre-reformer feed preheat, steam superheater, feed preheat and steam generation coils (E005).
- Reformer and pre-reformer catalysts contain nickel (Annex I, PDF p. 259; E051). Tube count, tube dimensions, catalyst volume and furnace dimensions are not given; most duty and size cells in the equipment list are blank (E027).

## Operating conditions

Single design point, SRC004-OP001:

| Quantity | Value | Evidence |
|---|---|---|
| Natural gas | 89.0% CH4, 7.0% C2H6, 1.0% C3H8, 0.1% C4H10, 2.0% CO2, 0.89% N2; HHV 51.473, LHV 46.502 MJ/kg | E006-E007 |
| Total NG | 30,563 kg/h (1,696.6 kmol/h), of which 4,332 kg/h supplementary fuel | E008-E009 |
| Pre-reformer feed (stream 4) | 5,514 kmol/h; 23.5% CH4, 73.1% H2O; 500 degC; 3.39 MPa | E011 |
| Reformer outlet gas (stream 5, after waste heat boiler) | 8,370 kmol/h; 2.4% CH4, 51.7% H2, 11.6% CO; 2.80 MPa | E012 |
| Steam-to-carbon | around 2.7-2.8 | E017 |
| Reformer tube outlet | "normally around 900-950 degC" (general statement; no single Base Case value) | E017 |
| Burner fuel | PSA tail gas 2,106 kmol/h plus supplementary NG 240 kmol/h | E009-E010 |
| H2 product | 100,000 Nm3/h = 8,994 kg/h; 99.99+%; 2.5 MPa; 40 degC | E003, E014 |
| Availability | 95% (economic assumption) | E030 |

## Performance indicators

- **Conversion (pre-reformer + reformer, stream 4 to 5):** CH4 84.6%; hydrocarbon carbon 87.1% (C003; E043). The reformer inlet after the pre-reformer is not tabulated, so the reformer alone cannot be isolated. The reformer outlet is not tabulated either; stream 5 has the same composition after the waste heat boiler.
- **Product:** 8,994 kg/h H2 (E014).
- **Author metrics:** total energy input 394.77 MW LHV; energy in product 299.70 MW LHV; 14.212 MJ NG (LHV) per Nm3 H2 (E015, E020). The report does not state an efficiency; the LHV ratios are 75.9% for H2 only and 78.4% with export power (C006; E049).
- **Heat-basis reference metrics (ours, OP001):**
  - Q_abs = stated **radiant duty 82.63 Mkcal/h = 96.1 MW** (E013; C002).
  - Q_fired = **157.9 MW LHV / 174.9 MW HHV**, of which tail gas 102.0 MW LHV (C004).
  - **EC_CH4,abs = 315 kJ/mol** CH4 converted (256 kJ/mol hydrocarbon carbon); **EC_CH4,fired = 574 kJ/mol HHV (518 LHV)** (C005).
  - **Radiant efficiency 0.61 (LHV)**, 0.55 (HHV) (C005).
- **Whole-system eta_HHV (ours):** **81.1%** for H2 only; 83.4% including the 9.9 MWe export; f_electric = 0 (C006).
- **Specific inputs:** 174.9 MJ NG (HHV) per kg H2 (158.0 MJ LHV); 1.10 kWh electricity exported per kg H2 (C006).
- **Emissions and cost (context):** 0.809 kg CO2/Nm3 H2 (about 9.0 kg CO2/kg H2); LCOH 11.4 euro cent/Nm3; TPC 171 million EUR; 4Q2014 EUR (E021, E024-E026).
- Power-basis metrics: not applicable.

## Reported system information

- **Boundary:** whole merchant plant: H2 plant, cogen steam turbine, demineralised water plant and utilities/BoP (E004). Product at PSA outlet, 2.5 MPa, no compression.
- **Mass balance:** heat and material balance, 15 streams, without enthalpies (E008-E014).
- **Energy balance:** no overall energy balance is tabulated; stack loss and cooling duties are not reported (E028). Power balance is reported (E018).
- **Hardware:** equipment list gives the reformer radiant duty, reactor vessel sizes (pre-reformer 2.1 m ID x 3.05 m; shift converter 3.4 m x 4.4 m; sulphur absorbers 2.45 m x 3.65 m), PSA flow, recycle compressor and a 12 MWe condensing steam turbine. Reformer furnace dimensions not given.
- **Costs:** TPC, TCR, O&M, LCOH (E024-E026).

## Reporting quality

Fired SMR reference source, so R1-R4 replace Q1-Q9.

| Item | Answer | Reason and evidence IDs |
|---|---|---|
| R1 Data type | design basis | Engineering design study with heat and material balance; no measured plant data (E001). |
| R2 Boundary | yes (plant); partly (reformer) | Plant units and power balance clearly stated; reformer radiant duty stated, but reformer inlet/outlet streams and overall energy balance not tabulated (E013, E027-E028). |
| R3 Basis | yes | NG and H2 HHV and LHV stated; performance on LHV basis; site reference conditions stated (E007, E015-E016, E029). |
| R4 Independence | partly | Prepared by Amec Foster Wheeler, the licensor of the Terrace Wall reformer used in the design; IEAGHG-managed and independently reviewed (E002). |

- Confidence in conversion/product results: **higher** for a design balance (consistent stream table; outlet CH4 matches stated range). Not measured performance.
- Confidence in energy results: **higher** for the stated radiant duty and plant inputs; **moderate** for our fired duty and EC values, which depend on the stream table and our heating values.

## Missing information and comparison limits

| Status | Gap or issue | Consequence |
|---|---|---|
| not_reported | Reformer inlet stream after the pre-reformer and reformer outlet temperature for the Base Case | Conversion is for pre-reformer + reformer combined; EC_CH4 uses CH4 converted across both |
| not_reported | Tube count, dimensions, furnace size (E027) | No reactor volume or power density comparison |
| not_reported | Overall energy balance, stack loss, cooling duties (E028) | Cannot check first-law closure |
| unclear | Calorie definition for Mkcal/h | International table calorie assumed (4.1868 kJ/kcal) |
| not_applicable | Measured operation, durability | Design basis; availability 95% assumed (E030) |

Comparison with SRC003 (NETL): Q_abs here is the stated radiant duty only; NETL's derived Q_abs (stream 7 to 8) may include convective preheat. IEAGHG converts surplus steam to exported electricity, whereas NETL exports steam uncredited and compresses H2 to 6.48 MPa with grid electricity. Whole-plant eta_HHV is therefore higher here (81.1% vs 75.7%). Compare the two on EC_CH4,abs, EC_CH4,fired and radiant efficiency with these boundary differences stated.

## Calculations

All calculations below are reproduced by [calculations.py](calculations.py) (`python3 calculations.py`).

### SRC004-C001: heating values and checks

Standard 25 degC heats of combustion, as for SRC003-C001, plus n-pentane 3509.0 / 3244.9 kJ/mol (HHV / LHV). The NG composition (E006; molar mass 30,563 / 1,696.6 = 18.01 kg/kmol) gives 51.476 MJ/kg HHV and 46.489 MJ/kg LHV, against the report's 51.473 and 46.502 (E007) (E041). 100,000 Nm3/h / 22.414 = 4,461.5 kmol/h, matching stream 12, so Nm3 is at 0 degC and 101.325 kPa.

### SRC004-C002: radiant duty

`Q_abs = 82.63e6 kcal/h x 4.1868 kJ/kcal / 3.6e6 = 96.1 MW` (E013, E042).

### SRC004-C003: conversion

Inputs E011-E012.

- CH4: 0.2350 x 5,514.0 = 1,295.8 kmol/h in; 0.0238 x 8,370.3 = 199.2 kmol/h out; **84.6%**.
- Hydrocarbon carbon in: 1,295.8 + 2(102.0) + 3(14.3) + 4(1.7) = 1,549.4 kmol C/h; **87.1%** converted.
- Outlet CH4 dry basis: 0.0238 / (1 - 0.2927) = 3.36%, within the stated 3.3-4% (E017) (E043).

### SRC004-C004: burner fuel duty

Inputs E009-E010, C001. Tail gas: 2,106.3 kmol/h x (0.0945 CH4, 0.1454 CO, 0.2369 H2) = 102.0 MW LHV / 112.9 MW HHV. Supplementary NG: 4,332 kg/h x 46.502 / 51.473 MJ/kg = 56.0 / 61.9 MW. **Q_fired = 157.9 MW LHV, 174.9 MW HHV** (E044).

### SRC004-C005: heat-basis EC_CH4 and radiant efficiency

Inputs C002-C004. CH4 converted 1,096.6 kmol/h = 304.6 mol/s; hydrocarbon carbon converted 1,350.2 kmol/h = 375.1 mol/s.

- `EC_CH4,abs = 96.1 MW / 304.6 mol/s = 315 kJ/mol` (256 kJ/mol per hydrocarbon carbon) (E045).
- `EC_CH4,fired = 174.9 / 304.6 = 574 kJ/mol HHV; 157.9 / 304.6 = 518 kJ/mol LHV` (E046).
- `Radiant efficiency = 96.1 / 157.9 = 0.609 LHV; 96.1 / 174.9 = 0.550 HHV` (E047).

The per-CH4 values overstate the cost slightly because C2+ conversion also uses reformer heat; the per-hydrocarbon-carbon value is the closer analogue of a methane-only feed.

### SRC004-C006: whole-system efficiencies

Inputs E007-E008, E014-E016, E018.

- NG input: 30,563 kg/h x 51.473 MJ/kg = 437.0 MW HHV. H2: 8,994 kg/h x 141.88 MJ/kg = 354.5 MW HHV.
- `eta_HHV = 354.5 / 437.0 = 81.1%` (H2 only); `(354.5 + 9.918) / 437.0 = 83.4%` with export power; `f_electric = 0` (no import) (E048).
- LHV: 299.70 / 394.77 = 75.9% (H2 only); 78.4% with export power (E049).
- Specific inputs: 437.0 x 3,600 / 8,994 = 174.9 MJ HHV/kg H2; 158.0 MJ LHV/kg H2; 9,918 / 8,994 = 1.10 kWh exported/kg H2 (E050).

## Revisions

- 2026-10-30: initial extraction of the Base Case by Claude (AI). Evidence IDs E031-E040 unused; numbering gap is intentional.
- 2026-11-20, after GPT cross-check (cross_check_log.md XR003): nickel catalyst added (E051); summary table catalyst cell changed from NR to Ni.
