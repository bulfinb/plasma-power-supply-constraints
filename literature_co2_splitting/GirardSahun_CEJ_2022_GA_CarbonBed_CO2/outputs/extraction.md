# Source extraction: SRC019

## Source and review

- Source ID / citation / DOI: SRC019. Girard-Sahun, F., Biondo, O., Trenchev, G., van Rooij, G., Bogaerts, A. (2022). Carbon bed post-plasma to enhance the CO2 conversion and remove O2 from the product stream. Chem. Eng. J. 442, 136268. https://doi.org/10.1016/j.cej.2022.136268
- Source filenames and document versions: manuscript.pdf, published version, SHA-256 `a40b795fc3d6969065327d7db150d6d3b010f42ad08f06338f041e9d229356d6`; ESI.pdf (9 pp.), SHA-256 `b9ae0df7447f1f822e5e2a0aad7c18736cc33a86a19184401666f263a2b9afeb`; ESI.docx (same content), SHA-256 `cbf96e65b8ce77115e69396cef3688e794bb2bd6954cdc628e48eef5c9210a44`. Printed page = PDF page.
- Retrieval date: 2026-11-11 (downloaded by BB).
- Protocol version: workflow.md 0.7, with the CO2-splitting metrics of [../../literature_review_objectives.md](../../literature_review_objectives.md).
- Extractor / date: Claude (AI), 2026-11-12.
- Coverage: full manuscript and ESI; Figs. 3-7 read from rendered pages. The 0D carbon-gasification model (validated on literature data, Section 3, 4.6) is recorded only as the authors' explanation, not as evidence.
- Reviewer / date / checks: Claude (AI), 2026-11-12; O and C balances and efficiency recalculated (C001-C005).
- Review status: ai_checked; partial human check by BB, 2026-11-25: OP002 peak (E012) and OP003 at 14 min (E014) confirmed; CO 7.3% kept (the Fig. 5 CO2 curve does not close with CO + O2; noted in E014) (human_checks/summary.csv). Other records, including C004: no human check.

## Electricity supply

- AC current-source power supply (AFS). Plasma power from V x I (HV probe, 2 ohm current sense resistor, oscilloscope) (E002). Supply efficiency not reported.
- Plasma scale: 0.533 kW (from SEI 3.2 kJ/L x 10 L/min, C001). No external heat; the carbon bed is heated by the plasma afterglow and by carbon oxidation (E015).
- Electrode wear "very limited" (E003).

## Reactor configuration

- Gliding arc plasmatron (reverse vortex, Nunnally design); outlet 26 mm long, ID 7.07 mm (E004).
- Carbon bed: basket of ~5 g activated charcoal directly at the anode exit (0-60 mm), fed by a ~200 cm3 silo; stainless mesh between arc and bed; thermocouples at 15 and 35 mm (E004).
- Control: dummy bed of ceramic beads (E017).

## Operating conditions

Pure CO2 (99.995%), 10 Ln/min, atmospheric pressure (E005); SEI ~3.2 kJ/L in all cases (E010). 14 min runs, triplicates (E006).

| OP | Configuration | Time point | Evidence |
|---|---|---|---|
| OP001 | GAP, no bed (benchmark) | steady (1-14 min) | E011 |
| OP002 | GAP + charcoal 1 bed | maximum, first ~1 min | E012, E013 |
| OP003 | GAP + charcoal 1 bed | ~14 min (deactivated) | E013, E014 |

## Performance indicators

- **Power boundary:** plasma power (V x I at the electrodes).
- **External heat:** no; but **solid carbon is a co-reactant** whose chemical energy is not counted by the authors (E008).
- Product: OP001 CO2/CO/O2 (O2 3.7%); OP002-OP003 CO2/CO with O2 at 0.2-0.8%.

| OP | X_CO2 (%) | CO (%) | O2 (%) | eta reported (%) | eta_LHV, carbon counted (%) | EC_CO, plasma (kWh/Nm3) | Carbon (kg/Nm3 CO) |
|---|---|---|---|---|---|---|---|
| OP001 | 7.6 | 7.2 | 3.7 | 27.9 | 27.0 (29.5) | 13.0 (11.9) | 0 |
| OP002 | 12.6 | 21.9 | 0.2 | 45.4 | 55.3 (58.4) | 3.95 (3.6) | 0.26 |
| OP003 | ~4.6-4.7 | ~7.3 | ~0.75 | NR | 23.8 (25.7) | 12.8 (11.7) | 0.21 |

Values from C001-C005 at Vm 24.5 L/mol (authors) with 22.414 L/mol in brackets.

