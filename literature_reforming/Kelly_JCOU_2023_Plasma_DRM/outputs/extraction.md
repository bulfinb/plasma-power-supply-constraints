# Kelly et al. (2023): dry reforming of methane in a 1 kW, 2.45 GHz atmospheric-pressure microwave plasma

## Source and review

- Source ID: **SRC011**. Sean Kelly, Elizabeth Mercer, Robin De Meyer, Radu-George Ciocarlan, Sara Bals and Annemie Bogaerts, "Microwave plasma-based dry reforming of methane: Reaction performance and carbon formation," Journal of CO2 Utilization 75 (2023) 102564. DOI: https://doi.org/10.1016/j.jcou.2023.102564. Open access (CC BY). University of Antwerp (PLASMANT, EMAT, LADCA) and University College Dublin.
- Documents: [manuscript.pdf](../manuscript.pdf), 12 pages (printed = PDF page). No ESI located; data available on request (E022). Retrieval date unknown.
- SHA-256 manuscript.pdf: `aff4decadf2631881e752644ece24056f6604e2fb04c13dcaca2a8f1efa7b0fe`
- Protocol 0.1 (with 2026-11-04 amendment). Extractor/reviewer: Claude (AI), 2026-11-05, same-extractor checks. Status: **ai_checked** (human_verified withdrawn 2026-11-10). Partial human check by BB, 2026-11-26: headline OP004 (E003, E004, E013; 1 kW fixed power, 10 nL/min, 45:55 results) confirmed; no changes (human_checks/summary.csv). Other records human verification pending.
- Coverage: full text, Table 1 and Figs. 1-6. Numerical values taken from the text and Table 1 (which carry stated uncertainties); figures not digitised. Literature rows of Table 1 are not extracted as evidence, but identify further candidates (see search log).
- Records: [evidence.csv](evidence.csv), 27 records (SRC011-E001-E022 source; E041-E045 reviewer calculations). Calculations C001-C002 in [calculations.py](calculations.py).
- Selection: record R005 in [../../search_and_selection_log.md](../../search_and_selection_log.md).

## Electricity supply

**Classification: atmospheric-pressure 2.45 GHz surface-wave microwave plasma ("warm plasma filament"), electrode-free, no catalyst, no external heating.**

| Quantity | Extraction | Evidence |
|---|---|---|
| Plasma scale | 1 kW absorbed microwave power at all operating points | E003 |
| Supply | Solid-state LDMOS 2.45 GHz source, WR340 waveguide, isolator, auto-tuner, sliding short | E001 |
| Power measurement | Six-port reflectometer (S-TEAM Homer auto-tuner); reflected power < 1% | E002 |
| Total process energy scale | Absorbed power is effectively the only energy input (no preheat or steam); solid-state source wall-plug efficiency and cooling not reported | E001 |

## Reactor configuration

16 mm ID quartz tube through a 20 mm coupling hole in a tapered WR340 section; swirl injection via a helical insert; the plasma filament sits at the tube centre, away from the walls (E005). Carbon deposits on the downstream tube wall at higher CH4 fractions. No catalyst.

## Operating conditions

All points: atmospheric pressure, 1 kW, 10 nL/min total CO2 + CH4 (24.05 L/mol reference, i.e. 20 degC), SEI 6 kJ/L (E003-E004, E009). Gas analysis after the exhaust temperature reached steady state (~15 min) (E006). Total time on stream not reported. 50/50 CO2/CH4 was unstable and extinguished (E016).

| OP | CO2/CH4 (%) | CH4 (mol/min) | Evidence |
|---|---|---|---|
| OP001 | 70/30 | 0.125 | E010 |
| OP002 | 65/35 | 0.146 | E011 |
| OP003 | 60/40 | 0.166 | E012 |
| OP004 | 55/45 | 0.187 | E013 |

Exhaust gas temperature ~15 cm downstream: 726 / 687 / 677 K at OP001 / OP003 / OP004 (E017).

## Performance indicators

