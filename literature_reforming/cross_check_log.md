# Cross-check against an independent GPT extraction

Each paper was extracted a second time, in full and blind, by a second AI (OpenAI GPT-6.1 Sol, Codex desktop app). The work was done in a separate local folder that is not published. The extraction followed workflow.md (version per paper below) and _source_template.md.

GPT had:
- the source documents, with SHA-256 hashes listed in a sources file;
- the objectives;
- SRC013 (Andersen) as the only worked example.

GPT did not have our extractions or short summaries, the search and selection files, or this log.

Our reforming extractions were made under protocols 0.1-0.5, which use five summary tables. GPT's follow workflow 0.9, which uses four tables and the core metrics SEI_CH4 and EC_CH4. Values are therefore compared metric by metric, not by table position.

Each paper gets a one-line summary of what agreed, then one row per difference that matters. Every difference is checked against the PDF.

Action is one of:
- **corrected:** our extraction is revised; see processing_log.md and the Revisions section of its extraction.md;
- **kept ours**;
- **workflow rule:** workflow.md is changed;
- **for human check:** the PDF does not settle it.

These checks are AI-to-AI. They do not change a source's status (ai_checked), and they are not logged in ../human_checks/. IDs use the prefix XR to keep them distinct from the CO2-splitting log.

## Independent extractions

| Source | Date | Tool | Model | Workflow | Notes |
|---|---|---|---|---|---|
| SRC008 Akande 2022 | 2026-11-20 | Codex desktop (version not recorded) | GPT-6.1 Sol (confirmed by BB; not logged by the tool) | 0.9 | manuscript and corrigendum |
| SRC004 Collodi (IEAGHG) 2017 | 2026-11-20 | Codex desktop (version not recorded) | as above | 0.9 | report incl. Annex I; fired reference (R1-R4) |
| SRC005 From 2024 | 2026-11-20 | Codex desktop (version not recorded) | as above | 0.9 | manuscript and supplementary |
| SRC006 From 2025 | 2026-11-20 | Codex desktop (version not recorded) | as above | 0.9 | manuscript and ESI; no 2024 values carried over |
| SRC002 Geng 2022 | 2026-11-20 | Codex desktop (version not recorded) | as above (now logged by GPT) | 0.9 | manuscript, ESI pdf and docx |
| SRC007 Hrabovsky 2018 | 2026-11-20 | Codex desktop (version not recorded) | as above | 0.9 | manuscript (no ESI) |
| SRC010 Hrycak 2023 | 2026-11-20 | Codex desktop (version not recorded) | as above | 0.9 | manuscript (no ESI) |

## Summary by paper

- **SRC008 Akande 2022** (2026-11-20): the 32 kW / 60 lpm CH4 / S/C 3 point is identical: X_CH4 96.6%, SEI_CH4 717 kJ/mol and EC_CH4 742 kJ/mol on absorbed microwave power, with steam-generator duty not reported. The corrigendum composition point (62 lpm) is also identical, at SEI_CH4 694 kJ/mol. Both found independently that the reported 2247 g H2/h (and 70 g/kWh) exceeds what 60 lpm CH4 can give (~1190-1295 g/h at complete SMR + WGS). Both found that Fig. 10 conflicts with the reported conversion. Differences XR001-XR002.
- **SRC004 Collodi (IEAGHG) 2017** (2026-11-20): Base Case design reference agrees on every value: 100,000 Nm3/h H2 (8,994 kg/h); CH4 feed ~21,600 mol/min; net CH4 conversion 84.6% over pre-reformer and reformer; radiant duty 96.1 MW, giving EC_CH4,abs 315-316 and EC_CH4,fired 574 kJ/mol (HHV); plant eta_HHV 81.1% (LHV ratio 75.9%); f_electric 0 with 9.918 MWe export; author metric 14.212 GJ LHV/1000 Nm3 H2. Both note that the 28 bar HTS-inlet pressure is not the tube pressure, and both label the case a design basis, not measured data. Difference XR003.
- **SRC005 From 2024** (2026-11-20): all reported values agree: 97% CH4 conversion at 900 degC, 10 barg, S/C 2.7 (start-up from 645 degC, steady after 2.3 h); 94 +/- 1% at 950 degC, 20 barg at TOS 485 and 1535 h (no deactivation; the 1050 h between them included other operating scenarios, as GPT notes); author reactor efficiency ~72% at ~25 kW and ~80% at ~35 kW (Fig. 5, I x V boundary, including sensible heating 400 -> 900 degC). Both find that point-matched power, CH4 feed and composition are not reported, so EC_CH4 is NR. Difference XR004.
- **SRC006 From 2025** (2026-11-20): same four conditions (numbered differently) with identical values: regulated run at 900 degC, 6 barg, 6.4 Nm3/h biogas, 80 h, module 1.99; unregulated run at 950 degC, 10 barg, 6.3 Nm3/h, 20 h; Table 2 cases at module 2.00 and 2.02. Both find no power or energy data (confidential). CH4 feed for the unregulated run: ours 2.67 mol/min (57.1% CH4), GPT 2.53-2.72 (54-58%), consistent. Difference XR005.
- **SRC002 Geng 2022** (2026-11-20): all shared values agree. CH4 conversion is ~7% plasma-off, ~60% at 15 W (300 degC) and ~80% at 15 W (440 degC); discharge power comes from the Q-V loop with frequency NR. EC_CH4 is ~1490 vs ~1468 kJ/mol at 300 degC and ~1120 vs ~1101 at 440 degC; the ~1.5% spread comes from the feed derivation. EY_H2 is 14.8-16.2 and 19.8-21.6 g/kWh, H2 selectivity 88% (not an efficiency), carbon recovery ~90%, and the runs last ~2 h. The unclear feed wording was resolved independently to the same ~1.0e-3 mol/min CH4: ours via the water feed and S/C 4.4, GPT via 25 mL/min CH4 at 25 degC. Both flag the printed balance/selectivity equations as inconsistent with the values. Furnace and steam duties are NR in both. Difference XR006.
- **SRC007 Hrabovsky 2018** (2026-11-20): same four test segments, with the same feeds and arc powers: SMR 150 and 75 slm CH4 at 120 kW; CO2-fed 125 slm CH4 at 116 and 88-89 kW. Fig. 8 has a 325 A segment at 88 kW and a later one at 89 kW; we use the later one. SEI_CH4 on arc power is identical (1076 / 2152 / 1248 / 947-958 kJ/mol). The author H2 costs are identical: 79 (conclusion) vs 86 (results) MJ/kg process basis, 116 MJ/kg CO2-fed, 192 MJ/kg on arc power. Torch efficiency is 0.57-0.60, plasma steam comes from the torch, there is no external heater, and the segments are minutes long (not endurance). GPT labels the CO2-fed runs "mixed" (CO2 plus torch steam); ours "DRM (+plasma H2O)". Difference XR007.
- **SRC010 Hrycak 2023** (2026-11-20): same three Table 1 points with identical reported values (X_CH4 48.9 / 66.1 / 74.3%; H2 239 / 234 / 171.5 g/h; EY 36.8 / 36.1 / 26.4 g/kWh at 6.5 kW absorbed), steam-vaporizer duty NR in both. GPT inferred the authors' molar volume from their own numbers (XR008), which changed our energy values. Our carbon-closure check (now 71-79%) has no counterpart in GPT's extraction.

