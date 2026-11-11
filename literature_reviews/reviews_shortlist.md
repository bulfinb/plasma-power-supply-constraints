# Review papers shortlist (pyrolysis, CO2 splitting and general context)

Version 0.1 - 2026-11-09. Prepared by Claude (AI) at BB's request; candidates, not yet screened in full.

## Purpose

Review papers are used to choose the 5-10 exemplary primary studies per topic (see the "Review approach" sections of [../literature_pyrolysis/literature_review_objectives.md](../literature_pyrolysis/literature_review_objectives.md) and [../literature_co2_splitting/literature_review_objectives.md](../literature_co2_splitting/literature_review_objectives.md)), and to source benchmark data. They are not extracted as evidence. From each, record: the comparison figures or tables of conversion vs energy (by plasma type and scale), the leading primary studies they cite, and the metric conventions they use.

Each review has its own folder, named FirstAuthor_Journal_Year_ShortTopic, with `manuscript.pdf` when available.

## How the candidates were found

2026-11-09, Claude's general web search tool (not Scopus or Web of Science), six queries: plasma methane pyrolysis reviews; Scapinello et al. by name; plasma CO2 splitting reviews 2023-2024; Wanten et al. 2023 by name; natural gas pyrolysis reviews (Schneider et al.); SOEC vs plasma CO2 techno-economics. Plus known reviews from the reforming work (Snoeckx and Bogaerts 2017) and two benchmark reviews chosen directly (Küngas 2020 for SOEC; Daza and Kuhn 2016 for RWGS). Metadata confirmed on Crossref 2026-11-09.

## Download status

Automatic download worked only from repositories and some open publishers; RSC, MDPI, Wiley, ACS and Elsevier pages blocked scripted access (HTTP 403), including for open-access papers. **Please download the papers marked "to download"** into their folders as `manuscript.pdf` (plus any ESI).

| Folder | Status | SHA-256 (downloaded copies) |
|---|---|---|
| Wanten_JEnergyChem_2023_CO2_Metrics | downloaded (published version, University of Antwerp repository) | `b21ec9cdbf31945fb258adeabacdfeb37ba84b92e9ccab0252e48c8258c6440f` |
| Bogaerts_FrontEnergyRes_2020_CO2_Perspective | downloaded (publisher, CC BY) | `2c4555507d97afe8cb4f39c9f8078cab30820a01a9d0cd66420d3055ab9d477a` |
| OsorioTejada_EES_2024_Plasma_vs_Electrolysis_CO | downloaded (published version, Warwick repository, CC BY) | `38c6e2060338921b3a423a4f12b8c9a7e960063a236d5ac80d729769f35c6656` |
| Kungas_JES_2020_SOEC_CO2 | downloaded (publisher, CC BY-NC-ND) | `66a31d7ee6ea60d8e6c17105c24dff11a069d1106e70028ac8da9f2ba25e1e13` |
| Schneider_ChemBioEngRev_2020_NG_Pyrolysis | downloaded (**accepted manuscript**, KIT repository; not the typeset version) | `baa254aa9aed84ade6e665b026ace0a57534730b95d85a67f950ad51382d7e78` |
| Bogaerts_NatChemEng_2025_Plasma_Electrification | downloaded (published version, University of Antwerp repository) | `9afbd0184ce71f867c14d0b1db31914b33365a66efb852e53356481cf2d391a2` |
| Li_FrontChemSciEng_2025_Plasma_Gas_Conversion | downloaded (publisher, CC BY) | `2cb7d774cc7a91df4bbc90e74e8dcae739758829dbd3861ba7ba40aa15427021` |
| vanRooij_PPCF_2018_Plasma_Electrification | downloaded (**author manuscript**, DIFFER repository; not the typeset version) | `8f9dd10c6dfed07356e2974a91fb7bf6b2610dc717a017085a6d5f84653700b5` |
| Snoeckx_ChemSocRev_2017_Plasma_CO2 | downloaded by BB 2026-11-11 (published version, 60 pp.) | `5d4c37c6d310da3ce742b6a8c826648b5f1da4524801b959424777fc525fe213` |
| Xu_GreenChem_2025_LTP_CO2_Dissociation | downloaded by BB 2026-11-11 (published version, 25 pp.) | `6661f1473c769ffe021edca60c96e2f6e67fa0a38a8c59f197fedbde975026a8` |
| Scapinello_CEP_2017_Plasma_NonOxidative_CH4 | to download (subscription) | |
| Wnukowski_Energies_2023_Plasma_Pyrolysis | to download (open access) | |
| Chen_EESCatal_2026_Plasma_CH4_Conversion | to download (open access) | |
| Moghaddam_EES_2025_CH4_Pyrolysis | to download (open access) | |
| Patlolla_RSER_2023_CH4_Pyrolysis | to download (subscription) | |
| SanchezBastardo_IECR_2021_CH4_Pyrolysis | to download (open access) | |
| Daza_RSCAdv_2016_RWGS | to download (open access) | |

