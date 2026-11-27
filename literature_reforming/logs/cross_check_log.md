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

Actions without a name were decided by Claude; BB's decisions are marked (BB, date). BB's checks are also recorded in ../../human_checks/summary.csv.

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
| SRC011 Kelly 2023 | 2026-11-20 | Codex desktop (version not recorded) | as above | 0.9 | manuscript |
| SRC014 Kwon 2023 | 2026-11-20 | Codex desktop (version not recorded) | as above | 0.9 | manuscript and SI (pdf, docx) |
| SRC003 Lewis (NETL) 2022 | 2026-11-20 | Codex desktop (version not recorded) | as above | 0.9 | report, Case 1 only; fired reference (R1-R4) |
| SRC009 Song 2020 | 2026-11-20 | Codex desktop (version not recorded) | as above | 0.9 | manuscript (no ESI) |
| SRC015 Wanten 2022 | 2026-11-20 | Codex desktop (version not recorded) | as above | 0.9 | manuscript and SI (pdf, docx) |
| SRC001 Wismann 2019 | 2026-11-20 | Codex desktop (version not recorded) | as above | 0.9 | manuscript and supplementary |
| SRC012 Zhu 2019 | 2026-11-20 | Codex desktop (version not recorded) | as above | 0.9 | manuscript and ESI |
| SRC013 Andersen 2020 | 2026-11-20 | Codex desktop (version not recorded) | as above | 0.9 | manuscript and ESI. Not strictly blind: our extraction was the worked example until its outputs were removed for this run |
| SRC027 Kaufmann 2026 | 2026-11-26 | Codex desktop (version not recorded) | GPT-6.1 Sol (user specified) | 0.9 | manuscript (no ESI); DRM runs only; GPT saw Wanten SRC015 outputs as context, not our SRC027 files |

## Summary by paper

