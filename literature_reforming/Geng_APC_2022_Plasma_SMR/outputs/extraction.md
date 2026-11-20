# Geng et al. (2022): plasma-assisted SMR

## Source and review

- Source ID: **SRC002**. Feiyang Geng, Vasudev P. Haribal and Jason C. Hicks, "Non-thermal plasma-assisted steam methane reforming for electrically-driven hydrogen production," Applied Catalysis A, General 647 (2022), 118903. DOI: https://doi.org/10.1016/j.apcata.2022.118903.
- Documents: supplied published [manuscript.pdf](../manuscript.pdf), 9 pages; [ESI.pdf](../ESI.pdf), 5 pages; original [ESI.docx](../ESI.docx). Retrieval/export dates unknown. PDF page numbers below are 1-based; ESI pages have no printed page numbers.
- Protocol: 0.1, incorporating the user's request for separate plasma scale. Extractor/reviewer: Codex AI, 2026-10-28, same-extractor checks. Status: **ai_checked; human verification pending**.
- Coverage: full manuscript and ESI text read; manuscript pp. 2-7 and ESI pp. 2, 3, 5 visually inspected; selected headline/control conditions extracted, not every plotted point. DOCX text has the same five figure captions and five embedded images, with no tables; the PDF is the citation reference. Image-by-image equivalence was not independently established.
- SHA-256, original files unchanged:
  - manuscript.pdf: `9f074ebfc8c0ce9d3efca9d2de06997cc753e1d3d67c8b97a6a11bf92d03e5ce`
  - ESI.pdf: `6f29c21456c523f6a9cc6cab6292ca05e4895ac00c2f8f4b502e841f6485efeb`
  - ESI.docx: `bdc63b75b3e2faa53b0490e145cfb8f65fb4f63847c1a65001e739b1bb8a3653`
- Records: [evidence.csv](evidence.csv), 64 records; [short_summary.txt](../short_summary.txt). Evidence IDs abbreviated below as E001 mean SRC002-E001. Condition IDs refer to the table below. No separate condition/calculation file is needed.

## Electricity supply

**Classification: nonthermal DBD plasma-assisted catalytic reforming with a temperature-controlled thermal background, not demonstrated plasma-only heating.** The authors set bulk gas temperatures of 300-440 degC and compare thermal operation with plasma added. The reactor heater technology and duty are not specified. A heated upstream steam generator is described (E005-E007). Do not infer the energy partition from the paper's phrase "electrically-driven."

| Quantity | Extraction | Evidence |
|---|---|---|
| Plasma scale | 10, 15 and 20 W reported discharge power; 0 W is plasma off | E001-E003 |
| Total process energy scale | Not reported; plasma watts omit unquantified thermal/upstream inputs and supply losses | E007 |
| Voltage | Example Q-V loop spans roughly -4.6 to +4.6 kV; not RMS and not assigned to a specific operating point | E004; ESI p. 2, Fig. S2 |
| Supply | High-voltage AC PMV500; detailed waveform/frequency/current not reported | E001; missing checklist |
| Power measurement | Oscilloscope Q-V loop, 10 nF monitor capacitor and 1000:1 voltage attenuation | E002 |

The authors describe using loop area to determine plasma power. Physically, Q-V loop area gives energy per cycle; frequency is needed to reconstruct average power. Frequency is not numerically supplied, so retain the authors' reported wattages without claiming independent reconstruction. These values are not wall-plug consumption. The illustrative voltage loop cannot be joined to all power settings.

For **plasma off**, retain the thermal operating temperature and mark only discharge power as zero. Do not mark total electricity or external heat as zero. Thermal heating and steam generation could themselves consume electricity; their energy carrier and duties are not quantified.

## Reactor configuration

Double-inlet quartz tube, 5.0 mm ID/7.5 mm OD; 1 mm OD tungsten inner electrode and external stainless steel mesh; packed bed held at 6 cm length. Catalyst/packing pellets are 250-355 micrometres (E008-E015). The principal catalyst charge is 200 mg commercial Ni/CaAl4O7 diluted with alumina. Its purchased composition is reported on an oxide basis (17.5 wt% NiO, 10.5 wt% CaO, 72 wt% Al2O3); this is not 17.5 wt% metallic Ni (E013-E014). The temperature study specifies 500 mg alumina with the catalyst (E016).

The thermocouple is **1.5 cm below the bed**, measuring what the authors call bulk gas temperature; catalyst surface temperature and local hot spots are not measured by this probe (E017). ESI Fig. S3 maps the gas, steam and electrical paths (E019).

The cascade comparison adds Cu/ZnO/Al2O3/MgO downstream at 300 degC, or within the plasma zone. Keep these configurations separate from the principal Ni-only experiment (E018, E059).

