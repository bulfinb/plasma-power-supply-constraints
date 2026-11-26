# Source extraction: SRC026 (benchmark: microwave plasma vs LT and HT electrolysis)

## Source and review

- Source ID / citation / DOI: SRC026. Hecimovic, A., Mayer, M.T., de Haart, L.G.J., Gupta, S., Kiefer, C.K., Navarrete, A., Schulz, A., Fantz, U. (2024). Benchmarking microwave-induced CO2 plasma splitting against electrochemical CO2 reduction for a comparison of promising technologies. J. CO2 Util. 83, 102825. https://doi.org/10.1016/j.jcou.2024.102825
- Source filenames and document versions: manuscript.pdf, published version (CC BY-NC-ND 4.0), KIT repository copy (publikationen.bibliothek.kit.edu/1000171552), SHA-256 `cb62f722a4d1bcbd4c3a8e80fb26bccb9c7f8ef6026092cd0a7faed73800731d`. 15 pages; printed page = PDF page. Supplementary Note (Table S1, LT electrolysis compilation) not obtained.
- Retrieval date: 2026-11-12 (downloaded by Claude).
- Protocol version: workflow.md 0.7; benchmark appraisal R1-R4; CO2-splitting metrics of [../../literature_review_objectives.md](../../literature_review_objectives.md).
- Extractor / date: Claude (AI), 2026-11-12.
- Coverage: whole paper; Tables 1 and 2 read from rendered pages (images in the PDF).
- Reviewer / date / checks: Claude (AI), 2026-11-12; Table 1 values cross-checked against EPC = 3.504 kWh/Nm3 / eta (C001-C004).
- Review status: ai_checked; partial human check by BB, 2026-11-25: OP001 (E009, E014, E041) confirmed; reported 3.89 kWh/Nm3 taken as a typo and the more conservative 3.98 used (human_checks/summary.csv). Other records: no human check.

## Role in the review

Second SOEC benchmark (record CR010), filling what Küngas 2020 (SRC025) lacks: SOEC conversion, CO purity and a system-level electricity figure. It is a comparison paper, not a single experiment. It is also the only source so far that sets plasma, LT and HT electrolysis side by side on one EPC basis. Plasma values for the cooled-channel torch duplicate SRC016/SRC017 (same group) and are not counted again; new plasma data are the membrane O2-separation demonstrator and the KEROGREEN 915 MHz setup.

## Electricity supply

- EPC_reactor (Table 1: EPC_process) uses power deposited in the reactor; EPC_total uses total power for the supply and peripherals (pumps, flow meters, cooling/heating) (E003).
- FZJ SOEC system: stack input 69.6 kW (DC); wall-plug efficiency computed with an assumed inverter/rectifier efficiency of 0.95 (E009).
- eCOs: EPC_tot 6-8 kWh/Nm3 from the Topsoe website, boundary not stated (E014).
- Plasma: microwave magnetron supplies up to 3 kW (2.45 GHz) and 6 kW (915 MHz, KEROGREEN) (E005, E012). Magnetron lifetime 8000 h, solid-state supplies "several years" (E020). Larger supplies: 15 kW at 2.45 GHz, up to 100 kW at 915 MHz (E008).

## Reactor configuration

- SOEC (FZJ): five-layer short stack, Ni-YSZ/YSZ/CGO/LSCF, 10x10 cm2 cells (80 cm2 effective), 800 C; scaled to a 70 kW system with a flow scheme adapted from a 10/40 kW reversible SOC demonstrator (ref. 111) (E009). CO is recirculated to the feed to keep Ni reduced (E021).
- eCOs: commercial SOEC system, 6-200 Nm3/h CO (E014).
- Plasma: 2.45 GHz torch with cooled effluent channels and reverse vortex (as SRC016/SRC017), and a nozzle version with 21 LCCF O2-permeable membranes in the ~1000 C effluent, swept with Ar (E005, E006, E011).

## Operating conditions

| OP | Technology | Basis | Scale | Evidence |
|---|---|---|---|---|
| OP001 | HT electrolysis, FZJ | calculation from measured short-stack IV | 70 kW, 1.0 A/cm2, 800 C, utilisation 86% | E009, E014 |
| OP002 | HT electrolysis, Topsoe eCOs | vendor data | 6-200 Nm3/h CO | E010, E014 |
| OP003 | LT electrolysis pilot (Krause et al. 2020) | literature value | 300 cm2, 240 W | E015 |
| OP004 | MW plasma, cooled channels | measured (= SRC016/SRC017) | 3 kW | E016 |
| OP005 | MW plasma with O2 membranes | measured | 3 kW | E011, E016 |
| OP006 | MW plasma, KEROGREEN 915 MHz | project data (website) | 6 kW, up to 60 slm | E012, E016 |

All at about 1 bar outlet (E019).

## Performance indicators

- **Power boundary:** EPC_total as defined by the authors (supply plus peripherals); FZJ includes a 0.95 rectifier assumption; eCOs boundary unknown (vendor).
- **External heat:** FZJ runs at ~1.66 V implied (C001), above the thermoneutral ~1.465 V, so the stack itself needs no external heat; preheating and heat-exchanger duties are in the flow scheme but not reported. eCOs: unknown.

