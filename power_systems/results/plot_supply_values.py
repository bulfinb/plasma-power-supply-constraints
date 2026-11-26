"""Figures from supply_values.csv (no data values in this script).

1. figures/supply_cost_per_kw.png/.svg  - every cost-per-kW value, grouped by supply class,
   coloured and shaped by what the price covers. Nominal currency and price year as stated;
   no currency or inflation conversion (USD and EUR are shown separately).
2. figures/supply_power_efficiency_frequency.png/.svg - unit power and efficiency against
   output frequency, coloured and shaped by what the efficiency refers to.
3. figures/supply_cost_vs_unit_size.png/.svg - cost per kW against unit or installation size (unit_size_kw).
4. figures/supply_class_map.png/.svg - each supply class as a box of frequency band x unit power,
   coloured by its efficiency range (supply_classes.csv map_value_ids and eta_low/eta_high).

Run from power_systems/: python3 figures/plot_supply_values.py
"""
import csv
import math
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker
import matplotlib.patches
import matplotlib.colors
import matplotlib.cm
from matplotlib.lines import Line2D

ROOT = Path(__file__).resolve().parent   # power_systems/results: data, scripts; figures/ below
OUT = ROOT / "figures"
OUT.mkdir(exist_ok=True)
rows = list(csv.DictReader(open(ROOT / "supply_values.csv", encoding="utf-8")))
DROPPED = {r["source_id"] for r in csv.DictReader(open(ROOT / "source_register.csv", encoding="utf-8")) if r["status"] == "dropped"}
rows = [r for r in rows if r["source_id"] not in DROPPED]   # dropped sources keep their rows for the record, not plotted

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
CLASS_ORDER = ["J1", "K1", "M1", "M2", "M3", "P1", "H1", "context"]
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
    hollow = r["qualifier"] in ONE_SIDED or r["data_type"] == "reviewer_calc"
    ax.plot(x, y, marker=mk, ms=8, color=col, mfc="white" if hollow else col, mew=2, zorder=3)
    if r["qualifier"] in ("<", "<="):
        ax.annotate("", xy=(x * 0.6, y), xytext=(x * 0.9, y), arrowprops=dict(arrowstyle="->", color=col, lw=1.5))
    if r["qualifier"] in (">", ">="):
        ax.annotate("", xy=(x * 1.65, y), xytext=(x * 1.1, y), arrowprops=dict(arrowstyle="->", color=col, lw=1.5))
    flag = " *" if r["status"] == "unverified" else ""
    per = ", per kVA" if r["unit"].endswith("/kVA") else ""
    labels.append(f"{r['supply_class']}  {short(r['item'])} ({r['currency']}{per}, {r['price_year']}){flag}  [{r['value_id']}]")
ax.set_yticks(range(len(cost)))
ax.set_yticklabels(labels[::-1], fontsize=7.5, color=INK)
ax.set_xscale("log")
ax.set_xlim(30, 60000)
ax.set_xlabel("Cost per kW of rated output (nominal currency, as stated; log scale)")
ax.grid(axis="x", which="major", color=GRID, lw=0.8)
ax.tick_params(axis="y", length=0)
handles = [Line2D([], [], marker=m, color=c, ls="", ms=7, mew=2, label=l) for l, c, m in SCOPE.values()
           if any(SCOPE.get(r["cost_scope"], SCOPE["not_stated"])[0] == l for r in cost)]
handles.append(Line2D([], [], marker="o", color=MUTED, mfc="white", ls="", ms=7, mew=2, label="one-sided (<, >) or reviewer-calculated"))
ax.legend(handles=handles, loc="upper left", bbox_to_anchor=(-0.02, -0.09), ncol=3, frameon=False, fontsize=7.5)
ax.set_title("Published supply cost per kW: sparse, mixed scope, mostly not the supply alone",
             loc="left", fontsize=10, color=INK)
