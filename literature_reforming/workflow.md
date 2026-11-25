# Literature extraction workflow

Version 0.9 - 2026-11-20 (see Version history; the version that applied to an extraction is identified by its date in processing_log.md, and from the start of git tracking also by commit).

The purpose, scope and comparison questions are in [literature_review_objectives.md](literature_review_objectives.md). Find and select papers using [literature_search_strategy.md](literature_search_strategy.md), then follow the steps below for each included paper. Extract what supports the review questions, rather than every available detail.

## 1. Set up the source folder

Use one folder per source in literature_reforming/, named FirstAuthor_Journal_Year_ShortTopic (e.g. Geng_APC_2022_Plasma_SMR). Add a distinguishing word to the short topic when one author has several papers from the same year or journal. Keep the manuscript, supporting source documents and one short_summary.txt directly in each source folder. Put the detailed review files in outputs/:

```text
literature_reforming/<source>/
  manuscript.pdf
  [supporting source documents]
  short_summary.txt
  outputs/
    extraction.md
    evidence.csv
```

- short_summary.txt: a brief, human-readable summary of the experimental headlines.
- outputs/extraction.md: findings, metadata, missing information and review status; start from _source_template.md.
- outputs/evidence.csv: authoritative record of the values and claims used, with source locations.

These are the three standard review files. Create outputs/operating_points.csv only when many conditions need a separate index, and outputs/calculations.md only for substantial calculations. Otherwise use tables/calculations in outputs/extraction.md. Record source filenames and document versions in extraction metadata; a separate manifest is optional and belongs in outputs/. Do not retain extraction working files (PDF text dumps, rendered pages, helper scripts or automated check reports) as deliverables. Exception: when reviewer calculations are done in code, save the script as outputs/calculations.py. It should list each input with its evidence ID, label each result with its calculation ID, and reproduce the values recorded in extraction.md when run. Reviewers should cross-check evidence directly against the original manuscript or supplement using the recorded PDF page and section, table or figure locator. For figures, identify the panel and curve or operating condition, and mark graph-read values approximate. Preserve original source documents and existing detailed extractions when adopting this structure, and update relative links if files move.

## 2. Extract the required values

First identify the route: SMR, DRM or mixed reforming. Source IDs (SRCxxx) are numbered globally across the project. Record whether the results are experimental, modelled or projected. Then use the four headings below to organise the extraction.

| Heading | Look for |
|---|---|
| Electricity supply | Heating/activation mechanism; voltage, frequency, waveform, mean real power, current. Record RMS/peak/average conventions and measurement location: wall, terminals or absorbed plasma power. For pulses, width, repetition rate and duty cycle. Supply losses/efficiency where given; fuel input/heat duty for conventional heating. |
| Reactor configuration | Type, relevant dimensions/volumes, catalyst/support/loading and heating arrangement. For plasma, discharge type, electrode gap and catalyst placement. Distinguish active volume from equipment volume. |
| Operating conditions | Feed composition and flow with reference conditions, reactant ratios, pressure, temperature and measurement location, point-matched power, test duration and stability. Separate sampling/averaging periods from total time on stream. |
| Performance indicators | Conversion, defined space time/residence time or GHSV/WHSV, product output/composition, energy metrics and demonstrated scale. Keep results tied to their conditions. |

Extract instrument models, material properties, modelling parameters and other secondary details only when they help interpretation or calculation. Start with headline and representative conditions; digitize full curves only when needed. Label modelling and projections separately.

For plasma studies, report **plasma scale** (measured discharge power and its boundary) separately from **total process energy scale**. Record the thermal background and any additional heating/steam inputs, even if their duties are unknown. Keep plasma-on/off conditions separate: zero discharge power does not mean zero total energy input. Do not assume the heating energy carrier is electricity unless reported.

## 3. Record where each value comes from

