# Plasma reforming shortlist, round 1 (fresh search)

Prepared 2026-11-05 by Claude (AI). Replaces benchmark_reading_shortlist.md as the working list for now; that file is kept unchanged.

Aim: experimental plasma reforming (SMR, DRM, mixed steam/CO2) that goes beyond proof of concept: kW-scale or integrated systems that report conversion together with an energy metric. Searches, screening decisions and the full record list are in [search_and_selection_log.md](search_and_selection_log.md). The search used a general web search tool, not Scopus/Web of Science, so it is a starting set, not a complete search.

Screening values below come from abstracts, repository records or partial full-text reading. None has been extracted or human-verified. Energy metrics marked "screening calc" are rough reviewer estimates to show whether EC_CH4 is likely to be calculable; they are not evidence records.

## Selection criteria used for the five

1. Scale: kW-level measured power, or a clearly integrated system.
2. Energy: power measured at a stated boundary, with conversion reported at the same condition so EC_CH4 is likely calculable.
3. Spread: at least one source per route (SMR, DRM, mixed) and more than one plasma type.
4. Access: full text obtainable (open access, author copy, or TCD library).

## Shortlist (five)

### 1. Hrabovsky et al. (2018) - SMR (with CO2 runs), DC thermal arc, ~90-140 kW

**Steam plasma methane reforming for hydrogen production.** Plasma Chemistry and Plasma Processing 38(4), 743-758. https://doi.org/10.1007/s11090-018-9891-5

- PLASGAS reactor, Institute of Plasma Physics, Prague: DC arc stabilized by argon and a water vortex, giving a steam plasma jet. Torch power 88-136 kW; CH4 75-150 slm; CO2 and water added in some runs (C/O = 1).
- Group reports CH4 conversion up to 99.5%, H2 selectivity up to 99.9%, minimum 158 kJ per mol H2 (from the companion ISPC 2017 abstract; check it is the same data). Syngas flow measured by argon tracer; composition close to equilibrium.
- Why: the largest-power SMR demonstration found, with flow measurement and an energy metric. Check: torch power vs power reaching the reactor (torch efficiency), argon plasma gas in the feed, which runs are pure steam (SMR) and which include CO2 (mixed).
- Access: Springer, paywalled; try TCD library or the Czech Academy repository (ASEP) postprint.

### 2. Akande and Lee (2022) - SMR, 915 MHz microwave torch, 15-50 kW

**Plasma steam methane reforming (PSMR) using a microwave torch for commercial-scale distributed hydrogen production.** International Journal of Hydrogen Energy 47(5), 2874-2884. https://doi.org/10.1016/j.ijhydene.2021.10.258

- Absorbed power from forward minus reflected power; CH4 60 lpm, steam 180-360 lpm; reactor 0.28 m ID x 2.27 m. Conversion 74.6% at 17 kW to 97.7% at 47 kW (S/C 3); 96.6-99.8% at 32 kW for S/C 3-5. Author optimum 2247 g H2/h and 70 g H2/kWh at 32 kW absorbed. No catalyst.
- **Consistency flag:** 60 lpm CH4 (0 degC) is about 161 mol/h, so even full reforming plus shift (4 H2 per CH4) gives at most about 1.3 kg H2/h. The reported 2247 g/h is about 1.7 times that limit (screening calc). Either the optimum used a different CH4 flow (total flow 240-420 lpm is quoted) or the H2 rate is wrong. This must be resolved before any energy metric is used.
- Why: the largest microwave SMR test found, with absorbed power, conversion and energy yield. Kept on the list because the flag itself is a useful finding for the review.
- Access: author copy at https://www.greenscience.com.au/_files/ugd/ff5f0c_9f52c16a44294f9eb41e710c0b18d050.pdf

### 3. Song, Lee, Kwak and Chang (2020) - DRM, inductively coupled plasma torch, 22-30 kW

**Study on CH4 dry reforming process by high power inductively coupled plasma torch at atmospheric pressure.** Current Applied Physics 20(1), 196-204. https://doi.org/10.1016/j.cap.2019.10.023

- 400 kHz ICP torch rated 30 kW (KAIST). CO2 and CH4 conversion about 95%; author energy conversion efficiency 57% at 22 kW, CO2 30 SLM, CH4 36 SLM. Products include C2H6, C2H4, C2H2; C2 selectivity rises with CH4 flow.
- Why: high-power DRM with conversion and an author efficiency at a stated condition. Check: whether 95% conversion and 57% ECE are the same point, the ECE definition, torch plate power vs plasma power, and any sheath/carrier gas (e.g. Ar) in the feed.
- Access: Elsevier, paywalled; TCD library. A related KAIST PhD thesis (2019, koasas.kaist.ac.kr handle 10203/283184) may give more detail.

