"""Reviewer calculations SRC014-C001 to C005 for Kwon, Kim & Song (2023).

Feed: total 24 SLPM = 12 SLPM N2 + 12 SLPM CH4+CO2 at the stated CH4/CO2 ratio
(SRC014-E004). SLPM reference state not stated: 0 degC (22.414 L/mol) used as the
main case, 20 degC (24.055 L/mol) printed for comparison.
Power: P = SEI x 24 SLPM / 60, SEI from measured V x I (E002, E011).
Run with: python3 calculations.py
"""

VMS = {"0 degC": 22.414, "20 degC": 24.055}   # 0 degC reproduces author eta (C003)
M_H2 = 2.016
LHV = {"H2": 241.8, "CO": 283.0, "CH4": 802.3}   # kJ/mol
HHV = {"H2": 285.8, "CO": 283.0, "CH4": 890.6}
EV = 96.485
FT = 24.0                                         # SLPM total (E004)

# OP: (CH4 SLPM, CO2 SLPM, SEI kJ/L, X_CH4 %, X_CO2 %, Y_H2 H-based % or None,
#      H2/CO or None, author eta %, author total conversion %, author conversion cost kJ/L)
OPS = {
    # E011 Table 1 SEI; E013 Fig. 9 bars at 4.2 (NQ ~52.0/40.6); E015 Y_H2 43.6 / 1.034 = 42.2 (the reported +3.4% is relative, as the H2O
    # change 13.9 -> 8.6% is stated as -38%);
    # E011 H2/CO NQ 0.91; E016 eta NQ ~54.3 (Fig. 11b); E013 Xtot NQ 22.4; E012 conv. cost 18.7
    "OP001 5/7 SEI 4.2 not quenched": (5, 7, 4.18, 52.0, 40.6, 42.2, 0.91, 54.3, 22.4, 18.7),
    # E011 Table 1 X 51.1/40.2, H2/CO 0.95; E015 Y_H2 43.6; E012 eta 55.3, Xtot 21.9, cost 19.1
    "OP002 5/7 SEI 4.2 quenched": (5, 7, 4.18, 51.1, 40.2, 43.6, 0.95, 55.3, 21.9, 19.1),
    # E011 Table 1 X 50.5/40.3, H2/CO 1.26; E014 Y_H2 44.0; E012 eta 53.2; E013 Xtot Q 22.5; cost 18.5
    "OP003 1/1 SEI 4.2 quenched": (6, 6, 4.17, 50.5, 40.3, 44.0, 1.26, 53.2, 22.5, 18.5),
    # E013 Fig. 9 bars at 2.3 (Q ~26.1/20.0), Xtot 11.1; E016 eta Q ~51.5, cost ~20.4 (Fig. 11)
    "OP004 5/7 SEI 2.3 quenched": (5, 7, 2.3, 26.1, 20.0, None, None, 51.5, 11.1, 20.4),
}

for label, vm in VMS.items():
    print(f"\n=== SLPM at {label} ({vm} L/mol) ===")
    for op, (ch4, co2, sei, xch4, xco2, yh2, h2co, eta_a, xtot_a, cc_a) in OPS.items():
        p = sei * FT / 60                           # kW
        f = lambda slpm: slpm / vm / 60             # mol/s
        f_ch4 = f(ch4)
        c_ch4 = f_ch4 * xch4 / 100
        c_co2 = f(co2) * xco2 / 100
        # C001 author total conversion and conversion cost from nominal feed
        xtot = (ch4 * xch4 + co2 * xco2) / FT
        line = (f"{op}: P={p:.3f} kW | C001 Xtot(nominal feed)={xtot:.1f}% (author {xtot_a}); "
                f"SEI/Xtot={sei/xtot*100:.1f} kJ/L (author {cc_a})\n"
                f"   C002 SEI_CH4={p/f_ch4:.0f} EC_CH4={p/c_ch4:.0f} kJ/mol; "
                f"per CH4+CO2 conv {p/(c_ch4+c_co2):.0f} kJ/mol = {p/(c_ch4+c_co2)/EV:.2f} eV")
        if yh2 is not None:
            # C003 H2 from H-based yield (H atoms in H2 / H atoms in CH4 fed); CO from H2/CO
            h2 = yh2 / 100 * 2 * f_ch4
            co = h2 / h2co
            eta = (h2 * LHV["H2"] + co * LHV["CO"]) / (p + c_ch4 * LHV["CH4"])
            eta_hhv = (h2 * HHV["H2"] + co * HHV["CO"]) / (p + f_ch4 * HHV["CH4"])
            line += (f"\n   C003 H2={h2*vm*60:.2f} SLPM CO={co*vm*60:.2f} SLPM (S_CO,C={co/(c_ch4+c_co2)*100:.0f}%) "
                     f"EC_H2={p/h2:.0f} kJ/mol EY_H2={h2*M_H2*3600/p:.1f} g/kWh "
                     f"eta_P,LHV={100*eta:.1f}% (author eta {eta_a}, same definition)"
                     f"\n   C004 eta_HHV(partial)={100*eta_hhv:.1f}% f_el={p/(p+f_ch4*HHV['CH4']):.2f}")
        else:
            line += f"\n   C003 not calculable (H2 yield not reported at this SEI); author eta {eta_a}% (Fig. 11b)"
        print(line)

# C005 N2 sensible heat share (context): heating 12 SLPM N2 to the measured pre-quench TC1
# temperature (~536 degC, OP001) is a lower bound on heat carried by the diluent
cp_n2 = 29.1e-3  # kJ/mol/K, approximate mean
q = 12 / 22.414 / 60 * cp_n2 * (536 - 20)
print(f"\nC005 N2 sensible heat to 536 degC ~{q*1000:.0f} W ({100*q/1.672:.0f}% of P); "
      "indicative, TC1 is off-axis and not the gas temperature")
