"""CO2 conversion vs LHV efficiency at the wall, plasma exemplars against the SOEC system.

Reads co2_synthesis.csv (no data values in this script).

eta_LHV = LHV of CO out / (wall electricity + LHV of carbon in), per Nm3 CO.
  LHV_CO = 283.0 kJ/mol = 3.51 kWh/Nm3 CO (0 C, 1 atm). It equals the CO2 splitting enthalpy, so without carbon
  eta_LHV is the field's dH efficiency on the wall basis.
  Carbon beds: carbon is an energy input; LHV_C = 393.5 kJ/mol = 32.8 MJ/kg (graphite; charcoal is similar).
Wall electricity: measured by the authors where available, else the industrial-supply estimate (bar = class range).
SOEC system (Hecimovic 2024 OP001) at its 86% utilisation, wall incl. rectifier. The SOEC stack values (Kungas 2020)
are not plotted: they exclude the heat supplied below the thermoneutral voltage and would give 97-140%.
SOEC system point is stack DC + rectifier only (no balance of plant, heat losses, degradation or CO purification);
the plasma wall values omit chillers, pumps and separation likewise. Caveat text: co2_synthesis_tables.md note [10].
Van Laer (SRC024) conversions as reported; if not expansion-corrected they would fall by 3-9 points and
eta_LHV by 1-3 points (synthesis table note [6]); not shown, as it does not move them out of the <10% corner.
Rows not plotted: Bryssinck OP004 (carbon use NR), Hecimovic 2024 OP002/OP005 (vendor figure; not matched).

Run from the repository root: ~/.venvs/science/bin/python literature_co2_splitting/synthesis/plot_x_vs_eta.py
"""
import csv
import re
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

HERE = Path(__file__).resolve().parent
rows = list(csv.DictReader(open(HERE / "co2_synthesis.csv", encoding="utf-8")))

KWH_NM3 = 3600 / (1000 / 22.414)            # kJ/mol per kWh/Nm3
LHV_CO = 283.0 / KWH_NM3                    # kWh/Nm3 CO
LHV_C = 393.5 / 12.011 / 3.6                # kWh/kg C

BLUE, ORANGE, AQUA = "#2a78d6", "#eb6834", "#1baf7a"
INK, MUTED, GRID = "#1f1f1e", "#6b6a64", "#e4e3de"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 8.5, "axes.edgecolor": MUTED,
                     "axes.labelcolor": INK, "xtick.color": MUTED, "ytick.color": MUTED,
                     "axes.spines.top": False, "axes.spines.right": False,
                     "svg.fonttype": "none", "savefig.facecolor": "white"})
STYLE = {
    "MW 2.45 GHz": (BLUE, "o"), "MW 915 MHz": (BLUE, "s"),
    "GA (AC)": (ORANGE, "^"), "GA (DC)": (ORANGE, "D"), "DC glow-to-arc": (ORANGE, "p"),
    "NRP": (AQUA, "*"), "DBD": (AQUA, "v"),
}


def family(route):
    for k in STYLE:
        if route.startswith(k) or (k == "DBD" and "DBD" in route):
            return k
    return None


def num(s):
    m = re.search(r"[\d.]+", s or "")
    return float(m.group()) if m else None


def f(s):
    return float(s) if s not in ("", None) else None


pts = []
for r in rows:
    fam = family(r["route"])
    x = num(r["X_CO2_pct"])
    bed = "C bed" in r["route"]
    c = f(r["carbon_kg_per_Nm3_CO"])
    if fam is None or x is None or r["source_id"] in ("SRC025", "SRC026") or (bed and c is None):
        continue
    if f(r["EC_CO_wall_measured_low"]):
        ec = (f(r["EC_CO_wall_measured_low"]), f(r["EC_CO_wall_measured_high"]))
    else:
        ec = (f(r["EC_CO_industrial_est_low"]), f(r["EC_CO_industrial_est_high"]))
    cin = c * LHV_C if bed else 0.0
    eta = (LHV_CO / (ec[1] + cin) * 100, LHV_CO / (ec[0] + cin) * 100)       # (low, high)
    eta_el = (LHV_CO / ec[1] * 100, LHV_CO / ec[0] * 100)
    corr = re.search(r"\(([\d.]+) corr", r["X_CO2_pct"])
    pts.append(dict(key=r["row_key"], fam=fam, x=x, eta=eta, eta_el=eta_el, bed=bed,
                    x_corr=float(corr.group(1)) if corr else None, head=r["headline"] == "yes"))

s = {r["row_key"]: r for r in rows}["Hecimovic 2024 OP001"]
soec_eta, soec_x = LHV_CO / f(s["EC_CO_wall_measured_high"]) * 100, num(s["X_CO2_pct"])