### 4. Hrycak et al. (2023) - mixed (steam reforming of synthetic biogas), 915 MHz microwave, 4.5-6.5 kW

**Hydrogen production by the steam reforming of synthetic biogas in atmospheric-pressure microwave (915 MHz) plasma.** Scientific Reports 13, 2204. https://doi.org/10.1038/s41598-023-29433-y

- Absorbed power 4.5-6.5 kW; CH4/CO2 3000-12,000 NL/h (40-100% CH4); steam 0.5-3 kg/h at 250-350 degC from an induction vaporizer. Table 1: best 239 g H2/h and 36.8 g H2/kWh at 6.5 kW, 6000 NL/h, 75% CH4, CH4 conversion 48.9%; highest conversion 74.3% at a different point.
- Screening calc: at the 239 g/h point, EC_CH4 is roughly 240 kJ/mol (absorbed microwave power; steam generation excluded), close to the reaction enthalpy. Worth checking carefully.
- Why: biogas feed makes it the closest plasma counterpart to the Topsoe eSMR biogas benchmark (From 2024). Limits: steam generator energy, run duration and carbon balance not reported; soot only qualitative.
- Access: open access (Scientific Reports; PMC9905514).

### 5. Kelly et al. (2023) - DRM, 2.45 GHz microwave, ~1 kW

**Microwave plasma-based dry reforming of methane: Reaction performance and carbon formation.** Journal of CO2 Utilization 75, 102564. https://doi.org/10.1016/j.jcou.2023.102564

- Solid-state 2.45 GHz source; absorbed power measured with a six-port reflectometer (reflected < 1%); about 1 kW and ~10 L/min. Conversion ~46-49% CO2 and ~55-67% CH4 at 30-45% CH4; energy cost ~2.8-3.0 eV/molecule (11.1-11.9 kJ/L). Gas expansion corrected with a measured factor; exhaust temperature measured; carbon particles characterised.
- Why: smaller than the others, but the best-documented energy and conversion measurement found, and it quantifies the carbon-formation problem that limits high-CH4 DRM. Useful as a reporting-quality reference.
- Access: open access (CC BY). Author preprint: https://medialibrary.uantwerpen.be/files/7783/02cdf42b-7ff5-4444-b7f1-edd44c408a29.pdf

## Remaining longlist (reserves)

| Record | Paper | Route / plasma | Why not in the five |
|---|---|---|---|
| R006 | Czylkowski et al. (2016) Energy 113, 653-661 | Mixed, 2.45 GHz microwave, up to 6 kW | Same group and similar scale to Hrycak 2023; the 2023 paper is open access and biogas-relevant |
| R007 | Zhu et al. (2019) Catal. Today 337, 69-75 | SMR, gliding arc + Ni catalyst, insulated, no extra heat | Strong integration case but ~3 SLM feed; first reserve for an SMR plasma-catalysis example |
| R008 | Kwon et al. (2023) J. CO2 Util. 70, 102448 | DRM, rotating gliding arc + quench, ~1.8 kW | Good energy reporting; N2 in feed; overlaps with DRM slots |
| R009 | Wanten et al. (2022) J. CO2 Util. 56, 101869 | DRM, confined APGD | Excellent conversion/energy but lab scale |
| R010 | Cleiren et al. (2017) ChemSusChem | DRM, gliding arc plasmatron | Low conversion; superseded by later work from the same group |
| R011 | Slaets et al. (2020) Green Chem. 22, 1366 | DRM with N2, gliding arc plasmatron | O2 runs ineligible; N2 dilution |
| R012 | Biondo et al. (2023) Green Chem. | DRM, reverse-vortex microwave | Similar to Kelly 2023; could replace it if access or quality differs |
| R013 | Korean landfill-gas plasma reforming demonstration plant (via Emerging Investigators 23-252) | Likely DRM of landfill gas, demonstration scale | Only a secondary source found; primary data and O2 use unknown. Worth chasing: the only demonstration-plant evidence found |
| R015 | Unidentified 6 kW microwave DRM (96.8% CH4, 68.4% CO2) | DRM, microwave | Original paper not yet identified |

## Gaps in this round

- No plasma reforming test with long time on stream (100 h or more) was found; durability is likely to be a major evidence gap.
- Database searches (Scopus/Web of Science) with the strategy's Boolean strings are still needed, followed by backward/forward citation searches from the five.
- Thermal (arc, ICP) and warm (microwave) plasmas dominate the kW-scale results; nonthermal DBD work is almost all small scale.
