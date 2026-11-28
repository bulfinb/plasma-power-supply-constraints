"""Manuscript figure: CH4 conversion vs energy per mol CH4 converted, plasma reforming headline points (no data values
in this script except the fired-SMR references, copied from build_synthesis.py FIRED).

Same style as the
power-supply manuscript figure (power_systems/results/plot_manuscript_figure.py). One panel instead of two:
- headline rows only (the plasma rows of the manuscript table, max two per paper);
- open marker = EC_CH4 at the paper's power boundary; filled marker = with a representative industrial supply
  (EC_CH4 / class efficiency, geometric mid of the class range; bar = range); thin line joins the pair;
- fired SMR references on a heat basis: open hexagon = heat absorbed by the tubes, filled = burner fuel (HHV);
  i.e. open = energy delivered to the reactor, filled = energy at the input (mains electricity or fuel);
- axes cut to EC 170-3500 kJ/mol and X_CH4 30-105%: Andersen 2020 (45 W DBD, ~8-9 MJ/mol) is drawn off-scale at the
  right edge (filled marker, arrow, values in MJ/mol) rather than dropped (BB 2026-11-25);
- point labels carry the reported power (P_kW; W below 1 kW) so scale is visible without another encoding (BB 2026-11-25);
- Joule-heated pilot (From 2024, reviewer estimate SRC005-C004): filled star at the industrial-supply value with bars
  for the EC and equilibrium-conversion ranges (supply efficiency 0.97-0.98, so the paper value is barely different).

Writes figures/manuscript_figure.png/.svg/.pdf and copies the pdf/png to manuscript/figures/reforming_figure.*.
Run from the repository root: ~/.venvs/science/bin/python literature_reforming/0_synthesis/plot_manuscript_figure.py
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
FIG = HERE / "figures"   # figure outputs (scripts and data stay in this folder)
FIG.mkdir(exist_ok=True)
MS_FIG = HERE.parent.parent / "manuscript" / "figures"
rows = list(csv.DictReader(open(HERE / "reforming_synthesis.csv", encoding="utf-8")))

# Reference categorical palette (dataviz skill, light mode), fixed slot order, as in the power-supply figure.
SLOT = ["#2a78d6", "#eb6834", "#1baf7a"]
INK, MUTED, GRID = "#1f1f1e", "#6b6a64", "#e4e3de"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 8.5, "axes.edgecolor": MUTED,
                     "axes.labelcolor": INK, "xtick.color": MUTED, "ytick.color": MUTED,
                     "axes.spines.top": False, "axes.spines.right": False,
                     "svg.fonttype": "none", "savefig.facecolor": "white"})
ROUTE = {"SMR": SLOT[0], "DRM": SLOT[1], "mixed": SLOT[2]}
ROUTE_LABEL = {"SMR": "steam (SMR)", "DRM": "dry (DRM)", "mixed": "mixed steam/CO$_2$"}
ACT = [  # (match in activation string, marker, legend label); legend order roughly by supply frequency
    ("arc torch", "P", "DC arc torch"), ("glow", "D", "DC glow"), ("GA", "^", "gliding arc"),
    ("gliding arc", "^", "gliding arc"), ("DBD", "v", "DBD"), ("ICP", "X", "RF ICP torch"),
    ("915", "s", "microwave 915 MHz"), ("2.45", "o", "microwave 2.45 GHz"),
]
DH = {"SMR": 206, "DRM": 247}
FIRED = [("NETL", 77.7, 340, 577), ("IEAGHG", 84.6, 315, 574)]   # name, X_CH4, EC_abs, EC_fired (build_synthesis FIRED)
LABEL = {"Hrabovsky 2018 OP001": "Hrabovsky", "Hrabovsky 2018 OP005": "Hrabovsky", "Akande 2022 OP008": "Akande",
         "Hrycak 2023 OP002": "Hrycak", "Hrycak 2023 OP001": "Hrycak", "Zhu 2019 OP004": "Zhu",
         "Geng 2022 OP002": "Geng", "Song 2020 OP013": "Song", "Kelly 2023 OP004": "Kelly",
         "Kwon 2023 OP003": "Kwon", "Wanten 2022 OP006": "Wanten", "Kaufmann 2026 OP002": "Kaufmann", "Andersen 2020 OP001": "Andersen"}
OFFSET = {   # label position relative to the filled (industrial-supply) marker: (dx, dy) points, ha, va
    "Hrabovsky 2018 OP001": ((6, -2), "left", "top"),
    "Hrabovsky 2018 OP005": ((6, 1), "left", "bottom"),
    "Akande 2022 OP008": ((6, 0), "left", "center"),   # right of the pair (83% point, 2026-11-26): Song below
    "Zhu 2019 OP004": ((-7, 0), "right", "center"),   # left of the pair, clear of Akande
    "Song 2020 OP013": ((6, 0), "left", "center"),
    "Wanten 2022 OP006": ((6, 0), "left", "center"),
    "Kelly 2023 OP004": ((6, 0), "left", "center"),
    "Kwon 2023 OP003": ((6, 0), "left", "center"),
    "Geng 2022 OP002": ((6, 0), "left", "center"),
    "Hrycak 2023 OP002": ((6, 0), "left", "center"),
    "Hrycak 2023 OP001": ((6, 0), "left", "center"),
}


def power_text(v):
    """Reported power with unit: 120 kW, 6.5 kW, 1.7 kW; below 1 kW in W (246 W, 15 W)."""
    if v >= 10:
        return f"{v:.0f} kW"
    if v >= 1:
        return f"{v:.1f}".rstrip("0").rstrip(".") + " kW"
    return f"{v * 1000:.0f} W"


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


pts, joule = [], None
for r in rows:
    if r["headline"] != "yes" or not f(r["EC_CH4_low"]):
        continue
    if "Joule" in r["activation"]:
        xs = [float(v) for v in re.findall(r"[\d.]+", r["X_CH4_pct"])[:2]]
        joule = dict(x=(min(xs), max(xs)), est=(f(r["EC_CH4_industrial_est_low"]), f(r["EC_CH4_industrial_est_high"])))
        continue
    mk = marker(r["activation"])
    if mk is None:
        continue
    pts.append(dict(key=r["row_key"], route=r["route"], mk=mk, x=num(r["X_CH4_pct"]), paper=f(r["EC_CH4_low"]), kw=f(r["P_kW"]),
                    est=(f(r["EC_CH4_industrial_est_low"]), f(r["EC_CH4_industrial_est_high"]))))

XMIN, XMAX, YMIN, YMAX = 170, 3500, 30, 105   # points beyond XMAX are drawn off-scale at the right edge
fig, ax = plt.subplots(figsize=(5.06, 3.6))

for route, dh in DH.items():
    ax.axvline(dh, color=ROUTE[route], lw=0.9, ls=(0, (3, 2)), alpha=0.8, zorder=1)
ax.text(DH["SMR"] * 0.975, YMIN + 1.5, r"$\Delta H^\circ$ SMR", rotation=90, fontsize=7, color=MUTED, ha="right", va="bottom")
ax.text(DH["DRM"] * 1.025, YMIN + 1.5, r"$\Delta H^\circ$ DRM", rotation=90, fontsize=7, color=MUTED, ha="left", va="bottom")

# Fired SMR references (heat basis)
for name, x, ec_abs, ec_fired in FIRED:
    ax.plot([ec_abs, ec_fired], [x, x], color=INK, lw=0.8, zorder=3)
    ax.plot(ec_fired, x, marker="h", ms=7, mfc=INK, mec=INK, ls="none", zorder=4)
    ax.plot(ec_abs, x, marker="h", ms=7, mfc="white", mec=INK, mew=1.2, ls="none", zorder=4)
ax.annotate("fired SMR (heat)", (440, sum(x for _, x, _, _ in FIRED) / len(FIRED)), fontsize=7.5, color=INK,
            ha="center", va="center")   # between the two reference lines

# Joule-heated pilot (reviewer estimate)
if joule:
    lo, hi = joule["est"]
    xc, ym = (lo * hi) ** 0.5, sum(joule["x"]) / 2
    ax.plot([lo, hi], [ym, ym], color=INK, lw=1.2, zorder=3)
    ax.plot([xc, xc], list(joule["x"]), color=INK, lw=1.2, zorder=3)
    ax.plot(xc, ym, marker="*", ms=11, mfc=INK, mec="white", mew=0.6, ls="none", zorder=4)
    ax.annotate("Joule-heated pilot", (xc, joule["x"][1]), xytext=(0, 3), textcoords="offset points", fontsize=7.5,
                color=INK, ha="center", va="bottom")

# Plasma headline points: open = paper boundary, filled = industrial supply
for p in pts:
    col = ROUTE[p["route"]]
    lo, hi = p["est"]
    xe = (lo * hi) ** 0.5
    name = f"{LABEL[p['key']]} {power_text(p['kw'])}"
    ms = 6.5 if p["mk"] in "PX" else 5.5
    if p["paper"] > XMAX:   # off-scale: filled marker at the right edge, arrow, values in MJ/mol
        xm = XMAX * 0.80
        ax.plot(xm, p["x"], marker=p["mk"], ms=ms, mfc=col, mec=col, ls="none", zorder=3)
        ax.annotate("", (XMAX * 0.99, p["x"]), xytext=(xm * 1.06, p["x"]),
                    arrowprops=dict(arrowstyle="-|>", color=col, lw=1.0, mutation_scale=8), zorder=3)
        ax.annotate(f"{name}\n{p['paper'] / 1000:.1f}\u2013{hi / 1000:.1f} MJ mol$^{{-1}}$",
                    (XMAX * 0.99, p["x"]), xytext=(0, 6), textcoords="offset points", fontsize=7.5, color=INK,
                    ha="right", va="bottom", linespacing=1.1)
        continue
    ax.plot([p["paper"], xe], [p["x"]] * 2, color=col, lw=0.8, alpha=0.6, zorder=2)
    if hi / lo > 1.02:   # supply-class range: thin bar with end caps
        ax.errorbar(xe, p["x"], xerr=[[xe - lo], [hi - xe]], fmt="none", ecolor=col, elinewidth=0.9, capsize=2,
                    capthick=0.9, zorder=2)
    ax.plot(p["paper"], p["x"], marker=p["mk"], ms=ms, mfc="white", mec=col, mew=1.2, ls="none", zorder=3)
    ax.plot(xe, p["x"], marker=p["mk"], ms=ms, mfc=col, mec=col, mew=1.0, ls="none", zorder=3)
    (dx, dy), ha, va = OFFSET.get(p["key"], ((6, 0), "left", "center"))
    # left-aligned: after the range; right-aligned: before the open marker; centred: over the open-filled pair
    anchor = {"left": hi, "right": min(p["paper"], lo)}.get(ha, (p["paper"] * xe) ** 0.5)
    ax.annotate(name, (anchor, p["x"]), xytext=(dx, dy), textcoords="offset points",
                fontsize=7.5, color=INK, ha=ha, va=va)

ax.set_xscale("log")
ax.set_xlim(XMIN, XMAX)
ax.set_ylim(YMIN, 100)
ax.set_xticks([200, 300, 500, 1000, 2000, 3000])
ax.xaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: f"{v:,.0f}"))
ax.xaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
ax.grid(True, which="major", color=GRID, lw=0.7)
ax.set_axisbelow(True)
ax.set_xlabel(r"Electricity per mol CH$_4$ converted, EC$_{\mathrm{CH_4}}$ (kJ mol$^{-1}$)")
ax.set_ylabel(r"CH$_4$ conversion (%)")

# Right-hand legend column (as in the power-supply figure)
x0 = ax.get_position().x1 + 0.03
kw = dict(frameon=False, fontsize=7.5, handletextpad=0.4, labelspacing=0.5, alignment="left",
          title_fontproperties={"size": 7.5, "weight": "bold"}, borderaxespad=0)
legs = []
h_route = [Line2D([], [], marker="s", color=c, ls="", ms=6, label=ROUTE_LABEL[r]) for r, c in ROUTE.items()]
seen, h_act = [], []
for _, m, lab in ACT:
    if lab not in seen:
        seen.append(lab)
        h_act.append(Line2D([], [], marker=m, color=MUTED, ls="", ms=6.5 if m in "PX" else 5.5, label=lab))
h_basis = [Line2D([], [], marker="o", mfc="white", mec=MUTED, mew=1.2, ls="", ms=5.5, label="at reported power boundary"),
           Line2D([], [], marker="o", color=MUTED, ls="", ms=5.5, label="with industrial supply"),
           Line2D([], [], marker="h", mfc="white", mec=INK, mew=1.2, ls="", ms=7, label="fired SMR: heat absorbed"),
           Line2D([], [], marker="h", color=INK, ls="", ms=7, label="fired SMR: fuel (HHV)"),
           Line2D([], [], marker="*", color=INK, mec="white", mew=0.6, ls="", ms=10, label="Joule-heated pilot (est.)")]
y = ax.get_position().y1 + 0.02
for title, h in (("Reforming route", h_route), ("Plasma type", h_act), ("Energy basis", h_basis)):
    leg = fig.legend(handles=h, loc="upper left", bbox_to_anchor=(x0, y), title=title, **kw)
    leg.get_title().set_color(INK)
    legs.append(leg)
    fig.canvas.draw()
    bb = leg.get_window_extent().transformed(fig.transFigure.inverted())
    y = bb.y0 - 0.035

for ext in ("png", "svg", "pdf"):
    fig.savefig(FIG / f"manuscript_figure.{ext}", dpi=300, bbox_inches="tight")
for ext in ("png", "pdf"):
    shutil.copy(FIG / f"manuscript_figure.{ext}", MS_FIG / f"reforming_figure.{ext}")
print(f"{len(pts)} plasma points; wrote", FIG / "manuscript_figure.png")
