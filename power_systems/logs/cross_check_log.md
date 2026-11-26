# Cross-check against an independent GPT extraction (power supplies)

A second AI (OpenAI GPT-6.1 Sol, Codex desktop app) re-extracted the 42 sources cited in supply_classes.csv, blind, in a separate local folder that is not published.

What it had:
- the archived local copies, with SHA-256 hashes;
- workflow.md section 4;
- the class codes (names only, no ranges);
- PW058 as the only worked example.

What it did not have: our supply_values.csv, supply_classes.csv, the notes or the figures.

GPT extracts every in-scope value, so it has many more rows than we do. We extracted only the values we use. The comparison therefore asks two questions:
1. Do the values we use agree?
2. Does GPT find anything that would change a class value?

Each difference that matters gets a row. Every difference is checked against the archived copy.

Action:
- **corrected:** our row is revised; see processing_log.md;
- **kept ours**;
- **for decision:** BB to decide, usually about a class range;
- **for human check:** not settled by the source.

These checks are AI-to-AI and are not logged in ../human_checks/. IDs use the prefix XP.

## Independent extraction

| Sources | Date | Tool | Model | Workflow | Rows |
|---|---|---|---|---|---|
| PW001-PW009, PW011 (batch 1) | 2026-11-20 | Codex desktop (version not recorded) | GPT-6.1 Sol | 0.1, section 4 | 192 (ours: 29 for these sources) |
| PW012-PW054, 32 sources (batch 2) | 2026-11-20 | Codex desktop (CLI 0.169.1) | GPT-6.1 Sol | 0.1, section 4 (GPT added waveform-basis quantity codes in its copy, 0.2) | 1082 (ours: 89 for these sources) |

## Summary by source (batch 1)

- **PW001 ABP Induction:** agrees. 16 MW at 250 Hz (Twin-Power), 42 MW per crucible and 126 MW installed at Tisco. GPT adds furnace energy use and plant capacities, which are not used.
- **PW002 SMS Elotherm:** our two family ranges agree (LLC 400-4000 kW at 1-10 kHz; series resonant 90-2400 kW to 200 kHz). GPT also finds the family headline "up to 600 kHz and up to 4500 kW" and the parallel-resonant range of 120-4500 kW. See XP001.
- **PW003 Meltech:** agrees (75-750 kW, ~98%).
- **PW004 TRUMPF TruHeat MF:** agrees. 91% overall efficiency (generator), 240 kW, 278 kVA, ≤1200 V, ≤1120 A. GPT tabulates all eight models and flags one table row (MF 7080) where the source appears to swap the efficiency and temperature cells. Our 91% is the series value and is not affected.
- **PW005 CEIA Power Cube:** agrees (≤100 kW input, >96%). GPT also records the reactive tank ratings (kVAR) and notes that the page calls the same sizes "output" in the text and "max input" in the table. Our row already uses input and notes the ambiguity (PW006).
- **PW006 CEIA news:** agrees (50 kW). Ours keeps the basis as not stated; GPT has rated output.
- **PW007 TRUMPF TruHeat HF:** agrees (100 kW, 210 kVA, power factor 0.9). GPT adds the other models (10-120 kW) and the family range of 10-500 kW. Every model gives the same 0.53 when output is divided by kVA x PF, which supports our calculated R1 value (PW007-V03).
- **PW008 Comet Synertia:** agrees (5 kW, >70%, 13.56-60 MHz). GPT lists each model at its own frequency.
- **PW009 Microwave Techniques MTX100:** agrees (100 kW, "approaching 80%", generator). GPT adds four values: a 902-928 MHz band, 30-100 kW, magnetron tube losses of 15-18%, and a maximum input of 150 kVA at 100 kW output. See XP002.
- **PW011 QST gyrotron:** agrees (1 MW, 50.6%). Ours labels the efficiency basis "device" (gyrotron); GPT has not stated. GPT adds transmission-line efficiencies, which are not used (H1 is context only).

## Summary (batch 2)

Every value we use agrees with GPT's, apart from unit formats:
- USD/W vs USD/kW;
- kEUR/kW vs EUR/kW;
- years vs hours;
- VA vs kVA.

