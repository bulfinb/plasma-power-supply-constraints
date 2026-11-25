# Processing log

Single record of the AI tools, model versions and human reviewers that processed each source (workflow.md section 3a). Review files say only "Claude (AI)" or "Codex AI"; this log carries the versions.

Source documents (manuscripts, supplements) are not distributed with this folder. Each `outputs/extraction.md` records SHA-256 hashes of the documents used, so readers can confirm they hold the same versions.

## Tools

| Tool | Version(s) | Model ID | Notes |
|---|---|---|---|
| Claude Code (Anthropic CLI) | 2.1.312-2.1.318 | claude-opus-5-5 (Claude Opus 5.5) | Versions and model IDs recovered 2026-11-05 from local session logs (~/.claude/projects/); every logged response in all three sessions used claude-opus-5-5 |
| Codex (OpenAI) | not recorded | not recorded | Initial extractions of SRC001 and SRC002, 2026-10-28; version not recoverable from this machine |

## Sessions

| Session ID | Tool | Dates | Claude Code version(s) | Model ID |
|---|---|---|---|---|
| (not recorded) | Codex | 2026-10-28 | NA | not recorded |
| 2fa545d5 | Claude Code | 2026-10-30 to 2026-11-04 | 2.1.312 (10-30, start), 2.1.314 (10-30 to 11-03), 2.1.317 (11-04), 2.1.318 (11-04, end) | claude-opus-5-5 |
| 674ce652 | Claude Code | 2026-10-30 (brief) | 2.1.314 | claude-opus-5-5 |
| 088bb8d0 | Claude Code | 2026-11-05 to 2026-11-10 | 2.1.318; 2.1.322 (2026-11-10) | claude-opus-5-5 |
| 95037651 | Claude Code | 2026-11-24 to 2026-11-25 | 2.1.331 | claude-opus-5-5 |

## Events

Power-systems events are logged in [../power_systems/processing_log.md](../power_systems/processing_log.md) from 2026-11-10; earlier power-systems rows below are also copied there.

Event types: extraction (initial), revision (substantive change to records), appraisal, summary update. A human check is recorded in the Human reviewer column of the AI row it reviewed (e.g. "reviewed by BB, date (human_verified)"), so each row shows both who extracted and who checked. The 2026-10-28 to 2026-11-04 rows were reconstructed on 2026-11-05 from the extraction files' revision notes and the session logs.

