# Power-supply constraints in plasma-driven methane reforming and CO2 splitting: evidence base

Brendan Bulfin, University College Cork.

Evidence base for an analysis of plasma reactors for two strongly endothermic gas-phase conversions, methane reforming and CO2 splitting, and of the power supplies needed to run them, compared with fired, Joule-heated and electrochemical benchmarks (B. Bulfin, manuscript in preparation). Every number used in the review can be traced from the manuscript figures to the synthesis tables, to an evidence record, and to a page of the source document.

| Topic | Reaction (298 K) | Benchmarks | Folder | Sources |
|---|---|---|---|---|
| Methane reforming | SMR +206, DRM +247 kJ/mol CH4 | Joule-heated eSMR pilot; fired SMR design studies | [literature_reforming/](literature_reforming/) | 11 plasma studies, 5 benchmark sources |
| CO2 splitting | CO2 -> CO + 1/2 O2, +283 kJ/mol | Solid oxide electrolysis (SOEC) | [literature_co2_splitting/](literature_co2_splitting/) | 10 plasma studies, 2 SOEC sources |
| Power supplies | - | Industrial supplies by technology class | [power_systems/](power_systems/) | 51 supply sources, 208 values |

## The angle of this analysis

Plasma studies usually report energy at the discharge, measured with laboratory supplies and with no heat recovery. This analysis first puts the demonstrated results on a common basis (conversion against electricity per mole of methane converted, or per Nm3 of CO), then asks a scale-up question:

> If each reactor type were built with representative, industrially available power supplies, what would its electricity demand at the wall be, compared with Joule-heated, fired and electrochemical routes?

Each supply technology (DC rectifier, kHz inverter, RF generator, 915 MHz or 2.45 GHz microwave source, pulsed supply) comes in a limited range of unit powers, with a characteristic wall-plug efficiency, cost and lifetime. Applying these to the reactor results shows how much electricity is lost before it reaches the plasma, and which combinations of plasma type, frequency and scale are realistic. Heat integration (steam raising, product heat, quenching) and product separation are the other terms that separate a laboratory result from a process; they are discussed but mostly not reported in the sources.

## Repository structure

```text
README.md                          this file
human_checks/
  summary.csv                      one row per human check (source, scope, records checked, findings)
  findings.csv                     one row per error found in a human check (one so far, HC001)
literature_reforming/              methane reforming
  literature_review_objectives.md  aims, scope, metrics
  literature_search_strategy.md    search terms, eligibility, screening
  workflow.md, _source_template.md extraction protocol and template
  logs/                            processing log (tools, models, human checks), search and selection log,
                                   independent cross-check log, shortlists
  0_synthesis/                     reforming_synthesis.csv, tables, build and plot scripts; figures/ holds the figures
  <FirstAuthor_Journal_Year_Topic>/
    short_summary.txt              headline results and standard comparison tables
    outputs/extraction.md          full extraction, reporting quality, gaps, calculations
    outputs/evidence.csv           every value used, with document, page, locator and quote
    outputs/calculations.py        reviewer calculations (reproduces the values in extraction.md)
literature_co2_splitting/          CO2 splitting, same layout (co2_synthesis.csv in 0_synthesis/)
power_systems/                     industrial power-supply data (mainly manufacturer and patent sources)
  README.md, workflow.md           folder guide and extraction rules
  results/                         source_register.csv, supply_values.csv, supply_classes.csv,
                                   discharge_supply_map.csv and the scripts; figures/ holds the figures
  logs/                            processing and cross-check logs
  notes/                           scale-up assessment, supply maturity, reactor matching, related literature, to-do lists
literature_reviews/
  reviews_shortlist.md             review papers used to locate studies and conventions (not extracted)
```

Source documents (PDFs) and local copies of web sources are not distributed. Each `extraction.md` and `power_systems/results/source_register.csv` records SHA-256 hashes so that readers can confirm they hold the same versions.

## Reproduce the synthesis and figures

From the repository root, with Python 3 and matplotlib:

```text
python3 literature_reforming/0_synthesis/build_synthesis.py
python3 literature_reforming/0_synthesis/plot_manuscript_figure.py
python3 literature_co2_splitting/0_synthesis/build_synthesis.py
python3 literature_co2_splitting/0_synthesis/plot_manuscript_figure.py
cd power_systems/results && python3 scaleup_wall_basis.py && python3 plot_supply_values.py && python3 plot_manuscript_figure.py
```

The synthesis builds read the supply-class efficiencies from `power_systems/results/supply_classes.csv`. Each source's reviewer calculations are reproduced by its `outputs/calculations.py`.

## Method and provenance

- **Extraction.** Each source is extracted under its topic's `workflow.md`: every value carries an evidence ID (e.g. SRC028-E012) with document, page and locator; reviewer calculations (e.g. SRC028-C002) are kept separate from reported values and are reproduced by script. Power is always given with its boundary (wall, supply output, absorbed or plasma power).
- **AI assistance.** Extractions were prepared by an AI (Claude Code with Claude Opus; two early sources with Codex) and checked by the same AI against the source (status `ai_checked`). Tool and model versions per source are in each topic's `logs/processing_log.md`.
- **Independent cross-check.** Every source was extracted a second time, blind, by a different AI (GPT), and each difference was checked against the source; differences and actions are in each topic's `logs/cross_check_log.md`.
- **Human checks.** BB checked the headline operating points of most sources against the source documents (`human_checks/summary.csv`); no errors were found. These are partial checks of the points used in the manuscript, not of the full papers. Each extraction states which records were checked; "Human check: none" means none was made. For the power supplies, BB checked the values behind every adopted efficiency range and the largest units and highest efficiencies in the manuscript power-supply figure (47 values, status `human_verified` in `power_systems/results/supply_values.csv`); one boundary description was corrected (`human_checks/findings.csv`, HC001), and no value changed.
- **Literature search and selection.** Selective, not comprehensive: candidates were located through recent reviews and targeted web searches (not Scopus or Web of Science), with a final check for recent publications; 52 searches and about 60 candidate studies are recorded. Plasma studies were selected for (i) kW-scale or integrated operation, (ii) power reported at a stated boundary with conversion at the same operating condition, so that electricity per unit product can be calculated, and (iii) coverage of each reaction route and the main discharge types, including the best reported lower-power result for a discharge type. The selection represents the best-documented results at scale, not the whole field. Each search, candidate and inclusion or exclusion reason is in the topic's `logs/search_and_selection_log.md`; the criteria are in `literature_search_strategy.md`.

