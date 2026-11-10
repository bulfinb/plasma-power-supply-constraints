# Literature review objectives

Version 0.2 - 2026-11-05 (0.1: 2026-10-30).

## Main objective

To benchmark the state of the art in plasma methane reforming, using published experimental evidence, against Joule-heated (eSMR) and conventional fired reforming; and to assess what each electrified route would require at industrial scale, from wall electricity to product.

The review has two parts:

1. **Demonstrated performance.** A traceable comparison of what has been demonstrated, under which conditions, on a stated power boundary, and what information is missing.
2. **Scale-up and whole-system view.** An indicative assessment of each reactor type scaled up with representative, industrially available power supplies: power-supply and coupling losses, heat integration, durability, and supply cost. In an optimised electrified plant, unrecoverable losses of the order of 20% in power delivery are significant, so the review treats supply efficiency, heat recovery and cost alongside plasma performance rather than as afterthoughts.

## Scope

Include the following reforming routes:

- Steam methane reforming (SMR).
- Dry methane reforming (DRM).
- Mixed reforming, including feeds containing both steam and carbon dioxide.

Include plasma systems with and without catalysts. Use conventional and Joule-heated reforming studies as benchmarks where suitable evidence is available. Joule-heated reforming is the primary benchmark: it is also electrically driven, but delivers the electricity as heat to a conventional catalytic reaction. Comparing plasma systems with it helps show what plasma activation adds beyond electrical heating. From et al. (2024), Topsoe's eSMR pilot plant on biogas (SRC005, From_CEJ_2024_eSMR_Biogas), is the primary Joule-heated benchmark: it reports a measured reactor energy efficiency and about 2000 h of operation, although its feed contains CO2 and point-matched power is not tabulated. Its follow-up, From et al. (2025, SRC006, From_CEJ_2025_eSMR_Biogas2), adds conversion and stability data from the same plant but no energy data. Wismann et al. (2019, SRC001) is the lab-scale complement for conversion and conditions.

Conventional flame-heated (fired) SMR is the industrial reference: the performance that electrified reforming must match or improve on. It is not reviewed in depth and is not part of the literature search. Instead, select one, or at most two, representative fired SMR systems directly, from an industrial design study, reference-plant report, handbook or published plant data. Label the data type (measured plant data, design basis or simulation) and never present it as an experimental demonstration. Wismann et al. (2019) also includes a side-fired reference design (SRC001-OP013), but it reports no fuel duty, so it supports volume and conditions comparisons only. The two selected fired reference systems, both extracted 2026-10-30 (SRC003 in Lewis_NETL_2022_Fired_SMR, SRC004 in Collodi_IEAGHG_2017_Fired_SMR): NETL, *Comparison of Commercial, State-of-the-Art, Fossil-Based Hydrogen Production Technologies*, DOE/NETL-2022/3241, 12 April 2022 (OSTI 1862910), which includes natural gas SMR cases with and without CCS; and IEAGHG, *Techno-Economic Evaluation of SMR Based Standalone (Merchant) Hydrogen Plant with CCS*, Report 2017-02, February 2017, whose base case is a 100,000 Nm3/h H2 SMR plant without CCS. Laboratory SMR in an electric tube furnace is a thermal control, not a fired-reformer benchmark.

This folder covers reforming. Methane pyrolysis/coupling and CO2 splitting are reviewed in the sibling folders [../literature_pyrolysis/](../literature_pyrolysis/) and [../literature_co2_splitting/](../literature_co2_splitting/), using this workflow.

The first search category covers experimental demonstrations of electrified, endothermic methane reforming using Joule heating or plasma. Exclude modelling-only studies, autothermal reforming and partial oxidation/other oxidative reforming experiments. Papers combining experiments and modelling are eligible for their qualifying experimental results. Record modelling and scale-up projections separately so that projected performance is distinguishable from demonstrated performance. Detailed eligibility criteria are in [literature_search_strategy.md](literature_search_strategy.md).

## Questions the review should answer

1. What reactor and plasma arrangements have been demonstrated, and at what scale?
2. What feed composition, temperature, pressure, electrical input and catalyst conditions were used?
3. What methane conversion, product composition or output, and energy performance were achieved under those conditions?
4. How long were systems operated, and what evidence of stability or deterioration was reported?
5. How do these results compare with suitable reforming benchmarks, and what missing information limits that comparison?

## Basis for comparison

Group results by reforming route before comparing performance. SMR, DRM and mixed reforming are all in scope, but their different feeds and products must remain clear. Avoid a single ranking across unlike conditions.

Keep performance tied to the operating conditions at which it was measured. Distinguish discharge power from the energy used by the whole process, including additional heating and steam preparation where reported. Compare energy efficiencies only when their definitions and included inputs are compatible.

The intended outcome is a concise account of demonstrated performance, strengths, limitations and evidence gaps. Extract details that help answer these questions; a complete transcription of every paper is unnecessary.