LABEL = {
    "Kiefer 2024 OP001": "Kiefer", "Kiefer 2024 OP003": "Kiefer", "Hecimovic 2023 OP002": "Hecimovic 23",
    "Bongers 2017 OP001": "Bongers", "Bongers 2017 OP003": "Bongers", "Girard-Sahun 2022 OP001": "Girard-Sahun",
    "Girard-Sahun 2022 OP002": "Girard-Sahun (peak, C)", "Girard-Sahun 2022 OP003": "Girard-Sahun (14 min, C)",
    "O'Modhrain 2024 OP001": "O'Modhrain", "Bryssinck 2025 OP003": "Bryssinck (C)", "Renninger 2022 OP001": "Renninger",
    "Yong 2023 OP001": "Yong", "Van Laer 2015 OP001": "Van Laer", "Van Laer 2015 OP003": "Van Laer",
}
OFFSET = {  # (dx, dy, ha, va) in points where the default collides
    "Kiefer 2024 OP003": (-6, 3, "right", "bottom"),
    "Hecimovic 2023 OP002": (6, -3, "left", "top"),
    "Girard-Sahun 2022 OP001": (6, 0, "left", "center"),
    "Girard-Sahun 2022 OP003": (6, -2, "left", "top"),
    "Van Laer 2015 OP003": (6, -2, "left", "top"),
}

LEAD = {"O'Modhrain 2024 OP001": (14.5, 25, "right")}

fig, ax = plt.subplots(figsize=(6.4, 4.8))
for p in pts:
    col, mk = STYLE[p["fam"]]
    xc = sum(p["eta"]) / 2
    ms = 11 if mk == "*" else 7
    if p["eta"][1] - p["eta"][0] > 0.3:
        ax.plot(p["eta"], [p["x"]] * 2, color=col, lw=1.5, alpha=0.6, zorder=2, solid_capstyle="round")
    ax.plot(xc, p["x"], marker=mk, ms=ms, mfc="white" if p["bed"] else col, mec=col if p["bed"] else "white",
            mew=1.4 if p["bed"] else 0.8, ls="none", zorder=4, alpha=1.0 if p["head"] else 0.55)
    if p["head"] and p["key"] in LABEL:
        if p["key"] in LEAD:   # fixed text position (data coords) with a thin leader line
            tx, ty, ha = LEAD[p["key"]]
            ax.annotate(LABEL[p["key"]], (xc, p["x"]), xytext=(tx, ty), textcoords="data", fontsize=6.8, color=INK,
                        ha=ha, va="center", arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.6, shrinkA=1, shrinkB=4))
        else:
            dx, dy, ha, va = OFFSET.get(p["key"], (5, 3, "left", "bottom"))
            ax.annotate(LABEL[p["key"]], (xc, p["x"]), xytext=(dx, dy), textcoords="offset points",
                        fontsize=6.8, color=INK, ha=ha, va=va)
ax.plot(soec_eta, soec_x, marker="h", ms=9, mfc=INK, mec="white", mew=0.8, ls="none", zorder=5)
ax.annotate(f"SOEC system\n({soec_x:.0f}% utilisation)", (soec_eta, soec_x), xytext=(-7, 0),
            textcoords="offset points", fontsize=6.8, color=INK, ha="right", va="center")

ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.set_xlabel("LHV efficiency at the wall (%)  =  LHV of CO / (electricity + LHV of carbon)")
ax.set_ylabel("CO₂ conversion, single pass (%)")
ax.grid(True, color=GRID, lw=0.6)
ax.set_axisbelow(True)
ax.set_title("Wall basis: measured, or with an industrial supply", loc="left", fontsize=9, color=INK)

handles = [Line2D([], [], marker=STYLE[k][1], color=STYLE[k][0], mec="white", ls="none",
                  ms=11 if STYLE[k][1] == "*" else 7, label=k) for k in STYLE]
handles += [Line2D([], [], marker="h", mfc=INK, mec="white", ls="none", ms=9, label="SOEC system (Hecimovic 2024)"),
            Line2D([], [], marker="o", mfc="white", mec=MUTED, mew=1.4, ls="none", ms=7,
                   label="carbon bed (carbon LHV counted)"),
            Line2D([], [], color=MUTED, lw=1.5, alpha=0.6, label="range (supply class / volume)")]
fig.legend(handles=handles, loc="lower center", ncol=3, frameon=False, fontsize=7.2, bbox_to_anchor=(0.5, -0.01))
fig.tight_layout(rect=(0, 0.2, 1, 1))
for ext in ("png", "svg"):
    fig.savefig(HERE / f"co2_x_vs_eta_lhv.{ext}", dpi=200, bbox_inches="tight")
for p in sorted(pts, key=lambda q: -sum(q["eta"])):
    print(f"{p['key']:26s} X {p['x']:5.1f}  eta_LHV {p['eta'][0]:5.1f}-{p['eta'][1]:5.1f}"
          + (f"  (electricity only {p['eta_el'][0]:.1f}-{p['eta_el'][1]:.1f})" if p["bed"] else ""))
print(f"SOEC system: X {soec_x}, eta_LHV {soec_eta:.1f}%; LHV_CO {LHV_CO:.3f} kWh/Nm3, LHV_C {LHV_C:.2f} kWh/kg")