- **Author's efficiency** (E008): eta = 283 kJ/mol x X_CO2 / SEI, i.e. counted as pure CO2 splitting even with the carbon bed; the authors note that "this must however be kept in mind".
- **Reviewer finding (C003, C004):** at the maximum, the O and C balances give 0.121 mol C consumed and 0.246 mol CO formed per mol CO2 fed, i.e. net CO2 + C -> 2 CO; net, the bed carbon equals half the CO formed (a balance result, not the atom origin: bed carbon may partly leave as CO2). The authors' 45.4% credits 283 kJ/mol per CO2 converted and does not count the carbon. With the carbon counted as an energy input, eta_LHV = LHV of CO out / (plasma power + LHV of carbon consumed) = 55% at the maximum, against 27% without the bed: the bed converts carbon into CO efficiently, using plasma heat for the Boudouard reaction, but half the product comes from a solid feedstock (0.26 kg C per Nm3 CO).
- **Transient:** the reported values are the maximum in the first ~1 min. Conversion falls to the benchmark at ~3.5 min and to ~4.7% at 14 min (below the benchmark) as the carbon surface saturates with oxygen; the silo does not restore it (E013, E016). At 14 min, eta_LHV is ~24% (carbon counted), below the no-bed 27%; the Fig. 5B balance (4.6%) now agrees with Fig. 6 (4.7%).
- **What persists:** O2 removal. O2 stays below 0.8% for the 14 min run (vs 3.7% without the bed) (E014). CO per unit plasma energy does not: at 14 min it is back to the no-bed level (12.8 vs 13.0 kWh/Nm3) while still consuming 0.21 kg carbon per Nm3 CO.
- Temperatures: carbon bed peaks ~1700 K then ~1200 K; without bed ~850 K at 15 mm (E015).
- Authors' outlook: extra heating (e.g. gas burner) or a thermal plasma to limit oxygen coverage, at extra energy cost; recycle of O2-free CO2/CO lowers overall efficiency (E016, E018).
- Duration: 14 min runs; benchmark steady within 1 min; carbon bed not steady (E013).

## Reporting quality

| Item | Answer | Reason and evidence IDs |
|---|---|---|
| Q1 Power measurement | yes | V x I with HV probe and current sense resistor (E002). |
| Q2 Feed definition | partly | Pure CO2 at 10 Ln/min; SEI converted with 24.5 L/mol, so the molar basis is ambiguous (E005, E009). |
| Q3 Product analysis | yes | NDIR, O2 sensor and calibrated GC, cross-checked; expansion-corrected via O balance (Eq. 5 printed with a probable typo) (E006, E007). |
| Q4 Balance closure | partly | O balance used to derive outlet flow; C balance (carbon consumed) not reported (E042). |
| Q5 Temperature | yes | Thermocouples in the effluent and bed, positions stated (E015). |
| Q6 Controls | yes | No-bed benchmark and inert dummy bed (E011, E017). |
| Q7 Repeatability | yes | Triplicates with error bars (E006, E011, E012). |
| Q8 Stability | yes | Time-resolved 14 min data reported, showing the decay (E013). |
| Q9 Energy completeness | no | Carbon consumed (chemical energy) not counted; no supply efficiency (E008). |

- Confidence in conversion/product results: higher. Multiple calibrated analysers, expansion correction, triplicates and time-resolved data.
- Confidence in energy results: lower as reported (efficiency on the wrong reaction enthalpy, transient peak); moderate for the recalculated values (E043, E044).

## Gaps and comparison limits

- The headline 45.4% (and 12.6%, 25.4 kJ/L) is a transient maximum on a pure-splitting enthalpy; it should not be compared with steady CO2-splitting results. Osorio-Tejada et al. 2024 (RV005) base a 100 t CO/day plant TEA on this point (RV005, Table 1).
- Carbon is a feedstock: any comparison must include its supply (0.21-0.26 kg/Nm3 CO), its cost and its CO2 origin. "Half the CO from carbon" is a net balance; the bed carbon may partly leave as CO2.
- SEI molar basis: 24.5 L/mol applied to Ln/min flows (E009).
- Carbon balance and carbon consumption rate not reported; reviewer values only.

## Calculations

All in outputs/calculations.py. Formation enthalpies (298 K): CO2 -393.5, CO -110.5 kJ/mol.

- SRC019-C001 Plasma power and SEI at both molar volumes. Inputs E005, E010. Result E041.
- SRC019-C002 Outlet flow and conversion from the O balance (2[O2]), compared with Eq. 5 as printed. Inputs E011, E012, E014. Result E042.
- SRC019-C003 Carbon consumed and CO formed per mol CO2 fed. Result E042.
- SRC019-C004 eta_LHV = LHV of CO out / (plasma power + LHV of carbon consumed), LHV_CO 283.0, LHV_C 393.5 kJ/mol; compared with the authors' 283 x X / SEI. Result E043.
- SRC019-C005 Electricity per mol CO (plasma power) and carbon per Nm3 CO. Result E044.

## Revisions

- 2026-11-19: C004 changed from the efficiency on the overall reaction enthalpy (28% at the maximum, carbon treated as free) to eta_LHV with carbon counted as an energy input (workflow 1.1, section 4). E043, the performance table and the finding text updated; evidence IDs kept.
- 2026-11-19, after GPT cross-check (cross_check_log.md XC005, XC007): net-carbon wording clarified; 14 min Fig. 5B reading corrected (CO ~7.3%, O2 ~0.75%; was ~9.7% and ~0.5%, read near 8 min). OP003 X 4.6%, EC_CO 12.8 kWh/Nm3, carbon 0.21 kg/Nm3 CO, eta_LHV 23.8%; "what persists" text revised. Evidence IDs kept.

## Plasma characteristics

- Regime: warm gliding arc plasmatron; arc ~3000 K from modelling (ref. 44, not measured); arc partly extends through the anode into the bed (mesh melted in one run) (E015).
- Gas temperature: thermocouples, ~850 K at 15 mm without bed; up to 1300 K at 4 mm with the earlier APS supply (E015).
- Other diagnostics: BET, SEM and TGA-MS of the charcoal (Table 5, ESI).
