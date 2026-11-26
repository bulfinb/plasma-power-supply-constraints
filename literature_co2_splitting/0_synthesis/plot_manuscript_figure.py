"""Manuscript figure: CO2 conversion vs electricity per Nm3 CO, plasma CO2-splitting headline points against SOEC
(no data values in this script; reads co2_synthesis.csv).

Publication version of co2_x_vs_ec (plot_x_vs_ec.py, kept as the working/SI figure); same conventions as the
reforming manuscript figure (literature_reforming/0_synthesis/plot_manuscript_figure.py):
- the plasma rows of the manuscript table (make_latex_table.py: headline rows minus SKIP);
- open marker = EC_CO at the paper's power boundary; filled marker = at the wall (measured where the authors measured
  it, else EC_CO plasma side / supply-class efficiency, geometric mid; bar = class range); thin line joins the pair;
- labels: author and reported power (W below 1 kW);
- carbon-bed points: grey halo behind the open/filled pair (carbon not counted as energy) (BB 2026-11-25);
- Hecimovic 2023 OP002 not plotted: same torch as Kiefer 2024, whose wall-plug values are measured (BB 2026-11-25);
- DBD conversions as reported (expansion-corrected values are in the table only);
- SOEC: the system design point (Hecimovic 2024 OP001) at its 86% utilisation, open = stack DC, filled = wall; the
  stack-only band (Kungas 2020, no conversion, heat below V_tn excluded) is left to the table note (BB 2026-11-25);
  reaction enthalpy line at 3.50 kWh/Nm3 CO.

Writes 0_manuscript_figure.png/.svg/.pdf here and copies the pdf/png to manuscript/figures/co2_figure.*.
Run from the repository root: ~/.venvs/science/bin/python literature_co2_splitting/0_synthesis/plot_manuscript_figure.py
"""
import csv
import re
import shutil
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker
from matplotlib.lines import Line2D

HERE = Path(__file__).resolve().parent
MS_FIG = HERE.parent.parent / "manuscript" / "figures"
rows = list(csv.DictReader(open(HERE / "co2_synthesis.csv", encoding="utf-8")))
BENCH = {"SRC025", "SRC026"}
SKIP = {"Hecimovic 2024 OP005", "Girard-Sahun 2022 OP001",   # as make_latex_table.py SKIP (plasma rows)
        "Hecimovic 2023 OP002"}                              # same torch as Kiefer 2024 (measured wall): shown once

SLOT = ["#2a78d6", "#eb6834", "#1baf7a"]
INK, MUTED, GRID, HALO = "#1f1f1e", "#6b6a64", "#e4e3de", "#d2d1cb"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 8.5, "axes.edgecolor": MUTED,
                     "axes.labelcolor": INK, "xtick.color": MUTED, "ytick.color": MUTED,
                     "axes.spines.top": False, "axes.spines.right": False,
                     "svg.fonttype": "none", "savefig.facecolor": "white"})
