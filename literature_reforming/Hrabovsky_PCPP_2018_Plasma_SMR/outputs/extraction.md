# Hrabovsky et al. (2018): steam and dry methane reforming in a ~100 kW water/argon-stabilized DC arc plasma

## Source and review

- Source ID: **SRC007**. M. Hrabovsky, M. Hlina, V. Kopecky, A. Maslani, P. Krenek, A. Serov and O. Hurba, "Steam plasma methane reforming for hydrogen production," Plasma Chemistry and Plasma Processing 38 (2018) 743-758. DOI: https://doi.org/10.1007/s11090-018-9891-5. Institute of Plasma Physics, Czech Academy of Sciences.
- Documents: supplied published [manuscript.pdf](../manuscript.pdf), 16 pages (printed pp. 743-758; PDF page = printed page - 742). No ESI located (search by BB, 2026-11-05). Retrieval date unknown.
- SHA-256 manuscript.pdf: `078cd4abf0a03e8629aee8c52fcb5e5015f2e3bb38944fbf48f6357a8a85c0cd`
- Protocol 0.1 (with 2026-11-04 amendment). Extractor/reviewer: Claude (AI), 2026-11-05, same-extractor checks. Status: **ai_checked; human verification pending**.
- Coverage: full text read; all figures inspected. Selected matched operating points from Figs. 7 and 8 (all eight segments) and the authors' plotted relations in Figs. 9-16. Section 2 (equilibrium calculations, Figs. 1-5) is modelling and is recorded only for the theoretical minimum energy.
- Records: [evidence.csv](evidence.csv), 51 records (SRC007-E001-E039 source records; E041-E052 reviewer calculations). Reviewer calculations C001-C008 in [calculations.py](calculations.py). Evidence IDs below are abbreviated (E001 = SRC007-E001).
- Selection: record R001 in [../../search_and_selection_log.md](../../search_and_selection_log.md). Folder renamed 2026-11-05 from `Harbovsky_2018_PCPP_Plasma_SMR_100kW` to the workflow naming convention.

## Electricity supply

**Classification: thermal plasma (DC arc torch, hybrid argon/water-vortex stabilization) used as the sole heat and activation source; no catalyst, no external furnace or steam generator.** Reactants (CH4, CO2, liquid water) are injected into the 200 L reactor and mixed with the plasma jet (E001, E008, E038).

| Quantity | Extraction | Evidence |
|---|---|---|
| Plasma scale (arc power) | 88-136 kW overall; 120 kW in the steam reforming run (Fig. 7); 89-116 kW in the dry reforming run (Fig. 8) | E003, E015, E016 |
| Arc current | 325-450 A; 400 A in Fig. 7 | E002, E015 |
| Torch efficiency | 0.57-0.60 (printed with a % unit; read as a fraction), so plasma jet power is about 57-60% of arc power | E005 |
| Plasma jet | 0.37-0.44 g/s; mean enthalpy 136-186 MJ/kg; bulk temperature 15,400-16,300 K; H2O/Ar volume ratio 2.2-3.0 | E006 |
| Power measurement | "Monitoring of the plasma torch operation parameters" and calorimetry on cooling-water loops; voltage/current instrumentation not described | E004 |
| Total process energy scale | Arc power is the largest input. Rectifier/supply losses, water pumps, water-jet ejector, quench spray, argon supply and afterburner are not reported | E004, E011 |

**Power boundaries.** Three boundaries appear and must not be mixed:

