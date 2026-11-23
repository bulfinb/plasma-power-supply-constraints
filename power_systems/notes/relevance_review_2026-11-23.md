# Power-supply relevance review

23 November 2026. Recommendations only: no source, value, class, calculation, manuscript or figure has been removed or changed by this review.

## Scope and decision rule

Reviewed all 61 PW source-register entries and all 209 rows in `supply_values.csv`, including the six additional PS/RV/SRC literature sources represented in that table. Checked dependencies in `supply_classes.csv`, the two topic synthesis builders, `figures/scaleup_wall_basis.py`, the discharge map, and the two power-supply plotting scripts. This is a relevance/dependency review of the existing records, not a new verification of every original document or a new literature search.

Keep all 15 Tier 1 sources, as requested. For lower-tier sources ask:

1. Does a recorded value support an efficiency range actually applied to a reactor projection?
2. Does it materially establish a useful efficiency, power or frequency extent in the figures?
3. Does it add distinct evidence on cost, maintenance, coupling or reactor compatibility that the study needs?

The third question prevents useful evidence being discarded simply because it is not an efficiency or power maximum. Do not select sources just because their efficiencies are high: lower measured efficiencies and evidence against optimistic scale-up remain important. A source's tier does not establish the boundary or applicability of every number it contains.

Recommendations distinguish dropping a numerical claim, dropping a separate class from the narrative, and excluding a source from the active study. Excluded material can remain in the public audit trail with the reason recorded; exclusion does not require erasing history.

## Summary recommendation

| Recommendation | PW sources | Meaning |
|---|---:|---|
| Retain Tier 1 | 15 | Retain every Tier 1 source. Select appropriate values for each figure; retention does not require putting every number in the main manuscript. |
| Retain as core lower-tier evidence | 18 | Needed for projection assumptions, meaningful scale limits, or distinct cost/coupling evidence. |
| Reserve/context | 12 | Keep accessible in the evidence base or a short SI discussion; usually omit a separate narrative entry or repeated plotted point. Some support older alternative scenarios. |
| Candidate for exclusion from the active study | 15 | Weak, superseded, out of scope, or redundant for the present questions. Two have dependencies that must be resolved before exclusion. |
| Already excluded | 1 | PW049 is already marked dropped. |

This produces a core of 33 PW sources, with 12 optional supporting sources. These are proposed editorial categories, not changes to the existing quality tiers or verification statuses.

## Which supply systems are actually needed?

| Class | Main reforming/CO2 synthesis | Other use now | Recommendation |
|---|---|---|---|
| J1 | Joule-heated and SOEC comparator projections | Low-voltage rectifier benchmark | Keep. |
| A1 | Thermal arc reforming | Torch power and maintenance context | Keep. |
| D1 | DC glow and DC gliding-arc projections | Measured laboratory arc-supply contrast | Keep. |
| K1 | DBD and AC gliding-arc projections | Ozone analogue and cost evidence | Keep. |
| K2 | Song ICP projection uses the 400 kHz sub-band, 0.91-0.96 | Broad K2 range, 0.91-0.98, used for the supply overview | Keep; distinguish the sub-band from the broad family range. |
| M1 | 915 MHz microwave projections | Industrial microwave power and tube replacement | Keep. |
| M2 | 2.45 GHz microwave projections | Magnetron alternative to a laboratory solid-state source | Keep. |
| P1 | Yong pulsed CO2 projections | Pulsed-power cost and load-matching evidence | Keep. Absence from a carrier-frequency plot is not a reason to drop it. |
| R1 | Not a selected main synthesis row; mentioned as an ICP sensitivity | Alternative Song case in `scaleup_wall_basis.py` | Retain as a short alternative/sensitivity, supported by retained Tier 1 PW007. No need for an equally long main class discussion. |
| R2 | Not a selected main synthesis row | Alternative Song case in `scaleup_wall_basis.py` | Candidate to drop as a projected industrial option: vendor RF evidence is at different operating frequencies, and the scenario does not establish a matching 400 kHz supply. Keep Tier 1 RF examples as context. |
| M3 | Not a selected main synthesis row | Alternative Kelly case in `scaleup_wall_basis.py`; Kelly used a solid-state laboratory source | Keep a brief explanation of the actual laboratory technology; candidate to drop the wall-efficiency projection because the recorded class range is amplifier/head efficiency, not mains efficiency. |
| H1 | No reactor projection | High-frequency/high-power context | Drop gyrotron and pulsed-accelerator excursions from the main narrative. Retain Tier 1 klystron/radar records in supporting material, as requested. One concise klystron counterexample can prevent implying an absolute GHz unit-power ceiling. |
| J2 | No supply-efficiency correction | Complete eREACT system claim printed by the older calculation utility | Drop as a power-supply class. Any retained system claim belongs with the reforming comparator and must keep its different product/boundary basis. |
| X1 | No reactor projection | Monolith plant-scale energy-use context | Drop as a power-supply class. An industrial-plasma example can remain in the manuscript introduction independently. |

