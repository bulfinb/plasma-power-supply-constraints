# Reforming synthesis tables

Built by build_synthesis.py from the short summaries (literature_reforming/*/short_summary.txt), including the
corrections from the GPT cross-check (../cross_check_log.md). Headline rows first within each source; supporting
rows in reforming_synthesis.csv. NR = not reported; NA = not applicable; ~ = approximate.

SEI_CH4 = kJ per mol CH4 fed; EC_CH4 = kJ per mol CH4 converted, both at each paper's power boundary (external heat
excluded). EC ind. = EC_CH4 with a representative industrial supply = EC_CH4 / class efficiency
(power_systems/results/supply_classes.csv) [1]. Reaction enthalpies at 298 K: SMR 206, DRM 247 kJ/mol CH4.
Conf. = confidence in conversion / energy results from the extraction (H higher, M moderate, L lower).

## 1. Steam methane reforming (SMR)

Source / OP          | Activation               | Class | CH4 (mol/min) | CH4:CO2:H2O | P (kW) | Boundary    | X_CH4 (%) | X_CO2 (%) | SEI_CH4 | EC_CH4 | EC ind.   | Duration       | Conf.
Wismann 2019 OP004   | Joule (lab)              | J1    | 0.0046        | 1:0:2 +H2   | NR     | NR          | 92.7      | NA        | -       | NR     | -         | >=0.75 h avg.  | M/L
Hrabovsky 2018 OP001 | DC arc torch             | A1    | 6.69          | 1:0:0.78    | 120    | arc         | 91.3      | NA        | 1076    | 1179   | 1203-1310 | ~4 min segment | M/M
Akande 2022 OP008    | MW 915 MHz torch         | M1    | 2.77          | 1:0:2.9     | 32     | absorbed MW | 83.1      | NA        | 694     | 835    | 1018-1128 | NR             | L/L
Hrycak 2023 OP002    | MW 915 MHz               | M1    | 2.06          | 1:0:1.35    | 6.5    | absorbed MW | 66.1      | NA        | 189     | 286    | 349-386   | NR             | M/L
Zhu 2019 OP004       | DC gliding arc + Ni cat. | D1    | 0.033         | 1:0:3       | 0.246  | discharge   | 90        | NA        | 441     | 490    | 505-533   | 6 h            | H/M
Geng 2022 OP002      | DBD + Ni cat.            | K1    | 0.001         | 1:0:4.4     | 0.015  | discharge   | ~60       | NA        | 894     | 1490   | 1620-1656 | ~2 h series    | M/L

## 2. Dry reforming (DRM)

Source / OP         | Activation              | Class | CH4 (mol/min) | CH4:CO2:H2O     | P (kW) | Boundary     | X_CH4 (%) | X_CO2 (%) | SEI_CH4 | EC_CH4 | EC ind.   | Duration    | Conf.
Song 2020 OP013     | RF ICP torch 400 kHz    | K2    | 1.61          | 1:0.83:0        | 22     | RF generator | 79.3      | 87.1      | 822     | 1036   | 1079-1138 | NR          | M/M
Kelly 2023 OP004    | MW 2.45 GHz             | M2    | 0.187         | 1:1.22:0        | 1      | absorbed MW  | 55.2      | 45.8      | 321     | 581    | 807-922   | ~0.25 h     | H/H
Kwon 2023 OP003     | AC rotating GA + quench | K1    | 0.268         | 1:1:0 (+50% N2) | 1.668  | discharge    | 50.5      | 40.3      | 374     | 740    | 804-822   | ~0.2 h      | H/H
Wanten 2022 OP006   | DC confined glow        | D1    | 0.015         | 1:1.86:0        | 0.145  | plasma       | ~73.5     | ~54.8     | 598     | 813    | 838-884   | NR          | H/M
Kaufmann 2026 OP002 | DC rotating glow        | D1    | 0.134         | 1:1:0           | 1.43   | plasma       | ~66       | ~70       | 641     | 971    | 1001-1055 | 2-5 min run | M/M
Andersen 2020 OP001 | DBD (no packing)        | K1    | 0.001         | 1:1:0           | 0.045  | discharge    | 32.6      | 22.4      | 2642    | 8103   | 8808-9003 | 1 h         | M/H

## 3. Mixed reforming (CO2 + steam, biogas)

Source / OP           | Activation         | Class | CH4 (mol/min) | CH4:CO2:H2O           | P (kW) | Boundary    | X_CH4 (%)         | X_CO2 (%) | SEI_CH4 | EC_CH4  | EC ind.   | Duration       | Conf.
Hrabovsky 2018 OP005  | DC arc torch       | A1    | 5.58          | 1:0.81:0.18           | 116    | arc         | 95.3              | 91.0      | 1248    | 1309    | 1336-1454 | ~2 min segment | M/M
Hrycak 2023 OP001     | MW 915 MHz         | M1    | 3.09          | 1:0.33:0.90           | 6.5    | absorbed MW | 48.9              | ~44       | 126     | 258     | 315-349   | NR             | M/L
From 2024 OP001       | Joule (eSMR pilot) | J1    | NR            | biogas; S/C 2.7       | NR     | NR          | 97                | NR        | -       | NR      | -         | ~1 h steady    | M/NA
From 2024 OP004-OP007 | Joule (eSMR pilot) | J1    | NR            | biogas; S/C 2-2.2     | NR     | Q_in (PSU)  | 94-97 (eq., est.) | NR        | -       | 388-485 | 394-500   | NR             | L/L
From 2025 OP002       | Joule (eSMR pilot) | J1    | 2.55          | biogas + H2; S/HC 2.3 | NR     | NR          | ~98               | ~42-54    | -       | NR      | -         | 80 h           | M/NA

## 4. Benchmarks

Fired SMR references: design studies, heat basis (kJ per mol CH4 converted in the reformer); not electrical. EC_CH4,abs = heat absorbed by the reformer tubes; EC_CH4,fired = burner fuel (HHV).

Source / OP                 | Scale                                | T (degC), p          | X_CH4 (%)                      | EC_CH4,abs | EC_CH4,fired (HHV) | eta_HHV (%)           | f_electric
Lewis (NETL) 2022 OP001     | 20,126 kg/h H2 (CH4 ~59,970 mol/min) | 871 outlet, 28.3 bar | 77.7 (reformer)                | 340        | 577                | 75.7 (plant, H2 only) | 1.2% (grid aux.)
Collodi (IEAGHG) 2017 OP001 | 8,994 kg/h H2 (CH4 ~21,600 mol/min)  | ~900-950 outlet      | 84.6 (pre-reformer + reformer) | 315        | 574                | 81.1 (plant, H2 only) | 0 (9.9 MWe export)

- Lewis (NETL) 2022 OP001: steam export ~143 MW not credited; author ETE 75.4% HHV.
- Collodi (IEAGHG) 2017 OP001: 83.4% including exported power.

Joule-heated benchmarks:

- **From 2024 OP004 / OP007:** author reactor efficiency ~72% at ~25 kW and ~80% at ~35 kW (Fig. 5; includes sensible heating 400 -> 900 degC; I x V boundary). Reviewer estimate EC_CH4 388-485 kJ/mol at Q_in from equilibrium Q_reaction / efficiency (SRC005-C004, E043-E045); not measured.
- **Topsoe eREACT (vendor claim):** ~1 kWh/Nm3 H2 system electricity (~81 kJ/mol H2); boundary not stated (PW037-V01).

## 5. Not plotted

- **Wismann 2019 (all OPs):** no point-matched electrical power.
- **From 2024 OP001, OP003; From 2025 (all):** no point-matched power and feed (From 2025 power confidential).
- **Geng 2022 OP001:** plasma off (furnace only); ~7% conversion.
- **Andersen 2020 OP006:** plasma off; ~1.5% conversion.
- **Akande 2022 H2 rate / energy yield:** exceeds the stoichiometric limit for the stated feed (not usable).

## Notes

[1] Class efficiencies: J1 0.97-0.98, A1 0.90-0.98, D1 0.92-0.97, K1 0.90-0.92, M1 0.74-0.82, M2 0.63-0.72, K2@400kHz 0.91-0.96. RF ICP (Song) uses a K2 scenario at 400 kHz: 0.91 is extrapolated from a 1-200 kHz family (PW004-V02); >0.96 is a claim at 100-400 kHz (PW005-V02). CEIA's 100 kW is an input rating; PW006 documents 50 kW output. A tube oscillator (R1, 0.53-0.60) would give ~1.6-1.8x higher values. Wanten and Zhu exclude their lab ballast resistors; the estimate replaces the ballasted lab supply with a D1 current-controlled supply. Kaufmann already uses a current-controlled driver (88-94% of the DC supply output reaches the plasma).
[2] External heat is excluded from every EC_CH4: furnace (Geng), steam generation (Akande, Hrycak, Zhu, the From pilots) and feed preheat are not reported. These EC_CH4 are lower bounds on electricity per mol CH4; Hrabovsky's torch evaporates its own water, so arc power is its whole process heat.
[3] Hrabovsky conversions are reviewer calculations from the Ar tracer; they match the authors' plotted points (cross-check XR007, for human check). Hrycak uses 24.25 L/mol (XR008).
[4] Akande's reported H2 rate is impossible for the stated feed, and its reported 96.6% conversion conflicts with the corrigendum composition; the headline uses the carbon-based 83.1% from that composition (OP008, 62 lpm, 32 kW; no soot assumed), lower confidence.
[5] Kwon feeds 50% N2; Hrycak and Akande add steam from a separate vaporizer. Unit scale: Hrabovsky ~90-120 kW, Akande 17-47 kW, Song 22-27 kW, Hrycak 4.5-6.5 kW, Kwon ~1.7 kW, Kaufmann 0.5-1.4 kW, Kelly 1 kW; Zhu, Wanten, Geng and Andersen are 15-250 W lab reactors.

## 6. Reading the tables (reviewer summary, for the narrative)

- Fired SMR needs 315-340 kJ of absorbed heat and ~575 kJ of fuel (HHV) per mol CH4 converted in the reformer
  (design studies); whole-plant H2 efficiency 76-81% HHV.
- With an industrial supply, the kW-scale plasma headline points cost (kJ electricity per mol CH4 converted):
  Hrycak ~310-390 (6.5 kW; steam generation excluded, ~25% carbon gap), Akande ~1020-1130 (32 kW, 83% from the corrigendum composition; lower confidence,
  impossible H2 rate), Song ~1080-1140 (22 kW) and Hrabovsky ~1200-1310 (120 kW, the only process-complete
  figure: the torch raises its own steam). Against fired SMR this is ~1-4x the absorbed heat and ~0.5-2.3x the
  fuel energy, but electricity against heat. Conversion 66-97% at these points; 94-99% costs ~1300-2400.
- Lab-scale points (paper boundary): Zhu 490 (Ni catalyst, steam excluded), Kaufmann 971 (1.4 kW; 574 at 0.5 kW and 42%), Kelly 581,
  Kwon 740, Wanten 813, Geng 1120-1490
  (furnace excluded), Andersen ~8100 kJ/mol (DBD).
- Joule heating converts at equilibrium (85-98%) and runs for 80-1535 h, but no paper gives power and feed at
  the same operating point. A reviewer estimate from the From 2024 pilot efficiencies (72-80%, ~23-35 kW) gives
  EC_CH4 ~390-485 kJ/mol at the supply output (SRC005-C004), below the kW-scale plasma torches.
- Durations: plasma results are minutes to hours (longest 6 h, Zhu); Joule pilots run for weeks.
