# Cross-check against an independent GPT extraction

Each paper was extracted a second time, in full and blind, by a second AI (OpenAI GPT-6.1 Sol in the Codex desktop app), in a separate local folder that is not published. It followed the same workflow.md (version per paper below) and _source_template.md. It had:

- the source documents, with SHA-256 hashes listed in a sources file;
- the objectives;
- SRC024 (Van Laer) as the only worked example.

It did not have our extractions or short summaries, the search and selection files, the synthesis, or this log. It produced its own extraction.md, evidence.csv, calculations.py and short_summary.txt for each paper.

## Independent extractions

| Source | Date | Tool | Model | Workflow | Notes |
|---|---|---|---|---|---|
| SRC018 Bongers 2017 | 2026-11-19 | Codex desktop (version not recorded) | GPT-6.1 Sol (confirmed by BB; not logged by the tool) | 1.0 (1.1 change not relevant: no carbon) | manuscript only (no ESI) |
| SRC021 Bryssinck 2025 | 2026-11-19 | Codex desktop (version not recorded) | as above | 1.1 (solid-carbon rule given during the extraction) | manuscript and ESI |
| SRC019 Girard-Sahun 2022 | 2026-11-19 | Codex desktop (version not recorded) | as above | 1.1 (text-vs-figure rule of 1.2 not yet given) | manuscript and PDF ESI |
| SRC017 Hecimovic 2023 | 2026-11-19 | Codex desktop (version not recorded) | as above | 1.2 | manuscript and ESI; length guidance given (shorter outputs) |
| SRC026 Hecimovic 2024 | 2026-11-20 | Codex desktop (version not recorded) | as above | 1.2 | manuscript; benchmark (R1-R4) |
| SRC016 Kiefer 2024 | 2026-11-20 | Codex desktop (version not recorded) | as above | 1.2 | manuscript (durability supplement not held by either) |
| SRC025 Kungas 2020 | 2026-11-20 | Codex desktop (version not recorded) | as above | 1.2 | manuscript; benchmark (R1-R4) |
| SRC020 O'Modhrain 2024 | 2026-11-20 | Codex desktop (version not recorded) | as above | 1.2 | manuscript and ESI |
| SRC022 Renninger 2022 | 2026-11-20 | Codex desktop (version not recorded) | as above | 1.2 | manuscript |
| SRC023 Yong 2023 | 2026-11-20 | Codex desktop (version not recorded) | as above | 1.2 | manuscript (supplement not held by either) |
| SRC024 Van Laer 2015 | 2026-11-20 | Codex desktop (version not recorded), new session | as above | 1.2 | manuscript. Not strictly blind: our extraction was the worked example in earlier GPT sessions; deleted before this fresh session |

Each paper gets a one-line summary of what agreed, then one row per difference that matters. Every difference is checked against the PDF. Action: **corrected** (our extraction revised; see processing_log.md and the Revisions section of its extraction.md), **kept ours**, **workflow rule** (workflow.md changed), or **for human check** (not settled by the PDF). These checks are AI-to-AI. They do not change a source's status (ai_checked) and are not logged in ../human_checks/.

## Summary by paper

