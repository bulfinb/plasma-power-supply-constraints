# Literature search and selection strategy: methane pyrolysis and coupling

Version 0.1 - 2026-11-09.

Objectives: [literature_review_objectives.md](literature_review_objectives.md). Extraction: [../literature_reforming/workflow.md](../literature_reforming/workflow.md). Search and selection procedure, record formats and exclusion logic follow [../literature_reforming/literature_search_strategy.md](../literature_reforming/literature_search_strategy.md) except where stated here.

## Selection approach

Selective, not comprehensive: the target is 5-10 exemplary plasma studies plus the benchmarks (see the objectives, "Review approach"). Searches are targeted: recent reviews and their comparison figures, searches for leading results by plasma type and scale, and backward/forward citation from strong candidates. Database Boolean searches (below) are optional and used to check that no leading result has been missed, not to screen the whole field. Record each search and why each candidate was chosen or not; a short candidate list with reasons replaces full-text screening of every hit.

## What to include

- An original experiment (or industrial plant data) with measured CH4 conversion or product formation.
- Route: non-oxidative methane pyrolysis to carbon and H2, or non-oxidative coupling to C2 hydrocarbons (mainly acetylene).
- Activation by plasma (any discharge type) or Joule/resistive heating, including electrically heated molten-media and moving-bed reactors.
- Enough information to identify the reactor, feed and at least one performance result.

Experiments combined with modelling are eligible for their experimental results. Industrial plant data (Monolith, Hüls, Kvaerner) are included as reference systems with their data type stated.

## What to exclude

| Reason | Application |
|---|---|
| Modelling only | Simulations or designs without a qualifying experiment or plant data. |
| Oxidative routes | Oxidative coupling of methane, partial oxidation, any intentional O2 or CO2 co-feed (CO2 co-feed is DRM: see literature_reforming). |
| Non-electric heating | Fuel-fired or solar pyrolysis, unless an electrically heated case is reported separately. |
| Other electrification | Induction and microwave dielectric heating without a discharge (record for a later category). |
| Different feed | Higher hydrocarbons, biomass or plastics without a separate methane/natural gas experiment. |
| No original demonstration | Reviews, perspectives, patents (patents may be used for industrial design data, labelled as such). |
| Duplicate evidence | As in the reforming strategy. |

## Search terms

Run plasma and Joule-heating searches separately; save exact expressions.

**Plasma**

```text
(methane OR "natural gas") AND
(pyrolysis OR decomposition OR cracking OR "non-oxidative coupling" OR acetylene OR "carbon black" OR "turquoise hydrogen") AND
(plasma OR plasmatron OR "arc discharge" OR "gliding arc" OR "microwave discharge" OR "dielectric barrier discharge" OR "glow discharge" OR "spark discharge" OR "RF discharge" OR "pulsed discharge" OR "thermal plasma")
```

**Joule/resistive heating**

```text
(methane OR "natural gas") AND (pyrolysis OR decomposition OR cracking) AND
("Joule heating" OR "resistive heating" OR "resistance heating" OR "electrically heated" OR "electric heating" OR "molten metal" OR "molten salt")
```

Screen molten-media hits for whether the heating is electrical and reported.

**Industrial reference searches** (targeted, not Boolean): Monolith Olive Creek energy use / electricity per tonne carbon black; Hüls arc acetylene process energy consumption (kWh/kg C2H2); Kvaerner carbon black and hydrogen process; BASF methane pyrolysis pilot Ludwigshafen.

## Records

Search and selection logs are in [search_and_selection_log.md](search_and_selection_log.md), with IDs prefixed PS (searches) and PR (records) to keep them distinct from the reforming logs. Included sources take the next free global source ID (shared across all topic folders; SRC016-SRC025 taken by CO2 splitting, next free SRC026).

## Version history

- 0.1 (2026-11-09): initial strategy.
- 0.1 amendment (2026-11-09): selective approach, 5-10 exemplary studies.
