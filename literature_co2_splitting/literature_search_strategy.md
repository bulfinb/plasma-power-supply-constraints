# Literature search and selection strategy: CO2 splitting

Version 0.1 - 2026-11-09.

Objectives: [literature_review_objectives.md](literature_review_objectives.md). Extraction: [../literature_reforming/workflow.md](../literature_reforming/workflow.md). Search and selection procedure, record formats and exclusion logic follow [../literature_reforming/literature_search_strategy.md](../literature_reforming/literature_search_strategy.md) except where stated here.

## Selection approach

Selective, not comprehensive: the target is 5-10 exemplary plasma studies plus the benchmarks (see the objectives, "Review approach"). Searches are targeted: recent reviews and their comparison figures, searches for leading results by plasma type and scale, and backward/forward citation from strong candidates. Database Boolean searches (below) are optional and used to check that no leading result has been missed, not to screen the whole field. Record each search and why each candidate was chosen or not; a short candidate list with reasons replaces full-text screening of every hit.

## What to include

- An original experiment with measured CO2 conversion or CO production and enough information to identify the reactor, feed and power.
- Route: CO2 -> CO + 1/2 O2, pure or with inert diluent.
- Activation by plasma (any discharge type), with or without catalysts, membranes or post-plasma quenching.

The field is large (hundreds of papers, mostly sub-kW). When choosing exemplars, prioritise, in order: (1) kW-scale or higher, or pilot systems; (2) papers reporting both conversion and energy efficiency with a stated power measurement; (3) papers with the best matched conversion and efficiency for each plasma type, including high-conversion results even at higher energy cost, since conversion is co-primary; (4) recent critical reviews, used to locate primary papers and the field's measurement conventions. Record the prioritisation rule in the search log when a search is truncated.

## What to exclude

| Reason | Application |
|---|---|
| Modelling only | Simulations or designs without a qualifying experiment. |
| Co-reactant feeds | CO2 with CH4 (DRM: literature_reforming), H2 (hydrogenation/RWGS), H2O (co-splitting); record H2O co-splitting as pending for discussion. |
| Non-plasma routes | Electrochemical and thermocatalytic routes (except the selected SOEC and H2 + RWGS benchmarks, chosen directly), photochemical, solar thermochemical, catalytic thermal. |
| Low pressure only | Sub-atmospheric results are eligible but flagged, since the vacuum-pumping energy is normally excluded; record pressure explicitly. |
| No original demonstration | Reviews and perspectives (use to find primary papers). |
| Duplicate evidence | As in the reforming strategy. |

## Search terms

```text
("CO2 splitting" OR "CO2 dissociation" OR "CO2 decomposition" OR "carbon dioxide splitting" OR "carbon dioxide dissociation" OR "CO2 conversion") AND
(plasma OR plasmatron OR "gliding arc" OR "microwave discharge" OR "microwave plasma" OR "dielectric barrier discharge" OR "glow discharge" OR "nanosecond pulsed" OR "spark discharge" OR "arc discharge" OR "RF discharge")
```

Supplementary: "energy efficiency" AND "CO2" AND plasma AND (kW OR "high power" OR pilot); and the targeted benchmark searches: SOEC CO2 electrolysis CO production electricity consumption and conversion (Topsoe eCOs); electrolytic H2 + RWGS CO production design study; D-CRBN plasma CO2 reactor.

## Records

Search and selection logs are in [search_and_selection_log.md](search_and_selection_log.md), with IDs prefixed CS (searches) and CR (records). Included sources take the next free global source ID (shared across all topic folders).

## Version history

- 0.1 (2026-11-09): initial strategy.
- 0.1 amendment (2026-11-09): selective approach, 5-10 exemplary studies.
