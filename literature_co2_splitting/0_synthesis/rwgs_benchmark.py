"""Reviewer estimate: electricity per CO for water electrolysis (PEM) followed by the reverse water-gas shift (RWGS).

A simple energy balance used as a benchmark point in the CO2-splitting figures; it is our estimate, not a
literature value. Writes rwgs_benchmark.csv next to this script.

Process: PEM electrolysis supplies H2 at 30 bar(g); H2 and CO2 (H2/CO2 = 2.3) are heated from 25 C to 850 C and
brought to equilibrium in a single pass at 31.01 bar(a): CO2 + H2 <=> CO + H2O. The equilibrium is restricted to
CO2, H2, CO and H2O (an RWGS-selective reactor; no methane or solid carbon). Ideal gas, Cantera GRI-Mech 3.0 data.

Electricity per mol CO (allocation: only the H2 consumed to make CO, one H2 per CO; the excess H2 leaves in the
syngas as product):
    EC_CO = W_PEM per mol H2 + (Q_RWGS + (1 - f) Q_preheat) / X
  W_PEM: 55.9 kWh/kg H2, full-system AC electricity at beginning of life (ITM Power NEPTUNE V specification
  sheet v2.8, p. 2; vendor figure, includes water purification and balance of plant; 30 bar(g) delivery).
  Q_RWGS, Q_preheat: reaction heat and feed preheat per mol CO2 fed, supplied as electric heat at 100%.
  f: fraction of the preheat recovered from the hot product; marker f = 0.5, range f = 0 to 1.
  X: single-pass CO2 conversion.
Excluded: CO2 capture and compression, separation of CO, H2, CO2 and water, recycle, heat losses, heater losses.

Run from the repository root: ~/.venvs/science/bin/python literature_co2_splitting/0_synthesis/rwgs_benchmark.py
"""
import csv
from pathlib import Path

import cantera as ct

HERE = Path(__file__).resolve().parent
T_REF, T_RWGS = 298.15, 850.0 + 273.15
P_BAR = 30.0 + 1.01325
H2_CO2 = 2.3
PEM_KWH_KG = 55.9
M_H2 = 2.01588e-3                      # kg/mol
KJ_PER_KWH_NM3 = 3600 / (1000 / 22.414)  # kJ/mol per kWh/Nm3


def gas():
    species = [s for s in ct.Species.list_from_file("gri30.yaml") if s.name in ("CO2", "H2", "CO", "H2O")]
    return ct.Solution(thermo="ideal-gas", species=species)


def enthalpy(g, T, amounts):
    g.TPX = T, P_BAR * 1e5, amounts
    return sum(amounts.values()) * g.enthalpy_mole / 1e6      # kJ


g = gas()
feed = {"CO2": 1.0, "H2": H2_CO2}
g.TPX = T_RWGS, P_BAR * 1e5, feed
g.equilibrate("TP")
prod = {s: float(x) * (1 + H2_CO2) for s, x in zip(g.species_names, g.X)}   # RWGS conserves moles
X = 1 - prod["CO2"]
q_pre = enthalpy(g, T_RWGS, feed) - enthalpy(g, T_REF, feed)
q_rx = enthalpy(g, T_RWGS, prod) - enthalpy(g, T_RWGS, feed)
w_h2 = PEM_KWH_KG * M_H2 * 3600                      # kJ per mol H2

rows = []
for f in (0.0, 0.5, 1.0):
    ec = w_h2 + (q_rx + (1 - f) * q_pre) / X
    rows.append(dict(preheat_recovered=f, EC_CO_kJ_mol=round(ec, 1), EC_CO_kWh_Nm3=round(ec / KJ_PER_KWH_NM3, 3)))
with open(HERE / "rwgs_benchmark.csv", "w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh)
    w.writerow(["quantity", "value", "unit"])
    w.writerow(["X_CO2", round(100 * X, 2), "%"])
    w.writerow(["dry_H2_CO", round(prod["H2"] / prod["CO"], 3), "mol/mol"])
    w.writerow(["W_PEM_per_mol_H2", round(w_h2, 1), "kJ/mol H2"])
    w.writerow(["Q_RWGS_per_mol_CO2_fed", round(q_rx, 2), "kJ"])
    w.writerow(["Q_preheat_per_mol_CO2_fed", round(q_pre, 2), "kJ"])
    for r in rows:
        w.writerow([f"EC_CO_preheat_recovered_{r['preheat_recovered']:g}", r["EC_CO_kWh_Nm3"], "kWh/Nm3 CO"])
print(f"X_CO2 {100 * X:.1f}%, dry H2/CO {prod['H2'] / prod['CO']:.2f}, W_PEM {w_h2:.1f} kJ/mol H2, "
      f"Q_RWGS {q_rx:.1f}, Q_preheat {q_pre:.1f} kJ/mol CO2 fed")
for r in rows:
    print(f"preheat recovered {r['preheat_recovered']:.0%}: EC_CO {r['EC_CO_kJ_mol']} kJ/mol = {r['EC_CO_kWh_Nm3']} kWh/Nm3")
