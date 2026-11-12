"""Reviewer calculations for SRC022 (Renninger et al. 2022, J. CO2 Util. 58, 101919).

Run: python3 calculations.py
Flows in SLM (standard litres, 0 degC: the authors' dH = 12.6 J/SCC equals 282.7 kJ/mol /
22.414 L/mol, E009). Powers: P_plasma (V x I at the reactor) and P_supply (DC output of the
lab supply feeding the driver; mains-side losses of the lab supply excluded, E004).
"""

DH_SCC = 12.6            # J per standard cm3 CO2 (E009)
VM = 22.414


def kwh_nm3(j_per_ml):
    return j_per_ml / 3.6          # J/mL = kJ/L = kJ per 1e-3 Nm3 -> kWh/Nm3


def run():
    print(f"C001 dH check: 12.6 J/SCC x 22414 = {DH_SCC*VM*1000/1000:.1f} kJ/mol (282.7 reference)")
    slm = 1.25
    scc_s = slm * 1000 / 60.0
    full = DH_SCC * scc_s            # W needed for 100% conversion at 100% efficiency
    print(f"C001 1.25 SLM: {scc_s:.2f} SCC/s; X=100% at eta=100% needs {full:.1f} W")
    # Fig. 4 readings (E012): P_supply, X, eta_plasma, eta_system
    fig4 = [(153, 0.17, 0.45, 0.29), (218, 0.21, 0.455, 0.25), (262, 0.274, 0.445, 0.275), (300, 0.278, 0.39, 0.25)]
    for ps, x, ep, es in fig4:
        pp = x * full / ep
        es_calc = x * full / ps
        print(f"C002 Fig.4 P_supply {ps} W: X {x*100:.1f}% -> P_plasma {pp:.0f} W (from eta_plasma), "
              f"driver {pp/ps:.2f}; eta_system calc {es_calc*100:.1f}% (fig {es*100:.0f}%)")
    # C003: energy per CO for the selected OPs
    ops = {
        "OP001 1.25 SLM, P_plasma ~162 W / P_supply 262 W, X 27.4%": (1.25, 162, 262, 0.274),
        "OP002 1.25 SLM, P_plasma ~99 W / P_supply 153 W, X ~17%": (1.25, 99, 153, 0.17),
        "OP003 0.65 SLM, E 20 J/SCC (P_plasma ~217 W), X ~28.8%": (0.65, 0.65 * 1000 / 60 * 20, None, 0.288),
    }
    for name, (q, pp, ps, x) in ops.items():
        scc = q * 1000 / 60
        e_p = pp / scc                         # J/SCC plasma
        ec_p = e_p / x                         # J per mL CO = per mL CO2 converted
        line = (f"C003 {name}: E_spec {e_p:.2f} J/SCC = {e_p*VM/96.485:.2f} eV | eta_plasma {x*DH_SCC/e_p*100:.1f}% | "
                f"EC_CO2 {ec_p*VM:.0f} kJ/mol = {kwh_nm3(ec_p):.2f} kWh/Nm3 CO (plasma)")
        if ps:
            e_s = ps / scc
            line += f" | supply basis {kwh_nm3(e_s/x):.2f} kWh/Nm3, eta_sys {x*DH_SCC/e_s*100:.1f}%"
        else:
            line += f" | supply basis at driver 0.61-0.65: {kwh_nm3(ec_p/0.65):.1f}-{kwh_nm3(ec_p/0.61):.1f} kWh/Nm3"
        print(line)
    print(f"C004 CO2 feed 1.25 SLM = {1.25/VM:.4f} mol/min; 0.65 SLM = {0.65/VM:.4f} mol/min")


if __name__ == "__main__":
    run()
