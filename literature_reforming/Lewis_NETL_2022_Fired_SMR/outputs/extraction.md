# NETL (2022): fired SMR reference plant (Case 1)

## Source and review

- Source ID: **SRC003**. E. Lewis, S. McNaul, M. Jamieson, M. S. Henriksen, H. S. Matthews, J. White, L. Walsh, J. Grove, T. Shultz, T. J. Skone and R. Stevens, *Comparison of Commercial, State-of-the-Art, Fossil-Based Hydrogen Production Technologies*, DOE/NETL-2022/3241, National Energy Technology Laboratory, 12 April 2022. OSTI 1862910.
- Role: **fired SMR reference system** (benchmark category; not an experimental demonstration). Data type: Aspen Plus process model, design basis (E001). Peer reviewed by independent experts (E002).
- Document: [ComparisonofCommercialStateofArtFossilBasedHydrogenProductionTechnologies_041222.pdf](../ComparisonofCommercialStateofArtFossilBasedHydrogenProductionTechnologies_041222.pdf), 327 PDF pages. Printed page = PDF page - 18 in the main body. SHA-256 `891c33af7beee1f11f562ebf075f345b7511905f2d95bea6dd957af02f912e0a`. PDF metadata shows a modification date of 2026-10-30; retrieval date unknown.
- Protocol version: 0.1.
- Extractor / date: Claude (AI), 2026-10-30.
- Coverage: front matter, contents, Sections 2.3 and 2.6, and Section 3.1-3.7 (Case 1 SMR without CO2 capture), PDF pp. 44, 47, 69-95. Exhibit 3-12 diagram inspected as an image. Case 2 (SMR with capture), Case 3 (ATR) and the gasification cases were not extracted.
- Reviewer / checks: same extractor. Text extracted with pdftotext and checked against internal consistency: NETL's NG heating values, H2 HHV output, auxiliary-load sum, carbon balance and author efficiencies are all reproduced (C001, C006).
- Review status: **ai_checked; partial human check by BB, 2026-11-26: Exhibit 3-4 streams 7, 8 and 15 and Exhibit 3-5 values (E004, E008-E010, E014-E016, E025, E027) confirmed, so reformer conversion 77.7% stands; absorbed duty (E042, Aspen enthalpies) not checked; no changes (human_checks/summary.csv). Other records human verification pending.**

## Electricity supply

Not an electrically heated system. The reformer is fired with natural gas and PSA off-gas (E021). Electricity is imported from the grid for auxiliaries only: **12.65 MWe total**, of which the H2 compressor is 10.01 MWe (about 79%) and the air blower 1.41 MWe (E025-E026). There is no on-site power generation; net power is -13 MWe.

## Reactor configuration

- Single train: ZnO sulfur guard, adiabatic prereformer, **side-fired tubular primary reformer** (Ni catalyst in high-alloy steel tubes), 2 x 3 high-temperature water-gas shift reactors, PSA and H2 compressor (E018, E024; Exhibit 3-3).
- Primary reformer design condition: 265,000 kg/h at 2.8 MPa and 871 degC, one unit (E036). Tube count, tube dimensions, firebox volume and footprint not reported (E037).
- Flue gas passes a convective heat-recovery section that preheats feed, raises superheated steam (about 53% used for reforming, the rest exported) and preheats boiler feedwater (E022).
- The prereformer outlet (stream 7, 395 degC) goes directly to the primary reformer in Exhibit 3-12; no separate mixed-feed preheat coil is shown (E039).

## Operating conditions

Single design point, SRC003-OP001:

| Quantity | Value | Evidence |
|---|---|---|
| Natural gas | 93.1% CH4, 3.2% C2H6, 0.7% C3H8, 0.4% n-C4H10, 1.0% CO2, 1.6% N2; HHV 52,295 kJ/kg | E006-E007 |
| Total NG | 70,979 kg/h (4,096 kmol/h): 3,687 kmol/h process, 410 kmol/h supplemental fuel | E008, E011-E012 |
| Reformer inlet (stream 7) | 13,930 kmol/h; 25.8% CH4, 67.6% H2O; 395 degC; 2.90 MPa | E015 |
| Reformer outlet (stream 8) | 19,519 kmol/h; 4.1% CH4, 46.1% H2, 14.3% CO; 871 degC; 2.83 MPa | E016 |
| Steam-to-carbon | 2.56 (author) | E017 |
| Burner fuel (stream 15) | 6,104 kmol/h: PSA off-gas (5,695 kmol/h) plus supplemental NG | E013-E014 |
| H2 product | 20,126 kg/h, 99.90 vol%, 6.48 MPa | E004-E005 |
| Capacity factor | 90% (design assumption) | E035 |

## Performance indicators

