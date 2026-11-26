"""Reforming synthesis: evidence tables from the short summaries (literature_reforming/*/short_summary.txt).

Run from the repository root:  ~/.venvs/science/bin/python literature_reforming/0_synthesis/build_synthesis.py
Writes reforming_synthesis.csv (all rows) and reforming_synthesis_tables.md (tables by route, benchmarks, notes).

Values are copied from each source's short summary, including the corrections from the GPT cross-check
(cross_check_log.md). EC_CH4 is kJ per mol CH4 converted, at each paper's power boundary. The industrial-supply
estimate is EC_CH4 / class efficiency from power_systems/supply_classes.csv (read at run time): the lab supply is
replaced by a representative industrial supply; steam generation, furnace heat, cooling and auxiliaries are not added.
"""
import csv
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
SUP = {r["class_id"]: r for r in csv.DictReader(open(ROOT / "power_systems" / "supply_classes.csv", encoding="utf-8"))}
ETA = {k: (float(v["eta_low"]), float(v["eta_high"])) for k, v in SUP.items() if v["eta_low"]}
# 400 kHz scenario: 0.91 extrapolated from the 1-200 kHz family (PW004-V02);
# >0.96 is a claim for 100-400 kHz equipment (PW005-V02), not a matched measurement.
ETA["K2@400kHz"] = (0.91, 0.96)
DH = {"SMR": 206, "DRM": 247}         # kJ/mol at 298 K, reference lines


def R(key, sid, route, act, cls, ch4, ratio, T, P_kw, boundary, heat, x_ch4, x_co2, sei, ec, dur, conv, energy,
      head=False, ev="", note=""):
    """ec: (low, high) kJ/mol CH4 converted at the paper boundary, or None."""
    return dict(key=key, sid=sid, route=route, act=act, cls=cls, ch4=ch4, ratio=ratio, T=T, P_kw=P_kw,
                boundary=boundary, heat=heat, x_ch4=x_ch4, x_co2=x_co2, sei=sei, ec=ec, dur=dur, conv=conv,
                energy=energy, head=head, ev=ev, note=note)


