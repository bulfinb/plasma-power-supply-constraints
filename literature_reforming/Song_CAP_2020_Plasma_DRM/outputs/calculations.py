"""Reviewer calculations SRC009-C001 to C006 for Song et al. (2020).

Inputs are reviewer figure readings (Figs. 4, 5, 6, 8, 9) and text values; evidence IDs
are in evidence.csv. SLM reference conditions are not stated: 0 degC, 1 atm assumed
(this reproduces the authors' Fig. 8 efficiency and Fig. 9 SED; C002).
Run with: python3 calculations.py
"""

V0, V20 = 22.414, 24.055   # L/mol
M_H2 = 2.016
LHV = {"H2": 241.8, "CO": 283.0, "CH4": 802.3}
HHV = {"H2": 285.8, "CO": 283.0, "CH4": 890.6}
# Author LHVs, Eqs. (6)-(11), kJ/mol (CO printed as 285)
LHV_AUTH = {"H2": 241, "CO": 285, "CH4": 803, "C2H6": 1429, "C2H4": 1323, "C2H2": 1257}

# OP: P (kW), CO2 in, CH4 in (SLM), X_CO2, X_CH4 (%), products (SLM)
OPS = {
    # Fig. 4(A) / 5(A): CO2 = CH4 = 20 SLM
    "OP001": (17.0, 20, 20, 70, 77, dict(H2=20.0, CO=27.0)),
    "OP002": (18.5, 20, 20, 88, 92, dict(H2=33.5, CO=28.0)),
    "OP003": (20.0, 20, 20, 91, 94, dict(H2=35.2, CO=29.6)),
    # Fig. 4(B) / 5(B): 25 / 25 SLM
    "OP004": (18.0, 25, 25, 60, 64, dict(H2=16.7, CO=27.1)),
    "OP005": (20.0, 25, 25, 86, 82, dict(H2=34.8, CO=38.7)),
    "OP006": (23.0, 25, 25, 88, 86, dict(H2=36.0, CO=42.0)),
    # Fig. 4(C) / 5(C) / 9(C): 30 / 30 SLM
    "OP007": (21.0, 30, 30, 86, 82, dict(H2=42.3, CO=45.1)),
    "OP008": (23.0, 30, 30, 91, 89, dict(H2=49.2, CO=49.1)),
    "OP009": (27.0, 30, 30, 94, 94, dict(H2=58.8, CO=55.5)),
    # Figs. 6, 8, 9(A,B): 22 kW, CO2 30 SLM, CH4 20-36 SLM
    "OP010": (22.0, 30, 20, 88.7, 98.0, dict(H2=33.3, CO=44.4, C2H2=0.32, C2H4=0.09, C2H6=0.0027)),
    "OP011": (22.0, 30, 32, 87.5, 84.0, dict(H2=45.1, CO=44.4, C2H2=2.72, C2H4=0.47, C2H6=0.0105)),
    "OP012": (22.0, 30, 34, 86.8, 81.2, dict(H2=47.1, CO=44.8, C2H2=3.00, C2H4=0.52, C2H6=0.0137)),
    "OP013": (22.0, 30, 36, 87.1, 79.3, dict(H2=48.8, CO=45.7, C2H2=3.324, C2H4=0.61, C2H6=0.015)),
}
AUTHOR = {"OP010": (46.6, 98.0, 17.0), "OP011": (53.9, 96.3, 14.75), "OP012": (55.2, 97.3, 14.37),
          "OP013": (56.7, 98.3, 13.97), "OP007": (None, 96.7, 14.4), "OP008": (None, 98.9, 14.2),
          "OP009": (None, 99.9, 14.1)}   # (ECE %, carbon balance %, SED kJ/L) read from Figs. 8-9


def mol_s(slm, vm=V0):
    return slm / vm / 60


