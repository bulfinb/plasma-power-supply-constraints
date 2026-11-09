# Are plasma power supplies a "niche product"? Supply maturity, limits and cost

> Source provenance: every web and manufacturer source cited here is listed in [source_register.csv](source_register.csv) with access date, SHA-256 of the local copy (kept in `source_archive/`, not distributed) and a Wayback Machine snapshot (made 2026-11-09). Sources still to retrieve: [BB_search.txt](BB_search.txt).

Moved here from literature_plasma_powersupply/README.md on 2026-11-09 so that manufacturer data sit with the other supply data. Local copies and archive snapshots of D1-D12: see [source_register.csv](source_register.csv).

Added 2026-11-09 (BB, with Claude). Status: argument to develop. Efficiencies come from [scaleup_sources.md](scaleup_sources.md) (T-numbers); the other sources are D1-D12 below. Manufacturer and other non-academic data live in this folder; academic papers on the supply side are in [../literature_plasma_powersupply/](../literature_plasma_powersupply/README.md).

Bogaerts (2025, RV015, p. 338) says that plasma-reactor capital cost is mainly set by the power supply. She calls the supply "still quite expensive today because it is still a 'niche product'", and notes challenges in degradation, reproducibility, control and energy efficiency for MW supplies. The first part, that the supply dominates capital cost, strengthens the case for treating the supply as a design constraint (see Novelty in [../README.md](../README.md)). The "niche product" explanation holds only in part.

**The power-conversion stage is mature elsewhere.** The same supply classes are established products in other industries:

| Supply class | Established use | Typical scale and efficiency |
|---|---|---|
| DC rectifiers | electrolysis, arc furnaces, DC plasma torches | MW to hundreds of MW; ~95-98% |
| kHz resonant inverters | induction heating and melting; industrial ozone generators (D1-D3) | MW-scale; ~90-95% (ozone inverter 91% max, T10) |
| RF tube oscillators, 13.56/27.12 MHz | dielectric heating and welding; semiconductor plasma processing | high-power units ~60-70% |
| Magnetrons, 915 MHz and 2.45 GHz | industrial microwave heating and drying | 915 MHz: ~84-88% (D4); 2.45 GHz: lower |

Ozone generation is a DBD process already run at MW scale on medium-frequency inverters:
- A conventional large unit makes 35 kg/h O3 from a 452 kW supply at about 1 kHz, about 11 kWh/kg (D1).
- Current Wedeco units reach more than 300 kg/h per unit (D2). At about 10 kWh/kg that implies roughly 3 MW per unit (reviewer estimate).

Industrial DBD with efficient power delivery therefore exists. The same patent (D1) also shows the DBD matching problem at scale: the load power factor is about 30%, which forces oversized transformers and inverters. The gap is the energy efficiency of the chemistry, plus reactive-power management, not the supply's conversion efficiency.

**Several limits are physical and will not ease with market volume:**

- **Frequency vs unit power and efficiency.** Semiconductor switching losses rise with frequency. Solid-state supplies are efficient at kHz, while high-power RF still relies on vacuum tubes (~60%).
- **Microwave unit power.** The magnetron cavity scales with wavelength, which caps single-unit power:
  - 915 MHz: 100 kW CW tubes at about 86% (D4).
  - 2.45 GHz: the largest commercial generators found are about 15 kW (D5). Industrial heating sources give about 6 kW per tube and 65-70% efficiency (D6, web, low quality).

  MW plants therefore need many modules. Magnetron cost also rises steeply with unit power (D9).
- **Solid-state microwave efficiency.** At 2.45 GHz, device drain efficiency is about 60-70% for LDMOS and GaN. The best reported 1 kW GaN source reached 70% (D7, D8). This is at device or module level, before the AC/DC stage, so wall-plug efficiency is lower.
- **Lifetime of tubes and magnetrons.** This is a known wear mechanism, not an immature product.

**The genuinely plasma-specific part is matching and control.** Plasma loads have negative differential resistance, an impedance that jumps at ignition and, for a DBD, a capacitance that changes in operation. This leads to reflected power, reactive power and ballast losses (PS002 in [../literature_plasma_powersupply/](../literature_plasma_powersupply/README.md); Wanten 2022, SRC015, where the ballast dissipated 1.6-2.6 times the plasma power).

**Implication.** Supply cost and efficiency are partly set by physics that is already known from mature industries. They can therefore be used now to gate design options: frequency band, unit power, number of modules and wall-to-plasma efficiency can be fixed before the plasma chemistry is assessed. This contrasts with expecting supplies to improve once the market grows. "Niche" fits the coupling and control electronics better than the power-conversion stage.

**Capital cost data found so far.** These are sparse and mostly for supply plus reactor, not the supply alone:

| Basis | Cost | Source |
|---|---|---|
| Gliding arc plasma (power unit + reactor body), industrial CO2 project basis | €1,085 per kW plasma power | D10, p. 5842 |
| Gliding arc 5.6 kW prototype, uninstalled power unit + reactor | €2,400 per kW | D10, p. 5842 |
| DBD plasma reactor, 144 kW and 3 MW designs | €1,300 per kW | as cited by D10, p. 5843 (Kaufmann et al. 2023; Lamberts-Van Assche et al. 2022) |
| Microwave torch above 75 kW | possibly below US$1 per W | D11; old |
| Nanosecond pulsed supply | ~€5,000 per kW | T12 |
| 30 kW, 915 MHz magnetron head (head only) | €109,000 list price (~€3,600 per kW) | D12; low quality |

