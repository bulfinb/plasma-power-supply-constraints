"""Reviewer calculations SRC011-C001 to C004 for Kelly et al. (2023).

All four operating points: 1 kW absorbed microwave power, 10 nL/min total CO2+CH4,
molar volume 24.05 L/mol (authors' reference, Eq. 7). Evidence IDs in evidence.csv.
Run with: python3 calculations.py
"""

VM = 24.05          # L/mol, authors' standard reference (E009)
EV = 96.485         # kJ/mol per eV/molecule
M_H2 = 2.016
LHV = {"H2": 241.8, "CO": 283.0, "CH4": 802.3}
HHV = {"H2": 285.8, "CO": 283.0, "CH4": 890.6}
P = 1.0             # kW (E003)
F_TOT = 10.0        # nL/min (E004)

# OP: CO2 frac, CH4 frac, X_CO2 %, X_CH4 %, X_tot %, author EC eV/molecule (Table 1 / text)
OPS = {
    "OP001": (0.70, 0.30, 49.4, 66.5, 53.5, 2.8),
    "OP002": (0.65, 0.35, 49.0, 63.0, 53.0, 2.8),   # Table 1 only (integers)
    "OP003": (0.60, 0.40, 46.2, 58.0, 50.0, 2.9),
    "OP004": (0.55, 0.45, 45.8, 55.2, 49.6, 3.0),
}
# Syngas data available at the two end points (E013-E015):
#   OP001: y_CO 41.0%, y_H2 23.0%, EC_syngas 7.8 kJ/L ; OP004: H2/CO 1.01, EC_syngas 6.9 kJ/L
SYN = {"OP001": dict(yCO=0.410, yH2=0.230, ec_syn=7.8),
       "OP004": dict(h2co=1.01, ec_syn=6.9)}

f_tot = F_TOT / VM / 60                     # mol/s
sei = P * 60 / F_TOT                        # kJ/L
print(f"SEI = {sei:.1f} kJ/L = {P/f_tot:.0f} kJ/mol total feed ({P/f_tot/EV:.2f} eV/molecule)\n")

print("C001 power basis (absorbed microwave power; no external heat)")
for op, (yco2, ych4, xco2, xch4, xtot, ec_auth) in OPS.items():
    f_ch4 = f_tot * ych4
    f_conv = f_ch4 * xch4 / 100
    ec_tot = P / (f_tot * xtot / 100)
    xtot_check = yco2 * xco2 + ych4 * xch4
    print(f"{op} {int(yco2*100)}/{int(ych4*100)}: SEI_CH4={P/f_ch4:.0f} EC_CH4={P/f_conv:.0f} kJ/mol "
          f"| EC per molecule converted={ec_tot:.0f} kJ/mol = {ec_tot/EV:.2f} eV (author {ec_auth}) "
          f"| X_tot check {xtot_check:.1f}% vs {xtot}%")

# C002 product flows from the authors' syngas energy cost: EC_syn = SEI / (alpha (y_CO + y_H2))
print("\nC002 syngas flows and H2 metrics (from EC_syngas, Eq. 8)")
for op, d in SYN.items():
    yco2, ych4, xco2, xch4, xtot, _ = OPS[op]
    a_syn = sei / d["ec_syn"]                       # alpha*(yCO + yH2)
    if "yCO" in d:
        alpha = a_syn / (d["yCO"] + d["yH2"])
        a_co, a_h2 = alpha * d["yCO"], alpha * d["yH2"]
        extra = f" alpha = {alpha:.2f}"
    else:
        a_co = a_syn / (1 + d["h2co"])
        a_h2 = a_syn - a_co
        extra = ""
    f_h2 = a_h2 * f_tot                              # mol/s
    f_co = a_co * f_tot
    f_conv = f_tot * ych4 * xch4 / 100
    # selectivity cross-checks against Fig. 4 values quoted in the text
    s_h = 2 * a_h2 / (4 * ych4 * xch4 / 100)
    s_c = a_co / (yco2 * xco2 / 100 + ych4 * xch4 / 100)
    eta = (f_h2 * LHV["H2"] + f_co * LHV["CO"]) / (P + f_conv * LHV["CH4"])
    eta_hhv = (f_h2 * HHV["H2"] + f_co * HHV["CO"]) / (P + f_tot * ych4 * HHV["CH4"])
    print(f"{op}:{extra} H2 {a_h2*F_TOT:.2f} nL/min, CO {a_co*F_TOT:.2f} nL/min | "
          f"EC_H2 = {P/f_h2:.0f} kJ/mol, EY_H2 = {f_h2*M_H2*3600/P:.1f} g/kWh, "
          f"eta_P,LHV = {100*eta:.1f}%, eta_HHV(partial) = {100*eta_hhv:.1f}%, "
          f"f_el = {P/(P+f_tot*ych4*HHV['CH4']):.2f} | check S_H,H2 = {s_h:.2f}, S_C,CO = {s_c:.2f}")
print("   (author S_H,H2 0.68 / 0.86; S_C,CO 0.91 / 0.85 at 70/30 / 55/45)")
