# Plasma CO2 splitting shortlist, round 1

Prepared 2026-11-11 by Claude (AI). Candidates for the 5-10 exemplary studies ([literature_review_objectives.md](literature_review_objectives.md), "Review approach"). Searches CS001-CS018 and the record list are in [search_and_selection_log.md](search_and_selection_log.md).

Sources of candidates: the downloaded reviews in [../literature_reviews/](../literature_reviews/) (Bogaerts & Centi 2020, Bogaerts 2025, Osorio-Tejada et al. 2024 Table 1, Li et al. 2025) and a general web search tool (not Scopus or Web of Science). The two field-wide compilations, Snoeckx & Bogaerts 2017 (RV001) and Xu et al. 2025 (RV002), were downloaded by BB on 2026-11-11 and checked the same day (searches CS017-CS018; see "Check against RV001 and RV002" below).

**Status of the numbers.** Every value below is from an abstract, a repository record, a search snippet or a review table. None has been extracted or checked against the full text. Values from snippets are often wrong (see the power-systems re-extraction). They are here only to explain why each candidate is on the list.

**Decision (BB, 2026-11-11): the nine below are approved as the exemplars.** Source folders and IDs:

| # | Folder | Source ID | Manuscript |
|---|---|---|---|
| 1 | Kiefer_CEJ_2024_MW_CO2 | SRC016 | downloaded (published version) |
| 2 | Hecimovic_JCOU_2023_MW_Quench_CO2 | SRC017 | published version + ESI (BB) |
| 3 | Bongers_PPP_2017_MW_CO2 | SRC018 | downloaded (published version) |
| 4 | GirardSahun_CEJ_2022_GA_CarbonBed_CO2 | SRC019 | published version + ESI (pdf, docx) (BB) |
| 5 | OModhrain_ACSEngAu_2024_MultiGA_CO2 | SRC020 | published version + ESI (BB) |
| 6 | Bryssinck_RCE_2025_GA_Pilot_CO2 | SRC021 | **accepted author version** (UAntwerp repository, 32 pp.) + ESI (BB); typeset version not obtained |
| 7 | Renninger_JCOU_2022_Glow_CO2 | SRC022 | published version (BB) |
| 8 | Yong_PSST_2023_NRP_CO2 | SRC023 | published version (BB); OSTI preprint removed |
| 9 | VanLaer_EnergyTechnol_2015_DBD_CO2 | SRC024 | downloaded (published version) |

Save downloads as `manuscript.pdf` (and `ESI.pdf` or `SI.pdf`) in the folder. SHA-256 of the copies, 2026-11-11 (Kiefer, Bongers, Van Laer fetched by Claude; the rest downloaded by BB; repeat in each extraction.md):

- Kiefer: `ef2d75a234e020e0ccd58a4e711e871a8bc3c94e6b6982ada4f16a188bb9a3f2`
- Bongers: `2cbc559513744bdb1b0436bd8d2212ed48973a5d1cd351a5cc16f2fd59e8ab98`
- Van Laer: `8bb54c87724d300c58a602e7fe427c713c7e7ccef7ebfcf86992841bd925395a`
- Hecimovic: `006cc945c8a63fc31b286a2e4a85c72fb7fefd42753e69fbfe670c0a0ef33a12`; ESI `93374f9d12943b461f63236d68f8be55a15d683ab888fa3852538cd230e135d3`
- Girard-Sahun: `a40b795fc3d6969065327d7db150d6d3b010f42ad08f06338f041e9d229356d6`; ESI.pdf `b9ae0df7447f1f822e5e2a0aad7c18736cc33a86a19184401666f263a2b9afeb`; ESI.docx `cbf96e65b8ce77115e69396cef3688e794bb2bd6954cdc628e48eef5c9210a44`
- O'Modhrain: `5c2a2c08094372e9b68d51fcd5292350ed3ed5dfa80e05d7e43b310ce07f4b61`; ESI `ac09d5bb3899c0957b59e9340cc7f54e9523a38e5d7b1b80d9fe62d383f23972`
- Bryssinck (author version): `e77e09c9b846b887bd2bd6e4f5c09da60645cc669e4c33e7086060707322437e`; ESI `af298f14bd33b805c504dabf1529dc1ef2cd53e919c30b5f46babab9b168b078`
- Renninger: `6be9fbbe56afe64cbd461ce8df74903ee16d2a1485051771bb889ca354e9f304`
- Yong: `10b1090a3866cb8d6f81055e4ebe5c7cdd58ac87fff4634b103f75133e86d92e`

