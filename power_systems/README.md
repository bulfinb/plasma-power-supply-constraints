# power_systems

Industrial power-supply data for the scale-up assessment: efficiency, unit power, frequency, cost, lifetime and voltage of the supplies a scaled-up plasma or Joule-heated reactor would use. Sources are mainly manufacturer documents, patents, tenders and trade press; peer-reviewed papers assessed as a whole are in [../literature_plasma_powersupply/](../literature_plasma_powersupply/README.md). Restructured 2026-11-10; method in [workflow.md](workflow.md).

## Structure

Top level: README and workflow. `results/` holds the data tables, the scripts and (in `figures/`) the figures; `logs/` the processing, cross-check and human-check records; `notes/` the written analysis and to-do lists.

| Path | Content |
|---|---|
| [workflow.md](workflow.md) | How sources are registered, values extracted and checked |
| [logs/](logs/) | [processing_log.md](logs/processing_log.md) (AI tool and model versions, human checks), [cross_check_log.md](logs/cross_check_log.md) (independent GPT re-extraction), [human_check_checklist.md](logs/human_check_checklist.md) and [human_check_worksheet.csv](logs/human_check_worksheet.csv) (steps and worksheet for the human check of each value) |
| [results/source_register.csv](results/source_register.csv) | One row per source (PW001...): earlier IDs (aliases), quality tier, document date, URL, local copy, SHA-256, Wayback snapshot, status |
| [results/supply_values.csv](results/supply_values.csv) | One row per value used: location, verbatim quote, item, class, frequency, quantity, qualifier, basis, cost scope, data type, status |
| [results/supply_classes.csv](results/supply_classes.csv) | Representative supply classes (J1, A1, D1, K1, K2, R1, R2, M1-M3, P1, H1) with ranges and the value IDs behind them |
| [results/discharge_supply_map.csv](results/discharge_supply_map.csv) | Discharge type in the review (DC arc, gliding arc, glow, DBD, microwave, RF ICP, pulsed, Joule) to supply class, with lab supply, electrical requirement and scale-up constraint |
| [notes/scaleup_assessment.md](notes/scaleup_assessment.md) | Efficiency chain, class table, indicative wall-basis EC_CH4 for the reforming sources |
| [notes/supply_maturity_niche.md](notes/supply_maturity_niche.md) | Are plasma supplies a "niche product"? Maturity, physical limits, capital cost |
| [notes/reactor_matching.md](notes/reactor_matching.md) | Voltage, impedance and matching between supply and reactor (illustrative calculations) |
| [results/](results/) (scripts) | `plot_supply_values.py` (cost per kW; power and efficiency vs frequency; cost vs unit size; class map), `plot_manuscript_figure.py`, `plot_icp_frequency_scale.py` (ICP torch frequency against diameter and power), `scaleup_wall_basis.py` (writes `scaleup_wall_basis.csv`, the wall-basis EC_CH4 table), `make_check_worksheet.py` (writes `logs/human_check_worksheet.csv`), `requirements.txt` |
| [results/figures/](results/figures/) | Figures produced by the scripts |
| [notes/BB_search.txt](notes/BB_search.txt) | Sources that need manual retrieval |
| [notes/suggested_quote_requests.txt](notes/suggested_quote_requests.txt) | Vendor budgetary quotes to request |
| `source_archive/` | Local copies, one folder per PW ID (gitignored; not redistributed) |
| [legacy/](legacy/) | Superseded work kept unchanged: the 2026-09 frequency survey (report, CSVs, figures) and the 2026-11-05 class table. Not cited; their sources are re-registered as PW IDs |

## Status (2026-11-10)

- 50 sources registered (PW049 dropped). 141 values extracted from archived copies, each with location and quote: 139 ai_checked, 2 unverified because no local copy is held yet (see notes/BB_search.txt).
- Human verification not yet started (use [../human_checks/](../human_checks/)).
- Re-extraction corrected several values cited before 2026-11-10; the changes are listed in [notes/scaleup_assessment.md](notes/scaleup_assessment.md).
- Supply cost per kW is still sparse, especially for kHz inverters and RF generators.

## Reproduce

From `power_systems/results/`: `python3 scaleup_wall_basis.py`, `python3 plot_supply_values.py`, `python3 plot_manuscript_figure.py` and `python3 plot_icp_frequency_scale.py` (needs matplotlib; see `requirements.txt`). Figures are written to `results/figures/`.
