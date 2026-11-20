"""Reviewer calculations SRC005-C001 to C002 for From et al. (2024), eSMR pilot plant.

Inputs are taken from the manuscript and labelled with evidence IDs in evidence.csv.
Run with: python3 calculations.py
"""
import math

# SRC005-C001: graph reading of Fig. 5 (manuscript.pdf p. 7), experimental points.
# Page rendered at 300 dpi (pdftoppm -r 300), top 45% cropped and viewed at 2000 px width.
# Pixel coordinates below refer to that view; values are approximate.
X_PX_0P01, X_PX_PER_DECADE = 320, 451    # x axis: 0.01 MW at 320 px, 0.1 MW at 771 px (log scale)
Y_PX_40, Y_PX_PER_PERCENT = 908, 11.85   # left y axis: 40% at 908 px, 100% at 197 px
POINTS_PX = {"OP004": (487, 535), "OP005": (513, 506), "OP006": (541, 465), "OP007": (564, 440)}  # E019-E022

for op, (x_px, y_px) in POINTS_PX.items():
    capacity = 0.01 * 10 ** ((x_px - X_PX_0P01) / X_PX_PER_DECADE)
    efficiency = 40 + (Y_PX_40 - y_px) / Y_PX_PER_PERCENT
    print("C001 %s: capacity axis %.4f MW; author efficiency %.1f%%" % (op, capacity, efficiency))
print("     author text: 72-80% (E023); capacity axis undefined (E024)")

# SRC005-C002: methane feed range for the energy-test flows.
# Biogas flows 15-27 Nm3/h (E018); CH4 50-75 mol% is the general raw-biogas range (E010).
# Normal reference assumed 0 degC, 1 atm (not stated in the paper).
NM3_PER_KMOL = 22.414
for biogas_nm3_h in (15, 27):
    low, high = (biogas_nm3_h * y / NM3_PER_KMOL * 1000 / 60 for y in (0.50, 0.75))
    print("C002 %d Nm3/h biogas: CH4 feed %.1f-%.1f mol/min" % (biogas_nm3_h, low, high))

# SRC005-C003: EC_CH4 not calculated. Point-matched Q_in, CH4 feed, biogas composition and
# conversion are not reported for the Fig. 5 points (E018, E024, E042).

# SRC005-C004: reviewer estimate of EC_CH4 for the pilot energy points (OP004-OP007), 2026-11-20.
# The paper gives eta = Q_reaction / Q_in (E006; SI Eqs. S5-S7), where Q_reaction = H_out*F_out - H_in*F_in
# (reaction heat plus heating the gas from inlet to exit). Q_in is not reported, so it is reconstructed as
# Q_in = Q_reaction / eta, with Q_reaction from an equilibrium calculation at the reported conditions:
# inlet 400 degC, exit 900 degC, 10 barg, S/C 2-2.2 (E018); exit gas at equilibrium (E013, OP001 at 900 degC).
# Unknowns spanned: biogas CH4 50-75% (rest CO2; E010), S/C 2.0-2.2 (steam per hydrocarbon carbon, Topsoe
# convention), and eSMR inlet gas either unreacted or equilibrated at 400 degC by the prereformer (E007).
# Thermodynamics: Cantera, GRI-Mech 3.0 ideal-gas data. Normal volume 22.414 Nm3/kmol (0 degC).
# Method check against the authors' own model: 99% efficiency, 920 degC exit, 30 barg, S/C 1.8, 400 degC inlet,
# CH4 feed -> 1.0 kWh/Nm3 syngas (E025, SI Eq. S11).
import itertools
import cantera as ct

ATM = ct.one_atm


