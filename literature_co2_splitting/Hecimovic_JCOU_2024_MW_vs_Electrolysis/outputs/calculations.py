"""Reviewer calculations for SRC026 (Hecimovic et al. 2024, J. CO2 Util. 83, 102825), benchmark.

Run: python3 calculations.py
Inputs carry evidence IDs; results carry calculation IDs (SRC026-Cxxx).
"""

VM = 22.414                    # L/mol, normal conditions (0 degC, 1 atm)
DH = 282.7                     # kJ/mol (2.93 eV/molecule, E004)
F = 96485.0
EPC_100 = DH / VM / 3.6        # kWh/Nm3 CO at 100% efficiency; authors quote 3.51 (E013)


def ec_co(epc):
    """kWh/Nm3 CO -> kJ/mol CO."""
    return epc * 3600.0 / (1000.0 / VM)


def run():
    print(f"EPC at 100% efficiency: {EPC_100:.3f} kWh/Nm3 (authors 3.51)")

    # C001 FZJ HT system (E009): stack 69.6 kW, CO 17.5 m3/h, rectifier/inverter 0.95,
    # reported wall-plug 89.0% and EPC 3.89 kWh/Nm3
    p_stack, co = 69.6, 17.5
    epc_stack = p_stack / co
    epc_wall = p_stack / 0.95 / co
    v_stack = epc_stack * 3.6e6 / 1000 * VM / (2 * F)
    print(f"C001 FZJ: stack EPC {epc_stack:.2f}; with 0.95 rectifier {epc_wall:.2f} kWh/Nm3; "
          f"eta at reported EPC 3.89 = {EPC_100/3.89*100:.1f}%; eta at 0.95 rectifier = "
          f"{EPC_100/epc_wall*100:.1f}%; EPC implied by 89.0% = {EPC_100/0.89:.2f}; "
          f"implied cell voltage {v_stack:.2f} V (thermoneutral ~1.465 V)")

    # C002 efficiency implied by each EPC in Table 1 (E013, E014, E016-E018)
    for label, epc, eta_rep in [("MW plasma reactor EPC_tot", 19.8, "up to 18"),
                                ("MW plasma reactor EPC_process", 12, "EE up to 27"),
                                ("MW + membranes EPC_tot", 35, "up to 10"),
                                ("MW + membranes EPC_process", 19, "EE up to 18"),
                                ("KEROGREEN EPC_process", 11.4, "EE 34"),
                                ("eCOs EPC_tot low", 6, "wall-plug 90"),
                                ("eCOs EPC_tot high", 8, "wall-plug 90"),
                                ("LT pilot EPC_process", 10.2, "EE 25-35")]:
        print(f"C002 {label}: {epc} kWh/Nm3 -> eta {EPC_100/epc*100:.1f}% (reported {eta_rep}); "
              f"EC_CO {ec_co(epc):.0f} kJ/mol")

    # C003 O2 separated by the membranes (E011): 42 sccm = 5% of O2 produced
    o2_prod = 42 / 0.05                       # sccm
    co_prod = 2 * o2_prod / 1000              # slm
    print(f"C003 membranes: O2 produced {o2_prod:.0f} sccm -> CO {co_prod:.2f} slm = "
          f"{co_prod*60/1000:.3f} Nm3/h (Table 1: 0.12)")

    # C004 KEROGREEN (E012, E016): 60 slm max, X 14%
    print(f"C004 KEROGREEN: 60 slm x 0.14 = {60*0.14:.1f} slm CO = {60*0.14*60/1000:.2f} Nm3/h "
          f"(Table 1: 0.56 Nm3/h -> {0.56*1000/60/0.14:.0f} slm CO2 at X 14%)")


if __name__ == "__main__":
    run()