## Sources

| ID | Source | Topic / route | Activation | Role | Human check |
|---|---|---|---|---|---|
| SRC001 | Wismann et al. 2019, Science | SMR | Joule heating (lab) | context (not plotted) | none |
| SRC002 | Geng et al. 2022, Appl. Catal. A | SMR | DBD + Ni catalyst | plasma | partial (feed) |
| SRC003 | Lewis et al. 2022, NETL report | SMR | fired | benchmark (design) | headline |
| SRC004 | Collodi et al. 2017, IEAGHG report | SMR | fired | benchmark (design) | none |
| SRC005 | From et al. 2024, Chem. Eng. J. | mixed (biogas) | Joule heating (pilot) | benchmark | none |
| SRC006 | From et al. 2025, Chem. Eng. J. | mixed (biogas) | Joule heating (pilot) | benchmark (durability) | none |
| SRC007 | Hrabovsky et al. 2018, Plasma Chem. Plasma Process. | SMR, mixed | DC arc torch, ~120 kW | plasma | headline |
| SRC008 | Akande and Lee 2022, Int. J. Hydrogen Energy | SMR | microwave torch, 915 MHz, 15-50 kW | plasma | headline |
| SRC009 | Song et al. 2020, Curr. Appl. Phys. | DRM | RF ICP torch, 22-27 kW | plasma | headline |
| SRC010 | Hrycak et al. 2023, Sci. Rep. | SMR, mixed | microwave, 915 MHz, 6.5 kW | plasma | headline |
| SRC011 | Kelly et al. 2023, J. CO2 Util. | DRM | microwave, 2.45 GHz, 1 kW | plasma | headline |
| SRC012 | Zhu et al. 2019, Catal. Today | SMR | gliding arc + Ni catalyst, 0.25 kW | plasma | headline |
| SRC013 | Andersen et al. 2020, Chem. Eng. J. | DRM | packed-bed DBD, 45 W | plasma | none |
| SRC014 | Kwon et al. 2023, J. CO2 Util. | DRM | rotating gliding arc, 1.7 kW | plasma | none |
| SRC015 | Wanten et al. 2022, J. CO2 Util. | DRM | confined DC glow, 0.15 kW | plasma | headline |
| SRC027 | Kaufmann et al. 2026, J. CO2 Util. | DRM | rotating DC glow-to-arc, 0.5-1.4 kW | plasma | headline |
| SRC016 | Kiefer et al. 2024, Chem. Eng. J. | CO2 splitting | microwave, 2.45 GHz, 2.7 kW (wall metered) | plasma | headline |
| SRC017 | Hecimovic et al. 2023, J. CO2 Util. | CO2 splitting | microwave, 2.45 GHz (same torch as SRC016) | plasma | none |
| SRC018 | Bongers et al. 2017, Plasma Process. Polym. | CO2 splitting | microwave, 915 MHz, 3-10 kW | plasma | headline |
| SRC019 | Girard-Sahun et al. 2022, Chem. Eng. J. | CO2 splitting | AC gliding arc + carbon bed | plasma | headline |
| SRC020 | O'Modhrain et al. 2024, ACS Eng. Au | CO2 splitting | five DC gliding arcs, 7.1 kW | plasma | headline |
| SRC021 | Bryssinck et al. 2025, React. Chem. Eng. | CO2 splitting | seven DC gliding arcs + carbon bed, 8 kW | plasma | headline |
| SRC022 | Renninger et al. 2022, J. CO2 Util. | CO2 splitting | DC glow-to-arc, 0.16 kW | plasma | headline |
| SRC023 | Yong et al. 2023, Plasma Sources Sci. Technol. | CO2 splitting | nanosecond pulsed (batch) | plasma | none |
| SRC024 | Van Laer and Bogaerts 2015, Energy Technol. | CO2 splitting | packed-bed DBD | plasma | none |
| SRC028 | Kim et al. 2014, Plasma Chem. Plasma Process. | CO2 splitting | three-phase AC gliding arc, 0.6 kW | plasma | partial |
| SRC025 | Küngas 2020, J. Electrochem. Soc. | CO2 splitting | SOEC stack | benchmark | none |
| SRC026 | Hecimovic et al. 2024, J. CO2 Util. | CO2 splitting | SOEC system (design) vs microwave plasma | benchmark | headline |

"Headline" means the operating points used in the manuscript were checked against the source; "partial" means selected records only. Details are in `human_checks/summary.csv` and in each extraction. For the power-supply values (`power_systems/`), the headline values (adopted efficiency ranges and figure extremes) have a human check; the remaining values are AI-checked.

## Licence

The code (Python scripts) is released under the MIT licence (`LICENSE`); the data and text (evidence records, synthesis tables, logs, notes and figures) under CC BY 4.0 (`LICENSE-DATA.md`). Source documents are not included and remain under their own copyright.

## How to cite

Please cite the archived release of this repository (DOI to be added on release; see `CITATION.cff`) and the accompanying article (in preparation).
