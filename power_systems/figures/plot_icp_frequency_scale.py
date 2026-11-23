"""ICP torch frequency against scale (supporting-information figure).

(a) torch (confinement tube) diameter against operating frequency, with the skin-depth coupling band;
(b) torch or generator power against frequency, with the frequency-power ranges of solid-state and tube supplies.

All numbers come from supply_values.csv by value ID. Constants:
  SIGMA = 1e3 S/m, argon at 8000 K and 1 atm (PW055-V01, Boulos 1985); MU0 = 4 pi 1e-7 H/m.
  Coupling band r/delta from PW055-V02 (optimum 1.5-4.0); r/delta < 1: coupling "drops rather drastically" (same quote).
The band is f = (r/delta)^2 / (pi MU0 SIGMA r^2) with r = D/2. It is indicative: sigma depends on gas and temperature.

Run from power_systems/: <python with matplotlib> figures/plot_icp_frequency_scale.py
"""
import csv
import math
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

ROOT = Path(__file__).resolve().parent.parent
V = {r["value_id"]: r for r in csv.DictReader(open(ROOT / "supply_values.csv", encoding="utf-8"))}

INK, MUTED, GRID = "#1f1f1f", "#6b6b6b", "#e4e4e4"
BLUE, ORANGE, GREEN = "#2a78d6", "#eb6834", "#1baf7a"
SIGMA, MU0 = 1e3, 4e-7 * math.pi