- **SRC018 Bongers 2017** (2026-11-19): same five operating points; OP001-OP002 values identical (X 83% and 47%; 14.8 and 10.0 kWh/Nm3 CO); OP005 within reading precision. Differences XC001-XC003.
- **SRC021 Bryssinck 2025** (2026-11-19): best point agrees (X 20%, EC_CO 7.33 vs 7.25 kWh/Nm3, carbon 0.268 kg/Nm3 CO in both, eta_LHV 35.9 vs 36.2%). Both found independently that the empty-reactor control is inconsistent (6.4% conversion and 13.5 MWh/t imply 2 CO per CO2 converted) and that recycle lowers CO output. Difference XC004.
- **SRC019 Girard-Sahun 2022** (2026-11-19): no-bed and peak points agree (X 7.6% and 12.6%; EC_CO 13.0 and 3.95 kWh/Nm3; carbon 0.263 kg/Nm3 CO; eta_LHV 27.0% and 55.3% in both). Differences XC005-XC007.
- **SRC017 Hecimovic 2023** (2026-11-20): the 55% headline point is identical (2.7 kW, 5 ls/min, SEI 779 kJ/mol, 17.6 kWh/Nm3 CO). Both found independently that the reported efficiencies are ~9-10% above X x 2.9 / SEI on the stated 20 degC flow basis, and that the 57% maximum pairs with ~16.5% efficiency (Figs. 8-9), not the ~20% in the conclusion. Difference XC008.
- **SRC026 Hecimovic 2024** (2026-11-20): both found independently that the FZJ SOEC figure is 69.6 kW / 17.5 Nm3/h = 3.98 kWh/Nm3 (4.19 with the 0.95 rectifier), not the reported 3.89, and that the vendor 6-8 kWh/Nm3 implies 44-58%, not 90%. Cooled-channel plasma at 19.8 kWh/Nm3 (total) and membrane reactor at 35 kWh/Nm3 agree. Difference XC009.
- **SRC016 Kiefer 2024** (2026-11-20): same four operating points (OP001/OP002 numbered the other way round). All headline values agree within figure-reading precision: wall-plug energy 19.6 kWh/Nm3 CO (17.9%) at both 9.3 slm points, wall power ~3760 W (no pump) and ~4220 W (with pump), 56.6% conversion at ~33 kWh/Nm3 (wall eta ~10.5-10.7%), durability 29 h 20 min in four blocks at ~27% and ~20 kWh/Nm3. No differences needing action; GPT rates figure-read energy points moderate rather than higher, and writes external heat as NR rather than no.
- **SRC025 Kungas 2020** (2026-11-20): same three stack cases with identical values (2.5 kWh/Nm3 at 200 mA/cm2, EE 91%; 2.96 -> 3.06 over 2000 h; ~3.3 -> ~3.6 over 7600 h), all stack DC with heat, rectifier and utilisation not reported. Both flag the Table I voltage (1.1 V) vs text (1.13 V) mismatch and the author's Topsoe employment. Difference XC010.
- **SRC020 O'Modhrain 2024** (2026-11-20): headline point identical (five active arcs, 80 L/min, 7.1 kW plug, X 8.7%, SEI 126 kJ/mol = 1.30 eV, 17.9 kWh/Nm3 CO, ~20% plug efficiency). Both note that the reported ~777-779 g/h is CO2 converted (not CO), that gas flows through all five nodes even with one active arc, and that the plug boundary includes supply losses (PSU ~80%). GPT also notes that the abstract's "1 eV" for 5.3 kJ/L is ~1.3 eV at the stated flow reference; our tables already use 1.30 eV. Difference XC011.
- **SRC022 Renninger 2022** (2026-11-20): headline agrees (1.25 SLM, ~262-265 W driver input, ~160-165 W plasma, eta 45% plasma / 28% system, 12.5-12.8 kWh/Nm3 CO at driver input, 7.8-7.9 on plasma power). Both note that the "system" boundary is the DC input to the driver, not the wall, and the bed/flow controls (7.5% without bed, 10.5% upflow). Differences XC012-XC013.
- **SRC023 Yong 2023** (2026-11-20): both headline points identical (5.8 bar, 700 uJ, 21 W deposited, 420 s: 14% / 23%, 15.1 kWh/Nm3 CO; 5 bar, 800 uJ, ~120 s: ~3.3% / ~27%, ~13). Both flag the unstated chamber volume per data set (200 vs 400 mL) and that the text's 27% / 4% / 865 uJ / 420 s does not reconstruct. GPT adds a 12.2 bar point (~2.3% / ~17%), consistent with ours. Difference XC014.
- **SRC024 Van Laer 2015** (2026-11-20): same three packed-bed points with identical author values and energy per CO (42.0% / 4.7%, 74 kWh/Nm3; 37.8% / 6.4%, 54; 10.0% / 9.6%, 36; plasma basis). Both find that the 60-80 W "applied power" is not the plasma power and back out ~20-37 W; the spread is only the assumed molar volume (ours shows 24.5 and 22.414 L/mol in C001, GPT 22.414). Difference XC015.