## Selection criteria

1. Matched conversion and efficiency: both reported at the same operating point, with a stated power measurement. High conversion counts as much as high efficiency.
2. Spread across plasma types (microwave, gliding arc, glow, nanosecond pulsed, DBD) and pressures.
3. Scale: kW-level or multi-reactor and pilot systems preferred.
4. Post-plasma steps that change conversion or separation (quenching, carbon bed, recirculation).
5. Access: open access or repository copy available.

## Proposed exemplars (nine)

### 1. Kiefer et al. (2024): microwave torch, 2.45 GHz, 0.1-1 bar, "in view of industrial application"

Kiefer, Antunes, Hecimovic, Meindl & Fantz. *CO2 dissociation using a lab-scale microwave plasma torch: an experimental study in view of industrial application.* Chem. Eng. J. 481 (2024) 148326. https://doi.org/10.1016/j.cej.2023.148326

- IPP Garching / Augsburg. Pressure scan from about 100 mbar to atmospheric. Impurity tolerance also tested (N2 improves efficiency; H2O the exception, from a conference abstract).
- Why: the microwave work most directly framed for industry, near atmospheric pressure, from the group whose quenching results are cited by Bogaerts 2025.
- Access: **downloaded** (Augsburg repository copy of the published version, CC BY; page 1 is the repository cover sheet, the article starts on PDF page 2).

### 2. Hecimovic et al. (2023): microwave, reverse vortex with cooled effluent channels, near 1 bar

Hecimovic, Kiefer, Meindl, Antunes & Fantz. *Fast gas quenching of microwave plasma effluent for enhanced CO2 conversion.* J. CO2 Util. 71 (2023) 102473. https://doi.org/10.1016/j.jcou.2023.102473 (citation from Crossref; the 57% at 900 mbar result is confirmed in the abstract of this paper).

