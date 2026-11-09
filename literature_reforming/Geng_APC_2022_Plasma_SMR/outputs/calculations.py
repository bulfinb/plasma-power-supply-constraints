"""Reviewer calculations SRC002-C003 to C005 for Geng et al. (2022).

Inputs are taken from the manuscript and labelled with evidence IDs in evidence.csv.
Run with: python3 calculations.py
"""

# SRC002-C003: methane feed from the liquid water feed.
WATER_ML_MIN = 0.08       # mL/min liquid water at S/C 4.4, E021-E022
WATER_DENSITY = 0.997     # g/mL, assumed
M_H2O = 18.015            # g/mol
S_TO_C = 4.4              # E022
F_H2O = WATER_ML_MIN * WATER_DENSITY / M_H2O   # mol/min
F_CH4_IN = F_H2O / S_TO_C                      # mol/min
print("C003 F_H2O = %.4e mol/min; F_CH4,in = %.4e mol/min = %.4e mol/s"
      % (F_H2O, F_CH4_IN, F_CH4_IN / 60))
print("     equivalent to %.1f mL/min at 0 degC, %.1f mL/min at 25 degC (1 atm)"
      % (F_CH4_IN * 22414, F_CH4_IN * 24465))

# SRC002-C004: power-basis SEI_CH4 and EC_CH4 (discharge power only; furnace heat excluded).
EV_PER_MOLECULE = 96.485  # kJ/mol
P_DISCHARGE = 15.0        # W, E035, E047
f_ch4_mol_s = F_CH4_IN / 60
sei = P_DISCHARGE / f_ch4_mol_s / 1000
print("C004 SEI_CH4 = %.0f kJ/mol CH4 fed (%.1f eV/molecule)" % (sei, sei / EV_PER_MOLECULE))
for point, conversion in [("OP002, 300 degC", 0.60), ("OP008, 440 degC", 0.80)]:  # E036, E048
    ec = P_DISCHARGE / (f_ch4_mol_s * conversion) / 1000
    print("     %s: EC_CH4 = %.0f kJ/mol (%.1f eV/molecule)" % (point, ec, ec / EV_PER_MOLECULE))

# SRC002-C005: power-basis EC_H2 and EY_H2. Flow reference not stated: 0 and 25 degC bounds.
M_H2 = 2.016  # g/mol
for point, h2_ml_min in [("OP002, 300 degC", 45), ("OP008, 440 degC", 60)]:  # E058
    results = []
    for molar_volume in (22.414, 24.465):  # L/mol at 0 and 25 degC, 1 atm
        f_h2 = h2_ml_min / 1000 / molar_volume / 60          # mol/s
        ec_h2 = P_DISCHARGE / f_h2 / 1000                     # kJ/mol H2
        ey_h2 = f_h2 * M_H2 * 3600 / (P_DISCHARGE / 1000)     # g H2/kWh
        results.append((ec_h2, ey_h2))
    print("C005 %s: EC_H2 = %.0f-%.0f kJ/mol; EY_H2 = %.1f-%.1f g/kWh"
          % (point, results[0][0], results[1][0], results[1][1], results[0][1]))
