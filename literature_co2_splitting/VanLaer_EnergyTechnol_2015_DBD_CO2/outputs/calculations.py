"""Reviewer calculations for SRC024 (Van Laer & Bogaerts 2015, Energy Technol. 3, 1038-1044).

Run: python3 calculations.py
Authors: eta = dH x X / (SEI x Vm), SEI = P_plasma x 60 / flow (kJ/L), dH = 279.8 kJ/mol (E008);
P_plasma from V(t) I(t) (E007); Vm not stated (24.5 and 22.414 L/mol both shown).
Conversion X = (CO2_in - CO2_out)/CO2_in from GC signals against a no-plasma reference (E006):
no gas-expansion correction stated.
"""

DH = 279.8
KWH_NM3 = 3.6e3 / (1000.0 / 22.414)

# OP: (label, flow mL/min, applied W, X, eta)
OPS = [
    ("OP001 best combined (1.6-1.8 mm, 60 W, 20 mL/min)", 20, 60, 0.378, 0.064),
    ("OP002 max conversion (2.0-2.24 mm, 80 W, 20 mL/min)", 20, 80, 0.420, 0.047),
    ("OP003 max efficiency (1.6-1.8 mm, 60 W, 100 mL/min)", 100, 60, 0.100, 0.096),
    ("OP004 empty reactor (60 W, 20 mL/min; from factors 1.9, 1.8)", 20, 60, 0.378 / 1.9, 0.064 / 1.8),
]


def expansion_corrected(x_app):
    """If X_app = 1 - y_CO2,out (no expansion correction), the true X satisfies
    y_CO2,out = (1 - X)/(1 + X/2)  ->  X = X_app / (1 + (1 - X_app)/2)."""
    return x_app / (1 + (1 - x_app) / 2)


def run():
    for label, q, p_app, x, eta in OPS:
        out = [label]
        for vm in (24.5, 22.414):
            sei_l = DH * x / (eta * vm)                 # kJ/L implied by reported X and eta (C001)
            p_pl = sei_l * q / 1000 / 60 * 1000          # W
            out.append(f"Vm {vm}: SEI {sei_l:.1f} kJ/L, P_plasma {p_pl:.1f} W ({p_pl/p_app*100:.0f}% of applied)")
        ec = DH / eta                                    # kJ/mol CO2 converted (plasma) (C002)
        out.append(f"EC_CO2 {ec:.0f} kJ/mol = {ec/KWH_NM3:.1f} kWh/Nm3 CO (plasma)")
        xc = expansion_corrected(x)                      # C003
        out.append(f"expansion-corrected X {xc*100:.1f}% (eta {eta*xc/x*100:.1f}%)")
        f = q / 1000 / 24.5 / 60                         # mol/s at 24.5 L/mol
        out.append(f"eta on applied power {x*DH*1000*f/p_app*100:.1f}% (24.5 L/mol)")   # C004
        print("C00x " + " | ".join(out))


if __name__ == "__main__":
    run()