- **Methane conversion:** primary reformer 77.7% (stream 7 to 8; author ">77%"). Plant level, from CH4 in the process natural gas to CH4 slip after shift, 76.6% (C003; E043, E050).
- **Product:** 20,126 kg/h H2 at 99.90 vol% after PSA recovery of 85% (E004, E023).
- **Author metrics:** HHV effective thermal efficiency 75.4% and cold gas efficiency 76.7%; LHV 70.5% and 71.9% (E027). ETE = (H2 heating value + net power) / NG heating value, with net power negative; CGE = H2 heating value / NG heating value (E028). Export steam receives no credit in either metric or in cost (E032).
- **Heat-basis reference metrics (ours, reformer level, OP001):**
  - Q_abs (process-gas heat uptake, stream 7 to 8) = **264.3 MW** (C002).
  - Q_fired (burner fuel) = **447.7 MW HHV / 396.5 MW LHV**, of which recycled PSA off-gas is 344.3 MW HHV and supplemental NG 103.2 MW HHV (C004).
  - **EC_CH4,abs = 340 kJ/mol** CH4 converted; **EC_CH4,fired = 577 kJ/mol HHV (510 kJ/mol LHV)** (C005).
  - Q_abs / Q_fired = 0.67 on an LHV basis (0.59 HHV) (C005).
- **Whole-system eta_HHV (ours):** **75.7%**, f_electric 1.2% (C006). Export steam (514 GJ/h, about 143 MW sensible + latent, 0 degC reference) is a heat export, kept separate and not credited.
- **Specific inputs:** 184.4 MJ NG (HHV) and 0.63 kWh electricity per kg H2 (C006).
- **Emissions and cost (context):** 9.3 kg CO2/kg H2 at the stack; 12 kg CO2e/kg H2 life cycle; LCOH $1.06/kg H2 (Dec 2018 USD), 73% fuel; TOC $713/(kg H2/day) (E031, E033-E034).
- Power-basis metrics (SEI, EC_CH4 on electrical power): not applicable.

## Reported system information

- **Boundary:** whole plant from natural gas at 3.1 MPa to H2 at 6.48 MPa, including sulfur guard, prereformer, reformer, shift, PSA, compression, cooling tower and water treatment (Sections 3.1-3.3). CO2 transport and storage not applicable to Case 1.
- **Mass balance:** full stream table (Exhibit 3-4); carbon balance closes at 51,337 kg C/h (E030).
- **Energy balance:** Exhibit 3-11 (0 degC reference). In: NG 3,712 GJ/h HHV, auxiliary power 46 GJ/h. Out: H2 2,846 GJ/h HHV, export steam 514, stack 287, cooling tower 138; unaccounted 1.3 GJ/h (E029).
- **Hardware:** major equipment list (Exhibits in Section 3.6); single-train design; DCS designed for 99.5% availability. Catalyst initial fills and replacement rates are listed in Exhibit 3-15.
- **Utilities:** raw water consumption 5.3 m3/min (E040).
- **Costs:** Section 3.7; Dec 2018 USD; NG $4.42/MMBtu HHV.

## Reporting quality

Fired SMR reference source, so R1-R4 replace Q1-Q9.

| Item | Answer | Reason and evidence IDs |
|---|---|---|
| R1 Data type | design basis (simulation) | Aspen Plus model of a commercial-technology design; no measured plant data (E001). |
| R2 Boundary | yes (plant); partly (reformer) | Whole-plant boundary and equipment fully stated; reformer-only duties not stated and derived here (E038, C002-C004). |
| R3 Basis | yes | HHV and LHV both reported, NG composition and heating values given, scale and conditions stated (E006-E010, E027). |
| R4 Independence | yes | US government laboratory, independently peer reviewed (E002); not a technology vendor. Some cost inputs come from vendor quotes. |

- Confidence in conversion/product results: **higher** for an internally consistent design model (stream table, carbon balance and energy balance close). It is not measured performance.
- Confidence in energy results: **higher** for plant-level values; **moderate** for our reformer-level Q_abs and Q_fired, which are derived from the stream table rather than stated by the authors.

## Missing information and comparison limits

| Status | Gap or issue | Consequence |
|---|---|---|
| not_reported | Reformer fired duty, absorbed duty and radiant efficiency (E038) | Derived from the stream table (C002-C004); treat as reviewer values |
| not_reported | Tube count, dimensions, catalyst volume per tube, firebox volume, footprint (E037) | No reactor volume or power density comparison with Wismann OP013 or plasma reactors |
| not_applicable | Measured operation, time on stream, degradation | Design basis; 90% capacity factor is an assumption (E035) |
| unclear | Q_abs uses stream 7 to 8; any convective preheat of stream 7 inside the reformer block is included in it | Q_abs/Q_fired of 0.67 (LHV) is the process-gas share of burner fuel, not a stated radiant efficiency |
| not_reported | Reformer-only electrical use | Plant electricity is dominated by H2 compression (E026), which lab reactors do not include |

