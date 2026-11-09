"""Reviewer calculations SRC003-C001 to C006 for NETL (2022), Case 1 fired SMR.

Inputs are taken from the report and labelled with evidence IDs in evidence.csv.
Run with: python3 calculations.py
"""

# SRC003-C001: standard 25 degC heats of combustion, kJ/mol (HHV, LHV).
# Cite a specific property source (e.g. NIST Chemistry WebBook) in the report.
HHV = {"H2": 285.83, "CH4": 890.6, "C2H6": 1560.7, "C3H8": 2219.2, "C4H10": 2877.5, "CO": 282.98}
LHV = {"H2": 241.83, "CH4": 802.3, "C2H6": 1428.6, "C3H8": 2043.1, "C4H10": 2657.3, "CO": 282.98}

# Combustible mole fractions and molar flows (kmol/h), Exhibit 3-4 and Exhibit 2-6.
NG = {"CH4": 0.931, "C2H6": 0.032, "C3H8": 0.007, "C4H10": 0.004}  # E006
NG_MW = 17.328                                                       # kg/kmol, Exhibit 3-4 stream 3
F_NG_TOTAL = 4096                                                    # stream 3, E008
F_NG_PROCESS = 3687                                                  # stream 4, E011
F_NG_FUEL = 410                                                      # stream 14, E012
PSA_OFFGAS = {"CH4": 0.1410, "CO": 0.0137, "H2": 0.3085}             # stream 13, E013
F_PSA_OFFGAS = 5695
BURNER_FUEL = {"CH4": 0.1940, "C2H6": 0.0022, "C3H8": 0.0005,
               "C4H10": 0.0003, "CO": 0.0128, "H2": 0.2878}          # stream 15, E014
F_BURNER_FUEL = 6104

# Reformer inlet (stream 7, E015) and outlet (stream 8, E016).
M_REFORMER = 240966          # kg/h, same for both streams
H_STREAM7 = -10182.33        # kJ/kg, Aspen Plus enthalpy (elements at 25 degC reference)
H_STREAM8 = -6233.86         # kJ/kg
F_STREAM7, Y_CH4_STREAM7 = 13930, 0.2583
F_STREAM8, Y_CH4_STREAM8 = 19519, 0.0411
F_STREAM10, Y_CH4_STREAM10 = 15654, 0.0513   # shift outlet, Exhibit 3-4 continued

# Plant-level values, Exhibits 3-4 and 3-5.
F_H2_PRODUCT, Y_H2_PRODUCT = 9959, 0.9998    # stream 11/12
M_H2_PRODUCT = 20126                         # kg/h, E004
P_ELECTRIC_MW = 12.65                        # total auxiliaries, E025
NG_HHV_INPUT_MW = 1031.068                   # E009
NETL_NG_HHV, NETL_NG_LHV = 52.295, 47.201    # MJ/kg, E007


def heating_value(composition, table):
    """Mixture heating value in kJ/mol of mixture."""
    return sum(y * table[species] for species, y in composition.items())


def duty_mw(composition, flow_kmol_h, table):
    """Chemical energy flow in MW for a stream."""
    return heating_value(composition, table) * flow_kmol_h / 3600


# SRC003-C001: validate heating values against NETL natural gas.
ng_hhv = heating_value(NG, HHV) / NG_MW
ng_lhv = heating_value(NG, LHV) / NG_MW
print("C001 NG HHV %.3f MJ/kg (NETL %.3f); LHV %.3f MJ/kg (NETL %.3f)"
      % (ng_hhv, NETL_NG_HHV, ng_lhv, NETL_NG_LHV))
print("     total NG %.1f MW HHV (NETL %.1f)" % (duty_mw(NG, F_NG_TOTAL, HHV), NG_HHV_INPUT_MW))

# SRC003-C002: reformer process-gas heat uptake.
q_abs = M_REFORMER * (H_STREAM8 - H_STREAM7) / 3.6e6  # MW
print("C002 Q_abs = %.1f MW" % q_abs)

# SRC003-C003: methane conversion, reformer and plant.
ch4_in = Y_CH4_STREAM7 * F_STREAM7
ch4_out = Y_CH4_STREAM8 * F_STREAM8
ch4_conv = ch4_in - ch4_out
ch4_process = NG["CH4"] * F_NG_PROCESS
ch4_slip = Y_CH4_STREAM10 * F_STREAM10
print("C003 reformer: CH4 in %.1f, out %.1f, converted %.1f kmol/h, X = %.1f%%"
      % (ch4_in, ch4_out, ch4_conv, 100 * ch4_conv / ch4_in))
print("     plant: X = %.1f%%" % (100 * (ch4_process - ch4_slip) / ch4_process))

# SRC003-C004: burner fuel duty.
q_fired_hhv = duty_mw(BURNER_FUEL, F_BURNER_FUEL, HHV)
q_fired_lhv = duty_mw(BURNER_FUEL, F_BURNER_FUEL, LHV)
print("C004 Q_fired = %.1f MW HHV, %.1f MW LHV" % (q_fired_hhv, q_fired_lhv))
print("     PSA off-gas %.1f / %.1f MW; supplemental NG %.1f / %.1f MW (HHV / LHV)"
      % (duty_mw(PSA_OFFGAS, F_PSA_OFFGAS, HHV), duty_mw(PSA_OFFGAS, F_PSA_OFFGAS, LHV),
         duty_mw(NG, F_NG_FUEL, HHV), duty_mw(NG, F_NG_FUEL, LHV)))

# SRC003-C005: heat-basis energy cost per mol CH4 converted.
ch4_conv_mol_s = ch4_conv / 3.6
print("C005 EC_CH4,abs = %.0f kJ/mol" % (1000 * q_abs / ch4_conv_mol_s))
print("     EC_CH4,fired = %.0f kJ/mol HHV, %.0f kJ/mol LHV"
      % (1000 * q_fired_hhv / ch4_conv_mol_s, 1000 * q_fired_lhv / ch4_conv_mol_s))
print("     Q_abs/Q_fired = %.3f LHV, %.3f HHV" % (q_abs / q_fired_lhv, q_abs / q_fired_hhv))

# SRC003-C006: whole-system eta_HHV (workflow.md section 4) and author metrics.
h2_hhv_mw = Y_H2_PRODUCT * F_H2_PRODUCT * HHV["H2"] / 3600
denominator = P_ELECTRIC_MW + NG_HHV_INPUT_MW
print("C006 H2 product %.1f MW HHV" % h2_hhv_mw)
print("     eta_HHV = %.1f%%, f_electric = %.1f%%"
      % (100 * h2_hhv_mw / denominator, 100 * P_ELECTRIC_MW / denominator))
print("     check author CGE %.1f%%, ETE %.1f%%"
      % (100 * h2_hhv_mw / NG_HHV_INPUT_MW, 100 * (h2_hhv_mw - P_ELECTRIC_MW) / NG_HHV_INPUT_MW))
print("     %.1f MJ NG HHV/kg H2; %.2f kWh electricity/kg H2"
      % (NG_HHV_INPUT_MW * 3600 / M_H2_PRODUCT, 1000 * P_ELECTRIC_MW / M_H2_PRODUCT))
