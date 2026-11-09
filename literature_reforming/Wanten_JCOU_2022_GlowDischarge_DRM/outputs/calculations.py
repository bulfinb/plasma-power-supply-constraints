"""Reviewer calculations SRC015-C001 to C006 for Wanten et al. (2022), confined APGD DRM.

Flows in L/min with the authors' molar volume 24.05 L/mol ("normal conditions",
~20 degC; SRC015-E007), which reproduces their eV/molecule values. If the MFC
litres are at 0 degC (22.414 L/mol) all per-mol energies fall by ~7% (printed).
Plasma power P = SEI x flow (SEI read from Fig. 4 right axis, checked against
EC x X_tot). The plasma-power method is not stated; the DC supply drives the
plasma through a 300 kOhm series ballast resistor (E003), whose I^2 R loss is
computed in C005.
Run with: python3 calculations.py
"""

EV = 96.485                     # kJ/mol per eV/molecule
LHV = {"H2": 241.8, "CO": 283.0, "CH4": 802.3}
HHV = {"H2": 285.8, "CO": 283.0, "CH4": 890.6}
M_H2 = 2.016
R_BALLAST = 300e3               # ohm (E003)

# OP: (CH4 frac, I mA, Q L/min, X_CO2 %, X_CH4 %, X_tot author %, EC author kJ/L,
#      SEI kJ/L, H2/CO, S_CO C-based fraction)
OPS = {
    # Fig. 3a/b, 4a, 6a (E010, E012, E016); S_CO,C 95-100% (E017) -> 0.97 used
    "OP001 25% 25 mA 1.0 L/min": (0.25, 25, 1.0, 45.5, 73.0, 52, 13.7, 7.1, 0.36, 0.97),
    # Text: X_tot 62+-1, EC 13.9+-0.4 kJ/L, 3.5 eV (E013); X Fig. 3a; H2/CO Fig. 6a/c
    "OP002 25% 35 mA 1.0 L/min": (0.25, 35, 1.0, 55.1, 85.3, 62, 13.9, 8.6, 0.33, 0.97),
    # Text: X_CO2 63.7+-0.4, X_CH4 94.28+-0.07, X_tot 71+-3 (E011); EC Fig. 4b; Fig. 7b S_CO,C ~0.95
    "OP003 25% 25 mA 0.5 L/min": (0.25, 25, 0.5, 63.7, 94.28, 71, 16.0, 11.7, 0.31, 0.95),
    # Text: X_tot 74+-3, EC 17+-1 kJ/L, 4.2 eV (E013); H2/CO 0.60+-0.01 (E016); Fig. 7c S_CO,C ~0.95
    "OP004 35% 25 mA 0.5 L/min": (0.35, 25, 0.5, 66.4, 86.8, 74, 17.0, 12.5, 0.60, 0.95),
    # Fig. 3b, 4b, 6b
    "OP005 25% 25 mA 2.0 L/min": (0.25, 25, 2.0, 19.6, 36.3, 23.8, 14.0, 3.4, 0.475, 0.97),
    # Fig. 3c, 4c; H2/CO 0.628+-0.009 (E016)
    "OP006 35% 35 mA 1.0 L/min": (0.35, 35, 1.0, 54.8, 73.5, 61, 14.2, 8.7, 0.628, 0.97),
}
# Fig. 7 H-based H2 yields at 25 mA, 0.5 L/min, for the C003 cross-check (E018)
Y_H2_FIG7 = {"OP003 25% 25 mA 0.5 L/min": 42, "OP004 35% 25 mA 0.5 L/min": 60}

for label, vm in {"24.05 L/mol (author)": 24.05, "22.414 L/mol (0 degC)": 22.414}.items():
    print(f"\n=== Molar volume {label} ===")
    for op, (fch4, i_ma, q, xco2, xch4, xtot_a, ec_a, sei, h2co, sco) in OPS.items():
        p = sei * q / 60                                    # kW
        f_tot = q / vm / 60                                 # mol/s
        f_ch4, f_co2 = f_tot * fch4, f_tot * (1 - fch4)
        c_ch4, c_co2 = f_ch4 * xch4 / 100, f_co2 * xco2 / 100
        xtot = fch4 * xch4 + (1 - fch4) * xco2
        # C001 consistency: X_tot and SEI vs EC x X_tot
        out = (f"{op}: P={p*1000:.0f} W | C001 X_tot={xtot:.1f}% (author {xtot_a}); "
               f"EC_a x X_tot={ec_a*xtot_a/100:.2f} vs SEI read {sei} kJ/L")
        # C002 EC_CH4 and per-molecule cost
        ec_mol = p / (c_ch4 + c_co2)
        out += (f"\n   C002 SEI_CH4={p/f_ch4:.0f} EC_CH4={p/c_ch4:.0f} kJ/mol; "
                f"per CH4+CO2 conv {ec_mol:.0f} kJ/mol = {ec_mol/EV:.2f} eV")
        # C003 products: CO = S_CO,C x C converted; H2 = H2/CO x CO
        co = sco * (c_ch4 + c_co2)
        h2 = h2co * co
        y_h2 = h2 / (2 * f_ch4) * 100
        eta = (h2 * LHV["H2"] + co * LHV["CO"]) / (p + c_ch4 * LHV["CH4"])
        out += (f"\n   C003 Y_H2(H-based)={y_h2:.0f}%"
                + (f" (Fig. 7 {Y_H2_FIG7[op]}%)" if op in Y_H2_FIG7 else "")
                + f" EC_H2={p/h2:.0f} kJ/mol EY_H2={h2*M_H2*3600/p:.1f} g/kWh eta_P,LHV={100*eta:.1f}%")
        # C004 partial eta_HHV
        eta_hhv = (h2 * HHV["H2"] + co * HHV["CO"]) / (p + f_ch4 * HHV["CH4"])
        out += f"\n   C004 eta_HHV(partial)={100*eta_hhv:.1f}% f_el={p/(p+f_ch4*HHV['CH4']):.2f}"
        # C005 ballast loss and supply-output basis
        i = i_ma / 1000
        p_bal = i**2 * R_BALLAST / 1000                       # kW
        v_pl, v_bal = p * 1000 / i, i * R_BALLAST
        share = p / (p + p_bal)
        out += (f"\n   C005 V_plasma={v_pl/1000:.1f} kV, ballast drop {v_bal/1000:.1f} kV, supply ~{(v_pl+v_bal)/1000:.1f} kV; "
                f"ballast {p_bal*1000:.0f} W; plasma share of supply output {100*share:.0f}%; "
                f"EC_CH4 at supply output {p/share/c_ch4:.0f} kJ/mol")
        print(out)

# C006 thermodynamic reference: DRM 247 kJ/mol = 2.56 eV/molecule (E009)
print(f"\nC006 DRM enthalpy 247 kJ/mol = {247/EV:.2f} eV per molecule of CH4+CO2 pair; "
      f"per reactant molecule converted {247/2/EV:.2f} eV")
