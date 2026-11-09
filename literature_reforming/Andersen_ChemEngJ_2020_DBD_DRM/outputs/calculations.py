"""Reviewer calculations SRC013-C001 to C005 for Andersen et al. (2020).

Feed: 25 Nml/min CH4 + 25 Nml/min CO2 (SRC013-E004). The authors convert ml to mol
with 24.46 L/mol (25 degC, 1 atm) in Eq. (7) (E009); this molar volume reproduces
their E (mmol/kJ) in Table 3 (C001), so it is used here. Results at 22.414 L/mol
(0 degC) are printed for comparison (about 9% lower EC).
Plasma power 45 W, discharge (oscilloscope) basis; no external heating (E002, E006).
Run with: python3 calculations.py
"""

VM_AUTH = 24.46      # L/mol, authors' Eq. (7) (E009)
VM_0C = 22.414
M_H2 = 2.016
LHV = {"H2": 241.8, "CO": 283.0, "CH4": 802.3}   # kJ/mol
HHV = {"H2": 285.8, "CO": 283.0, "CH4": 890.6}
EV = 96.485          # kJ/mol per eV/molecule
P = 0.045            # kW (E002)
DH_DRM, DH_C2 = 247.0, 65.9   # kJ/mol, authors' R1 and R2 (E009)

# Table 3 (E013-E017): X_CH4, X_CO2 (%), H2/CO, E (mmol/kJ), eta (%)
# Table S.2 (E019): S_H2 (H-based, % of 2*CH4 conv), S_CO (C-based, % of CH4+CO2 conv)
OPS = {
    "OP001 plasma only": (32.6, 22.4, 0.899, 0.206, 4.44, 30.6, 39.8),
    "OP002 Al2O3":       (27.2, 21.8, 0.879, 0.185, 4.16, 33.3, 41.0),
    "OP003 Ag/Al2O3":    (27.3, 21.4, 0.852, 0.183, 4.14, 32.5, 42.3),
    "OP004 Pt/Al2O3":    (32.5, 22.1, 0.840, 0.205, 4.39, 26.3, 36.7),
    "OP005 Cu/Al2O3":    (32.6, 16.1, 1.04, 0.185, 3.43, 25.6, 32.2),
}


def mol_s(nml_min, vm):
    return nml_min / 1000 / vm / 60


for vm in (VM_AUTH, VM_0C):
    f_ch4 = f_co2 = mol_s(25, vm)
    print(f"\n=== molar volume {vm} L/mol: F_CH4 = {f_ch4*60*1000:.3f} mmol/min ===")
    print(f"C002 SEI = {P/(2*f_ch4):.0f} kJ/mol total feed ({P*1000*60/50:.0f} J/ml, author 54); "
          f"SEI_CH4 = {P/f_ch4:.0f} kJ/mol")
    for op, (xch4, xco2, h2co, e_auth, eta_auth, s_h2, s_co) in OPS.items():
        c_ch4 = f_ch4 * xch4 / 100
        c_co2 = f_co2 * xco2 / 100
        # C001 author metrics
        e = (c_ch4 + c_co2) / P                      # mol/kJ
        sei_kj_mol = (P * 1000 * 60 / 50) * VM_AUTH  # authors: SEI 54 J/ml x 24.46 L/mol (Eq. 7)
        eta = (xco2 / 100 * DH_DRM + (xch4 - xco2) / 100 * DH_C2 / 2) / sei_kj_mol * 100
        # C002 EC_CH4 and per molecule converted
        ec_ch4 = P / c_ch4
        ec_mol = P / (c_ch4 + c_co2)
        # C003 products from selectivities (H2, CO only)
        h2 = s_h2 / 100 * 2 * c_ch4
        co = s_co / 100 * (c_ch4 + c_co2)
        eta_p = (h2 * LHV["H2"] + co * LHV["CO"]) / (P + c_ch4 * LHV["CH4"])
        # C004 partial eta_HHV (feed CH4 HHV; CO2 has no heating value)
        eta_hhv = (h2 * HHV["H2"] + co * HHV["CO"]) / (P + f_ch4 * HHV["CH4"])
        print(f"{op}: E={e*1000:.3f} mmol/kJ (author {e_auth}) eta={eta:.2f}% (author {eta_auth}) | "
              f"EC_CH4={ec_ch4:.0f} kJ/mol; per CH4+CO2 conv {ec_mol:.0f} kJ/mol = {ec_mol/EV:.1f} eV | "
              f"H2/CO={h2/co:.3f} (author {h2co}) EC_H2={P/h2:.0f} kJ/mol "
              f"EY_H2={h2*M_H2*3600/P:.2f} g/kWh eta_P,LHV={100*eta_p:.1f}% "
              f"eta_HHV(part.)={100*eta_hhv:.1f}% f_el={P/(P+f_ch4*HHV['CH4']):.2f}")

# C005 context: ratio of EC_CH4 to the DRM reaction enthalpy (authors' basis)
f_ch4 = mol_s(25, VM_AUTH)
print(f"\nC005 OP001 EC_CH4 / 247 kJ/mol = {P/(f_ch4*0.326)/DH_DRM:.0f}x; "
      f"plasma residence time in empty discharge volume 17.7 cm3 at 50 ml/min = {17.7/50*60:.0f} s")
