# Plasma power supplies: literature

Started 2026-11-09. Prepared by Claude (AI) at BB's request; status: candidates, not extracted.

## Purpose

Academic papers only (manufacturer and other non-academic data are in [../power_systems/](../power_systems/)). Papers on how the power supply and its matching to the plasma affect the energy balance at scale: wall-plug vs plasma efficiency, supply topologies, numbering-up of reactors on shared supplies, and techno-economic studies showing the supply's share of capital cost. These support the scale-up assessment in each topic folder and complement the representative supply table in [../power_systems/notes/scaleup_assessment.md](../power_systems/notes/scaleup_assessment.md) (which holds supply efficiencies and costs, not plasma papers). One folder per paper, named FirstAuthor_Journal_Year_ShortTopic, with `manuscript.pdf`.

## Papers

| ID | Folder | Citation / DOI | Why | Copy and SHA-256 |
|---|---|---|---|---|
| PS001 | Kiefer_CEJ_2024_MW_CO2_WallPlug | Kiefer, Antunes, Hecimovic, Meindl & Fantz (2024) Chem. Eng. J. 481, 148326. [10.1016/j.cej.2023.148326](https://doi.org/10.1016/j.cej.2023.148326) | 2.45 GHz microwave plasma torch for CO2 splitting (~1-2.7 kW) with the torch and vacuum pump on an energy meter: wall-plug efficiency up to 17.9% (19.6 kWh/Nm3 CO) vs plasma efficiency ~25-27%; breakdown of losses (reflected power, microwave source, vacuum pump); plasma and wall-plug efficiency move in opposite directions with power; 29 h durability test; impurity tolerance. Also a candidate exemplar for literature_co2_splitting | published version (CC BY), Augsburg repository; `ef2d75a234e020e0ccd58a4e711e871a8bc3c94e6b6982ada4f16a188bb9a3f2` |
| PS002 | Baik_IEEETPEL_2026_DBD_PowerElectronics | Baik & Roy, "Review of Power Electronic Solutions for Dielectric Barrier Discharge Applications", IEEE Trans. Power Electron. (conditionally accepted; DOI [10.1109/TPEL.2026.3658517](https://doi.org/10.1109/TPEL.2026.3658517)); arXiv:2512.18067 | Review of DBD supply topologies (resonant inverters, flyback, push-pull, Marx, pulsed) and the capacitive, dynamic load that makes DBD supplies hard to design and scale; replaces the parallel-DBD conference abstract that could not be retrieved (see below) | **arXiv preprint**, not the final published version; `8436fb77895beb06d212e2fd30decb4d96c0e673b27984c75aa040c78d818313` |

## Related perspective

Bogaerts (2025) Nat. Chem. Eng. 2, 336-340 ([../literature_reviews/Bogaerts_NatChemEng_2025_Plasma_Electrification](../literature_reviews/Bogaerts_NatChemEng_2025_Plasma_Electrification), RV015 in [../literature_reviews/reviews_shortlist.md](../literature_reviews/reviews_shortlist.md)) lists "power supply matching" alongside energy-efficiency optimisation as a reactor-design lever (Fig. 2), and states that overall energy efficiency should be optimised by matching the power supply to the plasma, together with heat recovery and gas recycling. It is a short comment, so it names the issue rather than quantifying it.

## Techno-economic assessments: capital cost and the power supply

Academic studies that quantify plasma capital cost and the share taken by the power supply. Values used are in [../power_systems/supply_values.csv](../power_systems/supply_values.csv) under the PS ID.

| ID | Citation / DOI | Why | Copy |
|---|---|---|---|
| PS003 | Lamberts-Van Assche, Thomassen & Compernolle (2022) J. CO2 Util. 64, 102156. [10.1016/j.jcou.2022.102156](https://doi.org/10.1016/j.jcou.2022.102156) | Prospective TEA of DBD plasma CO2 conversion (144 kW); electricity price and power supply investment are the main cost factors (as summarised by Osorio-Tejada 2024); Table 6: power supply €173,000 of €188,143 CAPEX for a 144 kW pilot (~92%; the source of the "€1,300/kW DBD reactor"); supply cost function 1500·kW + 900 € from industry estimates; power source efficiency ~50% (source to plasma). Extracted 2026-11-10 (PS003-V01 to -V05) | browser print of the ScienceDirect full-text web page (`manuscript_html_save_to_pdf.pdf`, 26 pp., no journal page numbers; Elsevier PDF download failed); `a663cea79ac260cb9db7b36bcb783ead9fcf719a78b71e1261548bcd5b2df10f` |
| PS004 | Kaufmann, Rößner, Renninger, Lambarth, Raab, Stein, Seithümmer & Birke (2023) Appl. Sci. 13, 4839. [10.3390/app13084839](https://doi.org/10.3390/app13084839) | TEA of plasma CO2 splitting in power-to-liquid plants (3 MW); Plasma reactor cost functions (DBD 0.05614·P^0.5331, GA 0.1123·P^0.5331 Mio EUR, from PEM electrolyser manufacturing); ~€1,300/kW DBD at 3 MW, taken from PS003; O2 separation (GDE) 30-70% of capex. Extracted 2026-11-10 (PS004-V01 to -V06) | published version (CC BY); `44cdf041db538e9adc37e9a110abeab209b25836472b8b087771532ff1cd24bb` |
| (RV005) | Osorio-Tejada et al. (2024) Energy Environ. Sci. 17, 5833-5853, in [../literature_reviews/](../literature_reviews/reviews_shortlist.md) | Gliding arc power unit + reactor €1,085/kW from an industrial project; lab supplies costly because built for flexibility (p. 5842) | downloaded |
| (RV017) | van Rooij et al. (2018) Plasma Phys. Control. Fusion 60, 014019, in [../literature_reviews/](../literature_reviews/reviews_shortlist.md) | Industrial microwave CO2-to-CO process design and cost, including supply | downloaded |

Bogaerts (2025, RV015, p. 338) states that warm-plasma capital cost is mainly the power supply. The argument about whether supplies are a "niche product", with manufacturer data, is in [../power_systems/notes/supply_maturity_niche.md](../power_systems/notes/supply_maturity_niche.md).

## Not retrieved / further candidates

- APS DPP 2025 abstract on parallel DBD reactors (inconsistent product distribution; power consumption doubled for two reactors; supply capability exceeded for three): the archive page returned "Not Found" and no paper was located. Not included; PS002 covers the supply-side issue.
- Parallel DBD tubes for H2O2 synthesis (Dalian University of Technology, 2009; INIS record): overall efficiency limited by very low supply energy-transfer efficiency; impedance matching proposed. Old and a different chemistry; candidate only.
- Gliding arc numbering-up, series vs parallel gas and electrical connections (Catal. Sci. Technol. 2024, d4cy00655k): candidate; not yet checked.

## Sources of the search

2026-11-09, Claude's general web search tool: Kiefer et al. by author names (from the ESCAMPIG 2024 abstract P71); two searches for parallel DBD reactors and power supply. Metadata from Crossref and arXiv.
