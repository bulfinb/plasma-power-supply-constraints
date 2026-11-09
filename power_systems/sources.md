# Power generation evidence register

> Source provenance: every web and manufacturer source cited here is listed in [source_register.csv](source_register.csv) with access date, SHA-256 of the local copy (kept in `source_archive/`, not distributed) and a Wayback Machine snapshot (made 2026-11-09). Sources still to retrieve: [BB_search.txt](BB_search.txt).

## Voltage audit update

`voltage_sources.csv` records published RMS output limits separately from input and beam voltages. S4 model table gives D: 240 kW, 1200 V RMS maximum, 1120 A RMS maximum and 1-200 kHz; the earlier 0.5 kHz family headline has been replaced with this model-specific lower bound. S7 gives F1 (HF7100): 100 kW / 6600 V RMS; F2 (HF7030): 30 kW / 6300 V RMS; F3 (HF7060): 60 kW / 6300 V RMS; F4 (HF7010): 10 kW / 5000 V RMS; all nominally 400-3000 kHz. Do not assign these voltages to the 500 kW family rating.

S16: [CEIA detailed SA400 specifications](https://induction.ceia.net/it-IO/product/power-cube-sa-400-series) identify 50 kW as maximum input power and separately give inductor reactive kVAR ratings. E is now marked input_rating and omitted from output-power plots and scaling counts; its family efficiency claim remains in the efficiency panel. Earlier table descriptions must be read with this correction. Manufacturer tables make voltage/current/power distinctions essential.

No arbitrary voltage has been assigned to microwave sources or missing converter specifications. Beam voltages from S13 are internal DC, not load RF voltages. The additional voltage figure has a sourced ratings panel and a separate explicitly assumed dielectric-load calculation, documented in reactor_matching.md.

Research date: 8 September 2026. Public manufacturer pages and primary technical reports. A product page is evidence of a published offering, not confirmation of delivery availability or a performance guarantee. This is a selected evidence map, not a comprehensive market maximum survey.

| Source | Dataset points | Primary source and extracted evidence |
|---|---|---|
| S1 | A; aggregate context | [ABP: Inductive melting in steelworks (2015)](https://abpinduction.com/wp-content/uploads/2020/02/ABP-Inductive_melting_in_steelworks_M._Chaabet_E._Doetsch.pdf), PDF page 3: 16 MW / 250 Hz Twin-Power supply. Page 5: three operating 42 MW supplies, 126 MW installed; exact frequency of those supplies is not specified. |
| S2 | B | [SMS Elotherm converters](https://www.sms-elotherm.com/en/service/retrofit/converters): LLC family 1-10 kHz, 400-4000 kW. No numeric efficiency. Wider 1-600 kHz / 120-4500 kW family is deliberately not plotted as a paired maximum. |
| S3 | C | [Meltech Pulsar IGBT](https://www.induction-furnaces.com/new-furnaces/pulsar-igbt-inverter-technology/): 75-750 kW, 200-10000 Hz; around 98% operating efficiency. Not a measured efficiency curve. |
| S4 | D | [TRUMPF TruHeat MF 7000 G2](https://www.trumpf.com/en_US/products/power-electronics/generators-for-industrial-heating/truheat-mf/truheat-mf-serie-7000-g2/): 7240 rated 240 kW, nominal 0.5-200 kHz, overall efficiency 91%. No guarantee of identical power and efficiency throughout the frequency range. |
| S5 | E | [CEIA SA/400 family](https://induction.ceia.net/en-IT/product/power-cube-sa-400-series): efficiency above 96% under a range of load conditions. Exact metering boundary not supplied. |
| S6 | E | [CEIA 50 kW SA/400 announcement](https://induction.ceia.net/es-EC/about-us/news/48): 12.5, 25 and 50 kW versions; 100-400 kHz working band. Selected 50 kW offering, not asserted to be the current family maximum. |
| S7 | F | [TRUMPF TruHeat HF 7000](https://www.trumpf.com/de_DE/produkte/leistungselektronik/generatoren-zur-industriellen-erwaermung/truheat-hf/truheat-hf-serie-7000/): tube technology, headline 10-500 kW family and 400-3000 kHz. Table includes smaller models. No numeric efficiency is given. |
| S8 | G, H | [Comet Synertia RF generators](https://pct.comet.tech/en/products/synertia_rf_power_delivery_platform/synertia_rf_generator): 5 kW at 13.56 and 27.12 MHz; family power efficiency above 70%. Lower bound, not an observation of exactly 70%. |
| S9 | I | [Microwave Techniques MTX100](https://www.microwavetechniques.com/industrial-microwave-generators/100-kw-mtx/): 100 kW at 915 MHz, operation approaching 80% efficiency. Magnetron losses separately described as 15-18%. |
| S10 | J | [SAIREM microwave plasma guide](https://www.sairem.com/wp-content/uploads/2021/01/SAIREM-MW-technology-guide-for-lab-grown-diamonds-applications.pdf), printed page 7: GMP100, 10 kW, 2450 MHz, 85% power efficiency. Confirm measurement boundary before comparing contractually with other vendors. |
| S11 | K (separate panel) | [QST primary report at IAEA FEC 2020/2021](https://conferences.iaea.org/event/214/contributions/17030/): second ITER gyrotron 1.05 MW, 50.6% total gyrotron efficiency, 300 s long-pulse test at 170 GHz. Not a continuous chemical-plant installation or grid-to-output efficiency. |
| S12 | Scaling context only | [SAIREM EvoMag 915](https://www.sairem.com/microwave-radiofrequency-equipment/industrial-generators/evomag-915-mhz-magnetron-generator/): up to 100 kW per generator, >80% efficiency; container solutions combine sources into several MW. No 100 MW installation established here. |

## Interpretation and exclusions

### Higher-frequency and pulsed additions

| Source | Points | Primary source and extracted evidence |
|---|---|---|
| S13 | L, M, N | [Canon commercial klystron lineup](https://etd.canon/en/product/category/microwave/klystron.html) and [April 2025 catalogue](https://etd.canon/en/download/files/microwave_tube_catalog_EN.pdf), PDF page 4: E37705 325 MHz / 600 kW CW / 60%; E3732 508.6 or 508.9 MHz / 1200 kW CW / 63%; E3718 1250 MHz / 1200 kW CW / 63%. These are tube ratings, not complete AC-powered generator efficiencies. Models marked under development are not included. |
| S14 | O | [CPI VPS3499 transmitter datasheet](https://www.cpi-edb.com/docs/datasheets/163/VPS3499%20KLYSTRON%20TRANS%20%20NF%20FINAL%2012-19-24.pdf), page 3: 2.7-3.0 GHz, 1 MW peak, RF duty 0.002, 0.4-5 microsecond pulses. Average RF power calculated as 2 kW. The apparent PRF unit inconsistency in the datasheet is not used. |
| S15 | P | [CPI authors at 2024 accelerator applications meeting](https://indico.jlab.org/event/722/contributions/13920/): existing XL4/XL5 devices approximately 40% efficient, 50 MW peak, 18-20 kW average. A representative 12 GHz point is plotted for this reported class; not an exact specification of both models at that frequency. Proposed improved efficiencies are excluded. |

`high_frequency_sources.csv` adds commercial tubes and pulsed transmitters. The scale graph explicitly distinguishes complete supplies from specialist tubes and research results. Pulsed peak markers are connected to average markers at the same frequency; they are not additional continuous capacity. Rectangular-pulse approximation: average = peak × pulse width × repetition rate; use the waveform energy integral for arbitrary pulse shapes. Carrier frequency, pulse repetition frequency, and inverter switching frequency are distinct.

The added CW klystrons demonstrate commercially listed MW output in the MHz/GHz region. Thus a strict universal decrease in available output with frequency is not supported. Their quoted 60-63% tube efficiencies incur upstream supply and auxiliary losses in addition. A 100 MW continuous target would arithmetically need at least 84 of the 1.2 MW tubes, or 1000 of the 100 kW microwave generators, before redundancy and delivery losses. A 50 MW peak / 20 kW average pulsed source would need 5000 units on an average-power basis, not two.

- Horizontal segments represent quoted operating/product-family frequency bands. They are not sampled efficiency curves, uncertainty intervals, or proof of maximum power across the whole band. No regression or interpolated technology envelope is fitted.
- A/B/C/E/F are supply or family ratings, not counts of internal power modules. A is an installed supply; other industrial entries are product offerings. K is separately marked research evidence.
- Quoted efficiency values use different vendor definitions. Arrows mark lower bounds (>), and approximate language is preserved. Missing efficiencies remain missing. None of these observations establishes total grid-to-reaction efficiency.
- Do not calculate efficiency simply as kW/kVA. Apparent-power ratings may be sizing limits, and even multiplying by nameplate power factor may not give actual input at the output operating point.
- The 126 MW ABP installation is excluded from frequency coordinates because its exact output frequency is unavailable. It is evidence of aggregate scale, not a single 126 MW source.
- A SAIREM 120 kW 13.56/27.12 MHz catalogue appeared in the search index, but its direct URL returned 404. It is not used in the figures. This also warns against treating the 5 kW Comet examples as an RF market ceiling.
- The survey supports investigating a low-kHz power architecture, but cannot establish a universal monotonic decrease of efficiency or power with frequency. CEIA's >96% claim at 100-400 kHz and high-power gyrotrons are important counterexamples to overly broad statements.
- Application, topology, duty cycle, load impedance, voltage and cooling confound cross-vendor comparisons. Supplier frequency-resolved full-load and part-load curves are needed for a quantitative optimum.

## Reproduction

The project environment is `.venv`, created from a local Python 3.14 installation with `--system-site-packages` to reuse the user's installed matplotlib. From the project root run `power_systems\.venv\Scripts\python.exe power_systems\plot_power_systems.py`. No activation is required. The script reads adjacent CSV files and writes PNG/SVG figures and a calculated 100 MW scaling table into `figures/`. Each plotted label contains its dataset ID, linked above to its source. For a different installation, install `requirements.txt`. The earlier `.python_packages` directory is not used.

The 100 MW calculations mean electrical/RF output before matching and reactor losses. Unit counts are arithmetic only, with no redundancy; family maximum ratings require vendor confirmation. Efficiency scenarios are illustrative and are not assigned to a particular device.