- **SRC008 Akande 2022** (2026-11-20): the 32 kW / 60 lpm CH4 / S/C 3 point is identical: X_CH4 96.6%, SEI_CH4 717 kJ/mol and EC_CH4 742 kJ/mol on absorbed microwave power, with steam-generator duty not reported. The corrigendum composition point (62 lpm) is also identical, at SEI_CH4 694 kJ/mol. Both found independently that the reported 2247 g H2/h (and 70 g/kWh) exceeds what 60 lpm CH4 can give (~1190-1295 g/h at complete SMR + WGS). Both found that Fig. 10 conflicts with the reported conversion. Differences XR001-XR002.
- **SRC004 Collodi (IEAGHG) 2017** (2026-11-20): Base Case design reference agrees on every value: 100,000 Nm3/h H2 (8,994 kg/h); CH4 feed ~21,600 mol/min; net CH4 conversion 84.6% over pre-reformer and reformer; radiant duty 96.1 MW, giving EC_CH4,abs 315-316 and EC_CH4,fired 574 kJ/mol (HHV); plant eta_HHV 81.1% (LHV ratio 75.9%); f_electric 0 with 9.918 MWe export; author metric 14.212 GJ LHV/1000 Nm3 H2. Both note that the 28 bar HTS-inlet pressure is not the tube pressure, and both label the case a design basis, not measured data. Difference XR003.
- **SRC005 From 2024** (2026-11-20): all reported values agree: 97% CH4 conversion at 900 degC, 10 barg, S/C 2.7 (start-up from 645 degC, steady after 2.3 h); 94 +/- 1% at 950 degC, 20 barg at TOS 485 and 1535 h (no deactivation; the 1050 h between them included other operating scenarios, as GPT notes); author reactor efficiency ~72% at ~25 kW and ~80% at ~35 kW (Fig. 5, I x V boundary, including sensible heating 400 -> 900 degC). Both find that point-matched power, CH4 feed and composition are not reported, so EC_CH4 is NR. Difference XR004.
- **SRC006 From 2025** (2026-11-20): same four conditions (numbered differently) with identical values: regulated run at 900 degC, 6 barg, 6.4 Nm3/h biogas, 80 h, module 1.99; unregulated run at 950 degC, 10 barg, 6.3 Nm3/h, 20 h; Table 2 cases at module 2.00 and 2.02. Both find no power or energy data (confidential). CH4 feed for the unregulated run: ours 2.67 mol/min (57.1% CH4), GPT 2.53-2.72 (54-58%), consistent. Difference XR005.
- **SRC002 Geng 2022** (2026-11-20): all shared values agree. CH4 conversion is ~7% plasma-off, ~60% at 15 W (300 degC) and ~80% at 15 W (440 degC); discharge power comes from the Q-V loop with frequency NR. EC_CH4 is ~1490 vs ~1468 kJ/mol at 300 degC and ~1120 vs ~1101 at 440 degC; the ~1.5% spread comes from the feed derivation. EY_H2 is 14.8-16.2 and 19.8-21.6 g/kWh, H2 selectivity 88% (not an efficiency), carbon recovery ~90%, and the runs last ~2 h. The unclear feed wording was resolved independently to the same ~1.0e-3 mol/min CH4: ours via the water feed and S/C 4.4, GPT via 25 mL/min CH4 at 25 degC. Both flag the printed balance/selectivity equations as inconsistent with the values. Furnace and steam duties are NR in both. Difference XR006.
- **SRC007 Hrabovsky 2018** (2026-11-20): same four test segments, with the same feeds and arc powers: SMR 150 and 75 slm CH4 at 120 kW; CO2-fed 125 slm CH4 at 116 and 88-89 kW. Fig. 8 has a 325 A segment at 88 kW and a later one at 89 kW; we use the later one. SEI_CH4 on arc power is identical (1076 / 2152 / 1248 / 947-958 kJ/mol). The author H2 costs are identical: 79 (conclusion) vs 86 (results) MJ/kg process basis, 116 MJ/kg CO2-fed, 192 MJ/kg on arc power. Torch efficiency is 0.57-0.60, plasma steam comes from the torch, there is no external heater, and the segments are minutes long (not endurance). GPT labels the CO2-fed runs "mixed" (CO2 plus torch steam); ours "DRM (+plasma H2O)". Difference XR007.
- **SRC010 Hrycak 2023** (2026-11-20): same three Table 1 points with identical reported values (X_CH4 48.9 / 66.1 / 74.3%; H2 239 / 234 / 171.5 g/h; EY 36.8 / 36.1 / 26.4 g/kWh at 6.5 kW absorbed), steam-vaporizer duty NR in both. GPT inferred the authors' molar volume from their own numbers (XR008), which changed our energy values. Our carbon-closure check (now 71-79%) has no counterpart in GPT's extraction.
- **SRC011 Kelly 2023** (2026-11-20): the two end points of the CH4:CO2 series agree exactly at 1 kW absorbed, 10 L/min and the authors' 24.05 L/mol:
  - CH4:CO2 = 3:7: X_CH4 66.5%, X_CO2 49.4%, SEI_CH4 481 kJ/mol, EC_CH4 723 kJ/mol;
  - CH4:CO2 = 4.5:5.5: X_CH4 55.2%, X_CO2 45.8%, SEI_CH4 321 kJ/mol, EC_CH4 581 kJ/mol.
  Also identical: the author energy cost (2.8 / 3.0 eV per molecule converted), the exhaust temperatures 726 / 677 K (thermocouple, not plasma), water inferred from the O deficit (13.6 / 6.7%), and the atom-selectivity sums (C 0.94, H 1.04). GPT notes that the reported total conversion (53.5 / 49.6%) differs slightly from re-weighting the individual values (54.5 / 50.0%), within the stated errors. Difference XR009.
