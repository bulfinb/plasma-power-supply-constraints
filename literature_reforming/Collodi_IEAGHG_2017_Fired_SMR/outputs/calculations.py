"""Reviewer calculations SRC004-C001 to C006 for IEAGHG 2017-02, Base Case (SMR without CCS).

Inputs are taken from the report and labelled with evidence IDs in evidence.csv.
Run with: python3 calculations.py
"""

# SRC004-C001: standard 25 degC heats of combustion, kJ/mol (HHV, LHV).
# Same values as SRC003 (NETL); cite a specific property source in the report.
HHV = {"H2": 285.83, "CH4": 890.6, "C2H6": 1560.7, "C3H8": 2219.2, "C4H10": 2877.5,
       "C5H12": 3509.0, "CO": 282.98}
LHV = {"H2": 241.83, "CH4": 802.3, "C2H6": 1428.6, "C3H8": 2043.1, "C4H10": 2657.3,
       "C5H12": 3244.9, "CO": 282.98}
KCAL = 4.1868  # kJ/kcal (international table calorie)

# Heat and material balance, Base Case (PDF p. 44), streams 1, 3, 4, 5, 8, 12.
NG = {"CH4": 0.8900, "C2H6": 0.0700, "C3H8": 0.0100, "C4H10": 0.0010, "C5H12": 0.0001}  # E006
F_NG_TOTAL, M_NG_TOTAL = 1696.6, 30563        # stream 1, kmol/h and kg/h, E008
F_NG_FUEL, M_NG_FUEL = 240.4, 4332            # stream 3, E009
TAIL_GAS = {"CH4": 0.0945, "CO": 0.1454, "H2": 0.2369}  # stream 8, E010
F_TAIL_GAS = 2106.3
STREAM4 = {"CH4": 0.2350, "C2H6": 0.0185, "C3H8": 0.0026, "C4H10": 0.0003}  # pre-reformer feed, E011
F_STREAM4 = 5514.0
F_STREAM5, Y_CH4_STREAM5, Y_H2O_STREAM5 = 8370.3, 0.0238, 0.2927  # HTS inlet = reformer outlet gas, E012
CARBON_NUMBER = {"CH4": 1, "C2H6": 2, "C3H8": 3, "C4H10": 4}

# Stated values.
RADIANT_DUTY_MMKCAL_H = 82.63                 # steam reformer furnace radiant duty, E013
NG_LHV_REPORT, NG_HHV_REPORT = 46.502, 51.473 # MJ/kg, E007
H2_LHV_REPORT, H2_HHV_REPORT = 119.96, 141.88 # MJ/kg, E016
M_H2 = 8994                                   # kg/h, E014
F_H2_PRODUCT = 4461.5                         # kmol/h, stream 12, E014
P_EXPORT = 9.918                              # MWe to grid, E018
ENERGY_INPUT_LHV, ENERGY_PRODUCT_LHV = 394.77, 299.70  # MW, E015


def heating_value(composition, table):
    """Mixture heating value in kJ/mol of mixture."""
    return sum(y * table[species] for species, y in composition.items())


def duty_mw(composition, flow_kmol_h, table):
    """Chemical energy flow in MW for a stream."""
    return heating_value(composition, table) * flow_kmol_h / 3600


# SRC004-C001: validate heating values against the report's natural gas values.
ng_mw = M_NG_TOTAL / F_NG_TOTAL
print("C001 NG HHV %.3f MJ/kg (report %.3f); LHV %.3f MJ/kg (report %.3f)"
      % (heating_value(NG, HHV) / ng_mw, NG_HHV_REPORT, heating_value(NG, LHV) / ng_mw, NG_LHV_REPORT))
print("     Nm3 check: 100,000 Nm3/h / 22.414 = %.1f kmol/h (stream 12: %.1f)" % (100000 / 22.414, F_H2_PRODUCT))

# SRC004-C002: radiant (absorbed) duty.
q_abs = RADIANT_DUTY_MMKCAL_H * 1e6 * KCAL / 3.6e6  # MW
print("C002 Q_abs (radiant duty) = %.1f MW" % q_abs)