## Exclusion candidates with little consequence for the present projections

| Sources | Proposed exclusion | Consequence |
|---|---|---|
| PW010 | Unretrieved 85% efficiency claim and duplicated 10 kW GMP100 rating | The unverified 85% point currently appears in the raw efficiency plot. It is not used in M2's adopted range. PW050 supplies the stronger model-specific evidence. |
| PW013 | Canon web listing, superseded by PW014 | No extracted values; no numerical consequence. |
| PW016 | Pulsed 12 GHz accelerator klystrons | Removes contextual 18-20 kW and 40% device points, not a process projection or the highest CW unit power. |
| PW011 | 170 GHz fusion gyrotron | Removes the extreme-frequency 1 MW/50.6% context points. No projection changes. Tier 1 PW014 still documents MW-class high-frequency tube power; do not describe the retained map as covering all possible GHz technologies. |
| PW030 | Generic 100 EUR/kW plasma-supply remark | Removes an unsupported, scope-undefined low-cost point, not a price for a specified supply. |
| PW032 | Electrolyser CAPEX category context | No quantitative supply performance; stronger rectifier cost evidence is retained in PW022. |
| PW036 | Monolith annual electricity converted to average plant power | No projection or supply-figure dependency. This is plant consumption rather than a supply unit rating. |
| PW037 | Complete eREACT electricity-per-H2 claim | Removes J2 as a supply class, not the literature-based Joule comparator. No main synthesis supply-efficiency dependency. |
| PW041, PW043 | Ozone production capacities | No electrical supply power or efficiency; neither sets the present electrical class map. |
| PW042 | Architecture-only ozone brochure | No numeric records; architecture can be explained from retained sources. |
| PW052 | Unretrieved Spellman lead | No extracted values. D1 already has PW054, PW053 and PW051. |
| PW060 | Low-pressure Baylor ICP facility description | Adds a 15 kW/13.56 MHz point and diameter to the ICP figure but no efficiency, projection, maximum-power or otherwise indispensable point. Other retained torch examples remain. |
| PW049 | Used-equipment listing | Already dropped; preserve that status rather than treating it as an active source. |

## Exclusion candidates that require resolving an efficiency dependency

### PW045: recommend excluding the numerical claims

This unsourced Tier 3 knowledge-base page supports several class descriptions. Most of its M2 power/efficiency claims are superseded by model-specific evidence. More importantly, PW045-V04 is used to support M1's current upper limit: 0.95 supply-stage efficiency multiplied by 0.88 gives about 0.84.

The original quote calls the 88% number **generator efficiency**, while the extraction notes reinterpret it as a tube value. That ambiguity makes it unsuitable for setting the upper end of a stage-product estimate. It is a prominent, favourable efficiency point in the raw figure, but prominence is a reason to scrutinise it, not to retain it automatically.

Do not simply remove the citation while preserving its numerical contribution. Rebuild and justify the M1 range first. For illustration only, using 0.86 instead of 0.88 with the same assumed 0.95 supply stage gives 0.817, about 82%; this is not a validated replacement upper bound. Retained sources PW009, PW012, PW017 and PW050 still support the technology and a generator efficiency around 80%.

### PW031: recommend excluding the numerical claims

This is another unsourced Tier 3 page from the same site. Its 65-75% tube range contributes to the explanatory M2 stage-product method. Its solid-state comparison and lifetime claims overlap other sources and do not justify a separate narrative.

Excluding it need not automatically change the adopted 0.63-0.72 M2 scenario, which also cites Tier 1 PW050 and Kiefer (SRC016), but the range's explanation must be rewritten and its endpoints/boundaries rechecked. The class CSV itself says the simple stage-product calculation gives approximately 0.59-0.71, rather than directly producing 0.63-0.72. The Kiefer upper-end measurement includes delivery to the absorbed-power boundary. Those qualifications remain regardless of whether PW031 is excluded.

## Lower-tier evidence that should not be removed merely to simplify the narrative

