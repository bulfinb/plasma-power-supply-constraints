# Plasma reforming: benchmark-oriented download shortlist

Prepared 2026-10-29. Purpose: select experimental demonstrations for the extraction workflow, prioritising useful scale, integration and energy reporting over small-cell plasma-effect studies. Geng (2022, plasma SMR) is already extracted and is not counted here. The electrically heated benchmarks are also extracted: From (2024, Topsoe eSMR pilot plant on biogas, SRC005) as the primary Joule-heated benchmark and Wismann (2019, lab-scale Joule-heated SMR, SRC001) as its complement.

This is a screening shortlist, not a completed extraction or a verified ranking of efficiencies/technology readiness. Citations and selection indicators were checked against publisher pages, author-hosted papers or institutional records. Most full manuscripts and ESI have not yet been audited. Performance maxima are separate reported indicators unless explicitly matched; power ratings, absorbed power and total plant electricity must remain distinct. SMR, DRM and mixed steam/CO2 reforming are separate comparison groups.

## First download batch: scale and process engineering

### 1. Akande and Lee (2022) - SMR, microwave torch

**Plasma steam methane reforming (PSMR) using a microwave torch for commercial-scale distributed hydrogen production.** International Journal of Hydrogen Energy 47(5), 2874-2884.

- DOI/publisher: https://doi.org/10.1016/j.ijhydene.2021.10.258
- Screening evidence: https://www.sciencedirect.com/science/article/pii/S0360319921043688
- Author paper copy: https://www.greenscience.com.au/_files/ugd/ff5f0c_9f52c16a44294f9eb41e710c0b18d050.pdf
- Reported experimental range: microwave power 15-50 kW, total feed 240-420 L/min. Reported optimum H2 output 2247 g/h; energy yield based on absorbed microwave power. A 75 kW generator rating is not the experimental operating range.
- Why prioritise: strong scale anchor for SMR, with reactor geometry, steam supply and downstream heat recovery/separation described. Separate experiments from ASPEN simulations. The authors' commercial-scale wording does not establish commercial deployment or long-term reliability.

### 2. Surov et al. (2017) - AC thermal plasma, mixed reforming/hardware

**Multi-gas AC plasma torches for gasification of organic substances.** Fuel 203, 1007-1014.

- DOI: https://doi.org/10.1016/j.fuel.2017.02.104
- Screening evidence: https://www.sciencedirect.com/science/article/pii/S0016236117302569
- Reported hardware programme: AC torches covering 5-500 kW; paper includes methane reforming as well as solid-fuel gasification.
- Why prioritise: connects reforming to developed high-power arc hardware and thermal losses/lifetime. Extract the actual methane-test power and feed, not the maximum torch-family rating. Torch thermal efficiency and electrode life must not be presented as whole-reformer efficiency or continuous methane-test duration.

### 3. Rutberg et al. (2015) - mixed steam/CO2 thermal-plasma reforming

**Conversion of methane by CO2 + H2O + CH4 plasma.** Applied Energy 148, 159-168.

- DOI: https://doi.org/10.1016/j.apenergy.2015.02.087
- Screening evidence: https://www.sciencedirect.com/science/article/abs/pii/S0306261915002731
- Reports methane conversion 91-98.3% and energy consumption per mass of converted methane; discusses heat losses and volumetric thermal-energy loading. Verify actual measured power/throughput in the downloaded experimental section before assigning a scale.
- Why prioritise: process-performance counterpart to the high-power thermal-plasma literature; useful for heat-loss and reactor-intensification analysis. Chemistry is mixed steam/CO2 reforming, not pure SMR. Check overlap with Surov before treating as independent evidence.
- Useful hardware companion (optional extra download): Rutberg et al. (2015), **AC plasma torch with a H2O/CO2/CH4 mix as the working gas for methane reforming**, Journal of Physics D: Applied Physics 48, 245204. https://doi.org/10.1088/0022-3727/48/24/245204 . Publisher full text was inaccessible during screening; scale claims for this companion are not validated here.

### 4. Choi, Han, Shim and Moon (2025) - microwave steam plasma, SMR

**Methane steam reforming for eco-friendly H2 production using atmospheric-pressure microwave steam plasma.** Current Applied Physics 75, 8-14.

- DOI: https://doi.org/10.1016/j.cap.2025.04.005
- Institutional screening source: https://pure.jbnu.ac.kr/en/publications/methane-steam-reforming-for-eco-friendly-hsub2sub-production-usin/
- Reports an optimum at 6 kW and S/C 4.7, with plasma reforming and plasma/catalytic combinations.
- Why prioritise: recent multi-kW SMR study that can connect plasma heat supply, catalyst integration and conversion. Audit total energy, carbon balance and product destination; lower CO2 in the outlet alone does not establish lower life-cycle emissions or better reforming efficiency.

### 5. Czylkowski et al. (2016) - combined steam/CO2 reforming, microwave

**Microwave plasma-based method of hydrogen production via combined steam reforming of methane.** Energy 113, 653-661.

- DOI: https://doi.org/10.1016/j.energy.2016.07.088
- Screening evidence: https://www.sciencedirect.com/science/article/pii/S0360544216310131
- Reports 2.45 GHz excitation, up to 6 kW absorbed power and total working-gas flow up to 9000 NL/h. These maxima should not be assumed to describe the same point without extraction.
- Why prioritise: multi-kW/high-flow scale anchor; useful for later microwave supply/coupling assessment. Despite the title, feed includes CO2 and steam: keep separate from pure SMR.

