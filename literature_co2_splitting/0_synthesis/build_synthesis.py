"""CO2 splitting synthesis: one row per extracted operating point (SRC016-SRC026, SRC028).

Run from the repository root:  python3 literature_co2_splitting/0_synthesis/build_synthesis.py
Writes co2_synthesis.csv (all rows) and co2_synthesis_tables.md (headline rows, aligned tables).

Values are copied from each source's short_summary.txt comparison tables (evidence IDs given per row);
nothing here is new evidence. Three energy columns are kept apart:
  EC_CO at the paper's own power boundary (as reported or reviewer-calculated in the extraction);
  EC_CO at a measured wall/plug boundary, where the paper measured one;
  EC_CO with a representative industrial supply = EC at the plasma-side boundary / class efficiency
  (power_systems/supply_classes.csv), the same method as power_systems/figures/scaleup_wall_basis.py.
The industrial-supply column is an estimate (reviewer calculation), never a demonstrated value.
"""
import csv
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
KWH_NM3 = 3600 / (1000 / 22.414)          # kJ/mol per kWh/Nm3 (0 C, 1 atm) = 80.69
EC_DH = 282.7 / KWH_NM3                   # 3.50 kWh/Nm3 CO = 100% on dH (282.7 kJ/mol)
LHV_CO_KWH = 283.0 / KWH_NM3              # LHV of CO, kWh/Nm3 CO
LHV_C_KWH_KG = 393.5 / 12.011 / 3.6       # LHV of carbon (graphite), kWh/kg
EC_DG = 257.2 / KWH_NM3                   # 3.19 kWh/Nm3 CO = dG at 298 K (reference line)

SUP = {r["class_id"]: r for r in csv.DictReader(open(ROOT / "power_systems/supply_classes.csv", encoding="utf-8"))}
ETA = {k: (float(v["eta_low"]), float(v["eta_high"])) for k, v in SUP.items() if v["eta_low"]}

# Lab supply efficiency used to move plug-basis results to the plasma side (reviewer judgement, see note)
GA_PSU = (0.77, 0.83)   # measured for the GAD-1000 arc supply, SRC020-E010; SRC021 implies 0.83 (E015)


def R(key, sid, route, cls, p, P_kw, boundary, x, ec_b, units="1", ec_wall=None, plug_basis=False,
      carbon=None, x_note="", conv="", energy="", dur="", ev="", head=False, note=""):
    """ec_b, ec_wall: (low, high) kWh/Nm3 CO; P_kw at the paper's boundary (None = NR)."""
    return dict(key=key, sid=sid, route=route, cls=cls, p=p, P_kw=P_kw, boundary=boundary, x=x, ec_b=ec_b,
                units=units, ec_wall=ec_wall, plug_basis=plug_basis, carbon=carbon, x_note=x_note, conv=conv,
                energy=energy, dur=dur, ev=ev, head=head, note=note)


