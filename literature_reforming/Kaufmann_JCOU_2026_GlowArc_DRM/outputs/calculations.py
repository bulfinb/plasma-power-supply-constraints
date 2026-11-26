"""Reviewer calculations for SRC027 (Kaufmann et al. 2026, J. CO2 Util. 105, 103347).

Run: ~/.venvs/science/bin/python calculations.py
Flow 6 SLM total (E007); SLM reference not stated. Main basis 22.414 L/mol (0 degC, 1 atm), which reproduces
the authors' EC range (C003); results also printed at 24.46 L/mol (25 degC) for the sensitivity (workflow sec. 4).
Powers: plasma (V x I at the reactor, E004-E005) and supply = DC supply output feeding the plasma driver (E005-E006).
"""

VM, VM_ALT = 22.414, 24.46
EV = 96.485                     # kJ/mol per eV/molecule
FLOW_L_S = 6.0 / 60.0           # 6 SLM -> L/s

# E011: text endpoints of the SEI range, supply (plasma) kJ/L
END = [(5.7, 5.1), (15.9, 14.3)]
RATIO = sum(p / s for s, p in END) / len(END)

# Selected operating points. SEI_supply from Fig. 13b diamonds (E013, E015) or text (E011, OP002);
# conversions from Fig. 13b bars (E013-E015), +-1 percentage point reading precision.
OPS = {
    # key: (x_CH4_in, SEI_supply kJ/L, SEI_plasma kJ/L or None, X_CH4, X_CO2, eta_BGs supply basis, S_C,CO)
    "OP001 50/50, 20 mm, 0.24 A": (0.5, 6.0, None, 0.42, 0.385, 0.57, 0.81),
    "OP002 50/50, 40 mm, 0.4 A": (0.5, 15.9, 14.3, 0.66, 0.70, 0.445, 0.81),
    "OP003 60/40, 40 mm, 0.4 A": (0.4, 12.3, None, 0.525, 0.56, 0.525, 0.93),
}

# Fig. 13a points (E012): (mixture, SEI_supply, X_tot) used for the C003 check of the authors' EC range
FIG13A = [("50/50", 5.9, 0.265), ("50/50", 6.0, 0.403), ("50/50", 8.6, 0.433), ("50/50", 9.4, 0.444),
          ("50/50", 15.9, 0.68), ("60/40", 5.2, 0.32), ("60/40", 5.7, 0.323), ("60/40", 6.5, 0.405),
          ("60/40", 7.6, 0.462), ("60/40", 12.3, 0.547)]


def run():
    print(f"C001 SEI_plasma / SEI_supply from text endpoints: "
          + ", ".join(f"{p}/{s} = {p/s:.3f}" for s, p in END) + f"; mean {RATIO:.3f}")
    print("C002 per OP (power basis, no external heat):")
    for name, (xin, sei_s, sei_p, xch4, xco2, eta, sc) in OPS.items():
        if sei_p is None:
            sei_p = sei_s * RATIO
        xtot = (1 - xin) * xco2 + xin * xch4
        for vm, lab in ((VM, "22.414"), (VM_ALT, "24.46")):
            seich4_p = sei_p * vm / xin
            seich4_s = sei_s * vm / xin
            print(f"  {name} [{lab} L/mol]: SEI_P {sei_p:.2f} kJ/L | X_tot {xtot*100:.1f}% | "
                  f"SEI_CH4 {seich4_p:.0f} (plasma) / {seich4_s:.0f} (supply) kJ/mol | "
                  f"EC_CH4 {seich4_p/xch4:.0f} (plasma) / {seich4_s/xch4:.0f} (supply) kJ/mol | "
                  f"EC_tot {sei_p*vm/xtot/EV:.2f} eV/molecule (plasma)")
        print(f"  {name}: P from SEI x 6 SLM = {sei_p*FLOW_L_S*1000:.0f} W plasma, "
              f"{sei_s*FLOW_L_S*1000:.0f} W supply; CH4 feed {6.0*xin/VM:.4f} mol/min "
              f"({6.0*xin/VM_ALT:.4f} at 24.46)")
    print("C003 author EC range check (EC = SEI_P x Vm / X_tot; authors 3.3-4.7 eV, E016):")
    for vm in (VM, VM_ALT):
        ecs = [s * RATIO * vm / x / EV for _, s, x in FIG13A]
        print(f"  Vm {vm}: {min(ecs):.2f}-{max(ecs):.2f} eV/molecule over the Fig. 13a points")
    print(f"C004 OP002 power: SEI 14.3 kJ/L x 0.1 L/s = {14.3*FLOW_L_S*1000:.0f} W plasma, "
          f"15.9 x 0.1 = {15.9*FLOW_L_S*1000:.0f} W supply; text: highest efficiency at PP = 1660 W (40 mm) and "
          f"supply up to 1750 W (E006) -> ~14% / ~9% above the SEI-implied values")


if __name__ == "__main__":
    run()