ROWS = [
    # ---------- SMR: Joule-heated benchmark (lab) ----------
    R("Wismann 2019 OP004", "SRC001", "SMR", "Joule (lab)", "J1", 4.6e-3, "1:0:2 +H2", "~750 wall", None, "NR", "steam, preheat NR",
      "92.7", "NA", None, None, ">=0.75 h avg.", "M", "L", True, "SRC001-E050-E085", "no electrical power reported"),
    R("Wismann 2019 OP012", "SRC001", "SMR", "Joule (lab)", "J1", 2.3e-2, "1:0:2 +H2", "~780 wall", None, "NR", "steam, preheat NR",
      "85.0", "NA", None, None, ">=0.75 h avg.", "M", "L", False, "SRC001-E050-E085", "no electrical power reported"),
    # ---------- SMR: thermal arc ----------
    R("Hrabovsky 2018 OP001", "SRC007", "SMR", "DC arc torch", "A1", 6.69, "1:0:0.78", "927-1127 reactor", 120, "arc",
      "none (water evaporated by plasma)", "91.3", "NA", 1076, (1179, 1179), "~4 min segment", "M", "M", True,
      "SRC007-E041, E046", "conversion from Ar tracer (reviewer; XR007 for human check)"),
    R("Hrabovsky 2018 OP002", "SRC007", "SMR", "DC arc torch", "A1", 3.35, "1:0:0.63", "927-1127 reactor", 120, "arc",
      "none (water evaporated by plasma)", "99.1", "NA", 2152, (2172, 2172), "~4 min segment", "M", "M", False,
      "SRC007-E042, E046", "conversion from Ar tracer (reviewer)"),
    # ---------- SMR: microwave ----------
    R("Akande 2022 OP003", "SRC008", "SMR", "MW 915 MHz torch", "M1", 2.68, "1:0:3", "500-650 reformer", 32, "absorbed MW",
      "steam generator NR", "96.6", "NA", 717, (742, 742), "NR", "L", "L", True, "SRC008-E014, E046",
      "reported H2 rate exceeds the stoichiometric limit; corrigendum composition gives ~83% (OP008)"),
    R("Akande 2022 OP001", "SRC008", "SMR", "MW 915 MHz torch", "M1", 2.68, "1:0:3", "500-650 reformer", 17, "absorbed MW",
      "steam generator NR", "74.6", "NA", 381, (511, 511), "NR", "L", "L", False, "SRC008-E014", ""),
    R("Akande 2022 OP006", "SRC008", "SMR", "MW 915 MHz torch", "M1", 2.68, "1:0:3", "500-650 reformer", 47, "absorbed MW",
      "steam generator NR", "97.7", "NA", 1053, (1078, 1078), "NR", "L", "L", False, "SRC008-E014", ""),
    R("Hrycak 2023 OP002", "SRC010", "SMR", "MW 915 MHz", "M1", 2.06, "1:0:1.35", "NR (steam 250-350)", 6.5, "absorbed MW",
      "steam vaporizer NR", "66.1", "NA", 189, (286, 286), "NR", "M", "L", True, "SRC010-E041",
      "Vm 24.25 L/mol (XR008); 7.6% lower at 0 degC; carbon closure ~71%"),
    # ---------- SMR: gliding arc / DBD ----------
    R("Zhu 2019 OP004", "SRC012", "SMR", "DC gliding arc + Ni cat.", "D1", 0.033, "1:0:3", "977-651 bed", 0.246, "discharge",
      "steam generation excl.", "90", "NA", 441, (490, 490), "6 h", "H", "M", True, "SRC012-E042",
      "plasma-catalytic; ~646 kJ/mol with indicative steam duty"),
    R("Zhu 2019 OP003", "SRC012", "SMR", "DC gliding arc", "D1", 0.033, "1:0:3", "NR", 0.246, "discharge",
      "steam generation excl.", "65", "NA", 441, (679, 679), "NR", "H", "M", False, "SRC012-E042", "plasma alone"),
    R("Geng 2022 OP002", "SRC002", "SMR", "DBD + Ni cat.", "K1", 1.0e-3, "1:0:4.4", "300 bulk", 0.015, "discharge",
      "furnace 300 degC + steam, NR", "~60", "NA", 894, (1490, 1490), "~2 h series", "M", "L", True, "SRC002-E065-E067",
      "feed confirmed by BB; plasma-off control ~7%"),
    R("Geng 2022 OP008", "SRC002", "SMR", "DBD + Ni cat.", "K1", 1.0e-3, "1:0:4.4", "440 bulk", 0.015, "discharge",
      "furnace 440 degC + steam, NR", "~80", "NA", 894, (1120, 1120), "NR", "M", "L", False, "SRC002-E068", ""),
    # ---------- DRM ----------
    R("Song 2020 OP013", "SRC009", "DRM", "RF ICP torch 400 kHz", "K2@400kHz", 1.61, "1:0.83:0", "NR", 22, "RF generator",
      "none", "79.3", "87.1", 822, (1036, 1036), "NR", "M", "M", True, "SRC009-E041",
      "author efficiency 57% (headline); boundary contradictory (absorbed vs delivered)"),
    R("Song 2020 OP009", "SRC009", "DRM", "RF ICP torch 400 kHz", "K2@400kHz", 1.34, "1:1:0", "NR", 27, "RF generator",
      "none", "94", "94", 1210, (1288, 1288), "NR", "M", "M", False, "SRC009-E041", ""),
    R("Song 2020 OP010", "SRC009", "DRM", "RF ICP torch 400 kHz", "K2@400kHz", 0.89, "1:1.5:0", "NR", 22, "RF generator",
      "none", "98.0", "88.7", 1479, (1510, 1510), "NR", "M", "M", False, "SRC009-E041", ""),
    R("Kelly 2023 OP004", "SRC011", "DRM", "MW 2.45 GHz", "M2", 0.187, "1:1.22:0", "~404 exhaust", 1.0, "absorbed MW",
      "none", "55.2", "45.8", 321, (581, 581), "~0.25 h", "H", "H", True, "SRC011-E041", ""),
    R("Kelly 2023 OP001", "SRC011", "DRM", "MW 2.45 GHz", "M2", 0.125, "1:2.33:0", "~453 exhaust", 1.0, "absorbed MW",
      "none", "66.5", "49.4", 481, (723, 723), "~0.25 h", "H", "H", False, "SRC011-E041", ""),
    R("Kwon 2023 OP003", "SRC014", "DRM", "AC rotating GA + quench", "K1", 0.268, "1:1:0 (+50% N2)", "~370 TC1", 1.668,
      "discharge", "none", "50.5", "40.3", 374, (740, 740), "~0.2 h", "H", "H", True, "SRC014-E042",
      "author efficiency 53.2%"),
    R("Kwon 2023 OP002", "SRC014", "DRM", "AC rotating GA + quench", "K1", 0.223, "1:1.4:0 (+50% N2)", "~360 TC1", 1.672,
      "discharge", "none", "51.1", "40.2", 450, (880, 880), "~0.2 h", "H", "H", False, "SRC014-E042",
      "author efficiency 55.3%"),
    R("Wanten 2022 OP006", "SRC015", "DRM", "DC confined glow", "D1", 0.0146, "1:1.86:0", "NR", 0.145, "plasma",
      "none", "~73.5", "~54.8", 598, (813, 813), "NR", "H", "M", True, "SRC015-E042",
      "300 kOhm lab ballast excluded (plasma 28-39% of supply output)"),
    R("Wanten 2022 OP003", "SRC015", "DRM", "DC confined glow", "D1", 0.0052, "1:3:0", "NR", 0.097, "plasma",
      "none", "94.28", "63.7", 1126, (1194, 1194), "NR", "H", "M", False, "SRC015-E042", "highest CH4 conversion"),
    R("Kaufmann 2026 OP001", "SRC027", "DRM", "DC rotating glow", "D1", 0.134, "1:1:0", "NR", 0.54, "plasma",
      "none", "~42", "~38.5", 241, (574, 574), "2-5 min run", "M", "M", False, "SRC027-E042",
      "20 mm, 0.24 A; power-electronic current control, no ballast; supply output 640 kJ/mol (driver 88-94%)"),
    R("Kaufmann 2026 OP002", "SRC027", "DRM", "DC rotating glow", "D1", 0.134, "1:1:0", "NR", 1.43, "plasma",
      "none", "~66", "~70", 641, (971, 971), "2-5 min run", "M", "M", True, "SRC027-E043",
      "40 mm, 0.4 A; P = SEI x flow (text quotes 1660 W); supply output 1080 kJ/mol"),
    R("Kaufmann 2026 OP003", "SRC027", "DRM", "DC rotating glow", "D1", 0.107, "1:1.5:0", "NR", 1.10, "plasma",
      "none", "~52.5", "~56", 618, (1178, 1178), "2-5 min run", "M", "M", False, "SRC027-E044",
      "60/40 CO2/CH4: little solid carbon (S_C,CO ~93%)"),
    R("Andersen 2020 OP001", "SRC013", "DRM", "DBD (no packing)", "K1", 1.02e-3, "1:1:0", "ambient", 0.045, "discharge",
      "none", "32.6", "22.4", 2642, (8103, 8103), "1 h", "M", "H", True, "SRC013-E042", "best packed case (Cu) same EC_CH4"),
    # ---------- mixed reforming ----------
    R("Hrabovsky 2018 OP005", "SRC007", "mixed", "DC arc torch", "A1", 5.58, "1:0.81:0.18", "927-1127 reactor", 116, "arc",
      "none", "95.3", "91.0", 1248, (1309, 1309), "~2 min segment", "M", "M", True, "SRC007-E043, E046",
      "CO2 + torch steam (our DRM label); Ar tracer conversion (XR007)"),
    R("Hrabovsky 2018 OP008", "SRC007", "mixed", "DC arc torch", "A1", 5.58, "1:0.81:0.18", "927-1127 reactor", 89, "arc",
      "none", "83.3", "89.0", 958, (1149, 1149), "~6 min segment", "M", "M", False, "SRC007-E044, E046", ""),
    R("Hrycak 2023 OP001", "SRC010", "mixed", "MW 915 MHz", "M1", 3.09, "1:0.33:0.90", "NR (steam 250-350)", 6.5,
      "absorbed MW", "steam vaporizer NR", "48.9", "~44", 126, (258, 258), "NR", "M", "L", True, "SRC010-E041",
      "best H2 rate 239 g/h; Vm 24.25 (XR008); carbon closure ~74%"),
    R("Hrycak 2023 OP003", "SRC010", "mixed", "MW 915 MHz", "M1", 1.03, "1:1:1.79", "NR (steam 250-350)", 6.5,
      "absorbed MW", "steam vaporizer NR", "74.3", "~60", 378, (509, 509), "NR", "M", "L", False, "SRC010-E041", ""),
    R("From 2024 OP001", "SRC005", "mixed", "Joule (eSMR pilot)", "J1", None, "biogas; S/C 2.7", "900 cat. exit", None, "NR",
      "steam, preheat NR", "97", "NR", None, None, "~1 h steady", "M", "NA", True, "SRC005-E013",
      "10 barg; equilibrium conversion"),
    R("From 2024 OP003", "SRC005", "mixed", "Joule (eSMR pilot)", "J1", None, "biogas; S/C 2.1", "950 cat. exit", None, "NR",
      "steam, preheat NR", "94", "NR", None, None, "1535 h TOS", "M", "NA", False, "SRC005-E016-E017",
      "20 barg; no deactivation over 1050 h"),
    R("From 2024 OP004-OP007", "SRC005", "mixed", "Joule (eSMR pilot)", "J1", None, "biogas; S/C 2-2.2", "900 cat. exit",
      None, "Q_in (PSU)", "steam, preheat, compression excl.", "94-97 (eq., est.)", "NR", None, (388, 485), "NR", "L", "L",
      True, "SRC005-E043-E045",
      "reviewer estimate C004: equilibrium Q_reaction / author efficiency 71.5-79.5%; ~23-35 kW if Fig. 5 axis is Q_in"),
    R("From 2025 OP002", "SRC006", "mixed", "Joule (eSMR pilot)", "J1", 2.55, "biogas + H2; S/HC 2.3", "900 exit gas", None,
      "NR", "steam, preheat NR", "~98", "~42-54", None, None, "80 h", "M", "NA", True, "SRC006-E013, E042",
      "6 barg; power confidential; conversion reviewer-calculated"),
]