| OP | X_CO2 (%) | CO out (Nm3/h) | EPC_tot (kWh/Nm3 CO) | EC_CO (kJ/mol) | Wall-plug eff. (%) | Product |
|---|---|---|---|---|---|---|
| OP001 FZJ | 86.6 (design cap 86) | 17.5 | **3.98-4.19** (calculated, C001; reported 3.89) | 321-338 | 83.7-88.1 calc. (reported 89.0) | CO + CO2, no separation |
| OP002 eCOs | >95 (up to 95 in text) | 6-200 | 6-8 (vendor) | 484-646 | 90 (inconsistent, see Gaps) | 99.0 vol% CO standard; up to 99.999 |
| OP003 LT pilot | 35 | 0.023 | NR (EPC_process 10.2) | NR | NR | CO, CO2, H2, H2O |
| OP004 MW plasma | up to 56 | 0.22 | 19.8 | 1598 | up to 18 | CO2/CO/O2 |
| OP005 MW + membranes | up to 26 | 0.12 | 35 | 2824 | up to 10 | CO2/CO/O2, 5% of O2 removed |
| OP006 KEROGREEN | 14 | 0.56 | NR (EPC_process 11.4) | NR | NR (EE 34) | CO2/CO/O2 |

- Maximum conversion and efficiency are not simultaneous for plasma and LT (authors, p. 11); the plasma rows combine maxima from different conditions and are not used as matched points. Matched plasma points come from SRC016.
- SOEC conversion: utilisation "can be as high as 95%" (E010); FZJ capped at 86% "to prevent any carbon formation" (E009); CO recirculation keeps Ni reduced (E021).
- O2 separation for plasma: required for most uses (O2 below 1%, e.g. Fischer-Tropsch); no efficient continuous method yet; the membrane demonstrator removed 5% of the O2 (E007, E011).
- CO/CO2 separation by PSA: ~0.25 kWh/Nm3 of gas treated (Jouny et al. 2018, cited) (E018). Useful for the separation step in the whole-system assessment.
- Durability: SOEC tested up to 8000 h, LT 4000 h, plasma 29.3 h; SOEC cold start 4-6 h with hot standby needed, plasma and LT start in minutes (E019).

## Reporting quality (benchmark items R1-R4)

| Item | Answer | Reason and evidence IDs |
|---|---|---|
| R1 Data type | mixed | FZJ SOEC: process calculation from measured short-stack IV (E009). eCOs: vendor website (E010, E014). Plasma: measured lab data (E016). KEROGREEN: project website (E012). |
| R2 Boundary | partly | EPC_total defined (E003), but FZJ uses an assumed rectifier efficiency and eCOs gives no boundary; heat-exchanger and preheat duties not reported. |
| R3 Basis | partly | Nm3 normal conditions implied (3.51 kWh/Nm3 at 100%, E013); FZJ CO flow given as "m3/h" without reference conditions; scales stated. |
| R4 Independence | yes for authors, no for eCOs data | No vendor author, no competing interests declared (E001, E002); eCOs values are Topsoe's own claims. |

- Confidence in conversion/product results: moderate. SOEC conversion and purity are stated but come from a design cap (FZJ) and vendor data (eCOs).
- Confidence in energy results: lower for the SOEC benchmark values. The FZJ reported EPC 3.89 does not match its own inputs (stack-only 3.98; with the stated 0.95 rectifier 4.19), likely a 3.89/3.98 transposition; the calculated range is used, and the eCOs 6-8 kWh/Nm3 contradicts the 90% wall-plug efficiency in the same column, as the authors' own footnote notes. Plasma values are consistent with SRC016.

## Gaps and comparison limits

- **FZJ value (C001):** stack 69.6 kW / 17.5 m3/h = 3.98 kWh/Nm3 at the stack (88.1%); with the stated 0.95 rectifier, 4.19 kWh/Nm3 (83.7%). The reported 3.89 is probably a transposition of 3.98 (BB, 2026-11-12). **The review uses the calculated range 3.98-4.19 kWh/Nm3 CO** (design calculation, stack DC to wall-plug with assumed rectifier).
- **eCOs inconsistency (C002, E013):** 6-8 kWh/Nm3 implies 44-58% efficiency, not 90%. The 6-8 figure is the only plant-level electricity number in hand; its boundary (compression, purification, heaters, standby) is unknown.
- SOEC heat: FZJ at 1 A/cm2 operates above thermoneutral, so its electricity covers the reaction enthalpy; Küngas's lower-current stack values (SRC025, 2.5-3.6 kWh/Nm3) do not. Use FZJ-type values for a wall-to-product comparison.
- KEROGREEN: only website data; no EPC_total; 0.56 Nm3/h implies ~67 slm at 14% against a stated maximum of 60 slm (C004).

## Calculations

All in outputs/calculations.py. EPC at 100% efficiency 3.504 kWh/Nm3 (dH 282.7 kJ/mol, 22.414 L/mol), matching the authors' 3.51 (E013).

- SRC026-C001 FZJ consistency: stack EPC, EPC with 0.95 rectifier, efficiency at each, implied cell voltage. Inputs E009. Result E041.
- SRC026-C002 Efficiency implied by each Table 1 EPC, and EC_CO in kJ/mol. Inputs E014-E016. Result E042.
- SRC026-C003 CO flow from the membrane O2 figure (42 sccm = 5%). Input E011. Result E043.
- SRC026-C004 KEROGREEN CO flow from 60 slm x 14%. Inputs E012, E016. Result E043.

## Revisions

None.

## Plasma characteristics

As SRC016 for the cooled-channel torch (core ~6000 C cited, E005). Effluent 300-400 C behind the cooled channels, ~1000 C behind the nozzle (E006). No other diagnostics.