def q_reaction(y_ch4, sc, t_in, t_out, p_barg, prereformed):
    """Return (Q_reaction per mol CH4 converted [kJ/mol], X_CH4, syngas H2+CO per mol CH4 fed, Q per mol CH4 fed)."""
    p = p_barg * 1e5 + ATM
    g = ct.Solution("gri30.yaml")
    n_ch4 = 1.0
    feed = {"CH4": n_ch4, "CO2": n_ch4 * (1 - y_ch4) / y_ch4, "H2O": sc * n_ch4}
    n_feed = sum(feed.values())
    g.TPX = t_in + 273.15, p, feed
    if prereformed:
        g.equilibrate("TP")
    # moles: track via element balance on carbon
    n_c = feed["CH4"] + feed["CO2"]
    c_per_mol = sum(g.n_atoms(s, "C") * g.X[i] for i, s in enumerate(g.species_names))
    n_in = n_c / c_per_mol
    h_in = g.enthalpy_mole * n_in / 1e6           # kJ, for n_in in mol
    g.TP = t_out + 273.15, p
    g.equilibrate("TP")
    c_per_mol = sum(g.n_atoms(s, "C") * g.X[i] for i, s in enumerate(g.species_names))
    n_out = n_c / c_per_mol
    h_out = g.enthalpy_mole * n_out / 1e6
    ch4_out = g["CH4"].X[0] * n_out
    x = 1 - ch4_out / n_ch4
    syngas = (g["H2"].X[0] + g["CO"].X[0]) * n_out
    q = h_out - h_in
    return q / (x * n_ch4), x, syngas, q


q, x, syn, qf = q_reaction(1.0, 1.8, 400, 920, 30, prereformed=False)
NM3 = 22.414e-3  # Nm3 per mol
print("C004 check (authors' scale-up case, CH4 feed): X_CH4 %.3f; Q_reaction %.0f kJ/mol CH4 conv; "
      "%.2f kWh/Nm3 syngas at eta 0.99 (authors: 1.0)" % (x, q, qf / 3600 / (syn * NM3) / 0.99))

ETA_POINTS = {"OP004": 0.715, "OP005": 0.739, "OP006": 0.774, "OP007": 0.795}   # C001 (E019-E022)
results = []
for y, sc, pre in itertools.product((0.50, 0.625, 0.75), (2.0, 2.2), (False, True)):
    q, x, syn, qf = q_reaction(y, sc, 400, 900, 10, pre)
    results.append((y, sc, pre, x, q))
    print("C004 y_CH4 %.3f S/C %.1f prereformed %-5s: X_CH4 %.3f; Q_reaction %.0f kJ/mol CH4 conv" % (y, sc, pre, x, q))
qs = [r[4] for r in results]
print("C004 Q_reaction range %.0f-%.0f kJ/mol CH4 converted" % (min(qs), max(qs)))
for op, eta in ETA_POINTS.items():
    print("C004 %s eta %.3f: EC_CH4 at Q_in %.0f-%.0f kJ/mol" % (op, eta, min(qs) / eta, max(qs) / eta))
print("C004 overall EC_CH4 at Q_in: %.0f-%.0f kJ/mol (eta 0.715-0.795)" % (min(qs) / 0.795, max(qs) / 0.715))

# SRC005-C005: consistency check of the Fig. 5 "Capacity [MW]" axis (E024), 2026-11-20.
# If the axis is Q_in, then Q_in = F_CH4 * X * Q_reaction / eta should match it. Two readings of the
# 15-27 Nm3/h flow (E018): (a) biogas only; (b) total process gas (biogas + steam). Lowest flow paired with
# OP004 and highest with OP007 (C002 interpretation).
for label, steam_in_flow in (("(a) biogas", False), ("(b) process gas", True)):
    for flow, op in ((15, "OP004"), (27, "OP007")):
        vals = []
        for y, sc in itertools.product((0.50, 0.625, 0.75), (2.0, 2.2)):
            q, x, syn, qf = q_reaction(y, sc, 400, 900, 10, False)
            ch4_frac = y / (1 + sc * y) if steam_in_flow else y
            f_ch4 = flow * ch4_frac / NM3 / 3600          # mol/s
            vals.append(f_ch4 * x * q / ETA_POINTS[op])  # kW
        print("C005 %s %d Nm3/h -> implied Q_in %.0f-%.0f kW (Fig. 5 axis at %s: %.1f kW)"
              % (label, flow, min(vals), max(vals), op, {"OP004": 23.5, "OP007": 34.8}[op]))
