# Wismann et al. (2019): traceable extraction

## Registration and coverage

- Source ID: **SRC001**.
- Citation: Sebastian T. Wismann et al., "Electrified methane reforming: A compact approach to greener industrial hydrogen production," Science 364(6442), 756-759 (24 May 2019).
- DOI: https://doi.org/10.1126/science.aaw8775. Citation verified from supplied PDFs; no external literature was added to this extraction.
- Inputs: [manuscript.pdf](../manuscript.pdf), 5 PDF pages (4 article pages plus publisher information); [supplementary.pdf](../supplementary.pdf), 25 PDF pages. Supplement pp. 23-25 contain references with printed page numbers restarting at 1. Use PDF page numbers for unambiguous lookup.
- Document versions and SHA-256 hashes: manuscript.pdf (5 pp., Supplied local published article PDF), SHA-256 `3ab1991aa15a589446b52f2e1c5139666764876d8681212ba0dd2c40c34f3865`; supplementary.pdf (25 pp., Supplied local supplementary PDF; contains references pages labelled Submitted Manuscript: Confidential), SHA-256 `dab5db62e1c0e423633eeb2b90ed9fdf83405ef1820cfbef5ed65bfc182cb04e`. Retrieval date unknown.
- Protocol: [../workflow.md](../../workflow.md), version 0.1.
- Extraction/review date: 2026-10-28. Extractor: Codex AI. Review status: **ai_checked by the same extractor; human check: none**.
- Coverage: all supplied text read; labelled conversions in Figs. S2-S4 extracted; selected relevant figures visually inspected. Full curve digitization, full CFD reproduction, and extraction of every auxiliary plot coordinate were not performed. Plot temperatures are approximate visual readings, not author-tabulated data.
- Outputs: [evidence.csv](evidence.csv); the operating points and calculations are in this file (sections Operating points and Calculations), merged here on 2026-11-26 from the former operating_points.csv and calculations.md to match the standard source layout. Individual claims below link by evidence ID to the CSV, where the original document/page/locator is recorded.

**Pilot outcome:** the paper provides a useful reactor/conversion/design benchmark. It does not provide the point-matched electrical input and complete stream/duty data needed to calculate our HHV efficiency or electricity fraction. It must therefore remain incomplete for those comparisons.

## Electricity supply

| Field | Extracted information | Evidence |
|---|---|---|
| Mechanism | AC direct resistance heating of the FeCrAl tube through end copper sockets | SRC001-E001, E003 |
| Upstream voltage | 220 V before transformation; amplitude convention unspecified | SRC001-E002 |
| Reactor voltage | RMS potential is mentioned as a measured CFD boundary, but no numerical operating value is given | SRC001-E006, E010 |
| Frequency | Not reported; do not assume 50 Hz | SRC001-E012 |
| Waveform | AC; detailed waveform shape not reported | SRC001-E001, E013 |
| Mean real power | Not reported numerically at the operating points | SRC001-E014 |
| Current | Current probe specified; operating current values not reported | SRC001-E005, E011 |
| Instrumentation | Agilent DSO-X 2014A oscilloscope; Keysight 1146B current probe | SRC001-E004-E005 |
| Adjustment | Potential across sockets increased through variotransformer/coils | SRC001-E007 |
| Wall consumption and supply efficiency | Not reported | SRC001-E015, E019 |

The **1 A** in the methods is a contact-resistance test before heating, not an operating current (SRC001-E008). Local inward heat flux in Fig. S5 is calculated from gas enthalpy change and is not a substitute for total electrical supply power (SRC001-E090). Supply ratings, power factor, electrical sampling/uncertainty, and pulse characteristics have explicit missing-information records (SRC001-E016-E020).

## Reactor configuration

The demonstrated apparatus is one 50 cm FeCrAlloy tube, 6 mm OD, carrying a porous nickel-impregnated zirconia washcoat on its inner surface. The nominal main coated length is 28 cm and the figure specifies a 128 micrometre radial coating. The tube is surrounded by FreeFlow insulation in an 11 cm OD casing. External spot-welded thermocouples measure wall temperatures, not gas temperatures (SRC001-E021-E031; supplementary p. 2 and manuscript Fig. 2).

**Selected inner diameter: 5.3 mm**, following the user's instruction on 2026-10-28. The preparation section prints 5.2 mm (SRC001-E023); the transport discussion prints 5.3 mm (SRC001-E025), and Fig. 2's 6 mm OD/0.35 mm wall geometry supports 5.3 mm (SRC001-E022, E024). Both source statements are preserved, but all current geometry calculations use 5.3 mm. This is a recorded modelling choice, not a correction to the original PDF.

