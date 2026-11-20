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

## Summary by paper

- **SRC008 Akande 2022** (2026-11-20): the 32 kW / 60 lpm CH4 / S/C 3 point is identical: X_CH4 96.6%, SEI_CH4 717 kJ/mol and EC_CH4 742 kJ/mol on absorbed microwave power, with steam-generator duty not reported. The corrigendum composition point (62 lpm) is also identical, at SEI_CH4 694 kJ/mol. Both found independently that the reported 2247 g H2/h (and 70 g/kWh) exceeds what 60 lpm CH4 can give (~1190-1295 g/h at complete SMR + WGS). Both found that Fig. 10 conflicts with the reported conversion. Differences XR001-XR002.

## Differences

| ID | Date | Source / record | Ours | GPT | Checked against PDF | Action |
|---|---|---|---|---|---|---|
| XR001 | 2026-11-20 | SRC008 corrigendum composition point (62 lpm, 32 kW): conversion | 83.1%, from the carbon basis of the wet composition (no soot), EC_CH4 835 kJ/mol | unclear; residual CH4 fraction not taken as conversion, EC_CH4 NR | both defensible: ours is a labelled reviewer calculation that assumes no solid carbon (none observed) and no unmeasured carbon species | kept ours (conditional, labelled) |
| XR002 | 2026-11-20 | SRC008 operating points | power scan 17, 32, 47 kW at S/C 3 (EC_CH4 511, 742, 1078 kJ/mol) | S/C 5 at 32 kW (X 99.8%, EC_CH4 719 kJ/mol) | different points from the same figures, consistent | kept ours (noted) |
