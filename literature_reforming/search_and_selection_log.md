# Search and selection log

Kept as specified in literature_search_strategy.md ("Simple search and selection records"). One file for both tables; do not keep duplicate logs elsewhere.

Started 2026-11-05. Searcher: Claude (AI), at BB's request. No independent duplicate screening has been done.

## Search log

Round 1 (2026-11-05) aim: a fresh start, ignoring benchmark_reading_shortlist.md. Looking for plasma reforming demonstrations beyond proof of concept: kW-scale or integrated systems that report conversion together with an energy metric.

Discovery route: Claude's web search tool (a general web search engine, about 10 results returned per query). **Not** Scopus, Web of Science or Google Scholar; database searches with the Boolean strings in the strategy are still to be run where TCD access allows. All returned results were screened by title/snippet; promising records were followed up on publisher, repository or author pages.

| Search ID | Date | Database / discovery route | Exact query or seed paper | Fields / filters | Results returned | Results screened / stopping rule | Notes |
|---|---|---|---|---|---|---|---|
| S001 | 2026-11-05 | Web search tool | plasma steam methane reforming hydrogen kW scale energy efficiency conversion experimental | none | 10 | all 10 | Mostly partial oxidation (MIT plasmatron) and pyrolysis; none eligible |
| S002 | 2026-11-05 | Web search tool | dry reforming of methane plasma high energy efficiency high conversion gliding arc plasmatron energy cost | none | 10 | all 10 | Cleiren 2017, Slaets 2020, Kwon 2023 |
| S003 | 2026-11-05 | Web search tool | microwave plasma dry reforming methane atmospheric pressure kW conversion energy cost kJ/mol | none | 10 | all 10 | Kelly 2023, Wanten 2022; 6 kW microwave DRM cited second-hand (original not identified) |
| S004 | 2026-11-05 | Web search tool | rotating gliding arc plasma methane reforming syngas energy efficiency long-term stability | none | 10 | all 10 | Kwon 2023 again; no long-duration tests found |
| S005 | 2026-11-05 | Web search tool | thermal plasma torch methane CO2 reforming conversion energy efficiency syngas pilot | none | 10 | all 10 | Hrabovsky 2018 (PLASGAS), Song 2020 (ICP torch), Korean landfill-gas demonstration plant |
| S006 | 2026-11-05 | Web search tool | demonstration-scale plasma gas reforming syngas methanol plant methane conversion 95.1% CO2 conversion 30.5% | none | 10 | all 10 | Follow-up of S005; only a secondary student article found |
| S007 | 2026-11-05 | Web search tool | Hrabovsky steam plasma methane reforming hydrogen production Plasma Chemistry and Plasma Processing water stabilized torch | none | 10 | all 10 | Confirms Hrabovsky 2018 citation; full text not retrieved |
| S008 | 2026-11-05 | Web search tool | microwave plasma steam reforming methane hydrogen production kW energy yield g/kWh conversion | none | 10 | all 10 | Czylkowski 2016; Hrycak 2023 |
| S009 | 2026-11-05 | Web search tool | KAIST inductively coupled plasma torch dry reforming CO2 CH4 30 kW 95% conversion energy conversion efficiency | none | 10 | all 10 | Song 2020 metadata |
| S010 | 2026-11-05 | Web search tool | microwave plasma dry reforming 6 kW 96.8% CH4 conversion 68.4% CO2 atmospheric pressure | none | 10 | all 10 | Original of the 6 kW result not identified |
| S011 | 2026-11-05 | Web search tool | gliding arc plasma catalytic steam reforming methane hydrogen energy efficiency hours stability distributed hydrogen | none | 10 | all 10 | Zhu 2019 |
| S012 | 2026-11-05 | Web search tool | Kelly Bogaerts microwave plasma dry reforming methane Journal of CO2 Utilization 2023 carbon formation energy cost | none | 10 | all 10 | Kelly 2023 (open access); Biondo 2023 |
| S013 | 2026-11-05 | Web search tool | plasma biogas dry reforming kW scale long-term operation hours syngas energy efficiency experimental | none | 10 | all 10 | Nothing new eligible |
| S014 | 2026-11-05 | Web search tool | Wanten atmospheric pressure glow discharge dry reforming confining plasma 94% CH4 conversion Journal of CO2 Utilization 2022 | none | 10 | all 10 | Wanten 2022 metadata |
| S015 | 2026-11-05 | Web search tool | microwave plasma torch steam methane reforming commercial-scale distributed hydrogen production 50 kW | none | 10 | all 10 | Akande 2022 |
| S016 | 2026-11-05 | Web search tool | DC thermal plasma jet CO2 reforming of methane conversion energy efficiency kW Tao International Journal of Hydrogen Energy | none | 10 | all 10 | Only a conference abstract (Sun, ICOPS 2010) |
| S017 | 2026-11-05 | Web search tool | Czylkowski microwave plasma biogas steam reforming hydrogen 239 g/h 36.8 g/kWh 74.3% methane conversion | none | 10 | all 10 | Hrycak 2023 full text read (PMC) |
| S018 | 2026-11-05 | Web search tool | Lee Kwak Chang "Study on CH4 dry reforming process by high power inductively coupled plasma torch at atmospheric pressure" Current Applied Physics 2020 | none | 10 | all 10 | First author is Song |
| S019 | 2026-11-05 | Web search tool | plasma reforming methane hydrogen experimental long duration test 100 hours arc plasmatron steam or CO2 reforming energy efficiency | none | 10 | all 10 | No eligible long-duration test found |
| S020 | 2026-11-05 | Web search tool | Hrabovsky Hlina Maslani steam plasma methane reforming water argon stabilized arc 110 kW methane CO2 conversion energy hydrogen ISPC | none | 10 | all 10 | Power 88-136 kW, CH4 75-150 slm (repository abstract) |
| S021 | 2026-11-05 | Backward citation search | Kelly et al. (2023) SRC011, Table 1 and Section 3.2 (MW plasma DRM literature) | none | 6 MW DRM reports in Table 1 | all 6 | Identified R015 (Chun 2017); new R018 (Sun 2021), R019 (Chun 2019, with catalyst) |

