"""Reviewer calculations SRC008-C001 to C007 for Akande and Lee (2022), with corrigendum.

Inputs are from manuscript.pdf / erratum.pdf and carry the evidence IDs in evidence.csv.
Flows are given in "lpm" with no reference conditions; 0 degC, 1 atm is assumed
(25 degC sensitivity shown). Run with: python3 calculations.py
"""

V0, V25 = 22.414, 24.465          # L/mol at 0 and 25 degC, 1 atm
M_H2 = 2.016
LHV = {"H2": 241.8, "CO": 283.0, "CH4": 802.3}   # kJ/mol
HHV = {"H2": 285.8, "CO": 283.0, "CH4": 890.6}


def mol_s(lpm, vm=V0):
    return lpm / vm / 60


# ---------------------------------------------------------------- C001
# Stoichiometric ceiling on H2 production: CH4 + 2 H2O -> CO2 + 4 H2 (complete
# reforming plus shift) at the stated CH4 flow of 60 lpm (E012, E015).
for vm, label in ((V0, "0 degC"), (V25, "25 degC")):
    h2_max_g_h = 4 * mol_s(60, vm) * M_H2 * 3600
    print(f"C001 H2 ceiling at 60 lpm CH4 ({label}): {h2_max_g_h:.0f} g/h; "
          f"max EY at 32 kW = {h2_max_g_h/32:.1f} g/kWh")
print("     Author: 2247 g/h and 70 g/kWh at 32 kW (E016-E017) -> "
      f"{2247/(4*mol_s(60)*M_H2*3600):.2f} x the 0 degC ceiling")
print(f"     2247 g/h of H2 = {2247/M_H2*V0/60:.0f} lpm H2 at 0 degC "
      "(cf. 240-420 lpm total inlet flow, E011)")

# Internal consistency of Fig. 7 (H2 rate) with Fig. 8 (energy yield): H2 = EY x P
for p, ey, fig7 in ((27, 56, 1532), (32, 70, 2247), (37, 54, 2230), (42, 46, 2230)):
    print(f"     {p} kW: EY x P = {ey*p:.0f} g/h vs Fig. 7 ~{fig7} g/h")

# ---------------------------------------------------------------- C002
# Conversion implied by the corrigendum's "best" outlet composition (E019-E020):
# CH4 3.4, H2 63.4, CO 10.4, CO2 6.3, H2O 16.5 mol% at 62 lpm CH4, 180 lpm steam, 32 kW.
x = dict(CH4=3.4, H2=63.4, CO=10.4, CO2=6.3, H2O=16.5)
c_frac = (x["CH4"] + x["CO"] + x["CO2"]) / 100
X_c = 1 - x["CH4"] / (x["CH4"] + x["CO"] + x["CO2"])
F_out = 62 / c_frac                     # lpm, from carbon balance (no soot, E021)
out = {k: v / 100 * F_out for k, v in x.items()}
h_in, h_out = 4 * 62 + 2 * 180, 4 * out["CH4"] + 2 * out["H2"] + 2 * out["H2O"]
o_in, o_out = 180, out["CO"] + 2 * out["CO2"] + out["H2O"]
print(f"\nC002 X_CH4 from composition = {100*X_c:.1f}% ; outlet {F_out:.0f} lpm (carbon basis); "
      f"H closure {100*h_out/h_in:.0f}%, O closure {100*o_out/o_in:.0f}%; "
      f"sum of mole % = {sum(x.values()):.1f}")
h2_g_h = mol_s(out["H2"]) * M_H2 * 3600
print(f"     H2 = {out['H2']:.0f} lpm = {h2_g_h:.0f} g/h; EY_H2 = {h2_g_h/32:.1f} g/kWh; "
      f"EC_H2 = {32/mol_s(out['H2']):.0f} kJ/mol (absorbed MW, steam heat excluded)")
f_conv8 = mol_s(62) * X_c
eta_lhv = (mol_s(out["H2"]) * LHV["H2"] + mol_s(out["CO"]) * LHV["CO"]) / (32 + f_conv8 * LHV["CH4"])
print(f"     EC_CH4 = {32/f_conv8:.0f} kJ/mol; eta_P,LHV = {100*eta_lhv:.1f}% (absorbed MW basis)")