ROWS = [
    # --- microwave, 2.45 GHz (same torch: SRC016, SRC017) ---
    R("Kiefer 2024 OP001", "SRC016", "MW 2.45 GHz", "M2", "~1.01", 2.70, "absorbed", "34.4", (1135 / KWH_NM3,) * 2,
      ec_wall=(19.6, 19.6), conv="moderate", energy="higher", dur="29 h at OP004", ev="SRC016-E011, E018, E044",
      head=True, note="best measured wall-plug result in the set; no pump"),
    R("Kiefer 2024 OP002", "SRC016", "MW 2.45 GHz", "M2", "0.15", 2.70, "absorbed", "38.6", (1011 / KWH_NM3,) * 2,
      ec_wall=(19.6, 19.6), conv="moderate", energy="higher", ev="SRC016-E012, E044", note="wall incl. vacuum pump"),
    R("Kiefer 2024 OP003", "SRC016", "MW 2.45 GHz", "M2", "0.90", 2.70, "absorbed", "56.6", (1734 / KWH_NM3,) * 2,
      ec_wall=(33, 33), conv="moderate", energy="higher", ev="SRC016-E019, E021, E044", head=True,
      note="highest conversion; wall incl. pump, figure read"),
    R("Kiefer 2024 OP004", "SRC016", "MW 2.45 GHz", "M2", "~1.01", 2.25, "absorbed", "~27", (1099 / KWH_NM3,) * 2,
      ec_wall=(20, 21), conv="moderate", energy="higher", dur="29.3 h", ev="SRC016-E024, E025",
      note="durability test plateau"),
    R("Hecimovic 2023 OP001", "SRC017", "MW 2.45 GHz", "M2", "~1.01", 2.70, "absorbed", "~34.5", (14.0, 14.0),
      conv="higher", energy="moderate", ev="SRC017-E011, E041, E042", note="same torch as SRC016"),
    R("Hecimovic 2023 OP002", "SRC017", "MW 2.45 GHz", "M2", "0.90", 2.70, "absorbed", "55", (17.6, 17.6),
      conv="higher", energy="moderate", ev="SRC017-E015, E041, E042", head=True, note="cooled effluent channels"),
    R("Hecimovic 2023 OP003", "SRC017", "MW 2.45 GHz", "M2", "0.90", 2.70, "absorbed", "~56.5", (21.3, 21.3),
      conv="higher", energy="moderate", ev="SRC017-E015, E042"),
    # --- microwave, 915 MHz and 2.45 GHz at reduced pressure ---
    R("Bongers 2017 OP001", "SRC018", "MW 915 MHz", "M1", "0.20", 8.1, "MW power", "83", (14.8, 14.8),
      conv="moderate", energy="lower", ev="SRC018-E003, E041", head=True, note="highest conversion; pump excluded"),
    R("Bongers 2017 OP002", "SRC018", "MW 915 MHz", "M1", "0.20", 3.1, "MW power", "47", (10.0, 10.0),
      conv="moderate", energy="lower", ev="SRC018-E041"),
    R("Bongers 2017 OP003", "SRC018", "MW 915 MHz", "M1", "0.20", 3.1, "MW power", "~10", (6.9, 6.9),
      conv="moderate", energy="lower", ev="SRC018-E041", head=True, note="best efficiency; pump excluded"),
    R("Bongers 2017 OP004", "SRC018", "MW 915 MHz", "M1", "0.20", 10.0, "MW power", "~22.5", (9.9, 9.9),
      conv="moderate", energy="lower", ev="SRC018-E042", note="text 40% eff., figure ~36%"),
    R("Bongers 2017 OP005", "SRC018", "MW 2.45 GHz", "M2", "0.4-0.6", None, "MW power", "~12.5", (7.7, 7.7),
      conv="moderate", energy="lower", ev="SRC018-E013"),
    # --- gliding arc ---
    R("Girard-Sahun 2022 OP001", "SRC019", "GA (AC)", "K1", "~1.01", 0.533, "plasma", "7.6", (13.0, 13.0),
      conv="higher", energy="moderate", dur="0.23 h", ev="SRC019-E041", head=True, note="no bed"),
    R("Girard-Sahun 2022 OP002", "SRC019", "GA (AC) + C bed", "K1", "~1.01", 0.533, "plasma", "12.6", (3.95, 3.95),
      carbon=0.26, conv="higher", energy="lower", dur="~1 min peak", ev="SRC019-E043, E044", head=True,
      note="transient peak; half of CO from carbon"),
    R("Girard-Sahun 2022 OP003", "SRC019", "GA (AC) + C bed", "K1", "~1.01", 0.533, "plasma", "~4.7", (12.8, 12.8),
      carbon=0.21, conv="higher", energy="lower", dur="14 min", ev="SRC019-E013, E043", head=True,
      note="after 14 min"),
    R("O'Modhrain 2024 OP001", "SRC020", "GA (DC) x5", "D1", "~1.01", 7.1, "plug", "8.7", (17.9, 17.9), units="5",
      ec_wall=(17.9, 17.9), plug_basis=True, conv="moderate", energy="higher", ev="SRC020-E006, E010, E043",
      head=True, note="plug incl. PSU (77-83%)"),
    R("O'Modhrain 2024 OP002", "SRC020", "GA (DC) x3", "D1", "~1.01", 4.3, "plug", "~7.6", (16.5, 16.5), units="3",
      ec_wall=(16.5, 16.5), plug_basis=True, conv="moderate", energy="higher", ev="SRC020-E042"),
    R("O'Modhrain 2024 OP003", "SRC020", "GA (DC) x1", "D1", "~1.01", 1.48, "plug", "~2.1", (15.5, 15.5), units="1",
      ec_wall=(15.5, 15.5), plug_basis=True, conv="moderate", energy="higher", ev="SRC020-E042"),
    R("Bryssinck 2025 OP001", "SRC021", "GA (DC) x7", "D1", "~1.01", 8.5, "plug", "~6.4 (inconsistent)", (16.9, 16.9),
      units="7", ec_wall=(16.9, 16.9), plug_basis=True, conv="lower", energy="lower", dur="200 s",
      ev="SRC021-E042", note="no bed; 12% CO implies ~12.8% conversion"),
    R("Bryssinck 2025 OP002", "SRC021", "GA (DC) x7 + C bed", "D1", "~1.01", 8.5, "plug", "~16", (7.0, 7.0), units="7",
      ec_wall=(7.0, 7.0), plug_basis=True, carbon=0.27, conv="moderate", energy="moderate", dur="200 s",
      ev="SRC021-E041, E043"),
    R("Bryssinck 2025 OP003", "SRC021", "GA (DC) x7 + C bed", "D1", "~1.01", 8.1, "plug", "20", (7.33, 7.33), units="7",
      ec_wall=(7.33, 7.33), plug_basis=True, carbon=0.27, conv="moderate", energy="moderate", dur="~0.15 h",
      ev="SRC021-E015, E043", head=True, note="pilot best; semi-continuous carbon feed"),
    R("Bryssinck 2025 OP004", "SRC021", "GA (DC) x7 + C bed", "D1", "~1.01", 9.5, "plug", "12.7 (total inlet)",
      (17.1, 17.1), units="7", ec_wall=(17.1, 17.1), plug_basis=True, carbon=None, conv="moderate", energy="moderate",
      dur="~0.1 h", ev="SRC021-E043", note="50% recycle; carbon use NR"),
    R("Kim 2014 OP001", "SRC028", "GA (AC) 3-phase", "K1", "~1 (NR)", 0.6, "plasma input", "7.8 (CR 12.3)", (9.14, 9.14),
      conv="lower", energy="lower", ev="SRC028-E042, E043",
      note="carbon-based X; reported CR is the uncorrected CO2 concentration drop; feed preheat (400 C) not counted"),
    R("Kim 2014 OP002", "SRC028", "GA (AC) 3-phase", "K1", "~1 (NR)", 0.6, "plasma input", "6.4 (CR ~10.3)", (7.81, 7.81),
      conv="lower", energy="lower", ev="SRC028-E042, E043", head=True,
      note="best efficiency (45% on X_C; 72% on reported CR, quoted ~61-65% in reviews); feed preheat (400 C) not counted"),
    # --- DC glow-to-arc ---
    R("Renninger 2022 OP001", "SRC022", "DC glow-to-arc", "D1", "~1.01", 0.162, "plasma", "27.4", (7.9, 7.9),
      conv="moderate", energy="moderate", dur="<10 h total", ev="SRC022-E004, E005, E042", head=True,
      note="12.8 kWh/Nm3 at lab driver DC input (61-65%)"),
    R("Renninger 2022 OP002", "SRC022", "DC glow-to-arc", "D1", "~1.01", 0.099, "plasma", "~17", (7.8, 7.8),
      conv="moderate", energy="moderate", ev="SRC022-E042"),
    R("Renninger 2022 OP003", "SRC022", "DC glow-to-arc", "D1", "~1.01", 0.217, "plasma", "~28.8", (19.3, 19.3),
      conv="moderate", energy="moderate", ev="SRC022-E041"),
    # --- nanosecond pulsed ---
    R("Yong 2023 OP001", "SRC023", "NRP (batch)", "P1", "5.8", 0.021, "deposited", "14", (15.1, 16.3),
      conv="moderate", energy="lower", dur="420 s batch", ev="SRC023-E041, E042", head=True,
      note="chamber volume per data set unclear"),
    R("Yong 2023 OP002", "SRC023", "NRP (batch)", "P1", "5.0", 0.024, "deposited", "3.3", (13, 13),
      conv="moderate", energy="lower", dur="120 s batch", ev="SRC023-E042"),
    # --- DBD ---
    R("Van Laer 2015 OP001", "SRC024", "packed DBD", "K1", "~1.01", 0.023, "plasma (implied)", "28.8 (rep. 37.8)",
      (71.0, 71.0), conv="moderate-lower", energy="lower", ev="SRC024-E041-E043", head=True,
      note="X expansion-corrected by reviewer (E043-E044)"),
    R("Van Laer 2015 OP002", "SRC024", "packed DBD", "K1", "~1.01", 0.034, "plasma (implied)", "32.6 (rep. 42.0)",
      (95.2, 95.2), conv="moderate-lower", energy="lower", ev="SRC024-E041-E043"),
    R("Van Laer 2015 OP003", "SRC024", "packed DBD", "K1", "~1.01", 0.020, "plasma (implied)", "6.9 (rep. 10.0)",
      (52.4, 52.4), conv="moderate-lower", energy="lower", ev="SRC024-E041-E043", head=True, note="best efficiency"),
    R("Van Laer 2015 OP004", "SRC024", "DBD (empty)", "K1", "~1.01", 0.021, "plasma (implied)", "14.2 (rep. ~19.9)",
      (136.6, 136.6), conv="moderate-lower", energy="lower", ev="SRC024-E041-E043"),
    # --- benchmarks: SOEC (stack DC; heat below V_tn not counted) and O2-membrane plasma demonstrator ---
    R("Kungas 2020 OP001", "SRC025", "SOEC stack", "J1", "NR", None, "stack DC", "NR", (2.5, 2.70),
      conv="lower", energy="moderate", ev="SRC025-E007, E013, E041", head=True,
      note="best cell voltage; Table I vs text mismatch; heat NR"),
    R("Kungas 2020 OP002", "SRC025", "SOEC stack", "J1", "NR", None, "stack DC", "NR", (2.96, 3.06),
      conv="lower", energy="moderate", dur="2000 h", ev="SRC025-E041", note="start -> end of test"),
    R("Kungas 2020 OP003", "SRC025", "SOEC stack", "J1", "NR", None, "stack DC", "NR", (3.3, 3.6),
      conv="lower", energy="moderate", dur="7600 h", ev="SRC025-E041", head=True, note="system test; start -> end"),
    R("Hecimovic 2024 OP001", "SRC026", "SOEC system (calc.)", "J1", "~1", 69.6, "stack DC", "86 (utilisation)",
      (3.98, 3.98), ec_wall=(4.19, 4.19), conv="moderate", energy="lower", ev="SRC026-E009, E041", head=True,
      note="wall = stack / 0.95 rectifier (authors); 17.5 Nm3/h CO"),
    R("Hecimovic 2024 OP002", "SRC026", "SOEC eCOs (vendor)", "", "~1", None, "total, NR", ">95 (vendor)", (6, 8),
      conv="moderate", energy="lower", dur="8000 h (SOEC)", ev="SRC026-E013, E014, E042", head=True,
      note="vendor web figure; boundary NR; inconsistent with stated 90%"),
    R("Hecimovic 2024 OP005", "SRC026", "MW 2.45 GHz + O2 membr.", "", "~1", 3.0, "total", "up to 26", (35, 35),
      ec_wall=(35, 35), conv="moderate", energy="moderate", ev="SRC026-E016, E042", head=True,
      note="5% of O2 removed; not a matched point"),
]


