"""Manuscript figure: supply unit power and efficiency against output frequency (no data values in this script).

Writes figures/0_manuscript_figure.png/.svg/.pdf and figures/0_manuscript_figure_caption.txt.
A simplified version of supply_power_efficiency_frequency (plot_supply_values.py, kept for the SI):
- (a) unit power only: rated or family-maximum output of one supply unit. Installed systems, average power of
  pulsed transmitters, single devices and laboratory units are left out (installation sizes go in the caption).
- (b) published efficiencies (points) with the adopted class ranges of supply_classes.csv (boxes) for the
  classes used in the projections; the K2 box is the 400 kHz sub-band used for the ICP torch
  (scaleup_wall_basis.py SUBBAND). Tube- and amplifier-only values (in the SI figure), torch thermal efficiencies (downstream of the supply) and supply-stage-only,
  system and pulsed values are left out, as is PW019-V02 (not used in any range).
- Context classes (R1, R2, M3, H1) in grey; M3 drawn just right of 2.45 GHz. Projections and dropped sources are skipped.

Run from power_systems/: python3 figures/plot_manuscript_figure.py
"""
import csv
import math
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker
from matplotlib.lines import Line2D
from matplotlib.patches import Patch, Rectangle

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "figures"
DROPPED = {r["source_id"] for r in csv.DictReader(open(ROOT / "source_register.csv", encoding="utf-8")) if r["status"] == "dropped"}
rows = [r for r in csv.DictReader(open(ROOT / "supply_values.csv", encoding="utf-8")) if r["source_id"] not in DROPPED]
classes = {c["class_id"]: c for c in csv.DictReader(open(ROOT / "supply_classes.csv", encoding="utf-8")) if c["status"] != "dropped"}

SELECTED = ["J1", "A1", "D1", "K1", "K2", "M1", "M2"]   # P1 has no carrier frequency
CONTEXT = {"R1", "R2", "M3", "H1"}
SUBBAND = {"K2": (1e5, 4e5, 0.91, 0.96)}                 # 400 kHz case (scaleup_wall_basis.py)
BAND = {"K1": (1e3, 3e4), "M1": (9.15e8, 9.15e8), "M2": (2.45e9, 2.45e9)}   # supply_classes.csv frequency column
M3_SHIFT = 1.35   # M3 shares 2.45 GHz with M2: drawn just right of it
NOT_UNIT = {"PW026-V04", "PW027-V02", "PW046-V10", "SRC020-V05"}   # lab inverters/amplifiers, a single device, a lab supply
NOT_USED = {"PW019-V02"}

# Reference categorical palette (dataviz skill, light mode), fixed slot order; grey for context.
SLOT = ["#2a78d6", "#eb6834", "#1baf7a"]
INK, MUTED, GRID, CTX = "#1f1f1e", "#6b6a64", "#e4e3de", "#a9a8a2"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 8.5, "axes.edgecolor": MUTED,
                     "axes.labelcolor": INK, "xtick.color": MUTED, "ytick.color": MUTED,
                     "axes.spines.top": False, "axes.spines.right": False,
                     "svg.fonttype": "none", "savefig.facecolor": "white"})
DC_X = 10.0
DC_SHIFT = {"A1": 0.55, "J1": 1.0, "D1": 1.8}


