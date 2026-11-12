"""Reviewer calculations for SRC023 (Yong et al. 2023, Plasma Sources Sci. Technol. 32, 115012).

Run: python3 calculations.py
Batch reactor: N0 = P0 V / (Z R T0); E_tot = E_pulse x f x tau (E009); SEI = E_tot / N0;
eta = Phi x dH / SEI with dH = 2.9 eV (E010). Chamber volume 400 cm3, reduced to 200 cm3 with
resin "as needed for the case of higher pressures" (E003): which volume applies to each data
set is not stated, so both are shown. Z for CO2 at 300 K: ~0.975 (5 bar), ~0.97 (5.8 bar),
~0.955 (9 bar) - reviewer approximations (virial estimate), +/-1%.
"""

R, T0, F = 8.314, 300.0, 30e3
EV = 96.485
DH = 2.9 * EV
KWH_NM3 = 3.6e3 / (1000.0 / 22.414)


def eta(p_bar, z, e_uj, tau, phi, v_cm3):
    n0 = p_bar * 1e5 * v_cm3 * 1e-6 / (z * R * T0)
    e_tot = e_uj * 1e-6 * F * tau
    sei = e_tot / n0 / 1000.0          # kJ/mol
    return n0, e_tot, sei, phi * DH / sei


def run():
    cases = [
        ("OP001 best conversion: 5.8 bar, 700 uJ, 420 s, Phi 14% (reported eta 23%)", 5.8, 0.97, 700, 420, 0.14),
        ("OP002 best efficiency (text): 5 bar, 865 uJ, 420 s, Phi 4% (reported 27%)", 5.0, 0.975, 865, 420, 0.04),
        ("OP002 Fig. 8b: 5 bar, 800 uJ, 120 s, Phi 3.3% (fig ~27%)", 5.0, 0.975, 800, 120, 0.033),
        ("Fig. 8b: 5 bar, 800 uJ, 360 s, Phi 9.5% (fig ~21.5%)", 5.0, 0.975, 800, 360, 0.095),
        ("Fig. 13a: 9 bar, ~920 uJ, 150 s, Phi 4.4% (fig ~24%)", 9.0, 0.955, 920, 150, 0.044),
    ]
    for name, p, z, e, tau, phi in cases:
        out = []
        for v in (200, 400):
            n0, et, sei, et_a = eta(p, z, e, tau, phi, v)
            out.append(f"V {v}: N0 {n0*1000:.1f} mmol, SEI {sei/EV:.2f} eV, eta {et_a*100:.1f}%")
        print(f"C001 {name}: E_tot {e*1e-6*F*tau:.0f} J | " + " | ".join(out))
    # C002: energy per CO at OP001 (deposited energy), from reported eta and from 200 cm3 recalculation
    ec_rep = DH / 0.23
    n0, et, sei, et_a = eta(5.8, 0.97, 700, 420, 0.14, 200)
    print(f"C002 OP001 EC_CO from reported eta: {ec_rep:.0f} kJ/mol = {ec_rep/KWH_NM3:.1f} kWh/Nm3; "
          f"recalc (200 cm3): {sei/0.14:.0f} kJ/mol = {sei/0.14/KWH_NM3:.1f} kWh/Nm3 (deposited energy)")
    print(f"C003 average deposited power at 700 uJ x 30 kHz = {700e-6*F:.0f} W; "
          f"CO2 processed in 420 s (200 cm3, 5.8 bar) = {n0*1000:.1f} mmol = {n0/7:.4f} mol/min equivalent")
    print(f"C004 gap growth 150 -> 250 um in 240 s (E006): {100/240*60:.0f} um per minute")


if __name__ == "__main__":
    run()
