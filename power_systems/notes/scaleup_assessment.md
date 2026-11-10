# Industrial power supplies for scaled-up electrified reforming

First drafted 2026-11-05; rebuilt 2026-11-10 from [../supply_values.csv](../supply_values.csv) after every value was re-extracted from the archived source copies (see [../workflow.md](../workflow.md)). Status: **ai_checked; human verification pending**. Class data: [../supply_classes.csv](../supply_classes.csv). Calculation: [../figures/scaleup_wall_basis.py](../figures/scaleup_wall_basis.py), output `../figures/scaleup_wall_basis.csv`. Source IDs (PWxxx) resolve in [../source_register.csv](../source_register.csv); value IDs (PWxxx-Vnn) in supply_values.csv.

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
| K1 | kHz HV resonant inverter (gliding arc, DBD) | 0.90-0.92 (induction analogue 91%, tier 1 spec; 250 W ozone inverter 91%, others 69-70%) | DBD supply alone ~1,200-1,500 EUR/kW (industry estimates, 144 kW pilot, 2022); supply + reactor 1,085-2,400 EUR/kW (gliding arc) | NR | PW004-V02, PW026-V01 to -V03, PS003-V01, -V02, RV005-V01, -V02 |
| K2 | Induction-heating inverter (analogue) | 0.91-0.98 | NR | NR | PW004-V02, PW005-V02, PW003-V02 |
| R1 | RF tube oscillator (ICP) | 0.53-0.60 | NR | NR | PW024-V01, PW007-V03 |
| R2 | Solid-state RF | 0.70-0.80 (vendor claims); Class E amplifier 91.5% at 600 W, 12-15 MHz (amplifier only) | NR | NR | PW008-V02, PW025-V01, PW027-V01 |
| M1 | 915 MHz magnetron, 75-100 kW units | 0.80-0.86 | turnkey ~1,000-3,000 USD/kW (undated); tube 100-300 USD/kW | tube <=6,000 h | PW009-V01, PW012-V01, PW017-V01, PW020-V01, PW033-V01, -V02 |
| M2 | 2.45 GHz magnetron, up to 15 kW | 0.63-0.70 (datasheet, calculated; ~70% in a 2024 review table) | ~1,000 USD/kW (2024, scope not stated) | >15,000 h expected (vendor); 6,000-15,000 h (tier 3); 1-3 years (2024 review) | PW050-V05, -V06, PW045-V01, PW046-V02, -V04, -V05, PW044-V01, PW031-V03 |
| M3 | 2.45 GHz GaN solid-state | 0.56-0.70 (amplifier/head only); LDMOS ~60%, GaN ~65% expected | ~3,000 USD/kW (LDMOS, 2024); 5-10x magnetron per W (tier 3) | ~10 years | PW018-V01, PW019-V01, PW046-V01, -V06 to -V09, PW031-V01 |
| P1 | Nanosecond pulsed | 0.45-0.92 (load-dependent) | ~5,000 EUR/kW (2009 estimate); 20,000-30,000 EUR/kW state of the art (2009) | NR | PW028-V01, PW029-V01, -V02, -V03, -V04 |
| H1 | Klystron, gyrotron (context) | 0.40-0.63 (tube only); ~0.25 HV DC to average RF for a 1 MW-peak pulsed radar transmitter (PW015-V06, calculated) | >5 USD/W (klystrons) | NR | PW014, PW011-V01, PW016-V01, PW020-V03 |

Scale evidence: induction supplies of 16 MW per unit and 126 MW installed (PW001-V01, -V03); 915 MHz microwave containers of "several megawatts" from 100 kW units (PW012-V03); Monolith's plasma methane pyrolysis expansion contracted 2,000 GWh/y of electricity, ~228 MW average (PW036-V01, -V02; reviewer arithmetic). Joule benchmark: Topsoe states its eREACT reactor needs ~1 kWh per Nm3 H2, ~81 kJ/mol H2 (PW037-V01; vendor claim, plant boundary not stated).

### Changes made when the values were re-extracted (2026-11-10)