| OP | X_CO2 (%) | X_CH4 (%) | X_tot (%) | H2/CO | H2O (%, O balance) | C2H2 (%) | Author EC (eV/molecule; kJ/L) | Evidence |
|---|---|---|---|---|---|---|---|---|
| OP001 | 49.4 +/- 1.8 | 66.5 +/- 1.7 | 53.5 +/- 1.7 | 0.56 | 13.6 +/- 3.2 | ~0.70 | 2.8 +/- 0.1; 11.1 | E010, E014 |
| OP002 | 49 | 63 | 53 | NR | 12.1 +/- 3.3 | NR | 2.8 | E011, E014 |
| OP003 | 46.2 +/- 2.3 | 58.0 +/- 1.8 | 50 | NR | 7.2 +/- 4.7 | NR | 2.9 | E012, E014 |
| OP004 | 45.8 +/- 2.5 | 55.2 +/- 1.5 | 49.6 +/- 2.1 | 1.01 | 6.7 +/- 5.2 | ~1.58 | 3.0 +/- 0.1; 11.9 | E013-E014 |

Conversions are corrected for gas expansion with a measured factor alpha (O2 probe gas, plasma ON vs OFF) (E008). Exhaust mole fractions at OP001: CO 41.0%, H2 23.0% (dry). Water is inferred from the O balance (not measured), so O closes by construction; cumulative C selectivity 0.94-0.97 and H selectivity ~1.04, both with large errors (E015). C2H4, C2H6 and solid carbon were not measured. Solid carbon is described as a small (<1%) but important by-product: it destabilises the plasma above ~45% CH4 and deposits on the tube. It is characterised as metal-free amorphous carbon black with 21 nm primary particles (E018).

Small inconsistency: X_tot recomputed from Eq. (4) with the stated individual conversions is ~1 point higher than the stated X_tot (e.g. 54.5 vs 53.5% at 70/30), within the stated uncertainty (C001).

### Energy metrics

- **Power-basis metrics (absorbed microwave power; no external heat; C001-C002):**

| OP | SEI_CH4 (kJ/mol) | EC_CH4 (kJ/mol CH4 conv.) | EC per mol CH4+CO2 converted (kJ/mol; eV) | EC_H2 (kJ/mol) | EY_H2 (g/kWh) | eta_P,LHV (%) |
|---|---|---|---|---|---|---|
| OP001 | 481 | 723 | 270; 2.80 | 522 | 13.9 | 67.8 |
| OP002 | 412 | 654 | 272; 2.82 | NR | NR | NR |
| OP003 | 361 | 622 | 289; 2.99 | NR | NR | NR |
| OP004 | 321 | 581 | 291; 3.02 | 330 | 22.0 | 66.4 |

  EC per molecule reproduces the authors' 2.8-3.0 eV. For DRM, EC per mol CH4 converted (our primary metric) charges all the power to CH4 although about half the converted molecules are CO2; compare DRM sources on the per-molecule metric as well. H2 and CO flows are derived from the authors' syngas energy cost (Eq. 8); they reproduce the authors' H and C selectivities within 0.02 (C002). Derived alpha = 1.20 at OP001.
- **Author metrics:** EC_tot = SEI / X_tot (kJ/L and eV/molecule of CO2+CH4 converted), 2.8-3.0 eV; EC_syngas = SEI / syngas produced, 1.9-1.7 eV (7.8-6.9 kJ/L) (E009-E010, E013). Compared with a 4.27 eV/molecule (60% efficiency) competitiveness target (E020).
- **eta_HHV (partial):** 53.1% (OP001), 45.4% (OP004); f_electric 0.35 / 0.26; excludes source losses and cooling (E044).
- **Energy completeness:** absorbed microwave power is the only process energy input; wall-plug efficiency of the solid-state source not reported. Exhaust heat (~700 K at 15 cm) not recovered.

## Reporting quality

