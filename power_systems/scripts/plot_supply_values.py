"""Figures from supply_values.csv (no data values in this script).

1. figures/supply_cost_per_kw.png/.svg  - every cost-per-kW value, grouped by supply class,
   coloured and shaped by what the price covers. Nominal currency and price year as stated;
   no currency or inflation conversion (USD and EUR are shown separately).
2. figures/supply_power_efficiency_frequency.png/.svg - unit power and efficiency against
   output frequency, coloured and shaped by what the efficiency refers to.

Run from power_systems/: python3 scripts/plot_supply_values.py
"""
import csv
import math
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "figures"
OUT.mkdir(exist_ok=True)
rows = list(csv.DictReader(open(ROOT / "supply_values.csv", encoding="utf-8")))

# Reference categorical palette (dataviz skill, light mode), slots in fixed order.
SLOT = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4"]
INK, MUTED, GRID = "#1f1f1e", "#6b6a64", "#e4e3de"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 9, "axes.edgecolor": MUTED,
                     "axes.labelcolor": INK, "xtick.color": MUTED, "ytick.color": MUTED,
                     "axes.spines.top": False, "axes.spines.right": False,
                     "svg.fonttype": "none", "savefig.facecolor": "white"})
ONE_SIDED = {">", ">=", "<", "<=", "up_to", "approaching"}


