"""Write human_check_worksheet.csv: one row per value in supply_values.csv, grouped by source,
in the order recommended in human_check_checklist.md. No data values in this script.

Priority of a value: 1 = cited in an efficiency range of supply_classes.csv (drives the wall-basis
EC_CH4); 2 = cited in a cost or lifetime entry of supply_classes.csv; 3 = other.
Sources are ordered by the highest priority among their values, then by ID, so each source is
opened once. Rerun after supply_values.csv changes (checked marks are not carried over).

Run from power_systems/: python3 scripts/make_check_worksheet.py
"""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent   # power_systems/results: data, scripts; figures/ below
values = list(csv.DictReader(open(ROOT / "supply_values.csv", encoding="utf-8")))
classes = list(csv.DictReader(open(ROOT / "supply_classes.csv", encoding="utf-8")))
register = {r["source_id"]: r for r in csv.DictReader(open(ROOT / "source_register.csv", encoding="utf-8"))}
values = [v for v in values if register.get(v["source_id"], {}).get("status") != "dropped"]   # dropped sources are not checked
classes = [c for c in classes if c["status"] != "dropped"]

used = {}  # value_id -> (priority, "class:field" list)
for c in classes:
    for field, prio in (("eta_value_ids", 1), ("cost_value_ids", 2), ("lifetime_value_ids", 2)):
        for vid in filter(None, (x.strip() for x in c[field].split(";"))):
            p, where = used.get(vid, (9, []))
            used[vid] = (min(p, prio), where + [f"{c['class_id']}:{field.split('_')[0]}"])

# Literature-folder papers held outside source_archive/
PAPER_COPY = {
    "PS003": "../literature_plasma_powersupply/LambertsVanAssche_JCOU_2022_DBD_TEA/manuscript_html_save_to_pdf.pdf",
    "PS004": "../literature_plasma_powersupply/Kaufmann_ApplSci_2023_PlasmaCO2_PtL_TEA/manuscript.pdf",
    "RV005": "../literature_reviews/OsorioTejada_EES_2024_Plasma_vs_Electrolysis_CO/manuscript.pdf",
    "SRC009": "../literature_reforming/Song_CAP_2020_Plasma_DRM/manuscript.pdf",
}


def copy_path(sid):
    if sid in PAPER_COPY:
        return PAPER_COPY[sid]
    r = register.get(sid)
    if not r or not r["local_copy"]:
        return "NO LOCAL COPY"
    return " | ".join(f"../source_archive/{sid}/{f.strip()}" for f in r["local_copy"].split("|"))


def flags(r):
    f = []
    n = (r["notes"] + " " + r["location"]).lower()
    if r["status"] == "unverified":
        f.append("SKIP: no local copy")
    if r["data_type"] == "reviewer_calc":
        f.append("recompute from notes")
    if "image" in n or "scan" in n or r["source_id"] == "PW055":
        f.append("read from page image")
    if r["data_type"] == "secondary":
        f.append("source quotes another source")
    if not r["value_low"]:
        f.append("qualitative (no value)")
    if r["source_id"] == "PW026":
        f.append("Table IV is an image")
    if r["source_id"] == "PW019":
        f.append("English and Spanish copies held")
    return "; ".join(f)


rows = []
for r in values:
    p, where = used.get(r["value_id"], (3, []))
    rows.append((p, r, where))
src_prio = {}
for p, r, _ in rows:
    src_prio[r["source_id"]] = min(p, src_prio.get(r["source_id"], 9))
rows.sort(key=lambda t: (src_prio[t[1]["source_id"]], t[1]["source_id"], t[1]["value_id"]))

out = ROOT.parent / "logs" / "human_check_worksheet.csv"
cols = ["order", "priority", "value_id", "source_id", "local_copy", "location", "quote", "value_as_extracted",
        "basis", "cost_scope", "supply_class", "data_type", "used_in_class_table", "flags", "checked", "finding_ids"]
with open(out, "w", encoding="utf-8", newline="") as fh:
    w = csv.writer(fh)
    w.writerow(cols)
    for i, (p, r, where) in enumerate(rows, 1):
        val = " ".join(x for x in (r["qualifier"], r["value_low"] if r["value_low"] == r["value_high"] else
                                   f"{r['value_low']}-{r['value_high']}", r["unit"]) if x)
        if r["currency"]:
            val += f" ({r['currency']}, {r['price_year']})"
        w.writerow([i, p, r["value_id"], r["source_id"], copy_path(r["source_id"]), r["location"], r["quote"], val,
                    r["basis"], r["cost_scope"], r["supply_class"], r["data_type"], " ".join(where), flags(r), "", ""])
print(f"wrote {out} ({len(rows)} values, {len(src_prio)} sources)")
for k in (1, 2, 3):
    print(f"  priority {k}: {sum(1 for p, _, _ in rows if p == k)} values")
