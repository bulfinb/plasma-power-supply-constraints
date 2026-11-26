"""Manuscript figure: supply unit power and efficiency against output frequency (no data values in this script).

Writes figures/manuscript_figure.png/.svg/.pdf (caption text is drafted in the manuscript).
A simplified version of supply_power_efficiency_frequency (plot_supply_values.py, kept for the SI):
- (a) unit power only: rated or family-maximum output of one supply unit. Installed systems, average power of
  pulsed transmitters, single devices and laboratory units are left out (installation sizes go in the caption).
- (b) published efficiencies only, labelled by class. The adopted class ranges are not drawn: they are in the
  manuscript tables and SI 1 (Table S4). Tube- and amplifier-only values (in the SI figure), torch thermal efficiencies
  (downstream of the supply), supply-stage-only, system and pulsed values are left out, as is PW019-V02 (not used in any range).
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

ROOT = Path(__file__).resolve().parent   # power_systems/results: data, scripts; figures/ below
OUT = ROOT / "figures"
DROPPED = {r["source_id"] for r in csv.DictReader(open(ROOT / "source_register.csv", encoding="utf-8")) if r["status"] == "dropped"}
rows = [r for r in csv.DictReader(open(ROOT / "supply_values.csv", encoding="utf-8")) if r["source_id"] not in DROPPED]
classes = {c["class_id"]: c for c in csv.DictReader(open(ROOT / "supply_classes.csv", encoding="utf-8")) if c["status"] != "dropped"}

SELECTED = ["J1", "A1", "D1", "K1", "K2", "M1", "M2"]   # P1 has no carrier frequency
CONTEXT = {"R1", "R2", "M3", "H1"}
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
# DC band: left of the 30 Hz divider. Widened in log units (DC_STRETCH) so it keeps its physical width when the
# axes are narrowed; the DC positions are stretched about the divider by the same factor.
DC_EDGE, DC_STRETCH = 30.0, 1.198
def dcpos(x):
    return DC_EDGE / (DC_EDGE / x) ** DC_STRETCH
XLO = dcpos(4.0)
DC_X = dcpos(10.0)
DC_SHIFT = {k: dcpos(10.0 * v) / DC_X for k, v in {"A1": 0.55, "J1": 1.0, "D1": 1.8}.items()}


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


fig, (axp, axe) = plt.subplots(2, 1, figsize=(5.06, 5.87), sharex=True, gridspec_kw={"height_ratios": [1, 1.06]})
fig.subplots_adjust(hspace=0.08)

# ---- (a) unit power ----
top = {}
K2_OFF = {"PW058-V06": ((-6, -3), "right"), "PW006-V01": ((0, -12), "center"),
          "PW002-V02": ((-4, 2), "right")}   # clear of R1, of each other and of the 4.5 MW label
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
    if cls == "K2":   # K2 points are spread over 0.2-600 kHz among K1 and R1: label each one
        off, ha = K2_OFF.get(r["value_id"], ((4, 2), "left"))
        axp.annotate("K2", (x, v), xytext=off, textcoords="offset points", fontsize=7.5, color=MUTED, ha=ha)
        continue
    key = "R2 VHF" if cls == "R2" and x > 1e7 else cls   # R2 has two frequency groups (1 MHz; 13.56-60 MHz)
    if v > top.get(key, (0,))[0]:
        top[key] = (v, x)
ABOVE = {"J1", "A1", "D1", "H1", "R2 VHF"}   # centred directly above the uppermost point
POFF = {"K1": ((-6, -3), "right")}           # left of its point: a K2 line (75-750 kW, 0.2-10 kHz) runs just above
for key, (v, x) in top.items():
    off, ha = (((3 if key == "A1" else 0), 6), "center") if key in ABOVE else POFF.get(key, ((4, 2), "left"))   # A1 nudged off the y-axis
    axp.annotate(key.split()[0], (x, v), xytext=off, textcoords="offset points", fontsize=7.5,
                 color=style(key.split()[0])[1], ha=ha)
axp.set_yscale("log")
axp.set_ylim(0.5, 1e4)
axp.set_ylabel("Unit output power (kW)")
axp.text(-0.17, 1.0, "(a)", transform=axp.transAxes, fontsize=9, color=INK, fontweight="bold")

# ---- (b) efficiency: published values only (adopted class ranges are in the tables and SI 1) ----
# Labels: one per class group, placed by value id where a class has separated groups or crowded neighbours.
LAB = {"PW021-V01": ((-6, -3), "right"),    # J1, left of the point (top of axis above)
       "PW054-V01": ((0, -12), "center"),   # D1 generator values, below the lowest (92%)
       "PW023-V01": ((0, -13), "center"),   # A1
       "SRC020-V01": ((-6, -3), "right"),   # D1 into an arc load, left (clear of the DC line)
       "PW026-V01": ((-6, -3), "right"),    # K1 lab inverter at 10 kHz
       "PW026-V03": ((6, -3), "left"),      # K1 lab inverters at 40-60 kHz
       "PW003-V02": ((6, -3), "left"), "PW004-V02": ((6, -3), "left"),   # K2 values spread over 0.2-600 kHz
       "PW005-V02": ((0, 6), "center"), "PW058-V08": ((6, -3), "left")}
LAB_CLASSES = {"J1", "D1", "A1", "K1", "K2"}   # labelled via LAB only; other classes once, at their highest point
pts, best = [], {}
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
    tcol = CTX if cls in CONTEXT else (SLOT[1] if basis == "into_load" else INK)
    if r["value_id"] in LAB:
        off, ha = LAB[r["value_id"]]
        axe.annotate(cls, (x, y), xytext=off, textcoords="offset points", fontsize=7.5, color=tcol, ha=ha)
    elif cls not in LAB_CLASSES and y > best.get(cls, (0, 0, 0))[1]:
        best[cls] = (x, y, tcol)
for cls, (x, y, tcol) in best.items():
    axe.annotate(cls, (x, y), xytext=(6, -3), textcoords="offset points", fontsize=7.5 if tcol != CTX else 7, color=tcol)

axe.set_xscale("log")
axe.set_xlim(XLO, 1e10)
axe.set_ylim(50, 100)
ticks = [DC_X] + [10.0 ** k for k in range(2, 11, 2)]
axe.set_xticks(ticks)
axe.set_xticklabels(["DC"] + [f"$10^{{{k}}}$" for k in range(2, 11, 2)])
axe.xaxis.set_minor_locator(matplotlib.ticker.NullLocator())
axe.set_ylabel("Efficiency (%)")
axe.set_xlabel("Output frequency (Hz)")
axe.text(-0.17, 1.0, "(b)", transform=axe.transAxes, fontsize=9, color=INK, fontweight="bold")
for a in (axp, axe):
    a.axvspan(XLO, DC_EDGE, color=GRID, alpha=0.35, lw=0, zorder=0)
    a.axvline(DC_EDGE, color=MUTED, lw=0.8, ls=(0, (2, 2)), zorder=0)
    a.grid(which="major", color=GRID, lw=0.7)
    a.set_axisbelow(True)

# Right-hand column: class key (top), then the efficiency-basis legend. Boundary terms as in the manuscript
# power_boundaries figure (P_mains, P_generator, P_absorbed).
KEY = [("J1", "low-voltage rectifiers"), ("A1", "DC arc-torch supplies"), ("D1", "high-voltage DC"),
       ("K1", "kHz high-voltage inverters"), ("K2", "induction-heating inverters"),
       ("M1", "915 MHz magnetron generators"), ("M2", "2.45 GHz magnetron generators"),
       ("R1", "RF tube oscillators"), ("R2", "solid-state RF"), ("M3", "solid-state microwave"),
       ("H1", "klystrons")]
DY = 0.034
x0 = axp.get_position().x1 + 0.03
y0 = axp.get_position().y1 - 0.01
fig.text(x0, y0, "Supply classes", fontsize=7.5, color=INK, fontweight="bold", va="center")
y = y0
for cid, name in KEY:
    col = "#878680" if cid in CONTEXT else INK   # a shade darker than CTX for small text
    y -= DY + (0.02 if cid == "R1" else 0)       # small gap before the context classes
    fig.text(x0, y, cid, fontsize=7.5, color=col, fontweight="bold", va="center")
    fig.text(x0 + 0.045, y, name, fontsize=7.5, color=col, va="center")

handles = [Line2D([], [], marker="o", color=SLOT[0], ls="", ms=6, label=r"$P_{\mathrm{generator}}/P_{\mathrm{mains}}$"),
           Line2D([], [], marker="^", color=SLOT[1], ls="", ms=6, label=r"measured at $P_{\mathrm{absorbed}}$"),
           Line2D([], [], marker="o", color=SLOT[0], mfc="white", mew=1.6, ls="", ms=6, label="boundary not stated"),
           Line2D([], [], marker="o", color=CTX, ls="", ms=6, label="context classes")]
leg = fig.legend(handles=handles, loc="upper left", bbox_to_anchor=(x0 - 0.012, y - 0.045), ncol=1, frameon=False,
                 fontsize=7.5, handletextpad=0.4, labelspacing=0.7, title="Efficiency (b)", alignment="left",
                 title_fontproperties={"size": 7.5, "weight": "bold"})
leg.get_title().set_color(INK)

for ext in ("png", "svg", "pdf"):
    fig.savefig(OUT / f"manuscript_figure.{ext}", dpi=300, bbox_inches="tight")
print("wrote", OUT / "manuscript_figure.png")