- **SRC014 Kwon 2023** (2026-11-20): the same three 1.67 kW points (no quench, quench, quench at CH4:CO2 1:1) agree: X_CH4 ~52 / 51.1 / 50.5%, SEI_CH4 450 / 450 / 374 kJ/mol, EC_CH4 865-869 / 880 / 740 kJ/mol, and author efficiency 55.3 / 53.2%. Both use 22.414 L/mol; ours notes that it reproduces the author efficiency. Both flag the 50% N2 dilution in the authors' per-litre costs and that water is inferred from the atom balance. GPT also notes the peak efficiency is given once as 55.6% and elsewhere as 55.3%. Difference XR010.
- **SRC003 Lewis (NETL) 2022** (2026-11-20): Case 1 (no capture) agrees on every value:
  - scale and conditions: 20,126 kg/h H2; primary-reformer CH4 feed ~59,970 mol/min; 871 degC and 28.3 bar abs at the reformer outlet; reformer CH4 conversion 77.7%;
  - heat basis: Q_abs 264.3 MW gives EC_CH4,abs 340 kJ/mol; Q_fired 447-448 MW HHV gives EC_CH4,fired 576-577 kJ/mol;
  - plant: eta_HHV 75.7% with f_electric 1.2% (12.65 MWe grid, mostly H2 compression); author CGE 76.7% and ETE 75.4%; export steam ~143 MW, not credited.
  H2 purity differs only in source: ours is the 99.90 vol% minimum specification (Exhibit 2-10), GPT's the modelled 0.9998 in stream 12. Both are stated in the report. No differences needing action.
