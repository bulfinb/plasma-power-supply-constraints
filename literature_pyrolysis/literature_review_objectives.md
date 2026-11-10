# Literature review objectives: electrified methane pyrolysis and coupling

Version 0.1 - 2026-11-09.

Part of the electrified endothermic processes review (see [../README.md](../README.md)). Sibling topics: [../literature_reforming/](../literature_reforming/) and [../literature_co2_splitting/](../literature_co2_splitting/). Extraction follows the shared [../literature_reforming/workflow.md](../literature_reforming/workflow.md) and [../literature_reforming/_source_template.md](../literature_reforming/_source_template.md), with the route-specific metrics below.

## Main objective

To benchmark plasma methane pyrolysis and non-oxidative coupling, using published experimental and industrial evidence, against electrically (Joule) heated pyrolysis and against hydrogen from fired SMR; and to assess what each electrified route would require at industrial scale, from wall electricity to product.

The two parts mirror the reforming review:

1. **Demonstrated performance.** A traceable comparison of what has been demonstrated, under which conditions, on a stated power boundary, and what information is missing.
2. **Scale-up and whole-system view.** Each reactor type scaled up with representative industrial power supplies ([../power_systems/notes/scaleup_assessment.md](../power_systems/notes/scaleup_assessment.md)): supply and coupling losses, heat integration (hot H2 and carbon leave at high temperature), carbon handling, durability and cost. Unrecoverable delivery losses of ~20% are significant in an optimised plant.

Pyrolysis is the topic in this review with the strongest industrial plasma precedent. Industrial data are therefore collected deliberately, not only as background:

- **Monolith** (plasma methane pyrolysis to carbon black and H2, Nebraska; commercial).
- **Hüls arc process** (electric-arc acetylene from hydrocarbons, Marl, ~1940 to 1990s; multi-MW arcs).
- Earlier and other thermal plasma carbon black / H2 processes (e.g. the Kvaerner CB&H process).

## Review approach: exemplary studies

This topic is not reviewed comprehensively. The aim is a set of **5-10 exemplary plasma studies** that together show the state of the art in performance against the benchmarks, plus the benchmarks themselves. Choose exemplars so that, between them, they:

- show the best demonstrated performance on the primary metrics at matched operating points (CH4 conversion with EC_CH4 or EC_H2, and product selectivity);
- span the main plasma types (thermal arc/torch, microwave, gliding arc, non-thermal) and the largest demonstrated scales;
- report enough (point-matched power, feed, products, power boundary) for the metrics below to be calculated and traced.

Recent critical reviews are used to locate candidates and the field's conventions. Each exemplar is extracted in full with the shared workflow; screening records explain why a candidate was or was not chosen.

## Scope

Routes (all endothermic, non-oxidative):

- Methane pyrolysis/decomposition: CH4 -> C(s) + 2H2, +74.8 kJ/mol CH4 (298 K).
- Non-oxidative coupling to acetylene: 2CH4 -> C2H2 + 3H2, +376 kJ/mol C2H2 (+188 kJ/mol CH4).
- Non-oxidative coupling to ethylene/ethane where reported alongside the above (2CH4 -> C2H4 + 2H2, +202 kJ/mol C2H4).

Natural gas feeds and H2 or Ar dilution are eligible; record the diluent and whether H2 is recycled. Activation: plasma (all discharge types) and Joule/resistive heating, including electrically heated packed, moving-bed and molten-media reactors when the heat is electrical and reported. Catalytic and non-catalytic systems.

**Benchmarks:**

- **Joule-heated pyrolysis** (primary electrified comparator), e.g. BASF's electrically heated moving-carbon-bed pilot, if experimental data are published.
- **Fired SMR** for hydrogen: reuse SRC003 (NETL 2022) and SRC004 (IEAGHG 2017) from the reforming folder; no new fired references are searched.
- **Industrial plasma plants** (Monolith, Hüls): plant or design data, labelled by data type (measured plant data, design basis, vendor claim).

## Questions the review should answer

1. What reactor and plasma arrangements have been demonstrated, and at what scale (lab, pilot, industrial)?
2. What feed, dilution, temperature, pressure and electrical input were used?
3. What CH4 conversion, product selectivity (H2, C2H2, C2H4, solid carbon) and energy performance were achieved?
4. What happened to the carbon (form, quality, recovery, deposition, fouling), and how long did systems run?
5. How do these results compare with Joule-heated pyrolysis, industrial plasma plants and SMR hydrogen, and what missing information limits that comparison?

## Energy performance indicators

Use workflow.md section 4, with these route-specific definitions:

```text
EC_CH4   = P / F_CH4,conv                 (kJ/mol CH4 converted; primary)
EC_H2    = P / F_H2,net                   (kJ/mol H2); also kWh/kg H2
EC_prod  = P / F_C2H2                      (kJ/mol C2H2) for coupling papers; also kWh/kg C2H2
eta_P,LHV = sum(F_i,out * LHV_i) / (P + F_CH4,conv * LHV_CH4),  i = H2, C2H2, C2H4, C2H6
eta_dH   = F_CH4,conv * dH_R / P           (reaction-enthalpy efficiency, dH_R from product split)
```

Report solid carbon separately: as mass rate and fraction of converted carbon, and as energy only when its HHV basis is stated (carbon black ~32.8 MJ/kg). Never fold carbon into eta_P,LHV silently; state when it is included.

Reference lines: 74.8 kJ/mol CH4 (to C + H2) and 188 kJ/mol CH4 (to C2H2 + H2). Hydrogen from SMR, for comparison: fired SMR reformer heat per mol H2 from SRC003/SRC004.

## Synthesis plan

As in the reforming review (evidence table, conversion vs EC_CH4 plot, scale plot, whole-system table, reporting-quality summary, narrative), grouped by product route (carbon + H2; acetylene; ethylene) and then by activation (Joule, thermal arc/torch, microwave, gliding arc, DBD, other plasma). Industrial plants are shown as reference markers with their data type. Do not rank across product routes.

## Scale-up and whole-system assessment

Same approach as [../literature_reforming/literature_review_objectives.md](../literature_reforming/literature_review_objectives.md): wall-basis EC with representative supplies, then heat integration (quenching and heat recovery from hot H2/carbon), then cost and durability, including carbon product value, which can dominate pyrolysis economics. Demonstrated values and estimates stay separate.

## Version history

- 0.1 (2026-11-09): initial objectives.
- 0.1 amendment (2026-11-09): selective review of 5-10 exemplary studies against the benchmarks, not a comprehensive review.
