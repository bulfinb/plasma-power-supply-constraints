"""CO2 conversion vs energy per CO, plasma exemplars against the SOEC benchmark.

Reads co2_synthesis.csv (no data values in this script). Two panels, same axes:
  (a) EC_CO at each paper's own power boundary (absorbed, plasma, deposited, plug);
  (b) EC_CO at the wall: measured where the authors measured it, else the industrial-supply estimate
      (bar = class efficiency range). Carbon-bed points are hollow (electricity only; carbon not counted).
References: 100% on dH (3.50 kWh/Nm3, vertical line); SOEC stack DC band (Kungas 2020; conversion not reported,
heat below V_tn excluded); SOEC system point at its 86% utilisation (Hecimovic 2024 OP001: stack DC in (a),
wall incl. 0.95 rectifier in (b)).
The O2-membrane demonstrator (Hecimovic 2024 OP005) and vendor eCOs figure are not plotted (not matched points).

Run from the repository root: python3 literature_co2_splitting/0_synthesis/plot_x_vs_ec.py
"""
import csv
import re
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker
from matplotlib.lines import Line2D

HERE = Path(__file__).resolve().parent
FIG = HERE / "figures"   # figure outputs (scripts and data stay in this folder)
FIG.mkdir(exist_ok=True)
rows = list(csv.DictReader(open(HERE / "co2_synthesis.csv", encoding="utf-8")))

# Reference categorical palette (dataviz skill, light mode), first three slots (validated all-pairs for scatter).
BLUE, ORANGE, AQUA = "#2a78d6", "#eb6834", "#1baf7a"
INK, MUTED, GRID, BAND = "#1f1f1e", "#6b6a64", "#e4e3de", "#d9d8d2"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 8.5, "axes.edgecolor": MUTED,
                     "axes.labelcolor": INK, "xtick.color": MUTED, "ytick.color": MUTED,
                     "axes.spines.top": False, "axes.spines.right": False,
                     "svg.fonttype": "none", "savefig.facecolor": "white"})

# Discharge family -> colour (group) and marker (subtype)
STYLE = {
    "MW 2.45 GHz": (BLUE, "o"), "MW 915 MHz": (BLUE, "s"),
    "GA (AC)": (ORANGE, "^"), "GA (DC)": (ORANGE, "D"), "DC glow-to-arc": (ORANGE, "p"),
    "NRP": (AQUA, "*"), "DBD": (AQUA, "v"),
}


def family(route):
    for k in STYLE:
        if route.startswith(k) or (k == "NRP" and route.startswith("NRP")) or (k == "DBD" and "DBD" in route):
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
    if fam is None or x is None or r["source_id"] in ("SRC025", "SRC026"):
        continue
    corr = re.search(r"\(([\d.]+) corr", r["X_CO2_pct"])
    wall = (f(r["EC_CO_wall_measured_low"]), f(r["EC_CO_wall_measured_high"]))
    est = (f(r["EC_CO_industrial_est_low"]), f(r["EC_CO_industrial_est_high"]))
    pts.append(dict(key=r["row_key"], fam=fam, x=x, x_corr=float(corr.group(1)) if corr else None,
                    paper=(f(r["EC_CO_boundary_low"]), f(r["EC_CO_boundary_high"])),
                    wall=wall if wall[0] else None, est=est if est[0] else None,
                    bed="C bed" in r["route"], head=r["headline"] == "yes"))

soec = {r["row_key"]: r for r in rows if r["source_id"] in ("SRC025", "SRC026")}
stack = (min(f(soec[k]["EC_CO_boundary_low"]) for k in soec if k.startswith("Kungas")),
         max(f(soec[k]["EC_CO_boundary_high"]) for k in soec if k.startswith("Kungas")))
sys_row = soec["Hecimovic 2024 OP001"]
system = (f(sys_row["EC_CO_boundary_low"]), f(sys_row["EC_CO_wall_measured_high"]))   # (stack DC, wall)
sys_x = num(sys_row["X_CO2_pct"])                                                    # utilisation (%)
EC_DH = 3.50

LABEL = {  # short direct labels for headline points (author only)
    "Kiefer 2024 OP001": "Kiefer", "Kiefer 2024 OP003": "Kiefer", "Hecimovic 2023 OP002": "Hecimovic 23",
    "Bongers 2017 OP001": "Bongers", "Bongers 2017 OP003": "Bongers", "Girard-Sahun 2022 OP001": "Girard-Sahun",
    "Girard-Sahun 2022 OP002": "Girard-Sahun (peak, C)", "O'Modhrain 2024 OP001": "O'Modhrain",
    "Bryssinck 2025 OP003": "Bryssinck (C)", "Renninger 2022 OP001": "Renninger", "Yong 2023 OP001": "Yong",
    "Van Laer 2015 OP001": "Van Laer", "Van Laer 2015 OP003": "Van Laer",
}

OFFSET = {  # label placement (points, ha, va) where the default collides
    "Hecimovic 2023 OP002": (-6, 2, "right", "bottom"),
    "Kiefer 2024 OP003": (6, 2, "left", "bottom"),
    "Girard-Sahun 2022 OP001": ("data", 8.6, 1.4, "right"),
    "O'Modhrain 2024 OP001": (6, -1, "left", "center"),
    "Bryssinck 2025 OP003": (-7, 4, "right", "bottom"),
    "Girard-Sahun 2022 OP002": ("data", 4.4, 36, "left"),
    "Bongers 2017 OP003": (-6, 0, "right", "center"),
}

