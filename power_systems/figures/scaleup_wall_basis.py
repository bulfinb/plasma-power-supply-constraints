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

# Classes without sourced efficiency values use an analogue class for eta (reviewer judgement,
# stated in supply_classes.csv range_basis). Written to the output as eta_basis.
ANALOGUE = {}  # e.g. {"D1": "K1"} before D1 had sourced values (2026-11-11)
# Frequency-specific scenario: (eta_low, eta_high, supporting value IDs).
SUBBAND = {
    # K2 at 400 kHz: the 91% endpoint (PW004-V02, family rated 1-200 kHz)
    # is extrapolated to 400 kHz; >96% is a 100-400 kHz claim (PW005-V02).
    # PW005-V01 is a 100 kW INPUT rating; PW006-V01 documents 50 kW OUTPUT.
    "K2@400kHz": (0.91, 0.96, "PW004-V02; PW005-V02"),
}

# Literature EC_CH4 ranges (kJ/mol CH4 converted) from literature_reforming/*/short_summary.txt, table 4
LIT = [
    # source, route, paper power boundary, EC low, EC high, supply class id
    ("Hrabovsky 2018 (SRC007)", "SMR/DRM", "arc power", 1149, 2172, "A1"),
    ("Song 2020 (SRC009)", "DRM", "RF generator output", 1036, 1510, "R1"),   # sensitivity: RF tube oscillator
    ("Song 2020 (SRC009)", "DRM", "RF generator output", 1036, 1510, "K2@400kHz"),
    ("Akande 2022 (SRC008)", "SMR", "absorbed MW", 511, 1078, "M1"),
    ("Hrycak 2023 (SRC010)", "mixed", "absorbed MW (lower bounds)", 258, 509, "M1"),  # revised 2026-11-20 (Vm 24.25, XR008)
    ("Kelly 2023 (SRC011)", "DRM", "absorbed MW", 581, 723, "M2"),
    ("Kwon 2023 (SRC014)", "DRM", "discharge", 740, 948, "K1"),
    ("Zhu 2019 (SRC012)", "SMR", "discharge (steam excl., lab ballast excl.)", 490, 679, "D1"),
    ("Geng 2022 (SRC002)", "SMR", "discharge (furnace excl.)", 1120, 1490, "K1"),
    ("Wanten 2022 (SRC015)", "DRM", "plasma (300 kOhm lab ballast excl.)", 813, 1194, "D1"),
    ("Andersen 2020 (SRC013)", "DRM", "discharge", 8103, 9712, "K1"),
]

rows = []
for src, route, boundary, lo, hi, sid in LIT:
    if sid in SUBBAND:
        cls = sid.split("@")[0]
        e_lo, e_hi, ids = SUBBAND[sid]
        basis = (f"{cls} scenario at {sid.split('@')[1]} ({ids}); "
                 "0.91 extrapolated from 1-200 kHz; >0.96 claim at 100-400 kHz")
    else:
        cls = sid
        src_cls = ANALOGUE.get(sid, sid)
        e_lo, e_hi = float(sup[src_cls]["eta_low"]), float(sup[src_cls]["eta_high"])
        basis = f"analogue: {src_cls} range ({sid} has no sourced efficiency)" if src_cls != sid else f"{sid} class range"
    w_lo, w_hi = lo / e_hi, hi / e_lo
    rows.append([src, route, boundary, lo, hi, cls, sup[cls]["representative_supply"], e_lo, e_hi, basis,
                 round(w_lo), round(w_hi)])
    print(f"{src:24s} {sid:9s} eta {e_lo:.2f}-{e_hi:.2f}: EC_CH4 {lo}-{hi} -> wall {w_lo:.0f}-{w_hi:.0f} kJ/mol")

out = ROOT / "figures" / "scaleup_wall_basis.csv"
with out.open("w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["source", "route", "paper_power_boundary", "EC_CH4_low", "EC_CH4_high", "supply_id",
                "representative_supply", "eta_low", "eta_high", "eta_basis", "EC_CH4_wall_low", "EC_CH4_wall_high"])
    w.writerows(rows)
print(f"wrote {out}")
