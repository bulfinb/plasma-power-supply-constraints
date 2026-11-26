# Industrial power supplies for scaled-up electrified reforming

First drafted 2026-11-05; rebuilt 2026-11-10 from [supply_values.csv](../results/supply_values.csv) after every value was re-extracted from the archived source copies (see [../workflow.md](../workflow.md)). Status: **ai_checked; human check: none**. Class data: [../supply_classes.csv](../results/supply_classes.csv). Calculation: [../figures/scaleup_wall_basis.py](../results/scaleup_wall_basis.py), output `../figures/scaleup_wall_basis.csv`. Source IDs (PWxxx) resolve in [source_register.csv](../results/source_register.csv); value IDs (PWxxx-Vnn) in supply_values.csv.

## Purpose

The review sources report energy at the discharge, arc, absorbed-microwave or RF-generator boundary, measured with lab supplies. This note asks a different question: if each reactor type were scaled up with a **representative industrially available supply** suited to that discharge, how much electricity would be drawn from the wall, and what are the indicative costs and lifetimes? It is not a benchmark of the supplies used in the papers.

## Efficiency chain

Wall electricity reaches the reaction through up to four stages; each paper's power boundary sits at a different point in this chain.

| Stage | Symbol | Examples | Where the papers sit |
|---|---|---|---|
| Wall to generator output | eta_supply | rectifier, inverter, magnetron/tube, solid-state amplifier | Discharge-power papers (Kwon, Zhu, Andersen, Geng) and arc-power papers (Hrabovsky) are after this stage |
| Generator output to plasma or heater | eta_couple | reflected power, waveguide, matching network, ballast, coil losses | Absorbed-microwave papers (Kelly, Akande, Hrycak) are after this stage; Song's RF power is before it |
| Plasma to process gas | eta_thermal | torch electrode and wall cooling | Inside arc-power and absorbed-power EC values already |
| Heat integration | NA | steam raising, feed preheat, heat recovery from hot product | Mostly absent in lab tests; present in eSMR and fired SMR |

Indicative wall-basis EC_CH4 = reported EC_CH4 / eta_supply, using the class range. eta_couple is not applied separately; this understates wall demand for Song (RF matching and coil losses not included).

## Representative supply classes