## Differences

| ID | Date | Source / record | Ours | GPT | Checked against PDF | Action |
|---|---|---|---|---|---|---|
| XC001 | 2026-11-19 | SRC018 OP005 power | ~1 kW | NR | GPT right: 1 kW and 14 slm belong to Exps. 1-2, not Exp. 7 | corrected |
| XC002 | 2026-11-19 | SRC018 gas temperature 5700 K | conditions from the Fig. 4 caption (5 kW, 75 slm), assigned to OP001-OP004 | caption and text conflict flagged; not assigned | GPT right: the text says the Fig. 2d setup (3.1 kW, 0.6 eV); the caption says 0.9 eV | corrected (conflict noted; not assigned to any OP) |
| XC003 | 2026-11-19 | SRC018 OP003-OP004 (75 slm) | Fig. 3b values (X ~10%, ~22.5%; eta ~36% at 10 kW) | text values (X 11%, 23%; eta 40%) | both defensible; the figure agrees with the paper's own X x 2.9 / SEI | kept ours; workflow rule (text vs figure) |
| XC004 | 2026-11-19 | SRC021 operating points | 4 OPs | 8 OPs, adding the 65 mm bed, 110 L/min, recycle off and 540 s; eta_LHV ~22-23% at 65 mm and 110 L/min | values consistent with our C001 | kept ours (noted: the carbon-bed benefit depends on bed temperature) |
| XC005 | 2026-11-19 | SRC019 OP003 (bed, 14 min): Fig. 5B reading | CO ~9.7%, O2 ~0.5% (X 5.6%, EC_CO 9.5, eta_LHV 30%) | CO ~7.2%, O2 ~0.75% (X 4.6%, EC_CO 12.9, eta_LHV 23.7%) | GPT right: at 14 min CO is ~7.3% (Figs. 5B and 5C); ours was read near 8 min. Corrected balance now agrees with Fig. 6 (4.7%) | corrected (extraction, summary, synthesis, figures): at 14 min the bed is back to the no-bed energy per CO and below it on eta_LHV |
| XC006 | 2026-11-19 | SRC019 operating points | no-bed, charcoal 1 peak, 14 min | adds charcoal 2 peak (X 11.3%, author eta 40.4%, eta_LHV 51.5%) | consistent with the paper | kept ours (noted) |
| XC007 | 2026-11-19 | SRC019 "half the CO comes from the carbon" | stated as fact | net CO-equivalent only; bed carbon may partly leave as CO2 | GPT right: the O/C balance gives the net amount, not the atom origin | corrected (wording) |
| XC008 | 2026-11-20 | SRC017 operating points | 1 bar no pump at ~2.7 kW (X ~34.5%), SEI 10.1 eV (X ~56.5%), SEI ~1.2 eV | standard torch 1.5 kW (X ~13.5%), wide inlets ~2.85 kW (X ~35.5%), 1 bar no pump at 1.5 kW (X ~20%) | different points from the same figures; headline point identical; synthesis uses only the headline | kept ours (noted) |
| XC009 | 2026-11-20 | SRC026 FZJ SOEC design calculation | included as OP001 (labelled design calculation; 3.98-4.19 kWh/Nm3 at 86% utilisation) | kept outside the summary tables as a design calculation, not experimental | same numbers; a choice of presentation | kept ours: it is the SOEC system benchmark, labelled as calculated |
| XC010 | 2026-11-20 | SRC025 OP002 degradation rate | 2.2 %V/1000 h as reported | flags that 1.24 -> 1.28 V (or 2.96 -> 3.06 kWh/Nm3) over 2000 h gives ~1.6-1.7 %/1000 h, not 2.2 | the voltages are rounded to 0.01 V, which can account for up to ~2.0 %/1000 h; not settled by the PDF | kept ours as reported; not used in any headline |
| XC011 | 2026-11-20 | SRC020 supporting operating points | 3 active nodes at 60 L/min; 1 central node at 80 L/min (flow-matched to the headline; X ~2.1%, 15.5 kWh/Nm3) | 1 central node at 50 L/min (the paper's single-node optimum, 24%; 15.1 kWh/Nm3); 5 nodes at 30 L/min (X 1.6%) | different points from Figs. 3-4, both consistent with the paper | kept ours (noted: single-node optimum is 24% at 50 L/min) |
| XC012 | 2026-11-20 | SRC022 Fig. 4 conversion readings | 27.4% at ~262 W (conclusion text); 27.8% at ~300 W | ~28.2% at ~265 W and ~28.8% at ~303 W (figure) | figure re-read at 300 dpi: GPT's readings are right; at ~265 W the text gives 27.4%, so text kept (rule 1.2); at ~300 W ours was misread | corrected (300 W reading); kept ours for the headline (2% effect on EC_CO) |
| XC013 | 2026-11-20 | SRC022 driver efficiency at ~216 W | not flagged | Fig. 4 eta_system/eta_plasma ~25/46 implies ~54%, outside the stated 61-65% | GPT right | corrected (added to Gaps) |
| XC014 | 2026-11-20 | SRC023 balance closure and conversion confidence | C and O closed; Q4 yes; conversion confidence higher | carbon balance assumed (Phi = CO/(CO+CO2)); electrode carbon deposits unquantified; moderate | GPT right: the paper confirms only N_CO ~ 2 N_O2, and reports carbon deposition | corrected (Q4 partly, conversion confidence moderate; no values change) |
| XC015 | 2026-11-20 | SRC024 gas-expansion correction | conversion likely not expansion-corrected; corrected values estimated (e.g. 37.8% -> 28.8%) | correction method unclear; reported values kept, no estimate | both flag it; ours adds a conditional estimate | kept ours |

## Closing summary (CO2 splitting, 2026-11-20)

- **Papers:** all 11 sources were extracted a second time by GPT-6.1 Sol (Codex). Ten were blind; Van Laer only partly, as it had been the worked example.
- **Differences logged:** XC001-XC015.
- **Corrections to our extractions:** seven, in four papers.
  - Bongers: XC001 (2.45 GHz power) and XC002 (gas temperature conditions).
  - Girard-Sahun: XC005 (14 min figure reading) and XC007 (net-carbon wording).
  - Renninger: XC012 (a figure reading) and XC013 (a driver-efficiency inconsistency).
  - Yong: XC014 (balance closure and confidence).
- **Conclusion changed by a correction:** one, XC005. At 14 min the carbon bed is back to the no-bed energy per CO, and below it on eta_LHV.
- **No headline energy or conversion values changed**, apart from that late-time point.
- **Workflow change:** one, the text-vs-figure rule (XC003, workflow 1.2).
- **Kept ours:** the other differences were either different but valid operating-point choices (XC004, XC006, XC008, XC009, XC011) or judgement calls (XC003, XC010, XC015).
- **Critical findings that both extractions reached independently:**
  - Bryssinck's no-bed control is inconsistent.
  - Hecimovic 2023's reported efficiencies are ~9-10% above the recalculation.
  - Hecimovic 2024's SOEC figure is 3.98, not 3.89 kWh/Nm3, and the vendor's 90% does not match 6-8 kWh/Nm3.
  - Kungas' Table I voltage disagrees with the text.
  - Yong's chamber volume is undefined.
  - Van Laer's applied power is not the plasma power.
- **Status:** all sources remain ai_checked; human verification is still pending. Start with the corrected rows and the critical findings above.