# Fired SMR references (design studies; heat basis)
FIRED = [
    dict(key="Lewis (NETL) 2022 OP001", sid="SRC003", scale="20,126 kg/h H2 (CH4 ~59,970 mol/min)", T="871 outlet, 28.3 bar",
         x="77.7 (reformer)", ec_abs=340, ec_fired=577, eta="75.7 (plant, H2 only)", fel="1.2% (grid aux.)",
         note="steam export ~143 MW not credited; author ETE 75.4% HHV"),
    dict(key="Collodi (IEAGHG) 2017 OP001", sid="SRC004", scale="8,994 kg/h H2 (CH4 ~21,600 mol/min)", T="~900-950 outlet",
         x="84.6 (pre-reformer + reformer)", ec_abs=315, ec_fired=574, eta="81.1 (plant, H2 only)", fel="0 (9.9 MWe export)",
         note="83.4% including exported power"),
]
JOULE_BENCH = [
    ("From 2024 OP004 / OP007", "author reactor efficiency ~72% at ~25 kW and ~80% at ~35 kW (Fig. 5; includes sensible "
     "heating 400 -> 900 degC; I x V boundary). Reviewer estimate EC_CH4 388-485 kJ/mol at Q_in from equilibrium "
     "Q_reaction / efficiency (SRC005-C004, E043-E045); not measured"),
    ("Topsoe eREACT (vendor claim)", "~1 kWh/Nm3 H2 system electricity (~81 kJ/mol H2); boundary not stated (PW037-V01)"),
]
NOT_PLOTTED = [
    ("Wismann 2019 (all OPs)", "no point-matched electrical power"),
    ("From 2024 OP001, OP003; From 2025 (all)", "no point-matched power and feed (From 2025 power confidential)"),
    ("Geng 2022 OP001", "plasma off (furnace only); ~7% conversion"),
    ("Andersen 2020 OP006", "plasma off; ~1.5% conversion"),
    ("Akande 2022 H2 rate / energy yield", "exceeds the stoichiometric limit for the stated feed (not usable)"),
]


