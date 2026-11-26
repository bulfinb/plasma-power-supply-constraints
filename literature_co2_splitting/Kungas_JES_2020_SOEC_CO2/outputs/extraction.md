# Source extraction: SRC025 (benchmark: SOEC CO2 electrolysis)

## Source and review

- Source ID / citation / DOI: SRC025. Küngas, R. (2020). Review - Electrochemical CO2 reduction for CO production: comparison of low- and high-temperature electrolysis technologies. J. Electrochem. Soc. 167, 044508. https://doi.org/10.1149/1945-7111/ab7099
- Source filenames and document versions: manuscript.pdf, published version (CC BY-NC-ND 4.0, IOP), SHA-256 `66a31d7ee6ea60d8e6c17105c24dff11a069d1106e70028ac8da9f2ba25e1e13`. PDF page 1 is the IOP cover sheet; article on PDF pages 2-12 (printed = PDF - 1). Same file as ../../../literature_reviews/Kungas_JES_2020_SOEC_CO2/manuscript.pdf (RV006).
- Retrieval date: 2026-11-09 (download stamp on PDF page 1).
- Protocol version: workflow.md 0.7; benchmark appraisal R1-R4 (section 5) in place of Q1-Q9; CO2-splitting metrics of [../../literature_review_objectives.md](../../literature_review_objectives.md).
- Extractor / date: Claude (AI), 2026-11-12.
- Coverage: SOEC content of the whole review (thermodynamics, figures of merit, Figs. 4-5, Tables I-II, industrial perspective). Low-temperature and molten carbonate data recorded only as context (E018).
- Reviewer / date / checks: Claude (AI), 2026-11-12; Eq. 16 reproduced against the reported voltage/EPC pairs (C001).
- Review status: ai_checked. Human check: none.

## Role in the review

SOEC benchmark (objectives: "Benchmarks"). The review is by a Topsoe author and summarises Topsoe's own stack tests (refs 57, 61, 62, conference proceedings) (E001). It is the citable peer-reviewed source for SOEC stack electricity use and durability. It gives no single-pass conversion, product purity or plant-level electricity (E019, E021); those need a second source (candidate: Hecimovic et al. 2024, record CR010).

## Electricity supply

- Electricity metric: EPC = E n F / (FE Vm), kWh per Nm3 CO, from the cell voltage and current, i.e. **DC electricity to the stack** (E011). Rectifier losses, heaters, blowers, compressors and product purification are outside this boundary (E009, E016).
- External heat: yes, for operation below the thermoneutral voltage (about 1.465 V, C002). The stacks in OP001-OP002 run at 1.05-1.28 V, so part of the reaction energy (283 kJ/mol) enters as heat; its amount is not reported (E003, E042). The 7600 h system included heaters and heat exchangers, with no power given (E016).

## Reactor configuration

- Solid oxide cells: LSCF-CGO | CGO | YSZ | Ni-YSZ (E013); 8250 cm2 active-area stacks at 750 C (E008); range 700-900 C (E004).
- O2 forms at the anode and leaves separately; with a pure CO2 feed the cathode product is CO + unconverted CO2, free of H2/H2O (E004). Unlike plasma, no O2 removal step is needed; CO/CO2 separation still is.

## Operating conditions

| OP | Test | Current density (mA/cm2) | Cell voltage (V) | Duration | Evidence |
|---|---|---|---|---|---|
| OP001 | stack, polarisation (Table I) | 200 +/- 30 (CO) | 1.1 (Table I); 1.13 (text) | NR | E007, E013 |
| OP002 | stack in furnace, durability | 450 | 1.24 -> 1.28 | 2000 h | E015 |
| OP003 | stack in a two-stack system with heaters and heat exchangers | 640 | ~1.38 -> ~1.5 (from EPC, C003) | 7600 h | E016, E017 |

Feed: CO2 (purity, flow and utilisation NR). Pressure NR. Temperature 750 C for the Fig. 4 stack; not stated for the durability tests.

## Performance indicators

- **Power boundary:** stack DC electricity (cell voltage x current), from Eq. 16.
- **External heat:** yes below thermoneutral; not quantified.
- Product separation/recycle: not included.