def num(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def fpos(r):
    a, b = num(r["freq_low_hz"]), num(r["freq_high_hz"])
    if a is None and b is None:
        return None
    if a == 0 and not b:
        x = DC_X * DC_SHIFT.get(r["supply_class"], 1.0)
        return x, x, x
    a, b = a or b, b or a
    if r["supply_class"] == "M3":
        a, b = a * M3_SHIFT, b * M3_SHIFT
    return a, b, math.sqrt(a * b)


def style(cls):
    return (CTX, CTX) if cls in CONTEXT else (INK, MUTED)


fig, (axp, axe) = plt.subplots(2, 1, figsize=(7.0, 6.4), sharex=True, gridspec_kw={"height_ratios": [1, 1.25]})
fig.subplots_adjust(hspace=0.08)

# ---- (a) unit power ----
top = {}
for r in rows:
    if r["quantity"] != "output_power" or r["basis"] == "installed" or r["value_id"] in NOT_UNIT or r["unit"] != "kW":
        continue
    cls = r["supply_class"]
    if cls not in SELECTED and cls not in CONTEXT:
        continue
    v, p = num(r["value_high"]) or num(r["value_low"]), fpos(r)
    if not v or p is None:
        continue
    a, b, x = p
    col, _ = style(cls)
    if b > a:
        axp.plot([a, b], [v, v], color=col, lw=1.2, alpha=0.7, solid_capstyle="round", zorder=1)
    axp.plot(x, v, "o", ms=5.5, color=col, zorder=2)
    if v > top.get(cls, (0,))[0]:
        top[cls] = (v, x)
for cls, (v, x) in top.items():
    axp.annotate(cls, (x, v), xytext=(4, 2), textcoords="offset points", fontsize=7.5, color=style(cls)[1])
axp.set_yscale("log")
axp.set_ylim(0.5, 1e4)
axp.set_ylabel("Unit output power (kW)")
axp.text(-0.1, 1.0, "(a)", transform=axp.transAxes, fontsize=9, color=INK, fontweight="bold")

# ---- (b) efficiency: adopted ranges (boxes) and published values (points) ----
for cls in SELECTED:
    c = classes[cls]
    lo, hi = float(c["eta_low"]), float(c["eta_high"])
    if cls in SUBBAND:
        f0, f1, lo, hi = SUBBAND[cls]
    elif cls in ("J1", "A1", "D1"):
        f0 = f1 = DC_X * DC_SHIFT[cls]
    else:
        f0, f1 = BAND[cls]
    w = 1.18 if f0 == f1 else 1.0   # minimum width for single frequencies (log axis)
    x0, x1 = f0 / w, f1 * w
    axe.add_patch(Rectangle((x0, lo * 100), x1 - x0, (hi - lo) * 100, facecolor=SLOT[0], alpha=0.16,
                            edgecolor=SLOT[0], lw=0.8, zorder=1))
    xc = math.sqrt(x0 * x1)
    pos = {"A1": ((xc, lo * 100), (0, -13), "center"), "J1": ((xc, hi * 100), (0, 4), "center")}
    xy, off, ha = pos.get(cls, ((x1, hi * 100), (3, 1), "left"))
    axe.annotate(cls, xy, xytext=off, textcoords="offset points", fontsize=7.5, color=INK, fontweight="bold", ha=ha)

ctx_lab = set()
for r in rows:
    if r["quantity"] != "efficiency" or r["value_id"] in NOT_USED or r["data_type"] == "projection":
        continue
    cls, basis = r["supply_class"], r["basis"]
    if cls not in SELECTED and cls not in CONTEXT:
        continue
    if basis in ("power_supply_stage", "system", "device", "amplifier_or_head") or (cls == "A1" and basis == "into_load"):
        continue   # stage, tube or amplifier only (SI figure), whole system, or torch thermal efficiency (downstream)
    lo, hi = num(r["value_low"]), num(r["value_high"]) or num(r["value_low"])
    p = fpos(r)
    if lo is None or p is None:
        continue
    a, b, x = p
    if basis == "into_load":
        col, mk, fill = SLOT[1], "^", True
    elif basis == "generator":
        col, mk, fill = SLOT[0], "o", True
    else:
        col, mk, fill = SLOT[0], "o", False      # boundary not stated
    if cls in CONTEXT:
        col = CTX
    y = (lo + hi) / 2 * 100
    if hi > lo:
        axe.plot([x, x], [lo * 100, hi * 100], color=col, lw=1.6, zorder=2)
    axe.plot(x, y, marker=mk, ms=6, color=col, mfc=col if fill else "white", mew=1.6, zorder=3)
    if cls in CONTEXT and cls not in ctx_lab:
        axe.annotate(cls, (x, y), xytext=(4, -9), textcoords="offset points", fontsize=7, color=CTX)
        ctx_lab.add(cls)

axe.set_xscale("log")
axe.set_xlim(4, 1e10)
axe.set_ylim(45, 100)
ticks = [DC_X] + [10.0 ** k for k in range(2, 11, 2)]
axe.set_xticks(ticks)
axe.set_xticklabels(["DC"] + [f"$10^{{{k}}}$" for k in range(2, 11, 2)])
axe.xaxis.set_minor_locator(matplotlib.ticker.NullLocator())
axe.set_ylabel("Efficiency (%)")
axe.set_xlabel("Output frequency (Hz)")
axe.text(-0.1, 1.0, "(b)", transform=axe.transAxes, fontsize=9, color=INK, fontweight="bold")
for a in (axp, axe):
    a.axvspan(4, 30, color=GRID, alpha=0.35, lw=0, zorder=0)
    a.axvline(30, color=MUTED, lw=0.8, ls=(0, (2, 2)), zorder=0)
    a.grid(which="major", color=GRID, lw=0.7)
    a.set_axisbelow(True)

handles = [Patch(facecolor=SLOT[0], alpha=0.3, edgecolor=SLOT[0], label="adopted class range"),
           Line2D([], [], marker="o", color=SLOT[0], ls="", ms=6, label="complete generator"),
           Line2D([], [], marker="o", color=SLOT[0], mfc="white", mew=1.6, ls="", ms=6, label="boundary not stated"),
           Line2D([], [], marker="^", color=SLOT[1], ls="", ms=6, label="measured into a plasma load"),
           Line2D([], [], marker="o", color=CTX, ls="", ms=6, label="context classes (grey)")]
axe.legend(handles=handles, loc="upper left", bbox_to_anchor=(0.0, -0.13), ncol=3, frameon=False, fontsize=7.5)

for ext in ("png", "svg", "pdf"):
    fig.savefig(OUT / f"0_manuscript_figure.{ext}", dpi=300, bbox_inches="tight")
print("wrote", OUT / "0_manuscript_figure.png")

inst = {r["value_id"]: r for r in rows if r["basis"] == "installed"}
caption = (
    "Published power supplies against output frequency. (a) Output power of a single supply unit (rated or "
    "family maximum); lines show stated frequency bands. Installed systems built from several units are larger: "
    "induction-heating supplies of 16-42 MW and an installation of 126 MW, a 1.76 MW precipitator installation of "
    "32 high-voltage DC units, and 915 MHz microwave containers of several MW. (b) Published efficiencies (points) "
    "and the ranges adopted for the projections (boxes; for K2, the 100-400 kHz range used for the ICP torch). "
    "Efficiency is from mains input to generator output unless marked; values for the tube or amplifier alone are "
    "not shown (Supporting Information 1). DC supplies are drawn side by side in the shaded band (A1 arc-torch supplies, J1 "
    "rectifiers, D1 high-voltage DC). Grey: classes not used in the projections (R1 RF tube oscillator, R2 "
    "solid-state RF, M3 solid-state microwave, drawn just right of 2.45 GHz; H1 klystron). Projected values are not shown. Nanosecond pulsed supplies (P1) have no carrier "
    "frequency and are not shown. Data and sources: power_systems/supply_values.csv.")
(OUT / "0_manuscript_figure_caption.txt").write_text(caption + "\n", encoding="utf-8")
print(caption)
print("installed rows (caption):", ", ".join(f"{k} {v['value_low']} {v['unit']}" for k, v in inst.items()))