- **PW021:** the 98.5% rectifier claim is the present numerical basis for J1 and the A1 upper-end judgement. It is Tier 2 and its boundary is not fully stated, but removing it without replacement would undermine two selected projection ranges.
- **PW023:** the 90% requirement anchors A1. Keep it labelled as a tender requirement, not demonstrated performance.
- **PW051 and PW053:** establish industrial high-voltage DC performance and scale beyond the Tier 1 rack supply. Keep the distinction between ESP operation and arcs, and the measured 77-83% arc-load evidence in SRC020.
- **PW039:** the approximately 452 kW ozone example is the main industrial K1 power anchor. It describes a multi-tube ozone system in patent background; it is not proof of one chemical plasma reactor at that power.
- **PW001 and PW002:** important large-scale K2 evidence. PW001's 16 MW Twin-Power installation is not a single semiconductor module. PW002's 4.5 MW and 600 kHz are family maxima, explicitly not stated to occur together. Keep these sources while improving the figure's scale labelling.
- **PW003:** the approximately 98% claim helps define the broad K2 efficiency envelope but does not set the 400 kHz projection, whose upper end is 96%. Keep as qualified broad-frequency context, not a measured 400 kHz result.
- **PW028:** needed to understand the low end of P1's broad range, but 45-85% concerns source-to-reactor energy transfer, not independently demonstrated mains-to-plasma efficiency. Retain the source and correct the interpretation before treating the endpoints as interchangeable with supply-conversion efficiency. Its register says full text was obtained, so reassess the source-tier description if appropriate.
- **PW056 and PW058:** respectively a large actual ICP facility and the design/technology argument connecting larger torches to lower frequencies. Keep the 1.2 MW figure as a generator rating at a low-pressure facility, and the patent statements as qualified design/background claims rather than universal limits.
- **PW048:** useful beyond its old cost estimate: it reports approximately 95% coupling in a particular 2.45 GHz torch. This directly addresses the delivery-stage gap. It is one operating configuration, not a generic correction for all microwave reactors.
- **PW033, PW046 and the PS/RV literature:** retain the distinct cost, lifetime and modelling evidence. The tiers of the full-text sources and the types of individual claims deserve separate consideration; a peer-reviewed comparison table is not automatically a measured commercial quotation.

## Full PW source inventory

Projection column: **Main** = supports a selected class efficiency (including an assumption behind a bound); **Alternative** = supports a range used only in the older alternative calculation utility; **No** = no direct efficiency-range dependency found. A source can still be important for scale, coupling, cost or lifetime.