1. **Arc power** (torch electrical input; our primary power basis). Used by the authors for their "total energy" figure (192 MJ/kg H2, E031).
2. **Plasma jet power** = arc power x torch efficiency (0.57-0.60). Not reported per point; reviewer range in C005.
3. **Process enthalpy** (author's metric, Eq. 12) = (torch power - torch loss - reactor loss) / mol CH4 fed: the energy actually absorbed by the reacting stream. All the authors' figure relations (Figs. 9-16) and their 79-116 MJ/kg costs use this basis (E007, E030).

The water reactant is fed as **liquid** and heated/evaporated in the reactor by the plasma (Eq. 4 uses liquid water; E038). Arc power therefore already covers steam generation; there is no separate external heat input to add.

## Reactor configuration

PLASGAS reactor: torch mounted at the top of a 200 L refractory reactor (also used for biomass and waste gasification), followed by a quenching chamber (water spray to 300 degC), filter, scrubber, water-jet ejector (reactor held a few hundred Pa below ambient) and an afterburner (E008, E011). No catalyst. Reactant injection positions and reactor dimensions other than volume are not given. Residence time 18-35 s from measured flows (E033).

## Operating conditions

Feeds: CH4 75-150 slm; CO2 51-134 slm (dry reforming); liquid water 38-94 g/min (steam reforming); argon tracer 50 slm (E009, E014). Reference conditions for slm are not stated; 0 degC, 1 atm assumed (20 degC sensitivity in C007). Pressure about atmospheric (slight under-pressure, E011). Reactor temperature "kept between 1200 and 1400 K" by adjusting power and feeds; location and method unstated and no point values (E010).

Matched operating points (all from two short test runs; each segment lasts about 2-5 min):

| OP | Route | Arc power (kW) / current (A) | CH4 (slm) | CO2 (slm) | H2O (g/min) | Evidence |
|---|---|---|---|---|---|---|
| OP001 | SMR | 120 / 400 | 150 | 0 | 94 | E015, E017 |
| OP002 | SMR | 120 / 400 | 75 | 0 | 38 | E015, E018 |
| OP003 | SMR | 120 / 400 | 125 | 0 | 75 | E015, E019 |
| OP004 | SMR | 120 / 400 | 100 | 0 | 56 | E015, E020 |
| OP005 | DRM (+plasma steam) | 116 / 400 | 125 | 101 | 18 | E016, E021 |
| OP006 | DRM (+plasma steam) | 97 / 350 | 125 | 101 | 18 | E016, E022 |
| OP007 | DRM (+plasma steam) | 107 / 375 | 125 | 101 | 18 | E016, E023 |
| OP008 | DRM (+plasma steam) | 89 / 325 | 125 | 101 | 18 | E016, E024 |

**Steam-to-carbon.** The added water gives H2O/CH4 0.63-0.78 (C001). The authors say water was added "to reach ratio of methane to steam corresponding to the Eq. (1)" (1:1). Adding about 18 g/min (1.0 mol/min) of plasma steam brings all four SMR points to 0.92-0.93, which supports reading the Fig. 7 water flows as *excluding* plasma steam (reviewer interpretation). Either way S/C is about 1, far below industrial S/C 2.5-3.

**Route classification.** The "dry reforming" runs contain about 18 g/min water (H2O/CH4 about 0.18 against CO2/CH4 0.81), which the authors attribute to plasma steam; they state the conditions "do not correspond exactly to Eq. (2)" (E016, p. 8). Strictly this is mixed reforming with a dominant CO2 share; we label these rows **DRM (+plasma steam)** and recommend synthesising them with DRM, flagged. The steam reforming rows also contain plasma argon and the 50 slm argon tracer (inert).

## Performance indicators

### Figure reading method

The paper tabulates no results. Outlet compositions (dry, mole %) for OP001-OP008 were read from the mass-spectrometer traces in Figs. 7 and 8 by reviewer pixel-colour digitisation of the embedded 300 dpi images: axis calibrated on the 10%-step gridlines; each trace's median height taken over the steady central part of each segment. Precision about +/-0.3 percentage points for major species; low traces (<1%) overlap the axis and are +/-0.5 points. CO2 in SMR segments OP002-OP004 is below 0.5% and could not be resolved (0.3% used). Compositions sum to 99.8-100.8% (C001), and the 325 A segment that appears twice in Fig. 8 reads identically (E024). Outlet molar flow is the argon tracer flow / argon mole fraction (the authors' method, E013).

### Results at matched points (reviewer calculations C001-C004)

