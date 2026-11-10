# Electrified endothermic processes: plasma and Joule heating at scale

Brendan Bulfin, University College Cork.

Literature review and evidence base on electrically driven endothermic chemical processes. Started October 2026 with methane reforming; extended in November 2026 to two further processes that are heavily investigated in plasma systems.

| Topic | Reaction (298 K) | Electrified comparator | Folder | Status |
|---|---|---|---|---|
| Methane reforming | SMR +206, DRM +247 kJ/mol CH4 | Joule-heated eSMR; fired SMR reference | `literature_reforming/` | 15 sources extracted |
| Methane pyrolysis and coupling | CH4 -> C + 2H2 +75 kJ/mol; 2CH4 -> C2H2 + 3H2 +376 kJ/mol | Joule-heated pyrolysis; industrial plasma plants (Monolith, Hüls); SMR hydrogen | `literature_pyrolysis/` | set up (selective: 5-10 exemplary studies); search not started |
| CO2 splitting | CO2 -> CO + 1/2 O2 +283 kJ/mol | SOEC electrolysis; electrolytic H2 + RWGS | `literature_co2_splitting/` | set up (selective: 5-10 exemplary studies); search not started |

The sections below describe the reforming topic, where the method was developed; the other topics follow the same workflow and scale-up angle.

## Context

Steam methane reforming (SMR) is strongly endothermic (+206 kJ/mol CH4) and is conventionally driven by burning natural gas in a fired furnace. Electrifying the heat input could remove those combustion emissions and allow renewable electricity to drive the reaction. Two electrified routes are compared:

- **Joule heating (eSMR):** electricity heats the catalyst structure directly, so a conventional catalytic reaction is fed electrically rather than by combustion (e.g. Topsoe eREACT).
- **Plasma reforming:** electricity sustains a discharge (thermal arc, RF or microwave torch, gliding arc, dielectric barrier discharge) that activates the reactants, with or without a catalyst.

Fired SMR is the industrial reference that both must match or improve on.

## Novelty

This study uses the scale and efficiency of commercially available power supplies to guide, and narrow, the design space of process-electrification pathways via plasma chemistry.

Plasma studies usually optimise the discharge and treat the power supply as laboratory equipment. At industrial scale the supply is a design constraint in its own right. Each supply technology (DC rectifier, kHz inverter, RF generator, 915 MHz or 2.45 GHz microwave source, pulsed supply) comes in a limited range of unit powers, with a characteristic wall-plug efficiency, cost and lifetime. Together these fix how many modules a plant would need and how much electricity is lost before it reaches the plasma. Applying them to the demonstrated reactor performance shows which combinations of plasma type, frequency, pressure and scale are realistic for industrial endothermic processes, and which are ruled out before the plasma chemistry is considered. Supporting material: [power_systems/](power_systems/) (supply efficiencies, scales and costs) and [literature_plasma_powersupply/](literature_plasma_powersupply/) (measured wall-plug vs plasma efficiency and supply matching).

## The angle of this review

Most plasma reforming papers report energy at the discharge: the power absorbed by the plasma, measured with laboratory supplies, with no heat recovery. This review first benchmarks the demonstrated performance on that common basis, then asks a whole-system question:

> If each reactor type were scaled up with representative, industrially available power supplies, what would its wall-to-product energy balance and cost look like, compared with Joule-heated and fired SMR?

Two factors decide this beyond the plasma itself:

1. **Power supply losses.** Industrial supplies range from ~98% (rectifiers for Joule heating or DC arcs) through ~80-86% (magnetron microwave) to ~60% (RF tube oscillators). In the present plasma results these losses are a small correction, because the plasma process itself dominates. In an optimised electrified plant, however, a 20% loss in the supply is significant: it means 25% more electricity per unit of power delivered, and it appears mostly as low-grade heat in cooling water, which cannot usefully drive a reaction at 700-900 degC. Competing against eSMR, with near-lossless power delivery, a plasma route must recover that margin elsewhere.
2. **Heat integration.** Hot products leave lab plasma reactors unrecovered, whereas fired and Joule-heated SMR recover heat into steam and feed preheat. A fair comparison needs heat recovery applied to the plasma cases too.

Cost (supply capital cost per kW, tube and electrode lifetimes) is the third consideration; published data are sparse.

## Repository structure