| ID | Tier | Projection role | Figure or other distinct relevance | Recommendation |
|---|---:|---|---|---|
| PW001 | 2 | No | K2 16 MW installed-supply point; larger installations without frequency data | Core; separate installed system from module. |
| PW002 | 2 | No | K2 multi-MW family scale and 600 kHz family extent | Core; do not combine independent maxima into a guaranteed operating point. |
| PW003 | 2 | No (broad K2 only) | Approx. 98% high-efficiency claim; 75-750 kW family | Core, with unstated efficiency boundary identified. |
| PW004 | 1 | Main: K1 and K2 sub-band | Named industrial inverter, 91%, output and electrical ratings | Retain Tier 1. |
| PW005 | 1 | Main: K2 sub-band | Greater than 96% claim at 100-400 kHz; input rating | Retain Tier 1; distinguish input from output power. |
| PW006 | 2 | No | Explicit 50 kW output at 100-400 kHz complements PW005's input rating | Core supporting scale evidence; no separate long entry needed. |
| PW007 | 1 | Alternative: R1 | 100 kW RF tube generator; indicative efficiency from ratings | Retain Tier 1. |
| PW008 | 2 | Alternative: R2 | Named commercial 5 kW RF generator; greater than 70%, boundary unstated | Reserve; only needed for short RF context if alternative projection is dropped. |
| PW009 | 2 | Main: M1 | 100 kW generator, approaching 80%, tube-loss estimate | Core. |
| PW010 | 2 | No adopted range | Unverified 85% M2 point; duplicate 10 kW rating | Drop candidate; superseded by PW050. |
| PW011 | 2 | No | Extreme-frequency fusion gyrotron, 1 MW at 170 GHz | Drop candidate from active process-supply comparison. |
| PW012 | 2 | Main: M1 | Greater than 80% generator efficiency, 100 kW units, multi-unit containers | Core. |
| PW013 | 2 | No | No extracted values; superseded by catalogue | Drop candidate. |
| PW014 | 1 | No | 0.6-1.2 MW CW klystrons; device efficiency | Retain Tier 1; concise context or appendix. |
| PW015 | 1 | No | Radar peak/average distinction; 2 kW average, not 1 MW continuous | Retain Tier 1; supporting context rather than main industrial envelope. |
| PW016 | 2 | No | 12 GHz pulsed accelerator klystrons; not a new CW maximum | Drop candidate. |
| PW017 | 1 | Main: M1 | 100 kW tube; approaching 86% device efficiency | Retain Tier 1. |
| PW018 | 2 | Alternative: M3 | Measured 6 kW solid-state microwave source, 56% head/amplifier | Reserve; useful upper unit-power context for actual laboratory technology. |
| PW019 | 2 | Alternative: M3 | 1 kW GaN head at 70%; lower magnetron comparison of uncertain boundary | Reserve; do not use the different boundaries as directly comparable efficiencies. |
| PW020 | 2 | Main: M1 corroboration | Undated tube/transmitter/klystron costs; 84% tube statement | Reserve; omit redundant undated prices from a concise quantitative cost figure. |
| PW021 | 2 | Main: J1 and A1 | 98.5% rectifier claim, currently important to both upper bounds | Core until a stronger replacement exists. |
| PW022 | 1 | No direct numeric efficiency bound | Rectifier cost benchmark, 3 MW design case and lifetime context | Retain Tier 1. |
| PW023 | 2 | Main: A1 | 100 kW torch-supply requirement, at least 90% efficiency | Core; requirement rather than measured performance. |
| PW024 | 2 | Alternative: R1 | Tube-oscillator efficiency and historical solid-state frequency context | Reserve; brief R1 sensitivity only. |
| PW025 | 2 | Alternative: R2 | Up to 80% RF efficiency claim, boundary unstated | Reserve; not needed for selected main projections. |
| PW026 | 1 | Main: K1 | Measured 91%, 70% and 69% DBD-load designs | Retain Tier 1, including less-efficient designs. |
| PW027 | 1 | No | 91.5% MHz amplifier at 600 W; important boundary-qualified counterexample | Retain Tier 1. |
| PW028 | 2 | Main: P1 | Load-dependent 45-85% energy transfer | Core; review boundary interpretation and possible tier reassessment. |
| PW029 | 1 | Main: P1 | Pulsed supply efficiency and dated cost estimates | Retain Tier 1. |
| PW030 | 2 | No | Unspecified 100 EUR/kW remark | Drop candidate from quantitative cost evidence. |
| PW031 | 3 | Main: M2 supporting derivation; Alternative: M3 context | Unsourced tube efficiency, cost ratio and lifetime statements | Drop candidate after M2 range explanation is rebuilt. |
| PW032 | 2 | No | Electrolyser CAPEX grouping; no useful numeric supply value | Drop candidate. |
| PW033 | 2 | No | Dated 100 kW magnetron tube cost and lifetime evidence | Core for maintenance and cost, not generator-price comparison. |
| PW034 | 2 | No | Thermal torch family to 500 kW and electrode lifetime | Core for A1 scale and maintenance; thermal efficiency is downstream. |
| PW035 | 2 | No | 60/200 kW torch examples and downstream thermal efficiency | Reserve; redundant for supply maximum, useful reactor context only. |
| PW036 | 3 | No | Annual plant electricity and inferred average consumption | Drop candidate from supply study; introduction context is separate. |
| PW037 | 2 | No | Complete eREACT system electricity claim | Drop candidate as a separate supply class (J2). |
| PW038 | 2 | No | Qualitative ballast-inductor cost issue | Reserve; short engineering context, no quantitative price point. |
| PW039 | 2 | No | Approx. 452 kW multi-tube ozone example and reactive-load requirement | Core industrial K1 scale anchor. |
| PW040 | 2 | No | Older reactive-load power-factor range | Reserve; can omit separate discussion if PW039 suffices. |
| PW041 | 2 | No | Ozone production capacity without electrical supply data | Drop candidate. |
| PW042 | 2 | No | Architecture-only brochure; no numerical rows | Drop candidate. |
| PW043 | 2 | No | Ozone production capacity without electrical supply data | Drop candidate. |
| PW044 | 1 | No | 15 kW 2.45 GHz magnetron-head scale | Retain Tier 1. |
| PW045 | 3 | Main: M1 upper bound and M2 corroboration; Alternative: M3 | Unsourced 88% claim helps set M1's favourable upper end | Drop candidate after M1 bound is rebuilt; most other claims redundant. |
| PW046 | 2 | Main: M2 corroboration; Alternative: M3 | Full-text microwave comparison, costs/lifetimes, measured GaN example | Core qualified comparison; possible tier reassessment for direct full-text measurements. |
| PW047 | 2 | No | Qualitative patent statement against assumed magnetron economies of scale | Reserve; useful caveat, not observed commercial price data. |
| PW048 | 2 | No supply-efficiency bound | Measured torch coupling; dated industrial analogue cost and projected plasma cost | Core for coupling; keep cost scopes distinct. |
| PW049 | 3 | No | No values; unverifiable used-equipment listing | Already dropped. |
| PW050 | 1 | Main: M1 supply-stage assumption and M2 | Named generator, supply-stage efficiency, input/output ratings, lifetime | Retain Tier 1; rating-based estimates remain conditional. |
| PW051 | 2 | Main: D1 | Greater than 95/97% claims and largest documented HV DC ratings | Core industrial analogue; ESP load qualification essential. |
| PW052 | 2 | No | Unretrieved lead, no extracted values | Drop candidate from active retrieval priorities. |
| PW053 | 2 | Main: D1 | Intermediate industrial efficiency from output and stated losses | Core; retain note about inconsistent input-kVA entry. |
| PW054 | 1 | Main: D1 | Greater than 92% named rack units and electrical ratings | Retain Tier 1. |
| PW055 | 1 | No selected main range | Skin-depth/coupling basis and historical ICP examples | Retain Tier 1. |
| PW056 | 2 | No | 1.2 MW, 400 kHz ICP facility; low-pressure operation | Core large actual plasma-facility example; generator rating, not chemical-process demonstration. |
| PW057 | 2 | No | 50 kW, 6 MHz ICP facility and diameter | Reserve; optional intermediate example in ICP-only SI figure. |
| PW058 | 2 | No direct endpoint (K2/R1/R2 contextual support) | Size/frequency argument and claimed efficient solid-state power domains | Core, explicitly patent background rather than an absolute technological envelope. |
| PW059 | 1 | No | Named 27.12 MHz analytical ICP generator | Retain Tier 1. |
| PW060 | 3 | No | 15 kW low-pressure ICP facility; not a needed limit | Drop candidate from the active ICP figure/discussion. |
| PW061 | 2 | No selected main range | Direct industrial ICP tube-generator application to 120 kW | Reserve; useful in ICP SI, but small incremental scale over Tier 1 PW007. |