## Operating conditions

Baseline SMR: 300 degC, ambient pressure, nominal S/C 4.4. Temperature study: 300/370/440 degC at 15 W. Water study: 0.08-0.12 mL liquid water/min and S/C 4.4-6.6 at constant methane flow (E020-E023).

**Feed ambiguity:** methods say "25 (+/-1) ml/min methane and steam." It is unclear whether 25 refers to methane alone or mixed feed. The water rate, stated S/C and hydrogen outputs make that distinction important. Preserve the wording and do not assign an exact methane/total-flow basis without clarification. Flow reference temperature/pressure is also unspecified. Plasma scale is available even though methane throughput cannot be unambiguously normalized.

Selected matched conditions (all experimental; approximate values retained as such):

| Point | Catalyst/configuration | Plasma (W) | Bulk gas (degC) | S/C | CH4 conversion | Evidence |
|---|---|---:|---:|---:|---|---|
| SRC002-OP001 | 200 mg Ni/CaAl4O7 + alumina, thermal | 0 | 300 | 4.4 | about 7% | E033-E034 |
| SRC002-OP002 | Same catalyst, plasma on | 15 | 300 | 4.4 | about 60% | E035-E036 |
| SRC002-OP003 | Ni catalyst, power sweep | 10 | 300 | 4.4 text / 4.5 caption | about 50% | E037-E038 |
| SRC002-OP004 | Ni catalyst, power sweep | 20 | 300 | 4.4 text / 4.5 caption | about 74% | E039-E040 |
| SRC002-OP005 | Ni catalyst, temperature control | 0 | 370 | 4.4 | about 22% | E041-E042 |
| SRC002-OP006 | Ni catalyst, temperature sweep | 15 | 370 | 4.4 | about 67% | E043-E044 |
| SRC002-OP007 | Ni catalyst, temperature control | 0 | 440 | 4.4 | about 44% | E045-E046 |
| SRC002-OP008 | Ni catalyst, temperature sweep | 15 | 440 | 4.4 | nearly 80% | E047-E048 |
| SRC002-OP009 | Alumina only, thermal | 0 | 300 | 4.4 | none observed | E049-E050 |
| SRC002-OP010 | Alumina only, plasma on | 15 | 300 | 4.4 | about 30% | E051-E052 |
| SRC002-OP011 | Ni catalyst, water sweep | not explicitly restated | 300 | 6.6 | about 74% | E053 |
| SRC002-OP012 | Ni plasma bed + 143 mg downstream Cu | not explicitly restated | 300 | 4.4 | not separately quantified for 143 mg case | E059 |

Plotted 370/440 degC thermal and 370 degC plasma values are visual estimates, roughly +/-3 percentage points reading precision; this is not author measurement uncertainty. Other approximate conversions come from author text. Bars/error bars occur in the figures, but a statistical definition is not supplied in the extracted methods.

**Duration:** Fig. 2c reaches about 130 min after plasma ignition for the Ni catalyst. Alumina coke analysis explicitly follows 2 h of reaction; Ni coke is discussed after the same reaction time. The stepped 0/10/15/20 W series reaches about 225 min, not 225 min continuously at 20 W (E026-E028). The 7 h reduction, 2 h Ar purge, 1 h steam stabilization and >=30 min pre-ignition period are preparation, not plasma-reforming durability tests (E024-E025).

## Performance indicators

- **Conversion:** headline nearly 80% at 15 W and 440 degC; at 300 degC, about 60% at 15 W and about 74% at 20 W. These are different conditions. The same-temperature Ni-catalyst plasma-on/off comparison is about 60% versus 7%, not a comparison of complete energy efficiencies.
- **Hydrogen:** author overall H2 selectivity is about 88% in the baseline 15 W Ni comparison and about 90% at 20 W (E054-E055). These are selectivities, not energy efficiencies. The temperature series reports H2 output increasing from 45 to 60 mL/min at 300 to 440 degC, 15 W (E058). Power-series text/figure values differ and are retained separately (E056-E057).
- **Cascade:** downstream Cu gives CO2/CO about 15 with 143 mg Cu; putting Cu within plasma does not give the same improvement. Text reports 63-65% methane conversion for the 60 mg Cu/alumina comparison; do not silently attach that conversion to the 143 mg case (E059).
- **Space time:** no author-defined residence time/GHSV/WHSV found. Nominal annular bed envelope is 1.131 mL (C001). Packing void fraction, effective active-plasma volume and unambiguous inlet-flow basis are unavailable, so no actual residence time is calculated.

### Energy assessment

