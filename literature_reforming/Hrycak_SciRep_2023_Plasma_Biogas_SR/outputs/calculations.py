"""Reviewer calculations SRC010-C001 to C005 for Hrycak et al. (2023).

Inputs: Table 1 (three tabulated best points) and Fig. 9 (power sweep, graph-read).
NL = normal litres; reference not stated. Vm 24.25 L/mol reproduces the authors' derived values (XR008). Evidence IDs in evidence.csv.
Run with: python3 calculations.py
"""

VM = 24.25   # L/mol; revised 2026-11-20 (XR008): reproduces the authors' H2 rate and conversion in all three Table 1 rows (was 22.414)
M_H2 = 2.016
LHV = {"H2": 241.8, "CO": 283.0, "CH4": 802.3}
HHV = {"H2": 285.8, "CO": 283.0, "CH4": 890.6}

# OP: P_abs kW, CH4:CO2 total NL/h, CH4 %, steam kg/h, H2 g/h, X_CH4 % (author),
#     outlet composition (vol %, excludes N2 marker and H2O; Table 1) or None
OPS = {
    "OP001": (6.5, 6000, 75, 3, 239, 48.9,
              dict(H2=40.0, CO2=11.8, CO=14.3, CH4=32.0, C2H2=1.6, C2H4=0.18, C2H6=0.06)),
    "OP002": (6.5, 3000, 100, 3, 234, 66.1,
              dict(H2=58.4, CO2=3.2, CO=14.4, CH4=21.1, C2H2=2.4, C2H4=0.4, C2H6=0.06)),
    "OP003": (6.5, 3000, 50, 2, 171.5, 74.3,
              dict(H2=46.78, CO2=13.71, CO=29.96, CH4=8.74, C2H2=0.56, C2H4=0.19, C2H6=0.06)),
    # Fig. 9 power sweep: 6000 NL/h, 50% CH4, 2 kg/h steam (graph-read, E020)
    "OP004": (4.5, 6000, 50, 2, 128.5, 40.5, None),
    "OP005": (5.5, 6000, 50, 2, 162.5, 42.3, None),
    "OP006": (6.5, 6000, 50, 2, 191.0, 49.4, None),
}


def steam_kw(kg_h):
    """Indicative duty to raise steam from 20 degC water to 300 degC vapour (C004)."""
    dh = 75.3e-3 * 80 + 40.65 + 34.5e-3 * 200      # kJ/mol: liquid heating + vaporisation + superheat
    return kg_h * 1000 / 18.015 / 3600 * dh


print("C001-C003 per operating point (absorbed microwave power; steam generation excluded)")
for op, (p, tot, pct, steam, h2_gh, x_auth, comp) in OPS.items():
    ch4 = tot * pct / 100
    co2 = tot - ch4
    f_ch4 = ch4 / VM / 3600                                     # mol/s
    f_conv = f_ch4 * x_auth / 100
    f_h2 = h2_gh / M_H2 / 3600
    sei = p / f_ch4
    ec = p / f_conv
    ec_h2 = p / f_h2
    ey = h2_gh / p
    s_kw = steam_kw(steam)
    line = (f"{op} P={p} kW {tot} NL/h {pct}% CH4 steam {steam} kg/h (S/C {steam*1000/18.015/(ch4/VM):.2f}) | "
            f"F_CH4={f_ch4*60:.2f} mol/min SEI_CH4={sei:.0f} EC_CH4={ec:.0f} kJ/mol "
            f"EC_H2={ec_h2:.0f} kJ/mol EY={ey:.1f} g/kWh | steam ~{s_kw:.2f} kW ({100*s_kw/p:.0f}% of P) "
            f"-> EC_CH4 incl. ~{(p+s_kw)/f_conv:.0f}")
    if comp:
        # Outlet flow anchored on the author's H2 rate (C002)
        f_out = (h2_gh / M_H2 * VM) / (comp["H2"] / 100)        # NL/h, dry, N2-free
        out = {k: v / 100 * f_out for k, v in comp.items()}
        x_h2anchor = 1 - out["CH4"] / ch4
        x_co2 = 1 - out["CO2"] / co2 if co2 else None
        c_out = out["CH4"] + out["CO"] + out["CO2"] + 2 * (out["C2H2"] + out["C2H4"] + out["C2H6"])
        f_co = out["CO"] / VM / 3600
        eta = (f_h2 * LHV["H2"] + f_co * LHV["CO"]) / (p + f_conv * LHV["CH4"])
        eta_hhv = (f_h2 * HHV["H2"] + f_co * HHV["CO"]) / (p + f_ch4 * HHV["CH4"])
        line += (f"\n      sum={sum(comp.values()):.2f}% F_out(dry,N2-free)={f_out:.0f} NL/h "
                 f"X_CH4(H2-anchored)={100*x_h2anchor:.1f}% vs author {x_auth}% ; "
                 f"X_CO2={'%.1f' % (100*x_co2) if x_co2 is not None else 'NA (no CO2 fed)'}% ; "
                 f"C closure={100*c_out/tot:.0f}% ; H2/CO={comp['H2']/comp['CO']:.2f}"
                 f"\n      eta_P,LHV={100*eta:.1f}% eta_HHV(partial)={100*eta_hhv:.1f}% "
                 f"f_el={p/(p+f_ch4*HHV['CH4']):.2f}")
    print(line)

# C005 check of author's energy-CH4 feedstock consumption yield (Table 3, 6.5 kW, 50% CH4, 2 kg/h)
print("\nC005 Table 3 check: EY / (CH4 feed, kNL/h)")
for tot, val in ((3, 17.6), (6, 9.8), (9, 6.1), (12, 4.9)):
    print(f"  {tot} kNL/h: author {val} -> implied EY {val*tot*0.5:.1f} g/kWh")
