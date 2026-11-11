# power_systems

Industrial power-supply data for the scale-up assessment: efficiency, unit power, frequency, cost, lifetime and voltage of the supplies a scaled-up plasma or Joule-heated reactor would use. Sources are mainly manufacturer documents, patents, tenders and trade press; peer-reviewed papers assessed as a whole are in [../literature_plasma_powersupply/](../literature_plasma_powersupply/README.md). Restructured 2026-11-10; method in [workflow.md](workflow.md).

## Structure

| Path | Content |
|---|---|
| [workflow.md](workflow.md) | How sources are registered, values extracted and checked |
| [processing_log.md](processing_log.md) | AI tool and model versions, human checks |
| [source_register.csv](source_register.csv) | One row per source (PW001...): earlier IDs (aliases), quality tier, document date, URL, local copy, SHA-256, Wayback snapshot, status |
| [supply_values.csv](supply_values.csv) | One row per value used: location, verbatim quote, item, class, frequency, quantity, qualifier, basis, cost scope, data type, status |
| [supply_classes.csv](supply_classes.csv) | Representative supply classes (J1, A1, D1, K1, K2, R1, R2, M1-M3, P1, H1) with ranges and the value IDs behind them |
| [discharge_supply_map.csv](discharge_supply_map.csv) | Discharge type in the review (DC arc, gliding arc, glow, DBD, microwave, RF ICP, pulsed, Joule) to supply class, with lab supply, electrical requirement and scale-up constraint |
| [notes/scaleup_assessment.md](notes/scaleup_assessment.md) | Efficiency chain, class table, indicative wall-basis EC_CH4 for the reforming sources |
| [notes/supply_maturity_niche.md](notes/supply_maturity_niche.md) | Are plasma supplies a "niche product"? Maturity, physical limits, capital cost |
| [notes/reactor_matching.md](notes/reactor_matching.md) | Voltage, impedance and matching between supply and reactor (illustrative calculations) |
| [figures/](figures/) | Figures and the scripts that make them: `plot_supply_values.py` (cost per kW; power and efficiency vs frequency; cost vs unit size; class map), `scaleup_wall_basis.py` (wall-basis EC_CH4 table) |
| [scripts/](scripts/) | `make_check_worksheet.py` (human-check worksheet), `requirements.txt` |
| [human_check_checklist.md](human_check_checklist.md), [human_check_worksheet.csv](human_check_worksheet.csv) | Steps for the human check of each value; worksheet (one row per value, by priority), made by `scripts/make_check_worksheet.py` |
| [BB_search.txt](BB_search.txt) | Sources that need manual retrieval |
| [suggested_quote_requests.txt](suggested_quote_requests.txt) | Vendor budgetary quotes to request |
| `source_archive/` | Local copies, one folder per PW ID (gitignored; not redistributed) |
| [legacy/](legacy/) | Superseded work kept unchanged: the 2026-09 frequency survey (report, CSVs, figures) and the 2026-11-05 class table. Not cited; their sources are re-registered as PW IDs |

## Status (2026-11-10)

- 50 sources registered (PW049 dropped). 141 values extracted from archived copies, each with location and quote: 139 ai_checked, 2 unverified because no local copy is held yet (see BB_search.txt).
- Human verification not yet started (use [../human_checks/](../human_checks/)).
- Re-extraction corrected several values cited before 2026-11-10; the changes are listed in [notes/scaleup_assessment.md](notes/scaleup_assessment.md).
- Supply cost per kW is still sparse, especially for kHz inverters and RF generators.

## Reproduce

From `power_systems/`: `python3 figures/scaleup_wall_basis.py` and `python3 figures/plot_supply_values.py` (needs matplotlib; see `scripts/requirements.txt`).
