"""CH4 conversion vs energy per mol CH4 converted (EC_CH4), plasma reforming against the fired SMR reference.

Reads reforming_synthesis.csv (no data values in this script except the fired-SMR reference rows, which are
copied from build_synthesis.py FIRED). Two panels, same axes:
  (a) EC_CH4 at each paper's power boundary (arc, absorbed microwave, RF generator, discharge, plasma);
  (b) EC_CH4 with a representative industrial supply (EC_CH4 / class efficiency; bar = class range).
Colour = route (SMR, DRM, mixed); marker = activation. External heat (furnace, steam generation) is excluded
from every plasma point. References: reaction enthalpy at 298 K (SMR 206, DRM 247 kJ/mol); fired SMR design
references (NETL, IEAGHG) on a heat basis: filled hexagon = burner fuel (HHV), open hexagon = heat absorbed by
the tubes; heat, not electricity. Joule-heated pilot (From 2024): reviewer estimate (SRC005-C004), open star with
bars spanning the EC range and the equilibrium conversion range; other Joule rows have no energy value.

Run from the repository root: ~/.venvs/science/bin/python literature_reforming/0_synthesis/plot_x_vs_ec.py
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
rows = list(csv.DictReader(open(HERE / "reforming_synthesis.csv", encoding="utf-8")))

BLUE, ORANGE, AQUA = "#2a78d6", "#eb6834", "#1baf7a"
INK, MUTED, GRID = "#1f1f1e", "#6b6a64", "#e4e3de"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 8.5, "axes.edgecolor": MUTED,
                     "axes.labelcolor": INK, "xtick.color": MUTED, "ytick.color": MUTED,
                     "axes.spines.top": False, "axes.spines.right": False,
                     "svg.fonttype": "none", "savefig.facecolor": "white"})
ROUTE = {"SMR": BLUE, "DRM": ORANGE, "mixed": AQUA}
ACT = [  # (match in activation string, marker, legend label)
    ("arc torch", "P", "DC arc torch"), ("915", "s", "microwave 915 MHz"), ("2.45", "o", "microwave 2.45 GHz"),
    ("ICP", "X", "RF ICP torch"), ("GA", "^", "gliding arc"), ("gliding arc", "^", "gliding arc"),
    ("glow", "D", "DC glow"), ("DBD", "v", "DBD"),
]
DH = {"SMR": 206, "DRM": 247}
FIRED = [("NETL", 77.7, 340, 577), ("IEAGHG", 84.6, 315, 574)]   # name, X_CH4, EC_abs, EC_fired (build_synthesis FIRED)


def marker(act):
    for k, m, _ in ACT:
        if k in act:
            return m
    return None


def f(s):
    return float(s) if s not in ("", None) else None


def num(s):
    m = re.search(r"[\d.]+", s or "")
    return float(m.group()) if m else None


pts = []
for r in rows:
    mk = marker(r["activation"])
    x = num(r["X_CH4_pct"])
    if mk is None or x is None or not f(r["EC_CH4_low"]):
        continue
    pts.append(dict(key=r["row_key"], route=r["route"], mk=mk, x=x, head=r["headline"] == "yes",
                    paper=(f(r["EC_CH4_low"]), f(r["EC_CH4_high"])),
                    est=(f(r["EC_CH4_industrial_est_low"]), f(r["EC_CH4_industrial_est_high"]))))

JOULE_PTS = []   # Joule rows with an energy value (reviewer estimate); X given as a range "94-97 (...)"
for r in rows:
    if "Joule" in r["activation"] and f(r["EC_CH4_low"]):
        xs = [float(v) for v in re.findall(r"[\d.]+", r["X_CH4_pct"])[:2]]
        JOULE_PTS.append(dict(x=(min(xs), max(xs)), paper=(f(r["EC_CH4_low"]), f(r["EC_CH4_high"])),
                              est=(f(r["EC_CH4_industrial_est_low"]), f(r["EC_CH4_industrial_est_high"]))))

LABEL = {"Hrabovsky 2018 OP001": "Hrabovsky", "Akande 2022 OP008": "Akande", "Hrycak 2023 OP002": "Hrycak",
         "Zhu 2019 OP004": "Zhu (Ni cat.)", "Geng 2022 OP002": "Geng", "Song 2020 OP013": "Song",
         "Kelly 2023 OP004": "Kelly", "Kwon 2023 OP003": "Kwon", "Wanten 2022 OP006": "Wanten", "Kaufmann 2026 OP002": "Kaufmann",
         "Andersen 2020 OP001": "Andersen", "Hrabovsky 2018 OP005": "Hrabovsky", "Hrycak 2023 OP001": "Hrycak"}
OFFSET = {   # (dx, dy, ha, va) in points where the default collides
    "Hrabovsky 2018 OP001": (6, -4, "left", "top"),
    "Hrabovsky 2018 OP005": (7, 0, "left", "center"),
    "Akande 2022 OP008": (-6, 0, "right", "center"),
    "Kwon 2023 OP003": (5, -3, "left", "top"),
}

fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.8), sharey=True)
for ax, panel in zip(axes, ("paper", "est")):
    for route, dh in DH.items():
        ax.axvline(dh, color=ROUTE[route], lw=1, ls="--", alpha=0.7, zorder=1)
    ax.text(DH["SMR"] * 0.97, 2, "ΔH SMR", rotation=90, fontsize=6.8, color=MUTED, ha="right", va="bottom")
    ax.text(DH["DRM"] * 1.03, 2, "ΔH DRM", rotation=90, fontsize=6.8, color=MUTED, ha="left", va="bottom")
    for name, x, ec_abs, ec_fired in FIRED:
        ax.plot([ec_abs, ec_fired], [x, x], color=INK, lw=0.8, zorder=4)
        ax.plot(ec_fired, x, marker="h", ms=8, mfc=INK, mec="white", mew=0.8, ls="none", zorder=5)
        ax.plot(ec_abs, x, marker="h", ms=8, mfc="white", mec=INK, mew=1.2, ls="none", zorder=5)
    ax.text(292, 81.2, "fired SMR\n(heat basis)", fontsize=6.6, color=INK, ha="right", va="center",
            bbox=dict(boxstyle="round,pad=0.15", fc="white", ec="none", alpha=0.85), zorder=6)
    for j in JOULE_PTS:
        lo, hi = j["paper"] if panel == "paper" else j["est"]
        xc, ym = (lo * hi) ** 0.5, sum(j["x"]) / 2
        ax.plot([lo, hi], [ym, ym], color=INK, lw=1.2, zorder=4)
        ax.plot([xc, xc], list(j["x"]), color=INK, lw=1.2, zorder=4)
        ax.plot(xc, ym, marker="*", ms=12, mfc="white", mec=INK, mew=1.2, ls="none", zorder=5)
        ax.annotate("Joule pilot\n(est.)", (lo, ym), xytext=(-5, 0), textcoords="offset points", fontsize=6.8,
                    color=INK, ha="right", va="center",
                    bbox=dict(boxstyle="round,pad=0.15", fc="white", ec="none", alpha=0.85), zorder=6)
    for p in pts:
        col = ROUTE[p["route"]]
        lo, hi = p["paper"] if panel == "paper" else p["est"]
        xc = (lo * hi) ** 0.5
        if hi / lo > 1.02:
            ax.plot([lo, hi], [p["x"]] * 2, color=col, lw=1.5, alpha=0.6, zorder=2, solid_capstyle="round")
        ax.plot(xc, p["x"], marker=p["mk"], ms=8 if p["mk"] in "PX" else 7, mfc=col, mec="white", mew=0.8,
                ls="none", zorder=3, alpha=1.0 if p["head"] else 0.5)
        if p["head"] and p["key"] in LABEL:
            dx, dy, ha, va = OFFSET.get(p["key"], (5, 3, "left", "bottom"))
            ax.annotate(LABEL[p["key"]], (xc, p["x"]), xytext=(dx, dy), textcoords="offset points",
                        fontsize=6.8, color=INK, ha=ha, va=va)
    ax.set_xscale("log")
    ax.set_xlim(150, 15000)
    ax.set_ylim(0, 100)
    ax.set_xticks([200, 300, 500, 1000, 2000, 5000, 10000])
    ax.xaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: f"{v:g}"))
    ax.xaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
    ax.grid(True, which="major", color=GRID, lw=0.6)
    ax.set_axisbelow(True)
    ax.set_xlabel("Energy per mol CH4 converted, EC_CH4 (kJ/mol)")
ax0, ax1 = axes
ax0.set_title("(a) at each paper's power boundary", loc="left", fontsize=9, color=INK)
ax1.set_title("(b) with a representative industrial supply", loc="left", fontsize=9, color=INK)
ax0.set_ylabel("CH4 conversion (%)")

handles = [Line2D([], [], marker="s", color=c, ls="none", ms=7, mec="white", label=r) for r, c in ROUTE.items()]
seen = []
for _, m, lab in ACT:
    if lab not in seen:
        seen.append(lab)
        handles.append(Line2D([], [], marker=m, color=MUTED, ls="none", ms=7, mec="white", label=lab))
handles += [Line2D([], [], marker="h", mfc=INK, mec="white", ls="none", ms=8, label="fired SMR: fuel (HHV)"),
            Line2D([], [], marker="h", mfc="white", mec=INK, mew=1.2, ls="none", ms=8, label="fired SMR: absorbed heat"),
            Line2D([], [], marker="*", mfc="white", mec=INK, mew=1.2, ls="none", ms=11,
                   label="Joule-heated pilot (reviewer estimate)"),
            Line2D([], [], color=MUTED, lw=1.5, alpha=0.6, label="range (supply class)")]
fig.legend(handles=handles, loc="lower center", ncol=7, frameon=False, fontsize=7.3, bbox_to_anchor=(0.5, -0.03))
fig.tight_layout(rect=(0, 0.1, 1, 1))
for ext in ("png", "svg"):
    fig.savefig(HERE / f"reforming_x_vs_ec.{ext}", dpi=200, bbox_inches="tight")
print(f"{len(pts)} plasma points plotted")
