# Industrial power supplies for scaled-up electrified reforming

> Source provenance: every web and manufacturer source cited here is listed in [source_register.csv](source_register.csv) with access date, SHA-256 of the local copy (kept in `source_archive/`, not distributed) and a Wayback Machine snapshot (made 2026-11-09). Sources still to retrieve: [BB_search.txt](BB_search.txt).

Researched 2026-11-05 (Claude Code 2.1.318, claude-opus-5-5; see literature_reforming/processing_log.md). Status: **ai_checked; human verification pending**. Data: [scaleup_supplies.csv](scaleup_supplies.csv). Calculation: [scaleup_wall_basis.py](scaleup_wall_basis.py), output `figures/scaleup_wall_basis.csv`.

## Purpose

The review sources report energy at the discharge, arc, absorbed-microwave or RF-generator boundary, measured with lab supplies. This table asks a different question: if each reactor type were scaled up with a **representative industrially available supply** suited to that discharge, how much electricity would be drawn from the wall, and what are the indicative costs and lifetimes? It is not a benchmark of the supplies used in the papers.

This complements the earlier survey in this folder (`power_sources.csv`, `sources.md`, S1-S17), which maps induction, RF and microwave supplies by frequency and scale. Source IDs S1-S17 refer to that survey; T01-T23 are new.

## Efficiency chain

Wall electricity reaches the reaction through up to four stages; each paper's power boundary sits at a different point in this chain.

| Stage | Symbol | Examples | Where the papers sit |
|---|---|---|---|
| Wall to generator output | eta_supply | rectifier, inverter, magnetron/tube, solid-state amplifier | Discharge-power papers (Kwon, Zhu, Andersen, Geng) and arc-power papers (Hrabovsky) are after this stage |
| Generator output to plasma or heater | eta_couple | reflected power, waveguide, matching network, ballast, coil losses | Absorbed-microwave papers (Kelly, Akande, Hrycak) are after this stage; Song's RF power is before it |
| Plasma to process gas | eta_thermal | torch electrode and wall cooling | Inside arc-power and absorbed-power EC values already |
| Heat integration | NA | steam raising, feed preheat, heat recovery from hot product | Mostly absent in lab tests; present in eSMR and fired SMR |

Indicative wall-basis EC_CH4 = reported EC_CH4 / eta_supply, using the class range in the CSV. eta_couple is not applied separately; this understates wall demand for Song (RF matching and coil losses not included).

## Representative supply classes

| ID | Class | eta (wall to output) | Cost | Lifetime | Main sources |
|---|---|---|---|---|---|
| J1 | Low-voltage high-current AC/DC (Joule) | 0.97-0.99 (reviewer range) | ~15-20% of electrolyser equipment capex; no EUR/kW found | NR | T05, T06, T16 |
| A1 | MW DC rectifier for arc torches | 0.90-0.98 | NR; ballast inductor a large share | electrodes >1000 h (vendor) | T05, T07, T18, T22 |
| R1 | RF tube oscillator (ICP) | ~0.60 | NR | NR | T08 |
| R2 | Solid-state RF | 0.70-0.80 (vendor) | NR | NR | S8, T09 |
| M1 | 915 MHz magnetron, 75-100 kW units | 0.80-0.86 | 1-3 USD/W complete (undated); tube ~0.3 USD/W | tube 2,000-15,000 h | S9, S12, T01, T04, T17 |
| M2 | 2.45 GHz magnetron, 6-30 kW | 0.80-0.85 | NR | tube 2,000-15,000 h | S10, T15, T17 |
| M3 | 2.45 GHz GaN solid-state | 0.56-0.70 (head/amplifier) | 5-10x magnetron per W | long (no tube) | T02, T03, T15 |
| K1 | kHz HV resonant inverter (gliding arc, DBD) | 0.90-0.92 | NR | NR | T07, T10, T11 |
| P1 | Nanosecond pulsed | 0.57-0.98 (load-dependent) | ~5,000 EUR/kW | NR | T12, T13 |

Scale evidence: induction supplies of 16 MW per unit and 126 MW installed (S1); microwave containers of several MW from 100 kW units (S12); Monolith's plasma methane pyrolysis expansion contracted 2,000 GWh/y of electricity, ~228 MW average (T20; reviewer arithmetic). Joule benchmark: Topsoe states its eREACT eSMR needs ~1 kWh per Nm3 H2, ~81 kJ/mol H2 (T21; vendor claim, plant boundary not stated).

## Indicative wall-basis EC_CH4 (scaleup_wall_basis.py)