## CO2 splitting

| ID | Folder | Citation / DOI | Why | Priority |
|---|---|---|---|---|
| RV001 | Snoeckx_ChemSocRev_2017_Plasma_CO2 | Snoeckx & Bogaerts (2017) Chem. Soc. Rev. 46, 5805-5863. [10.1039/C6CS00066E](https://doi.org/10.1039/C6CS00066E) | The standard field-wide comparison: conversion vs energy efficiency for all plasma types, for CO2 splitting and DRM; defines the efficiency target | high |
| RV002 | Xu_GreenChem_2025_LTP_CO2_Dissociation | Xu et al. (2025) Green Chem. 27, 9332-9356. [10.1039/D5GC02037A](https://doi.org/10.1039/D5GC02037A) | Recent critical review of low-temperature plasma CO2 dissociation with a comparative analysis of plasma technologies; updates RV001 | high |
| RV003 | Wanten_JEnergyChem_2023_CO2_Metrics | Wanten, Vertongen, De Meyer & Bogaerts (2023) J. Energy Chem. 86, 180-196. [10.1016/j.jechem.2023.07.005](https://doi.org/10.1016/j.jechem.2023.07.005) | How to compute conversion and energy metrics correctly (gas expansion); our Q3 check for CO2-splitting exemplars | high (method) |
| RV004 | Bogaerts_FrontEnergyRes_2020_CO2_Perspective | Bogaerts & Centi (2020) Front. Energy Res. 8, 111. [10.3389/fenrg.2020.00111](https://doi.org/10.3389/fenrg.2020.00111) | Perspective on prospects and gaps, including scale-up and comparison with other technologies | medium |
| RV005 | OsorioTejada_EES_2024_Plasma_vs_Electrolysis_CO | Osorio-Tejada et al. (2024) Energy Environ. Sci. 17, 5833-5853. [10.1039/D4EE00164H](https://doi.org/10.1039/D4EE00164H) | Techno-economic and energy-cost comparison of plasma and (low-temperature) electrolysis for CO; includes separation; not SOEC | high (benchmark) |
| RV006 | Kungas_JES_2020_SOEC_CO2 | Küngas (2020) J. Electrochem. Soc. 167, 044508. [10.1149/1945-7111/ab7099](https://doi.org/10.1149/1945-7111/ab7099) | Low- vs high-temperature (SOEC) CO2 electrolysis for CO, by a Topsoe author; source for the SOEC benchmark (eCOs) | high (benchmark) |
| RV007 | Daza_RSCAdv_2016_RWGS | Daza & Kuhn (2016) RSC Adv. 6, 49675-49691. [10.1039/C6RA05414E](https://doi.org/10.1039/C6RA05414E) | RWGS catalysis review: conversion and conditions for the H2 + RWGS benchmark; a design study may still be needed for energy | medium (benchmark) |

## Methane pyrolysis and coupling

| ID | Folder | Citation / DOI | Why | Priority |
|---|---|---|---|---|
| RV008 | Scapinello_CEP_2017_Plasma_NonOxidative_CH4 | Scapinello, Delikonstantis & Stefanidis (2017) Chem. Eng. Process. 117, 120-140. [10.1016/j.cep.2017.03.024](https://doi.org/10.1016/j.cep.2017.03.024) | Plasma non-oxidative methane conversion (pyrolysis and coupling to C2) across plasma types, with energy cost comparisons | high |
| RV009 | Wnukowski_Energies_2023_Plasma_Pyrolysis | Wnukowski (2023) Energies 16, 6441. [10.3390/en16186441](https://doi.org/10.3390/en16186441) | Plasma methane pyrolysis reactors (thermal, warm, non-thermal) and products, including carbon | high |
| RV010 | Chen_EESCatal_2026_Plasma_CH4_Conversion | Chen et al. (2026) EES Catal. 4, 31-54. [10.1039/D5EY00054H](https://doi.org/10.1039/D5EY00054H) | Most recent plasma methane conversion review (COx-free H2, chemicals, carbon materials) | medium |
| RV011 | Schneider_ChemBioEngRev_2020_NG_Pyrolysis | Schneider, Bajohr, Graf & Kolb (2020) ChemBioEng Rev. 7, 150-158. [10.1002/cben.202000014](https://doi.org/10.1002/cben.202000014) | Pyrolysis technologies by TRL, including plasma (Kvaerner, Monolith) and electrically heated routes; industrial context | high (benchmark context) |
| RV012 | SanchezBastardo_IECR_2021_CH4_Pyrolysis | Sánchez-Bastardo, Schlögl & Ruland (2021) Ind. Eng. Chem. Res. 60, 11855-11881. [10.1021/acs.iecr.1c01679](https://doi.org/10.1021/acs.iecr.1c01679) | Broad pyrolysis review (thermal, catalytic, molten media, plasma) with energy comparison against SMR | medium |
| RV013 | Moghaddam_EES_2025_CH4_Pyrolysis | Moghaddam et al. (2025) Energy Environ. Sci. 18, 2747-2790. [10.1039/D4EE06191H](https://doi.org/10.1039/D4EE06191H) | Recent pyrolysis review comparing with SMR and electrolysis; candidates for Joule-heated and industrial benchmarks | medium |
| RV014 | Patlolla_RSER_2023_CH4_Pyrolysis | Patlolla et al. (2023) Renew. Sustain. Energy Rev. 181, 113323. [10.1016/j.rser.2023.113323](https://doi.org/10.1016/j.rser.2023.113323) | Pyrolysis technologies including microwave, plasma and induction heating; reactor designs | low (overlaps RV011-RV013) |

## General context: plasma chemistry at scale

Perspectives used to frame the findings, not to select exemplars. Added 2026-11-09 after three further web searches (plasma chemistry scale-up perspectives 2023-2025; van Rooij et al. by name; scale-up and power supply perspectives).

| ID | Folder | Citation / DOI | Why | Priority |
|---|---|---|---|---|
| RV015 | Bogaerts_NatChemEng_2025_Plasma_Electrification | Bogaerts (2025) Nat. Chem. Eng. 2, 336-340. [10.1038/s44286-025-00229-3](https://doi.org/10.1038/s44286-025-00229-3) | Short comment on cold vs warm/thermal plasmas, reactor scale-up, start-ups and historical pilots (ScanArc, Monolith); figure of best performances by plasma type and process; names power supply matching, heat recovery and gas recycling as scale-up levers | high |
| RV016 | Li_FrontChemSciEng_2025_Plasma_Gas_Conversion | Li, Arun, van den Bogaard, van Raak, Liu & Gallucci (2025) Front. Chem. Sci. Eng. 19, 96. [10.1007/s11705-025-2567-9](https://doi.org/10.1007/s11705-025-2567-9) | Chemical-engineering view (Eindhoven) of experimental methods and trends across CO2 conversion, CH4 activation and N2 fixation; table of reviews 2020-2024 | medium |
| RV017 | vanRooij_PPCF_2018_Plasma_Electrification | van Rooij, Akse, Bongers & van de Sanden (2018) Plasma Phys. Control. Fusion 60, 014019. [10.1088/1361-6587/aa8f7d](https://doi.org/10.1088/1361-6587/aa8f7d) | Older, but the closest to our angle: an industrial process design and cost for microwave plasma CO2 to pure CO, including supply, separation and sub-atmospheric operation; finds separation the dominant cost factor | high |

Suggested reading order: RV001, RV002 and RV003 for CO2 splitting; RV008, RV009 and RV011 for pyrolysis. Lower-priority reviews can be dropped if the high-priority ones give enough candidates.

## Still missing

- A dedicated review or compilation of thermal-plasma/industrial methane pyrolysis energy data (Kvaerner, Monolith, Hüls acetylene). Fulcheri's group (Mines Paris) is the likely source; to search.
- An H2 + RWGS design study with electricity per mol CO (RV007 covers catalysis, not system energy).
