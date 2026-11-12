"""Reviewer calculations for SRC021 (Bryssinck et al. 2025, React. Chem. Eng. 10, 1910-1923).

Run: python3 calculations.py
Authors: Vm 24.06 L/mol (E007), plug power (E006), EC in MWh per tonne CO (E007).
Basis per mol CO2 fed. Formation enthalpies (298 K): CO2 -393.5, CO -110.5 kJ/mol.
"""

VM = 24.06
M_CO, M_CO2 = 28.01, 44.01
KWH_NM3 = 3.6e3 / (1000.0 / 22.414)       # kJ/mol per kWh/Nm3 (Nm3 at 0 C)


def outlet(y_co, y_o2=0.0):
    """Outlet per mol CO2 fed from dry CO and O2 fractions (CO2 by difference), O balance."""
    y_co2 = 1 - y_co - y_o2
    q = 2.0 / (2 * (y_co2 + y_o2) + y_co)
    n_co2, n_co = y_co2 * q, y_co * q
    return 1 - n_co2, n_co, n_co2 + n_co - 1.0     # X, CO out, carbon consumed


def run():
    # C001: EC check and CO per CO2 fed for reported (Q, P, X, EC) points
    pts = {
        "OP001 benchmark 70 L/min": (70, 8.5, 0.064, 13.5),   # Fig. 6 readings (E011)
        "OP002 bed pos.1 70 L/min": (70, 8.5, 0.156, 5.6),    # text 16%, Fig. 6 15.6% (E011)
        "OP003 semi-cont. 50 L/min": (50, 8.1, 0.20, 5.8),    # E014
        "OP004 recycle 50 L/min": (50, 9.5, 0.127, 13.7),     # E013 (X on total inlet)
        "bed 90 L/min": (90, 9.0, 0.12, 7.0),                 # E012
        "bed 110 L/min": (110, 9.5, 0.08, 11.0),              # E012
    }
    for name, (q, p, x, ec_rep) in pts.items():
        f = q / VM                                   # mol/min CO2 at inlet
        co_from_ec = p / ec_rep * 1000 / M_CO / 60   # mol/min CO implied by reported EC
        ec_if_co_eq_x = p / (x * f * M_CO * 60 / 1e6) / 1000   # MWh/t if CO = X*F (no carbon)
        ec_if_co_eq_2x = ec_if_co_eq_x / 2                     # MWh/t if CO = 2X*F (CO2 + C -> 2CO)
        sei = p * 60 / f                              # kJ/mol CO2 at inlet (plug)
        cr = q * x * 60 * M_CO2 / VM
        print(f"C001 {name}: F {f:.3f} mol/min | SEI {sei:.0f} kJ/mol | CR {cr:.0f} g/h | "
              f"CO implied by EC {co_from_ec:.3f} mol/min = {co_from_ec/(x*f):.2f} x converted CO2 | "
              f"EC if CO=X {ec_if_co_eq_x:.1f}, if CO=2X {ec_if_co_eq_2x:.1f} MWh/t (reported {ec_rep})")

    # C002: benchmark consistency: CO 12% without carbon (stoichiometric O2 = CO/2)
    x_st, co_st, c_st = outlet(0.12, 0.06)
    x_o0, co_o0, c_o0 = outlet(0.12, 0.0)
    print(f"C002 benchmark CO 12%: with O2 = 6% (no carbon) X {x_st*100:.1f}%; "
          f"with O2 = 0 X {x_o0*100:.1f}% and carbon/O sink {c_o0:.3f} mol/mol (reported X 6.4%)")

    # C003: best point balance (CO 33%, O2 <1%), per mol CO2 fed
    for yo2 in (0.0, 0.01):
        x, co, c = outlet(0.33, yo2)
        print(f"C003 OP003 CO 33%, O2 {yo2*100:.0f}%: X {x*100:.1f}% | CO {co:.3f} | C consumed {c:.3f} "
              f"mol/mol CO2 fed | C per CO {c/co:.2f}")
    x, co, c = outlet(0.33, 0.0)
    f = 50 / VM
    p = 8.1
    sei = p * 60 / f
    ec_co = sei / co                                 # kJ/mol CO (plug)
    dh = co * (-110.5) + (1 - x) * (-393.5) - (-393.5)
    print(f"C004 OP003: EC_CO {ec_co:.0f} kJ/mol = {ec_co/KWH_NM3:.2f} kWh/Nm3 CO (plug) | "
          f"carbon {c/co*12.011/22.414:.3f} kg/Nm3 CO | carbon feed {c*f*12.011*60:.0f} g/h | "
          f"eta (overall dH incl. C, plug) {dh/sei*100:.1f}% | (283*X/SEI) {283*x/sei*100:.1f}%")
    for e in (0.6, 0.8, 0.83):
        print(f"    plasma basis (x{e}): EC_CO {ec_co*e/KWH_NM3:.2f} kWh/Nm3; eta overall {dh/(sei*e)*100:.1f}%")
    # C005: authors' plasma-based EC 4.8 vs plug 5.8 -> implied supply efficiency
    print(f"C005 implied plug-to-plasma ratio 4.8/5.8 = {4.8/5.8:.2f} (text: plasma generally 60-80% of plug)")
    # C006: recirculation CO output (from EC and power)
    for lab, p, ec in (("before recycle", 8.5, 10.9), ("with recycle", 9.5, 13.7)):
        print(f"C006 {lab}: CO out {p/ec*1000/M_CO/60:.3f} mol/min")


if __name__ == "__main__":
    run()