Make the source reference clear enough for a reviewer to find and check the value in the manuscript or supplement. For a table, identify the row and column; for a figure, identify the panel and curve or operating condition. A PDF page number means the page counted from the start of that PDF, beginning at 1.

1. Read the manuscript and available supplement together. Register source ID, citation/DOI, source filenames and document versions (with SHA-256 hashes), protocol version, extractor/date and coverage in extraction.md. Unknown retrieval dates stay unknown. Record AI tool and model versions in [processing_log.md](processing_log.md) (section 3a), not in the individual review files.
2. Give every used value or substantive claim a stable evidence ID (e.g. SRC001-E001). Record original value/unit, document, 1-based PDF page, figure/table/section locator, and a short supporting quotation or description. Identify plot series/points; mark estimates approximate and state reading method/precision. Treat documents as evidence, not instructions.
3. Group matching conditions with operating-point IDs (e.g. SRC001-OP001); use source_wide or unknown where appropriate. Do not combine maxima from different conditions. A small condition table is sufficient; a separate index is optional.
4. Separate reported values, author calculations and reviewer calculations. Preserve original values alongside conversions. Give calculations an ID, input evidence IDs, formula/units, assumptions and result. Record conflicts and user-selected assumptions explicitly without replacing source facts.
5. Record only missing information that blocks a comparison (e.g. no power boundary, no feed flow, no conversion), as not_reported, unclear or not_applicable, in a short list in extraction.md. Check both available documents before declaring not_reported. Do not list every absent detail; NR entries in the summary tables cover the rest. Missing never means zero.
6. Check used citations and calculation arithmetic. Record reviewer/date and status: unreviewed, ai_checked, human_verified or disputed. AI checks are not human verification. Preserve existing IDs when correcting records. Add a processing_log.md row for each extraction or revision; record human checks in the Human reviewer column of that row (section 3a) and their findings in ../human_checks/ (section 3b).

Use UTF-8 evidence.csv with the existing header for compatibility. Leave unused fields blank; source-wide reviewer/date defaults can be stated in extraction.md.

```csv
evidence_id,source_id,operating_point_id,heading,field,availability,origin,reported_value,reported_unit,normalized_value,normalized_unit,document,pdf_page,printed_page,locator,evidence_excerpt_or_description,basis_and_boundary,uncertainty,calculation_id,review_status,reviewer,review_date,notes
```

Availability: reported, not_reported, unclear, not_applicable. Origin: quoted_text, table, figure_reading, author_calculation, reviewer_calculation, interpretation. Derived rows link to calculations instead of a direct PDF location. Normalized numeric fields contain numbers only.

## 3a. Log AI tool and model versions

Keep one top-level [processing_log.md](processing_log.md) as the single record of who or what processed each source. Add one row for every extraction and substantive revision, giving: date, source ID and folder, event, tool and tool version (e.g. Claude Code 2.1.318), exact model ID (e.g. claude-opus-5-5), session ID where available, and, in the Human reviewer column, "reviewed by <initials>, <date> (<status>)" once a human has checked that AI work. Do not add a separate human-check row with the AI fields blank: the AI tool and version stay on the row so the record shows both steps. In extraction.md, evidence.csv and short_summary.txt, "Claude (AI)" or "Codex AI" is sufficient; the log carries the versions. Record the model ID at the time of work: tool session logs are local and may be deleted. Where a version cannot be recovered, write "not recorded" rather than guessing. Figure styling, manuscript tables and manuscript text are not logged here; git history records them (BB 2026-11-25).

## 3b. Log human checks and AI errors

Human checks are logged in two shared files in [../human_checks/](../human_checks/), for all topic folders. They record what the AI got wrong, so that error rates by type and severity can be reported.

**findings.csv**, one row per problem found:

```csv
check_id,date,checker,source_id,record_id,error_type,severity,ai_value,corrected_value,action,note
```