## Differences

| ID | Date | Source / record | Ours | GPT | Checked against PDF | Action |
|---|---|---|---|---|---|---|
| XR001 | 2026-11-20 | SRC008 corrigendum composition point (62 lpm, 32 kW): conversion | 83.1%, from the carbon basis of the wet composition (no soot), EC_CH4 835 kJ/mol | unclear; residual CH4 fraction not taken as conversion, EC_CH4 NR | both defensible: ours is a labelled reviewer calculation that assumes no solid carbon (none observed) and no unmeasured carbon species | kept ours (conditional, labelled) |
| XR002 | 2026-11-20 | SRC008 operating points | power scan 17, 32, 47 kW at S/C 3 (EC_CH4 511, 742, 1078 kJ/mol) | S/C 5 at 32 kW (X 99.8%, EC_CH4 719 kJ/mol) | different points from the same figures, consistent | kept ours (noted) |
| XR003 | 2026-11-20 | SRC004 reformer catalyst | NR | nickel (Annex I) | GPT right: Annex I PDF p. 259 states the reformer and pre-reformer catalysts contain nickel | corrected (E051; summary table) |
| XR004 | 2026-11-20 | SRC005 Fig. 5 endpoint points: flow and CH4 feed | biogas 15 and 27 Nm3/h assigned to the ~25 and ~35 kW endpoints, giving CH4 5.6-8.4 and 10.0-15.1 mol/min (labelled reviewer interpretation) | flows not mapped to endpoints; CH4 feed NR | the paper gives the 15-27 Nm3/h range for the cohort, not per point; not settled by the PDF | kept ours (labelled assumption); for human check |
| XR005 | 2026-11-20 | SRC006 regulated run: conversion | X_CH4 ~98%, X_CO2 ~42-54% and O/C, H/C closure within 0.3% (labelled reviewer calculations from Table 1 and the Fig. 5C inlet ratio) | NR; residual CH4 0.24% not taken as conversion | ours is a conditional calculation; the authors report no conversion | kept ours (labelled reviewer calculation) |
| XR006 | 2026-11-20 | SRC002 operating points | plasma-off, 15 W at 300 and 440 degC (plus 20 W ~74% noted in text) | adds Al2O3-only 15 W (~30%, EC_CH4 ~2935), Ni 10 W (~50%, ~1174) and the Cu cascade (no EC: power not restated) | consistent with the paper; the S/C 4.4 vs Fig. 3 caption 4.5 noted by GPT | kept ours (noted) |
| XR007 | 2026-11-20 | SRC007 conversion and EC_CH4 per segment | X_CH4 91.3 / 99.1 / 95.3 / 83.3% (X_CO2 91.0 / 89.0) from digitised MS traces with the 50 slm Ar tracer; EC_CH4 1179 / 2172 / 1309 / 1149 kJ/mol; carbon closure 94-101% | conversion not reconstructed from gas fractions; EC_CH4 NR; uses the authors' conversion-vs-enthalpy points instead (~99-99.5%) | the paper states the Ar is a tracer added to determine the outlet flow (PDF p. 13), and our values match the authors' plotted points (95.8 / 91.5 vs 95.3 / 91.0; 82.7 / 88.8 vs 83.3 / 89.0) | kept ours (labelled reviewer calculation, cross-checked); for human check, as it underpins the only large thermal-arc EC_CH4 |
| XR008 | 2026-11-20 | SRC010 molar volume for NL flows | 22.414 L/mol (0 degC) assumed; EC_CH4 238 / 264 / 471 kJ/mol; H2-anchored X 2-4 points above the authors' | 24.25 L/mol inferred: the authors' H2 rate, composition and conversion imply 24.246 / 24.251 / 24.255 L/mol in the three rows; EC_CH4 258 / 286 / 509 | GPT right: at 24.25 L/mol our own H2-anchored conversion equals the authors' in all three rows; workflow section 4 prefers the molar volume that reproduces the authors' derived values | corrected (+8.2% on SEI_CH4 and EC_CH4; carbon closure 71-79%; also power_systems wall-basis table) |