- **Author energy metric:** no numerical experimental energy efficiency or closed energy-balance indicator located (E061). The reported power, conversion, selectivity and carbon balance characterize performance but do not give overall energy efficiency.
- **Our HHV efficiency / electricity fraction:** unavailable. Discharge power is reported, but total electrical consumption, reactor-heating duty, steam/preheat duties and compatible stream/reference-state data are incomplete (E007, E020, E061). Do not set external heat to zero or treat 15 W as the whole denominator. Do not infer electricity fraction = 100% from plasma operation.
- **Power-basis metrics (reviewer calculations, power basis; external heat excluded):** SEI_CH4 about 894 kJ/mol CH4 fed (9.3 eV/molecule) at 15 W. EC_CH4 about 1490 kJ/mol (15.5 eV/molecule) at SRC002-OP002 and about 1120 kJ/mol (11.6 eV/molecule) at SRC002-OP008. EC_H2 about 450-490 kJ/mol H2 and EY_H2 about 15-16 g H2/kWh at 300 degC; about 340-370 kJ/mol and 20-22 g/kWh at 440 degC. These use the methane flow derived from the water feed (C003) and include only the 15 W discharge power. Furnace and steam-generator heat are not reported, so no heat-included value can be calculated. EC_CH4 is about seven times the 206 kJ/mol SMR reaction enthalpy at 300 degC. eta_P,LHV is not calculable because point-matched CO flows were not extracted (C003-C005; E065-E070).
- **Completeness:** known discharge power; known operating temperature and existence of steam generation; unknown thermal duties, wall-plug losses, auxiliaries and recoverable heat. Plasma-off remains a heated reference, not a zero-energy reference. Differences in conversion do not determine thermal/plasma energy shares.

## Reporting quality

Appraised 2026-10-30 by Claude (AI) from the existing extraction records and evidence IDs, without re-reading the PDFs. Status: unreviewed; human check pending.

| Item | Answer | Reason and evidence IDs |
|---|---|---|
| Q1 Power measurement | partly | Q-V loop method stated (E002), but repetition frequency is not reported, so the 10/15/20 W values cannot be reconstructed; discharge power only. |
| Q2 Feed definition | partly | S/C and liquid water rate stated (E021-E022); methane-flow wording unclear and flow reference conditions not stated (E020). Water rate supports 25 mL/min CH4 (C003). |
| Q3 Product analysis | partly | GC-TCD with cold trap (E019); conversion equation uses measured product flow (E029). Calibration details not extracted. |
| Q4 Balance closure | partly | Carbon balance reported (about 90%), but the printed equation is inconsistent (E032). |
| Q5 Temperature | partly | Bulk gas thermocouple 1.5 cm below the bed (E017); catalyst temperature not measured. |
| Q6 Controls | yes | Plasma-off at the same temperature (OP001, OP005, OP007) and alumina-only with and without plasma (OP009, OP010). |
| Q7 Repeatability | partly | Error bars shown in figures; statistical definition not given. |
| Q8 Stability | partly | About 2 h time series at 15 W (E026-E028); no steady-state criterion extracted; no long-term test. |
| Q9 Energy completeness | no | Furnace, steam-generator and wall-power duties not reported (E007). |

- Confidence in conversion/product results: **moderate**. Matched controls are strong, but feed wording, carbon-balance definition and uncertainty are unclear.
- Confidence in energy results: **lower**. Only discharge power is known, its reconstruction is not possible, and the furnace supplies an unquantified share of the heat.

## Missing information and comparison limits

| Status | Gap or issue | Consequence |
|---|---|---|
| not_reported | Frequency, point-matched voltage/current and detailed waveform; supply efficiency/wall power | Cannot reconstruct electrical input from first principles or wall consumption |
| not_reported | Reactor-heater identification/duty; steam-generation/preheat duty; auxiliaries | No total energy scale, HHV efficiency or electricity fraction |
| unclear | 25 +/-1 mL/min flow wording; volumetric reference conditions | No defensible exact methane-throughput or common flow normalization |
| not_reported | Void fraction, defined residence time/GHSV/WHSV and effective active-plasma volume | No actual residence-time comparison |
| unclear | Fig. 3 caption S/C 4.5 versus text 4.4; conclusion says up to 7.7 while water study shows up to 6.6 | Preserve series definitions; do not create an experimental point at 7.7 |
| unclear | H2 power-series text: 40 at 10 W / 60 at 15 W, versus plotted roughly 37/52/62 at 10/15/20 W | Do not assemble a precise product-energy balance by mixing text and figure values |
| unclear | Printed Eq. (6) includes unconverted CH4 in numerator but converted CH4 in denominator | Retain literal formula (E032), flag inconsistency, do not reconstruct carbon closure from it |
| unclear | Overall-H2-selectivity printed normalization in Eqs. (3)-(4) | Retain author definition (E031); seek clarification before independent atom-balance reconstruction |
| not_reported | Long-duration steady operation, restart/cycle history and uncertainty definitions | Hour-scale plots do not establish long-term durability |