def num(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def save(fig, name):
    for ext in ("png", "svg"):
        fig.savefig(OUT / f"{name}.{ext}", dpi=200, bbox_inches="tight")
    plt.close(fig)
    print("wrote", OUT / f"{name}.png")


def short(t, n=46):
    t = t.split(" (")[0] if len(t) > n else t
    if len(t) <= n:
        return t
    return t[:n].rsplit(" ", 1)[0] + "..."


# ---------- 1. cost per kW ----------
SCOPE = {  # what the price covers -> (label, colour, marker)
    "tube_only": ("tube only", SLOT[0], "o"),
    "supply": ("supply", SLOT[1], "s"),
    "turnkey_system": ("turnkey system (supply + source)", SLOT[2], "D"),
    "supply_plus_reactor": ("supply + reactor", SLOT[3], "^"),
    "not_stated": ("scope not stated", SLOT[4], "v"),
}
CLASS_ORDER = ["K1", "M1", "P1", "H1"]
cost = [r for r in rows if r["quantity"] == "cost_per_kw" and num(r["value_low"])]
cost.sort(key=lambda r: (CLASS_ORDER.index(r["supply_class"]) if r["supply_class"] in CLASS_ORDER else 99,
                         num(r["value_low"])))
fig, ax = plt.subplots(figsize=(7.2, 0.36 * len(cost) + 1.4))
labels = []
for i, r in enumerate(cost):
    y = len(cost) - 1 - i
    lo, hi = num(r["value_low"]), num(r["value_high"]) or num(r["value_low"])
    lab, col, mk = SCOPE.get(r["cost_scope"], SCOPE["not_stated"])
    if hi > lo:
        ax.plot([lo, hi], [y, y], color=col, lw=2, solid_capstyle="round", zorder=2)
    x = math.sqrt(lo * hi)
    hollow = r["qualifier"] in ONE_SIDED
    ax.plot(x, y, marker=mk, ms=8, color=col, mfc="white" if hollow else col, mew=2, zorder=3)
    if r["qualifier"] in ("<", "<="):
        ax.annotate("", xy=(x * 0.6, y), xytext=(x * 0.9, y), arrowprops=dict(arrowstyle="->", color=col, lw=1.5))
    if r["qualifier"] in (">", ">="):
        ax.annotate("", xy=(x * 1.65, y), xytext=(x * 1.1, y), arrowprops=dict(arrowstyle="->", color=col, lw=1.5))
    flag = " *" if r["status"] == "unverified" else ""
    labels.append(f"{r['supply_class']}  {short(r['item'])} ({r['currency']}, {r['price_year']}){flag}  [{r['value_id']}]")
ax.set_yticks(range(len(cost)))
ax.set_yticklabels(labels[::-1], fontsize=7.5, color=INK)
ax.set_xscale("log")
ax.set_xlim(40, 60000)
ax.set_xlabel("Cost per kW of rated output (nominal currency, as stated; log scale)")
ax.grid(axis="x", which="major", color=GRID, lw=0.8)
ax.tick_params(axis="y", length=0)
handles = [Line2D([], [], marker=m, color=c, ls="", ms=7, mew=2, label=l) for l, c, m in SCOPE.values()
           if any(SCOPE.get(r["cost_scope"], SCOPE["not_stated"])[0] == l for r in cost)]
handles.append(Line2D([], [], marker="o", color=MUTED, mfc="white", ls="", ms=7, mew=2, label="one-sided value (<, >)"))
ax.legend(handles=handles, loc="upper left", bbox_to_anchor=(-0.02, -0.09), ncol=3, frameon=False, fontsize=7.5)
ax.set_title("Published supply cost per kW: sparse, mixed scope, mostly not the supply alone",
             loc="left", fontsize=10, color=INK)
ax.text(-0.02, -0.21, "Values from supply_values.csv (value ID in brackets). * unverified: no local copy of the source. "
         "Not converted between USD and EUR or to a common year.", fontsize=7, color=MUTED,
        transform=ax.transAxes)
save(fig, "supply_cost_per_kw")

# ---------- 2. unit power and efficiency vs frequency ----------
BASIS = {  # what the efficiency refers to -> (label, colour, marker)
    "generator": ("generator (mains in to rated output)", SLOT[0], "o"),
    "device": ("tube or transistor only", SLOT[1], "s"),
    "amplifier_or_head": ("amplifier / head only", SLOT[2], "D"),
    "into_load": ("measured into a load", SLOT[3], "^"),
    "not_stated": ("boundary not stated", SLOT[4], "v"),
}


def fmid(r):
    a, b = num(r["freq_low_hz"]), num(r["freq_high_hz"])
    if a is None and b is None:
        return None, None, None
    a = a if a else b
    b = b if b else a
    if not a or a <= 0:
        return None, None, None
    return a, b, math.sqrt(a * b)


fig, (axp, axe) = plt.subplots(2, 1, figsize=(7.2, 7.6), sharex=True)
fig.subplots_adjust(hspace=0.12)
# power panel: rated or family maximum output power per unit (kW)
for r in rows:
    if r["quantity"] not in ("output_power", "average_power") or r["supply_class"] == "context":
        continue
    v = num(r["value_high"]) or num(r["value_low"])
    if not v or r["unit"] != "kW":
        continue
    a, b, x = fmid(r)
    if x is None:
        continue
    if b > a:
        axp.plot([a, b], [v, v], color=MUTED, lw=1.5, solid_capstyle="round", zorder=1)
    axp.plot(x, v, "o", ms=6, color=INK, mfc="white" if r["status"] == "unverified" else INK, zorder=2)
    axp.annotate(r["supply_class"], (x, v), xytext=(4, 3), textcoords="offset points", fontsize=7, color=MUTED)
axp.set_yscale("log")
axp.set_ylabel("Unit output power (kW, log)")
axp.grid(which="major", color=GRID, lw=0.8)
axp.set_title("Supply unit power and efficiency by output frequency (published values)", loc="left", fontsize=10, color=INK)
# efficiency panel
used = set()
for r in rows:
    if r["quantity"] != "efficiency":
        continue
    lo, hi = num(r["value_low"]), num(r["value_high"]) or num(r["value_low"])
    a, b, x = fmid(r)
    if x is None or lo is None:
        continue
    lab, col, mk = BASIS.get(r["basis"], BASIS["not_stated"])
    used.add(r["basis"] if r["basis"] in BASIS else "not_stated")
    if b > a:
        axe.plot([a, b], [lo * 100, lo * 100], color=col, lw=1.5, alpha=0.6, zorder=1)
    if hi > lo:
        axe.plot([x, x], [lo * 100, hi * 100], color=col, lw=2, zorder=1)
    hollow = r["qualifier"] in ONE_SIDED or r["status"] == "unverified" or r["data_type"] == "reviewer_calc"
    axe.plot(x, (lo + hi) / 2 * 100, marker=mk, ms=7, color=col, mfc="white" if hollow else col, mew=2, zorder=3)
    axe.annotate(r["supply_class"], (x, (lo + hi) / 2 * 100), xytext=(5, -3), textcoords="offset points", fontsize=7, color=MUTED)
axe.set_xscale("log")
axe.set_ylim(35, 100)
axe.set_ylabel("Efficiency (%)")
axe.set_xlabel("Output frequency (Hz, log)")
axe.grid(which="major", color=GRID, lw=0.8)
handles = [Line2D([], [], marker=BASIS[k][2], color=BASIS[k][1], ls="", ms=7, mew=2, label=BASIS[k][0]) for k in BASIS if k in used]
handles.append(Line2D([], [], marker="o", color=MUTED, mfc="white", ls="", ms=7, mew=2, label="one-sided, calculated or unverified"))
axe.legend(handles=handles, loc="upper left", bbox_to_anchor=(-0.02, -0.13), frameon=False, fontsize=7.5, ncol=3)
fig.text(0.0, -0.035, "Class codes as in supply_classes.csv. DC supplies (J1, A1) have no output frequency and are not shown. "
         "Lines show stated frequency bands or value ranges.\nPulsed supplies (P1) have no carrier frequency and are not shown. Power panel: rated, family-maximum or installed output per unit.", fontsize=7, color=MUTED)
save(fig, "supply_power_efficiency_frequency")