def evaluate(op, vm=V0):
    p, co2, ch4, xco2, xch4, prod = OPS[op]
    r = {}
    f_ch4 = mol_s(ch4, vm)
    f_conv = f_ch4 * xch4 / 100
    f_co2conv = mol_s(co2, vm) * xco2 / 100
    f = {k: mol_s(v, vm) for k, v in prod.items()}
    r["SEI_total"] = p * 60 / (co2 + ch4)                       # kJ/L (SLM basis)
    r["SEI_CH4"] = p / f_ch4
    r["EC_CH4"] = p / f_conv
    r["EC_conv_total"] = p / (f_conv + f_co2conv)               # per mol (CH4+CO2) converted
    r["EC_H2"] = p / f["H2"]
    r["EY_H2"] = f["H2"] * M_H2 * 3600 / p
    r["eta_P_LHV"] = (f["H2"] * LHV["H2"] + f["CO"] * LHV["CO"]) / (p + f_conv * LHV["CH4"])
    r["eta_HHV"] = (f["H2"] * HHV["H2"] + f["CO"] * HHV["CO"]) / (p + f_ch4 * HHV["CH4"])
    r["f_el"] = p / (p + f_ch4 * HHV["CH4"])
    r["H2_CO"] = prod["H2"] / prod["CO"]
    r["H2_ceiling"] = prod["H2"] / (2 * ch4 * xch4 / 100)       # H2 / (2 x CH4 converted)
    r["SED"] = p * 60 / (prod["H2"] + prod["CO"])                # kJ/L syngas, Eq. (15)
    if "C2H2" in prod:
        num = sum(f[k] * LHV_AUTH[k] for k in prod)
        r["ECE_author_recalc"] = num / (p + f_conv * LHV_AUTH["CH4"])
        c_out = (co2 * (1 - xco2 / 100) + ch4 * (1 - xch4 / 100) + prod["CO"]
                 + 2 * (prod["C2H2"] + prod["C2H4"] + prod["C2H6"]))
        r["C_balance"] = c_out / (co2 + ch4)
        o_out = 2 * co2 * (1 - xco2 / 100) + prod["CO"]
        r["O_deficit_SLM"] = 2 * co2 - o_out                     # unmeasured O (likely H2O)
    return r


print("C001-C005 (0 degC SLM; P = generator 'input/applied' power, see extraction.md)")
for op in OPS:
    r = evaluate(op)
    p, co2, ch4, xco2, xch4, _ = OPS[op]
    line = (f"{op} P={p} kW CO2/CH4={co2}/{ch4} X={xco2}/{xch4}% | SEI={r['SEI_total']:.1f} kJ/L "
            f"SEI_CH4={r['SEI_CH4']:.0f} EC_CH4={r['EC_CH4']:.0f} EC_conv={r['EC_conv_total']:.0f} kJ/mol "
            f"| EC_H2={r['EC_H2']:.0f} kJ/mol EY={r['EY_H2']:.1f} g/kWh eta_P,LHV={100*r['eta_P_LHV']:.1f}% "
            f"eta_HHV={100*r['eta_HHV']:.1f}% f_el={r['f_el']:.2f} H2/CO={r['H2_CO']:.2f} "
            f"H2/(2 CH4conv)={r['H2_ceiling']:.2f} SED={r['SED']:.1f}")
    if "ECE_author_recalc" in r:
        line += (f"\n      author-ECE recalc={100*r['ECE_author_recalc']:.1f}% "
                 f"C-balance={100*r['C_balance']:.1f}% O deficit={r['O_deficit_SLM']:.1f} SLM")
    if op in AUTHOR:
        a = AUTHOR[op]
        line += f"\n      author (Figs. 8-9): ECE={a[0]} C-balance={a[1]} SED={a[2]}"
    print(line)

# C006 sensitivity: 20 degC SLM reference for the headline point
r0, r20 = evaluate("OP013"), evaluate("OP013", V20)
print(f"\nC006 OP013 at 20 degC SLM: EC_CH4 {r0['EC_CH4']:.0f} -> {r20['EC_CH4']:.0f} kJ/mol; "
      f"author ECE recalc {100*r0['ECE_author_recalc']:.1f} -> {100*r20['ECE_author_recalc']:.1f}%")
r0, r20 = evaluate("OP009"), evaluate("OP009", V20)
print(f"     OP009 at 20 degC SLM: EC_CH4 {r0['EC_CH4']:.0f} -> {r20['EC_CH4']:.0f} kJ/mol")
