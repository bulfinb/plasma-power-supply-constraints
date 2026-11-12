"""Reviewer calculations for SRC018 (Bongers et al. 2017, Plasma Process. Polym. 14, e1600126).

Run: python3 calculations.py
Flows in slm; reference conditions not stated. 0 degC (22.414 L/mol) reproduces the
authors' SEI values (C001), so it is used. Power = "MW power" (boundary see E003).
dH = 2.9 eV/molecule (authors, E006); review reference 2.93 eV.
"""

VM = 22.414
EV = 96.485
DH = 2.9
KWH_NM3 = 3.6e3 / (1000.0 / VM)   # 80.69 kJ/mol per kWh/Nm3

# OP: slm, P (W), alpha (fraction), reported SEI (eV), reported eta (%)
OPS = {
    "OP001": (11, 8100, 0.83, 10.3, 24),     # E009, Fig. 3a
    "OP002": (11, 3100, 0.47, 3.9, 35),      # E009, Fig. 3a
    "OP003": (75, 3100, 0.10, 0.6, 51),      # E010 (alpha 11 text; ~9.8 Fig. 3b)
    "OP004": (75, 10000, 0.225, 1.9, 36),    # E010/E011: Fig. 3b (text eta 40, alpha 23)
    "OP005": (None, None, 0.125, 0.8, 46.5), # E013, Fig. 7, Exp. 7 (RV, ~600 mbar)
}


def run():
    for op, (slm, p, a, sei_rep, eta_rep) in OPS.items():
        if slm:
            f = slm / VM / 60.0
            sei = p / f / 1000.0
        else:
            sei = sei_rep * EV
        eta = a * DH * EV / sei * 100
        ec = sei / a
        print(f"{op}: SEI {sei:.0f} kJ/mol = {sei/EV:.2f} eV (reported {sei_rep}) | eta = a*2.9/SEI "
              f"{eta:.1f}% (reported {eta_rep}) | EC_CO2 {ec:.0f} kJ/mol = {ec/KWH_NM3:.1f} kWh/Nm3 CO "
              f"(MW power basis; sub-atmospheric, pump excluded)" + (f" | F_CO2 {f*60:.3f} mol/min" if slm else ""))
    # C003: OP004 text pair check (eta 40 with alpha 23 at 1.9 eV)
    print(f"C003 text pair OP004: 0.23*2.9/1.86 = {0.23*2.9/1.86*100:.1f}% vs text 40%, Fig. 3b ~36%")
    # C004: the 2.45 GHz SEI 0.9 eV at 1 kW, 14 slm (E012)
    print(f"C004 1 kW / 14 slm = {1000/(14/VM/60)/1000/EV:.2f} eV (stated 0.9)")


if __name__ == "__main__":
    run()
