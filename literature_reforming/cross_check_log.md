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

## Summary by paper

- **SRC008 Akande 2022** (2026-11-20): the 32 kW / 60 lpm CH4 / S/C 3 point is identical: X_CH4 96.6%, SEI_CH4 717 kJ/mol and EC_CH4 742 kJ/mol on absorbed microwave power, with steam-generator duty not reported. The corrigendum composition point (62 lpm) is also identical, at SEI_CH4 694 kJ/mol. Both found independently that the reported 2247 g H2/h (and 70 g/kWh) exceeds what 60 lpm CH4 can give (~1190-1295 g/h at complete SMR + WGS). Both found that Fig. 10 conflicts with the reported conversion. Differences XR001-XR002.
- **SRC004 Collodi (IEAGHG) 2017** (2026-11-20): Base Case design reference agrees on every value: 100,000 Nm3/h H2 (8,994 kg/h); CH4 feed ~21,600 mol/min; net CH4 conversion 84.6% over pre-reformer and reformer; radiant duty 96.1 MW, giving EC_CH4,abs 315-316 and EC_CH4,fired 574 kJ/mol (HHV); plant eta_HHV 81.1% (LHV ratio 75.9%); f_electric 0 with 9.918 MWe export; author metric 14.212 GJ LHV/1000 Nm3 H2. Both note that the 28 bar HTS-inlet pressure is not the tube pressure, and both label the case a design basis, not measured data. Difference XR003.
- **SRC005 From 2024** (2026-11-20): all reported values agree: 97% CH4 conversion at 900 degC, 10 barg, S/C 2.7 (start-up from 645 degC, steady after 2.3 h); 94 +/- 1% at 950 degC, 20 barg at TOS 485 and 1535 h (no deactivation; the 1050 h between them included other operating scenarios, as GPT notes); author reactor efficiency ~72% at ~25 kW and ~80% at ~35 kW (Fig. 5, I x V boundary, including sensible heating 400 -> 900 degC). Both find that point-matched power, CH4 feed and composition are not reported, so EC_CH4 is NR. Difference XR004.
- **SRC006 From 2025** (2026-11-20): same four conditions (numbered differently) with identical values: regulated run at 900 degC, 6 barg, 6.4 Nm3/h biogas, 80 h, module 1.99; unregulated run at 950 degC, 10 barg, 6.3 Nm3/h, 20 h; Table 2 cases at module 2.00 and 2.02. Both find no power or energy data (confidential). CH4 feed for the unregulated run: ours 2.67 mol/min (57.1% CH4), GPT 2.53-2.72 (54-58%), consistent. Difference XR005.

## Differences

| ID | Date | Source / record | Ours | GPT | Checked against PDF | Action |
|---|---|---|---|---|---|---|
| XR001 | 2026-11-20 | SRC008 corrigendum composition point (62 lpm, 32 kW): conversion | 83.1%, from the carbon basis of the wet composition (no soot), EC_CH4 835 kJ/mol | unclear; residual CH4 fraction not taken as conversion, EC_CH4 NR | both defensible: ours is a labelled reviewer calculation that assumes no solid carbon (none observed) and no unmeasured carbon species | kept ours (conditional, labelled) |
| XR002 | 2026-11-20 | SRC008 operating points | power scan 17, 32, 47 kW at S/C 3 (EC_CH4 511, 742, 1078 kJ/mol) | S/C 5 at 32 kW (X 99.8%, EC_CH4 719 kJ/mol) | different points from the same figures, consistent | kept ours (noted) |
| XR003 | 2026-11-20 | SRC004 reformer catalyst | NR | nickel (Annex I) | GPT right: Annex I PDF p. 259 states the reformer and pre-reformer catalysts contain nickel | corrected (E051; summary table) |
| XR004 | 2026-11-20 | SRC005 Fig. 5 endpoint points: flow and CH4 feed | biogas 15 and 27 Nm3/h assigned to the ~25 and ~35 kW endpoints, giving CH4 5.6-8.4 and 10.0-15.1 mol/min (labelled reviewer interpretation) | flows not mapped to endpoints; CH4 feed NR | the paper gives the 15-27 Nm3/h range for the cohort, not per point; not settled by the PDF | kept ours (labelled assumption); for human check |
| XR005 | 2026-11-20 | SRC006 regulated run: conversion | X_CH4 ~98%, X_CO2 ~42-54% and O/C, H/C closure within 0.3% (labelled reviewer calculations from Table 1 and the Fig. 5C inlet ratio) | NR; residual CH4 0.24% not taken as conversion | ours is a conditional calculation; the authors report no conversion | kept ours (labelled reviewer calculation) |