# SRC004-C003: conversion across pre-reformer + reformer (stream 4 to stream 5).
ch4_in = STREAM4["CH4"] * F_STREAM4
ch4_out = Y_CH4_STREAM5 * F_STREAM5
hc_carbon_in = sum(y * F_STREAM4 * CARBON_NUMBER[s] for s, y in STREAM4.items())
print("C003 CH4 in %.1f, out %.1f kmol/h; CH4 conversion %.1f%%"
      % (ch4_in, ch4_out, 100 * (ch4_in - ch4_out) / ch4_in))
print("     hydrocarbon carbon in %.1f kmol/h; conversion %.1f%%"
      % (hc_carbon_in, 100 * (hc_carbon_in - ch4_out) / hc_carbon_in))
print("     reformer outlet CH4 dry basis %.2f%%" % (100 * Y_CH4_STREAM5 / (1 - Y_H2O_STREAM5)))

# SRC004-C004: burner fuel duty (PSA tail gas + supplementary NG).
q_tail_lhv, q_tail_hhv = duty_mw(TAIL_GAS, F_TAIL_GAS, LHV), duty_mw(TAIL_GAS, F_TAIL_GAS, HHV)
q_ngf_lhv, q_ngf_hhv = M_NG_FUEL * NG_LHV_REPORT / 3600, M_NG_FUEL * NG_HHV_REPORT / 3600
q_fired_lhv, q_fired_hhv = q_tail_lhv + q_ngf_lhv, q_tail_hhv + q_ngf_hhv
print("C004 tail gas %.1f / %.1f MW, supplementary NG %.1f / %.1f MW (LHV / HHV)"
      % (q_tail_lhv, q_tail_hhv, q_ngf_lhv, q_ngf_hhv))
print("     Q_fired = %.1f MW LHV, %.1f MW HHV" % (q_fired_lhv, q_fired_hhv))

# SRC004-C005: heat-basis energy cost and radiant efficiency.
ch4_conv_mol_s = (ch4_in - ch4_out) / 3.6
hc_conv_mol_s = (hc_carbon_in - ch4_out) / 3.6
print("C005 EC_CH4,abs = %.0f kJ/mol CH4 (%.0f kJ/mol hydrocarbon C)"
      % (1000 * q_abs / ch4_conv_mol_s, 1000 * q_abs / hc_conv_mol_s))
print("     EC_CH4,fired = %.0f kJ/mol HHV, %.0f kJ/mol LHV (per CH4); %.0f kJ/mol HHV per hydrocarbon C"
      % (1000 * q_fired_hhv / ch4_conv_mol_s, 1000 * q_fired_lhv / ch4_conv_mol_s,
         1000 * q_fired_hhv / hc_conv_mol_s))
print("     radiant efficiency Q_abs/Q_fired = %.3f LHV, %.3f HHV" % (q_abs / q_fired_lhv, q_abs / q_fired_hhv))

# SRC004-C006: whole-system efficiencies. No electricity import; power export is an output.
ng_hhv_mw = M_NG_TOTAL * NG_HHV_REPORT / 3600
h2_hhv_mw = M_H2 * H2_HHV_REPORT / 3600
print("C006 NG input %.1f MW HHV; H2 product %.1f MW HHV" % (ng_hhv_mw, h2_hhv_mw))
print("     eta_HHV (H2 only) = %.1f%%; with export power = %.1f%%; f_electric = 0"
      % (100 * h2_hhv_mw / ng_hhv_mw, 100 * (h2_hhv_mw + P_EXPORT) / ng_hhv_mw))
print("     LHV: H2 only %.1f%%; with export power %.1f%%"
      % (100 * ENERGY_PRODUCT_LHV / ENERGY_INPUT_LHV, 100 * (ENERGY_PRODUCT_LHV + P_EXPORT) / ENERGY_INPUT_LHV))
print("     %.1f MJ NG HHV/kg H2 (%.1f MJ LHV/kg H2); %.2f kWh exported/kg H2"
      % (ng_hhv_mw * 3600 / M_H2, ENERGY_INPUT_LHV * 3600 / M_H2, 1000 * P_EXPORT / M_H2))