def fmt(lo, hi, nd=1):
    if lo is None:
        return "NR"
    a, b = f"{lo:.{nd}f}", f"{hi:.{nd}f}"
    return a if a == b else f"{a}-{b}"


def sig(v, n=2):
    """Rate with n significant figures."""
    return "NR" if v is None else f"{v:.{max(0, n - 1 - int(__import__('math').floor(__import__('math').log10(abs(v)))))}f}"


def compute(r):
    lo, hi = r["ec_b"]
    # plasma-side EC used for the industrial-supply estimate
    if r["plug_basis"]:
        pl = (lo * GA_PSU[0], hi * GA_PSU[1])
    elif r["boundary"].startswith(("total", "NR")):
        pl = None
    else:
        pl = (lo, hi)
    est = None
    if pl and r["cls"] in ETA:
        e_lo, e_hi = ETA[r["cls"]]
        est = (pl[0] / e_hi, pl[1] / e_lo)
    r["ec_plasma"] = pl
    r["ec_est"] = est
    r["co_rate"] = (r["P_kw"] / ((lo + hi) / 2)) if r["P_kw"] else None
    best_wall = r["ec_wall"] or est
    r["bed"] = "C bed" in r["route"]
    if best_wall is None or r["sid"] in ("SRC025",):
        r["eta_wall"] = None
    elif r["bed"]:   # workflow 1.1: eta_LHV with the carbon counted as an energy input
        c_in = r["carbon"] * LHV_C_KWH_KG if r["carbon"] else None
        r["eta_wall"] = None if c_in is None else \
            (LHV_CO_KWH / (best_wall[1] + c_in) * 100, LHV_CO_KWH / (best_wall[0] + c_in) * 100)
    else:
        r["eta_wall"] = (EC_DH / best_wall[1] * 100, EC_DH / best_wall[0] * 100)
    return r