- **SRC009 Song 2020** (2026-11-20): the three shared points agree. At 22 kW, CO2/CH4 30/20 SLM: X 98 / 88.7%, EC_CH4 1510 kJ/mol, author efficiency ~47%. At 22 kW, 30/36: X 79 / 87%, EC_CH4 1036-1040 kJ/mol, author efficiency 57% (the headline, which goes with 79% CH4 conversion, not the abstract's 95%). At 27 kW, 30/30: X 94 / 94%, EC_CH4 1288 kJ/mol. Both flag the contradictory power boundary (captions say absorbed; the text says delivered, not absorbed), the unresolved Ar flow during reforming, and that the author efficiency includes C2 products. Ours adds a 21 kW point. GPT rates energy confidence lower, ours moderate. No differences needing action.
- **SRC015 Wanten 2022** (2026-11-20): GPT's three cases match three of our six at the authors' 24.05 L/mol:
  - 25% CH4, 35 mA, 1 L/min: X ~85 / ~55%, ~143 W, SEI_CH4 827-829 kJ/mol, EC_CH4 970-975 kJ/mol;
  - 35% CH4, 25 mA, 0.5 L/min: X ~87 / ~66%, ~105 W, EC_CH4 988-990 kJ/mol;
  - 25% CH4, 25 mA, 0.5 L/min: X 94.28 / 63.7%, ~96-97 W, EC_CH4 1173-1194 kJ/mol (the spread is the Fig. 4 SEI reading).
  Both note that the author cost is per CO2+CH4 converted (not EC_CH4), that the 300 kOhm ballast dissipates 188-368 W, outside the plasma power, and that water is inferred from the O balance. GPT rates conversion confidence moderate, ours higher. No differences needing action.
- **SRC001 Wismann 2019** (2026-11-20): conversions agree: 92.7% at 340 and 85.0% at 1700 Nml/min total feed (CH4/H2O/H2 30/60/10, 50 mbarg); GPT adds 91.6% at 1020 Nml/min. CH4 feed is 4.6e-3 and 2.3e-2 mol/min at 22.414 L/mol; GPT notes that the authors' industrial 50,000 Nm3/h = 2230 kmol/h implies ~22.42 L/mol, supporting the 0 degC reference. Both find no point-matched electrical power, so energy metrics are NR, and both note the averaging over at least 45 min (not endurance). Exit wall temperature at 1700 Nml/min: ours ~780 degC, GPT ~775 degC (within reading precision). No differences needing action.
- **SRC012 Zhu 2019** (2026-11-20): the two 246 W, 3 SLM, S/C 3 points agree: plasma alone X_CH4 65%, EC_CH4 679 kJ/mol; with the Ni-Ce catalyst X_CH4 90%, EC_CH4 490 kJ/mol; SEI_CH4 441 kJ/mol. Also identical: author efficiency 59% and 75% with 2.3 and 1.5 kWh/Nm3 (both on "total H2" = H2 + CO, not actual H2), bed temperature 977 -> 651 degC, and the 6 h stability test (ESI). Steam-vaporizer duty is excluded in both. Ours adds the 149 and 206 W points at 2.5 SLM. No differences needing action.
- **SRC013 Andersen 2020** (2026-11-20): the shared Table 3 rows agree exactly at 45 W plasma power and 24.46 L/mol:
  - plasma only: X 32.6 / 22.4%, EC_CH4 8103 kJ/mol, author E 0.206 mmol/kJ, eta 4.44%;
  - Pt: X 32.5 / 22.1%, EC_CH4 8128 kJ/mol, author eta 4.39%;
  - Cu: X 32.6 / 16.1%, EC_CH4 8103 kJ/mol, author eta 3.43%.
  Also identical: the C/H/O closure ranges 88-90 / 83-88 / 88-92% and the 5 x 1 h cycling. GPT notes that the printed Eq. (7) seems to omit the factor 0.5 for the equimolar feed, although the reported values reproduce; author values are kept in both. No differences needing action.

- **SRC027 Kaufmann 2026** (2026-11-26): the shared Fig. 13b points agree on supply-side values at 22.414 L/mol (both assumed; SLM reference not stated, +9.1% at 24.46): 50/50 low group X_CH4 ~42%, SEI_supply ~6.0 kJ/L, EC_CH4 640 kJ/mol; 50/50 top group X ~66 / ~70%, 15.9 kJ/L, EC_CH4 1080; 60/40 top group X_CH4 ~52-52.5%, 12.3 kJ/L, EC_CH4 1313-1325. Both read the author maxima 68 / 60% as plasma-basis (x ~1.06), the author 3.3-4.7 eV as per CO2 + CH4 converted (not EC_CH4), the driver efficiency 88-94% as source-wide, the supply boundary as not wall plug, alpha as a fitted correlation and the runs as 2-5 min. Both decline to equate the quoted 1660 W with the ~1590 W supply power implied by SEI x flow at the top point (our C004). Differences XR011-XR015.

## Differences

| ID | Date | Source / record | Ours | GPT | Checked against PDF | Action |
|---|---|---|---|---|---|---|
| XR001 | 2026-11-20 | SRC008 corrigendum composition point (62 lpm, 32 kW): conversion | 83.1%, from the carbon basis of the wet composition (no soot), EC_CH4 835 kJ/mol | unclear; residual CH4 fraction not taken as conversion, EC_CH4 NR | both defensible: ours is a labelled reviewer calculation that assumes no solid carbon (none observed) and no unmeasured carbon species | kept ours (conditional, labelled) |
| XR002 | 2026-11-20 | SRC008 operating points | power scan 17, 32, 47 kW at S/C 3 (EC_CH4 511, 742, 1078 kJ/mol) | S/C 5 at 32 kW (X 99.8%, EC_CH4 719 kJ/mol) | different points from the same figures, consistent | kept ours (noted) |
| XR003 | 2026-11-20 | SRC004 reformer catalyst | NR | nickel (Annex I) | GPT right: Annex I PDF p. 259 states the reformer and pre-reformer catalysts contain nickel | corrected (E051; summary table) |
| XR004 | 2026-11-20 | SRC005 Fig. 5 endpoint points: flow and CH4 feed | biogas 15 and 27 Nm3/h assigned to the ~25 and ~35 kW endpoints, giving CH4 5.6-8.4 and 10.0-15.1 mol/min (labelled reviewer interpretation) | flows not mapped to endpoints; CH4 feed NR | the paper gives the 15-27 Nm3/h range for the cohort, not per point; not settled by the PDF | kept ours (labelled assumption); for human check. Resolved (BB, 2026-11-27): flows mapped in order to the end points, read as total process gas (biogas + steam); CH4 feed revised to 2.7-6.0 mol/min (SRC005-C006, E046) |
| XR005 | 2026-11-20 | SRC006 regulated run: conversion | X_CH4 ~98%, X_CO2 ~42-54% and O/C, H/C closure within 0.3% (labelled reviewer calculations from Table 1 and the Fig. 5C inlet ratio) | NR; residual CH4 0.24% not taken as conversion | ours is a conditional calculation; the authors report no conversion | kept ours (labelled reviewer calculation) |
| XR006 | 2026-11-20 | SRC002 operating points | plasma-off, 15 W at 300 and 440 degC (plus 20 W ~74% noted in text) | adds Al2O3-only 15 W (~30%, EC_CH4 ~2935), Ni 10 W (~50%, ~1174) and the Cu cascade (no EC: power not restated) | consistent with the paper; the S/C 4.4 vs Fig. 3 caption 4.5 noted by GPT | kept ours (noted) |
| XR007 | 2026-11-20 | SRC007 conversion and EC_CH4 per segment | X_CH4 91.3 / 99.1 / 95.3 / 83.3% (X_CO2 91.0 / 89.0) from digitised MS traces with the 50 slm Ar tracer; EC_CH4 1179 / 2172 / 1309 / 1149 kJ/mol; carbon closure 94-101% | conversion not reconstructed from gas fractions; EC_CH4 NR; uses the authors' conversion-vs-enthalpy points instead (~99-99.5%) | the paper states the Ar is a tracer added to determine the outlet flow (PDF p. 13), and our values match the authors' plotted points (95.8 / 91.5 vs 95.3 / 91.0; 82.7 / 88.8 vs 83.3 / 89.0) | kept ours (labelled reviewer calculation, cross-checked); for human check, as it underpins the only large thermal-arc EC_CH4 BB 2026-11-26: Ar-tracer mass balance agreed (human check). |
| XR008 | 2026-11-20 | SRC010 molar volume for NL flows | 22.414 L/mol (0 degC) assumed; EC_CH4 238 / 264 / 471 kJ/mol; H2-anchored X 2-4 points above the authors' | 24.25 L/mol inferred: the authors' H2 rate, composition and conversion imply 24.246 / 24.251 / 24.255 L/mol in the three rows; EC_CH4 258 / 286 / 509 | GPT right: at 24.25 L/mol our own H2-anchored conversion equals the authors' in all three rows; workflow section 4 prefers the molar volume that reproduces the authors' derived values | corrected (+8.2% on SEI_CH4 and EC_CH4; carbon closure 71-79%; also power_systems wall-basis table) Endorsed by BB, 2026-11-20. |
| XR009 | 2026-11-20 | SRC011 operating points and confidence | four points of the CH4:CO2 series; conversion and energy confidence higher | the two end points only; confidence moderate | consistent; confidence is a judgement call (no repeats count stated, water and carbon inferred) | kept ours (noted) |
| XR010 | 2026-11-20 | SRC014 operating points and closure wording | adds the 0.92 kW quench point (X ~26%, EC_CH4 948); C closure "~100%"; pressure ~1.01 bar assumed | three 1.67 kW points; closure "partial" (sums use inferred water); pressure NR | consistent; GPT's closure wording is the more careful | kept ours (noted) |
| XR011 | 2026-11-26 | SRC027 power basis of the selected points | plasma basis as headline (EC_CH4 574 / 971 / 1178 kJ/mol); SEI_P text-reported at OP002 (14.3 kJ/L), interpolated at OP001/OP003 with the endpoint ratio 0.897 (C001) | supply basis only (640 / 1080 / 1325); no point plasma power inferred from the source-wide 88-94% | the text gives SEI_P only at the two SEI endpoints (p. 13); our ratio lies inside the stated driver range, and the headline OP002 needs no interpolation | kept ours (labelled reviewer calculation; supply values listed alongside) |
| XR012 | 2026-11-26 | SRC027 OP001 geometry | 20 mm, 0.24 A | lower-power pairing of geometry and current with Fig. 13b not explicit; no per-OP voltage or current assigned | Fig. 13a inset '20 mm, 0.24 A' is joined by a leader line to the 50/50 point at ~6.0 kJ/L, X_tot ~40%, which Fig. 13b group 1 matches; P/I ~2.2 kV agrees with the 2200 V quoted for 20 mm at 0.24 A (p. 7) | kept ours |
| XR013 | 2026-11-26 | SRC027 operating points | three points (50/50 low, 50/50 top, 60/40 top) | adds the 60/40 low group (SEI_supply ~6.5 kJ/L, X_CH4 ~43%, S_C,CO ~95%, EC_CH4 847 supply) | consistent with Fig. 13b | kept ours (noted) |
| XR014 | 2026-11-26 | SRC027 bar readings | X_CO2 ~38.5% (50/50 low); X_CH4 ~52.5% (60/40 top) | ~38%; ~52% (EC_CH4 1325 vs 1313) | within the +-1 point reading precision both state | kept ours |
| XR015 | 2026-11-26 | SRC027 appraisal | Q1 yes, Q4 partly, Q6 NA, Q8 no, Q9 yes | Q1 partly, Q4 no, Q6 no, Q8 partly, Q9 partly | Q4: S_C,CO is a selectivity, not a closure, and no C/H/O balance is reported, so GPT is right. Q6: no catalyst, so NA per workflow section 5. Q1, Q8, Q9 are judgement calls (both boundaries measured with probes; 2-5 min stated without a steady-state criterion; no external heat) | corrected Q4 to no; others kept ours |

## Closing summary (reforming, 2026-11-20)

- **Sources:** all 15 were extracted a second time by GPT-6.1 Sol (Codex) under workflow 0.9. Fourteen were blind; Andersen only partly, as it had been the worked example.
- **Differences logged:** XR001-XR010.
- **Corrections to our extractions:** two.
  - Collodi: nickel catalyst added (XR003).
  - Hrycak: molar volume changed from 22.414 to 24.25 L/mol, which reproduces the authors' own H2 rates and conversions. EC_CH4 rose ~8%, and the scale-up table was updated (XR008).
- **For human check:**
  - From 2024: assignment of the biogas flows to the Fig. 5 end points (XR004).
  - Hrabovsky: tracer-based conversion behind the only large thermal-arc EC_CH4 (XR007).
- **Kept ours:** the other differences were operating-point choices or labelled reviewer calculations (XR001, XR002, XR005, XR006, XR009, XR010).
- **Confirmed independently:**
  - Akande's H2 output exceeds what its methane feed can give.
  - The From papers give no matched power and feed.
  - Geng's feed is 25 mL/min CH4 (also confirmed by BB).
  - Song's 57% efficiency goes with 79% conversion, not the abstract's 95%, and its power boundary is contradictory.
  - Wismann reports no electrical power.
- **Pattern:** GPT tends to rate confidence one level lower where water or carbon is inferred rather than measured. This is worth harmonising in the human checks.
- **Status:** all sources remain ai_checked; human verification is still pending.

## Addendum (SRC027 Kaufmann 2026, 2026-11-26)

- **Differences logged:** XR011-XR015.
- **Corrections to our extraction:** one, in the appraisal: Q4 balance closure changed from partly to no (XR015). No values change.
- **Kept ours:** plasma-basis headline with labelled interpolation at OP001/OP003 (XR011), OP001 geometry (XR012), point choice and readings (XR013, XR014).
- **Confirmed independently:** EC_CH4 on the supply side (640 / 1080 / ~1320 kJ/mol), the plasma-basis reading of the author maxima, the combined-reactant author cost, and the unresolved 1660 W vs SEI x flow power.
- **Status:** ai_checked; human verification pending.
