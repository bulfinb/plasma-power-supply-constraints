# Processing log

Single record of the AI tools, model versions and human reviewers that processed each source in this folder (workflow.md section 3a, [../literature_reforming/workflow.md](../literature_reforming/workflow.md)). Review files say only "Claude (AI)"; this log carries the versions. Tool and session details are listed in [../literature_reforming/processing_log.md](../literature_reforming/processing_log.md) and repeated here only for sessions that touched this folder.

Source documents are not distributed. Each `outputs/extraction.md` records SHA-256 hashes of the documents used.

## Events

| Date | Source ID | Folder | Event | Tool and version | Model ID | Session | Human reviewer |
|---|---|---|---|---|---|---|---|
| 2026-11-09 | (folder) | literature_co2_splitting | folder set up: objectives, search strategy, logs | Claude Code 2.1.318 | claude-opus-5-5 | d3b811d6 | |
| 2026-11-11 | (folder) | literature_co2_splitting | searches CS001-CS018, records CR001-CR029, plasma_shortlist_2026-11-11.md (incl. RV001, RV002 check) | Claude Code 2.1.322 | claude-opus-5-5 | d3b811d6 | |
| 2026-11-11 | SRC016-SRC024 | literature_co2_splitting | nine exemplars approved by BB; folders created; Kiefer, Bongers, Van Laer published versions and Yong preprint downloaded from repositories; five left for BB to download | Claude Code 2.1.322 | claude-opus-5-5 | d3b811d6 | |
| 2026-11-11 | SRC017, SRC019-SRC023 | literature_co2_splitting | manuscripts and ESI downloaded by BB; checked by Claude (correct papers; Bryssinck is the accepted author version); hashes in plasma_shortlist_2026-11-11.md; OSTI preprint of SRC023 removed | Claude Code 2.1.322 | claude-opus-5-5 | d3b811d6 | |
| 2026-11-11 | SRC016 | Kiefer_CEJ_2024_MW_CO2 | extraction (workflow 0.7 + CO2 metrics): extraction.md, evidence.csv (E001-E032, E041-E046), calculations.py (C001-C006), short_summary.txt; ai_checked | Claude Code 2.1.322 | claude-opus-5-5 | d3b811d6 | |
| 2026-11-12 | SRC025 | Kungas_JES_2020_SOEC_CO2 | benchmark folder set up (PDF copied from literature_reviews/); extraction (workflow 0.7, R1-R4): extraction.md, evidence.csv (E001-E022, E041-E042), calculations.py (C001-C003), short_summary.txt; ai_checked. Nernst conversion bound tried at BB's suggestion and removed (bound >99% at operating voltages, not informative) | Claude Code 2.1.322 | claude-opus-5-5 | d3b811d6 | |
| 2026-11-12 | SRC026 | Hecimovic_JCOU_2024_MW_vs_Electrolysis | benchmark: published version downloaded from KIT repository; extraction (workflow 0.7, R1-R4): extraction.md, evidence.csv (E001-E021, E041-E043), calculations.py (C001-C004), short_summary.txt; ai_checked | Claude Code 2.1.322 | claude-opus-5-5 | d3b811d6 | |
| 2026-11-12 | SRC017 | Hecimovic_JCOU_2023_MW_Quench_CO2 | extraction (workflow 0.7 + CO2 metrics): extraction.md, evidence.csv (E001-E022, E041-E043), calculations.py (C001-C005), short_summary.txt; ai_checked. Finding: reported efficiencies ~9-10% above X*dH/SEI on the stated 20 C flow basis (E019) | Claude Code 2.1.322 | claude-opus-5-5 | d3b811d6 | |
| 2026-11-12 | SRC016 | Kiefer_CEJ_2024_MW_CO2 | revision: cross-reference to SRC017 (same torch; flow basis) added to extraction.md | Claude Code 2.1.322 | claude-opus-5-5 | d3b811d6 | |
| 2026-11-12 | SRC018 | Bongers_PPP_2017_MW_CO2 | extraction (workflow 0.7 + CO2 metrics): extraction.md, evidence.csv (E001-E017, E041-E043), calculations.py (C001-C004), short_summary.txt; ai_checked. Early View version; text eta 40% at 10 kW conflicts with Fig. 3b (~36%) | Claude Code 2.1.322 | claude-opus-5-5 | d3b811d6 | |
| 2026-11-12 | SRC019 | GirardSahun_CEJ_2022_GA_CarbonBed_CO2 | extraction (workflow 0.7 + CO2 metrics): extraction.md, evidence.csv (E001-E018, E041-E044), calculations.py (C001-C005), short_summary.txt; ai_checked. Finding: reported 45.4% credits 283 kJ/mol while net reaction is CO2 + C -> 2CO (recalc ~28%); peak is transient (<3.5 min) | Claude Code 2.1.322 | claude-opus-5-5 | d3b811d6 | |
| 2026-11-12 | SRC020 | OModhrain_ACSEngAu_2024_MultiGA_CO2 | extraction (workflow 0.7 + CO2 metrics): extraction.md, evidence.csv (E001-E017, E041-E043), calculations.py (C001-C003), short_summary.txt; ai_checked. Plug-power basis; PSU 77-83% measured; 1-node text SEI inconsistent with Fig. 3a | Claude Code 2.1.322 | claude-opus-5-5 | d3b811d6 | |