CONF = {"higher": "H", "moderate": "M", "lower": "L", "moderate-lower": "M-L", "": "NR"}
BND = {"absorbed": "abs", "MW power": "MW", "plasma (implied)": "plasma*", "deposited": "dep"}


def table(headers, rows):
    w = [max(len(h), *(len(x[i]) for x in rows)) for i, h in enumerate(headers)]
    line = lambda c: " | ".join(s.ljust(w[i]) for i, s in enumerate(c)).rstrip()
    return "\n".join([line(headers)] + [line(c) for c in rows])


def main():
    rows = [compute(r) for r in ROWS]
    cols = ["row_key", "source_id", "route", "supply_class", "eta_class_low", "eta_class_high", "p_bar", "units",
            "P_kW_at_boundary", "power_boundary", "X_CO2_pct", "EC_CO_boundary_low", "EC_CO_boundary_high",
            "EC_CO_wall_measured_low", "EC_CO_wall_measured_high", "EC_CO_plasma_side_low", "EC_CO_plasma_side_high",
            "EC_CO_industrial_est_low", "EC_CO_industrial_est_high", "eta_wall_pct_low", "eta_wall_pct_high",
            "carbon_kg_per_Nm3_CO", "CO_Nm3_per_h", "duration", "conv_confidence", "energy_confidence",
            "headline", "evidence", "notes"]
    rnd = lambda v, n=2: "" if v is None else round(v, n)
    with open(HERE / "co2_synthesis.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(cols)
        for r in rows:
            e = ETA.get(r["cls"], (None, None))
            g = lambda t, i: rnd(t[i]) if t else ""
            w.writerow([r["key"], r["sid"], r["route"], r["cls"], rnd(e[0]), rnd(e[1]), r["p"], r["units"],
                        rnd(r["P_kw"], 3), r["boundary"], r["x"], g(r["ec_b"], 0), g(r["ec_b"], 1),
                        g(r["ec_wall"], 0), g(r["ec_wall"], 1), g(r["ec_plasma"], 0), g(r["ec_plasma"], 1),
                        g(r["ec_est"], 0), g(r["ec_est"], 1), g(r["eta_wall"], 0), g(r["eta_wall"], 1),
                        rnd(r["carbon"]), "" if r["co_rate"] is None else float(sig(r["co_rate"], 3)), r["dur"], r["conv"], r["energy"],
                        "yes" if r["head"] else "", r["ev"], r["note"]])

    H = [r for r in rows if r["head"]]
    plasma = [r for r in H if r["sid"] not in ("SRC025", "SRC026")]
    bench = [r for r in H if r["sid"] in ("SRC025", "SRC026")]

    def cells(r):
        c = f"{r['carbon']:.2f}" if r["carbon"] else ("NR" if r["bed"] else "-")
        return [r["key"], r["route"], r["cls"] or "-", r["p"], fmt(r["P_kw"], r["P_kw"], 2) if r["P_kw"] else "NR",
                sig(r["co_rate"]), r["x"],
                f"{fmt(*r['ec_b'])} {BND.get(r['boundary'], r['boundary'])}", fmt(*r["ec_wall"]) if r["ec_wall"] else "-",
                fmt(*r["ec_est"]) if r["ec_est"] else "-", fmt(*r["eta_wall"], 0) if r["eta_wall"] else "-", c,
                f"{CONF[r['conv']]}/{CONF[r['energy']]}"]

    hd = ["Source / OP", "Route", "Class", "p (bar)", "P (kW)", "CO (Nm3/h)", "X_CO2 (%)",
          "EC paper", "EC wall", "EC ind.", "eta_wall (%)", "C (kg/Nm3)", "Conf."]
    md = f"""# CO2 splitting: synthesis tables

Generated by `build_synthesis.py` from the extractions SRC016-SRC026 and SRC028 (all ai_checked; human verification pending).
All rows, with evidence IDs and notes: `co2_synthesis.csv`. Below: headline operating points only.

EC = EC_CO in kWh/Nm3 CO (0 C, 1 atm; 1 kWh/Nm3 = 80.69 kJ/mol): "paper" at the paper's own power boundary
(abs = absorbed microwave; MW = "MW power", undefined; plasma* = implied from reported X and eta; dep = deposited
pulse energy; plug = whole process), "wall" measured by the authors, "ind." with an industrial supply (estimate).
Conf. = confidence in conversion / energy results from the extraction (H higher, M moderate, L lower). Reference lines: {EC_DH:.2f} kWh/Nm3 = 100% on
dH (282.7 kJ/mol); {EC_DG:.2f} kWh/Nm3 = dG at 298 K (257 kJ/mol).

## 1. Plasma exemplars (headline points)

{table(hd, [cells(r) for r in plasma])}

[1] P is at the paper's power boundary. CO (Nm3/h) =
    P / EC_CO at that boundary.
[2] EC wall: wall or plug electricity measured by the authors (Kiefer: microwave supply active power,
    + vacuum pump at OP003; O'Modhrain and Bryssinck: plug, whole process). Only three sources measured it.
[3] EC ind.: reviewer estimate = EC_CO at the plasma side / class efficiency (power_systems/
    supply_classes.csv): M1 {fmt(*ETA['M1'], 2)}, M2 {fmt(*ETA['M2'], 2)}, D1 {fmt(*ETA['D1'], 2)},
    K1 {fmt(*ETA['K1'], 2)}, P1 {fmt(*ETA['P1'], 2)}. Plug-basis gliding-arc rows are first moved to the plasma side with
    the measured arc-supply efficiency {GA_PSU[0]}-{GA_PSU[1]} (SRC020-E010; SRC021 implies 0.83), so the
    estimate replaces the lab supply with a D1-class supply. Vacuum pumps, chillers and gas handling are not added.
[4] eta_wall = {EC_DH:.2f} / EC_CO (measured wall where available, else the industrial-supply estimate). Carbon-bed
    rows: eta_LHV with the carbon counted as an energy input = LHV of CO / (EC_CO + C x LHV_C), LHV_CO 283.0 kJ/mol,
    LHV_C 393.5 kJ/mol (graphite) (workflow 1.1). EC_CO there is electricity only. Not given where C is NR.
[5] Bongers (SRC018) and Kiefer OP002-OP003 run below 1 bar; Bongers excludes the pump. Kiefer measured it
    (OP002 wall + pump 4.2 kW vs 3.8 kW without pump at OP001).
[6] Van Laer (SRC024) conversions are likely not expansion-corrected; X and EC_CO are on the reviewer's
    expansion-corrected conversion (reported X in brackets; EC_CO ~30% above the reported basis; SRC024-E044,
    since 2026-11-26). Plasma power implied from reported X and eta.
[7] Yong (SRC023) is a batch reactor; P is deposited pulse power. P1 is a provisional sensitivity range
    combining source-to-reactor transfer and other system-efficiency measurements with different boundaries;
    it is not a demonstrated mains-to-reactor range. Upstream conversion losses are unresolved.
[8] Renninger (SRC022) is on plasma power; its lab driver DC input gives 12.8 kWh/Nm3 (driver 61-65%).
[13] Kim (SRC028): X_CO2 is the reviewer's carbon-based conversion CO/(CO + CO2) from Fig. 2b; the authors' CR
     (in brackets) is the CO2 concentration drop without expansion correction (CO selectivity ~57%). On CR the
     efficiency would be 60-72%, the source of the ~61-65% quoted in reviews. Feed preheated in a 400 C steam
     generator (Fig. 1), not counted (~16 kJ/mol; eta ~30-32% if counted). "Plasma input" power, method NR.

## 2. Benchmarks (SOEC and the plasma O2-membrane demonstrator)

{table(["Source / OP", "Route", "P (kW)", "Conversion / util. (%)", "EC_CO paper basis", "EC_CO wall",
        "EC_CO ind. supply", "Duration", "Conf. (conv / energy)"],
       [[r["key"], r["route"], fmt(r["P_kw"], r["P_kw"]) if r["P_kw"] else "NR", r["x"],
         f"{fmt(*r['ec_b'], 2)} ({r['boundary']})", fmt(*r["ec_wall"], 2) if r["ec_wall"] else "-",
         fmt(*r["ec_est"], 2) if r["ec_est"] else "-", r["dur"] or "NR", f"{r['conv']} / {r['energy']}"]
        for r in bench])}

[9] SOEC stack DC from cell voltage (Kungas: EPC = E n F / (FE Vm)). Below the thermoneutral 1.465 V heat must be
    supplied; heat duties are not reported and not included. Arrows give start -> end of the durability test.
[10] Ind. supply = stack DC / J1 rectifier ({fmt(*ETA['J1'], 3)}). Hecimovic 2024 OP001 wall uses the authors' 0.95.
     Like-for-like caveat: the FZJ system value (4.19 kWh/Nm3, 84% on LHV) is stack DC + rectifier only. At ~1.66 V
     the stack releases ~37 kJ/mol CO above dH, about the ~42 kJ/mol needed to preheat the CO2 feed to 800 C, so
     with recuperation sensible heat is not a large missing term. Not included: balance-of-plant electricity
     (blowers, CO recycle, trim heaters), heat losses, hot standby, degradation (Kungas +3-9% over 2000-7600 h)
     and CO purification. The vendor plant figure (eCOs, 6-8 kWh/Nm3, 44-58%) is the only wall-to-product number.
     The plasma wall values have the same gap (chillers, pumps and CO separation excluded; product mostly CO2),
     so the comparison is reactor + supply on both sides: the closest like-for-like the literature allows.
[11] eCOs 6-8 kWh/Nm3 is a vendor web figure with no stated boundary (SRC026-E013).
[12] The membrane demonstrator removed 5% of the O2; 35 kWh/Nm3 is the authors' total and not a matched point.

## 3. Reading the tables (reviewer summary, for the narrative)

- Measured wall or plug energy for plasma without carbon is 15.5-33 kWh/Nm3 CO (Kiefer, O'Modhrain, Bryssinck
  no-bed, whose control is internally inconsistent; all rows in the CSV): about 4-8x the SOEC system value (4.2 incl. rectifier) and 4-9x the 100% line.
- Kiefer's measured wall value (19.6 kWh/Nm3 at OP001; absorbed/wall power 0.72) sets the upper end of the M2 range;
  the independent supply x tube estimate (0.59-0.71) is consistent with it.
- With industrial supplies, the lowest plasma results without carbon (Bongers OP003, Renninger OP001) would be
  ~8-9 kWh/Nm3, at 10-27% conversion and before separation and O2 removal; Bongers at 0.2 bar with the pump
  excluded, Renninger at 0.16 kW.
- High conversion (55-83%) costs ~18-34 kWh/Nm3 on the wall or industrial-supply basis.
- Carbon beds reach 7.3 kWh/Nm3 at the plug (Bryssinck OP003; ~5.8-6.6 with a D1 supply) plus 0.27 kg C per
  Nm3 CO.
- Counting the carbon (eta_LHV), the Girard-Sahun bed reaches ~52% only at its ~1 min peak and falls to ~22%
  after 14 min, below the no-bed value; Bryssinck's semi-continuous run holds ~36% at the plug over ~9 min. The
  lasting benefit of a bed is O2 removal; half the CO comes, net, from consumed carbon.
- Unit scale: largest plasma unit 10 kW (Bongers); largest CO output ~1.1-1.2 Nm3/h (Bryssinck, with carbon).
  The SOEC system case is 17.5 Nm3/h at 70 kW.
"""
    (HERE / "co2_synthesis_tables.md").write_text(md, encoding="utf-8")
    for r in rows:
        print(f"{r['key']:26s} {r['cls']:3s} ECb {fmt(*r['ec_b'])}  wall {fmt(*r['ec_wall']) if r['ec_wall'] else '-':>6s}"
              f"  est {fmt(*r['ec_est']) if r['ec_est'] else '-':>10s}  CO {r['co_rate'] or 0:.3f} Nm3/h"
              f"  eta {fmt(*r['eta_wall'], 0) if r['eta_wall'] else '-'}")


if __name__ == "__main__":
    main()
