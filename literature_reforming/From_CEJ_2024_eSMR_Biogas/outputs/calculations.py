"""Reviewer calculations SRC005-C001 to C002 for From et al. (2024), eSMR pilot plant.

Inputs are taken from the manuscript and labelled with evidence IDs in evidence.csv.
Run with: python3 calculations.py
"""
import math

# SRC005-C001: graph reading of Fig. 5 (manuscript.pdf p. 7), experimental points.
# Page rendered at 300 dpi (pdftoppm -r 300), top 45% cropped and viewed at 2000 px width.
# Pixel coordinates below refer to that view; values are approximate.
X_PX_0P01, X_PX_PER_DECADE = 320, 451    # x axis: 0.01 MW at 320 px, 0.1 MW at 771 px (log scale)
Y_PX_40, Y_PX_PER_PERCENT = 908, 11.85   # left y axis: 40% at 908 px, 100% at 197 px
POINTS_PX = {"OP004": (487, 535), "OP005": (513, 506), "OP006": (541, 465), "OP007": (564, 440)}  # E019-E022

for op, (x_px, y_px) in POINTS_PX.items():
    capacity = 0.01 * 10 ** ((x_px - X_PX_0P01) / X_PX_PER_DECADE)
    efficiency = 40 + (Y_PX_40 - y_px) / Y_PX_PER_PERCENT
    print("C001 %s: capacity axis %.4f MW; author efficiency %.1f%%" % (op, capacity, efficiency))
print("     author text: 72-80% (E023); capacity axis undefined (E024)")

# SRC005-C002: methane feed range for the energy-test flows.
# Biogas flows 15-27 Nm3/h (E018); CH4 50-75 mol% is the general raw-biogas range (E010).
# Normal reference assumed 0 degC, 1 atm (not stated in the paper).
NM3_PER_KMOL = 22.414
for biogas_nm3_h in (15, 27):
    low, high = (biogas_nm3_h * y / NM3_PER_KMOL * 1000 / 60 for y in (0.50, 0.75))
    print("C002 %d Nm3/h biogas: CH4 feed %.1f-%.1f mol/min" % (biogas_nm3_h, low, high))

# SRC005-C003: EC_CH4 not calculated. Point-matched Q_in, CH4 feed, biogas composition and
# conversion are not reported for the Fig. 5 points (E018, E024, E042).
