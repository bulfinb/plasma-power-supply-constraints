# From et al. (2024): electrified SMR of biogas, pilot plant

## Source and review

- Source ID: **SRC005**. Thomas N. From, Behzad Partoon, Marené Rautenbach, Martin Østberg, Anders Bentien, Kim Aasberg-Petersen and Peter M. Mortensen, "Electrified steam methane reforming of biogas for sustainable syngas manufacturing and next-generation of plant design: A pilot plant study," Chemical Engineering Journal 479 (2024) 147205. DOI: https://doi.org/10.1016/j.cej.2023.147205. Open access, CC BY-NC.
- Documents: [manuscript.pdf](../manuscript.pdf), 9 pages, publisher version (Topsoe-hosted copy); printed page numbers equal PDF page numbers. [supplementary.docx](../supplementary.docx), Supporting Information (energy efficiency and consumption models, Eqs. S4-S12), from the Elsevier supplementary-file server (mmc1.docx), kept in the format supplied. Retrieved 2026-11-04.
- SHA-256:
  - manuscript.pdf: `752f830bde1f30f96c2d88e3fa001afdfed3e2594a0e0b5923ab9d314c29e34d`
  - supplementary.docx: `bf2cca1ca61fcc9b135540a8cf8b472841b04720ae6b8ad5e04c58093bb33981`
- Protocol: 0.1. Extractor/reviewer: Claude (AI), 2026-11-04, same-extractor checks. Status: **ai_checked; human verification pending**.
- Coverage: full manuscript and Supporting Information read; Figs. 3-5 inspected visually and Fig. 5 graph-read. Modelled scale-up results (Fig. 5 curves, Fig. 6 flowsheet, Section 3.4) recorded only as modelling.
- Role in review: Joule-heated benchmark at pilot scale (primary electrified benchmark; Wismann 2019, SRC001, is the lab-scale complement).
- Records: [evidence.csv](evidence.csv), 33 records (E001-E031, E041-E042); [calculations.py](calculations.py); [short_summary.txt](../short_summary.txt). Evidence IDs below abbreviated E001 = SRC005-E001.

## Electricity supply

The catalyst structure is heated directly by electrical current (eREACT, Ni active material; E003). Power comes from an Agilent N8951A power supply unit (E004). The authors calculate power as Q_in = I·V, described as the "total power delivered from the PSU" (E005). The same paragraph also says "power received by the PSU", so whether Q_in sits before or after the PSU is **unclear**. Grid-to-PSU losses are not reported.

Absolute power is not tabulated. Fig. 4 gives power only relative to a 900 degC base case (about 52-65% at 750 degC and about 117% at 1000 degC; E015). Fig. 5 plots efficiency against an undefined "Capacity [MW]" axis spanning about 0.024-0.035 MW (E019-E022, E024). If that axis is Q_in, the pilot ran at roughly 24-35 kW; this is an interpretation, not a reported value.

## Reactor configuration

Pilot train (E007, Fig. 2A): biogas sulfur guards; two-stage diaphragm compressor to 10-25 barg; steam from an electric boiler and superheater; mixed feed preheated to 350-400 degC; adiabatic prereformer (Topsoe AR-401, Ni); eSMR reactor with alumina refractory lining; waste heat boiler to 100-130 degC; water cooler to <=40 degC; high-pressure separator; syngas flared. Biogas comes from an on-site 1200 m3 anaerobic digester.

Reactor dimensions, catalyst volume and catalyst mass are **not reported** (E029). No volume basis can be defined.

## Operating conditions

Biogas: 50-75 mol% CH4, 25-50% CO2, up to 2% N2 (general range for the raw gas; E010). The composition at each operating point is **not reported**. The feed is therefore mixed steam/CO2 reforming chemistry, not pure SMR. Overall envelope: 750-1000 degC catalyst exit, 3-20 barg, S/C 2.1-2.7, close to 2000 h of operation (E011). Temperature is measured with K-type thermocouples at the catalyst exit (E008).

| OP | Test | Exit T (degC) | Inlet T (degC) | p (barg) | S/C | Biogas flow | Evidence |
|---|---|---|---|---|---|---|---|
| OP001 | Start-up, steady state after ramp | 900 | 400 | 10 | 2.7 | NR | E012-E014 |
| OP002 | Stability, Table 1 Time 1 (TOS 485 h) | 950 | NR | 20 | 2.1 ± 0.1 | NR | E016 |
| OP003 | Stability, Table 1 Time 2 (TOS 1535 h) | 950 | NR | 20 | 2.1 ± 0.1 | NR | E017 |
| OP004-OP007 | Energy efficiency, four flows (Fig. 5) | 900 | 400 | 10 | 2-2.2 | 15-27 Nm3/h, individual flows NR | E018-E022 |

