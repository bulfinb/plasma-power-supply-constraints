# Source extraction: SRC022

## Source and review

- Source ID / citation / DOI: SRC022. Renninger, S., Stein, J., Lambarth, M., Birke, K.P. (2022). An optimized reactor for CO2 splitting in DC atmospheric pressure discharge. J. CO2 Util. 58, 101919. https://doi.org/10.1016/j.jcou.2022.101919
- Source filenames and document versions: manuscript.pdf, published version, SHA-256 `6be9fbbe56afe64cbd461ce8df74903ee16d2a1485051771bb889ca354e9f304`. No supplement. Printed page = PDF page.
- Retrieval date: 2026-11-11 (downloaded by BB).
- Protocol version: workflow.md 0.7, with the CO2-splitting metrics of [../../literature_review_objectives.md](../../literature_review_objectives.md).
- Extractor / date: Claude (AI), 2026-11-12.
- Coverage: full paper; Figs. 3 and 4 read from rendered pages.
- Reviewer / date / checks: Claude (AI), 2026-11-12; plasma power behind Fig. 4 and energy metrics recalculated (C001-C003).
- Review status: ai_checked. Human verification pending.

## Electricity supply

- Driver: DC lab power supply -> ZVS oscillator -> ferrite step-up transformer -> HV rectifier -> 1.5-3 H choke to suppress glow-to-arc transition (E003).
- Two boundaries (E004):
  - **Plasma power** P_plasma = I_plasma x V_plasma at the reactor (HV probes, shunt, average current).
  - **"System" power** P_supply = DC output of the lab power supply, i.e. driver input. The lab supply's own mains-to-DC losses are not included, so this is **not wall plug**. Helmholtz coil power excluded (main runs used permanent magnets).
- Driver efficiency 61-65% (E005); not optimised.
- Plasma scale: ~100-220 W. No external heat. Packed bed glows red (>800 C) at 192 W (E014).

## Reactor configuration

Pin (anode) to ring (cathode) DC glow-to-arc transition discharge in a 38 mm glass tube; water-cooled Cu electrodes; laminar downward flow from a 22-nozzle injector; ZrO2 packed bed (3 mm) inside the ring; axial magnetic field (30 mT) rotates the discharge (period 5-40 ms) to sweep the gas (E002, E015).

## Operating conditions

CO2 (purity not stated) at 0.65-1.25 SLM (0 C standard, consistent with 12.6 J/SCC) (E007, E009). Steady-state sampling after at least 1 min and two residence times (E006).

| OP | Q (SLM) | P_plasma (W) | P_supply (W) | Evidence |
|---|---|---|---|---|
| OP001 | 1.25 | ~162 | ~262 | E011, E012, E042 |
| OP002 | 1.25 | ~99 | ~153 | E012, E042 |
| OP003 | 0.65 | ~217 | NR | E010 |

## Performance indicators

- **Power boundary:** plasma (reactor terminals) and DC input to the driver; not wall plug.
- **External heat:** no.
- Product: CO2/CO/O2, unseparated; GC confirms stoichiometric CO and O2, no trace gases (E006).

| OP | X_CO2 (%) | E_spec (eV) | eta_plasma (%) | eta_system (%) | EC_CO plasma (kWh/Nm3) | EC_CO driver input (kWh/Nm3) |
|---|---|---|---|---|---|---|
| OP001 | 27.4 | 1.81 | 44.4 (reported 45) | 27.5 (reported 28) | 7.9 | 12.8 |
| OP002 | ~17 | 1.10 | 45.1 (fig ~45) | 29.2 (fig ~29) | 7.8 | 12.0 |
| OP003 | ~28.8 | 4.65 | 18.1 | NR (~11 at driver 0.61-0.65) | 19.3 | ~30-32 |

- Author's metrics: eta = X dH V / P with dH = 12.6 J/SCC on plasma or driver-input power (E009). Reproduced (E041).
- Statement mismatch: the text gives "45% at P_supply = 216 W", which is the 21% conversion point; the conclusion's 27.4% / 45% / 28% point is at ~262 W supply (~162 W plasma) (E012, E042). The abstract rounds to 43% at 27%.
- On plasma power, this is the best combined conversion and efficiency at 1 bar in the set so far (27% at ~44%, 7.9 kWh/Nm3 CO), but at ~160 W and with a ZrO2 packed bed whose role is unknown; without the bed conversion falls to 7.5% (E013).
- Conversion plateaus at ~29% regardless of flow (E010).
- Duration: <10 h total operation; no electrode wear observed (E014). Individual points after >=1 min steady state.

## Reporting quality

| Item | Answer | Reason and evidence IDs |
|---|---|---|
| Q1 Power measurement | yes | Plasma V x I with HV probes and shunt; driver input V x I (E004). |
| Q2 Feed definition | partly | Flows calibrated to standard conditions; purity not stated (E007). |
| Q3 Product analysis | yes | NDIR with GC confirmation; stoichiometry checked (E006). |
| Q4 Balance closure | partly | GC shows stoichiometric CO and O2; no numerical closure (E006). |
| Q5 Temperature | no | Only incandescence estimate of the bed (E014). |
| Q6 Controls | yes | Bed, flow direction, field and choke varied against a reference (E013). |
| Q7 Repeatability | no | Repeats and error bars not reported. |
| Q8 Stability | partly | Steady-state criterion stated; <10 h total, no long test (E006, E014). |
| Q9 Energy completeness | partly | Driver losses included; lab supply mains losses and coil power excluded (E004). |

- Confidence in conversion/product results: moderate. NDIR with GC confirmation, but no repeats or error bars.
- Confidence in energy results: moderate. Both boundaries measured; best-point statements slightly inconsistent; small scale.

## Gaps and comparison limits

- "System" efficiency is DC input to the driver, not wall plug; add the lab supply's mains-to-DC loss for a wall basis.
- Scale ~160 W at 1.25 SLM (0.056 mol/min CO2), the smallest in the set; the authors argue multi-kW is feasible at constant current with larger gaps (E015), but not shown.
- ZrO2 packed bed is essential (7.5% without it); mechanism unknown.
- No repeats or error bars.
- Hardware note: driver 61-65% (lab ZVS circuit with 3 H choke) (E005).

## Calculations

All in outputs/calculations.py.

- SRC022-C001 dH check: 12.6 J/SCC x 22,414 = 282.4 kJ/mol; power for 100% conversion at 1.25 SLM = 262.5 W.
- SRC022-C002 Plasma power behind each Fig. 4 point from X and eta_plasma; driver ratio; eta_system check. Input E012. Result E042.
- SRC022-C003 E_spec, efficiencies and EC_CO on plasma and driver-input bases. Inputs E010-E012. Result E041.

## Revisions

None.

## Plasma characteristics

- Regime: DC glow-to-arc transition, rotating in a 30 mT axial field; operation <2 kV, 50-275 mA; ignition <20 kV without aid (E015).
- Gas temperature: not measured; packed bed >800 C by incandescence at 192 W (E014).
- Other diagnostics: V-I characteristics vs field; rotation period from voltage modulation and high-speed video (E015).