| OP | X_CH4 (%) | X_CO2 (%) | C closure (%) | H2 out (kg/h) | H2/CO | Evidence |
|---|---|---|---|---|---|---|
| OP001 | 91.3 | NA | 97 | 2.18 | 3.21 | E041, E045 |
| OP002 | 99.1 | NA | 101 | 1.17 | 2.92 | E042, E045 |
| OP003 | 95.4 | NA | 94 | 1.93 | 3.25 | C003 |
| OP004 | 97.0 | NA | 96 | 1.55 | 3.14 | C003 |
| OP005 | 95.3 | 91.0 | 99 | 1.40 | 1.25 | E043, E045 |
| OP006 | 89.4 | 91.6 | 90 | 1.18 | 1.19 | C003 |
| OP007 | 93.1 | 89.9 | 97 | 1.30 | 1.20 | C003 |
| OP008 | 83.3 | 89.0 | 94 | 1.08 | 1.11 | E044, E045 |

**Cross-checks with the authors' own points.** OP008 (83.3/89.0%) matches the lowest-enthalpy dry reforming point in Fig. 10 (about 82.7/88.8% at ~355 kJ/mol); OP005 (95.3/91.0%) matches the point near 560 kJ/mol (about 95.8/91.5%). OP001 (91.3%) is consistent with the lowest steam point in Fig. 9 (about 91.5% at ~480 kJ/mol). H2/CO values are within the authors' stated 3-3.4 (steam) and 1.1-1.2 (dry) ranges, apart from OP002 (2.92) (E028). The authors report no conversions at stated feed/power, only against process enthalpy.

Author headline maxima, not matched to one point: CH4 conversion up to 99.5%, H2 selectivity up to 99.9%, CO2 conversion at most 93% (E027, E029). Conversion falls below about 700-800 kJ/mol process enthalpy (E026-E027). Small amounts of solid carbon were collected; no liquids (E034). Composition near equilibrium (E036).

### Energy metrics

- **Power-basis metrics (arc power; no external heat to add, since water is evaporated by the plasma; 0 degC slm):**

| OP | P_arc (kW) | SEI_CH4 (kJ/mol) | EC_CH4 (kJ/mol) | EC_CH4 jet basis (kJ/mol) | EC_H2 (MJ/kg) | EY_H2 (g/kWh) | eta_P,LHV (%) |
|---|---|---|---|---|---|---|---|
| OP001 | 120 | 1076 | 1179 | 672-707 | 198 | 18.2 | 49.3 |
| OP002 | 120 | 2152 | 2172 | 1238-1303 | 369 | 9.8 | 33.3 |
| OP003 | 120 | 1291 | 1354 | 772-812 | 224 | 16.1 | 45.8 |
| OP004 | 120 | 1614 | 1664 | 948-998 | 279 | 12.9 | 39.8 |
| OP005 | 116 | 1248 | 1309 | 746-786 | 299 | 12.1 | 48.3 |
| OP006 | 97 | 1044 | 1167 | 665-700 | 297 | 12.1 | 47.4 |
| OP007 | 107 | 1151 | 1237 | 705-742 | 296 | 12.1 | 48.4 |
| OP008 | 89 | 958 | 1149 | 655-689 | 297 | 12.1 | 48.9 |

  All EC_CH4 values are 4.6-10 times the 206 kJ/mol (SMR) or 247 kJ/mol (DRM) reaction enthalpies. They include heating the products to 1200-1400 K and evaporating the water, none of which is recovered (the gas is water-quenched). Jet-basis values use the torch efficiency range (not point-specific; C005).