| Source | Paper boundary | Supply class | EC_CH4 reported (kJ/mol) | EC_CH4 wall (kJ/mol) |
|---|---|---|---|---|
| Hrycak 2023 | absorbed MW (lower bounds) | M1 | 238-471 | 277-589 |
| Zhu 2019 | discharge; steam excl. | K1 | 490-679 | 533-754 |
| Akande 2022 | absorbed MW | M1 | 511-1078 | 594-1348 |
| Kelly 2023 | absorbed MW | M2 magnetron / M3 solid-state | 581-723 | 684-904 / 830-1291 |
| Kwon 2023 | discharge | K1 | 740-948 | 804-1053 |
| Wanten 2022 | plasma; lab ballast excl. | A1 (current-controlled DC) | 813-1194 | 830-1327 (lab ballast incl.: 2392-3490) |
| Song 2020 | RF generator output | R2 solid-state / R1 tube | 1036-1510 | 1295-2157 / 1727-2517 |
| Geng 2022 | discharge; furnace excl. | K1 | 1120-1490 | 1217-1656 |
| Hrabovsky 2018 | arc power | A1 | 1149-2172 | 1172-2413 |
| Andersen 2020 | discharge | K1 | 8103-9712 | 8808-10791 |

Reference lines: SMR 206, DRM 247 kJ/mol CH4. Values exclude steam raising, furnace heat and heat recovery as in the papers. Wanten 2022 used a 300 kOhm series ballast resistor that dissipated 1.6-2.6x the plasma power (SRC015-C005); an industrial glow array would need active current control per discharge instead, so the A1 row assumes that.

## Interpretation (for discussion; human check pending)

1. With industrial supplies, the wall correction is modest (+2-25%) for DC arcs, magnetrons and kHz inverters. It is larger only for RF tube oscillators (~+67%) and 2.45 GHz solid-state (+40-80%). Supply efficiency therefore does not change the broad ranking; the plasma process (regime, heat losses, lack of heat recovery) dominates.
2. The supply choice matters where frequency is forced: ICP torches and 2.45 GHz sources. Industrial microwave scale-up would favour 915 MHz magnetrons (100 kW units, ~85%) over 2.45 GHz solid-state, at the cost of tube replacement every few thousand hours.
3. All plasma wall-basis EC_CH4 values (≥ ~280 kJ/mol) lie above the reaction enthalpy, mainly because hot product heat is not recovered in the tests. Joule-heated eSMR (~81 kJ/mol H2 claimed, cf. plasma EC_H2 ~144-530 kJ/mol on discharge or absorbed basis) shows what heat integration plus a ~98% supply can achieve. Comparing like with like requires adding heat recovery to the plasma cases, which is the next step of the scale-up assessment.
4. Costs are sparse. Only microwave (1-3 USD/W complete, older and undated) and nanosecond pulsed (~5,000 EUR/kW) have figures; rectifier-class supplies are known only as a share of electrolyser capex. Lifetime is a real cost driver for magnetrons (2,000-15,000 h) and torch electrodes (~1,000 h claimed).

## Sources (T01-T23)