## Selection log

Title/abstract decisions are from abstracts, repository records or the first pages of full text. "Full-text decision" is pending for every record until the PDF has been read against the criteria.

| Record ID | Citation / DOI | Search IDs | Title/abstract decision | Full-text decision | Reason / qualifying experiments | Screener / date | Checker / date | Included source ID |
|---|---|---|---|---|---|---|---|---|
| R001 | Hrabovsky et al. (2018) Plasma Chem. Plasma Process. 38, 743-758. 10.1007/s11090-018-9891-5 | S005, S007, S020 | include | include (full text read 2026-11-05; no ESI located) | Steam (and CO2) reforming of CH4 in a DC water/argon-stabilized arc, 88-136 kW, CH4 75-150 slm | Claude / 2026-11-05 | | SRC007 |
| R002 | Akande & Lee (2022) Int. J. Hydrogen Energy 47, 2874-2884. 10.1016/j.ijhydene.2021.10.258 | S015 | include | include (full text and corrigendum read 2026-11-05; results internally inconsistent, see SRC008 extraction) | SMR in a 915 MHz microwave torch, 15-50 kW absorbed; flag: reported H2 rate exceeds stoichiometric limit for the stated CH4 flow (see shortlist) | Claude / 2026-11-05 | | SRC008 |
| R003 | Song, Lee, Kwak & Chang (2020) Curr. Appl. Phys. 20, 196-204. 10.1016/j.cap.2019.10.023 | S005, S009, S018 | include | include (full text read 2026-11-05; no ESI located) | DRM in a 400 kHz ICP torch, up to 30 kW; ~95% conversion, author ECE 57% at 22 kW | Claude / 2026-11-05 | | SRC009 |
| R004 | Hrycak et al. (2023) Sci. Rep. 13, 2204. 10.1038/s41598-023-29433-y | S008, S017 | include | include (full text read 2026-11-05; no ESI located) | Steam reforming of synthetic biogas (mixed route), 915 MHz, 4.5-6.5 kW absorbed | Claude / 2026-11-05 | | SRC010 |
| R005 | Kelly et al. (2023) J. CO2 Util. 75, 102564. 10.1016/j.jcou.2023.102564 | S003, S012 | include | include (full text read 2026-11-05; no ESI located) | DRM in 2.45 GHz microwave plasma, ~1 kW absorbed (six-port reflectometer); energy cost and carbon formation | Claude / 2026-11-05 | BB / 2026-11-10 | SRC011 |
| R006 | Czylkowski et al. (2016) Energy 113, 653-661. 10.1016/j.energy.2016.07.088 | S008 | include | pending | Combined steam/CO2 reforming, 2.45 GHz, up to 6 kW absorbed, 42.9 g H2/kWh | Claude / 2026-11-05 | | |
| R007 | Zhu et al. (2019) Catal. Today 337, 69-75. 10.1016/j.cattod.2019.05.015 | S011 | include | include (full text and ESI read 2026-11-05) | Gliding arc + Ni catalyst SMR, insulated, no extra heating; author efficiency 75% | Claude / 2026-11-05 | | SRC012 |
| R008 | Kwon, Kim & Song (2023) J. CO2 Util. 70, 102448. 10.1016/j.jcou.2023.102448 | S002, S004 | include | include (full text and ESI read 2026-11-05) | DRM in rotating gliding arc with product quench, ~1.7 kW, 50% N2; author efficiency 55.3% (= our eta_P,LHV); EC_CH4 740-948 kJ/mol | Claude / 2026-11-05 | | SRC014 |
| R009 | Wanten et al. (2022) J. CO2 Util. 56, 101869. 10.1016/j.jcou.2021.101869 | S003, S014 | include | include (full text and ESI read 2026-11-05) | DRM in confined DC APGD, ~0.1 kW; 94% CH4 / 64% CO2 conversion, author 3.5-4.2 eV/molecule; EC_CH4 813-1194 kJ/mol; 300 kOhm ballast dissipates 1.6-2.6x the plasma power | Claude / 2026-11-05 | | SRC015 |
| R010 | Cleiren et al. (2017) ChemSusChem 10, 4025-4036 (volume/pages from memory; confirm). 10.1002/cssc.201701274 | S002 | include | pending | DRM in gliding arc plasmatron; 66% efficiency at low conversion | Claude / 2026-11-05 | | |
| R011 | Slaets et al. (2020) Green Chem. 22, 1366-1377 (volume/pages from memory; confirm). 10.1039/C9GC03743H | S002 | include (N2-only runs) | pending | DRM with N2 in gliding arc plasmatron; O2-addition runs excluded as oxidative | Claude / 2026-11-05 | | |
| R012 | Biondo et al. (2023) Green Chem. (reverse-vortex microwave DRM, carbon deposition). DOI to confirm (RSC article D3GC03595F) | S012 | include | pending | DRM microwave plasma, ~14 kJ/L at 1:1 | Claude / 2026-11-05 | | |
| R013 | Emerging Investigators article 23-252 (plasma landfill-gas reforming, demonstration methanol plant, Daegu) | S005, S006 | pending | pending | Secondary source analysing plant data; primary plant report and whether O2 is fed are unknown. Find the primary source | Claude / 2026-11-05 | | |
| R014 | Sun et al. ICOPS 2010 abstract 2P-75 (DC plasma jet DRM) | S016 | exclude | | Conference abstract only; insufficient methods | Claude / 2026-11-05 | | |
| R015 | Chun, Hong & Choi (2017) J. CO2 Util. 19, 221-229 ("Reforming of methane to syngas in a microwave plasma torch at atmospheric pressure"); DOI to confirm | S003, S010, S021 | include | pending | Identified via Kelly 2023 Table 1 ref. [15]: 2.45 GHz MW torch, 6 kW, 30 L/min, 50:50 CO2/CH4, 68/97% conversion, ~3.6 eV/molecule | Claude / 2026-11-05 | | |
| R016 | Cohn/Bromberg MIT plasmatron reformer reports | S001, S019 | exclude | | Partial oxidation (oxidative reforming) | Claude / 2026-11-05 | | |
| R017 | Masláni et al. / VTT, methane in thermal steam plasma (pyrolysis) | S001, S020 | exclude | | Pyrolysis to H2 and carbon black, not reforming | Claude / 2026-11-05 | | |
| R018 | Sun, Lee & Bak (2021) J. CO2 Util. 46, 101464 ("Experiments and modeling of atmospheric pressure microwave plasma reforming of a methane-carbon dioxide mixture"); DOI to confirm | S021 | include | pending | Surface-wave MW DRM, 2 kW, 10 L/min, 50:50, 91/96% conversion, ~3.2 eV/molecule (per Kelly Table 1) | Claude / 2026-11-05 | | |
| R019 | Chun, Shin, Ma, Yang & Hong (2019) Catalysts 9, 292 ("CO2 microwave plasma-catalytic reactor for efficient reforming of methane to syngas") | S021 | include | pending | MW torch 3 kW, 30 L/min, with and without downstream Ni catalyst; 33/43% to 69/81% conversion; carbon deactivation reported (per Kelly Table 1) | Claude / 2026-11-05 | | |
| R020 | Andersen, Christensen, Østberg, Bogaerts & Jensen (2020) Chem. Eng. J. 397, 125519 ("Plasma-catalytic dry reforming of methane: Screening of catalytic materials in a coaxial packed-bed DBD reactor"); DOI 10.1016/j.cej.2020.125519 (Crossref-confirmed) | user request 2026-11-05 (DBD example) | include | include (full text and ESI read 2026-11-05) | Non-thermal packed-bed DBD DRM, 45 W, no external heating; EC_CH4 ~8-10 MJ/mol, author eta ~4%; no plasma-catalyst synergy; complements Geng 2022 (DBD SMR) | Claude / 2026-11-05 | | SRC013 |
