"""CO2 conversion vs LHV efficiency at the wall: plasma CO2-splitting headline points against the SOEC system
(no data values in this script; reads co2_synthesis.csv).

Same point set, colours, markers, labels and right-hand legends as the manuscript figure (plot_manuscript_figure.py).

eta_LHV = LHV of CO out / (wall electricity + LHV of carbon in), per Nm3 CO.
  LHV_CO = 283.0 kJ/mol = 3.51 kWh/Nm3 CO (0 C, 1 atm); it equals the CO2-splitting enthalpy, so without carbon
  eta_LHV is the usual reaction-enthalpy efficiency on the wall basis.
  Carbon beds: conversion and eta_LHV are both after the bed; the carbon consumed is an energy input
  (LHV_C = 393.5 kJ/mol, graphite).
Wall electricity: measured by the authors where available, else the industrial-supply estimate (bar = class range;
marker at the geometric mid of the electricity range, as in the manuscript figure).
SOEC: system design point (Hecimovic 2024 OP001) at its 86% utilisation, wall incl. the 0.95 design rectifier
(stack DC + rectifier only; no balance of plant, heat losses or CO purification). The plasma wall values likewise
omit chillers, pumps and separation.

Writes figures/co2_x_vs_eta_lhv.png/.svg.
Run from the repository root: ~/.venvs/science/bin/python literature_co2_splitting/0_synthesis/plot_x_vs_eta.py
"""
import csv
import re
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

HERE = Path(__file__).resolve().parent
FIG = HERE / "figures"
FIG.mkdir(exist_ok=True)
rows = list(csv.DictReader(open(HERE / "co2_synthesis.csv", encoding="utf-8")))
BENCH = {"SRC025", "SRC026"}
SKIP = {"Hecimovic 2024 OP005", "Girard-Sahun 2022 OP001", "Hecimovic 2023 OP002"}   # as the manuscript figure

KWH_NM3 = 3600 / (1000 / 22.414)            # kJ/mol per kWh/Nm3
LHV_CO = 283.0 / KWH_NM3                    # kWh/Nm3 CO
LHV_C = 393.5 / 12.011 / 3.6                # kWh/kg C

SLOT = ["#2a78d6", "#eb6834", "#1baf7a"]
INK, MUTED, GRID, HALO = "#1f1f1e", "#6b6a64", "#e4e3de", "#d2d1cb"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 8.5, "axes.edgecolor": MUTED,
                     "axes.labelcolor": INK, "xtick.color": MUTED, "ytick.color": MUTED,
                     "axes.spines.top": False, "axes.spines.right": False,
                     "svg.fonttype": "none", "savefig.facecolor": "white"})
STYLE = {
    "MW 2.45 GHz": (SLOT[0], "o", "microwave 2.45 GHz"), "MW 915 MHz": (SLOT[0], "s", "microwave 915 MHz"),
    "GA (AC)": (SLOT[1], "^", "gliding arc, AC"), "GA (DC)": (SLOT[1], "D", "gliding arc, DC"),
    "DC glow-to-arc": (SLOT[1], "p", "DC glow-to-arc"),
    "NRP": (SLOT[2], "*", "nanosecond pulsed"), "DBD": (SLOT[2], "v", "packed-bed DBD"),
}
OFFSET = {   # label position overrides: key -> ((dx, dy) points, ha, va); default right of the point
    "Van Laer 2015 OP003": ((0, 6), "center", "bottom"),      # above its marker
    "Girard-Sahun 2022 OP003": ((-8, -6), "right", "center"), # left of the halo, clear of Kim
}
TWO_LINE = {"O'Modhrain 2024 OP001", "Girard-Sahun 2022 OP003"}   # name above power, to fit the crowded corner
LEAD = {"O'Modhrain 2024 OP001": (25.5, 2.4)}   # label at a free spot (data coords) with a thin leader line


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


def power_text(v):
    if v >= 10:
        return f"{v:.0f} kW"
    if v >= 1:
        return f"{v:.1f}".rstrip("0").rstrip(".") + " kW"
    return f"{v * 1000:.0f} W"


def ms_of(mk):
    return 9 if mk == "*" else (6.5 if mk == "p" else 5.5)


pts = []
for r in rows:
    if r["headline"] != "yes" or r["source_id"] in BENCH or r["row_key"] in SKIP:
        continue
    bed = "C bed" in r["route"]
    c = f(r["carbon_kg_per_Nm3_CO"])
    if bed and c is None:
        continue
    wall_m = f(r["EC_CO_wall_measured_low"])
    lo, hi = (wall_m, f(r["EC_CO_wall_measured_high"]) or wall_m) if wall_m else \
        (f(r["EC_CO_industrial_est_low"]), f(r["EC_CO_industrial_est_high"]))
    cin = c * LHV_C if bed else 0.0
    mid = (lo * hi) ** 0.5
    eta = dict(lo=LHV_CO / (hi + cin) * 100, hi=LHV_CO / (lo + cin) * 100, mid=LHV_CO / (mid + cin) * 100)
    author = r["row_key"].rsplit(" ", 2)[0]
    pts.append(dict(key=r["row_key"], fam=family(r["route"]), x=num(r["X_CO2_pct"]), eta=eta, bed=bed,
                    label=f"{author} {power_text(f(r['P_kW_at_boundary']))}"))