With that choice, the nominal gas-channel volume within the main coated zone is **5.595 mL** (SRC001-C001; SRC001-E162). It excludes coating pore volume and residual catalytically active coating beyond the nominal main zone. It is neither total equipment volume nor complete active volume. Catalyst mass, nickel loading, active area and numerical coating porosity were not located (SRC001-E033-E036).

The industrial reactor is a **CFD/design extrapolation**, not the laboratory tube scaled and demonstrated at industrial output. It assumes ideal insulation, optimized connections without copper sockets/contact resistance, full internal coating, and pressure-independent conductivity/viscosity (SRC001-E107).

## Operating conditions

Laboratory feed is CH4/H2O/H2 = **30/60/10 on a molar basis**, preheated to **100 degC**, with operation **50 mbar above ambient** (SRC001-E038-E040). Derived S/C is **2** (SRC001-C004), distinct from the industrial S/C of 1.8. The 10% inlet hydrogen matters for both gross/net hydrogen production and feed HHV accounting.

Gas chromatography used TCD/FID at 15-minute intervals. The procedure states at least four consecutive GC measurements per condition; the model-fit discussion describes at least three steady measurements corresponding to at least 45 minutes of averaging. These are retained as separate statements rather than converted into an unsupported total run duration (SRC001-E041-E042).

The following twelve labelled conversion conditions were extracted from supplementary Figs. S2-S4. Temperatures are approximate visual estimates of the hot external wall near z = 42-43 cm, before terminal cooling; estimated reading uncertainty is +/-20 degC. They are not precision digitization or cooled outlet-gas temperatures.

| Operating point | Total wet feed (Nml/min) | CH4 conversion (%) | Approximate hot-exit wall temperature (degC) | Source |
|---|---:|---:|---:|---|
| SRC001-OP001 | 340 | 58.0 | 600 | Supplement p. 11, Fig. S2 |
| SRC001-OP002 | 340 | 75.3 | 650 | Supplement p. 11, Fig. S2 |
| SRC001-OP003 | 340 | 86.5 | 700 | Supplement p. 11, Fig. S2 |
| SRC001-OP004 | 340 | 92.7 | 750 | Supplement p. 11, Fig. S2 |
| SRC001-OP005 | 1020 | 50.9 | 620 | Supplement p. 12, Fig. S3 |
| SRC001-OP006 | 1020 | 62.9 | 650 | Supplement p. 12, Fig. S3 |
| SRC001-OP007 | 1020 | 75.6 | 700 | Supplement p. 12, Fig. S3 |
| SRC001-OP008 | 1020 | 82.2 | 720 | Supplement p. 12, Fig. S3 |
| SRC001-OP009 | 1020 | 91.6 | 790 | Supplement p. 12, Fig. S3 |
| SRC001-OP010 | 1700 | 61.1 | 680 | Supplement p. 13, Fig. S4 |
| SRC001-OP011 | 1700 | 72.4 | 720 | Supplement p. 13, Fig. S4 |
| SRC001-OP012 | 1700 | 85.0 | 780 | Supplement p. 13, Fig. S4 |

Every point has separate flow, conversion and temperature evidence records (SRC001-E050-E085). Normal-flow reference temperature and pressure are not explicitly defined (SRC001-E045); absolute molar flows have not been silently inferred. Fig. S7's additional 680 Nml/min initial/final activity comparison is recorded as a series-level observation, not merged with these twelve points (SRC001-E086).

## Performance indicators

### Space time

Authors' defined residence time, space time, GHSV and WHSV were not located (SRC001-E119-E120). We calculate the nominal main-coated-zone channel volume divided by total normal inlet flow, using the selected 5.3 mm ID:

| Total wet feed (Nml/min) | Nominal reference-flow space time (s) |
|---|---:|
| 340 | 0.9873 |
| 1020 | 0.3291 |
| 1700 | 0.1975 |

These are reviewer-derived values (SRC001-C002), **not actual hot-gas residence times**. The calculation does not resolve axial heating, reaction-induced expansion, pore gas, or the active residual outlet layer. Values must retain this volume/flow basis in future comparisons.

### Conversion and products

Conversion labels span 50.9-92.7% across the extracted conditions; compare using the point table, not a single pooled maximum. Numerical measured product compositions, H2/CO ratios, selectivities, hydrogen production rates, carbon balances and quantitative conversion uncertainties were not located for these points (SRC001-E121-E126, E131). Do not substitute ideal stoichiometry for measured product composition: water-gas shift and inlet H2 matter.