def num(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def freq(vid):
    r = V[vid]
    a, b = num(r["freq_low_hz"]), num(r["freq_high_hz"])
    return a or b, b or a


def kw(vid):
    r = V[vid]
    return num(r["value_low"]), num(r["value_high"]) or num(r["value_low"])


# Torches: (label, diameter value ID or None, power value ID or None, atmospheric?)
TORCHES = [
    ("VKI Plasmatron (generator rating)", "PW056-V01", "PW056-V02", False),
    ("Song 2020 (SRC009), generator max.", "SRC009-V01", "SRC009-V02", True),
    ("UT Austin 50 kW", "PW057-V02", "PW057-V01", True),
    ("Eckert (Boulos 1985)", "PW055-V08", "PW055-V09", True),
    ("Trekhov (Boulos 1985)", "PW055-V10", "PW055-V11", True),
    ("Dresvin compilation (Boulos 1985)", "PW055-V12", "PW055-V13", True),
    ("Model torch (Boulos 1985)", "PW055-V14", None, True),
    ("ICP-OES (Thermo iCAP 7600)", None, "PW059-V01", True),
]
DESIGN = ["PW058-V02", "PW058-V03", "PW058-V04"]  # patent design examples (minimum or optimum frequency for a diameter)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(7.2, 8.4), sharex=True)
fig.subplots_adjust(hspace=0.1)

# ---- (a) diameter vs frequency ----
lo_ratio, hi_ratio = num(V["PW055-V02"]["value_low"]), num(V["PW055-V02"]["value_high"])
dd = [d / 1000 for d in (5, 8, 12, 20, 30, 50, 80, 120, 200, 300, 500)]


def f_of(D, ratio):
    r = D / 2
    return ratio ** 2 / (math.pi * MU0 * SIGMA * r ** 2)


f_lo = [f_of(D, lo_ratio) for D in dd]
f_hi = [f_of(D, hi_ratio) for D in dd]
f_one = [f_of(D, 1.0) for D in dd]
D_mm = [D * 1000 for D in dd]
ax1.fill_betweenx(D_mm, f_lo, f_hi, color=BLUE, alpha=0.15, lw=0, zorder=0)
ax1.plot(f_one, D_mm, color=MUTED, lw=1, ls=(0, (3, 2)), zorder=1)
ax1.annotate("r/δ = 1: coupling\ndrops sharply below", (f_of(0.3, 1.0) * 0.55, 300), fontsize=7, color=MUTED, ha="right",
             va="center")
for lab, did, pid, atm in TORCHES:
    if not did:
        continue
    f, _ = freq(did)
    d = num(V[did]["value_low"])
    ax1.plot(f, d, "o", ms=7, color=INK, mfc=INK if atm else "white", mew=1.6, zorder=3)
    left = f > 1.5e7 or lab.startswith("Model")
    ax1.annotate(lab.split(" (")[0], (f, d), xytext=(-6 if left else 6, -3), ha="right" if left else "left",
                 textcoords="offset points", fontsize=7, color=MUTED)
for vid in DESIGN:
    f, _ = freq(vid)
    d = num(V[vid]["value_low"])
    ax1.plot(f, d, "D", ms=6, color=ORANGE, mfc="white", mew=1.6, zorder=3)
    if V[vid]["qualifier"] == ">=":
        ax1.annotate("", xy=(f, d * 1.45), xytext=(f, d * 1.06), arrowprops=dict(arrowstyle="->", color=ORANGE, lw=1.2))
ax1.set_yscale("log")
ax1.set_ylim(8, 600)
ax1.set_ylabel("Torch (tube) diameter (mm, log)")
ax1.grid(which="major", color=GRID, lw=0.8)
ttl = ax1.set_title("ICP torches: frequency falls as the torch grows", loc="left", fontsize=10, color=INK)
h1 = [Line2D([], [], marker="o", color=INK, ls="", ms=7, label="torch, atmospheric pressure"),
      Line2D([], [], marker="o", color=INK, mfc="white", ls="", ms=7, mew=1.6, label="torch, sub-atmospheric"),
      Line2D([], [], marker="D", color=ORANGE, mfc="white", ls="", ms=6, mew=1.6, label="design example (patent PW058)"),
      matplotlib.patches.Patch(color=BLUE, alpha=0.15, label=f"optimum coupling, r/δ = {lo_ratio:g}-{hi_ratio:g}")]
ax1.legend(handles=h1, loc="upper right", frameon=False, fontsize=7.5)

# ---- (b) power vs frequency, with supply ranges ----
# solid-state >=95% at >=100 kW up to 0.5 MHz (PW058-V06); at >=1 MHz about 30 kW (PW058-V05)
f6a, f6b = freq("PW058-V06")
p6 = num(V["PW058-V06"]["value_low"])
ax2.fill_between([5e2, f6b], [p6, p6], [3e3, 3e3], color=BLUE, alpha=0.13, lw=0, zorder=0)
ax2.annotate(f"solid-state ≥95%,\n≥{p6:g} kW up to {f6b/1e6:g} MHz\n(PW058)", (2.2e4, 1100), fontsize=7, color=BLUE, va="center")
f5a, _ = freq("PW058-V05")
p5 = num(V["PW058-V05"]["value_low"])
ax2.fill_between([f5a, 6e7], [0.3, 0.3], [p5, p5], color=BLUE, alpha=0.13, lw=0, zorder=0)
ax2.annotate(f"solid-state ≥95%:\n~{p5:g} kW at ≥{f5a/1e6:g} MHz (PW058)", (1.15e6, 0.45), fontsize=7, color=BLUE, va="bottom")
# induction-heating solid-state generators 100-400 kHz (K2): PW005-V01 (<=100 kW input), PW006-V01 (50 kW)
for vid in ("PW005-V01", "PW006-V01"):
    a, b = freq(vid)
    p = num(V[vid]["value_high"]) or num(V[vid]["value_low"])
    ax2.plot([a, b], [p, p], color=BLUE, lw=3, solid_capstyle="butt", zorder=2)
ax2.annotate("solid-state induction\ngenerators (K2)", (1.0e5, 62), xytext=(-4, 0), textcoords="offset points",
             fontsize=7, color=BLUE, ha="right", va="center")
# tube generators for ICP up to 120 kW at 2-3 MHz (PW061-V01)
a, b = freq("PW061-V01")
p = num(V["PW061-V01"]["value_low"])
ax2.plot([a, b], [p, p], color=ORANGE, lw=3, solid_capstyle="butt", zorder=2)
ax2.annotate("tube generators\n(TRUMPF, PW061)", (b, p), xytext=(5, 0), textcoords="offset points", fontsize=7,
             color=ORANGE, va="center")
# minimum sustaining power at 960 Hz (PW055-V04)
f4, _ = freq("PW055-V04")
p4 = num(V["PW055-V04"]["value_low"])
ax2.plot(f4, p4, "v", ms=7, color=GREEN, mfc="white", mew=1.6, zorder=3)
ax2.annotate("minimum sustaining power,\nargon, 1 atm (PW055)", (f4, p4), xytext=(7, -4), textcoords="offset points",
             fontsize=7, color=GREEN, va="top")
for lab, did, pid, atm in TORCHES:
    if not pid:
        continue
    f, _ = freq(pid)
    lo, hi = kw(pid)
    if hi > lo:
        ax2.plot([f, f], [lo, hi], color=INK, lw=2, zorder=2)
    ax2.plot(f, hi, "o", ms=7, color=INK, mfc=INK if atm else "white", mew=1.6, zorder=3)
    left = f > 1.5e7
    ax2.annotate(lab.split(" (")[0], (f, hi), xytext=(-6 if left else 6, 2), ha="right" if left else "left",
                 textcoords="offset points", fontsize=7, color=MUTED)
ax2.set_xscale("log")
ax2.set_yscale("log")
ax2.set_xlim(5e2, 6e7)
ax2.set_ylim(0.3, 3e3)
ax2.set_xlabel("Operating frequency (Hz, log)")
ax2.set_ylabel("Torch or generator power (kW, log)")
ax2.grid(which="major", color=GRID, lw=0.8)
foot = fig.text(0.0, 0.015, "Band in (a): r/δ = 1.5-4 with δ = (π f μ0 σ)^-1/2, σ = 10³ S/m (argon, 8000 K; PW055-V01, -V02), r = D/2; indicative only.\n"
         "Power in (b): rated generator output (VKI, Song, ICP-OES) or plasma/discharge power (others); line = stated range.\n"
         "Values and quotes in supply_values.csv (PW055-PW061, SRC009).", fontsize=7, color=MUTED, va="top")
for ext in ("png", "svg"):
    fig.savefig(ROOT / "figures" / f"icp_frequency_scale.{ext}", dpi=200, bbox_inches="tight")
print("wrote figures/icp_frequency_scale.png/.svg")
# Clean version for Supporting Information 1: no title or footnote (both go in the caption), panel labels.
ttl.set_visible(False)
foot.set_visible(False)
for a, lab in ((ax1, "(a)"), (ax2, "(b)")):
    a.text(-0.12, 1.0, lab, transform=a.transAxes, fontsize=9, color=INK, fontweight="bold")
for ext in ("png", "pdf"):
    fig.savefig(ROOT / "figures" / f"SI1_icp_frequency_scale.{ext}", dpi=300, bbox_inches="tight")
print("wrote figures/SI1_icp_frequency_scale.png/.pdf")