| ID | Source | Evidence used | Type |
|---|---|---|---|
| T01 | [Stellant Systems, CWM-100 magnetron sell sheet (2023)](https://stellantsystems.com/wp-content/uploads/2023/10/Magnetron_CWM-100kW_sellsheet_MAY2023.pdf) | 100 kW at 915 MHz, efficiency approaching 86% (tube) | vendor |
| T02 | [IMS 2019, "A Highly Efficient and Compact 6 kW GaN Solid-State Microwave Generator for CW 2.45 GHz"](https://2019.ims-ieee.org/paper_abstract/361) | 56% SSPA head efficiency; 74% transistor | peer-reviewed abstract |
| T03 | [EU CORDIS, CLEAN-HEAT project 666488 reporting](https://cordis.europa.eu/project/id/666488/reporting) | 1 kW GaN SSPA, 70% at 2.45 GHz | project report |
| T04 | [Fermilab partnerships page on magnetrons](https://partnerships.fnal.gov/?p=421) | Complete 915 MHz transmitters ~1-3 USD/W; tubes ~0.30 USD/W; klystrons >5 USD/W | lab web page, undated |
| T05 | [Modern Power Systems, "Grid-friendly rectifiers for hydrogen electrolysers"](https://www.modernpowersystems.com/analysis/hydrogen/grid-friendly-rectifiers-for-hydrogen-electrolysers/) | Thyristor rectifier 99.84%, IGBT 98.5% (vendor comparison); power management ~20% of equipment capex | trade press (vendor) |
| T06 | [Koponen et al., LUT, rectifier topologies for 3 MW electrolyser](https://lutpub.lut.fi/bitstream/10024/162276/1/koponen_et_al_comparison_of_finaldraft.pdf) | Converter ~15% of electrolyser capex; topology affects stack energy | peer-reviewed (accepted draft) |
| T07 | [Institute for Plasma Research, tender technical specification](https://nsd.ipr.res.in/documents/SECTION_C_TECHNICAL_SPECIFICATIONS_IPR_TN_PUR_TP_TET_20_21_5.pdf) | 100 kW IGBT supply: efficiency >=90%, PF >=0.9 (requirement) | tender spec |
| T08 | [Tekna, US 2005/0017646 A1, multi-coil induction plasma torch](https://patentimages.storage.googleapis.com/de/6a/d9/d046db365bf8ea/US20050017646A1.pdf) | Tube oscillator: ~40% of input lost; 20-40% as plasma enthalpy; solid-state limited to ~300-400 kHz | patent background |
| T09 | [TRUMPF TruPlasma RF Series 3000](https://www.trumpf.com/en_SG/products/power-electronics/plasma-excitation/truplasma-rf-series-3000/) | Efficiency "up to 80%" | vendor |
| T10 | IEEE, "Analysis and Assessment of Use of Voltage and Current Inverters Applied to the Ozone Generation in High Frequency" ([record](https://bvbvf1.bib-bvb.de/vufind/PrimoRecord/cdi_ieee_primary_9386269)) | Current-source full-bridge inverter, 91% max electrical efficiency | peer-reviewed (abstract) |
| T11 | IEEE Open J. Power Electronics (2022), Class E DBD supply ([DOAJ](https://doaj.org/article/b984cca08c5c4d7aa7c3612b384ef606)) | 91.5% peak, 600 W at 12-15 MHz | peer-reviewed (abstract) |
| T12 | [TU/e, "Boosting the energy efficiency of a nanosecond pulsed corona plasma system..."](https://research.tue.nl/en/publications/boosting-the-energy-efficiency-of-a-nanosecond-pulsed-corona-plas/) | Reactor efficiency 45 to 85%; system 95-98%; >90% at 20 kW; pulsed power ~5 kEUR/kW | peer-reviewed (abstract) |
| T13 | [Acta Physica Polonica A 115 (2009), ns pulse generator](https://przyrbwn.icm.edu.pl/APP/PDF/115/a115z628.pdf) | 85.2% into resistive load, 56.7% into discharge reactor | peer-reviewed |
| T14 | [van Rooij et al., microwave plasma CO2 (core.ac.uk 43597104)](https://core.ac.uk/download/43597104.pdf) | Microwave supplies ~0.1 EUR/W | peer-reviewed; optimistic |
| T15 | [RF Essentials knowledge base, 2.45 GHz industrial magnetrons](https://rfessentials.com/rf-knowledge-base/what-are-the-rf-design-challenges-for-a-high-power-industrial-magnetron-at-245-g/) | Magnetron life 6,000-15,000 h; solid-state 5-10x cost per W | web, low quality |
| T16 | [EU Clean Hydrogen Observatory, electrolyser cost](https://observatory.clean-hydrogen.europa.eu/hydrogen-landscape/production-trade-and-cost/electrolyser-cost) | Rectifier and transformer counted in balance of plant | agency |
| T17 | [arXiv 2203.07888, magnetrons as RF sources for HEP](https://arxiv.org/pdf/2203.07888) | Lifetimes ~6,000 h or less; cathode sputtering | preprint |
| T18 | [PyroGenesis, TMS 2013 publications extract](https://www.pyrogenesis.com/wp-content/uploads/2019/09/1.-TMS-2013-publications_Pyro-extract.pdf) | Torch thermal efficiency up to 70%; electrodes >1,000 h; 5-500 kW | vendor paper |
| T19 | [University of Toronto CACT, new DC torch design](https://cact.utoronto.ca/?p=6578) | 60-80% torch thermal efficiency | lab web page |
| T20 | [S&P Global (2021), DOE loan guarantee for Monolith](https://www.spglobal.com/market-intelligence/en/news-insights/articles/2021/12/doe-backs-neb-hydrogen-carbon-black-project-with-1b-loan-guarantee-68193136) and NPPD supply reports | 2,000 GWh/y renewable supply for expansion | news |
| T21 | [Topsoe, eREACT for electrifying low-carbon hydrogen](https://knowing-low.topsoe.com/ereact-for-electrifying-low-carbon-hydrogen-production) | ~1 kWh/Nm3 H2 electricity | vendor |
| T22 | [EP 3202234 B1, DC power supply for plasma torches](https://patentimages.storage.googleapis.com/8e/00/03/f0ac29e17ac02a/EP3202234B1.pdf) | 1-10 MW switched DC supplies; ballast inductor a substantial share of investment | patent |
| T23 | Ozone-generator patents found by search: [US 7744825, N-phase ozone generator](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7744825) (multi-tube designs, power factor ~30% at 1 kHz; attribution to this patent to confirm) and [US 4790980](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/4790980) (medium-frequency supply architecture; poor power factor requires oversizing) | DBD low power factor; oversizing | patent background |

All values were taken from search-result summaries and source abstracts or landing pages on 2026-11-05; full texts were not read. Confirm each value against the original before citing, and replace vendor claims with measured data where available.
