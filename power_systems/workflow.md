# Power-systems evidence workflow

Version 0.1 - 2026-11-10. Prepared by Claude (AI) at BB's request. It follows the same principles as the literature extraction workflow ([../literature_reforming/workflow.md](../literature_reforming/workflow.md)): every number traces to a stored copy of its source, with a location and a verbatim quote, and has a review status.

## 1. Scope

This folder holds data on industrial power supplies: efficiency, unit power, frequency, cost, lifetime and voltage. Sources are mainly manufacturer documents, patents, tenders, trade press, project reports and conference abstracts. A peer-reviewed paper may be registered here when only one or two supply values are taken from it. Papers that are read and assessed as a whole belong in [../literature_plasma_powersupply/](../literature_plasma_powersupply/README.md) (supply side) or [../literature_reviews/](../literature_reviews/reviews_shortlist.md); values from them are cited in `supply_values.csv` by their PS or RV ID.

## 2. Register the source

1. Assign the next ID in [source_register.csv](source_register.csv): PW001, PW002, ... IDs are never reused. A dropped source keeps its ID with status `dropped`.
2. Save a local copy in `source_archive/<ID>/` (gitignored, not redistributed): `original.<ext>` for a direct download, `wayback_<timestamp>.<ext>` for an archive copy, or the file name as downloaded for a manual download. Record the SHA-256 and size.
3. Make a Wayback Machine snapshot where possible and record its URL.
4. Fill the register columns:
   - `aliases`: IDs used for the same source in earlier notes (S, T and D series before 2026-11-10);
   - `doc_type` and `quality_tier` (section 3);
   - `document_date`: the date printed on the document or page, or `undated`;
   - `status`: `active` (local copy held), `to_retrieve` (no copy yet; see [BB_search.txt](BB_search.txt)) or `dropped`.
5. Sources that need a human to retrieve them go into BB_search.txt. Quotes to request from vendors go into [suggested_quote_requests.txt](suggested_quote_requests.txt).

## 3. Quality tiers

| Tier | Sources | Use |
|---|---|---|
| 1 | Peer-reviewed full text with a measured value; manufacturer datasheet or catalogue for a named model; standards | Can support a stated value on its own |
| 2 | Manufacturer web page or brochure ("up to", family claims); patent background sections; tender requirements; project reports; conference abstracts; trade press quoting a vendor; TEA estimates | Usable with the qualifier and data type kept; prefer a tier 1 source when one exists |
| 3 | Knowledge-base and blog pages, news, listings, undated secondary pages | Context or a lead to a better source; not used alone for a headline number |

The tier describes the source. The data type of each value (section 4) says what kind of claim it is.

## 4. Extract values: supply_values.csv

One row per quoted value. A row is extracted only from the local copy, never from a search summary. A value whose source has no local copy may be carried over from earlier notes with status `unverified` until the copy is obtained.