ax.text(-0.02, -0.21, "Values from supply_values.csv (value ID in brackets). * unverified: no local copy of the source. "
         "Not converted between USD and EUR or to a common year; per-kVA values (rectifiers) plotted as stated.", fontsize=7, color=MUTED,
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


DC_X = 10.0  # DC values are drawn in a separate band at this x position, labelled "DC"
DC_SHIFT = {"A1": 0.6, "D1": 1.6}  # DC classes side by side within the band (J1 and context at DC_X)


def fmid(r):
    a, b = num(r["freq_low_hz"]), num(r["freq_high_hz"])
    if a is None and b is None:
        return None, None, None
    if a == 0 and (b is None or b == 0):
        x = DC_X * DC_SHIFT.get(r["supply_class"], 1.0)
        return x, x, x
    a = a if a else b
    b = b if b else a
    if r["supply_class"] == "M3":   # same 2.45 GHz band as M2: drawn just right of it
        a, b = a * 1.35, b * 1.35
    if not a or a <= 0:
        return None, None, None
    return a, b, math.sqrt(a * b)


fig, (axp, axe) = plt.subplots(2, 1, figsize=(7.2, 7.6), sharex=True)
fig.subplots_adjust(hspace=0.12)
# power panel: rated or family maximum output power per unit (kW)
ptop = {}
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
    inst = r["basis"] == "installed"
    axp.plot(x, v, "s" if inst else "o", ms=6, color=INK, mfc="white" if inst or r["status"] == "unverified" else INK,
             mew=1.5, zorder=2)
    if v > ptop.get(r["supply_class"], (0,))[0]:
        ptop[r["supply_class"]] = (v, x)
for c, (v, x) in ptop.items():   # one label per class, at its largest value
    axp.annotate(c, (x, v), xytext=(4, 3), textcoords="offset points", fontsize=7, color=MUTED)
axp.legend(handles=[Line2D([], [], marker="o", color=INK, ls="", ms=6, label="single unit or product family"),
                    Line2D([], [], marker="s", color=INK, mfc="white", mew=1.5, ls="", ms=6,
                           label="installed system (several units)")],
           loc="lower left", bbox_to_anchor=(0.06, 1.0), ncol=2, frameon=False, fontsize=7.5)
axp.set_yscale("log")
axp.set_ylabel("Output power: unit / installed (kW, log)")
axp.grid(which="major", color=GRID, lw=0.8)
ttl = axp.set_title("Supply unit power and efficiency by output frequency (published values)", loc="left", fontsize=10, color=INK)
# efficiency panel
used = set()
labelled = []
for r in rows:
    if r["quantity"] != "efficiency" or r["basis"] in ("power_supply_stage", "system") or r["data_type"] == "projection":
        continue  # supply-stage-only efficiencies are not comparable with the other boundaries; projections omitted
    if r["supply_class"] == "A1" and r["basis"] == "into_load":
        continue  # torch thermal efficiency: downstream of the supply
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
    yl = (lo + hi) / 2 * 100
    if r["supply_class"] != "context":
        labelled.append((r["supply_class"], x, yl))
LOWEST = {"M3", "H1"}
OFFSET = {"J1": (-6, 2, "right"), "K1": (0, 9, "center")}
for c in sorted({c for c, _, _ in labelled}):
    pts = [(yy, xx) for cc, xx, yy in labelled if cc == c]
    yy, xx = min(pts) if c in LOWEST else max(pts)
    dx, dy, ha = OFFSET.get(c, (6, -3, "left"))
    axe.annotate(c, (xx, yy), xytext=(dx, dy), textcoords="offset points", fontsize=7.5, color=MUTED, ha=ha)
axe.set_xscale("log")
axe.set_xlim(4, 4e11)
axe.set_ylim(35, 100)
ticks = [DC_X] + [10.0 ** k for k in range(2, 12, 2)]
axe.set_xticks(ticks)
axe.set_xticklabels(["DC"] + [f"$10^{{{k}}}$" for k in range(2, 12, 2)])
axe.xaxis.set_minor_locator(matplotlib.ticker.NullLocator())
for a in (axp, axe):  # separate the DC band from the frequency axis
    a.axvspan(4, 30, color=GRID, alpha=0.35, lw=0, zorder=0)
    a.axvline(30, color=MUTED, lw=0.8, ls=(0, (2, 2)), zorder=0)
axe.set_ylabel("Efficiency (%)")
axe.set_xlabel("Output frequency (Hz, log)")
axe.grid(which="major", color=GRID, lw=0.8)
handles = [Line2D([], [], marker=BASIS[k][2], color=BASIS[k][1], ls="", ms=7, mew=2, label=BASIS[k][0]) for k in BASIS if k in used]
handles.append(Line2D([], [], marker="o", color=MUTED, mfc="white", ls="", ms=7, mew=2, label="one-sided, calculated or unverified"))
axe.legend(handles=handles, loc="upper left", bbox_to_anchor=(-0.02, -0.13), frameon=False, fontsize=7.5, ncol=3)
foot = fig.text(0.0, -0.035, "Class codes as in supply_classes.csv. DC supplies are shown side by side in the shaded band at left (A1 torch supplies, J1 rectifiers, D1 HV DC). "
         "Lines show stated frequency bands or value ranges.\nPulsed supplies (P1) have no carrier frequency and are not shown. Power panel: rated, family-maximum or installed output per unit. Supply-stage-only and pulsed-system estimates are not shown; context values are drawn unlabelled.", fontsize=7, color=MUTED)
save(fig, "supply_power_efficiency_frequency")
# Clean version for Supporting Information 1: no title or footnote (both go in the caption), panel labels.
ttl.set_visible(False)
foot.set_visible(False)
for a, lab in ((axp, "(a)"), (axe, "(b)")):
    a.text(-0.1, 1.0, lab, transform=a.transAxes, fontsize=9, color=INK, fontweight="bold")
for ext in ("png", "pdf"):
    fig.savefig(OUT / f"SI1_supply_power_efficiency_frequency.{ext}", dpi=300, bbox_inches="tight")
print("wrote", OUT / "SI1_supply_power_efficiency_frequency.png")
plt.close(fig)

# ---------- 3. cost per kW vs unit size ----------
# Rows with cost_per_kw and a unit_size_kw. Same colour/shape by cost scope as figure 1.
# Dashed lines join cost-function evaluations of the same source (PS004 DBD: V03 -> V05 low; GA: V04 -> V05 high).
SKIP_DUPLICATE = {"RV005-V04"}  # same 144 kW value as PS004-V01 (both from PS003)
byid = {r["value_id"]: r for r in rows}
cs = [r for r in rows if r["quantity"] == "cost_per_kw" and num(r["value_low"]) and num(r.get("unit_size_kw"))
      and r["value_id"] not in SKIP_DUPLICATE]
fig, ax = plt.subplots(figsize=(7.2, 5.0))
for a_id, b_id, end in (("PS004-V03", "PS004-V05", "value_low"), ("PS004-V04", "PS004-V05", "value_high")):
    a, b = byid[a_id], byid[b_id]
    ax.plot([num(a["unit_size_kw"]), num(b["unit_size_kw"])], [num(a["value_low"]), num(b[end])],
            color=MUTED, lw=1.2, ls=(0, (4, 3)), zorder=1)
ax.annotate("TEA cost functions, DBD and GA\n(electrolyser scaling, P$^{0.53}$; PS004)", (3.0e4, 4200), fontsize=7,
            color=MUTED, ha="center")
placed = []
for r in cs:
    x = num(r["unit_size_kw"])
    lo, hi = num(r["value_low"]), num(r["value_high"]) or num(r["value_low"])
    lab, col, mk = SCOPE.get(r["cost_scope"], SCOPE["not_stated"])
    if hi > lo:
        ax.plot([x, x], [lo, hi], color=col, lw=2, solid_capstyle="round", zorder=2)
    y = math.sqrt(lo * hi)
    hollow = (r["qualifier"] in ONE_SIDED or r["data_type"] == "reviewer_calc"
              or r["unit_size_qualifier"] in (">", "<") or "reviewer calc" in r["unit_size_ref"])
    ax.plot(x, y, marker=mk, ms=8, color=col, mfc="white" if hollow else col, mew=2, zorder=3)
    if r["unit_size_qualifier"] == ">":
        ax.annotate("", xy=(x * 1.8, y), xytext=(x * 1.15, y), arrowprops=dict(arrowstyle="->", color=col, lw=1.2))
    if r["qualifier"] in ("<", "<="):
        ax.annotate("", xy=(x, y * 0.6), xytext=(x, y * 0.88), arrowprops=dict(arrowstyle="->", color=col, lw=1.2))
    per = "/kVA" if r["unit"].endswith("/kVA") else ""
    dy = -3 - 9 * sum(1 for px, py in placed if 0.8 < x / px < 1.25 and 0.8 < y / py < 1.25)
    placed.append((x, y))
    above = r["unit_size_qualifier"] == ">"  # arrow points right, so label above the marker
    ax.annotate(f"{r['supply_class']} {r['currency']}{per} {r['price_year']}", (x, y), xytext=(-4, 8) if above else (7, dy),
                textcoords="offset points", fontsize=6.5, color=MUTED, ha="right" if above else "left")
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlim(0.1, 3e5)
ax.set_ylim(40, 20000)
ax.set_xlabel("Unit or installation size (kW, log)")
ax.set_ylabel("Cost per kW (nominal currency, log)")
ax.grid(which="major", color=GRID, lw=0.8)
ax.set_title("Supply cost per kW against unit size (published values)", loc="left", fontsize=10, color=INK)
handles = [Line2D([], [], marker=m, color=c, ls="", ms=7, mew=2, label=l) for l, c, m in SCOPE.values()
           if any(SCOPE.get(r["cost_scope"], SCOPE["not_stated"])[0] == l for r in cs)]
handles.append(Line2D([], [], marker="o", color=MUTED, mfc="white", ls="", ms=7, mew=2,
                      label="one-sided, calculated, or size estimated / lower bound"))
ax.legend(handles=handles, loc="upper left", bbox_to_anchor=(-0.02, -0.11), ncol=3, frameon=False, fontsize=7.5)
fig.text(0.0, -0.1, "Size from unit_size_kw in supply_values.csv (unit power, or installation size for pilots and plants). "
         "Labels: class, currency, price year; no currency or year conversion.\nRectifier values per kVA. "
         "Costs without a stated size are not shown (see figure supply_cost_per_kw).", fontsize=7, color=MUTED)
save(fig, "supply_cost_vs_unit_size")

# ---------- 4. class map: frequency band x unit power, coloured by efficiency ----------
# Box extents from the rows listed in supply_classes.csv map_value_ids (frequency from any listed row,
# unit power from listed output_power rows). Colour = midpoint of eta_low-eta_high, one sequential hue.
classes = [c for c in csv.DictReader(open(ROOT / "supply_classes.csv", encoding="utf-8")) if c["status"] != "dropped"]
SEQ = matplotlib.colors.LinearSegmentedColormap.from_list("seq", ["#dbe8f8", "#2a78d6", "#0d2f5c"])
NORM = matplotlib.colors.Normalize(vmin=0.4, vmax=1.0)
fig, ax = plt.subplots(figsize=(7.2, 5.2))
ax.axvspan(4, 30, color=GRID, alpha=0.35, lw=0, zorder=0)
ax.axvline(30, color=MUTED, lw=0.8, ls=(0, (2, 2)), zorder=0)
for c in classes:
    ids = [x.strip() for x in c["map_value_ids"].split(";") if x.strip()]
    if not ids or not c["eta_low"]:
        continue
    fr, pw = [], []
    for vid in ids:
        r = byid[vid]
        a, b, _ = fmid(r)
        if a:
            fr += [a, b]
        if r["quantity"] == "output_power":
            pw += [num(r["value_low"]), num(r["value_high"]) or num(r["value_low"])]
    f0, f1 = min(fr), max(fr)
    p0, p1 = min(pw), max(pw)
    # minimum visual size for single values: x0.8-1.25 in each direction
    if f1 / f0 < 1.6:
        f0, f1 = f0 / 1.25, f1 * 1.25
    if p1 / p0 < 1.6:
        p0, p1 = p0 / 1.25, p1 * 1.25
    if c["class_id"] == "M3":  # same 2.45 GHz band as M2: draw beside it
        f0, f1 = f0 * 1.6, f1 * 1.6
    eta_lo, eta_hi = num(c["eta_low"]), num(c["eta_high"])
    context = c["class_id"] == "H1"
    col = SEQ(NORM((eta_lo + eta_hi) / 2))
    ax.add_patch(matplotlib.patches.Rectangle((f0, p0), f1 - f0, p1 - p0, facecolor=col, alpha=0.35 if context else 0.85,
                                              edgecolor="white", lw=1.5, hatch="///" if context else None, zorder=2))
    stage = {"amplifier_or_head": "*", "device": "*", "wall_to_plasma": "†"}.get(c["efficiency_stage"], "")
    eta_txt = f"~{eta_lo*100:.0f}%" if eta_hi == eta_lo else f"{eta_lo*100:.0f}-{eta_hi*100:.1f}%".replace(".0%", "%")
    ax.annotate(f"{c['class_id']}  {eta_txt}{stage}",
                (math.sqrt(f0 * f1), p1), xytext=(0, 3), textcoords="offset points", ha="center", fontsize=7.5, color=INK,
                bbox=dict(boxstyle="round,pad=0.15", fc="white", ec="none", alpha=0.85), zorder=4)
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlim(4, 4e11)
ax.set_ylim(0.1, 5e4)
ax.set_xticks([DC_X] + [10.0 ** k for k in range(2, 12, 2)])
ax.set_xticklabels(["DC"] + [f"$10^{{{k}}}$" for k in range(2, 12, 2)])
ax.xaxis.set_minor_locator(matplotlib.ticker.NullLocator())
ax.set_xlabel("Output frequency (Hz, log)")
ax.set_ylabel("Output power: unit / installed (kW, log)")
ax.grid(which="major", color=GRID, lw=0.8, zorder=0)
ax.set_title("Supply classes: frequency, unit power and efficiency", loc="left", fontsize=10, color=INK)
sm = matplotlib.cm.ScalarMappable(norm=NORM, cmap=SEQ)
cb = fig.colorbar(sm, ax=ax, fraction=0.035, pad=0.02)
cb.set_label("Class efficiency, midpoint of range", fontsize=8, color=INK)
cb.ax.yaxis.set_major_formatter(matplotlib.ticker.PercentFormatter(1.0, decimals=0))
cb.outline.set_visible(False)
fig.text(0.0, -0.05, "Boxes span documented frequency and power extents (map_value_ids); maxima need not coincide. K2 includes installed system power; "
         "single values have a small minimum size.\nEfficiency: nominally mains to output; M2 includes absorbed-power evidence. * amplifier, head or tube only "
         "(mains efficiency lower). Hatched: H1, context only.\nPulsed supplies (P1) have no carrier frequency and are "
         "not shown. Lab prototypes are excluded from the boxes. M3 is drawn just right of M2; both are at 2.45 GHz.", fontsize=7, color=MUTED)
save(fig, "supply_class_map")
