"""Reviewer calculations SRC012-C001 to C005 for Zhu et al. (2019).

SLM converted at 0 degC, 1 atm (22.414 L/mol): this reproduces the authors' SEI
(246 W / 3 SLM = 110 kJ/mol, C001). Evidence IDs in evidence.csv.
Run with: python3 calculations.py
"""

VM = 22.414
M_H2 = 2.016
LHV = {"H2": 241.8, "CO": 283.0, "CH4": 802.3}
HHV = {"H2": 285.8, "CO": 283.0, "CH4": 890.6}


def mol_s(slm, vm=VM):
    return slm / vm / 60


# C001 SEI check (SEI = P / total inlet moles of CH4 + H2O)
for p, ft, sei in ((246, 3.0, 110), (149, 2.5, 80), (206, 2.5, 110), (187, 2.5, 100)):
    print(f"C001 P={p} W, Ft={ft} SLM: SEI = {p/1000/mol_s(ft):.0f} kJ/mol (author {sei}); "
          f"at 20 degC SLM {p/1000/mol_s(ft, 24.055):.0f}")

# Operating points: P (W), Ft (SLM), S/C, X_CH4 (%), and for OP003/OP004 selectivities
OPS = {
    "OP001 plasma alone, SEI 80, S/C 2": (149, 2.5, 2, 40, None),
    "OP002 plasma alone, SEI 110, S/C 2": (206, 2.5, 2, 56, None),
    "OP003 plasma alone, optimum (Fig. 4)": (246, 3.0, 3, 65, dict(sCO=0.77, sCO2=0.10, tH2_EC=2.3)),
    "OP004 plasma + Ni catalyst, optimum": (246, 3.0, 3, 90, dict(sCO=0.52, sCO2=0.46, tH2_EC=1.5)),
}
print("\nC002-C004 power basis (discharge power; steam vaporizer and ballast resistor excluded)")
for op, (p_w, ft, sc, x, sel) in OPS.items():
    p = p_w / 1000
    ch4 = ft / (1 + sc)                     # SLM CH4
    h2o = ft - ch4
    f_ch4 = mol_s(ch4)
    f_conv = f_ch4 * x / 100
    line = (f"{op}: CH4 {ch4:.3f} SLM ({f_ch4*60:.4f} mol/min) | SEI_CH4={p/f_ch4:.0f} "
            f"EC_CH4={p/f_conv:.0f} kJ/mol")
    if sel:
        conv_slm = ch4 * x / 100
        co = sel["sCO"] * conv_slm
        co2 = sel["sCO2"] * conv_slm
        h2 = 3 * co + 4 * co2                 # H2 from SMR to CO and to CO2 (C2Hx neglected)
        f_h2, f_co = mol_s(h2), mol_s(co)
        eta = (f_h2 * LHV["H2"] + f_co * LHV["CO"]) / (p + f_conv * LHV["CH4"])
        eta_auth = ((f_h2 + f_co) * LHV["H2"]) / (p + f_conv * LHV["CH4"])
        ec_auth = p / ((h2 + co) * 60 / 1000)          # kWh/Nm3 t-H2
        eta_hhv = (f_h2 * HHV["H2"] + f_co * HHV["CO"]) / (p + f_ch4 * HHV["CH4"])
        line += (f"\n      H2 {h2:.2f} SLM, CO {co:.2f}, t-H2 {h2+co:.2f} SLM | EC_H2={p/f_h2:.0f} kJ/mol "
                 f"EY_H2={f_h2*M_H2*3600/p:.1f} g/kWh eta_P,LHV={100*eta:.1f}% "
                 f"| author eta recalc {100*eta_auth:.1f}%, author EC recalc {ec_auth:.2f} kWh/Nm3 "
                 f"(reported {sel['tH2_EC']}) | eta_HHV(partial)={100*eta_hhv:.1f}% "
                 f"f_el={p/(p+f_ch4*HHV['CH4']):.2f}")
    print(line)

# C005 indicative steam-raising duty at the optimum (2.25 SLM steam from 20 degC water to
# saturated vapour at 100 degC; inlet steam temperature not reported)
h2o = 3.0 * 3 / 4
dh = 75.3e-3 * 80 + 40.65
q = mol_s(h2o) * dh * 1000                    # W
f_conv = mol_s(0.75) * 0.90
print(f"\nC005 steam duty ~{q:.0f} W ({100*q/246:.0f}% of 246 W); "
      f"OP004 EC_CH4 incl. ~{(0.246+q/1000)/f_conv:.0f} kJ/mol (indicative only)")