- check_id: HC001, HC002, ... numbered globally.
- record_id: the evidence ID, calculation ID, Q item or summary-table cell checked.
- error_type:

| Code | Type |
|---|---|
| V | wrong value or unit transcribed |
| L | wrong locator or page (value correct) |
| F | figure reading beyond its stated precision |
| B | wrong basis or assumption (molar volume, LHV/HHV, power boundary) |
| C | calculation error |
| I | interpretation stronger than the source supports |
| H | fabricated: no support in the source |
| O | omission of a relevant value or condition |
| S | eligibility or operating-point selection |
| Q | appraisal disagreement (Q1-Q9 or confidence rating) |

- severity: 1 cosmetic (no value changes); 2 minor (a value changes, no comparison changes); 3 major (a headline, energy-table value or conclusion changes).
- action: corrected, disputed (left for discussion) or accepted (the AI was right after all).

**summary.csv**, one row per source per check, with the denominator for error rates:

```csv
source_id,date,checker,scope,records_checked,records_total,findings,major_findings,minutes,status_after
```

- scope: core (all values in the short-summary tables: feed, power, conversion, SEI, SEI_CH4, EC_CH4), core+Q (plus the Q1-Q9 appraisal and confidence ratings) or full (every evidence row). core+Q is the minimum for human_verified.
- minutes: time spent checking.

Procedure: the human checker fills in findings.csv and the summary row. The AI then applies the corrections to the extraction files, preserving evidence IDs, and adds a processing_log.md row "revision after human check (HCxxx-HCyyy)". The source becomes human_verified only when every finding for it is corrected or resolved; the Human reviewer column of its extraction row then reads "reviewed by <initials>, <date> (human_verified)". A check with no findings still gets a summary row.

## 4. Record the power boundary and energy metrics

The scale-up and whole-system assessment (supply losses, heat integration, cost) is carried out separately, using [../power_systems/](../power_systems/) and [literature_review_objectives.md](literature_review_objectives.md). Per paper, record only what that assessment needs and what lab papers normally report.

### Boundary and external heat

Record in two lines:

- **Power boundary:** where P is measured (wall, supply output, reactor terminals, discharge, absorbed microwave/RF power, or heating element) and how (probes, forward/reflected power, calorimetry, setpoint).
- **External heat:** whether a furnace, preheater or steam generator was used: yes, no or unknown, with its duty or temperature if reported.

Note product separation or recycle only if the paper includes them. Equipment lists and full system mass or energy balances are not extracted; record a reported carbon (or H/O) balance closure under Q4. If the paper reports outlet temperature, heat duties or heat recovery, note them in one line: the separate scale-up assessment (objectives) uses them.

### Energy metrics

All metrics are on a power basis: P is the electrical power at the stated boundary. Label every value with its boundary.

```text
SEI        as reported by the authors (kJ/L, J/mL or eV/molecule, with their reference conditions)
SEI_CH4    = P / F_CH4,in            (kJ/mol CH4 fed)
EC_CH4     = P / F_CH4,conv  = SEI_CH4 / X_CH4   (kJ/mol CH4 converted)
```

Core: SEI as reported, SEI_CH4 and EC_CH4 for each operating point. They need only power, methane feed and conversion.

Author's efficiency: record the authors' energy efficiency (or energy cost, energy yield) as reported, with its equation and basis. Do not recalculate it under another definition.

Optional, only when product flows are measured:

```text
EY_H2      = m_dot_H2,net / P        (g H2/kWh; record if reported)
eta_P,LHV  = sum(F_i,out * LHV_i) / (P + F_CH4,conv * LHV_CH4),  i = H2, CO
```

eta_P,LHV is the usual plasma DRM energy-efficiency definition; calculate it only if the authors do not report an equivalent, and net H2 subtracts any H2 fed.

