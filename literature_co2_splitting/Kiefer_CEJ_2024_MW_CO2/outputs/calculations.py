"""Reviewer calculations for SRC016 (Kiefer et al. 2024, Chem. Eng. J. 481, 148326).

Run: python3 calculations.py
Each input carries its evidence ID; each result its calculation ID (SRC016-Cxxx).
Flows are standard litres per minute at 0 degC, 1013 hPa (SRC016-E006); the authors
use Vm = 22.414 L/mol (SRC016-E012), which is used here.
"""

VM = 22.414          # L/mol at 0 degC, 1 atm (SRC016-E006, E012)
DH = 2.93            # eV/molecule, authors' reaction enthalpy (SRC016-E011)
EV = 96.485          # kJ/mol per eV/molecule
DH_KJ = DH * EV      # 282.7 kJ/mol

# Operating points: flow (slm), absorbed power P_abs (W), conversion (fraction),
# reported wall-plug efficiency eta_tot (fraction or None), reported EPC (kWh/Nm3 or None)
OPS = {
    # OP001 cooling channels, atmospheric, pump disconnected (E018, E019)
    "OP001": dict(slm=9.3, p_abs=2700, x=0.344, eta_tot=0.179, epc=19.6),
    # OP002 standard configuration, 150 mbar, pump connected (E019, E020)
    "OP002": dict(slm=9.3, p_abs=2700, x=0.386, eta_tot=0.179, epc=19.6),
    # OP003 cooling channels, 900 mbar, pump connected, highest conversion (E015);
    # eta_tot read from Fig. 11 (E021), approximate
    "OP003": dict(slm=3.7, p_abs=2700, x=0.566, eta_tot=0.105, epc=None),
    # OP004 durability test, cooling channels, atmospheric (E024); x and eta_tot read
    # from Fig. 15 (E025), approximate
    "OP004": dict(slm=10.2, p_abs=2250, x=0.27, eta_tot=0.177, epc=None),
}


def run():
    print(f"DH = {DH_KJ:.1f} kJ/mol")
    for op, d in OPS.items():
        f_co2 = d["slm"] / VM / 60.0                    # mol/s
        sei_p = d["p_abs"] / f_co2 / 1000.0              # kJ/mol CO2 fed   (C001)
        sei_p_ev = sei_p / EV
        eta_p = d["x"] * DH_KJ / sei_p                   # (C002) check vs reported eta_p
        ec_co2_p = sei_p / d["x"]                        # kJ/mol CO2 conv, plasma basis (C003)
        p_tot = d["x"] * DH_KJ * 1000 * f_co2 / d["eta_tot"]   # W, wall-plug (C004)
        sei_w = p_tot / f_co2 / 1000.0                   # kJ/mol CO2 fed, wall basis
        ec_co2_w = sei_w / d["x"]                        # kJ/mol CO2 conv, wall basis (C005)
        co_nm3h = d["x"] * d["slm"] * 60 / 1000.0        # Nm3/h CO
        epc_calc = p_tot / 1000.0 / co_nm3h              # kWh/Nm3 CO (C006) check vs EPC
        print(f"{op}: F_CO2 {f_co2*60:.4f} mol/min | SEI_p {sei_p:.0f} kJ/mol ({sei_p_ev:.2f} eV) | "
              f"eta_p {eta_p*100:.1f}% | EC_CO2,p {ec_co2_p:.0f} kJ/mol | P_tot {p_tot:.0f} W | "
              f"SEI_wall {sei_w:.0f} kJ/mol | EC_CO2,wall {ec_co2_w:.0f} kJ/mol | "
              f"EPC calc {epc_calc:.1f} kWh/Nm3 (reported {d['epc']})")


if __name__ == "__main__":
    run()