Our reviewer calculations, which GPT does not make, are consistent with its component values:
- PW050-V05 (0.63-0.70);
- PW051-V05 (175-180 kW);
- PW053-V03 (0.946);
- PW022 total cost per kVA. GPT has the same totals, 85.2 / 88.2 / 158.2 / 153.6 EUR/kVA.

Basis labels differ in places (e.g. generator vs device, into_load vs system), with the same values.

GPT omitted three values that we hold, all confirmed in the archived copies, so we keep ours:
- PW034-V03 PyroGenesis 50-500 kW gross;
- PW035-V02 CACT 60 and 200 kW;
- PW050-V06 magnetron >15,000 h.

GPT also extracted all klystron tube data in PW014 (H1, context) and every catalogue model in PW054. These are not needed.

## Differences

| ID | Date | Source / record | Ours | GPT | Checked against source | Action |
|---|---|---|---|---|---|---|
| XP001 | 2026-11-20 | PW002 largest unit | K2 unit power from PW002-V01 (LLC to 4000 kW) | family "up to 4500 kW" and "up to 600 kHz"; parallel-resonant converters 120-4500 kW | confirmed in the archived page ("Converter systems with frequencies up to 600 kHz and performance up to 4500 kW") | applied (BB, 2026-11-20): PW002-V03 added; K2 unit scale 4.5 MW, band to 600 kHz |
| XP002 | 2026-11-20 | PW009 MTX100 efficiency basis | 0.80 "approaching", generator (the M1 class value) | also "150 kVA Max. at 100 kW Output" (100/150 = 0.67 at power factor 1) and tube losses of 15-18%; GPT notes not to derive efficiency from kVA | confirmed. The same kVA method gives our M2 (0.63-0.70, PW050) and R1 (0.53, PW007) values, but M1 uses the vendor claim. M1 by the kVA method would be ~0.67-0.74, close to M2 | applied (BB, 2026-11-20): both classes now use generator = HV supply x tube. M1 0.80 -> 0.74-0.84; M2 0.63-0.70 -> 0.63-0.72 (upper = Kiefer measured, SRC016-V01). New rows PW009-V03, PW045-V04, PW031-V04, SRC016-V01 |
| XP003 | 2026-11-20 | J1 lifetime | none in supply_classes.csv | PW022: rectifier lifetimes "exceeding even 30 years" (thyristor experience) and 20-30 years design life for IGBT | confirmed (PW022 PDF p. 31) | applied (BB, 2026-11-20): PW022-V05, -V06 added; J1 lifetime set |
| XP004 | 2026-11-20 | A1 lifetime text | "torch electrodes >1000 h" | same quote also gives "600 hours for the main anode" | confirmed: our PW034-V02 quote contains both | applied (BB, 2026-11-20): A1 lifetime text revised |
| XP005 | 2026-11-20 | R1 upper bound 0.60 | 1 - 40% loss "in the oscillator and tank circuit" (PW024) | same quote; GPT labels it the oscillator/tank stage, not the whole generator | the HV DC supply feeding the tube is outside the 40%, so 0.60 is an upper bound | applied (BB, 2026-11-20): note added to R1 range_basis |

## Closing summary (power supplies, 2026-11-20)

- **Scope:** all 42 class-cited sources were re-extracted by GPT-6.1 Sol: 1274 rows, against our 118 for these sources.
- **Agreement:** every value we use agrees, apart from unit formats. GPT missed three of our values, all confirmed in the archived copies.
- **Corrections to existing values:** none.
- **Changes from GPT's findings (applied on BB's decision):**
  - one added value: K2 to 4.5 MW (XP001);
  - one change of method for the magnetron classes: M1 0.74-0.84, M2 0.63-0.72 (XP002);
  - two lifetime additions or corrections (J1, A1; XP003-XP004);
  - one clarification (R1; XP005).
- **Downstream:** supply_values.csv, supply_classes.csv, the scale-up note, the supply figures, the wall-basis table and both syntheses and their figures were regenerated. No conclusion changes; the 915 MHz industrial-supply estimates now carry a ~+/-6% band.
- **Status:** values remain ai_checked; human verification is still pending.