## Other literature sources represented in the value table

These six sources do not have PW source-register tier assignments; do not silently assign them one for this review.

| Source | Relevance and recommendation |
|---|---|
| SRC009 | Keep. Actual 400 kHz chemical ICP reactor anchors the application of K2 and the size/frequency comparison. |
| SRC016 | Keep. Kiefer's measured electrical consumption anchors the M2 upper-end scenario and the distinction between generator and absorbed boundaries. |
| SRC020 | Keep. Actual 77-83% arc-load efficiency, laboratory cost and explicitly projected improvement are essential checks on industrial analogue assumptions. Separate measured/estimated/target values. |
| PS003 | Keep. Directly relevant DBD supply-cost estimate, dominant supply cost share and explicit 12 x 12 kW installation. |
| RV005 | Keep. Industrial/prototype gliding-arc cost estimates and manufacturer-suggested scaling; remove duplicate DBD price points from figures rather than dropping the source. |
| PS004 | Keep as cost-modelling evidence, not observed commercial pricing. It explains why the apparent cost-versus-scale trend cannot establish an empirical scaling law; place model curves separately if retained. |

## Suggested presentation after approval

1. Give the eight main projection classes full treatment in SI_1. Combine R1/R2/M3 into a short context/sensitivity section; remove J2/X1 as supply classes and avoid a separate gyrotron narrative.
2. Keep all Tier 1 sources in the study, but restrict the main overview to relevant continuous industrial evidence. Retain radar, amplifier-only and analytical-laboratory examples in clearly separate supporting material where needed.
3. Remove the unverified 85% M2 point and the ambiguous 88% M1 point from the main evidence figure only after recording the exclusions and resolving range dependencies. Do not selectively retain only the most efficient points.
4. Separate commercial output, multi-unit installed power and family maxima visually. Removing weak sources alone will not fix a figure that labels installed-system power as unit power.
5. Keep actual costs, historical estimates and assumed model curves distinct. De-duplicate prices propagated between PS003, PS004 and RV005.
6. Rebuild the selected efficiency ranges and all dependent projections/figures only after source decisions are agreed. Update the older discharge map and calculation utility as well as the main synthesis so excluded alternatives do not remain as apparently equivalent projections.

The clearest simplification is editorial: fewer fully developed classes and fewer redundant points. It should not hide the lower efficiencies, uncertain delivery boundaries, or industrial-analogue assumptions that materially affect the conclusions.