- **Process (author) basis:** EC_CH4 = process enthalpy / X_CH4 from the authors' plotted points: SMR about 525 kJ/mol (480 kJ/mol, 91.5%) to 926 (920 kJ/mol, 99.4%); DRM about 429 (355 kJ/mol, 82.7%) to 994 (C008, E051). Excludes torch and reactor losses (arc power x ~0.4-0.6).
- **Author energy metric:** H2 energy cost = energy per kg H2 produced. Process basis: minimum 79 MJ/kg (steam, Conclusions; = 158 kJ/mol in the abstract) or 86 MJ/kg (steam, Results text); 116 MJ/kg (dry) (E030). Arc-power basis: minimum 192 MJ/kg for steam reforming (E031). Our OP001 gives 198 MJ/kg on the same basis, within 3% (C004), which supports both the figure readings and the assumption that the 50 slm argon is the total argon in the reactor.
- **Whole-system eta_HHV (partial):** (H2 + CO HHV) / (arc power + CH4 feed HHV) = 51.3% (OP001), 36.4% (OP002), 49.7% (OP005), 46.9% (OP008); f_electric 0.52-0.71 (C006, E052). Partial because rectifier losses and auxiliaries (water pumps, ejector, quench water, argon supply) are excluded; the boundary is otherwise complete for the reactor (no external heat or steam). Unconverted CH4 excluded from products. Reformer-level syngas, no shift or H2 purification.
- **Energy completeness:** included: arc power, heating and evaporating water, torch and reactor heat losses (in arc power). Omitted/unknown: power-supply losses, auxiliary electricity, argon production, heat recovery (none; product gas quenched with water).

## Reporting quality

| Item | Answer | Reason and evidence IDs |
|---|---|---|
| Q1 Power measurement | partly | Arc power given per point (Figs. 7-8) and torch losses by calorimetry, but voltage/current measurement and averaging not described; torch efficiency only as a range (E003-E005, E015-E016). |
| Q2 Feed definition | partly | Feeds per point given in slm and g/min, but slm reference conditions not stated, plasma Ar/H2O flows only as ranges, and whether water flows include plasma steam is implicit (E006, E009, E015-E016). |
| Q3 Product analysis | partly | On-line QMS on a dry basis with an argon tracer for flow; calibration not described; CO not separated from N2 (m/z 28) in Fig. 8 (E012-E013). |
| Q4 Balance closure | no | No carbon or elemental balance reported; solid carbon not quantified. Reviewer carbon closure 90-101% (E034, E045). |
| Q5 Temperature | partly | Reactor 1200-1400 K stated as a controlled range; wall and quench thermocouples mentioned; no point values or locations (E010-E011). |
| Q6 Controls | partly | Thermal plasma: the relevant control is thermodynamic equilibrium, and the authors compare measured composition with equilibrium calculations qualitatively; no conventional-reactor comparison at matched conditions (E032, E036). |
| Q7 Repeatability | no | No repeats, error bars or uncertainties stated. A repeated 325 A segment in Fig. 8 reads the same (E024), but the authors do not present it as a repeat. |
| Q8 Stability | partly | Steady composition within 2-5 min segments and 30 s response after changes; no total time on stream, endurance test, or torch/electrode life (E035). |
| Q9 Energy completeness | partly | Arc power, torch and reactor losses and water evaporation covered (no external heat); supply losses and auxiliaries not reported (E004, E007, E038). |

- **Confidence in conversion/product results: moderate.** Matched feeds and powers with a tracer-based flow measurement, and our readings reproduce the authors' plotted conversions, but all values are graph-read from time traces, calibration is undescribed and there is no balance closure.
- **Confidence in energy results: moderate.** Arc power is point-matched and our calculation reproduces the authors' 192 MJ/kg total, but the slm reference, torch efficiency per point and auxiliary loads are not reported.

## Reported system information

- **Boundary:** authors' energy accounting covers the torch and reactor (arc power, torch loss, reactor loss); downstream quench, filter, scrubber, ejector and afterburner are described but their energy and water use are not given (E004, E007, E011).
- **Mass flows:** inlet CH4, CO2, water and argon given per point; outlet dry composition and argon-tracer flow; water content of product, solid carbon mass and outlet water not reported. No mass balance reported.
- **Energy flows:** arc power per point; torch efficiency range; reactor loss not reported per point; no energy balance table. Product gas is quenched with water from about 1200-1400 K to 300 degC: its sensible heat is not recovered.
- **Hardware:** 200 L reactor; hybrid water/argon DC torch (88-136 kW); quench chamber, filter tower, scrubber, water ejector, afterburner. Torch requires cooling water and argon; electrode/cathode lifetime, maintenance and costs not reported. Pilot-scale research facility shared with gasification work, not a dedicated reformer design.