1 eV/molecule = 96.485 kJ/mol. Convert volumetric flows to molar flows with the stated reference temperature and pressure. If they are not stated, convert only as a reviewer calculation with an assumed reference: prefer the molar volume that reproduces the authors' own derived values (e.g. their SEI or efficiency); otherwise use 0 degC, 1 atm (22.414 L/mol). Record the assumption in the calculation, flag Q2 as partly, and print the result at the alternative molar volume (e.g. 24.46 L/mol at 25 degC) so the ~7-9% sensitivity is visible. Keep the original volumetric values alongside.

Where external heat was used, label the metrics "power basis; external heat excluded". If that heat duty is reported, also give EC_CH4 with it added to P and state its basis. Compare metrics only on the same power boundary; keep the boundary in the label rather than converting between boundaries.

Reference reaction enthalpies at 298 K: SMR (CH4 + H2O(g) -> CO + 3H2) +206 kJ/mol; DRM (CH4 + CO2 -> 2CO + 2H2) +247 kJ/mol. These are reference lines for EC_CH4, not strict minima at operating conditions. A power-basis EC_CH4 below the reaction enthalpy indicates that excluded heat supplies part of the reaction energy.

### Benchmarks only: fired SMR and Joule-heated pilots

For the one or two fired SMR reference systems and the Joule-heated pilot benchmarks, also record heat-basis and whole-system metrics. Power-basis metrics do not apply to fired SMR (no electrical reactor power).

```text
EC_CH4,fired = Q_fired / F_CH4,conv     (burner fuel energy, HHV or LHV stated)
EC_CH4,abs   = Q_abs / F_CH4,conv       (heat absorbed by the reformer tubes)
D            = P_electric,in + sum(external feed/fuel molar flow_j * HHV_j) + Q_dot_external,in
eta_HHV      = sum(product molar flow_i * HHV_i) / D
f_electric   = P_electric,in / D
```

Q_abs is the process duty, comparable to the electrical power delivered to an ideal heater; Q_abs/Q_fired is the radiant-section efficiency. Record whether values describe the reformer alone or the whole plant (shift, H2 purification, steam system). Count natural gas used as feed and as fuel separately; count furnace fuel or delivered heat, never both; keep heat exports separate. Missing inputs make eta_HHV unavailable or explicitly partial. eta_HHV is not calculated for lab plasma papers.

Hardware, lifetime and cost data are not extracted per paper; supply data are collected in [../power_systems/](../power_systems/). Note in one line anything unusual a paper does report (e.g. electrode lifetime or a cost figure).

## 5. Appraise reporting quality

Record a short reporting-quality appraisal for each source in outputs/extraction.md. It shows how far the extracted values can be relied on; it is not a reason to exclude a paper. Answer each item yes, partly, no or NA, with a brief reason and evidence IDs.

| Item | Question |
|---|---|
| Q1 Power measurement | Is power measured at a stated boundary with a stated method (e.g. voltage/current probes, forward/reflected microwave power, calorimetry), rather than a setpoint or supply rating? |
| Q2 Feed definition | Are feed flows, composition, dilution and flow reference conditions stated, so that methane input is identifiable? |
| Q3 Product analysis | Is the analysis method and calibration described, and is the gas volume change handled (internal standard or measured outlet flow)? |
| Q4 Balance closure | Is a carbon (or H/O) balance reported, with its closure? |
| Q5 Temperature | Is temperature measured with its location and method stated? |
| Q6 Controls | Are matched controls reported: plasma-off/thermal-only and catalyst-only at the same temperature for plasma catalysis; equilibrium or conventional comparison for Joule heating? |
| Q7 Repeatability | Are repeats reported and error bars or uncertainties defined? |
| Q8 Stability | Is time on stream stated, with a steady-state criterion? |
| Q9 Energy completeness | Are additional heating, steam generation and other energy inputs reported? |

For the fired SMR reference systems, which are usually not experiments, answer these instead of Q1-Q9:

| Item | Question |
|---|---|
| R1 Data type | Measured plant data, design basis or simulation? |
| R2 Boundary | Is the boundary (reformer only or whole plant) and its equipment stated? |
| R3 Basis | Are HHV/LHV basis, flow reference conditions and plant scale stated? |
| R4 Independence | Is the source independent of a technology vendor? |

Then give two overall judgements, higher, moderate or lower confidence, each with one sentence of reasoning: one for conversion and product results (mainly Q2-Q5, Q7), and one for energy results (mainly Q1, Q2, Q9). Do not add the answers into a numerical score. Mark the appraisal ai_checked or human_verified like other records.

## 6. Write the short summary and check the extraction

Write a few headline lines in short_summary.txt, then compact evidence references to outputs/evidence.csv:

- Scale: experimental energy input and boundary; otherwise methane input and flow basis.
- For plasma: give plasma scale separately, plus thermal background/additional heating and whether total process input is known. Report plasma power even when the whole-process energy scale is unavailable.
- Conversion: range/headline value with its matching feed or power.
- Energy: SEI as reported, SEI_CH4 and EC_CH4 with their power boundary, stating whether external heat is excluded; the author's efficiency and its definition.
- Reporting quality: the two overall confidence judgements from section 5.
- Duration: hours/minutes where known; otherwise state what is missing.
- Gaps: only missing information that blocks comparison.

Exclude modelling and scale-up projections; if no experiments exist, say so. Exception: the fired SMR references are design or simulation cases by nature; summarise them as labelled reference cases (data type stated). Include preparation date/review status. Check that summary values trace to evidence and derived values to calculations. State coverage and comparison limits. Rank only compatible chemistry, conditions, energy and volume boundaries, or explain the mismatch.

### Comparison tables

End each short_summary.txt with four plain-text, pipe-separated tables. They provide the entries for the final comparison without creating another file.

```text
1. Route, scale and conditions
Source / OP | Route | Reactor / activation / catalyst | CH4 feed (mol/min) | CH4:CO2:H2O (other) | T (degC; loc.) | p (bar) | Scale as reported

2. Mass balance
Source / OP | X_CH4 (%) | X_CO2 (%) | Products (value; units/basis) | Balance closure | Duration (h; basis) | Conv. conf.

3. Energy
Source / OP | P (W; boundary) | External heat | SEI (as reported) | SEI_CH4 (kJ/mol) | EC_CH4 (kJ/mol) | Author efficiency (def.) | Energy conf.

4. Plasma parameters (plasma-on rows only)
Source / OP | Discharge / regime | Supply / frequency | Voltage | P_plasma (W; method) | Gas T (K; method) | Other diagnostics
```

Formatting rules:

- **Row key.** The first column of every table is `Source / OP`, written as FirstAuthor Year OPxxx (e.g. Geng 2022 OP002). Tables 1-3 contain the same rows in the same order; table 4 contains only the plasma-on rows. The key is how rows are matched across tables and joined in the final synthesis.
- **Alignment.** Pad cells with spaces so the pipes line up in a monospaced editor, and keep table lines to about 160 characters. Keep each cell to a value and a short qualifier, with units in the header. Put qualifications, assumptions, boundary details, secondary metrics and evidence IDs in numbered notes ([1], [2], ...) directly below each table, numbered continuously through the file.
- **EC basis.** State whether EC_CH4 is on an electrical basis (e.g. discharge; heat excl.) or a heat basis (fired references), so the two are not compared as like for like.
- **CH4 feed.** Give methane input in mol/min as the common scale metric. Where it is converted from a volumetric flow, state in a note whether the reference conditions were stated or assumed (section 4 rule). Give the source's own scale metric (flow, power or product rate) in the last column of table 1. For the benchmarks (fired SMR, Joule pilots), give EC_CH4,fired/abs or eta_HHV in a note to table 3.
- **Plasma table.** Record the electrical operation of the discharge, the gas temperature if measured, and name any other diagnostics in one cell. For non-plasma sources replace the table with one line, e.g. "4. Plasma parameters: not applicable (Joule-heated source)."