### 6. Czylkowski et al. (2024) - DRM, 915 MHz microwave

**Microwave plasma-assisted hydrogen production via conversion of CO2-CH4 mixture.** International Journal of Hydrogen Energy, pp. 421-432, published 12 August 2024.

- DOI: https://doi.org/10.1016/j.ijhydene.2024.06.313
- Screening evidence: https://www.sciencedirect.com/science/article/pii/S0360319924025539
- Atmospheric-pressure, high-flow 915 MHz source; reported best H2 production rate 156 g/h and best energy yield 24 g/kWh. These are separate maxima, not necessarily matched. Exact operating power/flow range to verify from full text.
- Why prioritise: a useful comparison with the 2.45 GHz work, particularly for coupling and scale-up. Different chemistry and operating conditions prevent attributing performance differences to frequency alone.

## Second batch: targeted integration/intensification comparisons

### 7. Kwon, Kim and Song (2023) - DRM, rotating gliding arc and quench

**Dry reforming of methane in a rotating gliding arc plasma: Improving efficiency and syngas cost by quenching product gas.** Journal of CO2 Utilization 70, 102448.

- DOI: https://doi.org/10.1016/j.jcou.2023.102448
- Screening evidence: https://www.sciencedirect.com/science/article/pii/S2212982023000598
- AC apparatus with a supply capable of 2 kW; methods show a 1.8 kW setpoint example, 20 kHz, total feed 24 SLPM including N2. Do not equate rating/setpoint with measured discharge power. Authors report an efficiency improvement through quenching.
- Why prioritise: system-level selectivity control can improve useful product yield even when conversion falls. Include quench/cooling energy and distinguish the author's LHV-based efficiency from our power-basis metrics and HHV efficiency.

### 8. Zhu et al. (2019) - SMR, gliding arc plus insulated catalyst bed

**Plasma catalytic steam methane reforming for distributed hydrogen production.** Catalysis Today 337, 69-75.

- DOI: https://doi.org/10.1016/j.cattod.2019.05.015
- Screening evidence: https://www.sciencedirect.com/science/article/abs/pii/S0920586119302329
- Reports 3 SLM total inlet feed, 90% methane conversion, 2.7 SLM total-H2 output at optimum conditions, and six-hour steady operation. Uses a Ni/CeO2/Al2O3 bed in a heat-insulated reactor without extra heating.
- Why include despite smaller scale: directly addresses the intended synergy of plasma chemistry, thermal utilisation and catalytic intensification. The author's total-H2 metric and reported 75% efficiency require definition/boundary checking, not direct adoption as our efficiency.

### 9. Xu et al. (2024) - DRM, post-plasma catalyst-bed design

**Improving the performance of gliding arc plasma-catalytic dry reforming via a new post-plasma tubular catalyst bed.** Journal of CO2 Utilization 83, 102820.

- DOI: https://doi.org/10.1016/j.jcou.2024.102820
- Author-hosted full text: https://medialibrary.uantwerpen.be/files/7783/2ec1c127-6097-43c0-bad3-0e0e4983acdc.pdf
- Institutional copy: https://backoffice.biblio.ugent.be/download/01J9V140H3TNXQMTVZRBQ5Y8KJ/01J9V16XQQWR459HDNM9SYW29D
- Table 1 reports 508 W, 8 L/min total flow and CH4/CO2 conversions 91%/79%. Feed is highly N2-diluted (methods baseline N2:CH4:CO2 = 8:1:1). Methods' quoted current/voltage do not obviously reproduce Table 1's 508 W; retain this for cross-checking.
- Why include despite sub-kW scale: deliberate post-plasma heat/mass-transfer integration, with no extra heating or insulation of the new post-plasma bed. High conversion is not by itself proof of nonthermal chemistry. The paper explicitly points to its ESI; the group publication list links supplementary material.

## Download and cross-check instructions

1. Download manuscript and every available ESI/supplement/data file. Keep supplements in the format supplied (some, such as Geng's ESI, are DOCX) and add a PDF export for page-number citation if needed. Not every paper has ESI; record 'none located' rather than assuming it exists.
2. Name folders as specified in workflow.md (FirstAuthor_Journal_Year_ShortTopic). Distinguish the two Czylkowski papers and any related Rutberg/Surov papers. Do not assign extraction evidence IDs until analysis starts.
3. Apply workflow.md. First human checks: actual measured plasma power versus generator rating, methane input versus total/diluted feed, conversion at the matched condition, extra heat/steam inputs, author efficiency equation/boundary, and actual steady time on stream.
4. Keep each paper's numerical maxima separate until matched conditions are confirmed. Our shortlist indicators are screening aids, not approved benchmark data.
5. In particular, check the Akande energy-yield basis, the actual methane-run scale in Surov/Rutberg, the total-H2 definition in Zhu, and the electrical/flow basis in Xu. Record human checks as human_verified only for the quantities actually checked.

Suggested initial SMR extraction order: Akande (2022), Choi (2025), Zhu (2019). Then use the mixed-reforming/thermal-arc and DRM papers as separate benchmark groups. This shortlist deliberately omits pyrolysis-only demonstrations, oxygen-assisted partial oxidation and process-modelling-only papers from the endothermic experimental comparison.