D10 also states (p. 5842) that lab plasma supplies are the most expensive component *because* they are built to be flexible across plasma types. Supplies designed for one industrial condition can be cheaper. This supports the "niche" reading only for the flexible lab units.

**Still open:**
- RF tube generator cost and efficiency at 100 kW+;
- an independent (non-vendor) measurement of ozone-plant inverter efficiency at MW scale;
- the primary DBD cost studies cited by D10 (Kaufmann 2023; Lamberts-Van Assche 2022).

## Sources (D1-D12)

Found 2026-11-09 by Claude's general web search tool. Vendor and listing data are labelled as such.

| ID | Source | Used for | Quality |
|---|---|---|---|
| D1 | Toshiba Mitsubishi-Electric Industrial Systems (TMEIC), US 7,744,825 B2, "N-phase ozone generator", granted 2010-06-29 ([Google Patents](https://patents.google.com/patent/US7744825B2/en)) | conventional large ozone generator: 35 kg/h, 452 kW supply, ~1 kHz inverter, ~11 kWh/kg, load power factor ~30% | patent background |
| D2 | Xylem Wedeco PDO/PDA series description ([mininglifeonline](https://mininglifeonline.net/equipment/ozone-oxidation/pdo-pda-series/1227)) | 14 to >300 kg/h per unit; IGBT converters with 12/18-pulse rectifiers | vendor |
| D3 | Wedeco SMO/SMA brochure ([motralec.com](https://www.motralec.com/Telecharger-2/Wedeco_SMO-SMA.pdf)); Suez Ozonia L announcement ([wateronline](https://www.wateronline.com/doc/suez-introduces-ozonia-l-the-next-generation-of-large-capacity-ozone-generators-0001)) | medium-frequency converter + HV transformer; units up to 60 kg/h | vendor |
| D4 | Stellant Systems CWM-100 magnetron datasheet, 2023 ([PDF](https://stellantsystems.com/wp-content/uploads/2023/10/Magnetron_CWM-100kW_sellsheet_MAY2023.pdf)); Fermilab partnerships page ([fnal.gov](https://partnerships.fnal.gov/?p=421)) | 100 kW CW at 915 MHz, efficiency approaching 86% (Fermilab: ~84%) | vendor datasheet; national lab |
| D5 | Muegge MH015KS 2.45 GHz, 15 kW generator listing ([everythingrf](https://www.everythingrf.com/products/microwave-generators/muegge-gmbh/854-551-mh015ks-310cn)) | largest 2.45 GHz commercial unit found (~15 kW) | vendor listing |
| D6 | RF Essentials, industrial microwave oven frequency and power ([rfessentials.com](https://rfessentials.com/rf-knowledge-base/what-is-the-frequency-and-power-requirement-for-an-industrial-microwave-oven/)) | 2.45 GHz 1.5-6 kW per tube at 65-70%; 915 MHz up to 100 kW at up to 88% | web, low quality |
| D7 | IEICE Trans. Electron. E107-C(10), 2024, GaN SSPAs for microwave heating and WPT, DOI [10.1587/transele.2024MMI0004](https://doi.org/10.1587/transele.2024MMI0004) | 450 W at 70% drain efficiency, 2.45 GHz; comparison: magnetron ~70%, LDMOS ~60%, GaN ~65% | peer-reviewed |
| D8 | EU CLEAN-HEAT project (H2020, 666488) results ([CORDIS](https://cordis.europa.eu/project/id/666488/reporting/es)) | 1 kW GaN source, 70% efficiency at 2.45 GHz | project report |
| D9 | US 9,237,639, "Microwave resonant cavity" ([USPTO](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/9237639)) | a 10 kW magnetron costs much more than ten 1 kW magnetrons | patent background |
| D10 | Osorio-Tejada et al. (2024) Energy Environ. Sci. 17, 5833-5853 (RV005; [../literature_reviews/OsorioTejada_EES_2024_Plasma_vs_Electrolysis_CO](../literature_reviews/OsorioTejada_EES_2024_Plasma_vs_Electrolysis_CO)) | plasma power-unit + reactor capital cost | peer-reviewed; checked in our PDF copy |
| D11 | MIT Plasma Science and Fusion Center report 99ja008 (1999; authors to record from the archived copy) ([dspace.mit.edu](https://dspace.mit.edu/bitstream/1721.1/95389/1/99ja008_full.pdf)) | microwave torch capital cost possibly below US$1 per W above 75 kW | institutional report; old |
| D12 | Used-equipment listing, Muegge 30 kW 915 MHz magnetron head WR975 ([machineseeker](https://www.machineseeker.co.uk/muegge-wr975/i-20729582); listing removed by 2026-11-09) | manufacturer reference price €109,000 | listing; low quality |

Only D1 and D10 were read in full text for the quoted values. The others were taken from search summaries or short web pages and should be checked before citing.

