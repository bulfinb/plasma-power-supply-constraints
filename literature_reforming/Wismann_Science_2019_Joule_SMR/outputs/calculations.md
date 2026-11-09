# Calculations and unavailable harmonized metrics

Source: SRC001. Protocol 0.1. Reviewer: Codex AI; same extractor, not independent human review. Date: 2026-10-28.
All results are AI-checked; none is human verified. IDs below reference evidence.csv.

## SRC001-C001 - Coated-zone gas-channel volume using selected 5.3 mm ID

Inputs: SRC001-E023 (5.2 mm bare ID), SRC001-E025 (5.3 mm alternate ID), SRC001-E022, SRC001-E024 (Fig. 2 geometry consistent with alternate ID), SRC001-E026 (280 mm coated length), SRC001-E027 (0.128 mm radial coat).

Formula: V_gas = pi/4 * (D_bare - 2*delta)^2 * L. Divide mm3 by 1000 to obtain mL.

- D_bare = 5.3 mm: V_gas = 5.594974 mL.

Decision: the user instructed "Just take 5.3 mm" on 2026-10-28. Use 5.3 mm as the bare tube ID, consistent with Fig. 2 wall geometry and supplementary p. 9. Preserve the preparation-section value of 5.2 mm as source evidence but do not use it in calculations.

Assumptions: uniform cylindrical channel and uniform radial coat. Excludes pore gas and the residual catalytically active outlet layer. This is a derived nominal volume, not a measured volume, complete active volume, or equipment volume. No dimensional uncertainty is reported. This user decision is not a human verification of all extracted evidence.

## SRC001-C002 - Conditional space time at the unspecified normal-flow reference

Inputs: SRC001-C001 and each operating point's total wet inlet flow evidence (linked in operating_points.csv). Formula: tau_N [s] = 60 * V_gas [mL] / F_N [Nml/min].

| Total inlet flow (Nml/min) | tau_N, selected 5.3 mm ID (s) |
|---|---:|
| 340 | 0.9873 |
| 1020 | 0.3291 |
| 1700 | 0.1975 |

These are nominal reference-flow space times, not reported author values and not actual hot residence times. Normal reference temperature/pressure is unspecified (SRC001-E045); gas expansion, reaction-induced mole changes, wall/gas temperature differences, and axial variations prevent conversion to an actual residence time from these data alone. Values are rounded for reporting; extra digits in CSV preserve the calculation, not measurement precision. No GHSV/WHSV is claimed.

## SRC001-C003 - HHV efficiency and electricity fraction: not calculable

eta_HHV = HHV_product_rate / D; f_electric = P_electric / D.
D = P_electric + HHV_external_feed_and_fuel_rate + Q_external,in.

Missing inputs: numerical point-matched power (SRC001-E014, SRC001-E015), external steam/preheat duty (SRC001-E049), complete product flows (SRC001-E122, SRC001-E124), and explicit normal-flow T/P (SRC001-E045). No numerical efficiency or electricity fraction is calculated. Heat flux in Fig. S5 cannot replace electrical input; ideal industrial insulation cannot be used as proof of complete measured energy closure.

The 10 mol% inlet H2 (SRC001-E038) is a combustible feed contribution and belongs in feed HHV as well as any gross outlet-H2 accounting. If a later metric uses net H2 production, specify it separately and avoid silently subtracting inlet H2 from only one side of an otherwise gross-stream balance. No external HHV property values were introduced in this pilot.

## SRC001-C004 - Laboratory steam-to-carbon ratio

Input: SRC001-E038. On the stated molar composition, S/C = 60/(30*1) = 2 mol steam/mol carbon. Methane is the only carbon-containing inlet component reported. This is reviewer-derived; industrial S/C = 1.8 is a different case.

## SRC001-C005 - Projected furnace/reformer volume ratio

Inputs: SRC001-E104 (1140 m3, Fig. 4) and SRC001-E106 (4.9 m3, Fig. 4 at 75.4% conversion). Ratio = 1140/4.9 = 232.65, approximately 230-fold.

This arithmetic uses printed figure values. Narrative values round to 1100 and approximately 5 m3. This is an industrial design/model comparison with furnace blowers/waste-heat equipment and electric wiring/power supply excluded. It is not a demonstrated full-plant size reduction. The abstract's potential 100-fold compactness statement is a broader rounded claim, not a separate measured benchmark. No uncertainty interval is supplied.

## SRC001-C006 - Methane feed for the experimental short summary

Inputs: SRC001-E038 (CH4 molar fraction 0.30) and the total normal feed flows in supplementary Figs. S2-S4 (SRC001-E050, SRC001-E062, SRC001-E077; each point also has its own flow record).

Formula: F_CH4,N = 0.30 * F_total,N, using the same unspecified normal-flow reference for both streams.

- 340 Nml/min total feed gives 102 Nml/min CH4; highest labelled conversion in Fig. S2 is 92.7% (SRC001-E060).
- 1020 Nml/min total feed gives 306 Nml/min CH4; highest labelled conversion in Fig. S3 is 91.6% (SRC001-E075).
- 1700 Nml/min total feed gives 510 Nml/min CH4; highest labelled conversion in Fig. S4 is 85.0% (SRC001-E084).

This is a volumetric split on the common normal reference, not a conversion to mol/s. No reference temperature or pressure is assumed. Results support short_summary.txt; no modelled industrial capacities are included there.
