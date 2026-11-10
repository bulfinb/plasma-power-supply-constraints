"""Indicative wall-basis EC_CH4 for the review sources with representative
industrial supplies (../supply_classes.csv). Not the authors' lab supplies.

EC_wall = EC_reported_basis / eta_supply, where eta_supply covers only the stages
between the wall and the power boundary used in each paper (see notes/scaleup_assessment.md).
Run from power_systems/: python3 figures/scaleup_wall_basis.py   (writes figures/scaleup_wall_basis.csv)
"""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sup = {r["class_id"]: r for r in csv.DictReader(open(ROOT / "supply_classes.csv", encoding="utf-8"))}

# Literature EC_CH4 ranges (kJ/mol CH4 converted) from literature_reforming/*/short_summary.txt, table 4
LIT = [
    # source, route, paper power boundary, EC low, EC high, supply class id
    ("Hrabovsky 2018 (SRC007)", "SMR/DRM", "arc power", 1149, 2172, "A1"),
    ("Song 2020 (SRC009)", "DRM", "RF generator output", 1036, 1510, "R1"),
    ("Song 2020 (SRC009)", "DRM", "RF generator output", 1036, 1510, "R2"),
    ("Akande 2022 (SRC008)", "SMR", "absorbed MW", 511, 1078, "M1"),
    ("Hrycak 2023 (SRC010)", "mixed", "absorbed MW (lower bounds)", 238, 471, "M1"),
    ("Kelly 2023 (SRC011)", "DRM", "absorbed MW", 581, 723, "M2"),
    ("Kelly 2023 (SRC011)", "DRM", "absorbed MW", 581, 723, "M3"),
    ("Kwon 2023 (SRC014)", "DRM", "discharge", 740, 948, "K1"),
    ("Zhu 2019 (SRC012)", "SMR", "discharge (steam excl.)", 490, 679, "K1"),
    ("Geng 2022 (SRC002)", "SMR", "discharge (furnace excl.)", 1120, 1490, "K1"),
    ("Wanten 2022 (SRC015)", "DRM", "plasma (300 kOhm lab ballast excl.)", 813, 1194, "A1"),
    ("Andersen 2020 (SRC013)", "DRM", "discharge", 8103, 9712, "K1"),
]

rows = []
for src, route, boundary, lo, hi, sid in LIT:
    s = sup[sid]
    e_lo, e_hi = float(s["eta_low"]), float(s["eta_high"])
    w_lo, w_hi = lo / e_hi, hi / e_lo
    rows.append([src, route, boundary, lo, hi, sid, s["representative_supply"], e_lo, e_hi,
                 round(w_lo), round(w_hi)])
    print(f"{src:24s} {sid:3s} eta {e_lo:.2f}-{e_hi:.2f}: EC_CH4 {lo}-{hi} -> wall {w_lo:.0f}-{w_hi:.0f} kJ/mol")

# Joule benchmark (vendor claim, per mol H2): 1 kWh/Nm3 H2 at 0 degC
print(f"\nJ2 Topsoe eREACT claim: {3600/(1000/22.414):.0f} kJ/mol H2 (system electricity, vendor claim)")

out = ROOT / "figures" / "scaleup_wall_basis.csv"
with out.open("w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["source", "route", "paper_power_boundary", "EC_CH4_low", "EC_CH4_high", "supply_id",
                "representative_supply", "eta_low", "eta_high", "EC_CH4_wall_low", "EC_CH4_wall_high"])
    w.writerows(rows)
print(f"wrote {out}")