## Performance indicators

- **Conversion:** 97% CH4 at OP001, at thermodynamic equilibrium (E013). 94 ± 1% at both OP002 and OP003, 1050 h apart, with no sign of deactivation (E016-E017). Conversion is calculated from the carbon balance. CO2 conversion is not reported. No conversion is reported for the energy points OP004-OP007.
- **Stability and duration:** close to 2000 h total (E011); matched stability comparison over 1050 h (Table 1).
- **Dynamics:** start-up from idle to 900 degC in 2.6 h (E014); heating rates up to 330 degC/h; a 49% power cut for 900 to 750 degC (E015).
- **Scale:** CH4 feed about 5.6-15.1 mol/min for the energy points (C002, E041; from 15-27 Nm3/h biogas at 50-75% CH4, 0 degC reference assumed). Product flows are not reported.
- **Modelling (excluded from the experimental comparison):** ≥99% efficiency and 1.0 kWh/Nm3 syngas at ≥1 MW, from a one-parameter heat-loss model fitted to the four points (E025); eSMR process 3.6 kWh/Nm3 H2 versus 4.2 for fired SMR, both LHV, natural gas basis (E026).

### Energy indicators

- Fired SMR reference metrics: not applicable.
- **Power-basis metrics:** EC_CH4, SEI, EC_H2 and EY_H2 are **not reported** and cannot be calculated directly (C003, E042). Point-matched absolute power, CH4 feed, biogas composition and conversion are not reported for OP004-OP007, and the capacity axis is undefined.
- **Reviewer estimate of EC_CH4 (added 2026-11-20):** **388-485 kJ/mol CH4 converted** at the Q_in boundary (E044, C004). It is Q_reaction / eta, with Q_reaction = 308-347 kJ/mol from an equilibrium calculation at the reported conditions (E043) and the four graph-read efficiencies. The method reproduces the authors' 1.0 kWh/Nm3 syngas scale-up value. If the 15-27 Nm3/h flows are total process gas, the Fig. 5 capacity axis matches Q_in, i.e. about 23-35 kW (E045, C005). Steam generation, preheat and compression are excluded.
- **Author energy metric:** reactor energy efficiency η = Q_reaction/Q_in (E006), where Q_reaction = H_out·F_out − H_in·F_in from 25 degC formation enthalpies. It includes the reaction heat **and** sensible heating of the gas from inlet (400 degC) to exit (900 degC). Values: 72-80% in the text (E023); graph-read 71.5, 73.9, 77.4 and 79.5% (C001, E019-E022). The remainder is heat loss, mainly to the surroundings. This is a reactor thermal efficiency on an electrical input basis. It is not eta_P,LHV and not eta_HHV.
- **Whole-system eta_HHV:** not calculable. Preheater, steam generation, compressor and grid-to-PSU duties are not reported (E028), and product flows are not tabulated.
- **Energy completeness:** reactor electrical input included; external preheat to 400 degC, steam generation, compression and supply losses omitted.

## Reporting quality

| Item | Answer | Reason and evidence IDs |
|---|---|---|
| Q1 Power measurement | partly | Q_in = I·V at the PSU is defined (E005), but absolute values are not tabulated, the capacity axis is undefined and the PSU boundary wording is ambiguous (E015, E024). |
| Q2 Feed definition | partly | Flow range and S/C given (E018), but point-specific flows and biogas composition are not reported (E010). |
| Q3 Product analysis | yes | GC with TCD and FID for CO, CO2, CH4, N2, H2 (E009). |
| Q4 Balance closure | no | Carbon/mass and energy balance closure not reported (E027). |
| Q5 Temperature | partly | Catalyst-exit thermocouples with stated control deviations (E008, E015); axial or catalyst temperature profiles not reported. |
| Q6 Controls | partly | Conversion compared with thermodynamic equilibrium (E013); equilibrium values not tabulated. No non-electrified control needed for a Joule benchmark. |
| Q7 Repeatability | partly | ±1 point on Table 1 conversions and error bars on Fig. 5 (E016-E017), but error-bar basis undefined (E030). |
| Q8 Stability | yes | Matched points 1050 h apart; close to 2000 h total (E011, E016-E017). |
| Q9 Energy completeness | partly | Reactor electrical input and reaction duty defined; preheat, steam and compression duties omitted (E028). |

- **Conversion/product results: moderate confidence.** GC analysis and a matched long-duration comparison, but feed composition and balance closure are not reported.
- **Energy results: moderate confidence for the author efficiency; EC_CH4 not available.** The efficiency is measured and its definition is given in the SI, but it is graph-read, not point-matched to flows and limited to the reactor boundary.
- **Independence:** Topsoe, the technology owner, co-authored the paper; Aarhus University co-authored and hosts the plant; no competing interests declared (E002).

