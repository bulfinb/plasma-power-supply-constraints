# Supply voltage and reactor compatibility

The required selection space is frequency, real output power, voltage, current, load impedance, duty cycle and matching-network capability. A frequency-power chart alone cannot establish usability.

## Voltage boundaries

Record mains AC input, internal DC link/beam supply, RF/AC output, and reactor electrode voltage separately. Keep RMS, peak, peak-to-peak and pulse quantities explicit. Transformer or resonant matching can change voltage and current; it does not create real power. Reactor electrode voltage can exceed generator terminal voltage with correspondingly changed impedance and component stress. At microwave frequencies, modal power and spatial electric field are more useful than a geometry-independent voltage.

`voltage_sources.csv` contains sourced output limits and explicit missing values for every original dataset. F1-F4 are specific models, not the maximum-power F family. Manufacturer maxima do not imply simultaneous achievable voltage, current, power and frequency.

## Linear sinusoidal load model

For RMS phasors, load admittance Y = G + jB:

- P = V_rms^2 G (real power)
- Q = -V_rms^2 B (reactive power; capacitive Q is negative)
- I_rms = V_rms sqrt(G^2+B^2)
- apparent power = V_rms I_rms
- load power factor = P / apparent power

This is load-side power factor, distinct from mains power factor. A resonance can compensate reactive demand at the generator while large currents/voltages remain within the resonant network.

For a homogeneous parallel-plate material (area A, gap d, negligible fringing), C = epsilon_0 epsilon_r' A/d. With dielectric loss tangent tan(delta) and conductivity sigma, counting each loss only once:

G = sigma A/d + 2 pi f C tan(delta)

P = V_rms^2 [sigma A/d + 2 pi f C tan(delta)].

For a pure dielectric-loss illustration (sigma=0), P=2 pi f C tan(delta) V_rms^2. At fixed C and tan(delta), the required voltage for fixed power decreases as f^(-1/2). Increasing frequency helps coupling at a given voltage but must be weighed against converter, matching and field-distribution losses. Real materials have frequency- and temperature-dependent properties; this is not a prediction for a catalyst bed.

Example assumption: C=10 nF and tan(delta)=0.1, with 100 kW real power per section. Required RMS voltage is approximately 126 kV at 1 kHz, 39.9 kV at 10 kHz, 12.6 kV at 100 kHz and 4.0 kV at 1 MHz. Reactive power magnitude is 1 MVAr; apparent power is approximately 1.005 MVA. These are calculated examples, not vendor ratings. If losses occur in a wall instead of the reacting material, that real power is not direct reaction-zone heating.

## Next reactor measurements / specifications

- Complex impedance or permittivity and conductivity versus frequency, temperature, composition and conversion, including startup.
- Electrode area and spacing, insulation thickness, geometry of conductive pathways and field concentrations.
- Required average power per independently supplied section; peak field, pulse width and repetition rate if pulsed.
- Allowed generator-side and reactor-side voltage/current, matching range, reactive component ratings and acceptable dissipation outside the reacting region.

Choose the lowest frequency that provides acceptable deposition and matching within these constraints, then compare total grid-to-reaction performance. Efficient low-kHz converters alone do not establish the optimum.

Physics reference: [COMSOL electromagnetic loss formulation](https://doc.comsol.com/6.3/doc/com.comsol.help.acdc/acdc_ug_modeling.06.24.html). Circuit and parallel-plate calculations above follow the stated linear model; inputs are assumptions. Commercial ratings are mapped in sources.md.