| Date | Source ID | Folder | Event | Tool and version | Model ID | Session | Human reviewer |
|---|---|---|---|---|---|---|---|
| 2026-10-28 | SRC001 | Wismann_Science_2019_Joule_SMR | extraction | Codex, not recorded | not recorded | not recorded | |
| 2026-10-28 | SRC002 | Geng_APC_2022_Plasma_SMR | extraction | Codex, not recorded | not recorded | not recorded | |
| 2026-10-30 | SRC001 | Wismann_Science_2019_Joule_SMR | appraisal and summary update | Claude Code 2.1.314 | claude-opus-5-5 | 2fa545d5 | |
| 2026-10-30 | SRC002 | Geng_APC_2022_Plasma_SMR | appraisal and revision | Claude Code 2.1.314 | claude-opus-5-5 | 2fa545d5 | |
| 2026-10-30 | SRC003 | Lewis_NETL_2022_Fired_SMR | extraction | Claude Code 2.1.312-2.1.314 | claude-opus-5-5 | 2fa545d5 | |
| 2026-10-30 | SRC004 | Collodi_IEAGHG_2017_Fired_SMR | extraction | Claude Code 2.1.314 | claude-opus-5-5 | 2fa545d5 | |
| 2026-11-04 | SRC005 | From_CEJ_2024_eSMR_Biogas | extraction | Claude Code 2.1.317 | claude-opus-5-5 | 2fa545d5 | |
| 2026-11-04 | SRC006 | From_CEJ_2025_eSMR_Biogas2 | extraction | Claude Code 2.1.318 | claude-opus-5-5 | 2fa545d5 | |
| 2026-11-05 | SRC001-SRC006 | (earlier sources) | summary update (five comparison tables) | Claude Code 2.1.318 | claude-opus-5-5 | 088bb8d0 | |
| 2026-11-05 | SRC007 | Hrabovsky_PCPP_2018_Plasma_SMR | extraction | Claude Code 2.1.318 | claude-opus-5-5 | 088bb8d0 | |
| 2026-11-05 | SRC008 | Akande_IJHE_2022_Plasma_SMR | extraction | Claude Code 2.1.318 | claude-opus-5-5 | 088bb8d0 | |
| 2026-11-05 | SRC009 | Song_CAP_2020_Plasma_DRM | extraction | Claude Code 2.1.318 | claude-opus-5-5 | 088bb8d0 | |
| 2026-11-05 | SRC010 | Hrycak_SciRep_2023_Plasma_Biogas_SR | extraction | Claude Code 2.1.318 | claude-opus-5-5 | 088bb8d0 | |
| 2026-11-05 | SRC011 | Kelly_JCOU_2023_Plasma_DRM | extraction | Claude Code 2.1.318 | claude-opus-5-5 | 088bb8d0 | |
| 2026-11-05 | SRC012 | Zhu_CatToday_2019_GlidingArc_SMR | extraction | Claude Code 2.1.318 | claude-opus-5-5 | 088bb8d0 | |
| 2026-11-05 | SRC013 | Andersen_ChemEngJ_2020_DBD_DRM | extraction | Claude Code 2.1.318 | claude-opus-5-5 | 088bb8d0 | |
| 2026-11-05 | SRC014 | Kwon_JCOU_2023_GlidingArc_DRM | extraction | Claude Code 2.1.318 | claude-opus-5-5 | 088bb8d0 | |
| 2026-11-05 | SRC015 | Wanten_JCOU_2022_GlowDischarge_DRM | extraction | Claude Code 2.1.318 | claude-opus-5-5 | 088bb8d0 | |
| 2026-11-05 | (all) | search_and_selection_log.md, plasma_shortlist_2026-11-05.md | literature search and screening | Claude Code 2.1.318 | claude-opus-5-5 | 088bb8d0 | |
| 2026-11-05 | (power_systems) | power_systems/scaleup_supplies.csv, scaleup_sources.md, scaleup_wall_basis.py | web search and representative supply table | Claude Code 2.1.318 | claude-opus-5-5 | 088bb8d0 | |
| 2026-11-09 | (all) | workflow.md, literature_review_objectives.md, literature_search_strategy.md, ../README.md | cross-references for new pyrolysis and CO2-splitting topic folders; folder renamed from literature/ | Claude Code 2.1.318 | claude-opus-5-5 | 088bb8d0 | |
| 2026-11-09 | (reviews) | literature_reviews/reviews_shortlist.md and review folders | web search, Crossref metadata check, open-access PDF downloads (5 of 14) | Claude Code 2.1.318 | claude-opus-5-5 | 088bb8d0 | |
| 2026-11-09 | (power supply) | literature_plasma_powersupply/ (README, PS001-PS002); literature_reviews RV015-RV017 | web search, Crossref/arXiv metadata, open-access PDF downloads | Claude Code 2.1.318 | claude-opus-5-5 | 088bb8d0 | |
| 2026-11-09 | (power supply) | literature_plasma_powersupply/README.md | discussion point on supply "niche product" claim (RV015); from general knowledge plus power_systems table, items to source | Claude Code 2.1.318 | claude-opus-5-5 | 088bb8d0 | |
| 2026-11-09 | (power supply) | literature_plasma_powersupply/README.md (D1-D10) | web search for to-source items (ozone, magnetron, solid-state, capex); D1 and D10 checked in full text | Claude Code 2.1.318 | claude-opus-5-5 | 088bb8d0 | |
| 2026-11-09 | (power supply) | literature_plasma_powersupply/README.md; power_systems/supply_maturity_niche.md | restructure: manufacturer data and niche discussion moved to power_systems; TEA papers PS003-PS004 added (Crossref-checked) | Claude Code 2.1.318 | claude-opus-5-5 | 088bb8d0 | |
| 2026-11-09 | (power supply) | power_systems/source_register.csv, source_archive/, BB_search.txt | local copies (direct or Wayback) and Wayback snapshots for D, T and S sources; cited values spot-checked in copies | Claude Code 2.1.318 | claude-opus-5-5 | 088bb8d0 | |
| 2026-11-10 | (all) | workflow.md (v0.5), literature_search_strategy.md, processing_log.md | revision after external LLM consistency review: flow reference rule, human-check logging, version renumbering, checker definition | Claude Code 2.1.322 | claude-opus-5-5 | 088bb8d0 | |
| 2026-11-10 | SRC010, SRC011 | Hrycak_SciRep_2023_Plasma_Biogas_SR; Kelly_JCOU_2023_Plasma_DRM | status revision: human_verified (BB, 2026-11-05, informal) withdrawn; ai_checked pending systematic human check | Claude Code 2.1.322 | claude-opus-5-5 | 088bb8d0 | |
| 2026-11-10 | (all) | workflow.md (v0.6), _source_template.md, literature_review_objectives.md | simplification at BB request: core energy metrics, boundary/heat lines, eta_HHV for benchmarks only, fewer diagnostics, four summary tables | Claude Code 2.1.322 | claude-opus-5-5 | 088bb8d0 | |
| 2026-11-10 | (all) | workflow.md (v0.7), human_checks/findings.csv, summary.csv | human-check and AI-error log set up | Claude Code 2.1.322 | claude-opus-5-5 | 088bb8d0 | |
| 2026-11-10 | (power_systems) | source_register.csv, supply_maturity_niche.md, BB_search.txt | D11 copy (manual download by BB) hashed and registered; authors recorded; cost statements checked against copy (pp. 1, 9) | Claude Code 2.1.322 | claude-opus-5-5 | 088bb8d0 | |
| 2026-11-10 | (power_systems) | source_register.csv, supply_maturity_niche.md, BB_search.txt | D5 Muegge datasheet (manual download by BB) hashed and registered; 2450 MHz / 15 kW checked; noted as magnetron head without efficiency or price | Claude Code 2.1.322 | claude-opus-5-5 | 088bb8d0 | |
| 2026-11-10 | (power_systems) | supply_maturity_niche.md, source_register.csv, BB_search.txt, suggested_quote_requests.txt, README.md | D12 dropped (unverifiable price; BB decision); quote request Q1 (915 MHz 100 kW generator) added | Claude Code 2.1.322 | claude-opus-5-5 | 088bb8d0 | |
| 2026-11-20 | (all) | workflow.md (v0.9), _source_template.md, literature_review_objectives.md | revision after external LLM consistency review (GPT-6.1 Sol): heat data for scale-up noted per paper; fired references as labelled reference cases; SHA-256 field in template; objectives wording (own workflow per topic, R1-R4 in quality summary, scale-up as a separate step) | Claude Code 2.1.322 | claude-opus-5-5 | d3b811d6 | |
| 2026-11-20 | SRC008 | literature_reforming | cross_check_log.md started; GPT cross-check of Akande logged (XR001-XR002); agreement on headline values, no corrections | Claude Code 2.1.322 | claude-opus-5-5 | d3b811d6 | |
| 2026-11-20 | SRC004 | Collodi_IEAGHG_2017_Fired_SMR | revision after GPT cross-check (XR003): nickel catalyst added (E051); otherwise full agreement | Claude Code 2.1.322 | claude-opus-5-5 | d3b811d6 | |
| 2026-11-20 | SRC005, SRC006 | literature_reforming | GPT cross-check logged (cross_check_log.md XR004-XR005); reported values agree, no corrections; XR004 flagged for human check | Claude Code 2.1.322 | claude-opus-5-5 | d3b811d6 | |
| 2026-11-20 | SRC002 | literature_reforming | GPT cross-check logged (cross_check_log.md XR006); full agreement, feed interpretation confirmed independently, no corrections | Claude Code 2.1.322 | claude-opus-5-5 | d3b811d6 | |
| 2026-11-20 | SRC002 | Geng_APC_2022_Plasma_SMR | partial human check of the CH4 feed interpretation (E020-E022, C003, E065): confirmed, no findings; E065 human_verified; summary and extraction notes updated | Claude Code 2.1.322 | claude-opus-5-5 | d3b811d6 | reviewed by BB, 2026-11-20 (partial: feed only) |
| 2026-11-20 | SRC007 | literature_reforming | GPT cross-check logged (cross_check_log.md XR007); reported values agree; tracer-based conversion and EC_CH4 kept, flagged for human check | Claude Code 2.1.322 | claude-opus-5-5 | d3b811d6 | |
| 2026-11-20 | SRC010 | Hrycak_SciRep_2023_Plasma_Biogas_SR | revision after GPT cross-check (XR008): Vm 22.414 -> 24.25 L/mol (reproduces the authors' H2 rates and conversions); volume-dependent values updated; stale "Human verified" table header corrected to pending; power_systems/figures/scaleup_wall_basis.py and notes/scaleup_assessment.md updated | Claude Code 2.1.322 | claude-opus-5-5 | d3b811d6 | |
| 2026-11-20 | SRC011, SRC014 | literature_reforming | GPT cross-check logged (cross_check_log.md XR009-XR010); headline values agree, no corrections | Claude Code 2.1.322 | claude-opus-5-5 | d3b811d6 | |
| 2026-11-20 | SRC003, SRC009 | literature_reforming | GPT cross-check logged (cross_check_log.md); full agreement, no corrections | Claude Code 2.1.322 | claude-opus-5-5 | d3b811d6 | |
| 2026-11-20 | SRC015, SRC001 | literature_reforming | GPT cross-check logged (cross_check_log.md); full agreement, no corrections | Claude Code 2.1.322 | claude-opus-5-5 | d3b811d6 | |
| 2026-11-20 | SRC012, SRC013 | literature_reforming | GPT cross-check logged (Andersen not strictly blind); full agreement, no corrections; closing summary of the reforming cross-check added to cross_check_log.md | Claude Code 2.1.322 | claude-opus-5-5 | d3b811d6 | |
| 2026-11-20 | (all) | 0_synthesis/ | reforming synthesis tables: build_synthesis.py, reforming_synthesis.csv (29 OP rows), reforming_synthesis_tables.md (headline rows by route, fired and Joule benchmarks, not-plotted list, notes, reading summary); values from the short summaries incl. GPT cross-check corrections; industrial-supply EC_CH4 from power_systems/supply_classes.csv; figures to follow | Claude Code 2.1.322 | claude-opus-5-5 | d3b811d6 | |
| 2026-11-20 | (all) | 0_synthesis/ | figure reforming_x_vs_ec.png/.svg (plot_x_vs_ec.py, reads reforming_synthesis.csv): X_CH4 vs EC_CH4 at the paper boundary and with an industrial supply; colour = route, marker = activation; reaction-enthalpy lines; fired SMR references on heat basis (fuel HHV and absorbed heat); Joule sources not plotted (no matched power) | Claude Code 2.1.322 | claude-opus-5-5 | d3b811d6 | |
| 2026-11-20 | (all) | 0_synthesis/ | rebuilt after the power-supply cross-check: M1 0.74-0.84, M2 0.63-0.72 (power_systems XP002); industrial-supply estimates, tables and figures regenerated; summary text updated | Claude Code 2.1.322 | claude-opus-5-5 | d3b811d6 | |
| 2026-11-20 | (all) | 0_synthesis/ | make_latex_table.py -> reforming_table.tex (booktabs table for the manuscript: max two headline cases per paper, plasma rows by decreasing power, fired SMR benchmarks block; Joule-heated benchmarks in the table note as no point-matched power) | Claude Code 2.1.322 | claude-opus-5-5 | d3b811d6 | |
| 2026-11-20 | SRC005 | From_CEJ_2024_eSMR_Biogas | Reviewer estimate C004 (EC_CH4 388-485 kJ/mol from Cantera equilibrium Q_reaction / author efficiency; checked against authors 1.0 kWh/Nm3) and C005 (capacity axis consistent with Q_in if flows are process gas); evidence E043-E045; search log round 2 (S022-S032, R021-R029); folders Wismann_IECR_2019_Joule_SMR_Dynamics and Wismann_CEJ_2021_Joule_SMR_Transient created (PDFs only) | Claude Code 2.1.322 | claude-opus-5-5 | d3b811d6 | |
| 2026-11-20 | SRC005 | 0_synthesis/ | From 2024 OP004-OP007 reviewer-estimate row (EC_CH4 388-485 kJ/mol, SRC005-C004) added to build_synthesis.py and to the LaTeX table as a Joule-heated pilot benchmark block; reading summary updated; figure unchanged (Joule not plotted) | Claude Code 2.1.322 | claude-opus-5-5 | d3b811d6 | |
| 2026-11-20 | SRC005 | 0_synthesis/ | plot_x_vs_ec.py: Joule-heated pilot reviewer estimate (From 2024, SRC005-C004) added as open star with EC and conversion range bars, both panels | Claude Code 2.1.322 | claude-opus-5-5 | d3b811d6 | |
| 2026-11-23 | (all) | 0_synthesis/ | rebuilt after the power-supply relevance review: M1 0.74-0.84 -> 0.74-0.82 (power_systems, PW045 dropped); M1 rows of the synthesis, table and figures updated | Claude Code 2.1.322 | claude-opus-5-5 | d3b811d6 | |
| 2026-11-25 | (all) | search_and_selection_log.md | round 3 started: BB's Google Scholar recency search for 2026 plasma and Joule-heated reforming logged (S033, nothing additional); search terms and screening criteria prepared for BB | Claude Code 2.1.331 | claude-opus-5-5 | 95037651 | |
| 2026-11-25 | (all) | 0_synthesis/ | manuscript figure plot_manuscript_figure.py -> 0_manuscript_figure.png/.svg/.pdf (copied to manuscript/figures/reforming_figure.*): headline rows only, one panel (open = paper power boundary, filled = industrial supply), style matched to the power-supply manuscript figure; axes 170-3500 kJ/mol and 30-105% with Andersen 2020 off-scale (BB); italic ΔH labels; reforming_synthesis.csv confirmed current (rebuild from build_synthesis.py identical) | Claude Code 2.1.331 | claude-opus-5-5 | 95037651 | |
| 2026-11-25 | (all) | 0_synthesis/ | make_latex_table.py trimmed (BB): table now supplements the figure, columns Source, Route, Reactor / catalyst, Power, T, p, assumed eta_PS; conversion/EC columns and paper-specific notes removed (kept in SI 2); figure placed before the table in the manuscript | Claude Code 2.1.331 | claude-opus-5-5 | 95037651 | |
