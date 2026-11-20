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
