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

Each paper gets a one-line summary of what agreed, then one row per difference that matters. Every difference is checked against the PDF. Action: **corrected** (our extraction revised; see processing_log.md and the Revisions section of its extraction.md), **kept ours**, **workflow rule** (workflow.md changed), or **for human check** (not settled by the PDF). These checks are AI-to-AI. They do not change a source's status (ai_checked) and are not logged in ../human_checks/.

## Summary by paper

- **SRC018 Bongers 2017** (2026-11-19): same five operating points; OP001-OP002 values identical (X 83% and 47%; 14.8 and 10.0 kWh/Nm3 CO); OP005 within reading precision. Differences XC001-XC003.
- **SRC021 Bryssinck 2025** (2026-11-19): best point agrees (X 20%, EC_CO 7.33 vs 7.25 kWh/Nm3, carbon 0.268 kg/Nm3 CO in both, eta_LHV 35.9 vs 36.2%). Both found independently that the empty-reactor control is inconsistent (6.4% conversion and 13.5 MWh/t imply 2 CO per CO2 converted) and that recycle lowers CO output. Difference XC004.

## Differences

| ID | Date | Source / record | Ours | GPT | Checked against PDF | Action |
|---|---|---|---|---|---|---|
| XC001 | 2026-11-19 | SRC018 OP005 power | ~1 kW | NR | GPT right: 1 kW and 14 slm belong to Exps. 1-2, not Exp. 7 | corrected |
| XC002 | 2026-11-19 | SRC018 gas temperature 5700 K | conditions from the Fig. 4 caption (5 kW, 75 slm), assigned to OP001-OP004 | caption and text conflict flagged; not assigned | GPT right: the text says the Fig. 2d setup (3.1 kW, 0.6 eV); the caption says 0.9 eV | corrected (conflict noted; not assigned to any OP) |
| XC003 | 2026-11-19 | SRC018 OP003-OP004 (75 slm) | Fig. 3b values (X ~10%, ~22.5%; eta ~36% at 10 kW) | text values (X 11%, 23%; eta 40%) | both defensible; the figure agrees with the paper's own X x 2.9 / SEI | kept ours; workflow rule (text vs figure) |
| XC004 | 2026-11-19 | SRC021 operating points | 4 OPs | 8 OPs, adding the 65 mm bed, 110 L/min, recycle off and 540 s; eta_LHV ~22-23% at 65 mm and 110 L/min | values consistent with our C001 | kept ours (noted: the carbon-bed benefit depends on bed temperature) |