### Energy efficiency and electricity fraction

The protocol's HHV efficiency and electricity fraction are **not calculable from the reported data** (SRC001-E128-E129; SRC001-C003). Missing inputs include electrical power, steam/preheat duty and complete outlet flows. Fully electric reactor heating does not mean an electricity fraction of 100%, because our denominator includes combustible feed HHV.

The paper's 20% laboratory and 23% industrial-model catalyst utilization values are effectiveness factors, **not energy efficiencies** (SRC001-E087, E116). Its methane LHV value in supplementary p. 7 supports a theoretical CO2-emission calculation, not the HHV efficiency requested here (SRC001-E130).

### Scale and compactness

| Case | Status | Conversion (%) | Volume (m3) | Evidence |
|---|---|---:|---:|---|
| SRC001-OP013: side-fired reference | Industrial flowsheet/design reference | 75.4 | 1140 in figure; 1100 in rounded text | SRC001-E092-E097, E104-E105 |
| SRC001-OP014: resistance-heated | Industrial model/design projection | 75.4 | 4.9 | SRC001-E098-E108 |
| SRC001-OP015: higher conversion | Industrial model/design projection | 95 | 15 | SRC001-E109-E111 |
| SRC001-OP016: supplementary case | Industrial CFD case for effectiveness/carbon analysis | 75.6 | Not specified for this case | SRC001-E112-E117 |

Fig. 4 compares at a production scale of **2230 kmol H2/h**. The reference conditions are Tin = 466 degC, Tout = 920 degC, S/C = 1.8, Pout = 26.7 barg; the electrical scale-up is constrained by a 20 degC approach to equilibrium (supplement p. 8; manuscript p. 3, Fig. 4). Do not assume every reference temperature applies unchanged to the 95% projected-conversion point.

The volume comparison excludes blowers and waste-heat equipment for the conventional furnace, and wiring/power supply for the electric reformer. It is not a full-plant footprint comparison. The printed 1140/4.9 ratio is about 230 (SRC001-C005); the abstract's potential 100-fold compactness statement is not a measured industrial result.

### Stability, carbon and response

The authors report no discernible activity loss between initial and final measurements, but total time on stream is unspecified (SRC001-E086, E047). Carbon activity is a thermodynamic/model assessment rather than a quantified measured carbon deposition rate (SRC001-E089, E117). Millisecond thermal response is a characteristic conduction timescale; possible second-scale startup is a proposal, not a measured startup trial (SRC001-E048, E091).

## Power-basis energy metrics

SEI, EC_CH4, EC_H2, EY_H2 and eta_P,LHV are **not calculable**: no point-matched electrical power is reported (SRC001-E014, E127), and product flows are not tabulated (SRC001-E122, E124). Compare this benchmark with plasma sources on conversion and conditions only.

## Reporting quality

Appraised 2026-10-30 by Claude (AI) from the existing extraction records and evidence IDs, without re-reading the PDFs. Status: unreviewed; human check: none.

| Item | Answer | Reason and evidence IDs |
|---|---|---|
| Q1 Power measurement | no | Oscilloscope and current probe specified (SRC001-E004-E005), but no operating power reported (E014). |
| Q2 Feed definition | partly | Molar composition and total flows stated (E038, E050-E085); normal reference T/P not defined (E045). |
| Q3 Product analysis | partly | GC with TCD/FID, at least four measurements per condition (E041); conversion equation and handling of volume change not stated (E121). |
| Q4 Balance closure | no | No measured carbon balance (E126). |
| Q5 Temperature | partly | External wall thermocouples with stated method and location (E031); gas and catalyst temperatures not measured. |
| Q6 Controls | partly | Measurements compared with a fitted CFD model; no experimental conventional or equilibrium comparison extracted. The industrial comparison is a design projection (E092-E108). |
| Q7 Repeatability | partly | Repeated GC measurements per condition (E041); no uncertainty or error bars (E131). |
| Q8 Stability | partly | Sampling and averaging periods stated (E041-E042); total time on stream not reported (E047); qualitative no activity loss (E086). |
| Q9 Energy completeness | no | Preheat and steam duties not reported (E049); electrical power not reported (E014). |

- Confidence in conversion/product results: **moderate**. Clearly labelled conversions at defined feeds and repeated GC measurements, but no balance closure, uncertainty or product flows.
- Confidence in energy results: **lower**. No electrical power or thermal duties are reported.