- **J1:** the "thyristor rectifier 99.84%" value cited on 2026-11-05 is not in the archived article (PW021), which says thyristor rectifiers are the *less* efficient option. Upper bound lowered to 0.985 (IGBT).
- **P1:** the 85.2% and 56.7% values attributed to the Acta Phys. Pol. paper are not in it (PW029). The range now rests on the TU/e abstract (45-85% energy transfer into the reactor, PW028) and PW029 (>90% at 20 kW; 92% ± 6%). The ~5 kEUR/kW cost is from PW029, not PW028, and the same paper gives 20-30 kEUR/kW for state-of-the-art pulsed power.
- **M2:** the lower bound 0.80 had been set equal to the 915 MHz class by assumption. The archived sources give 65-70% for 2.45 GHz magnetron generators (tier 3); the only support for 0.85 (SAIREM guide, PW010) has no local copy. The SAIREM GMP100 10 kW datasheet (PW050) states no generator efficiency, but its rated consumption (15.8 kVA, power factor >0.9) for 10 kW output gives 0.63-0.70 (reviewer calculation, PW050-V05). Range set to 0.63-0.70; the 85% value is not used.
- **M1:** tube lifetime "2,000-15,000 h" is not supported for 915 MHz; the archived source gives "6,000 hours or less" (PW033). New tube cost: <0.10 USD/W (PW033).
- **R1:** a second, indicative lower bound from the TruHeat HF 7100 rated input (0.53, reviewer calculation) widens the range to 0.53-0.60.
- **K1:** the 100 kW tender requirement (T07, now PW023) is a DC torch supply and moved to A1. K1 now rests on the induction-heating generator analogue (TRUMPF MF, 91%) and a 250 W ozone inverter study (PW026: 91% best case; the two modulated inverters 69-70%). The Class E DBD amplifier (PW027) runs at 12-15 MHz and is now under R2.
- **K1 cost:** the "1,300 EUR/kW DBD reactor" (RV005) is EUR 188,143 for a 144 kW pilot, of which EUR 173,000 is the power supply (PS003 Table 6). The same study takes the power source efficiency (source to plasma) as ~50% from its lab DBD and keeps it at scale (PS003-V04).
- **J1 cost:** "converter ~15% of electrolyser capex" (PW022) is not in the paper; its 15% is a hydrogen price decrease potential quoted from another study. The paper's Table 3 gives full rectifier-system costs instead: 85-88 EUR/kVA (thyristor) and 154-158 EUR/kVA (IGBT and two-stage) for a 3 MW, 10 kA supply. It also states that thyristors are generally more efficient than IGBTs, the opposite of PW021; the J1 range is unchanged.
- **M1 cost:** van Rooij et al. (PW030, Faraday Discuss. 2015) say only that "power (e.g. microwave) supplies are cheap (0.1 euro per W)", without frequency, scale or reference. Moved to context.
- **M2, M3:** a 2024 review table (PW046) gives magnetron ~70%, ~1,000 USD/kW, 1-3 years; LDMOS amplifier ~60%, ~3,000 USD/kW, ~10 years; GaN ~65% expected.

## Figures (figures/plot_supply_values.py)

- `supply_class_map.png`: each class as a box of frequency band against unit power, coloured by its efficiency range. The usable design space is DC and kHz (MW units, 90-98.5%) and 915 MHz (100 kW, 80-86%). RF tube generators reach 100 kW but at 53-60%; RF solid-state and 2.45 GHz sources are limited to ~0.25-15 kW per unit at 56-80% (amplifier or generator). Only vacuum tubes give MW at GHz, at 40-63% tube efficiency.
- `supply_cost_vs_unit_size.png`: cost per kW against unit or installation size. Published supply-only costs fall from ~1,200-5,000 EUR/kW at 10-150 kW (DBD, pulsed) to 85-160 EUR/kVA for 3 MW rectifiers; 915 MHz tubes are ~100-300 USD/kW at 100 kW. The TEA reactor cost functions (PS004) assume cost per kW falls as P^-0.47 from 3 to 100 MW (an electrolyser scaling), whereas the gliding arc manufacturer quoted in RV005 assumes constant cost per kW up to ~1,000 t CO2/y and an exponent of 0.9 beyond (cost per kW ~P^-0.1, RV005-V05). Whether plasma supplies follow either rule is not shown by any published data point above 144 kW.