def num(s):
    try:
        return float(str(s).lstrip("~").split()[0])
    except (ValueError, IndexError):
        return None


def compute(r):
    if r["ec"] and r["cls"] in ETA:
        e_lo, e_hi = ETA[r["cls"]]
        r["ec_est"] = (r["ec"][0] / e_hi, r["ec"][1] / e_lo)
    else:
        r["ec_est"] = None
    return r


def fmt(lo, hi, d=0):
    a, b = f"{lo:.{d}f}", f"{hi:.{d}f}"
    return a if a == b else f"{a}-{b}"


def table(rows, header):
    cols = list(zip(*([header] + rows)))
    widths = [max(len(str(c)) for c in col) for col in cols]
    line = lambda vals: " | ".join(str(v).ljust(w) for v, w in zip(vals, widths)).rstrip()
    return "\n".join([line(header)] + [line(r) for r in rows])


def main():
    rows = [compute(r) for r in ROWS]
    with open(HERE / "reforming_synthesis.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["row_key", "source_id", "route", "activation", "supply_class", "CH4_feed_mol_min", "CH4_CO2_H2O",
                    "T_degC_location", "P_kW", "power_boundary", "external_heat", "X_CH4_pct", "X_CO2_pct",
                    "SEI_CH4_kJ_mol", "EC_CH4_low", "EC_CH4_high", "EC_CH4_industrial_est_low",
                    "EC_CH4_industrial_est_high", "duration", "conv_confidence", "energy_confidence", "headline",
                    "evidence", "notes"])
        for r in rows:
            w.writerow([r["key"], r["sid"], r["route"], r["act"], r["cls"], r["ch4"] if r["ch4"] is not None else "",
                        r["ratio"], r["T"], r["P_kw"] if r["P_kw"] is not None else "", r["boundary"], r["heat"],
                        r["x_ch4"], r["x_co2"], r["sei"] if r["sei"] is not None else "",
                        *(r["ec"] if r["ec"] else ("", "")),
                        *((round(r["ec_est"][0]), round(r["ec_est"][1])) if r["ec_est"] else ("", "")),
                        r["dur"], r["conv"], r["energy"], "yes" if r["head"] else "", r["ev"], r["note"]])

    def trow(r):
        p = "NR" if r["P_kw"] is None else (f"{r['P_kw']:.3f}" if r["P_kw"] < 1 else f"{r['P_kw']:g}")
        ch4 = "NR" if r["ch4"] is None else (f"{r['ch4']:.2g}" if r["ch4"] < 0.1 else f"{r['ch4']:.3g}")
        return [r["key"], r["act"], r["cls"].split("@")[0], ch4, r["ratio"], p, r["boundary"], r["x_ch4"], r["x_co2"],
                "-" if r["sei"] is None else f"{r['sei']:g}", "NR" if not r["ec"] else fmt(*r["ec"]),
                fmt(*r["ec_est"]) if r["ec_est"] else "-", r["dur"], f"{r['conv']}/{r['energy']}"]

    hdr = ["Source / OP", "Activation", "Class", "CH4 (mol/min)", "CH4:CO2:H2O", "P (kW)", "Boundary", "X_CH4 (%)",
           "X_CO2 (%)", "SEI_CH4", "EC_CH4", "EC ind.", "Duration", "Conf."]
    parts = [f"""# Reforming synthesis tables

Built by build_synthesis.py from the short summaries (literature_reforming/*/short_summary.txt), including the
corrections from the GPT cross-check (../cross_check_log.md). Headline rows first within each source; supporting
rows in reforming_synthesis.csv. NR = not reported; NA = not applicable; ~ = approximate.

SEI_CH4 = kJ per mol CH4 fed; EC_CH4 = kJ per mol CH4 converted, both at each paper's power boundary (external heat
excluded). EC ind. = EC_CH4 with a representative industrial supply = EC_CH4 / class efficiency
(power_systems/supply_classes.csv) [1]. Reaction enthalpies at 298 K: SMR {DH['SMR']}, DRM {DH['DRM']} kJ/mol CH4.
Conf. = confidence in conversion / energy results from the extraction (H higher, M moderate, L lower).
"""]
    for route, title in (("SMR", "1. Steam methane reforming (SMR)"), ("DRM", "2. Dry reforming (DRM)"),
                         ("mixed", "3. Mixed reforming (CO2 + steam, biogas)")):
        sel = [trow(r) for r in rows if r["route"] == route and r["head"]]
        parts.append(f"## {title}\n\n" + table(sel, hdr) + "\n")
    fired = table([[f["key"], f["scale"], f["T"], f["x"], f["ec_abs"], f["ec_fired"], f["eta"], f["fel"]] for f in FIRED],
                  ["Source / OP", "Scale", "T (degC), p", "X_CH4 (%)", "EC_CH4,abs", "EC_CH4,fired (HHV)",
                   "eta_HHV (%)", "f_electric"])
    parts.append("## 4. Benchmarks\n\nFired SMR references: design studies, heat basis (kJ per mol CH4 converted in the "
                 "reformer); not electrical. EC_CH4,abs = heat absorbed by the reformer tubes; EC_CH4,fired = burner "
                 "fuel (HHV).\n\n" + fired + "\n\n" + "\n".join(f"- {f['key']}: {f['note']}." for f in FIRED) +
                 "\n\nJoule-heated benchmarks:\n\n" + "\n".join(f"- **{k}:** {v}." for k, v in JOULE_BENCH) + "\n")
    parts.append("## 5. Not plotted\n\n" + "\n".join(f"- **{k}:** {v}." for k, v in NOT_PLOTTED) + "\n")
    notes = [f"[1] Class efficiencies: " + ", ".join(f"{k} {fmt(*v, 2)}" for k, v in ETA.items() if k in
              {r['cls'] for r in rows}) + ". RF ICP (Song) uses a K2 scenario at 400 kHz: "
             "0.91 is extrapolated from a 1-200 kHz family (PW004-V02); >0.96 is a claim at 100-400 kHz "
             "(PW005-V02). CEIA's 100 kW is an input rating; PW006 documents 50 kW output. "
             "A tube oscillator (R1, 0.53-0.60) would give ~1.6-1.8x higher values. "
             "Wanten and Zhu exclude their lab ballast resistors; the estimate replaces the ballasted lab supply "
             "with a D1 current-controlled supply. Kaufmann already uses a current-controlled driver (88-94% of the DC supply"
             " output reaches the plasma).",
             "[2] External heat is excluded from every EC_CH4: furnace (Geng), steam generation (Akande, Hrycak, Zhu, "
             "the From pilots) and feed preheat are not reported. These EC_CH4 are lower bounds on electricity per mol "
             "CH4; Hrabovsky's torch evaporates its own water, so arc power is its whole process heat.",
             "[3] Hrabovsky conversions are reviewer calculations from the Ar tracer; they match the authors' plotted "
             "points (cross-check XR007, for human check). Hrycak uses 24.25 L/mol (XR008).",
             "[4] Akande's reported H2 rate is impossible for the stated feed; its conversion and EC_CH4 are kept with "
             "lower confidence.",
             "[5] Kwon feeds 50% N2; Hrycak and Akande add steam from a separate vaporizer. Unit scale: Hrabovsky "
             "~90-120 kW, Akande 17-47 kW, Song 22-27 kW, Hrycak 4.5-6.5 kW, Kwon ~1.7 kW, Kaufmann 0.5-1.4 kW, Kelly 1 kW; Zhu, Wanten, "
             "Geng and Andersen are 15-250 W lab reactors."]
    parts.append("## Notes\n\n" + "\n".join(notes) + "\n")
    parts.append("""## 6. Reading the tables (reviewer summary, for the narrative)

- Fired SMR needs 315-340 kJ of absorbed heat and ~575 kJ of fuel (HHV) per mol CH4 converted in the reformer
  (design studies); whole-plant H2 efficiency 76-81% HHV.
- With an industrial supply, the kW-scale plasma headline points cost (kJ electricity per mol CH4 converted):
  Hrycak ~310-390 (6.5 kW; steam generation excluded, ~25% carbon gap), Akande ~880-1000 (32 kW; lower confidence,
  impossible H2 rate), Song ~1080-1140 (22 kW) and Hrabovsky ~1200-1310 (120 kW, the only process-complete
  figure: the torch raises its own steam). Against fired SMR this is ~1-4x the absorbed heat and ~0.5-2.3x the
  fuel energy, but electricity against heat. Conversion 66-97% at these points; 94-99% costs ~1300-2400.
- Lab-scale points (paper boundary): Zhu 490 (Ni catalyst, steam excluded), Kaufmann 971 (1.4 kW; 574 at 0.5 kW and 42%), Kelly 581,
  Kwon 740, Wanten 813, Geng 1120-1490
  (furnace excluded), Andersen ~8100 kJ/mol (DBD).
- Joule heating converts at equilibrium (85-98%) and runs for 80-1535 h, but no paper gives power and feed at
  the same operating point. A reviewer estimate from the From 2024 pilot efficiencies (72-80%, ~23-35 kW) gives
  EC_CH4 ~390-485 kJ/mol at the supply output (SRC005-C004), below the kW-scale plasma torches.
- Durations: plasma results are minutes to hours (longest 6 h, Zhu); Joule pilots run for weeks.
""")
    (HERE / "reforming_synthesis_tables.md").write_text("\n".join(parts), encoding="utf-8")
    for r in rows:
        print(f"{r['key']:22s} {r['route']:5s} X {r['x_ch4']:>6s} EC {fmt(*r['ec']) if r['ec'] else 'NR':>9s} "
              f"ind. {fmt(*r['ec_est']) if r['ec_est'] else '-':>10s}")


if __name__ == "__main__":
    main()