## Reported system information

- Boundary: eSMR reactor for efficiency (E006). The pilot train is described (E007), but its auxiliary duties are not.
- Flows and balances: biogas flow range only; no stream table; closure not reported (E018, E027).
- Energy flows: reactor efficiency only; heat loss attributed mainly to the surroundings (E023).
- Hardware: Agilent N8951A PSU; reactor size not reported. Fast dynamic response reported (E014-E015).
- Costs: not reported.

## Missing information and comparison limits

| Status | Gap | Consequence |
|---|---|---|
| not_reported | Absolute electrical power per operating point | No EC_CH4 or SEI |
| unclear | Fig. 5 "Capacity [MW]" axis and mapping of 15-27 Nm3/h to the four points | Efficiency cannot be tied to a specific flow |
| not_reported | Biogas composition per operating point; Nm3 reference | CH4 feed only as a range (C002) |
| not_reported | Product flows and composition; CO2 conversion | No H2 yield, EC_H2 or EY_H2 |
| not_reported | Mass and energy balance closure | Q4 "no" |
| not_reported | Preheat, steam, compression and PSU-loss duties | eta_HHV not calculable |
| not_reported | Reactor and catalyst volume | No power density or volume comparison |
| not_applicable | Plasma characteristics | Joule-heated source |

Comparison limits:
- The feed contains CO2 (biogas), so this is mixed reforming; compare with pure SMR only with that label.
- The author efficiency includes sensible heating of the gas from 400 to 900 degC, so it is not directly comparable with plasma power-basis metrics.
- The conversion points (OP001-OP003) and efficiency points (OP004-OP007) are different tests at different pressures and S/C. Do not combine 97% or 94% conversion with the 72-80% efficiency.
- Modelled values (99%, 1.0 kWh/Nm3, 3.6 kWh/Nm3 H2) are extrapolations and excluded from the experimental comparison.

## Calculations

All in [calculations.py](calculations.py).

- **SRC005-C001, graph reading of Fig. 5.** Inputs E019-E022. Page rendered at 300 dpi; axes calibrated on the log capacity axis (0.01 and 0.1 MW) and linear efficiency axis (40 and 100%). Results: OP004 71.5% at 0.0235 MW; OP005 73.9% at 0.0268 MW; OP006 77.4% at 0.0309 MW; OP007 79.5% at 0.0348 MW. Approximate; consistent with the stated 72-80% (E023).
- **SRC005-C002, CH4 feed range.** Inputs E010, E018. CH4 = biogas flow × (0.50-0.75) / 22.414 Nm3/kmol. Results: 5.6-8.4 mol/min at 15 Nm3/h; 10.0-15.1 mol/min at 27 Nm3/h. Assumes a 0 degC, 1 atm normal reference; the range reflects unknown composition. Reviewer interpretation: the lowest flow is assumed to match the lowest-capacity point.
- **SRC005-C003, EC_CH4.** Not calculated directly: point-matched Q_in, CH4 feed, composition and conversion are not reported (E042). See C004 for a range estimate.
- **SRC005-C004, EC_CH4 estimate (2026-11-20).** Inputs E006, E007, E010, E013, E018, E019-E022. Q_reaction per mol CH4 converted from Cantera (GRI-Mech 3.0) equilibrium at 900 degC and 10 barg, inlet 400 degC, using the authors' definition (25 degC reference). Spanned: CH4 50-75% (rest CO2), S/C 2.0-2.2 (steam per hydrocarbon carbon), inlet unreacted or equilibrated at 400 degC. Results: X_CH4 0.94-0.97; Q_reaction 308-347 kJ/mol; EC_CH4 = Q_reaction/eta = 431-485 (OP004), 417-470 (OP005), 398-448 (OP006), 388-437 (OP007) kJ/mol. Check: the authors' scale-up case (920 degC, 30 barg, S/C 1.8, eta 0.99) gives 0.99 kWh/Nm3 syngas against their 1.0. Assumes the energy points were at equilibrium, as reported for OP001.
- **SRC005-C005, capacity axis check (2026-11-20).** Inputs E018, E043, C001. Implied Q_in = F_CH4 x X x Q_reaction / eta. Reading the flows as total process gas (biogas + steam) gives 21-23 kW at 15 Nm3/h and 34-38 kW at 27 Nm3/h, against axis values of 23.5 and 34.8 kW. Reading them as biogas gives 43-96 kW, which is inconsistent. Interpretation: the axis is probably Q_in and the flows probably include steam; if so, C002/E041 overstate the CH4 feed by about 2.2-2.5x.

## Review and revisions

- 2026-11-04: initial extraction (Claude, AI). Human verification pending, especially the Fig. 5 graph reading and the Q_in boundary.

## Plasma characteristics

Not applicable (Joule-heated source).
