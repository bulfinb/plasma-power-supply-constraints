"""Reviewer calculations SRC007-C001 to C008 for Hrabovsky et al. (2018).

Inputs are from manuscript.pdf and carry the evidence IDs listed in evidence.csv.
Outlet compositions are reviewer figure readings (pixel-colour digitisation of the
mass-spectrometer traces in Figs. 7 and 8; see extraction.md, "Figure reading method").
Run with: python3 calculations.py
"""

# ---------------------------------------------------------------- constants
V_M0 = 22.414    # L/mol, 0 degC and 1 atm (assumed slm reference; not stated, E009)
V_M20 = 24.055   # L/mol, 20 degC and 1 atm (sensitivity case)
M_H2, M_H2O, M_AR = 2.016, 18.015, 39.948    # g/mol
LHV = {"H2": 241.8, "CO": 283.0, "CH4": 802.3}   # kJ/mol, 298 K
HHV = {"H2": 285.8, "CO": 283.0, "CH4": 890.6}   # kJ/mol, 298 K
TORCH_EFF = (0.57, 0.60)   # E005 (printed as "0.57-0.60 %"; read as a fraction)
AR_TRACER_SLM = 50.0       # E014, E016

# ------------------------------------------------- operating points (inputs)
# Outlet dry mole % read from Fig. 7 (SMR, E015) and Fig. 8 (DRM, E016).
# CO2 values below ~0.5 % in Fig. 7 segments B-D could not be resolved from the
# axis line and are set to 0.3 % (midpoint of 0-0.5 %), see E015 notes.
OPS = {
    # id: route, P_arc kW, CH4 slm, CO2 slm, H2O g/min, outlet %: H2, CO, CO2, CH4, Ar
    "OP001": ("SMR", 120, 150, 0, 94, dict(H2=68.0, CO=21.2, CO2=1.0, CH4=2.2, Ar=8.4)),
    "OP002": ("SMR", 120, 75, 0, 38, dict(H2=63.4, CO=21.7, CO2=0.3, CH4=0.2, Ar=14.6)),
    "OP003": ("SMR", 120, 125, 0, 75, dict(H2=68.0, CO=20.9, CO2=0.3, CH4=1.1, Ar=9.5)),
    "OP004": ("SMR", 120, 100, 0, 56, dict(H2=66.5, CO=21.2, CO2=0.3, CH4=0.7, Ar=11.6)),
    "OP005": ("DRM", 116, 125, 101, 18, dict(H2=48.7, CO=39.1, CO2=1.7, CH4=1.1, Ar=9.4)),
    "OP006": ("DRM", 97, 125, 101, 18, dict(H2=46.2, CO=38.7, CO2=1.8, CH4=2.8, Ar=10.6)),
    "OP007": ("DRM", 107, 125, 101, 18, dict(H2=47.2, CO=39.2, CO2=2.0, CH4=1.7, Ar=9.8)),
    "OP008": ("DRM", 89, 125, 101, 18, dict(H2=43.2, CO=39.0, CO2=2.4, CH4=4.5, Ar=10.8)),
}


def evaluate(op, v_m=V_M0, extra_ar_slm=0.0):
    route, p_kw, ch4_slm, co2_slm, h2o_gmin, x = OPS[op]
    pct = {k: v / 100 for k, v in x.items()}
    f_out = (AR_TRACER_SLM + extra_ar_slm) / pct["Ar"]          # slm, dry outlet (C002)
    out = {k: pct[k] * f_out for k in ("H2", "CO", "CO2", "CH4")}  # slm
    x_ch4 = 1 - out["CH4"] / ch4_slm                              # C003
    x_co2 = 1 - out["CO2"] / co2_slm if co2_slm else None
    c_in = ch4_slm + co2_slm
    c_out = out["CH4"] + out["CO"] + out["CO2"]
    mol = lambda slm: slm / v_m / 60                              # slm -> mol/s
    f_ch4_in, f_conv = mol(ch4_slm), mol(ch4_slm) * x_ch4
    f_h2, f_co = mol(out["H2"]), mol(out["CO"])
    r = dict(route=route, P=p_kw, sum_pct=sum(x.values()), f_out=f_out,
             X_CH4=x_ch4, X_CO2=x_co2, C_closure=c_out / c_in,
             H2O_CH4=(h2o_gmin / M_H2O / 60) / f_ch4_in,
             F_CH4_mol_min=f_ch4_in * 60,
             H2_slm=out["H2"], H2_kg_h=f_h2 * M_H2 * 3.6, H2_CO=out["H2"] / out["CO"])
    # C004 power-basis metrics on ARC power (torch terminal electrical power)
    r["SEI_CH4"] = p_kw / f_ch4_in
    r["EC_CH4"] = p_kw / f_conv
    r["EC_H2"] = p_kw / f_h2
    r["MJ_per_kg_H2"] = p_kw / (f_h2 * M_H2) / 1000 * 1000      # kJ/g = MJ/kg
    r["EY_H2"] = f_h2 * M_H2 * 3600 / p_kw                       # g/kWh
    r["eta_P_LHV"] = (f_h2 * LHV["H2"] + f_co * LHV["CO"]) / (p_kw + f_conv * LHV["CH4"])
    # C005 plasma-jet basis: arc power x torch efficiency (range, not point-specific)
    r["EC_CH4_jet"] = tuple(p_kw * e / f_conv for e in TORCH_EFF)
    # C006 partial eta_HHV (arc power + CH4 feed HHV; auxiliaries, rectifier, Ar excluded)
    d = p_kw + f_ch4_in * HHV["CH4"]
    r["eta_HHV"] = (f_h2 * HHV["H2"] + f_co * HHV["CO"]) / d
    r["f_electric"] = p_kw / d
    return r