| OP | FE (%) | EPC (kWh/Nm3 CO) | EC_CO = EC_CO2 (kJ/mol) | Fraction of dH as electricity | X_CO2 |
|---|---|---|---|---|---|
| OP001 | 100 | 2.5 (Table I) [2.70 from 1.13 V] | 202 [218] | 71% [77%] | NR |
| OP002 | 100 | 2.96 -> 3.06 | 239 -> 247 | 84-87% | NR |
| OP003 | 100 | ~3.3 -> ~3.6 (Fig. 5a) | ~266 -> ~290 | ~94-103% | NR |

- Author's metrics: EPC (above), EE = E0 FE / E on a Gibbs-energy basis, cell only: >90% at 200 mA/cm2, >70% at 700-800 mA/cm2 (E009, E010). Not recalculated.
- Range statement: SOEC stack EPC below 3.4 kWh/Nm3 even at very high current density; 2.5 at ~200 mA/cm2 (E014). Theoretical minimum 2.3 kWh/Nm3 at 800 C (E012).
- Degradation: 2.2 %V/1000 h (2000 h test); 1.2-1.3 %V/1000 h (7600 h system test) (E015, E016).
- Scale: 12 Nm3/h CO demo (2016); two 96 Nm3/h commercial plants contracted for 2020 (E020).
- **Conversion: not reported** (E021). Measured single-pass utilisation and CO purity are needed from another source.

## Reporting quality (benchmark items R1-R4)

| Item | Answer | Reason and evidence IDs |
|---|---|---|
| R1 Data type | measured | Stack test data (Topsoe), reported second-hand in a review; primary data in conference proceedings refs 57, 61, 62 (E001, E015, E016). |
| R2 Boundary | partly | Stack DC electricity only; heat, heaters, rectifier and balance of plant excluded and not quantified (E011, E016, E019). |
| R3 Basis | partly | Nm3 at "normal conditions" (22.414 L/mol reproduces the values); stack size and temperature given; feed flow, utilisation and pressure NR (E008, E011, E021). |
| R4 Independence | no | Author employed by the eCOs vendor; data are the company's own tests; no competing-interest statement (E001, E022). |

- Confidence in conversion/product results: lower. FE 100% is stated and verified by chromatography (E006), but conversion and purity are not reported.
- Confidence in energy results: moderate. Stack EPC values are consistent with the reported voltages (C001) and with each other across tests, but the boundary excludes heat and balance of plant, and the data are vendor-sourced.

## Gaps and comparison limits

- Stack DC electricity is not comparable one-to-one with plasma wall-plug values (e.g. Kiefer 2024, SRC016: 19.6 kWh/Nm3). At minimum a rectifier efficiency and the heat supply must be added; both are outside this source. Record the comparison as "stack DC; heat excluded" vs "wall-plug".
- Internal inconsistency at OP001: Table I gives EPC 2.5 kWh/Nm3 at 1.1 V, but the text gives 1.13 V for the same stack at 200 mA/cm2, which by Eq. 16 is 2.70 kWh/Nm3 (E007, E013). Both kept.
- Single-pass conversion, CO purity, feed utilisation and plant-level EPC: not reported (E019, E021).
- Durability-test temperatures not stated.

## Calculations

All in outputs/calculations.py.

- SRC025-C001 Eq. 16 check: EPC = E n F / (FE Vm) with 22.414 L/mol reproduces 2.96 and 3.06 kWh/Nm3 from 1.24 and 1.28 V (E015). 1.1 V gives 2.63 against the Table I 2.5 (rounding or inconsistency, see Gaps). Result E042.
- SRC025-C002 Thermoneutral voltage V_tn = 282.7 kJ/mol / 2F = 1.465 V, EPC 3.50 kWh/Nm3. Result E042.
- SRC025-C003 EC_CO (kJ/mol) = EPC x 3600 / (1000/22.414); cell voltage back-calculated from EPC; fraction of dH supplied as electricity. Result E041.

## Revisions

None.

## Plasma characteristics

Not applicable (electrochemical benchmark).
