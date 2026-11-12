"""Reviewer calculations for SRC020 (O'Modhrain et al. 2024, ACS Eng. Au 4, 333-344).

Run: python3 calculations.py
Authors' molar volume 23.6 L/mol (17 degC, flow meter calibration; E007). Power = plug
power from a three-phase meter (E006). Plasma power estimated with the measured PSU
efficiency 0.77-0.83 (E010). dH 283 kJ/mol.
"""

VM = 23.6
DH = 283.0
KWH_NM3 = 3.6e3 / (1000.0 / 22.414)   # kJ/mol per kWh/Nm3 (Nm3 at 0 C)

# OP: flow (L/min), plug power (kW), conversion (fraction)
OPS = {
    "OP001": (80, 7.1, 0.087),      # 5 reactors (E011)
    "OP002": (60, 4.3, 0.076),      # 3 reactors; P from ESI (E013); X from CR 510 g/h (E012), C002
    "OP003": (80, 1.48, 0.021),     # 1 central reactor; Fig. 3a at 80 L/min (E014): P ~1.48 kW, X ~2.1%
}


def run():
    # C002: back out X and P from reported SEI (kJ/L) and conversion rate (g/h)
    for label, q, sei, cr in [("OP002", 60, 4.2, 510), ("OP003", 80, 1.4, 187)]:
        x = cr * VM / (q * 60 * 44)
        p = sei * q / 60
        print(f"C002 {label}: X = CR*Vm/(Q*60*44) = {x*100:.2f}% ; P = SEI*Q/60 = {p:.2f} kW")
    print("C002 note: text pairs 23% with SEI 1.4 kJ/L; X from CR at 1.4 kJ/L gives 17.9%; Fig. 3a power gives SEI 1.11 kJ/L")
    for op, (q, p, x) in OPS.items():
        f = q / VM / 60.0                         # mol/s
        sei_l = p * 60 / q                        # kJ/L
        sei = p / f                               # kJ/mol (plug)
        eta = x * DH / sei * 100                  # C001
        ec = sei / x                              # kJ/mol CO2 converted (plug)
        cr = q * x * 60 * 44 / VM
        print(f"C001 {op}: F {f*60:.3f} mol/min | SEI {sei_l:.2f} kJ/L = {sei:.0f} kJ/mol ({sei/96.485:.2f} eV) | "
              f"eta_plug {eta:.1f}% | EC_plug {ec/1000:.2f} MJ/mol = {ec/KWH_NM3:.1f} kWh/Nm3 CO | CR {cr:.0f} g/h")
        for e_psu in (0.77, 0.80, 0.83):          # C003 plasma-basis estimate
            print(f"    PSU eff {e_psu}: eta_plasma {eta/e_psu:.1f}% | EC_plasma {ec*e_psu/1000:.2f} MJ/mol "
                  f"= {ec*e_psu/KWH_NM3:.1f} kWh/Nm3")


if __name__ == "__main__":
    run()