| ID | Class | eta (wall to output) | Cost | Lifetime | Values |
|---|---|---|---|---|---|
| J1 | Low-voltage high-current AC/DC (Joule) | 0.97-0.985 (upper: IGBT rectifier ~98.5%; lower: reviewer allowance for transformer) | 85-88 EUR/kVA (thyristor) to 154-158 EUR/kVA (IGBT), 3 MW incl. transformer and compensation (2021 estimate); power management ~20% of electrolyser equipment capex | NR | PW021-V01, -V02, PW022-V01, -V02 |
| A1 | MW DC rectifier for arc torches | 0.90-0.98 (lower: tender requirement) | no EUR/kW; ballast inductor a substantial share (qualitative) | torch electrodes >1,000 h (vendor) | PW023-V01, PW021-V01, PW038-V01, PW034-V02 |
| D1 | HV DC switch-mode, current-controlled (glow, DC gliding arc) | 0.92-0.97 (lower: Technix SR >92% at full load, 1.5-8 kW, datasheet; NWL 70 kW ESP unit ~94.6% from stated losses; upper: ANDRITZ SIR >95%, >97% SiC, vendor claims). ESP corona loads; part load not stated | NR | NR | PW054-V01, PW053-V03, PW051-V01, -V02 |
| K1 | kHz HV resonant inverter (AC gliding arc, DBD) | 0.90-0.92 (induction analogue 91%, tier 1 spec; 250 W ozone inverter 91%, others 69-70%) | DBD supply alone ~1,200-1,500 EUR/kW (industry estimates, 144 kW pilot, 2022); supply + reactor 1,085-2,400 EUR/kW (gliding arc) | NR | PW004-V02, PW026-V01 to -V03, PS003-V01, -V02, RV005-V01, -V02 |
| K2 | Induction-heating inverter (analogue) | 0.91-0.98 | NR | NR | PW004-V02, PW005-V02, PW003-V02 |
| R1 | RF tube oscillator (ICP) | 0.53-0.60 | NR | NR | PW024-V01, PW007-V03 |
| R2 | Solid-state RF | 0.70-0.80 (vendor claims); Class E amplifier 91.5% at 600 W, 12-15 MHz (amplifier only) | NR | NR | PW008-V02, PW025-V01, PW027-V01 |
| M1 | 915 MHz magnetron, 75-100 kW units | 0.74-0.82 (HV supply 0.90-0.95 x tube 0.82-0.86; vendor generator claims ~0.80 inside) | turnkey ~1,000-3,000 USD/kW (undated); tube 100-300 USD/kW | tube <=6,000 h | PW009-V01, PW012-V01, PW020-V01, PW033-V01, -V02 |
| M2 | 2.45 GHz magnetron, up to 15 kW | 0.63-0.72 (datasheet rated input 0.63-0.70; supply x tube ~0.59-0.71; measured 0.72, Kiefer 2024) | ~1,000 USD/kW (2024, scope not stated) | >15,000 h expected (vendor); 6,000-15,000 h (tier 3); 1-3 years (2024 review) | PW050-V05, -V06, PW045-V01, PW046-V02, -V04, -V05, PW044-V01, PW031-V03 |
| M3 | 2.45 GHz GaN solid-state | 0.56-0.70 (amplifier/head only); LDMOS ~60%, GaN ~65% expected | ~3,000 USD/kW (LDMOS, 2024); 5-10x magnetron per W (tier 3) | ~10 years | PW018-V01, PW019-V01, PW046-V01, -V06 to -V09, PW031-V01 |
| P1 | Nanosecond pulsed | 0.45-0.92 (load-dependent) | ~5,000 EUR/kW (2009 estimate); 20,000-30,000 EUR/kW state of the art (2009) | NR | PW028-V01, PW029-V01, -V02, -V03, -V04 |
| H1 | CW klystron (context) | 0.60-0.63 (tube only); ~0.25 HV DC to average RF for a 1 MW-peak pulsed radar transmitter (PW015-V06, calculated) | >5 USD/W (klystrons) | NR | PW014, PW011-V01, PW016-V01, PW020-V03 |

Scale evidence: induction supplies of 16 MW per unit and 126 MW installed (PW001-V01, -V03); 915 MHz microwave containers of "several megawatts" from 100 kW units (PW012-V03); Monolith's plasma methane pyrolysis expansion contracted 2,000 GWh/y of electricity, ~228 MW average (PW036-V01, -V02; reviewer arithmetic). Joule benchmark: Topsoe states its eREACT reactor needs ~1 kWh per Nm3 H2, ~81 kJ/mol H2 (PW037-V01; vendor claim, plant boundary not stated).

### Changes made when the values were re-extracted (2026-11-10)

- **2026-11-11, class assignments checked against the extraction records:** Zhu 2019 (SRC012) is a DC gliding arc with a ballast resistor, not a kHz AC supply; Wanten 2022 (SRC015) uses a kV/mA HV DC supply, not a high-current arc rectifier. Both moved from K1 and A1 to the new class D1 (HV DC, current-controlled), which has no sourced values; the K1 range is used as an analogue. Later the same day D1 was given sourced values (PW051 ANDRITZ SIR leaflet, PW053 NWL ESP supply paper, PW054 Technix SR datasheet): range 0.92-0.97. Wall basis: Zhu 505-738, Wanten 838-1298 kJ/mol. A K2 sub-band row (solid-state, 100-400 kHz) added for Song 2020.

