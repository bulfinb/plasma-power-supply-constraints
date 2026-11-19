"""Reviewer calculations for SRC019 (Girard-Sahun et al. 2022, Chem. Eng. J. 442, 136268).

Run: python3 calculations.py
Basis: 1 mol CO2 fed. Inlet 10 Ln/min CO2 (E005); SEI 3.2 kJ/L (E010).
The authors convert SEI to kJ/mol with Vm = 24.5 L/mol (E009); if 'Ln' means 0 degC,
22.414 L/mol applies. Both are shown.
Standard enthalpies of formation (kJ/mol, 298 K): CO2 -393.5, CO -110.5, O2 0, C(s) 0.
C004 (revised 2026-11-19, workflow 1.1): eta_LHV = LHV of CO out / (electricity + LHV of carbon consumed),
LHV_CO 283.0 kJ/mol, LHV_C 393.5 kJ/mol (graphite). Replaces the efficiency on the overall reaction enthalpy.
"""

HF = {"CO2": -393.5, "CO": -110.5, "O2": 0.0, "C": 0.0}
KWH_NM3 = 3.6e3 / (1000.0 / 22.414)    # 80.69 kJ/mol per kWh/Nm3
LHV_CO, LHV_C = 283.0, 393.5           # kJ/mol


def balance(y_co2, y_co, y_o2):
    """Outlet per mol CO2 fed from dry outlet mole fractions, using the O balance
    (authors' Eq. 5): Q_out/Q_in = 2 / (2 y_CO2 + 2 y_O2 + y_CO).
    NOTE: Eq. (5) in the paper writes [O2] with coefficient 1; O atoms in O2 count 2.
    Both versions are returned."""
    out = {}
    for label, k_o2 in (("O-balance (2*O2)", 2.0), ("authors' Eq. 5 (1*O2)", 1.0)):
        q = 2.0 / (2 * y_co2 + k_o2 * y_o2 + y_co)
        n_co2, n_co, n_o2 = y_co2 * q, y_co * q, y_o2 * q
        x = 1 - n_co2
        c_consumed = n_co2 + n_co - 1.0             # carbon balance: C from the bed
        dh = (n_co * HF["CO"] + n_co2 * HF["CO2"]) - HF["CO2"]   # kJ per mol CO2 fed
        out[label] = dict(q=q, x=x, n_co=n_co, n_o2=n_o2, c=c_consumed, dh=dh)
    return out


CASES = {
    # benchmark, no bed: Fig. 3 / Fig. 5A text (E011): CO 7.2%, O2 3.6% (Fig. 3: 3.7), CO2 balance
    "benchmark (no bed)": (1 - 0.072 - 0.036, 0.072, 0.036),
    # with bed, maximum (Fig. 3, charcoal 1, E012): CO 21.9%, O2 0.2%
    "bed, maximum (Fig. 3)": (1 - 0.219 - 0.002, 0.219, 0.002),
    # with bed, after 14 min (Fig. 5B reading, E014): CO2 ~90%, CO ~9.7%, O2 ~0.5%
    "bed, 14 min (Fig. 5B)": (0.898, 0.097, 0.005),
}


def run():
    p_kw = 3.2 * 10 / 60.0
    print(f"C001 plasma power = 3.2 kJ/L x 10 L/min / 60 = {p_kw:.3f} kW")
    for vm in (24.5, 22.414):
        sei = 3.2 * vm
        print(f"C001 SEI = {sei:.1f} kJ/mol CO2 at Vm {vm} L/mol ({sei/96.485:.3f} eV)")
    for name, (y2, y1, yo) in CASES.items():
        res = balance(y2, y1, yo)
        r = res["O-balance (2*O2)"]
        ra = res["authors' Eq. 5 (1*O2)"]
        line = (f"C002/C003 {name}: X_CO2 {r['x']*100:.1f}% (authors' Eq.5: {ra['x']*100:.1f}%) | "
                f"CO out {r['n_co']:.3f} mol/mol CO2 fed | C consumed {r['c']:.3f} | dH {r['dh']:.1f} kJ/mol CO2 fed")
        print(line)
        for vm in (24.5, 22.414):
            sei = 3.2 * vm
            eta_auth = r["x"] * 283 / sei * 100              # authors' definition (283 x X / SEI)
            eta_lhv = r["n_co"] * LHV_CO / (sei + max(r["c"], 0.0) * LHV_C) * 100   # C004: eta_LHV, carbon counted
            ec_co = sei / r["n_co"]                           # C005: electricity per mol CO (plasma)
            c_per_co = r["c"] / r["n_co"]
            print(f"    Vm {vm}: eta (283*X/SEI) {eta_auth:.1f}% | eta_LHV (C counted) {eta_lhv:.1f}% | "
                  f"EC_CO {ec_co:.0f} kJ/mol = {ec_co/KWH_NM3:.2f} kWh/Nm3 | C {c_per_co:.2f} mol/mol CO "
                  f"= {c_per_co*12/22.414:.3f} kg C/Nm3 CO, LHV {c_per_co*393.5/KWH_NM3:.2f} kWh/Nm3 CO")


if __name__ == "__main__":
    run()