# Discharge -> (colour by family, marker, legend label); legend order as listed
STYLE = {
    "MW 2.45 GHz": (SLOT[0], "o", "microwave 2.45 GHz"), "MW 915 MHz": (SLOT[0], "s", "microwave 915 MHz"),
    "GA (AC)": (SLOT[1], "^", "gliding arc, AC"), "GA (DC)": (SLOT[1], "D", "gliding arc, DC"),
    "DC glow-to-arc": (SLOT[1], "p", "DC glow-to-arc"),
    "NRP": (SLOT[2], "*", "nanosecond pulsed"), "DBD": (SLOT[2], "v", "packed-bed DBD"),
}
EC_DH = 3.50
XMIN, XMAX, YMIN, YMAX = 3, 100, 0, 92
OFFSET = {   # label position: (dx, dy) points, ha, va; anchor rule as in the reforming figure
    "Kiefer 2024 OP001": ((6, 0), "left", "center"),
    "Kiefer 2024 OP003": ((6, 0), "left", "center"),
    "Bongers 2017 OP001": ((6, 0), "left", "center"),
    "Bongers 2017 OP003": ((0, 6), "center", "bottom"),      # centred above the pair (BB 2026-11-26)
    "Kim 2014 OP002": ((0, -7), "center", "top"),             # below, centred on the pair
    "Girard-Sahun 2022 OP002": ((-7, 6), "left", "bottom"),  # two lines, just above the grey halo (BB 2026-11-26)
    "Girard-Sahun 2022 OP003": ((7, -3), "left", "center"),  # close to the markers, slightly down
    "Renninger 2022 OP001": ((2, 5), "left", "center"),      # BB 2026-11-25: up about a marker width
    "Bryssinck 2025 OP003": ((6, 5), "left", "center"),
    "Yong 2023 OP001": ((-10, 3), "left", "bottom"),         # just above the end of the range bar
    "O'Modhrain 2024 OP001": ((6, 0), "left", "center"),     # right, two lines (see TWO_LINE)
    "Van Laer 2015 OP001": ((0, 6), "center", "bottom"),     # above, centred on the pair
    "Van Laer 2015 OP003": ((6, 0), "left", "center"),       # right of the pair
}
ANCHOR_OPEN = {"Girard-Sahun 2022 OP002"}   # label starts over the open marker, between the dH line and Bryssinck
TWO_LINE = {"O'Modhrain 2024 OP001", "Girard-Sahun 2022 OP002"}   # name above power, to keep clear of Van Laer


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


pts = []
for r in rows:
    if r["headline"] != "yes" or r["source_id"] in BENCH or r["row_key"] in SKIP:
        continue
    fam = family(r["route"])
    wall_m = f(r["EC_CO_wall_measured_low"])
    wall = (wall_m, f(r["EC_CO_wall_measured_high"]) or wall_m) if wall_m else \
        (f(r["EC_CO_industrial_est_low"]), f(r["EC_CO_industrial_est_high"]))
    author = r["row_key"].rsplit(" ", 2)[0]
    label = f"{author} {power_text(f(r['P_kW_at_boundary']))}"
    pts.append(dict(key=r["row_key"], fam=fam, x=num(r["X_CO2_pct"]), paper=f(r["EC_CO_boundary_low"]),
                    paper_hi=f(r["EC_CO_boundary_high"]), wall=wall, label=label, bed="C bed" in r["route"]))

soec = {r["row_key"]: r for r in rows if r["source_id"] in BENCH}
sys_row = soec["Hecimovic 2024 OP001"]
sys_dc, sys_wall, sys_x = f(sys_row["EC_CO_boundary_low"]), f(sys_row["EC_CO_wall_measured_low"]), num(sys_row["X_CO2_pct"])

fig, ax = plt.subplots(figsize=(5.06, 4.2))   # taller than the reforming figure: crowded below 20%
ax.axvline(EC_DH, color=MUTED, lw=0.9, ls=(0, (3, 2)), zorder=1)
ax.text(EC_DH * 1.025, YMIN + 1.5, r"$\Delta H^\circ$", rotation=90, fontsize=7, color=MUTED, ha="left", va="bottom")

ax.plot([sys_dc, sys_wall], [sys_x, sys_x], color=INK, lw=0.8, zorder=3)
ax.plot(sys_dc, sys_x, marker="h", ms=7, mfc="white", mec=INK, mew=1.2, ls="none", zorder=4)
ax.plot(sys_wall, sys_x, marker="h", ms=7, mfc=INK, mec=INK, ls="none", zorder=4)
ax.annotate("SOEC system", (sys_wall, sys_x), xytext=(6, 0), textcoords="offset points", fontsize=7.5, color=INK,
            ha="left", va="center")

