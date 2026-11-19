# Source extraction: SRC021

## Source and review

- Source ID / citation / DOI: SRC021. Bryssinck, R., Smith, G.J., O'Modhrain, C., Van Assche, T., Trenchev, G., Bogaerts, A. (2025). Performance of a gliding arc plasmatron pilot reactor with an integrated carbon bed and recirculation for upscaled CO2 conversion. React. Chem. Eng. 10, 1910-1923. https://doi.org/10.1039/D5RE00190K
- Source filenames and document versions: manuscript.pdf, **accepted author version** (University of Antwerp IRUA, 32 pp., line-numbered; PDF p. 1 is the repository cover, printed page = PDF - 1), SHA-256 `e77e09c9b846b887bd2bd6e4f5c09da60645cc669e4c33e7086060707322437e`; ESI.pdf (published supplementary information, model details), SHA-256 `af298f14bd33b805c504dabf1529dc1ef2cd53e919c30b5f46babab9b168b078`. Typeset version not obtained; page references are to the author version.
- Retrieval date: 2026-11-11 (downloaded by BB).
- Protocol version: workflow.md 0.7, with the CO2-splitting metrics of [../../literature_review_objectives.md](../../literature_review_objectives.md).
- Extractor / date: Claude (AI), 2026-11-12.
- Coverage: experimental sections, Figs. 5-12 (Figs. 5, 6, 12 read from rendered pages); the 2D post-plasma model (Section 3, 4.5, ESI) recorded only as the authors' interpretation.
- Reviewer / date / checks: Claude (AI), 2026-11-12; EC, CR and O/C balances recalculated (C001-C006).
- Review status: ai_checked. Human verification pending (E042 changes the benchmark comparison).

## Electricity supply

- Seven ~1 kW switching-type HV DC supplies, one per node (same type as SRC020) (E003).
- **Power boundary: plug**, "the total power of the system", in a 10 ft container with PSUs, heat pump/chiller and PLC; the recycle compressor adds ~1 kW (E006, E013). Which auxiliaries are metered is not stated.
- Plasma power "generally 60-80%" of plug (E006); the authors' plasma-based EC (4.8 vs 5.8 MWh/t) implies 0.83 (C005).
- Plasma scale: 7.6-9.5 kW plug. No external heat; bed heated by the plasma effluent (1300-1400 K).

## Reactor configuration

- Multi-reactor gliding arc plasmatron pilot (D-CRBN): seven reverse-vortex GAP nodes on one anode plate; water-jacketed post-plasma chamber 170 mm x 470 mm; carbon bed 136 mm x 27 mm at 35 mm (position 1) or 65 mm (position 2) from the anode plate; silo with screw feeder; recirculation loop with pump (E002).
- Carbon: 50 g activated carbon NORIT PK 3-5 mm per run (E004).

## Operating conditions

CO2 99.7%, 50-110 L/min; Vm 24.06 L/mol (E004, E007). Runs of ~200-560 s (E018). Triplicates except the semi-continuous run (E005, E014).

| OP | Configuration | Q (L/min) | P plug (kW) | Evidence |
|---|---|---|---|---|
| OP001 | no bed (benchmark) | 70 | 8.5 | E009, E011 |
| OP002 | bed position 1 | 70 | 8.5 | E008, E011 |
| OP003 | bed position 1, semi-continuous feed (best) | 50 | 8.1 | E014 |
| OP004 | bed position 1 + 50% recycle (fresh 25 L/min) | 50 total | 9.5 | E013 |

## Performance indicators

- **Power boundary:** plug.
- **External heat:** no. **Carbon is a co-reactant** (not counted by the authors).
- Product: CO2/CO with O2 below 1% when the bed is present (E013); benchmark O2 not reported.

| OP | X_CO2 (%) | CO (vol%) | EC reported (MWh/t CO) | EC_CO plug (kWh/Nm3) | Carbon (kg/Nm3 CO) | CO per CO2 converted (C001) |
|---|---|---|---|---|---|---|
| OP001 | ~6.4 (Fig. 6) [see E042] | 12 (max) | ~13.5 | ~16.9 | NR | 2.01 (impossible without carbon) |
| OP002 | ~16 | 27 (max) | 5.6 | ~7.0 | ~0.27 | 1.99 |
| OP003 | 20 (18-20) | 33 (peak) | 5.8 (5.8-6.1) | 7.33 | 0.27 | 2.00 |
| OP004 | 12.7 (total inlet) | 23 | 13.7 | ~17.1 | NR | 1.56 |

kWh/Nm3 = MWh/t x 1.25 (1 t CO = 800 Nm3). OP003 details (C003, C004): per mol CO2 fed, 0.198 mol C consumed and 0.395 mol CO formed; ~296 g C/h; EC_CO 592 kJ/mol (plug); eta_LHV with the carbon counted as an energy input 35.9% at the plug (41.1% at 0.83 plug-to-plasma) vs 23.9% as 283 x X / SEI.

