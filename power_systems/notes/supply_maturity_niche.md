# Are plasma power supplies a "niche product"? Supply maturity, limits and cost

Added 2026-11-09 (BB, with Claude); rebuilt 2026-11-10 from [../supply_values.csv](../supply_values.csv) after every value was re-extracted from the archived source copies. Status: argument to develop; values ai_checked, human verification pending. Source IDs (PWxxx) resolve in [../source_register.csv](../source_register.csv) (earlier IDs D1-D12 are listed there as aliases); value IDs (PWxxx-Vnn) in supply_values.csv. Academic papers on the supply side are in [../../literature_plasma_powersupply/](../../literature_plasma_powersupply/README.md).

Bogaerts (2025, RV015, p. 338) says that plasma-reactor capital cost is mainly set by the power supply. She calls the supply "still quite expensive today because it is still a 'niche product'", and notes challenges in degradation, reproducibility, control and energy efficiency for MW supplies. The first part, that the supply dominates capital cost, strengthens the case for treating the supply as a design constraint (see Novelty in [../../README.md](../../README.md)). The "niche product" explanation holds only in part.

**The power-conversion stage is mature elsewhere.** The same supply classes are established products in other industries:

| Supply class | Established use | Scale and efficiency found | Values |
|---|---|---|---|
| DC rectifiers | electrolysis, arc furnaces, DC plasma torches | MW; IGBT rectifiers ~98.5%; torch supply tender >=90% | PW021-V01, PW023-V01 |
| kHz resonant inverters | induction heating and melting; industrial ozone generators | to 4 MW per unit, 16-42 MW installed supplies; 91% (spec) to ~98% (claim) | PW002-V01, PW001-V01, PW004-V02, PW003-V02 |
| RF tube oscillators, 0.4-3 MHz | induction heating; ICP torches | to 500 kW per family; ~53-60% | PW007-V01, -V03, PW024-V01 |
| Magnetrons, 915 MHz | industrial microwave heating and drying | 100 kW per unit; generator ~80%, tube ~84-86% | PW009-V01, PW012-V01, PW017-V01, PW020-V04 |

Ozone generation is a DBD process already run at hundreds of kW to MW scale on medium-frequency inverters:
- A conventional large unit (35 kg/h class) has 452 kW discharge power at about 1 kHz and 11 kWh/kg (PW039-V01, -V02).
- Current Wedeco units reach "more than 300 kg/h" per unit (PW041-V01). At about 10 kWh/kg that implies roughly 3 MW per unit (reviewer estimate).

Industrial DBD with efficient power delivery therefore exists. The same patent also shows the DBD matching problem at scale: the load power factor is about 30%, so a 452 kW load needs a 1,500 kVA transformer (PW039-V03). An older patent gives 0.4-0.5 and states that "the supplies must be oversized" (PW040-V01). The gap is the energy efficiency of the chemistry, plus reactive-power management, not the supply's conversion efficiency.

**Several limits are physical and will not ease with market volume:**

- **Frequency vs unit power and efficiency.** Semiconductor switching losses rise with frequency. Solid-state supplies are efficient at kHz (91-98%, K2), while high-power RF still relies on vacuum tubes (~53-60%, R1); solid-state RF generators are 1.5-5 kW units at >70-80% (PW008-V01, -V02; PW025-V01).
- **Microwave unit power.** The magnetron cavity scales with wavelength, which caps single-unit power:
  - 915 MHz: 100 kW CW tubes at efficiencies approaching 86% (PW017-V01).
  - 2.45 GHz: the largest commercial unit found is a 15 kW magnetron head (PW044-V01; no efficiency or price on the datasheet). A knowledge-base page gives 1.5-6 kW per tube and 65-70% generator efficiency (PW045-V01, -V02; tier 3).

  MW plants therefore need many modules. Within one band, magnetron price rises steeply with unit power (PW047-V01: "the price of a 10 KW magnetron is much higher than the price of ten 1 KW magnetrons"). Across bands the reverse holds: 100 kW 915 MHz tubes cost 0.1-0.3 USD/W (PW033-V01, PW020-V02).
- **Solid-state microwave efficiency.** At 2.45 GHz, GaN amplifiers reach 70% drain efficiency at 450 W (PW046-V01) and 70% for a 1 kW source (PW019-V01); a 6 kW GaN generator head reached 56% (PW018-V01). These are device or head values before the AC/DC stage, so wall-plug efficiency is lower.
- **Lifetime of tubes and magnetrons.** 915 MHz industrial magnetrons: "6,000 hours or less" (PW033-V02). This is a known wear mechanism, not an immature product.

