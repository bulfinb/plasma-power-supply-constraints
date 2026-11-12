"""Reviewer calculations for SRC025 (Küngas 2020, J. Electrochem. Soc. 167, 044508), SOEC benchmark.

Run: python3 calculations.py
Inputs carry evidence IDs; results carry calculation IDs (SRC025-Cxxx).
"""

F = 96485.0      # C/mol
N = 2            # electrons per CO (E011)
VM = 22.414      # L/mol, normal conditions; reproduces the reported EPC (C001)
KWH = 3.6e6      # J/kWh
DH = 282.7       # kJ/mol, CO2 -> CO + 1/2 O2 at 298 K (review reference, objectives)


def epc_from_voltage(e_cell, fe=1.0):
    """Eq. 16: EPC = E n F / (FE Vm), returned in kWh/Nm3 CO."""
    return e_cell * N * F / (fe * VM) * 1000 / KWH


def voltage_from_epc(epc):
    return epc * KWH / 1000 * VM / (N * F)


def ec_co(epc):
    """kWh/Nm3 CO -> kJ/mol CO (C003)."""
    return epc * 3600.0 / (1000.0 / VM)


def run():
    # C001: check Eq. 16 against reported pairs (E013, E015)
    for v, epc_rep in [(1.1, 2.5), (1.24, 2.96), (1.28, 3.06)]:
        print(f"C001 E={v} V -> EPC {epc_from_voltage(v):.2f} kWh/Nm3 (reported {epc_rep})")
    # C002: thermoneutral voltage and the matching EPC (reaction enthalpy as electricity)
    v_tn = DH * 1000 / (N * F)
    print(f"C002 V_tn ~ {v_tn:.3f} V; EPC at V_tn {epc_from_voltage(v_tn):.2f} kWh/Nm3")
    # C003: EC_CO for the selected points (EPC inputs: E013, E015, E016 figure reading, E012)
    for op, epc in [("OP001", 2.5), ("OP002 start", 2.96), ("OP002 end", 3.06),
                    ("OP003 start ~", 3.3), ("OP003 end ~", 3.6), ("max <", 3.4),
                    ("theor. 800 C", 2.3), ("theor. 25 C", 3.2)]:
        print(f"C003 {op}: EPC {epc} kWh/Nm3 = {ec_co(epc):.0f} kJ/mol CO; "
              f"cell V {voltage_from_epc(epc):.2f} V; fraction of dH as electricity {ec_co(epc)/DH*100:.0f}%")


if __name__ == "__main__":
    run()