## Review log and pilot lessons

| Date | Reviewer | Scope and checks | Result |
|---|---|---|---|
| 2026-10-28 | Codex AI, same extractor | Read all manuscript/supplement text; visually inspected main pp. 2-3, supplement pp. 2, 5-9, 11-17, 20, 22; checked labels, units, boundaries and calculation arithmetic | ai_checked; plot readings remain approximate; no independent or human verification |
| 2026-10-28 | User instruction | Selected 5.3 mm inner diameter for calculations | Decision applied; contradictory source value retained |
| 2026-10-28 | Record-integrity checks | CSV re-read; unique IDs; operating-point joins; in-range page locators; calculation links; original PDF hashes | Passed (recorded at extraction; temporary validation file removed). |

The workflow successfully prevented three misleading comparisons: upstream voltage versus terminal voltage; catalyst effectiveness versus energy efficiency; projected industrial volume versus demonstrated laboratory scale.

Suggested refinements for subsequent sources:

1. Make voltage measurement location a mandatory qualifier, even when the value is missing.
2. Explicitly flag combustible inlet additives such as H2 when calculating product energy and gross/net production.
3. Record user-selected values separately from source-reported facts, as done here for inner diameter.
4. Separate field coverage from curve coverage. This pilot extracts labelled operating points, not every marker in every plot; later digitization should append stable IDs and preserve the approximate readings as a prior revision.

These are pilot findings; the shared protocol remains at version 0.1.

## Operating points