The paper supports a comparison of **plasma-assisted conversion at a stated thermal background**. It does not support ranking against Joule-heated SMR on total energy consumption without additional data. Values quoted from other studies in the introduction/discussion are not experimental results of this source; separate WGS/RWGS controls in Fig. 8 are not headline SMR conversion tests.

## Calculations

### SRC002-C001: nominal annular bed envelope

Inputs E008, E010, E011: quartz ID 5 mm, rod OD 1 mm, bed length 60 mm. Assuming a centered rod spanning the bed:

`V = pi/4 * (5^2 - 1^2) * 60 / 1000 = 1.130973 mL`, approximately **1.13 mL** (E063).

This geometric envelope includes packing solids; it is not void volume, measured active discharge volume or equipment volume. No material porosity or actual residence time is inferred.

### SRC002-C002: matched conversion difference

Inputs E034/E036: `60% - 7% = approximately 53 percentage points` at 300 degC, S/C 4.4, matching Ni-catalyst configuration (E064). This is a conversion difference, not energy efficiency or a measured nonthermal fraction of the reaction.

Calculations C003-C005 are reproduced by [calculations.py](calculations.py) (`python3 calculations.py`).

### SRC002-C003: methane feed from the water feed

Inputs E021-E022: 0.08 mL/min liquid water at S/C 4.4 (0.08 to 0.12 mL/min corresponds to S/C 4.4 to 6.6 at constant methane flow; the 0.08-4.4 pairing is inferred from that ratio). Assumed water density 0.997 g/mL; M_H2O = 18.015 g/mol.

`F_H2O = 0.08 * 0.997 / 18.015 = 4.427e-3 mol/min`; `F_CH4,in = 4.427e-3 / 4.4 = 1.006e-3 mol/min = 1.677e-5 mol/s` (E065).

This equals about 22.6 mL/min at 0 degC/1 atm or 24.6 mL/min at 25 degC/1 atm. It supports reading the methods' "25 (+/-1) ml/min methane and steam" as 25 mL/min of methane, not of total feed; a total feed of 25 mL/min would imply only about 4.6 mL/min CH4. The interpretation is the reviewer's; BB confirmed it on 2026-11-20 against PDF pp. 2-6 (feed sentence, water feed 0.08-0.12 mL/min at S/C 4.4-6.6, S/C 4.4 baseline with the Fig. 3 caption giving 4.5). The GPT cross-check reached the same feed independently (XR006). The molar flow does not depend on the gas reference conditions.

### SRC002-C004: power-basis SEI and EC_CH4

Inputs C003; E035-E036 (OP002: 15 W, about 60%); E047-E048 (OP008: 15 W, nearly 80%, taken as 80%). 1 eV/molecule = 96.485 kJ/mol.

- `SEI_CH4 = 15 / 1.677e-5 = 894 kJ/mol CH4 fed (9.3 eV/molecule)` (E066).
- OP002: `EC_CH4 = 15 / (1.677e-5 * 0.60) = 1491 kJ/mol (15.5 eV/molecule)` (E067).
- OP008: `EC_CH4 = 15 / (1.677e-5 * 0.80) = 1118 kJ/mol (11.6 eV/molecule)` (E068).

Power basis is reported discharge power only; furnace and steam-generator heat excluded and not reported. Conversions are approximate author values.

### SRC002-C005: power-basis EC_H2 and EY_H2

Inputs E058: H2 output 45 mL/min at 300 degC and 60 mL/min at 440 degC, 15 W, S/C 4.4 (temperature series, same nominal conditions as OP002/OP008). The flow reference is not stated, so results are given for 0 degC (22.414 L/mol) and 25 degC (24.465 L/mol). No H2 is fed, so gross equals net.

- 300 degC: `EC_H2 = 448-489 kJ/mol H2`; `EY_H2 = 14.8-16.2 g H2/kWh` (E069).
- 440 degC: `EC_H2 = 336-367 kJ/mol H2`; `EY_H2 = 19.8-21.6 g H2/kWh` (E070).

The H2 flows come from the temperature series, while OP002's conversion comes from the Fig. 2 series at the same nominal conditions.

## Review and revisions

- 2026-10-28: same-extractor AI checked selected values against rendered original pages, identified on/off thermal controls, checked arithmetic, and retained contradictory statements separately. Human verification pending.
- Structural checks: 64 unique evidence IDs, valid source page ranges and CSV re-read; original PDF/DOCX hashes unchanged. Used IDs/condition table and calculation links checked.
- Applied user's request for separate plasma scale. Shared workflow updated to 0.7 without adding another required output file.