- **Author's metric:** EC per tonne of CO in the outlet on plug power (E007). CO from the carbon is counted as product; the carbon is not counted as an input.
- **Net reaction with the bed is CO2 + C -> 2CO** (E041): the reported EC values at 70 and 50 L/min correspond exactly to two CO per CO2 converted. At 90 and 110 L/min (1.70, 1.41) and with recycle (1.56) the ratio is lower, i.e. less carbon reacted or some O left the bed as O2/CO2.
- **Benchmark inconsistency (E042):** without carbon, 12% CO requires ~12.8% conversion (with ~6% O2); the reported 6.4% is what the O balance gives with O2 = 0, and the reported 13.5 MWh/t also needs CO = 2X. Either the benchmark conversion is understated by about half, or an unreported oxygen sink was present. The headline "more than two-fold, from ca. 6% ... to 20%" (p. 28) depends on this; on the CO measurement the gain is ~13% -> 16-20%.
- Bed position matters: 35 mm (1400 K) doubles conversion relative to 65 mm (1200 K); closer was not possible because the carbon destabilised the arcs (E008).
- Higher flow lowers bed temperature, conversion and CO; EC rises (E012).
- Recirculation (50%) raised conversion of the total inlet (10 -> 13%) but lowered CO output (0.464 -> 0.413 mol/min) and raised EC (10.9 -> 13.7 MWh/t), partly from the ~1 kW compressor (E013, E044).
- Semi-continuous feeding held conversion at 18-20% over three 3-min cycles; fresh cold carbon temporarily cools the bed (1400 -> 1300 K) and lowers CO (E014).
- Duration: runs of minutes; no long-term data (E018).

## Reporting quality

| Item | Answer | Reason and evidence IDs |
|---|---|---|
| Q1 Power measurement | partly | Plug power stated per point; meter and metered auxiliaries not described (E006). |
| Q2 Feed definition | yes | Purity, flow and Vm stated (E004, E007). |
| Q3 Product analysis | partly | NDIR CO2 and CO, optical O2; O-balance method; calibration not described; O2 values not reported (E005). |
| Q4 Balance closure | no | No C or O balance reported; reviewer balance shows a benchmark inconsistency (E042). |
| Q5 Temperature | yes | Thermocouples in the bed and downstream, positions stated (E008). |
| Q6 Controls | partly | No-bed benchmark, but internally inconsistent (E042). |
| Q7 Repeatability | partly | Triplicates for most tests; best point from a single run (E014). |
| Q8 Stability | partly | Time traces of minutes; semi-continuous run ~9 min; no long-term test (E018). |
| Q9 Energy completeness | partly | Plug power incl. recycle compressor; carbon chemical energy not counted; auxiliaries unclear (E006, E007). |

- Confidence in conversion/product results: moderate with the bed (consistent with the CO measurement and CO2 + C stoichiometry); lower for the benchmark (E042).
- Confidence in energy results: moderate. Plug basis and reproducible EC arithmetic, but carbon uncounted and metered scope unclear.

## Gaps and comparison limits

- Carbon consumption (~0.27 kg/Nm3 CO; ~300 g/h at the best point) must be added to any comparison, with its cost and origin.
- Benchmark conversion likely misreported (E042); human check advised.
- Accepted author version only; page numbers differ from the journal.
- Run times of minutes; carbon bed deactivation over longer times not tested here (cf. SRC019).

## Calculations

All in outputs/calculations.py. Vm 24.06 L/mol; 1 t CO = 35,701 mol = 800 Nm3.

- SRC021-C001 CO output implied by reported EC and power; ratio to converted CO2; EC if CO = X or 2X. Inputs E008, E011-E014. Result E041.
- SRC021-C002 Benchmark: conversion from CO 12% with O2 6% vs 0. Input E009. Result E042.
- SRC021-C003 Best point O/C balance (CO 33%, O2 0-1%). Input E014. Result E043.
- SRC021-C004 EC_CO, carbon per CO, carbon rate, eta_LHV = LHV of CO out / (electricity + LHV of carbon consumed), LHV_CO 283.0, LHV_C 393.5 kJ/mol (plug and plasma basis). Result E043.
- SRC021-C005 Plug-to-plasma ratio implied by the authors' 4.8 vs 5.8 MWh/t. Input E015.
- SRC021-C006 CO output before and with recycle. Input E013. Result E044.

## Revisions

- 2026-11-19: C004 changed from the efficiency on the overall reaction enthalpy (14.6% at the plug, carbon treated as free) to eta_LHV with carbon counted as an energy input (workflow 1.1, section 4). E043 and the OP003 note updated; evidence IDs kept.

## Plasma characteristics

- Regime: warm gliding arc plasmatron, ~1 kW per node (E003).
- Gas temperature: bed 940 K (empty), 1200-1400 K (with carbon), downstream 500-860 K (thermocouples) (E008); ~6000 K at the node outlets from the model only (E017).
- Other diagnostics: none.