- Up to 57% conversion at 900 mbar, at SEI above 5.5 eV/molecule. The earlier nozzle study (Hecimovic, D'Isa, Carbone & Fantz 2022) raised conversion at 4.7 slm from 5% to 35%.
- Why: the high-conversion end for microwave near atmospheric pressure. Efficiency will be modest at that SEI, which is the point of including it.
- Access: gold open access (CC BY-NC-ND), but ScienceDirect blocked the script. **BB to download.**

### 3. Bongers et al. (2017): microwave, vortex, up to 8 kW, sub-atmospheric with quenching

Bongers et al. *Plasma-driven dissociation of CO2 for fuel synthesis.* Plasma Process. Polym. 14 (2017) e1600126. https://doi.org/10.1002/ppap.201600126

- DIFFER. Osorio-Tejada et al. 2024 (Table 1) list one point: 11 slm, 8 kW, SEI 44 MJ/m3, efficiency 22%, conversion 83%, at 20 kPa. Gas temperature above 4000 K, so dissociation is mainly thermal.
- Why: kW-scale microwave, with the highest conversion found. **Flag:** 200 mbar, so vacuum pumping is outside the power boundary (strategy: eligible but flagged).
- Access: **downloaded** (published version, University of Twente repository).

### 4. Girard-Sahun et al. (2022): gliding arc plasmatron with a post-plasma carbon bed

Girard-Sahun et al. *Carbon bed post-plasma to enhance the CO2 conversion and remove O2 from the product stream.* Chem. Eng. J. 442 (2022) 136268. https://doi.org/10.1016/j.cej.2022.136268

- 10 L/min, 530 W. Efficiency 27.9% to 45.4% and conversion 7.6% to 12.6% with the bed (Osorio-Tejada Table 1). O2 removed from the product. The early gain fades as the bed deactivates (time-resolved data).
- Why: the basis of the Osorio-Tejada techno-economic plant, and the clearest case of a post-plasma step that changes separation. Carbon is consumed, so it is not pure CO2 splitting; the carbon input must be counted.
- A 2025 J. Energy Chem. follow-up (bed size and insulation) reports 41% conversion and 51% efficiency at high SEI, with a revised efficiency definition. Consider it as an alternative or companion.
- Access: Maastricht University repository holds the published version but blocked the script (HTTP 403). **BB to download.**

### 5. O'Modhrain et al. (2024): multi-reactor gliding arc plasmatron, plug-power basis

O'Modhrain, Trenchev, Gorbanev & Bogaerts. *Upscaling plasma-based CO2 conversion: case study of a multi-reactor gliding arc plasmatron.* ACS Eng. Au 4 (2024) 333-344. https://doi.org/10.1021/acsengineeringau.3c00067

- Several plasmatrons in parallel in one housing. Conversion 9% and efficiency 19% on a **plug-power basis**, at SEI around 5.3 kJ/L (1 eV/molecule).
- Why: one of very few papers reporting efficiency from the wall plug, which is the review's boundary. Parallel scale-up, as in the D-CRBN pilot.
- Access: gold open access (CC BY-NC-ND); ACS and PubMed Central blocked the script. **BB to download** (plus Supporting Information).

### 6. Bryssinck et al. (2025): gliding arc pilot reactor with carbon bed and recirculation

Bryssinck, Smith, O'Modhrain, Van Assche, Trenchev, Bogaerts et al. *Performance of a gliding arc plasmatron pilot reactor with an integrated carbon bed and recirculation* (title truncated in Crossref; check). React. Chem. Eng. 10 (2025) 1910-1923. https://doi.org/10.1039/D5RE00190K

- Pilot reactor. Maximum conversion 20%. Recirculation raised the energy cost from 10.9 to 13.7 MWh/t CO.
- Why: the largest-scale gliding arc data found, with recirculation (overall conversion) and energy per tonne CO. Close to the D-CRBN design.
- Access: RSC blocked the script; only an accepted manuscript is listed (VUB repository, returned HTTP 503). **BB to download** the published version and ESI.

### 7. Renninger et al. (2022): DC atmospheric-pressure glow discharge, optimised reactor

Renninger, Stein, Lambarth & Birke. *An optimized reactor for CO2 splitting in DC atmospheric pressure discharge.* J. CO2 Util. 58 (2022) 101919. https://doi.org/10.1016/j.jcou.2022.101919 (University of Stuttgart). Earlier paper: Renninger, Lambarth & Birke, *High efficiency CO2-splitting in atmospheric pressure glow discharge*, J. CO2 Util. 42 (2020) 101322.

- 43% efficiency at 27% conversion (efficiency "in the plasma"), up to 220 W. The authors state that kW-scale scale-up is feasible. The earlier Renninger et al. 2020 paper reports a **system** efficiency of up to 22%, and 20% conversion at 14.4%.
- Why: the best matched conversion and efficiency found at 1 bar. It reports both plasma and system power boundaries.
- Access: subscription only, no open copy found. **BB to download** (TCD library).

### 8. Yong, Zhong, Pannier, Laux & Cappelli (2023): nanosecond repetitively pulsed discharge, up to about 6 bar

*High-pressure CO2 dissociation with nanosecond pulsed discharges.* Plasma Sources Sci. Technol. 32 (2023) 115012. https://doi.org/10.1088/1361-6595/ad066e (first author Yong, per Crossref; the arXiv v1 lists Pannier first).

- Batch reactor. Best case: 14% conversion, 23% efficiency at 5.8 bar. Efficiency about 20% below 15% conversion, with little sensitivity to pressure.
- Why: the only nanosecond-pulsed candidate with both metrics, and above atmospheric pressure. **Flag:** batch, not flow; SEI is defined per batch.
- Access: only a pre-publication version obtained (OSTI, 34 pp., saved as preprint_OSTI.pdf; arXiv v1 not kept). IOP blocked the script. **BB to download** the published version.

### 9. Van Laer & Bogaerts (2015): packed-bed DBD (ZrO2 beads)

Van Laer & Bogaerts. *Improving the conversion and energy efficiency of carbon dioxide splitting in a zirconia-packed dielectric barrier discharge reactor.* Energy Technol. 3 (2015) 1038-1044. https://doi.org/10.1002/ente.201500127

- Maximum conversion 42%; maximum efficiency 9.6%, at different points. Packing raised conversion by up to 1.9 times and efficiency by up to 2.2 times.
- Why: represents the DBD class, at high conversion and low efficiency. It is included for coverage, not as a scale-up candidate. Alternative: Ozkan et al. 2017 (26% conversion, 20% efficiency per Osorio-Tejada Table 1, which looks high for a DBD and needs checking).
- Access: **downloaded** (published version, University of Antwerp repository).

## Benchmarks and reference systems (selected directly)

| Item | Source | Status |
|---|---|---|
| SOEC CO2 electrolysis | Küngas 2020 (RV006, downloaded); Topsoe slides, DOE HTE workshop 2022: 14,000 h stack test, 30,000 Nm3 CO at 3.44 kWh/Nm3 CO, Faradaic efficiency 99% (stack level, excludes balance of plant). eCOs purity up to 99.995% (Topsoe product page). | Check Küngas for a system-level value |
| Microwave plasma vs LT and HT electrolysis | Hecimovic et al. (2024) J. CO2 Util. 83, 102825, https://doi.org/10.1016/j.jcou.2024.102825. Plasma at about 20 kWh/Nm3 CO, with an added O2-removal step. | Download (open access, KIT repository) |
| Gliding arc plant TEA | Osorio-Tejada et al. 2024 (RV005, downloaded): 100 t CO/day, 19.5 GJ/t CO, assumes 80% plug-to-plasma efficiency. | Read; note it assumes the supply efficiency rather than measuring it |
| H2 + RWGS | Not yet found: a design study with electricity per mol CO. | To search |
| D-CRBN pilot | Bogaerts 2025: 7 gliding-arc reactors of about 1 kW, 100 L/min CO2; "pilot XL" with 18 reactors due 2025. No performance data published. | Reference system only |

## Considered and not proposed (for now)

- **Historical microwave records** (Legasov 1978; Asisov 1983): 80-90% efficiency at 100-200 mbar, supersonic flow. Never reproduced (Bogaerts & Centi 2020). Mention in the narrative only.
- **den Harder et al. 2017; D'Isa et al. 2020; Mitsingas et al. 2016**: microwave results already covered by candidates 1-3.
- **Meng et al. 2023** (AC glow, 12% conversion, 42% efficiency); **Ivanov et al. 2023** (gliding glow); **Vertongen et al. 2023** (comparison of warm plasmas, about 10% conversion at about 30% efficiency): covered by candidates 4-7. Vertongen 2023 is useful context for the narrative.
- **Russian counter-flow quenching study** (Ioffe journals, 3 kW microwave, 43.9% efficiency at 14.3% conversion): language and access to check; a possible alternative to candidate 2.
- **Uytdenhouwen et al. 2019** (micro-DBD, 70% conversion, 0.74% efficiency): an extreme point; may be shown in the plot from a review rather than extracted.
- **Stuttgart 2.45 GHz/915 MHz torch** (DPG 2026 abstract, up to 6 kW, 74 slm): no published results yet.
- **915 MHz cavity up to 10 kW** (AVS 2014 abstract, 15-36% efficiency from 1 to 0.2 bar): conference abstract only.

## Check against RV001 and RV002 (2026-11-11)

Text of both reviews searched for best results by plasma type (Snoeckx & Bogaerts 2017, section 5.1; Xu et al. 2025, "Evaluation of CO2 conversion performance", Fig. 6, and post-plasma section, Fig. 5). Values are as stated in the reviews, not checked against the primary papers.

**Outcome: no change to the nine proposed.** No result in either review beats the nine on matched conversion and efficiency at a credible power boundary. Points that need follow-up:

| Candidate (from) | What the review says | Decision |
|---|---|---|
| Wang, Zhang, Liu & Wang (2012) Plasma Chem. Plasma Process. 32, 979-989 (Xu ref. 98) | Packed-bed DBD with Ca0.8Sr0.2TiO3: conversion 48.71%, efficiency 44.62%, the "optimal balance" in Xu Fig. 6a | **Check full text.** Far above every other DBD result: Snoeckx (2017) gives 42% as the highest DBD conversion and 23% as the highest DBD efficiency. If it holds up (power measurement, gas-expansion correction), it would replace Van Laer & Bogaerts as the DBD exemplar; if not, it is a reporting-quality example |
| Kim, Lim & Chun (2014) Plasma Chem. Plasma Process. 34, 125-143 (Snoeckx ref. 160, Xu ref. 123) | Gliding arc: highest reported GA efficiency, 65% (Snoeckx) or 61.55% (Xu) | Not proposed: conversion not given in either review, likely low. Plot point only; check if a high-efficiency GA point is needed |
| Mercer et al. (2023) Fuel (Xu ref. 109) | Microwave with a converging-diverging nozzle downstream: conversion and efficiency improved together | Alternative to candidate 2 (Hecimovic 2023); same idea (fast quenching near 1 bar) |
| Zhang et al. (2022) ACS Sustainable Chem. Eng. 10, 7712-7725 (Xu ref. 122) | Gliding arc with biochar: conversion 27.1%, efficiency 39.59% | Alternative to candidate 4 (Girard-Sahun); carbon is consumed in both |
| Chen et al. (2017) Appl. Catal. B 214, 114-125 (Xu ref. 112) | Surface-wave microwave + NiO/TiO2: efficiency up to 56% at SEI about 2.9 eV, conversion 45% | Not proposed. **Inconsistent as quoted:** 45% x 2.93/2.9 gives 45% efficiency, not 56%; pressure not stated in Xu |
| Tsuji et al. (2001) Chem. Lett. (Xu ref. 115) | Microwave, conversion up to 92% with Ar dilution | Not proposed: heavy dilution |
| Pandiyan et al. (2022) J. CO2 Util. 57, 101904 (Xu ref. 70) | Microwave plasma followed by an SOEC to convert the CO2/CO/O2 mixture and separate CO and O2 | Not an exemplar; relevant to the SOEC benchmark discussion (plasma-electrolysis hybrid) |
| Kelly, Verheyen, Cowley & Bogaerts (2022) Chem 8, 2797-2816 (Xu ref. 110) | Microwave in simulated Martian atmosphere (about 0.1 atm): 76.1 g/h CO | Not proposed: low pressure, Mars application |
| van Rooij et al. (Xu ref. 117) | Attempt to reproduce the historical high-efficiency microwave results: maximum near 50% | Narrative: supports excluding the Legasov/Asisov records |
| Indarto et al. (2006) (Snoeckx ref. 161) | Gliding arc, 35% conversion with N2 dilution | Not proposed: dilution |

Field-level points useful for the narrative (from Xu Fig. 6 discussion): DBD flow rates are usually below 1 L/min, against up to 75-80 L/min for gliding arc and microwave; mean conversion is highest for microwave (about 34%); GA conversion is usually below 30% at SEI below 4 eV/molecule. Snoeckx (2017) section 6 asks for clear reporting of dilution, gas-expansion correction and which power is reported (applied vs plasma), the same issues as our Q3 check.

## Open points for BB

- Approve, cut or change the nine. Candidates 1-3 are all microwave, at different conversion and pressure points. Candidate 9 (DBD) is included only for coverage.
- Wang et al. (2012) DBD: worth a full-text check now? If its 49%/45% holds, it changes the DBD picture.