print("C001-C006 per operating point (base case: 0 degC slm, Ar in reactor = 50 slm)")
for op in OPS:
    r = evaluate(op)
    xco2 = "%.1f" % (100 * r["X_CO2"]) if r["X_CO2"] is not None else "NA"
    print(f"{op} {r['route']} P={r['P']} kW | sum={r['sum_pct']:.1f}% F_out={r['f_out']:.0f} slm "
          f"| F_CH4={r['F_CH4_mol_min']:.2f} mol/min H2O/CH4={r['H2O_CH4']:.2f} "
          f"| X_CH4={100*r['X_CH4']:.1f}% X_CO2={xco2}% C-closure={100*r['C_closure']:.0f}% "
          f"| H2={r['H2_slm']:.0f} slm ({r['H2_kg_h']:.2f} kg/h) H2/CO={r['H2_CO']:.2f}")
    print(f"      SEI_CH4={r['SEI_CH4']:.0f} EC_CH4={r['EC_CH4']:.0f} kJ/mol (arc); "
          f"jet {r['EC_CH4_jet'][0]:.0f}-{r['EC_CH4_jet'][1]:.0f}; EC_H2={r['EC_H2']:.0f} kJ/mol "
          f"= {r['MJ_per_kg_H2']:.0f} MJ/kg; EY_H2={r['EY_H2']:.1f} g/kWh; "
          f"eta_P,LHV={100*r['eta_P_LHV']:.1f}%; eta_HHV(partial)={100*r['eta_HHV']:.1f}% "
          f"f_el={r['f_electric']:.2f}")

# C007 sensitivity: plasma-forming argon not included in the 50 slm tracer, and 20 degC slm.
# Plasma Ar from plasma mass flow 0.37-0.44 g/s and H2O/Ar volume ratio 2.2-3.0 (E005).
ar_lo = 0.37 / (3.0 * M_H2O + M_AR) * V_M0 * 60
ar_hi = 0.44 / (2.2 * M_H2O + M_AR) * V_M0 * 60
print(f"\nC007 plasma Ar estimate {ar_lo:.1f}-{ar_hi:.1f} slm (0 degC)")
for op in ("OP001", "OP002", "OP005", "OP008"):
    b, a, w = evaluate(op), evaluate(op, extra_ar_slm=ar_hi), evaluate(op, v_m=V_M20)
    print(f"{op}: X_CH4 {100*b['X_CH4']:.1f} -> {100*a['X_CH4']:.1f}% with plasma Ar; "
          f"EC_H2 {b['MJ_per_kg_H2']:.0f} -> {a['MJ_per_kg_H2']:.0f} MJ/kg; "
          f"EC_CH4 {b['EC_CH4']:.0f} -> {a['EC_CH4']:.0f} (plasma Ar), {w['EC_CH4']:.0f} (20 degC slm)")

# C008 process-enthalpy basis (author boundary: arc power - torch loss - reactor loss),
# EC_CH4 = process enthalpy / X_CH4, from the authors' own plotted points (Figs. 9, 10).
print("\nC008 process-basis EC_CH4 from author points (graph-read, approximate)")
for label, pe, x in [("SMR lowest enthalpy", 480, 0.915), ("SMR highest enthalpy", 920, 0.994),
                     ("DRM lowest enthalpy", 355, 0.827), ("DRM highest enthalpy", 990, 0.996)]:
    print(f"  {label}: {pe} kJ/mol CH4 fed, X_CH4 {100*x:.1f}% -> EC_CH4 {pe/x:.0f} kJ/mol")