- **J1:** the "thyristor rectifier 99.84%" value cited on 2026-11-05 is not in the archived article (PW021), which says thyristor rectifiers are the *less* efficient option. Upper bound lowered to 0.985 (IGBT).
- **P1:** the 85.2% and 56.7% values attributed to the Acta Phys. Pol. paper are not in it (PW029). The range now rests on the TU/e abstract (45-85% energy transfer into the reactor, PW028) and PW029 (>90% at 20 kW; 92% ± 6%). The ~5 kEUR/kW cost is from PW029, not PW028, and the same paper gives 20-30 kEUR/kW for state-of-the-art pulsed power.
- **M2:** the lower bound 0.80 had been set equal to the 915 MHz class by assumption. The archived sources give 65-70% for 2.45 GHz magnetron generators (tier 3); the only support for 0.85 (SAIREM guide, PW010) has no local copy. The SAIREM GMP100 10 kW datasheet (PW050) states no generator efficiency, but its rated consumption (15.8 kVA, power factor >0.9) for 10 kW output gives 0.63-0.70 (reviewer calculation, PW050-V05). Range set to 0.63-0.70; the 85% value is not used.
- **M1 efficiency (2026-11-11, BB decision):** the upper bound 0.86 was a magnetron tube value (PW017-V01; PW020-V04 ~84% is also a tube value); M1 now uses the generator values only, ~0.80 (PW009-V01, PW012-V01). Wall basis: Akande 639-1348, Hrycak 298-589 kJ/mol.
- **M1 and M2 (2026-11-20, BB decision after the GPT cross-check, XP002):** both classes now use one method, generator = HV supply stage x magnetron tube. M1: 0.90-0.95 x 0.82-0.88 (tube loss 15-18%, PW009-V03; 86%, PW017-V01; 84%, PW020-V04; up to 88%, PW045-V04) -> 0.74-0.84, with the vendor generator claims (~0.80) inside. M2: >0.90 x 0.65-0.75 (PW031-V04; ~70%, PW046-V02) -> ~0.59-0.71; the rated-input datasheet value 0.63-0.70 (PW050-V05) is a lower bound; upper 0.72 from Kiefer's measured wall-to-absorbed ratio (SRC016-V01). Rated input kVA is a sizing value, so kVA-based efficiencies are lower bounds (MTX100: >=0.67).
- **Relevance review (2026-11-23, BB decision; notes/relevance_review_2026-11-23.md):** 15 sources dropped (PW010, PW011, PW013, PW016, PW030, PW031, PW032, PW036, PW037, PW041, PW042, PW043, PW045, PW052, PW060). Without the tier 3 PW045, M1 is 0.74-0.82 (tube 0.82-0.86); M2 stays 0.63-0.72 on PW050 and Kiefer (SRC016-V01) without PW031. H1 is CW klystrons only (0.60-0.63). Classes J2 and X1 removed. The R2 and M3 alternative cases were removed from scaleup_wall_basis.py. Values above that cite dropped sources are kept as history.
- **M1:** tube lifetime "2,000-15,000 h" is not supported for 915 MHz; the archived source gives "6,000 hours or less" (PW033). New tube cost: <0.10 USD/W (PW033).
- **R1:** a second, indicative lower bound from the TruHeat HF 7100 rated input (0.53, reviewer calculation) widens the range to 0.53-0.60.
- **K1:** the 100 kW tender requirement (T07, now PW023) is a DC torch supply and moved to A1. K1 now rests on the induction-heating generator analogue (TRUMPF MF, 91%) and a 250 W ozone inverter study (PW026: 91% best case; the two modulated inverters 69-70%). The Class E DBD amplifier (PW027) runs at 12-15 MHz and is now under R2.
- **K1 cost:** the "1,300 EUR/kW DBD reactor" (RV005) is EUR 188,143 for a 144 kW pilot, of which EUR 173,000 is the power supply (PS003 Table 6). The same study takes the power source efficiency (source to plasma) as ~50% from its lab DBD and keeps it at scale (PS003-V04).
- **J1 cost:** "converter ~15% of electrolyser capex" (PW022) is not in the paper; its 15% is a hydrogen price decrease potential quoted from another study. The paper's Table 3 gives full rectifier-system costs instead: 85-88 EUR/kVA (thyristor) and 154-158 EUR/kVA (IGBT and two-stage) for a 3 MW, 10 kA supply. It also states that thyristors are generally more efficient than IGBTs, the opposite of PW021; the J1 range is unchanged.
- **M1 cost:** van Rooij et al. (PW030, Faraday Discuss. 2015) say only that "power (e.g. microwave) supplies are cheap (0.1 euro per W)", without frequency, scale or reference. Moved to context.
- **M2, M3:** a 2024 review table (PW046) gives magnetron ~70%, ~1,000 USD/kW, 1-3 years; LDMOS amplifier ~60%, ~3,000 USD/kW, ~10 years; GaN ~65% expected.