Comparison limits: this is a plant-level design at 222 kNm3/h H2 with shift, PSA and 6.48 MPa compression. Lab plasma and Joule-heated reactors report reformer-outlet syngas at around ambient pressure. Compare at reformer level where possible (EC_CH4,abs and EC_CH4,fired against EC_CH4), and keep plant-level eta_HHV separate. Heat-basis (fuel) and power-basis (electricity) metrics are not converted to primary energy.

## Calculations

All calculations below are reproduced by [calculations.py](calculations.py) (`python3 calculations.py`).

### SRC003-C001: heating values

Standard 25 degC heats of combustion (kJ/mol), HHV / LHV: H2 285.83 / 241.83; CH4 890.6 / 802.3; C2H6 1560.7 / 1428.6; C3H8 2219.2 / 2043.1; n-C4H10 2877.5 / 2657.3; CO 282.98 / 282.98. Values as tabulated in standard references (e.g. NIST Chemistry WebBook); cite a specific source in the report.

Check: NETL natural gas (E006, MW 17.328) gives 906.1 kJ/mol = 52.29 MJ/kg HHV and 47.18 MJ/kg LHV, against NETL's 52.295 and 47.201 (E007), within 0.04% (E041). Total NG 4,096 kmol/h gives 1,031.0 MW HHV, against NETL's 1,031.07 MW (E009).

### SRC003-C002: reformer process-gas heat uptake, Q_abs

Inputs E015-E016. Aspen Plus enthalpies use the elements at 25 degC as reference, so the difference includes reaction heat and sensible heat. Mass flow is unchanged (240,966 kg/h).

`Q_abs = 240,966 kg/h x (-6,233.86 - (-10,182.33)) kJ/kg = 951.4 GJ/h = 264.3 MW` (E042).

### SRC003-C003: methane conversion

Inputs E015-E016, E011, and stream 10 (Exhibit 3-4 continued, PDF p. 79, printed p. 61: 15,654 kmol/h, 0.0513 CH4).

- Reformer: CH4 in = 0.2583 x 13,930 = 3,598.1 kmol/h; out = 0.0411 x 19,519 = 802.2 kmol/h; converted 2,795.9 kmol/h (776.6 mol/s); **X = 77.7%** (E043).
- Plant: CH4 in process NG = 0.931 x 3,687 = 3,432.6 kmol/h; CH4 after shift = 803.1 kmol/h; **X = 76.6%** (E050). The prereformer converts C2+ and forms some CH4, so the reformer inlet has more CH4 than the process NG.

### SRC003-C004: burner fuel duty, Q_fired

Inputs E012-E014, C001.

- Stream 15 (6,104 kmol/h): 264.1 kJ/mol HHV, 233.8 kJ/mol LHV; **Q_fired = 447.7 MW HHV, 396.5 MW LHV** (E044).
- Of which PSA off-gas (stream 13): 344.3 MW HHV / 303.1 MW LHV; supplemental NG (stream 14): 103.2 MW HHV / 93.1 MW LHV.

### SRC003-C005: heat-basis EC_CH4 and duty ratio

Inputs C002-C004.

- `EC_CH4,abs = 264.3 MW / 776.6 mol/s = 340 kJ/mol` (E045). It exceeds the 205.8 kJ/mol reaction enthalpy (E020) mainly because of sensible heating of the steam-rich feed from 395 to 871 degC.
- `EC_CH4,fired = 447.7 / 776.6 = 577 kJ/mol HHV; 396.5 / 776.6 = 510 kJ/mol LHV` (E046). Most burner fuel is recycled PSA off-gas from the process feed; on supplemental NG alone the value would be 133 kJ/mol HHV, which understates the fuel consumed and is not used.
- `Q_abs / Q_fired = 264.3 / 396.5 = 0.667 LHV; 264.3 / 447.7 = 0.590 HHV` (E047).

### SRC003-C006: whole-system eta_HHV

Inputs E004, E009, E025, C001. H2 product 0.9998 x 9,959 kmol/h = 9,957 kmol/h; 9,957 x 285.83 / 3,600 = 790.6 MW HHV (matches 2,846 GJ/h in E029).

- `D = P_el + NG HHV = 12.65 + 1,031.07 = 1,043.7 MW`
- `eta_HHV = 790.6 / 1,043.7 = 75.7%`; `f_electric = 12.65 / 1,043.7 = 1.2%` (E048)
- Check: author CGE = 790.6 / 1,031.07 = 76.7% and ETE = (790.6 - 12.65) / 1,031.07 = 75.4%, matching E027.
- Specific inputs: 1,031.07 MW x 3,600 / 20,126 kg/h = 184.4 MJ NG HHV/kg H2; 12,650 kW / 20,126 kg/h = 0.63 kWh/kg H2 (E049).

Export steam (about 143 MW, 0 degC reference) is a heat export and is excluded from the numerator; no Q_dot_external,in.

## Revisions

- 2026-10-30: initial extraction of Case 1 by Claude (AI). Folder renamed from NETL_2022_fossil_based_H2 to Lewis_NETL_2022_Fired_SMR, following the workflow naming convention.