```text
README.md                         this file
literature_plasma_powersupply/
  README.md                        academic papers only: supply matching, wall-plug vs plasma efficiency, TEA of supply capex (PS001-)
literature_reviews/
  reviews_shortlist.md             review papers used to pick exemplary studies and benchmarks (pyrolysis, CO2 splitting)
  <FirstAuthor_Journal_Year_Topic>/manuscript.pdf
literature_pyrolysis/, literature_co2_splitting/
  literature_review_objectives.md, literature_search_strategy.md, search_and_selection_log.md, processing_log.md
literature_reforming/
  literature_review_objectives.md  aims, scope, comparison basis and synthesis plan
  literature_search_strategy.md    search terms, eligibility, screening
  workflow.md                      extraction protocol (evidence IDs, metrics, reporting quality); shared by all topics
  _source_template.md              template for each extraction
  search_and_selection_log.md      searches run and screening decisions
  plasma_shortlist_2026-11-05.md   current plasma shortlist and reserves
  processing_log.md                AI tool/model versions and human checks for every source
  <FirstAuthor_Journal_Year_Topic>/
    short_summary.txt              headline results and five comparison tables
    outputs/extraction.md          full extraction, reporting quality, missing data
    outputs/evidence.csv           every value used, with page and locator
    outputs/calculations.py        reviewer calculations (where used)
power_systems/                     all manufacturer and other non-academic supply data
  supply_maturity_niche.md         are plasma supplies a "niche product"? maturity, physical limits, capex (D1-D12)
  source_register.csv              every non-academic source: version, access date, SHA-256, Wayback snapshot
  source_archive/                  local copies (not distributed)
  BB_search.txt                    sources that need manual retrieval
  scaleup_supplies.csv             representative industrial supplies by plasma/Joule class
  scaleup_sources.md               efficiency chain, sources (T01-T23), indicative wall-basis results
  scaleup_wall_basis.py            applies supply efficiencies to the reviewed EC_CH4 values
  power_sources.csv, sources.md, power_systems_report.*   earlier survey of MW-scale induction/RF/microwave supplies (S1-S17)
```

Source manuscripts and supplements are not distributed. Each `extraction.md` records SHA-256 hashes of the documents used so readers can confirm they hold the same versions.

## Sources reviewed so far

| ID | Source | Route | Activation | Role |
|---|---|---|---|---|
| SRC001 | Wismann et al. 2019, Science | SMR | Joule heating | lab benchmark |
| SRC002 | Geng et al. 2022, Appl. Catal. A | SMR | DBD + catalyst | plasma |
| SRC003 | Lewis et al. 2022, NETL report DOE/NETL-2022/3241 | SMR | fired | industrial reference |
| SRC004 | IEAGHG 2017 (Collodi et al.), Report 2017-02 | SMR | fired | industrial reference |
| SRC005 | From et al. 2024, Chem. Eng. J. | mixed (biogas) | Joule heating (eSMR pilot) | primary benchmark |
| SRC006 | From et al. 2025, Chem. Eng. J. | mixed (biogas) | Joule heating (eSMR pilot) | benchmark |
| SRC007 | Hrabovsky et al. 2018, Plasma Chem. Plasma Process. | SMR, DRM | DC thermal arc, ~120 kW | plasma |
| SRC008 | Akande et al. 2022, Int. J. Hydrogen Energy | SMR | microwave torch, 17-47 kW | plasma |
| SRC009 | Song et al. 2020, Curr. Appl. Phys. | DRM | RF induction torch, 21-27 kW | plasma |
| SRC010 | Hrycak et al. 2023, Sci. Rep. | mixed | microwave, 915 MHz, 4.5-6.5 kW | plasma |
| SRC011 | Kelly et al. 2023, J. CO2 Util. | DRM | microwave, 2.45 GHz, 1 kW | plasma |
| SRC012 | Zhu et al. 2019, Catal. Today | SMR | gliding arc + Ni catalyst, 0.25 kW | plasma |
| SRC013 | Andersen et al. 2020, Chem. Eng. J. | DRM | packed-bed DBD, 45 W | plasma |
| SRC014 | Kwon et al. 2023, J. CO2 Util. | DRM | rotating gliding arc, ~1.7 kW | plasma |
| SRC015 | Wanten et al. 2022, J. CO2 Util. | DRM | confined DC glow discharge, ~0.1 kW | plasma |

Review status of each source (AI-checked or human-verified) is in its `extraction.md` and in `literature_reforming/processing_log.md`.

## Method and provenance

- Extractions follow `literature_reforming/workflow.md`: every value carries an evidence ID, document page and locator; reviewer calculations are separate from reported values and reproducible from `calculations.py`.
- The primary energy metric is EC_CH4, the electrical energy per mole of methane converted, always with its power boundary stated (discharge, absorbed, arc, generator or wall).
- Extractions were prepared with AI assistance (Claude Code with Claude Opus 5.5; an initial pass on two sources with Codex). Tool and model versions for every source are recorded in `literature_reforming/processing_log.md`. AI checks are not treated as verification; human-verified sources are marked as such.
- The literature search so far used a general web search tool, not Scopus or Web of Science; database searches are still to be run (see `literature_reforming/search_and_selection_log.md`).

## Status (2026-11-09)

- Reforming: 15 sources extracted, all ai_checked; systematic human verification to follow.
- Representative industrial supply table drafted (`power_systems/scaleup_*`), AI-checked from source summaries; full texts to be confirmed.
- Next: human verification of remaining sources; synthesis evidence table and conversion vs EC_CH4 plot; heat-recovery treatment for plasma cases; supply capital-cost data; database searches.
- Pyrolysis and CO2 splitting: objectives, search strategies and empty logs set up 2026-11-09; searches not yet run.