# ---------------------------------------------------------------- C003
# Conversion implied by Fig. 10 outlet mole fractions (E022), assuming 3-4 mol H2
# per mol CH4 converted (SMR to CO / full shift) and no other H2 source.
print("\nC003 X_CH4 implied by Fig. 10 (y_CH4, y_H2) vs author Fig. 6/9 values")
for p, y_ch4, y_h2, author in ((27, 0.26, 0.45, 85.7), (32, 0.14, 0.63, 96.6),
                               (37, 0.09, 0.58, 97.3), (42, 0.02, 0.58, None)):
    rng = []
    for n in (3, 4):
        r = y_ch4 / (y_h2 / n)            # CH4 out per CH4 converted
        rng.append(100 / (1 + r))
    print(f"     {p} kW: implied X_CH4 {rng[0]:.0f}-{rng[1]:.0f}% ; author {author}")

# ---------------------------------------------------------------- C004
# Power-basis EC_CH4 and SEI_CH4 from author conversions (absorbed microwave power;
# steam-generator heat excluded, not reported). CH4 60 lpm.
print("\nC004 power basis (absorbed microwave power; external steam heat excluded)")
pts = [("OP001", 17, 60, 74.6), ("OP002", 27, 60, 85.7), ("OP003", 32, 60, 96.6),
       ("OP004", 37, 60, 97.3), ("OP006", 47, 60, 97.7), ("OP007", 32, 60, 99.8)]
for op, p, ch4, X in pts:
    f_in = mol_s(ch4)
    print(f"     {op}: P={p} kW SEI_CH4={p/f_in:.0f} EC_CH4={p/(f_in*X/100):.0f} kJ/mol "
          f"({p/(mol_s(ch4, V25)*X/100):.0f} at 25 degC)")

# ---------------------------------------------------------------- C005
# Indicative steam-raising duty (NOT reported): 180 lpm steam from liquid at 25 degC
# to saturated vapour at 100 degC (cp,liq 75.3 J/mol K; dHvap 40.65 kJ/mol). Bounds:
# lpm referenced to 0 degC, or to actual steam at ~120 degC (32.3 L/mol).
dh = 75.3e-3 * 75 + 40.65
for vm, lab in ((V0, "0 degC normal"), (32.3, "actual ~120 degC")):
    q = mol_s(180, vm) * dh
    ec = (32 + q) / (mol_s(60) * 0.966)
    print(f"C005 steam duty ({lab} basis): {q:.1f} kW = {100*q/32:.0f}% of 32 kW; "
          f"OP003 EC_CH4 incl. this heat ~{ec:.0f} kJ/mol (indicative only)")
    # added 2026-11-27: same duty at the adopted headline OP008 (62 lpm CH4, carbon-based X 83.1%)
    ec8 = (32 + q) / (mol_s(62) * 0.831)
    print(f"C005 ({lab} basis): OP008 EC_CH4 incl. this heat ~{ec8:.0f} kJ/mol (indicative only)")

# ---------------------------------------------------------------- C006
# Partial eta_HHV at OP008 (composition-derived flows; absorbed MW + CH4 HHV;
# steam generation, generator losses and auxiliaries excluded)
d = 32 + mol_s(62) * HHV["CH4"]
eta_hhv = (mol_s(out["H2"]) * HHV["H2"] + mol_s(out["CO"]) * HHV["CO"]) / d
print(f"\nC006 OP008 eta_HHV (partial) = {100*eta_hhv:.1f}%; f_electric = {32/d:.2f}")

# ---------------------------------------------------------------- C007
# Reformer volume and space time at 32 kW, S/C 3 (0.28 m ID x 2.27 m, E009)
import math
v = math.pi / 4 * 0.28**2 * 2.27
print(f"C007 reformer volume {1000*v:.0f} L; nominal space time at 240 lpm (0 degC) "
      f"{v*1000/240*60:.0f} s (inlet basis, not at reactor temperature)")
