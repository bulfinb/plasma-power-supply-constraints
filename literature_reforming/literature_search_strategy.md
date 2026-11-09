# Literature search and selection strategy

Version 0.1 - 2026-10-30.

## Purpose and current category

Find experimental demonstrations of **electrified, endothermic methane reforming**, beginning with Joule-heated and plasma systems. The review objectives are in [literature_review_objectives.md](literature_review_objectives.md). Extract included papers using [workflow.md](workflow.md).

This document describes the planned search. It does not imply that the searches have already been completed. Record the actual searches and any changes to this strategy.

## What to include

Include a paper when it meets all of these conditions:

- It reports an original experiment demonstrating methane reforming, with measured conversion or product formation. A reactor proposal or catalyst characterisation alone is insufficient.
- The reforming route is endothermic: steam methane reforming (SMR), dry methane reforming (DRM), or mixed steam/CO2 reforming (often called bi-reforming).
- Electrical activation or heating uses Joule/resistive heating or plasma. Plasma-assisted systems with additional external heating are eligible; record that heating explicitly.
- The paper provides enough information to identify the reactor, feed and at least one experimental performance result.

Include catalytic and non-catalytic systems, laboratory and larger demonstrations, and all reported plasma discharge types. No minimum conversion, efficiency, power or test duration is required. Missing energy inputs, uncertainties or durability data are recorded as limitations rather than automatic grounds for exclusion.

Papers combining experiments and modelling are eligible. Extract experimental results separately from modelled or projected results; only demonstrated experimental results enter the current comparison table.

## What to exclude

| Reason | Application |
|---|---|
| Modelling only | Simulations, thermodynamic calculations or proposed designs without a qualifying reforming experiment. |
| Oxidative reforming | Autothermal reforming, partial oxidation, oxidative steam/dry reforming, oxidative coupling, and tri-reforming involving intentional oxygen addition. Electrical assistance does not make these eligible. |
| Different reaction | Methane pyrolysis/decomposition, coupling or combustion without qualifying steam/CO2 reforming. Pyrolysis/coupling papers go to literature_pyrolysis; pure CO2 splitting to literature_co2_splitting. |
| Different feedstock | Reforming of methanol, ethanol or other fuels without a separately reported methane-reforming experiment. |
| Other electrification method | Microwave dielectric heating (no discharge), induction heating, photochemical or electrochemical systems without Joule-heated or plasma activation. Microwave, RF and other electrically generated plasmas are plasma systems and remain eligible. Retain potentially useful references for a later category rather than adding them to this one. |
| No original demonstration | Reviews, perspectives, patents or abstracts without sufficient original experimental results. Reviews may be used to find primary papers. |
| Duplicate evidence | Multiple records of the same paper, or repeated experimental results without new relevant data. Link companion reports rather than counting the same experiment twice. |

Screen mixed-scope papers by experiment. A paper containing both oxidative and qualifying endothermic experiments can be included for the latter only. Do not exclude a paper merely because it discusses partial oxidation in its introduction. Flag unclear reaction routes for discussion before inclusion.

Conventional fuel-heated reforming is outside the search. One or two representative fired SMR reference systems are selected directly as benchmarks; see [literature_review_objectives.md](literature_review_objectives.md).

## Where and when to search

Use Scopus and/or Web of Science where institutional access is available. Use Google Scholar as a supplementary discovery route and to locate accessible copies. Record which services were actually searched; do not imply coverage of an unavailable database.

Start without a publication-year restriction, searching through the recorded search date. Start with English-language full texts for practical screening; record potentially relevant papers excluded because a usable translation is unavailable. Prioritise journal articles; include full conference papers when sufficient methods and experimental results are available. Tag preprints separately and use the published version where available.

## Search terms

Run Joule-heating and plasma searches separately. These are starting Boolean expressions; adapt field labels and syntax to each database and save the exact expression used. For Scopus/Web of Science, begin with title, abstract and keyword fields. For Google Scholar, use shorter combinations from the same terms and record the results-screening limit.

**Joule/resistive heating**

```text
(methane OR biogas) AND
(reforming OR "steam methane reforming" OR "dry reforming" OR "mixed reforming" OR "bi-reforming" OR bireforming) AND
("Joule heating" OR "Joule heated" OR "resistive heating" OR "resistance heating" OR "ohmic heating" OR "electrically heated" OR "direct electrical heating")
```

**Plasma**

```text
(methane OR biogas) AND
(reforming OR "steam methane reforming" OR "dry reforming" OR "mixed reforming" OR "bi-reforming" OR bireforming) AND
(plasma OR plasmatron OR "dielectric barrier discharge" OR "gliding arc" OR "glow discharge" OR "spark discharge" OR "corona discharge" OR "arc discharge" OR "microwave discharge" OR "radio frequency discharge" OR "RF discharge" OR "nanosecond pulsed discharge" OR "pulsed discharge")
```

The term plasma also matches thermal plasma, plasma torch and microwave plasma. The named discharge types catch papers that describe the discharge without using the word plasma in searchable fields. Treat microwave, RF, DC/AC arc and torch systems as plasma systems.

Do not require the word experimental: relevant papers may not use it in searchable fields. Avoid broad NOT filters for modelling, oxygen or partial oxidation, since eligible mixed-scope papers may mention these terms. Apply the exclusions during screening.

Check the reference lists of included papers and relevant reviews, then look for newer papers citing the included demonstrations. Record these as backward or forward citation searches. Existing papers and shortlists are seed references, not evidence that the database search is complete; screen them against the same criteria.

## Selection steps

1. Record each search and export or save its results where practical.
2. Remove duplicate records, retaining the DOI or another stable identifier.
3. Screen titles and abstracts for potential relevance. Keep uncertain records for full-text screening.
4. Read the full text and available supplement against the criteria above. Record include, exclude or pending, with a short reason. A temporarily unavailable full text stays pending rather than becoming a scientific exclusion.
5. Assign an included source ID and create its source folder. Use the extraction workflow and the comparison tables in workflow.md section 6.
6. Have a human reviewer verify included experiments and extracted values, and record uncertain eligibility decisions with their reasons. Record who screened and checked the papers; do not imply independent duplicate screening if it was not performed.

Pilot this procedure on the two existing sources and a few new candidates. The existing sources are Wismann et al. (2019), Joule-heated SMR (SRC001, the Joule-heating benchmark), and Geng et al. (2022), plasma-assisted SMR (SRC002). Record changes to criteria and recheck earlier decisions when those changes could affect eligibility.

## Simple search and selection records

Keep two tables in a shared spreadsheet or text file under literature_reforming/. Choose one place for these records and avoid maintaining duplicate logs.

Search log columns:

```text
Search ID | Date | Database / discovery route | Exact query or seed paper | Fields / filters | Results returned | Results screened / stopping rule | Notes
```

Selection log columns:

```text
Record ID | Citation / DOI | Search IDs | Title/abstract decision | Full-text decision | Reason / qualifying experiments | Screener / date | Checker / date | Included source ID
```

Record one main exclusion reason at full-text stage. Preserve pending decisions and retrieval issues. If a supplementary search screens only a fixed number of results, record the number and sort order so that the limit is visible. Summarise numbers found, duplicates removed, full texts assessed and papers included when writing the review methods.