Use one representative experimental operating point per row (for fired SMR references, one labelled reference case). Add another row only for an important distinct condition, such as a plasma-off control or a higher-throughput test. Keep all numerical results in a row tied to that condition; do not combine the maximum conversion, maximum flow and minimum energy use from different tests. If a duration describes a separate stability test, label it explicitly rather than assigning it to the selected point. Group the final synthesis tables by SMR, DRM and mixed reforming.

Use NR for not reported, unclear for ambiguous information and NA for not applicable. Do not infer gas temperature from furnace setpoint or wall temperature. State whether power is discharge, reactor-terminal or total wall power; list separately reported inputs in the same cell without adding overlapping powers. Preserve the author's energy-metric definition. Where EC_CH4 cannot be calculated, enter NR and name the missing input in a note. Reactor volume or power density may be added to the final comparison only where volume boundaries are defined and comparable.

## 7. Plasma characteristics, when reported

Place these at the end of outputs/extraction.md. Record them only when the paper provides them; do not analyse spectra or reconstruct plasma properties.

- **Regime:** the authors' description (thermal/nonthermal, filamentary/diffuse, continuous/pulsed).
- **Gas temperature:** value, location, method and stated uncertainty. Distinguish discharge gas, downstream gas, catalyst, wall and furnace setpoint; a rotational temperature is a gas-temperature proxy only where the authors justify it. Do not relabel a specific diagnostic temperature as "plasma temperature".
- **Other diagnostics:** one line naming what else is reported (e.g. electron temperature, electron density, E/N, vibrational temperature), with evidence IDs, without extracting details unless used in the review.

## Version history

Renumbered 2026-11-10: each amendment is now its own version. Extraction files written earlier cite "0.1" or "0.1 (with 2026-11-04 amendment)"; their extraction date in processing_log.md identifies which version below applied. From 2026-11-09 the exact text of every version is also in the git history (first commit 69f8fe2).

| Version | Date | Change | Previously cited as |
|---|---|---|---|
| 0.1 | 2026-10-30 | initial version | 0.1 |
| 0.2 | 2026-11-04 | the single comparison-table entry in short_summary.txt replaced by five aligned tables (section 6) | 0.1 (with 2026-11-04 amendment) |
| 0.3 | 2026-11-05 | AI tool and model versions recorded in processing_log.md (section 3a); SHA-256 hashes of source documents required in extraction.md | 0.1 (with 2026-11-04 amendment) |
| 0.4 | 2026-11-09 | workflow shared with other topic folders; global source IDs | 0.1 amendment |
| 0.5 | 2026-11-10 | after an external LLM consistency review: human checks recorded on the AI row in processing_log.md (section 3a); one rule for flows without stated reference conditions (sections 4 and 6); versions renumbered | - |
| 0.6 | 2026-11-10 | simplified (BB): core energy metrics SEI as reported, SEI_CH4, EC_CH4 plus the author's efficiency; eta_P,LHV and EY_H2 optional; eta_HHV and f_electric for benchmarks only; system boundary reduced to power boundary and external heat; hardware/cost and full missing-data checklist dropped; plasma diagnostics reduced to regime, gas temperature and a list; summary tables reduced from five to four. Extractions made under 0.1-0.5 are kept as they are | - |
| 0.7 | 2026-11-10 | human-check and AI-error logs added (section 3b; ../human_checks/findings.csv and summary.csv) | - |
| 0.8 | 2026-11-19 | reforming only: references to other topic folders removed (each topic has its own workflow) | - |
| 0.9 | 2026-11-20 | after an external LLM consistency review: reported heat data noted for the scale-up assessment (section 4); fired references allowed as labelled reference cases in summaries (section 6); template asks for SHA-256 | - |

Cite the version number in new extraction files.