| OP | Label | Type | Conditions | Comparability | Evidence |
|---|---|---|---|---|---|
| OP001 | Lab 340 Nml/min, 58.0% CH4 conversion | experiment with fitted CFD temperature profile | CH4/H2O/H2 30/60/10; +50 mbar gauge; inlet 100 degC; wall exit about 600 degC | No point-matched electrical power; feed contains H2; flow reference T/P undefined; temperature approximate. | E038, E039, E040, E041, E031, E050, E051, E052, E137 |
| OP002 | Lab 340 Nml/min, 75.3% CH4 conversion | experiment with fitted CFD temperature profile | CH4/H2O/H2 30/60/10; +50 mbar gauge; inlet 100 degC; wall exit about 650 degC | No point-matched electrical power; feed contains H2; flow reference T/P undefined; temperature approximate. | E038, E039, E040, E041, E031, E053, E054, E055, E139 |
| OP003 | Lab 340 Nml/min, 86.5% CH4 conversion | experiment with fitted CFD temperature profile | CH4/H2O/H2 30/60/10; +50 mbar gauge; inlet 100 degC; wall exit about 700 degC | No point-matched electrical power; feed contains H2; flow reference T/P undefined; temperature approximate. | E038, E039, E040, E041, E031, E056, E057, E058, E141 |
| OP004 | Lab 340 Nml/min, 92.7% CH4 conversion | experiment with fitted CFD temperature profile | CH4/H2O/H2 30/60/10; +50 mbar gauge; inlet 100 degC; wall exit about 750 degC | No point-matched electrical power; feed contains H2; flow reference T/P undefined; temperature approximate. | E038, E039, E040, E041, E031, E059, E060, E061, E143 |
| OP005 | Lab 1020 Nml/min, 50.9% CH4 conversion | experiment with fitted CFD temperature profile | CH4/H2O/H2 30/60/10; +50 mbar gauge; inlet 100 degC; wall exit about 620 degC | No point-matched electrical power; feed contains H2; flow reference T/P undefined; temperature approximate. | E038, E039, E040, E041, E031, E062, E063, E064, E145 |
| OP006 | Lab 1020 Nml/min, 62.9% CH4 conversion | experiment with fitted CFD temperature profile | CH4/H2O/H2 30/60/10; +50 mbar gauge; inlet 100 degC; wall exit about 650 degC | No point-matched electrical power; feed contains H2; flow reference T/P undefined; temperature approximate. | E038, E039, E040, E041, E031, E065, E066, E067, E147 |
| OP007 | Lab 1020 Nml/min, 75.6% CH4 conversion | experiment with fitted CFD temperature profile | CH4/H2O/H2 30/60/10; +50 mbar gauge; inlet 100 degC; wall exit about 700 degC | No point-matched electrical power; feed contains H2; flow reference T/P undefined; temperature approximate. | E038, E039, E040, E041, E031, E068, E069, E070, E149 |
| OP008 | Lab 1020 Nml/min, 82.2% CH4 conversion | experiment with fitted CFD temperature profile | CH4/H2O/H2 30/60/10; +50 mbar gauge; inlet 100 degC; wall exit about 720 degC | No point-matched electrical power; feed contains H2; flow reference T/P undefined; temperature approximate. | E038, E039, E040, E041, E031, E071, E072, E073, E151 |
| OP009 | Lab 1020 Nml/min, 91.6% CH4 conversion | experiment with fitted CFD temperature profile | CH4/H2O/H2 30/60/10; +50 mbar gauge; inlet 100 degC; wall exit about 790 degC | No point-matched electrical power; feed contains H2; flow reference T/P undefined; temperature approximate. | E038, E039, E040, E041, E031, E074, E075, E076, E153 |
| OP010 | Lab 1700 Nml/min, 61.1% CH4 conversion | experiment with fitted CFD temperature profile | CH4/H2O/H2 30/60/10; +50 mbar gauge; inlet 100 degC; wall exit about 680 degC | No point-matched electrical power; feed contains H2; flow reference T/P undefined; temperature approximate. | E038, E039, E040, E041, E031, E077, E078, E079, E155 |
| OP011 | Lab 1700 Nml/min, 72.4% CH4 conversion | experiment with fitted CFD temperature profile | CH4/H2O/H2 30/60/10; +50 mbar gauge; inlet 100 degC; wall exit about 720 degC | No point-matched electrical power; feed contains H2; flow reference T/P undefined; temperature approximate. | E038, E039, E040, E041, E031, E080, E081, E082, E157 |
| OP012 | Lab 1700 Nml/min, 85.0% CH4 conversion | experiment with fitted CFD temperature profile | CH4/H2O/H2 30/60/10; +50 mbar gauge; inlet 100 degC; wall exit about 780 degC | No point-matched electrical power; feed contains H2; flow reference T/P undefined; temperature approximate. | E038, E039, E040, E041, E031, E083, E084, E085, E087, E088, E089, E159 |
| OP013 | Conventional side-fired reference design | industrial flowsheet/design reference | Reference: Tin 466 degC; Tout 920 degC; Pout 26.7 barg; S/C 1.8; 75.4% CH4 conversion | Not an experimental industrial demonstration. | E092, E093, E094, E095, E096, E097, E104, E105 |
| OP014 | Resistance-heated 75.4% scale-up | CFD extrapolation/design projection | Reference: Tin 466 degC; Tout 920 degC; Pout 26.7 barg; S/C 1.8; 75.4% CH4 conversion | Not an experimental industrial demonstration. | E098, E099, E100, E101, E102, E103, E106, E107, E108, E161 |
| OP015 | Resistance-heated 95% scale-up | CFD extrapolation/design projection | 95% conversion; 15 m3; capacity 2230 kmol H2/h; see Fig. 4 for scope | Not an experimental industrial demonstration. | E109, E110, E111 |
| OP016 | Supplementary industrial 75.6% case | CFD extrapolation | 1000 Nml/min/tube; 26.7 barg; S/C 1.8; 75.6% CH4 conversion; 20 degC equilibrium approach | Not an experimental industrial demonstration. | E112, E113, E114, E115, E116, E117 |

## Calculations

Source: SRC001. Protocol 0.1. Reviewer: Codex AI; same extractor, not independent human review. Date: 2026-10-28.
All results are AI-checked; none is human verified. IDs below reference evidence.csv.

### SRC001-C001 - Coated-zone gas-channel volume using selected 5.3 mm ID

Inputs: SRC001-E023 (5.2 mm bare ID), SRC001-E025 (5.3 mm alternate ID), SRC001-E022, SRC001-E024 (Fig. 2 geometry consistent with alternate ID), SRC001-E026 (280 mm coated length), SRC001-E027 (0.128 mm radial coat).

Formula: V_gas = pi/4 * (D_bare - 2*delta)^2 * L. Divide mm3 by 1000 to obtain mL.

- D_bare = 5.3 mm: V_gas = 5.594974 mL.

Decision: the user instructed "Just take 5.3 mm" on 2026-10-28. Use 5.3 mm as the bare tube ID, consistent with Fig. 2 wall geometry and supplementary p. 9. Preserve the preparation-section value of 5.2 mm as source evidence but do not use it in calculations.

Assumptions: uniform cylindrical channel and uniform radial coat. Excludes pore gas and the residual catalytically active outlet layer. This is a derived nominal volume, not a measured volume, complete active volume, or equipment volume. No dimensional uncertainty is reported. This user decision is not a human verification of all extracted evidence.