fig, axes = plt.subplots(1, 2, figsize=(10, 4.6), sharey=True)
for ax, panel in zip(axes, ("paper", "wall")):
    ax.axvspan(*stack, color=BAND, alpha=0.55, lw=0, zorder=0)
    ax.plot([EC_DH, EC_DH], [0, 74], color=MUTED, lw=1, ls="--", zorder=1)   # stops below the stack label
    ax.text(stack[0] * 1.03, 99, "SOEC\nstack DC\n(conv. NR,\nheat\nexcl.)", fontsize=6.3, color=MUTED, va="top")
    sx = system[0] if panel == "paper" else system[1]
    ax.plot(sx, sys_x, marker="h", ms=9, mfc=INK, mec="white", mew=0.8, ls="none", zorder=5)
    ax.annotate(f"SOEC system\n({sys_x:.0f}% utilisation)", (sx, sys_x), xytext=(7, 0), textcoords="offset points",
                fontsize=6.8, color=INK, va="center")
    ax.text(EC_DH * 0.97, 2, "100% on ΔH", rotation=90, fontsize=7, color=MUTED, ha="right", va="bottom")
    for p in pts:
        col, mk = STYLE[p["fam"]]
        if panel == "paper":
            lo, hi = p["paper"]
        elif p["wall"]:
            lo, hi = p["wall"]
        else:
            lo, hi = p["est"]
        xc = (lo * hi) ** 0.5
        face = "white" if p["bed"] else col
        ms = 11 if mk == "*" else 7
        if hi / lo > 1.02:
            ax.plot([lo, hi], [p["x"]] * 2, color=col, lw=1.5, alpha=0.6, zorder=2, solid_capstyle="round")
        if p["x_corr"] is not None:
            ax.plot([xc, xc], [p["x_corr"], p["x"]], color=col, lw=1, ls=":", zorder=2)
            ax.plot(xc, p["x_corr"], marker=mk, ms=ms * 0.6, mfc="white", mec=col, mew=1, ls="none", zorder=3)
        ax.plot(xc, p["x"], marker=mk, ms=ms, mfc=face, mec=col if p["bed"] else "white", mew=1.4 if p["bed"] else 0.8,
                ls="none", zorder=4, alpha=1.0 if p["head"] else 0.55)
        if p["head"] and p["key"] in LABEL:
            o = OFFSET.get(p["key"], (5, 3, "left", "bottom"))
            if o[0] == "data":   # fixed text position with a thin leader line
                ax.annotate(LABEL[p["key"]], (xc, p["x"]), xytext=(o[1], o[2]), textcoords="data", fontsize=6.8,
                            color=INK, ha=o[3], va="center",
                            arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.6, shrinkA=1, shrinkB=4))
            else:
                ax.annotate(LABEL[p["key"]], (xc, p["x"]), xytext=o[:2], textcoords="offset points",
                            fontsize=6.8, color=INK, ha=o[2], va=o[3])
    ax.set_xscale("log")
    ax.set_xlim(2, 130)
    ax.set_ylim(0, 100)
    ax.xaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: f"{v:g}"))
    ax.set_xticks([2, 3, 5, 10, 20, 50, 100])
    ax.grid(True, which="major", color=GRID, lw=0.6)
    ax.set_axisbelow(True)
ax0, ax1 = axes
ax0.set_title("(a) at each paper's power boundary", loc="left", fontsize=9, color=INK)
ax1.set_title("(b) at the wall: measured, or with an industrial supply", loc="left", fontsize=9, color=INK)
ax0.set_ylabel("CO₂ conversion, single pass (%)")
for ax in axes:
    ax.set_xlabel("Electricity per CO (kWh/Nm³ CO)")

handles = [Line2D([], [], marker=STYLE[k][1], color=STYLE[k][0], mec="white", ls="none",
                  ms=11 if STYLE[k][1] == "*" else 7, label=k) for k in STYLE]
handles += [Line2D([], [], marker="h", mfc=INK, mec="white", ls="none", ms=9, label="SOEC system (Hecimovic 2024)"),
            Line2D([], [], marker="o", mfc="white", mec=MUTED, mew=1.4, ls="none", ms=7,
                   label="carbon bed (+0.21-0.27 kg C/Nm³ CO)"),
            Line2D([], [], color=MUTED, lw=1.5, alpha=0.6, label="range (supply class / volume)"),
            Line2D([], [], color=MUTED, lw=1, ls=":", marker="o", mfc="white", ms=4,
                   label="if expansion-corrected")]
fig.legend(handles=handles, loc="lower center", ncol=5, frameon=False, fontsize=7.5, bbox_to_anchor=(0.5, -0.02))
fig.tight_layout(rect=(0, 0.1, 1, 1))
for ext in ("png", "svg"):
    fig.savefig(FIG / f"co2_x_vs_ec.{ext}", dpi=200, bbox_inches="tight")
print(f"{len(pts)} plasma points; SOEC stack {stack}, system {system}")