| Column | Content |
|---|---|
| `value_id` | `<source ID>-V01`, `-V02`, ... |
| `source_id` | PWxxx, or a PS/RV ID for papers held in the literature folders |
| `location` | page (printed or PDF, say which), section, table or claim number |
| `quote` | the shortest verbatim text that carries the value (original language if not English, with translation in `notes`) |
| `item` | model, product family, installation or device as named in the source |
| `maker` | manufacturer or operator |
| `supply_class` | class code from [supply_classes.csv](supply_classes.csv) (J1, J2, A1, K1, K2, R1, R2, M1-M3, P1, H1, X1), or `context` |
| `freq_low_hz`, `freq_high_hz` | output frequency or band; DC = 0; blank if not stated |
| `quantity` | `output_power`, `input_power`, `peak_power`, `average_power`, `installed_power`, `efficiency`, `coupling_efficiency`, `cost_per_kw`, `cost_ratio`, `cost_share`, `cost_ratio` (relative cost), `frequency_limit`, `duty_cycle`, `heat_rejected`, `lifetime_h`, `voltage_rms`, `current_rms`, `power_factor`, `specific_energy`, `capacity` (product rate) |
| `qualifier` | `=`, `~`, `>`, `>=`, `<`, `<=`, `up_to`, `approaching`, `range` |
| `value_low`, `value_high` | numbers as stated (same value in both for a single number) |
| `unit` | `kW`, `kVA`, `fraction`, `EUR/kW`, `USD/kW`, `h`, `V`, `A`, `kWh/kg`, `kg/h`, ... Efficiencies are stored as fractions |
| `basis` | what the value refers to. Efficiency: `device` (tube or transistor), `amplifier_or_head`, `generator` (mains input to rated output), `power_supply_stage` (HV or switch-mode supply feeding a separate head), `into_load` (measured into a stated load), `system`, `not_stated`. Power: `rated_output`, `rated_input`, `family_max`, `installed`, `average`, `peak` |
| `cost_scope` | cost rows only: `tube_only`, `head_only`, `supply`, `turnkey_system`, `supply_plus_reactor`, `share_of_plant_capex`, `not_stated` |
| `currency`, `price_year` | cost rows only; `price_year` is the year of the document if no other year is given, or `undated` |
| `data_type` | `vendor_spec` (datasheet value for a model), `vendor_claim` (marketing or family claim), `measured`, `requirement` (tender), `estimate` (author estimate), `projection`, `patent_background`, `secondary` (the source quotes another source), `reviewer_calc` |
| `status` | `ai_checked`, `human_verified` or `unverified` |
| `extracted` | date of extraction |
| `notes` | boundary caveats, conversions, translation |

Rules:

- A statement without a number (e.g. "a substantial part of the investment") may be recorded with blank value, qualifier and unit, so that notes can cite it; it is never plotted.
- Keep the source's own number and qualifier. Do not round, convert "up to 80%" into 0.80 without the `up_to` qualifier, or combine values from different sources in one row.
- Reviewer arithmetic (for example 2,000 GWh/y to an average MW) goes in its own row with `data_type = reviewer_calc`, the formula in `notes`, and the input row's ID.
- Unit conversions for plotting (currency, price year, W to kW) are done in scripts, not in this file.
- Record what the efficiency includes. A tube or transistor efficiency is not a generator efficiency, and neither is a wall-to-load efficiency.

## 5. Supply classes: supply_classes.csv

[supply_classes.csv](supply_classes.csv) summarises each representative class (J1, A1, K1, ...) used in the scale-up assessment. Each efficiency, cost and lifetime range lists the `value_id`s it rests on. Where a range is a reviewer judgement (for example a lower bound allowing for transformer losses), say so in `range_basis`. The class table is derived from supply_values.csv and is never edited without updating the cited values.

## 6. Notes, scripts and figures

- `notes/` holds the written analysis: [scaleup_assessment.md](notes/scaleup_assessment.md), [supply_maturity_niche.md](notes/supply_maturity_niche.md), [reactor_matching.md](notes/reactor_matching.md). Notes cite value IDs or source IDs, not search summaries.
- `scripts/` reads supply_values.csv and supply_classes.csv and writes to `figures/`. Scripts do not contain data values except documented constants (e.g. currency conversion factors with their source).
- `legacy/` keeps superseded work unchanged for the record. Do not cite it; its sources have been re-registered.

## 7. Checks and logging

- Log each extraction session in [processing_log.md](processing_log.md) (tool and model versions only there).
- Human checks use the shared logs in [../human_checks/](../human_checks/), with `value_id` as the record ID, following section 3b of the literature workflow. Steps and priorities are in [human_check_checklist.md](human_check_checklist.md); the worksheet is generated by `scripts/make_check_worksheet.py`. A source becomes human_verified only when its rows have been checked and all findings resolved.

## Version history

| Version | Date | Change |
|---|---|---|
| 0.1 | 2026-11-10 | First version. Replaces the separate S, T and D series with PW IDs; one value table; legacy survey frozen |