### SRC001-C002 - Conditional space time at the unspecified normal-flow reference

Inputs: SRC001-C001 and each operating point's total wet inlet flow evidence (linked in the Operating points table above). Formula: tau_N [s] = 60 * V_gas [mL] / F_N [Nml/min].

| Total inlet flow (Nml/min) | tau_N, selected 5.3 mm ID (s) |
|---|---:|
| 340 | 0.9873 |
| 1020 | 0.3291 |
| 1700 | 0.1975 |

These are nominal reference-flow space times, not reported author values and not actual hot residence times. Normal reference temperature/pressure is unspecified (SRC001-E045); gas expansion, reaction-induced mole changes, wall/gas temperature differences, and axial variations prevent conversion to an actual residence time from these data alone. Values are rounded for reporting; extra digits in CSV preserve the calculation, not measurement precision. No GHSV/WHSV is claimed.

### SRC001-C003 - HHV efficiency and electricity fraction: not calculable

eta_HHV = HHV_product_rate / D; f_electric = P_electric / D.
D = P_electric + HHV_external_feed_and_fuel_rate + Q_external,in.

Missing inputs: numerical point-matched power (SRC001-E014, SRC001-E015), external steam/preheat duty (SRC001-E049), complete product flows (SRC001-E122, SRC001-E124), and explicit normal-flow T/P (SRC001-E045). No numerical efficiency or electricity fraction is calculated. Heat flux in Fig. S5 cannot replace electrical input; ideal industrial insulation cannot be used as proof of complete measured energy closure.

The 10 mol% inlet H2 (SRC001-E038) is a combustible feed contribution and belongs in feed HHV as well as any gross outlet-H2 accounting. If a later metric uses net H2 production, specify it separately and avoid silently subtracting inlet H2 from only one side of an otherwise gross-stream balance. No external HHV property values were introduced in this pilot.

### SRC001-C004 - Laboratory steam-to-carbon ratio

Input: SRC001-E038. On the stated molar composition, S/C = 60/(30*1) = 2 mol steam/mol carbon. Methane is the only carbon-containing inlet component reported. This is reviewer-derived; industrial S/C = 1.8 is a different case.

### SRC001-C005 - Projected furnace/reformer volume ratio

Inputs: SRC001-E104 (1140 m3, Fig. 4) and SRC001-E106 (4.9 m3, Fig. 4 at 75.4% conversion). Ratio = 1140/4.9 = 232.65, approximately 230-fold.

This arithmetic uses printed figure values. Narrative values round to 1100 and approximately 5 m3. This is an industrial design/model comparison with furnace blowers/waste-heat equipment and electric wiring/power supply excluded. It is not a demonstrated full-plant size reduction. The abstract's potential 100-fold compactness statement is a broader rounded claim, not a separate measured benchmark. No uncertainty interval is supplied.

### SRC001-C006 - Methane feed for the experimental short summary

Inputs: SRC001-E038 (CH4 molar fraction 0.30) and the total normal feed flows in supplementary Figs. S2-S4 (SRC001-E050, SRC001-E062, SRC001-E077; each point also has its own flow record).

Formula: F_CH4,N = 0.30 * F_total,N, using the same unspecified normal-flow reference for both streams.

- 340 Nml/min total feed gives 102 Nml/min CH4; highest labelled conversion in Fig. S2 is 92.7% (SRC001-E060).
- 1020 Nml/min total feed gives 306 Nml/min CH4; highest labelled conversion in Fig. S3 is 91.6% (SRC001-E075).
- 1700 Nml/min total feed gives 510 Nml/min CH4; highest labelled conversion in Fig. S4 is 85.0% (SRC001-E084).

This is a volumetric split on the common normal reference, not a conversion to mol/s. No reference temperature or pressure is assumed. Results support short_summary.txt; no modelled industrial capacities are included there.

## Reproducibility and revision record

- Existing evidence IDs were preserved when the user selected 5.3 mm. Draft-only alternative-volume/lower-space-time IDs E134-E136, E138, E140, E142, E144, E146, E148, E150, E152, E154, E156 and E158 are retired, not reassigned; E135 is among the retired volume IDs. Current CSV contains 148 records; gaps in numbering are intentional. Selected volume is E162.
- Changes: initial pilot extraction; applied user's 5.3 mm decision; retained source discrepancy and documented all missing energy inputs.
- 2026-11-26: operating_points.csv, calculations.md and source_manifest.json merged into this file (Operating points, Calculations, Registration); no content changed.
