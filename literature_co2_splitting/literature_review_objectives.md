# Literature review objectives: electrified CO2 splitting

Version 0.1 - 2026-11-09.

Part of the electrified endothermic processes review (see [../README.md](../README.md)). Sibling topics: [../literature_reforming/](../literature_reforming/) and [../literature_pyrolysis/](../literature_pyrolysis/). Extraction follows [workflow.md](workflow.md) and [_source_template.md](_source_template.md).

## Main objective

To benchmark plasma CO2 splitting (CO2 -> CO + 1/2 O2), using published experimental evidence, against the main electrified alternatives for making CO from CO2, high-temperature electrolysis (SOEC) and electrolytic H2 plus reverse water-gas shift (RWGS); and to assess what the plasma route would require at industrial scale, from wall electricity to product.

**Conversion is as important as energy efficiency here.** Single-pass CO2 conversion sets the size and energy of the downstream separation (CO from O2 and unconverted CO2) and recycle. A plasma result with good energy efficiency at 10-20% conversion is not equivalent to SOEC or RWGS at high conversion. Conversion and efficiency are therefore always reported and plotted together, never efficiency alone.

The review has two parts:

1. **Demonstrated performance.** A traceable comparison of what has been demonstrated, under which conditions, on a stated power boundary, and what information is missing.
2. **Scale-up and whole-system view.** Plasma reactors scaled up with representative industrial power supplies ([../power_systems/notes/scaleup_assessment.md](../power_systems/notes/scaleup_assessment.md)): supply and coupling losses, heat integration, CO/O2/CO2 separation (often omitted but energy-intensive at low conversion), durability and cost. Unrecoverable delivery losses of ~20% are significant in an optimised plant.

CO2 splitting differs from the other two topics in its benchmark. Direct thermal splitting needs temperatures far above what Joule-heated reactors reach, so the electrified competitor is electrochemical (SOEC), not resistive heating. This tests whether the review's conclusions on supply losses and heat recovery hold against a non-thermal competitor.

## Review approach: exemplary studies

This topic is not reviewed comprehensively. The aim is a set of **5-10 exemplary plasma studies** that together show the state of the art in performance against the benchmarks, plus the benchmarks themselves. Choose exemplars so that, between them, they:

- show the best demonstrated performance on the primary metrics at matched operating points (X_CO2 and EC_CO2 together; high-conversion results count as much as high-efficiency ones);
- span the main plasma types (microwave, gliding arc, glow/arc, DBD, nanosecond pulsed) and pressures and the largest demonstrated scales;
- report enough (point-matched power, feed, products, power boundary) for the metrics below to be calculated and traced.

Recent critical reviews are used to locate candidates and the field's conventions. Each exemplar is extracted in full with the shared workflow; screening records explain why a candidate was or was not chosen.

## Scope

- Route: CO2 -> CO + 1/2 O2, +283 kJ/mol CO2 (298 K) = 2.93 eV/molecule.
- Pure CO2 or CO2 with inert diluent (Ar, He, N2: record it). CO2 with H2, CH4 or H2O co-feed is out of scope (CO2 + CH4 is DRM, in literature_reforming).
- Activation: all plasma types (microwave, gliding arc, glow, DBD, nanosecond pulsed, RF, arc), with or without catalysts or O2-conducting membranes.
- Reported CO/O2 separation steps are recorded; whole-system products are defined as CO at a stated purity.

**Benchmarks** (selected directly, not searched; one or two only):

- **SOEC CO2 electrolysis** at commercial or pilot scale (e.g. Topsoe eCOs on-site CO generation), with electricity per Nm3 CO, single-pass conversion and product purity; data type labelled (vendor, measured, design).
- **Electrolytic H2 + RWGS** (CO2 + H2 -> CO + H2O, +41 kJ/mol): not sourced or extracted from the literature (decision 2026-11-12). With excess H2 the product is syngas, not CO, so a literature design study is not a like-for-like benchmark per mol CO; the route is treated separately in the synthesis. No RWGS source is to be extracted.
- **Thermodynamic reference**: 283 kJ/mol enthalpy and the free-energy minimum (257 kJ/mol at 298 K) as reference lines.

Industrial or pilot plasma data, if any, are collected as reference systems: e.g. D-CRBN (University of Antwerp spin-off, BluePlasma consortium). As standard practice, record declared competing interests and author affiliations with spin-offs in each extraction (no concern about any specific group is implied).

## Questions the review should answer

1. What plasma arrangements have been demonstrated, and at what scale and pressure?
2. What feed, flow, pressure, power and quenching or separation conditions were used?
3. What CO2 conversion and energy efficiency were achieved together, at matched conditions, and what CO production rate? What is the best conversion at an acceptable energy cost for each plasma type?
4. How long were systems operated, and what degradation (electrodes, walls, catalysts) was reported?
5. How do the results compare with SOEC and H2 + RWGS, on conversion as well as energy, and what missing information limits that comparison?

## Energy performance indicators

Used in workflow.md section 4 (the field's standard metrics, kept with our explicit boundary):

X_CO2 (expansion-corrected, single pass) is a co-primary metric with EC_CO2: record it at every operating point with its correction method. Where a paper reports product separation or recycle, record its energy and the resulting overall conversion.

```text
SEI      = P / F_CO2,in                 (kJ/mol, also eV/molecule; diluent excluded from F unless stated)
X_CO2    = conversion, expansion-corrected (record correction method)
EC_CO2   = P / F_CO2,conv               (kJ/mol CO2 converted; primary)
EC_CO    = P / F_CO,out                 (kJ/mol CO); also kWh/Nm3 CO for SOEC comparison
eta_dH   = X_CO2 * 283 / SEI(kJ/mol)    (the field's "energy efficiency"; record the author's dH value)
```

Many papers report SEI per molecule of total gas including diluent; recalculate on CO2 when the diluent fraction is known. Gas-expansion correction is a known source of overestimated conversion in this literature; record it under reporting quality (Q3).

## Synthesis plan

Evidence table, X_CO2 vs EC_CO2 as the main plot (and eta_dH vs SEI) by plasma type and pressure, with SOEC and RWGS conversion/energy shown on the same axes, scale plot, whole-system table including separation where reported, reporting-quality summary, narrative. SOEC shown as a reference band with its data type.

## Scale-up and whole-system assessment

Wall-basis EC_CO2 and EC_CO with representative supplies, then product separation and recycle as a function of single-pass conversion, then heat integration, then cost and durability. Demonstrated values and estimates stay separate.

## Version history

- 0.1 (2026-11-09): initial objectives.
- 0.1 amendment (2026-11-09): selective review of 5-10 exemplary studies against the benchmarks, not a comprehensive review; conversion made co-primary with energy efficiency; H2 + RWGS added as a benchmark; conflict-of-interest wording neutralised.
- 0.1 amendment (2026-11-12): H2 + RWGS benchmark no longer sourced from literature (see Benchmarks); SOEC benchmarks extracted as SRC025-SRC026.