| Item | Answer | Reason and evidence IDs |
|---|---|---|
| Q1 Power measurement | yes | Absorbed power by six-port reflectometer; reflected < 1% (E002). |
| Q2 Feed definition | yes | Flow, composition and molar-volume reference stated (E004, E009). |
| Q3 Product analysis | yes | NDIR/TCD with external calibration standards; gas expansion measured with an O2 probe (E007-E008). C2H4/C2H6 and water not measured. |
| Q4 Balance closure | partly | O balance used to infer water (closes by construction); C and H cumulative selectivities 0.94-1.04 reported with large errors; solid carbon not quantified (E014-E015, E018). |
| Q5 Temperature | partly | Exhaust temperature at ~15 cm by thermocouple; no plasma or near-plasma gas temperature (E017). |
| Q6 Controls | no | No thermal or catalytic comparison; plasma OFF used only as the inlet reference. Literature comparison only (E019). |
| Q7 Repeatability | partly | Uncertainties given for most values, but their basis (repeats, standard deviation) is not stated. |
| Q8 Stability | partly | Steady-state criterion (exhaust temperature after ~15 min); total time on stream not reported; 50/50 unstable (E006, E016). |
| Q9 Energy completeness | partly | No external heat; source wall-plug efficiency and cooling not reported. |

- **Confidence in conversion/product results: higher.** Calibrated analysers, measured gas expansion, stated uncertainties and atom-balance checks; water and minor products inferred or missing.
- **Confidence in energy results: higher.** Absorbed power measured with a stated method at matched conditions and no external heat; only the wall-plug boundary is missing.

## Reported system information

- **Boundary:** microwave source to exhaust; analysis of cooled, dried exhaust.
- **Mass flows:** inlet CO2/CH4; outlet dry composition with alpha; water inferred; solid carbon unquantified.
- **Energy flows:** absorbed microwave power; exhaust temperature only.
- **Hardware:** solid-state 2.45 GHz source (power rating not stated; operated at 1 kW), 16 mm quartz tube. Electrode-free design avoids erosion; carbon deposition on the tube and plasma extinction at high CH4 are the main operating limits. No lifetime or costs. Authors suggest carbon black could be a saleable by-product (E018).

## Missing information and comparison limits

| Field | Status |
|---|---|
| Wall-plug power / source efficiency | not_reported |
| Time on stream beyond ~15 min steady state | not_reported |
| Solid carbon quantity; C2H4, C2H6 | not_reported |
| Water (measured) | not_reported (inferred) |
| Plasma gas temperature | not_reported (exhaust at 15 cm only) |
| alpha values | not_reported (derived by reviewer) |
| Basis of uncertainties | unclear |
| ESI | none located |

Comparison limits: 1 kW lab scale (smallest on the shortlist); DRM only at a single power and flow; CH4 limited to 45% by carbon formation. Energy costs per molecule are directly comparable with the DRM literature (Fig. 3 / Table 1); EC_CH4 is higher than per-molecule values by construction.

## Calculations

| ID | Inputs | Method | Result |
|---|---|---|---|
| C001 | E003-E004, E009-E013 | SEI_CH4, EC_CH4, EC per molecule converted; X_tot check | 581-723 kJ/mol CH4; 2.80-3.02 eV |
| C002 | E010, E013, E015 | Syngas flows from EC_syngas; EC_H2, EY_H2, eta_P,LHV, partial eta_HHV; selectivity check | See energy table |

## Revisions

- 2026-11-05: extraction informally reviewed by BB and marked human_verified. No values changed.
- 2026-11-10: human_verified status withdrawn at BB's request; returned to ai_checked pending a systematic human check. The 2026-11-05 BB review was informal. No values changed.

## Plasma characteristics

| Characteristic | Reported |
|---|---|
| Regime | Surface-wave sustained, contracted "warm" plasma filament at tube centre (~one skin depth), continuous 2.45 GHz (E005, E021) |
| Gas temperature | Not measured in the plasma. Exhaust plume ~15 cm downstream: 677-726 K (K-type thermocouple; placed at a "safe distance" to avoid coupling) (E017) |
| Other temperatures | Incandescent carbon particles > 1500 K, inferred from colour only (E021) |
| Electron temperature/density, E/N, ionization | not reported |
| Diagnostic basis | Visual imaging of the discharge; carbon characterised ex situ by SEM/EDX, Raman, TGA (E018) |
