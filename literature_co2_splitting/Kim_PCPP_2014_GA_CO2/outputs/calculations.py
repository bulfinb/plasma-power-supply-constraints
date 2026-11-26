"""Reviewer calculations for SRC028 (Kim, Lim & Chun 2014, Plasma Chem. Plasma Process. 34, 125-143).

Run: python3 calculations.py
Case 1 (pure CO2) only. P = 0.6 kW "plasma input power" for all points (E004).
Flows in L/min, reference conditions not stated; 22.414 L/mol (0 degC) used (workflow 4),
24.465 L/mol (25 degC) as sensitivity. The authors give no energy value in molar units
to reproduce (EDE is in L/min/W, independent of molar volume).
Fig. 2 values read by eye from the embedded 150 ppi image (E011, E012): +/-0.3 points
for conversion and concentrations, +/-1 point for CO selectivity.
dH = 283 kJ/mol (review reference).
"""

VM = 22.414
VM25 = 24.465
DH = 283.0
P = 600.0                      # W, E004
KWH_NM3 = 3.6e3 / (1000.0 / VM)  # 80.69 kJ/mol per kWh/Nm3

# CO2 feed (L/min): (CR reported, %; EDE, L/min/W; y_CO2, y_CO, y_O2 dry outlet, %)
# Fig. 2a (E011) and Fig. 2b (E012)
FIG2 = {
    6:  (5.4, 0.00054, 94.5, 2.6, 0.8),
    8:  (7.3, 0.00097, 92.3, 4.0, 1.3),
    10: (9.5, 0.00159, 90.0, 5.6, 1.9),
    12: (11.4, 0.00228, 88.2, 6.8, 2.5),
    14: (12.4, 0.00290, 87.3, 7.4, 2.8),   # OP001: text 12.3% at 14 L/min (E013)
    15: (12.3, 0.00308, 87.4, 7.1, 2.9),
    17: (12.2, 0.00346, 87.6, 6.9, 2.8),
    20: (10.3, 0.00347, 89.2, 6.1, 2.5),   # OP002: best carbon-based efficiency
    24: (7.9, 0.00318, 91.8, 4.4, 1.7),
    28: (6.3, 0.00296, 92.9, 3.7, 1.2),
    32: (5.0, 0.00267, 94.3, 2.8, 0.8),
}
OPS = {"OP001": 14, "OP002": 20}


def metrics(lpm, x, vm=VM):
    f = lpm / vm / 60.0                 # mol/s CO2 fed
    sei = P / f / 1000.0                # kJ/mol CO2
    return sei, (x * DH / sei * 100 if x else None), (sei / x if x else None)


def run():
    print("C001 EDE check: EDE = CR x F / P; C002 carbon-based X = y_CO/(y_CO + y_CO2); "
          "C003 SEI, eta, EC (22.414 L/mol)")
    print(" F   CR_rep  EDE_rep EDE_calc | sum_dry O2/CO | X_C   X_exp | SEI   eta_rep eta_C | EC_CO (kJ/mol, kWh/Nm3)")
    for lpm, (cr, ede, yco2, yco, yo2) in FIG2.items():
        ede_c = cr / 100 * lpm / P
        xc = yco / (yco + yco2)                      # C002, no solid carbon assumed
        y = yco2 / 100
        xexp = (1 - y) / (1 + y / 2)                 # C004, CO2/CO/O2 only, from y_CO2
        sei, eta_rep, _ = metrics(lpm, cr / 100)
        _, eta_c, ec = metrics(lpm, xc)
        print(f"{lpm:3d} {cr:5.1f}  {ede:.5f} {ede_c:.5f} | {yco2+yco+yo2:5.1f} {yo2/yco:5.2f} | "
              f"{xc*100:4.1f} {xexp*100:5.1f} | {sei:5.1f} {eta_rep:5.1f} {eta_c:5.1f} | {ec:5.0f} {ec/KWH_NM3:5.2f}")
    print()
    for op, lpm in OPS.items():
        cr, ede, yco2, yco, yo2 = FIG2[lpm]
        xc = yco / (yco + yco2)
        sei, eta_rep, ec_rep = metrics(lpm, cr / 100)
        _, eta_c, ec_c = metrics(lpm, xc)
        sei25, _, ec25 = metrics(lpm, xc, VM25)
        print(f"{op} ({lpm} L/min): F_CO2 {lpm/VM:.3f} mol/min; SEI {sei:.1f} kJ/mol = {sei/96.485:.3f} eV "
              f"(25 C: {sei25:.1f})")
        print(f"  reported CR {cr}%: eta {eta_rep:.1f}%, EC_CO2 {ec_rep:.0f} kJ/mol "
              f"(= 1.345/EDE: {VM*60/1000/ede:.0f})")
        print(f"  carbon-based X {xc*100:.1f}%: eta {eta_c:.1f}%, EC_CO2 = EC_CO {ec_c:.0f} kJ/mol = "
              f"{ec_c/KWH_NM3:.2f} kWh/Nm3 CO (25 C: {ec25:.0f} kJ/mol)")
        print(f"  CO selectivity implied y_CO/CR = {yco/cr*100:.0f}%; O2/CO {yo2/yco:.2f} (0.5 expected); "
              f"dry sum {yco2+yco+yo2:.1f}%")


if __name__ == "__main__":
    run()