**The genuinely plasma-specific part is matching and control.** Plasma loads have negative differential resistance, an impedance that jumps at ignition and, for a DBD, a capacitance that changes in operation. This leads to reflected power, reactive power and ballast losses (PS002 in [../../literature_plasma_powersupply/](../../literature_plasma_powersupply/README.md); Wanten 2022, SRC015, where the ballast dissipated 1.6-2.6 times the plasma power).

**Implication.** Supply cost and efficiency are partly set by physics that is already known from mature industries. They can therefore be used now to gate design options: frequency band, unit power, number of modules and wall-to-plasma efficiency can be fixed before the plasma chemistry is assessed. This contrasts with expecting supplies to improve once the market grows. "Niche" fits the coupling and control electronics better than the power-conversion stage.

**Capital cost data found so far.** These are sparse and often not for the supply alone:

| Basis | Cost | Year | Value |
|---|---|---|---|
| MW rectifier system for electrolysis (thyristor; IGBT), incl. transformer, filter, compensation | 85-88 EUR/kVA; 154-158 EUR/kVA | 2021 | PW022-V01; -V02 (Table 3, 3 MW 10 kA) |
| Gliding arc plasma, power unit + reactor body, industrial CO2 project basis | 1,085 EUR per kW plasma power | 2024 | RV005-V01 (p. 5842) |
| Gliding arc 5.6 kW prototype, uninstalled power unit + reactor body | 2,400 EUR/kW | 2024 | RV005-V02 (p. 5842) |
| DBD power supply alone, industry price estimates (12 x 12 kW; cost function) | ~1,200 EUR/kW; 1,500 EUR/kW + 900 EUR | 2022 | PS003-V02 (calculated); -V01 (Table 6) |
| DBD plasma reactor (TEA) | 1,300 EUR/kW | 2022 | RV005-V04 (p. 5843, citing Lamberts-Van Assche 2022, PS003) |
| DBD pilot plant, 144 kW, reactor + power supply: EUR 188,143 | ~1,300 EUR/kW | 2022 | PS004-V01 (Kaufmann et al. 2023, p. 6, summarising PS003) |
| Plasma reactor cost functions (PEM electrolyser analogue), DBD; gliding arc, 3 MW | ~1,300; ~2,670 EUR/kW (scope not stated) | 2019 basis | PS004-V03; -V04 (calculated) |
| Same cost functions extrapolated to 100 MW | 260-520 EUR/kW | 2019 basis | PS004-V05 (calculated) |
| 915 MHz turnkey microwave transmitters | ~1,000-3,000 USD/kW | undated | PW020-V01 |
| 915 MHz turnkey microwave systems incl. power supply | <1,000 USD/kW | 1999 | PW048-V01 (citing a vendor) |
| Microwave torch above 75 kW (projection) | <1,000 USD/kW | 1999 | PW048-V02 |
| 100 kW 915 MHz magnetron tube only | <100 USD/kW to ~300 USD/kW | 2022; undated | PW033-V01; PW020-V02 |
| 2.45 GHz magnetron; LDMOS solid-state amplifier (scope not stated) | ~1,000 USD/kW; ~3,000 USD/kW | 2024 | PW046-V04; -V07 |
| Klystrons | >5,000 USD/kW | undated | PW020-V03 |
| Nanosecond pulsed modulator (estimate for a new design) | ~5,000 EUR/kW | 2009 | PW029-V02 |
| State-of-the-art pulsed power | 20,000-30,000 EUR/kW | 2009 | PW029-V03 |

The 1,300 EUR/kW DBD figure quoted by RV005 traces back to PS003 through PS004: EUR 188,143 for a 144 kW pilot, reactor and power supply together (PS004-V01). In PS003 Table 6 the power supply is EUR 173,000 of this (~92%, PS003-V03), from an industry price estimate for 12 x 12 kW units (~1,200 EUR/kW, PS003-V02); its cost function for other sizes is 1,500 EUR/kW + 900 EUR (PS003-V01). The "reactor" figure is therefore essentially a lab-derived supply price. PS004 then used it as the floor of its own reactor cost function, which is borrowed from PEM electrolyser manufacturing (PS004-V02) and falls to ~260 EUR/kW (DBD) at 100 MW only because of that assumed scaling exponent.

RV005 also states (p. 5842) that at lab scale "the power supply unit is typically the most expensive component", *because* lab units are built to be flexible across plasma types (RV005-V03). Supplies designed for one industrial condition can be cheaper. This supports the "niche" reading only for the flexible lab units.

**Still open:**
- cost per kW of kHz inverters and RF tube generators - the quote requests in [../suggested_quote_requests.txt](../suggested_quote_requests.txt) start this;
- RF tube generator efficiency measured at 100 kW+;
- an independent (non-vendor) measurement of ozone-plant inverter efficiency at MW scale;
- a supplier quote for a MW-class DBD or gliding arc supply, to test the 1,200-1,500 EUR/kW industry estimates of PS003 at scale.
