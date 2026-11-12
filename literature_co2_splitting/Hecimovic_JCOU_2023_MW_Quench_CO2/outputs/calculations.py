"""Reviewer calculations for SRC017 (Hecimovic et al. 2023, J. CO2 Util. 71, 102473).

Run: python3 calculations.py
Flows are in ls/min at 20 degC, 1 atm (SRC017-E006): 24.055 L/mol. The authors use
dH = 2.9 eV/molecule (E008); the review reference is 2.93 eV (282.7 kJ/mol).
"""

VM20 = 22.414 * 293.15 / 273.15     # 24.055 L/mol at 20 degC, 1 atm
VM0 = 22.414
EV = 96.485                          # kJ/mol per eV/molecule
DH_AUTH = 2.9
DH_REV = 2.93
KWH_NM3 = 3.6e3 / (1000.0 / VM0)     # kJ/mol per kWh/Nm3 = 80.69

# OP: flow (ls/min, 20 C), absorbed power (W), conversion, reported/figure eta (%)
OPS = {
    "OP001": dict(f=10, p=2700, x=0.345, eta_fig=27.0),   # Fig. 2a/b, no pump, atmospheric (E011)
    "OP002": dict(f=5, p=2700, x=0.55, eta_fig=21.7),     # text p. 5 and Fig. 7b (E013, E014)
    "OP003": dict(f=None, p=2700, x=0.566, eta_fig=16.4, sei_ev=10.1),  # Fig. 8/9 max (E015)
    "OP004": dict(f=None, p=None, x=0.12, eta_fig=30.0, sei_ev=None),   # text p. 7 (E016)
}


def run():
    for op, d in OPS.items():
        if d.get("f"):
            f = d["f"] / VM20 / 60.0                      # mol/s
            sei = d["p"] / f / 1000.0                      # kJ/mol  (C001)
            sei_0c = d["p"] / (d["f"] / VM0 / 60.0) / 1000.0
        elif d.get("sei_ev"):
            sei = d["sei_ev"] * EV
            sei_0c = None
        else:
            # OP004: SEI implied by the authors' eta and X (C003)
            sei_auth = d["x"] * DH_AUTH / (d["eta_fig"] / 100) * EV
            print(f"{op}: SEI implied by reported 30% at X 12% = {sei_auth/EV:.2f} eV; "
                  f"Kiefer 2024 (SRC016-E016) gives eta_p 27% at X 12.3% for the same torch")
            continue
        eta_auth = d["x"] * DH_AUTH * EV / sei * 100       # C002, authors' dH, 20 C flow
        eta_rev = d["x"] * DH_REV * EV / sei * 100
        ec_co2 = sei / d["x"]                              # kJ/mol CO2 converted (C004)
        line = (f"{op}: SEI {sei:.0f} kJ/mol ({sei/EV:.2f} eV) | eta X*2.9/SEI {eta_auth:.1f}% "
                f"(2.93: {eta_rev:.1f}%) vs figure {d['eta_fig']}% (ratio {d['eta_fig']/eta_auth:.2f}) | "
                f"EC_CO2 {ec_co2:.0f} kJ/mol = {ec_co2/KWH_NM3:.1f} kWh/Nm3 CO (absorbed)")
        if sei_0c:
            line += (f" | if flow taken at 0 C: SEI {sei_0c/EV:.2f} eV, eta {d['x']*DH_AUTH*EV/sei_0c*100:.1f}%")
        print(line)
    # C005: flow conversions to Kiefer's 0 degC slm
    for ls in (4, 5, 10, 15):
        print(f"C005 {ls} ls/min (20 C) = {ls*273.15/293.15:.2f} slm (0 C)")


if __name__ == "__main__":
    run()