Record internal plasma characteristics as supporting catalogue information; detailed plasma mechanisms are not a primary objective of this review.

## Energy performance indicators

The primary energy indicator is the field's power-basis energy accounting: specific energy input (SEI) and energy cost per mole of methane converted (EC_CH4), together with SEI per mole of methane fed and the authors' own efficiency as reported; H2 energy yield and power-basis efficiency are added only where product flows allow. These metrics are calculable for most experimental papers and allow plasma and Joule-heated systems to be compared on the electrical power applied to the reactor. Their power boundary, and whether external heat is excluded, is always stated.

The whole-system HHV efficiency (eta_HHV) is calculated for the benchmarks (fired SMR and Joule-heated pilots), not for lab plasma papers, which do not report the inputs it needs. Definitions are in [workflow.md](workflow.md), section 4.

## Synthesis plan

The synthesis is descriptive. Results from different reactors, conditions and boundaries are too varied for pooled statistics or meta-analysis.

1. **Evidence table.** One row per selected operating point, grouped by route (SMR, DRM, mixed). Within each route, group by activation: fired reformer (reference; SMR only), Joule heating (benchmark), thermal arc/torch, microwave, gliding arc, dielectric barrier discharge and other plasma. Assemble it from the four tables (five for extractions made before workflow 0.6) at the end of each source's short_summary.txt, joined on the `Source / OP` key. Keep the plasma parameters as a separate table for plasma rows.
2. **Energy-conversion plot.** For each route, plot CH4 conversion against EC_CH4 (logarithmic axis), with marker shape by activation type. Show the 298 K reaction enthalpy as a reference line. Where external heat is reported, pair the power-only point with the point including external heat. Several matched points per paper may be plotted, identified by source. Show the fired SMR reference as a marker or band using reformer heat per mole of methane converted (fired duty and absorbed duty, section 4 of workflow.md). Distinguish its heat basis from the electrical basis of the other points.
3. **Scale plot.** Plot EC_CH4 against applied power or methane throughput, to show whether energy performance changes with scale.
4. **Benchmark table.** List eta_HHV for the fired SMR references and Joule-heated pilots, with boundary and missing inputs. The fired SMR reference is the main like-for-like comparison with electrified systems. Compare at reformer level (reformer outlet syngas) where possible, and state plant-level values (after shift and H2 purification) separately.
5. **Reporting-quality summary.** One row per source with the Q1-Q9 answers and the two confidence judgements. Use lower-confidence results to qualify conclusions, not to exclude them.
6. **Narrative synthesis.** For each route: demonstrated scale, best matched conversion and energy performance, stability and duration, catalyst integration, comparison with the Joule-heated and fired benchmarks, and evidence gaps.
7. **Not-plotted list.** Sources or operating points that cannot be placed on the plots, with the missing input (e.g. no point-matched power).

Do not rank across routes or power boundaries. Do not convert electricity and fuel heat to primary energy unless a stated conversion factor is applied and labelled. When the Joule-heated benchmark lacks point-matched power, compare it on conversion and conditions only and state that limit.

## Scale-up and whole-system assessment

Assess scale-up potential using a combined system boundary containing the reactor, reactor peripherals and power electronics. Evaluate net mass and energy balances across that boundary, together with hardware cost, complexity, durability and utility requirements, as technical indicators of potential industrial deployment. Identify incomplete boundaries and missing flows rather than treating discharge performance as whole-system performance.

Use representative industrially available power supplies for each reactor type, not the laboratory supplies used in the experiments. The supply data, their sources and the efficiency chain from wall to reaction are kept in [../power_systems/scaleup_sources.md](../power_systems/scaleup_sources.md) and [../power_systems/scaleup_supplies.csv](../power_systems/scaleup_supplies.csv). Apply supply efficiencies only to the stages outside each paper's stated power boundary, and keep wall-basis results labelled as indicative.

Steps, in order of priority:

1. Wall-basis EC_CH4 (and EC_H2 where product flows allow) for each source, using the representative supply efficiency range.
2. Heat integration: identify the recoverable heat in hot products and the external heat (steam raising, preheat) each case would need, so that plasma cases can be compared with heat-integrated eSMR and fired SMR.
3. Cost and durability: supply capital cost per kW, tube and electrode lifetimes, catalyst stability, with currency, year and scope.

Demonstrated values and scale-up estimates must stay separate. Estimates are reviewer calculations with stated assumptions, not experimental results.

## How to carry out the review

Follow [workflow.md](workflow.md) for the extraction steps, required values, file structure and source references. A reviewer should be able to check each used value or claim directly against the original manuscript or supporting information.

## Version history

- 0.1 (2026-10-30): initial objectives.
- 0.2 (2026-11-05): scale-up and whole-system assessment moved from follow-on work into the review's objectives; scope wording generalised to the review goal.
- 0.2 amendment (2026-11-09): pointer to the new pyrolysis and CO2-splitting topic folders.
