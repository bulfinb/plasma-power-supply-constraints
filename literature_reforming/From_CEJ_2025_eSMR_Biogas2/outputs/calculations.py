"""Reviewer calculations SRC006-C001 to C004 for From et al. (2025), eSMR pilot plant, feed-forward control.

Inputs are taken from the manuscript and labelled with evidence IDs in evidence.csv.
Run with: python3 calculations.py
"""

NM3_PER_KMOL = 22.414  # normal reference assumed 0 degC, 1 atm (not stated in the paper)


def mol_min(nm3_h):
    return nm3_h / NM3_PER_KMOL * 1000 / 60


# SRC006-C001: methane feed.
# OP001: 6.3 Nm3/h biogas at CH4/CO2 1.33 (57.1% CH4) at TOS 0 (E008).
print("C001 OP001 CH4 feed %.2f mol/min (biogas %.2f mol/min)" % (mol_min(6.3 * 0.571), mol_min(6.3)))
# OP002: 6.4 Nm3/h biogas (E010); biogas CH4/CO2 about 1.1-1.22 outside CO2-addition periods (E011, graph-read).
for ratio in (1.10, 1.22):
    y_ch4 = ratio / (1 + ratio)
    print("     OP002 biogas CH4/CO2 %.2f: %.1f%% CH4, CH4 feed %.2f mol/min" % (ratio, 100 * y_ch4, mol_min(6.4 * y_ch4)))
# Table 2 (OP003-OP008): 6 Nm3/h biogas, composition not reported; 50-75% CH4 range.
print("     OP003-OP008 CH4 feed %.1f-%.1f mol/min (50-75%% CH4 assumed)" % (mol_min(6 * 0.50), mol_min(6 * 0.75)))

# SRC006-C002: CH4 and CO2 conversion at OP002 from Table 1 (wet mol%, 80 h average; E013).
OUT = {"H2": 53.0, "H2O": 23.0, "CO": 17.3, "CO2": 6.2, "CH4": 0.24}
carbon_out = OUT["CO"] + OUT["CO2"] + OUT["CH4"]
# Inlet CH4 share of carbon from the Fig. 5C CH4/CO2 ratio range, including added CO2 (E011).
for ratio in (0.78, 1.22):
    x_ch4 = ratio / (1 + ratio)
    x_conv_ch4 = 1 - (OUT["CH4"] / carbon_out) / x_ch4
    x_conv_co2 = 1 - (OUT["CO2"] / carbon_out) / (1 - x_ch4)
    print("C002 inlet CH4/CO2 %.2f: X_CH4 %.1f%%, X_CO2 %.1f%%" % (ratio, 100 * x_conv_ch4, 100 * x_conv_co2))

# SRC006-C003: elemental consistency, outlet O/C and H/C vs inlet setpoints 2.22 and 6.46 (E012).
o_c = (OUT["H2O"] + OUT["CO"] + 2 * OUT["CO2"]) / carbon_out
h_c = (2 * OUT["H2"] + 2 * OUT["H2O"] + 4 * OUT["CH4"]) / carbon_out
print("C003 outlet O/C %.2f (inlet 2.22); H/C %.2f (inlet 6.46)" % (o_c, h_c))

# SRC006-C004: EC_CH4 and other power-basis metrics not calculated; no electrical power reported (E005).