## Indicative wall-basis EC_CH4 (figures/scaleup_wall_basis.py)

| Source | Paper boundary | Supply class | EC_CH4 reported (kJ/mol) | EC_CH4 wall (kJ/mol) |
|---|---|---|---|---|
| Hrycak 2023 | absorbed MW (lower bounds) | M1 | 238-471 | 277-589 |
| Zhu 2019 | discharge; steam excl. | K1 | 490-679 | 533-754 |
| Akande 2022 | absorbed MW | M1 | 511-1078 | 594-1348 |
| Kelly 2023 | absorbed MW | M2 magnetron / M3 solid-state | 581-723 | 830-1148 / 830-1291 |
| Kwon 2023 | discharge | K1 | 740-948 | 804-1053 |
| Wanten 2022 | plasma; lab ballast excl. | A1 (current-controlled DC) | 813-1194 | 830-1327 (lab ballast incl.: 2392-3490) |
| Song 2020 | RF generator output | R2 solid-state / R1 tube | 1036-1510 | 1295-2157 / 1727-2849 |
| Geng 2022 | discharge; furnace excl. | K1 | 1120-1490 | 1217-1656 |
| Hrabovsky 2018 | arc power | A1 | 1149-2172 | 1172-2413 |
| Andersen 2020 | discharge | K1 | 8103-9712 | 8808-10791 |

Reference lines: SMR 206, DRM 247 kJ/mol CH4. Values exclude steam raising, furnace heat and heat recovery as in the papers. Wanten 2022 used a 300 kOhm series ballast resistor that dissipated 1.6-2.6x the plasma power (SRC015-C005); an industrial glow array would need active current control per discharge instead, so the A1 row assumes that.

## Interpretation (for discussion; human check pending)

1. With industrial supplies, the wall correction is modest (+2-25%) for DC arcs, 915 MHz magnetrons and kHz inverters. It is larger for RF tube oscillators (+67-89%), 2.45 GHz magnetrons (+43-59%) and 2.45 GHz solid-state (+43-79%). Supply efficiency therefore does not change the broad ranking; the plasma process (regime, heat losses, lack of heat recovery) dominates.
2. The supply choice matters where frequency is forced: ICP torches and 2.45 GHz sources. Industrial microwave scale-up would favour 915 MHz magnetrons (100 kW units, ~80-86%) over 2.45 GHz sources, at the cost of tube replacement every few thousand hours.
3. All plasma wall-basis EC_CH4 values (≥ ~280 kJ/mol) lie above the reaction enthalpy, mainly because hot product heat is not recovered in the tests. Joule-heated eSMR (~81 kJ/mol H2 claimed, cf. plasma EC_H2 ~144-530 kJ/mol on discharge or absorbed basis) shows what heat integration plus a ~98% supply can achieve. Comparing like with like requires adding heat recovery to the plasma cases, which is the next step of the scale-up assessment.
4. Costs are sparse and mostly not for the supply alone. MW rectifier systems for electrolysis cost ~85-160 EUR/kVA including transformer and compensation (2021 estimate). Microwave has the most points (turnkey 1-3 USD/W undated, <1 USD/W in 1999; tubes 0.1-0.3 USD/W; 2.45 GHz magnetron ~1 USD/W and LDMOS ~3 USD/W in 2024); pulsed power 5-30 kEUR/kW (2009); DBD supplies ~1,200-1,500 EUR/kW from industry price estimates for a 144 kW pilot (2022), ~92% of that pilot's capital cost; gliding arc supply + reactor 1,085-2,400 EUR/kW. The Joule-heating supply is therefore an order of magnitude cheaper per kW than any plasma supply with a published price. Lifetime is a real cost driver for magnetrons (≤6,000 h at 915 MHz) and torch electrodes (~1,000 h claimed).

## Sources

All sources are in [../source_register.csv](../source_register.csv) under PW IDs, with the IDs used in this note before 2026-11-10 (T01-T23) listed as aliases. Two values (PW010, the SAIREM guide, optional) come from a source without a local copy and are marked `unverified` in supply_values.csv; see [../BB_search.txt](../BB_search.txt).