## Missing information and comparison limits

| Field | Status |
|---|---|
| slm reference temperature/pressure | not_reported (0 degC assumed; +7% in energy metrics at 20 degC) |
| Whether 50 slm Ar includes plasma-forming Ar | unclear (C007: up to -1.3 points X_CH4, -13% EC_H2 if not) |
| Whether Fig. 7 water flows include plasma steam | unclear (reviewer interpretation: excluded) |
| Torch efficiency and reactor loss per operating point | not_reported |
| Reactor temperature per point; gas temperature location | not_reported |
| Product analysis calibration; CO/N2 separation | not_reported |
| Carbon/elemental balance; solid carbon mass | not_reported |
| Power supply (rectifier) efficiency; auxiliary electricity | not_reported |
| Time on stream; torch electrode lifetime | not_reported |
| Uncertainties/repeats | not_reported |
| ESI | none located |

Comparison limits: S/C about 1 (vs 2.5-3 in conventional SMR); no catalyst; outlet gas at 1200-1400 K quenched without heat recovery, so the high EC_CH4 partly reflects unrecovered sensible heat rather than chemistry alone. Results are short steady segments in two test runs. Conflicting author minima: 79 vs 86 MJ/kg (steam) and "at 500 kJ/mol" vs Fig. 16's lowest dry point near 355 kJ/mol (E030).

## Calculations

All in [calculations.py](calculations.py); run `python3 calculations.py` to reproduce.

| ID | Inputs | Method | Result | Limitations |
|---|---|---|---|---|
| C001 | E015-E024 | Figure readings; feeds to mol/min (0 degC slm); H2O/CH4 from added water | Table above; H2O/CH4 0.63-0.78 (SMR, added water), 0.18 (DRM) | Graph-read |
| C002 | E013-E014, E017-E024 | F_out = 50 slm / x_Ar | 342-595 slm dry | Ar basis (C007) |
| C003 | C002 | X_i = 1 - x_i F_out / F_i,in; C closure = (CH4+CO+CO2)out / (CH4+CO2)in | See results table | Solid carbon excluded |
| C004 | C003, E015-E016 | SEI_CH4, EC_CH4, EC_H2, EY_H2, eta_P,LHV on arc power (workflow section 4) | See energy table | LHV 241.8/283.0/802.3 kJ/mol |
| C005 | C004, E005 | EC_CH4 x torch efficiency 0.57-0.60 | Jet-basis range | Efficiency not point-specific |
| C006 | C003-C004 | eta_HHV = (H2, CO HHV)/(P_arc + CH4 HHV) | 36-51% | Partial boundary |
| C007 | E005-E006 | Plasma Ar 5.3-7.4 slm from jet mass flow and H2O/Ar ratio; 20 degC slm | Sensitivities listed | Estimate |
| C008 | E026-E027 | Process enthalpy / X_CH4 from author points | 429-994 kJ/mol | Graph-read |

## Revisions

- 2026-11-05: source folder renamed to Hrabovsky_PCPP_2018_Plasma_SMR (was Harbovsky_2018_PCPP_Plasma_SMR_100kW); no evidence IDs or values changed.

## Plasma characteristics

| Characteristic | Reported |
|---|---|
| Regime | Thermal plasma; DC arc in contact with a water vortex plus argon flow (hybrid water/gas stabilization); described as extremely high enthalpy, low mass flow (E001, E006) |
| Gas temperature | Plasma jet "bulk plasma temperature" 15,400-16,300 K at torch exit; method not stated (probably derived from enthalpy) (E006). Reactor gas 1200-1400 K (location/method not stated) (E010). Quench inlet/outlet thermocouples, values not reported except 300 degC outlet (E011) |
| Mean plasma enthalpy | 136-186 MJ/kg (E006) |
| Electron temperature/density, E/N, ionization degree | not reported |
| Diagnostic basis | Torch parameters and calorimetry; no optical diagnostics in this paper. Details of the torch in the authors' refs 31-32 |