s = {r["row_key"]: r for r in rows}["Hecimovic 2024 OP001"]
soec_eta, soec_x = LHV_CO / f(s["EC_CO_wall_measured_low"]) * 100, num(s["X_CO2_pct"])

fig, ax = plt.subplots(figsize=(5.06, 4.2))
ax.plot(soec_eta, soec_x, marker="h", ms=7, mfc=INK, mec=INK, ls="none", zorder=4)
ax.annotate("SOEC system", (soec_eta, soec_x), xytext=(-7, 0), textcoords="offset points", fontsize=7.5,
            color=INK, ha="right", va="center")
for p in pts:
    col, mk, _ = STYLE[p["fam"]]
    e = p["eta"]
    if p["bed"]:
        ax.plot([e["lo"] - 0.5, e["hi"] + 0.5], [p["x"]] * 2, color=HALO, lw=10.5, solid_capstyle="round", zorder=1.5)
    if e["hi"] - e["lo"] > 0.3:
        ax.errorbar(e["mid"], p["x"], xerr=[[e["mid"] - e["lo"]], [e["hi"] - e["mid"]]], fmt="none", ecolor=col,
                    elinewidth=0.9, capsize=2, capthick=0.9, zorder=2)
    ax.plot(e["mid"], p["x"], marker=mk, ms=ms_of(mk), mfc=col, mec=col, ls="none", zorder=3)
    (dx, dy), ha, va = OFFSET.get(p["key"], ((6, 0), "left", "center"))
    anchor = e["hi"] if ha == "left" else (e["lo"] if ha == "right" else e["mid"])
    text = p["label"].replace(" ", "\n", 1) if p["key"] in TWO_LINE else p["label"]
    if p["key"] in LEAD:
        ax.annotate(text, (e["mid"], p["x"]), xytext=LEAD[p["key"]], textcoords="data", fontsize=7.5, color=INK,
                    ha="left", va="center", linespacing=1.0,
                    arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.6, shrinkA=1, shrinkB=4))
        continue
    ax.annotate(text, (anchor, p["x"]), xytext=(dx, dy), textcoords="offset points", fontsize=7.5,
                color=INK, ha=ha, va=va, linespacing=1.0)

ax.set_xlim(0, 100)
ax.set_ylim(0, 92)
ax.grid(True, color=GRID, lw=0.7)
ax.set_axisbelow(True)
ax.set_xlabel(r"LHV efficiency, $\eta_{\mathrm{LHV}}$ (%)")
ax.set_ylabel(r"CO$_2$ conversion (%)")

x0 = ax.get_position().x1 + 0.03
kw = dict(frameon=False, fontsize=7.5, handletextpad=0.4, labelspacing=0.5, alignment="left",
          title_fontproperties={"size": 7.5, "weight": "bold"}, borderaxespad=0)
h_type = [Line2D([], [], marker=mk, color=col, ls="", ms=ms_of(mk), label=lab) for col, mk, lab in STYLE.values()]
h_basis = [Line2D([], [], marker="o", color=MUTED, ls="", ms=5.5, label="plasma, at the wall"),
           Line2D([], [], marker="h", color=INK, ls="", ms=7, label="SOEC system, at the wall"),
           Line2D([], [], marker="o", color=HALO, ls="", ms=9.5, label="carbon bed (carbon LHV\ncounted as input)")]
y = ax.get_position().y1 + 0.02
for title, h in (("Plasma type", h_type), ("Energy basis", h_basis)):
    leg = fig.legend(handles=h, loc="upper left", bbox_to_anchor=(x0, y), title=title, **kw)
    leg.get_title().set_color(INK)
    fig.canvas.draw()
    y = leg.get_window_extent().transformed(fig.transFigure.inverted()).y0 - 0.035

for ext in ("png", "svg"):
    fig.savefig(FIG / f"co2_x_vs_eta_lhv.{ext}", dpi=300, bbox_inches="tight")
for p in sorted(pts, key=lambda q: -q["eta"]["mid"]):
    print(f"{p['key']:26s} X {p['x']:5.1f}  eta_LHV {p['eta']['lo']:5.1f}-{p['eta']['hi']:5.1f}")
print(f"SOEC system: X {soec_x}, eta_LHV {soec_eta:.1f}%")