## Supply class by discharge type ([discharge_supply_map.csv](../results/discharge_supply_map.csv))

Added 2026-11-11. For each discharge type in the review, the map records the lab supply as given in the extraction records (literature_reforming/*/outputs/extraction.md, evidence IDs), the electrical requirement, the candidate industrial classes, the class used in the wall-basis calculation and the scale-up constraint, with value IDs. It is by discharge type, so it also applies to the pyrolysis and CO2-splitting sources when they are added.

| Discharge | Review sources | Class | eta (wall to output) | Verdict on the supply |
|---|---|---|---|---|
| Thermal DC arc | SRC007 | A1 | 0.90-0.98 | not limiting; torch efficiency and electrode life are |
| Gliding arc, AC (~20 kHz) | SRC014 | K1 | 0.90-0.92 | not limiting; ~600 arcs per MW at lab arc power (numbering-up) |
| Gliding arc, DC | SRC012 | D1 | 0.92-0.97 | efficiency not limiting (ESP units 70-180 kW); ~4,000 arcs per MW, each needing its own current control in place of the lab ballast |
| Glow, DC | SRC015 | D1 | 0.92-0.97 | efficiency not limiting; ~7,000-10,000 discharges per MW, each needing its own current control |
| DBD | SRC013, SRC002 | K1 | 0.90-0.92 | efficiency not limiting (ozone units ~0.5 MW); load power factor 0.3-0.5 and supply cost (~1,200-1,500 EUR/kW) are |
| Microwave 915 MHz | SRC008, SRC010 | M1 | 0.74-0.82 | not limiting (100 kW units); tube life <=6,000 h |
| Microwave 2.45 GHz | SRC011 | M2 / M3 | 0.63-0.72 / 0.56-0.70 | limiting: <=15 kW units, ~70-170 units per MW |
| RF ICP (9.6 kHz-40 MHz; SRC009 at 400 kHz) | SRC009 | K2 / R1 / R2 | 0.91-0.96 / 0.53-0.60 / 0.70-0.80 | depends on torch size: torches >=100 mm run at <=0.5 MHz, where >=95% solid-state supplies of >=100 kW exist; small MHz torches need tubes or solid-state units of <=~30 kW |
| ns pulsed | none yet | P1 | 0.45-0.92 | limiting: 1-20 kW units, 5-30 kEUR/kW (2009) |
| Joule (benchmark) | SRC001, SRC005, SRC006 | J1 | 0.97-0.985 | not limiting; 85-158 EUR/kVA at 3 MW |

Arcs or discharges per MW are reviewer arithmetic (1 MW divided by the lab power per arc or discharge); industrial designs may run larger arcs. Three groups follow: (i) supply not limiting: DC arc, kHz gliding arc and DBD, 915 MHz, Joule; (ii) supply limits efficiency or unit size: 2.45 GHz, tube RF, ns pulsed; (iii) supply efficient but the load is the problem: HV DC for glow and DC gliding arc. HV DC switch-mode supplies are a mature product (>5,500 ANDRITZ SIR units in electrostatic precipitators, PW051-V08) at >92-97% and up to ~180 kW per unit, but an ESP corona load shares current across many wires by itself, whereas glow discharges and arcs have negative differential resistance and need current control per discharge. For the low-power discharges (gliding arc, glow, DBD) the scale-up question is distribution and control of current over many parallel discharges more than the size of the supply.

**ICP frequency and torch size** (figure `results/figures/icp_frequency_scale.png`, supporting information). Induction torches have been built from 9.6 kHz to 40 MHz and 0.5 kW to ~1 MW (PW055-V05). The induced current flows in a skin layer of depth delta = (pi f mu0 sigma)^-1/2, about 8 mm at 4 MHz in atmospheric argon at 8000 K (PW055-V01); coupling is best for plasma radius / delta of 1.5-4 and drops sharply below 1 (PW055-V02). The minimum frequency therefore falls roughly as 1/D^2, and "an increase of rn ... has to be accompanied by a decrease in the operating frequency and an increase in the power level" (PW055-V03). A patent gives the design examples ~4 MHz for a 40 mm tube, ~0.5 MHz for >=100 mm and a 50 kHz band for >=200 mm (PW058-V02 to -V04); its own sizing equation (D >= 3.5 delta, PW058-V01) gives ~1.9 MHz for 40 mm, so the examples follow the Boulos band rather than that equation. Real torches sit in or above the band: Song's 80 mm torch at 400 kHz (SRC009), the 160 mm VKI Plasmatron at 400 kHz and 1.2 MW (PW056-V01, -V02), and smaller torches at 2.6-17 MHz (PW055, PW057, PW060); analytical ICPs run at 27.12 MHz and <=1.6 kW (PW059-V01). The low-frequency limit is the sustaining power: ~1 MW at 960 Hz in argon (PW055-V04).

On the supply side the same patent states that >=95% solid-state supplies are commercial at >=100 kW for 0-0.5 MHz but limited to ~30 kW at >=1 MHz, against 50-60% for vacuum-tube supplies (PW058-V05 to -V08); TRUMPF offers tube generators for ICP up to 120 kW at 2-3 MHz (PW061-V01). Scaling an ICP torch up (>=100 mm) thus moves it into the frequency range of efficient solid-state supplies, the reverse of the microwave case, where the large-unit band (915 MHz) differs from the band most lab work uses (2.45 GHz) and the reactor must be redesigned. Not shown: coil and matching losses, and whether chemistry demonstrated in small MHz torches carries over to large low-frequency torches.

## Figures (results/plot_supply_values.py; ICP figure results/plot_icp_frequency_scale.py)

- `supply_class_map.png`: each class as a box of frequency band against unit power, coloured by its efficiency range. The usable design space is DC and kHz (MW units, 90-98.5%) and 915 MHz (100 kW, ~80%). RF tube generators reach 100 kW but at 53-60%; RF solid-state and 2.45 GHz sources are limited to ~0.25-15 kW per unit at 56-80% (amplifier or generator). Only vacuum tubes give MW at GHz, at 40-63% tube efficiency.
- `icp_frequency_scale.png` (supporting information): (a) torch diameter against frequency with the skin-depth coupling band; (b) torch or generator power against frequency with the solid-state and tube supply ranges. Shows that larger torches run at lower frequency, inside the range of efficient high-power solid-state supplies.
- `supply_cost_vs_unit_size.png`: cost per kW against unit or installation size. Published supply-only costs fall from ~1,200-5,000 EUR/kW at 10-150 kW (DBD, pulsed) to 85-160 EUR/kVA for 3 MW rectifiers; 915 MHz tubes are ~100-300 USD/kW at 100 kW. The TEA reactor cost functions (PS004) assume cost per kW falls as P^-0.47 from 3 to 100 MW (an electrolyser scaling), whereas the gliding arc manufacturer quoted in RV005 assumes constant cost per kW up to ~1,000 t CO2/y and an exponent of 0.9 beyond (cost per kW ~P^-0.1, RV005-V05). Whether plasma supplies follow either rule is not shown by any published data point above 144 kW.

## Indicative wall-basis EC_CH4 (results/scaleup_wall_basis.py)

| Source | Paper boundary | Supply class | EC_CH4 reported (kJ/mol) | EC_CH4 wall (kJ/mol) |
|---|---|---|---|---|
| Hrycak 2023 | absorbed MW (lower bounds) | M1 | 258-509 | 307-688 |
| Zhu 2019 | discharge; steam and lab ballast excl. | D1 (HV DC) | 490-679 | 505-738 |
| Akande 2022 | absorbed MW | M1 | 511-1078 | 608-1457 |
| Kelly 2023 | absorbed MW | M2 magnetron / M3 solid-state | 581-723 | 807-1148 / 830-1291 |
| Kwon 2023 | discharge | K1 | 740-948 | 804-1053 |
| Wanten 2022 | plasma; lab ballast excl. | D1 (HV DC) | 813-1194 | 838-1298 (lab ballast incl.: 2392-3490) |
| Song 2020 | RF generator output | K2 solid-state 100-400 kHz / R2 solid-state / R1 tube | 1036-1510 | 1079-1659 / 1295-2157 / 1727-2849 |
| Geng 2022 | discharge; furnace excl. | K1 | 1120-1490 | 1217-1656 |
| Hrabovsky 2018 | arc power | A1 | 1149-2172 | 1172-2413 |
| Andersen 2020 | discharge | K1 | 8103-9712 | 8808-10791 |

Reference lines: SMR 206, DRM 247 kJ/mol CH4. Values exclude steam raising, furnace heat and heat recovery as in the papers. Wanten 2022 used a 300 kOhm series ballast resistor that dissipated 1.6-2.6x the plasma power (SRC015-C005); an industrial glow array would need active current control per discharge instead, so the D1 row assumes that. The D1 range (0.92-0.97) is for full-load ESP and rack HV DC supplies; the efficiency of many small current-controlled channels at part load is not sourced, so the D1 rows are a lower bound on wall demand. The K2 row for Song uses 0.91-0.96 from solid-state induction generators covering 100-400 kHz (PW004-V02, PW005-V02); these efficiencies are for induction-heating loads, not plasma.

## Interpretation (for discussion; human check: none)

1. With industrial supplies, the wall correction is modest (+2-25%) for DC arcs, 915 MHz magnetrons and kHz inverters. It is larger for RF tube oscillators (+67-89%), 2.45 GHz magnetrons (+43-59%) and 2.45 GHz solid-state (+43-79%). Supply efficiency therefore does not change the broad ranking; the plasma process (regime, heat losses, lack of heat recovery) dominates.
2. The supply choice matters where frequency is forced: ICP torches and 2.45 GHz sources. For the 400 kHz ICP torch, solid-state induction generators (50-100 kW at 100-400 kHz) would cut the wall correction from +67-89% (tube) to +4-10%, if their induction-heating efficiencies carry over to a plasma load. Industrial microwave scale-up would favour 915 MHz magnetrons (100 kW units, ~80%) over 2.45 GHz sources, at the cost of tube replacement every few thousand hours.
3. All plasma wall-basis EC_CH4 values (≥ ~300 kJ/mol) lie above the reaction enthalpy, mainly because hot product heat is not recovered in the tests. Joule-heated eSMR (~81 kJ/mol H2 claimed, cf. plasma EC_H2 ~144-530 kJ/mol on discharge or absorbed basis) shows what heat integration plus a ~98% supply can achieve. Comparing like with like requires adding heat recovery to the plasma cases, which is the next step of the scale-up assessment.
4. Costs are sparse and mostly not for the supply alone. MW rectifier systems for electrolysis cost ~85-160 EUR/kVA including transformer and compensation (2021 estimate). Microwave has the most points (turnkey 1-3 USD/W undated, <1 USD/W in 1999; tubes 0.1-0.3 USD/W; 2.45 GHz magnetron ~1 USD/W and LDMOS ~3 USD/W in 2024); pulsed power 5-30 kEUR/kW (2009); DBD supplies ~1,200-1,500 EUR/kW from industry price estimates for a 144 kW pilot (2022), ~92% of that pilot's capital cost; gliding arc supply + reactor 1,085-2,400 EUR/kW. The Joule-heating supply is therefore an order of magnitude cheaper per kW than any plasma supply with a published price. Lifetime is a real cost driver for magnetrons (≤6,000 h at 915 MHz) and torch electrodes (~1,000 h claimed).

## Sources

All sources are in [source_register.csv](../results/source_register.csv) under PW IDs, with the IDs used in this note before 2026-11-10 (T01-T23) listed as aliases. Two values (PW010, the SAIREM guide, optional) come from a source without a local copy and are marked `unverified` in supply_values.csv; see [../BB_search.txt](BB_search.txt).