for p in pts:
    col, mk, _ = STYLE[p["fam"]]
    lo, hi = p["wall"]
    xe = (lo * hi) ** 0.5
    xp = (p["paper"] * p["paper_hi"]) ** 0.5
    ms = 9 if mk == "*" else (6.5 if mk == "p" else 5.5)
    if p["bed"]:   # carbon bed: rounded grey halo behind the pair
        ax.plot([min(xp, xe) / 1.003, max(xp, xe) * 1.003], [p["x"]] * 2, color=HALO, lw=13,
                solid_capstyle="round", zorder=1.5)   # widened slightly so a single point (Bryssinck) still shows
    ax.plot([xp, xe], [p["x"]] * 2, color=col, lw=0.8, alpha=0.6, zorder=2)
    if hi / lo > 1.02:
        ax.errorbar(xe, p["x"], xerr=[[xe - lo], [hi - xe]], fmt="none", ecolor=col, elinewidth=0.9, capsize=2,
                    capthick=0.9, zorder=2)
    ax.plot(xp, p["x"], marker=mk, ms=ms, mfc="white", mec=col, mew=1.2, ls="none", zorder=3)
    ax.plot(xe, p["x"], marker=mk, ms=ms, mfc=col, mec=col, mew=1.0, ls="none", zorder=3)
    (dx, dy), ha, va = OFFSET.get(p["key"], ((6, 0), "left", "center"))
    anchor = {"left": max(hi, xe), "right": min(xp, lo)}.get(ha, (xp * xe) ** 0.5)
    if p["key"] in ANCHOR_OPEN:
        anchor = xp
    text = p["label"].replace(" ", "\n", 1) if p["key"] in TWO_LINE else p["label"]
    ax.annotate(text, (anchor, p["x"]), xytext=(dx, dy), textcoords="offset points", fontsize=7.5,
                color=INK, ha=ha, va=va, linespacing=1.0)

ax.set_xscale("log")
ax.set_xlim(XMIN, XMAX)
ax.set_ylim(YMIN, YMAX)
ax.set_xticks([3, 5, 10, 20, 50, 100])
ax.xaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: f"{v:g}"))
ax.xaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
ax.grid(True, which="major", color=GRID, lw=0.7)
ax.set_axisbelow(True)
ax.set_xlabel(r"Electricity per CO, EC$_{\mathrm{CO}}$ (kWh Nm$^{-3}$)")
ax.set_ylabel(r"CO$_2$ conversion (%)")

x0 = ax.get_position().x1 + 0.03
kw = dict(frameon=False, fontsize=7.5, handletextpad=0.4, labelspacing=0.5, alignment="left",
          title_fontproperties={"size": 7.5, "weight": "bold"}, borderaxespad=0)
h_type = [Line2D([], [], marker=mk, color=col, ls="", ms=9 if mk == "*" else (6.5 if mk == "p" else 5.5), label=lab)
          for col, mk, lab in STYLE.values()]
h_basis = [Line2D([], [], marker="o", mfc="white", mec=MUTED, mew=1.2, ls="", ms=5.5, label="at reported power boundary"),
           Line2D([], [], marker="o", color=MUTED, ls="", ms=5.5, label="at the wall"),
           Line2D([], [], marker="h", mfc="white", mec=INK, mew=1.2, ls="", ms=7, label="SOEC system: stack DC"),
           Line2D([], [], marker="h", color=INK, ls="", ms=7, label="SOEC system: wall"),
           Line2D([], [], marker="o", color=HALO, ls="", ms=12, label="carbon bed (carbon consumed)")]
y = ax.get_position().y1 + 0.02
for title, h in (("Plasma type", h_type), ("Energy basis", h_basis)):
    leg = fig.legend(handles=h, loc="upper left", bbox_to_anchor=(x0, y), title=title, **kw)
    leg.get_title().set_color(INK)
    fig.canvas.draw()
    y = leg.get_window_extent().transformed(fig.transFigure.inverted()).y0 - 0.035

for ext in ("png", "svg", "pdf"):
    fig.savefig(HERE / f"0_manuscript_figure.{ext}", dpi=300, bbox_inches="tight")
for ext in ("png", "pdf"):
    shutil.copy(HERE / f"0_manuscript_figure.{ext}", MS_FIG / f"co2_figure.{ext}")
print(f"{len(pts)} plasma points; SOEC system {sys_dc}->{sys_wall} at {sys_x}%")
