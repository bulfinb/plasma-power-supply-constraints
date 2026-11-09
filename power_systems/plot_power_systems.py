"""Plot traceable published ratings, not a fitted frequency-performance law.

Run: python plot_power_systems.py
Input provenance: power_sources.csv and sources.md next to this script.
"""
from pathlib import Path
import csv
import math

ROOT = Path(__file__).resolve().parent
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

OUT = ROOT / 'figures'
OUT.mkdir(exist_ok=True)
with (ROOT / 'power_sources.csv').open(encoding='utf-8', newline='') as f:
    rows = list(csv.DictReader(f))
for r in rows:
    for k in ['frequency_min_hz', 'frequency_max_hz', 'power_kw']:
        r[k] = float(r[k])
    r['efficiency_percent'] = float(r['efficiency_percent']) if r['efficiency_percent'] else None
    assert 0 < r['frequency_min_hz'] <= r['frequency_max_hz']
    assert r['source_ids'] and r['power_kw'] > 0
    assert r['efficiency_percent'] is None or 0 < r['efficiency_percent'] <= 100

plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 10,
                     'axes.spines.top': False, 'axes.spines.right': False,
                     'svg.fonttype': 'none', 'savefig.facecolor': 'white'})
COLORS = {'Induction': '#176d8a', 'Induction tube': '#7351a1',
          'RF solid state': '#ba6024', 'Microwave magnetron': '#28835e',
          'Fusion gyrotron': '#6d6d6d'}

def save(fig, name):
    for ext in ['png', 'svg']:
        fig.savefig(OUT / f'{name}.{ext}', dpi=190, bbox_inches='tight')
    plt.close(fig)

def setup_frequency(ax):
    ax.set_xscale('log')
    ax.set_xlim(100, 1e10)
    ax.set_xticks([1e2, 1e3, 1e4, 1e5, 1e6, 1e7, 1e8, 1e9, 1e10],
                 ['100 Hz', '1 kHz', '10 kHz', '100 kHz', '1 MHz', '10 MHz', '100 MHz', '1 GHz', '10 GHz'])
    ax.grid(axis='both', which='major', alpha=.18)
    ax.set_xlabel('Output frequency (log scale)')

def band(ax, r, y, marker='o'):
    a, b = r['frequency_min_hz'], r['frequency_max_hz']
    color = COLORS[r['technology']]
    if a != b:
        ax.plot([a, b], [y, y], color=color, linewidth=2, marker='|', markersize=9)
    x = math.sqrt(a*b)
    ax.plot(x, y, marker=marker, color=color, markersize=7,
            markerfacecolor='white' if r['efficiency_qualifier'] == 'greater_than' else color)
    return x

industrial = [r for r in rows if r['scope'] != 'research']
fig, (ax, eff) = plt.subplots(2, 1, figsize=(13, 10))
fig.subplots_adjust(hspace=.40, top=.89, bottom=.18)
fig.suptitle('Power-source frequency: published industrial evidence', fontsize=18, x=.125, ha='left')
fig.text(.125, .935, 'Selected offerings and installed supplies | source IDs in brackets | researched 8 September 2026', color='#555555')
setup_frequency(ax)
ax.set_yscale('log')
ax.set_ylim(1, 200000)
ax.set_ylabel('Published output power (kW, log scale)')
ax.set_title('A. Supply / model / family ratings — not a market ceiling', loc='left', fontsize=12)
ax.axhline(100000, color='#777777', linestyle='--', linewidth=1)
ax.text(130, 116000, '100 MW aggregate design target', fontsize=9)
offsets = {'A':(8,0), 'B':(8,10), 'C':(-5,10), 'D':(-10,-21), 'E':(-10,-21),
           'F':(7,10), 'G':(-9,-23), 'H':(8,9), 'I':(-8,10), 'J':(-8,-22)}
for r in industrial:
    if r['scope']=='input_rating':
        continue
    x = band(ax, r, r['power_kw'], 's' if r['scope']=='installation' else 'o')
    dx, dy = offsets[r['id']]
    text = f"{r['id']} [{r['source_ids']}] {r['power_kw']:g} kW"
    ax.annotate(text, (x,r['power_kw']), xytext=(dx,dy), textcoords='offset points',
                fontsize=9, ha='right' if r['id'] in ['I','J'] else 'left')
setup_frequency(eff)
eff.set_ylim(60, 104)
eff.set_ylabel('Quoted generator efficiency (%)')
eff.set_title('B. Efficiency claims — vendor boundaries differ; no fitted trend', loc='left', fontsize=12)
eff_offsets={'C':(0,9),'D':(0,-18),'E':(0,-23),'G':(-10,-20),'H':(9,-20),'I':(-6,-22),'J':(-6,10)}
for r in industrial:
    y = r['efficiency_percent']
    if y is None:
        continue
    x = band(eff, r, y, '^' if r['efficiency_qualifier']=='greater_than' else 'o')
    q = r['efficiency_qualifier']
    prefix = {'approximate':'~', 'stated':'', 'greater_than':'>', 'approaching':'approaches '}[q]
    if q == 'greater_than':
        eff.annotate('', (x,y+4), (x,y+.7), arrowprops={'arrowstyle':'->','color':COLORS[r['technology']]})
    dx,dy=eff_offsets[r['id']]
    eff.annotate(f"{r['id']} [{r['source_ids']}] {prefix}{y:g}%", (x,y), xytext=(dx,dy),
                 textcoords='offset points', fontsize=9, ha='right' if r['id'] in ['G','I','J'] else 'left')
handles=[Line2D([0],[0],color=c, marker='o',label=t) for t,c in COLORS.items() if t!='Fusion gyrotron']
fig.legend(handles=handles, loc='lower center', bbox_to_anchor=(.5,.065), ncol=4, frameon=False)
fig.text(.125,.027,'Horizontal segments show quoted frequency bands, not measured performance curves or guaranteed full-power envelopes.\n'
         'IDs A–J resolve to models and primary-source URLs in power_sources.csv and sources.md. Missing efficiencies are omitted.',fontsize=9)
save(fig,'frequency_evidence')

# Separately show research evidence and aggregate installations to avoid mixing boundaries.
fig, axes=plt.subplots(1,2,figsize=(12,4.8))
fig.subplots_adjust(bottom=.26,wspace=.4,top=.8)
fig.suptitle('Scale context and counterexample',fontsize=17)
axes[0].bar(['ABP installed\n3 × 42 MW'],[126],color=COLORS['Induction'],width=.45)
axes[0].axhline(100,color='#777777',ls='--')
axes[0].set_ylabel('Aggregate installed output (MW)')
axes[0].set_ylim(0,150)
axes[0].text(0,129,'126 MW [S1]',ha='center')
axes[0].set_title('Exact frequency unavailable; excluded from frequency plot',fontsize=10)
axes[1].scatter([170],[1.05],color=COLORS['Fusion gyrotron'],s=100,marker='D')
axes[1].set_xlim(150,190); axes[1].set_ylim(0,1.5)
axes[1].set_xlabel('Output frequency (GHz)'); axes[1].set_ylabel('Gyrotron output (MW)')
axes[1].annotate('K [S11]: 1.05 MW\n50.6% gyrotron efficiency\n300 s acceptance test',(170,1.05),xytext=(0,15),textcoords='offset points',ha='center')
fig.text(.12,.07,'Gyrotron data is specialist fusion evidence, not a continuous chemical-plant installation.\n'
         'It disproves a universal monotonic power ceiling; its efficiency excludes upstream supply and plant losses.',fontsize=10)
save(fig,'scale_context')

# Exact energy-balance scenarios, not measured product data.
scenarios=[98,95,91,85,80,70]
losses=[100/(e/100)-100 for e in scenarios]
assert abs(losses[4]-25) < 1e-9
fig,ax=plt.subplots(figsize=(10,5.5))
fig.subplots_adjust(bottom=.22,top=.82)
fig.suptitle('Generator losses before power reaches the reactor',fontsize=17)
fig.text(.125,.88,'Calculated for 100 MW electrical / RF output; downstream losses excluded',fontsize=11)
bars=ax.bar([f'{e}%' for e in scenarios],losses,color='#ba6024',width=.65)
ax.bar_label(bars,labels=[f'{v:.1f} MW' for v in losses],padding=5)
ax.set_ylim(0,50);ax.set_ylabel('Upstream generator loss (MW)');ax.set_xlabel('Generator efficiency scenario')
ax.grid(axis='y',alpha=.18)
fig.text(.125,.055,'Calculation: loss = 100 MW × (1 / efficiency − 1). At 80%, grid input is 125 MW.\n'
         'These are illustrative efficiency scenarios, not assignments to particular products.',fontsize=10)
save(fig,'upstream_losses_100mw')

with (OUT/'scaling_100mw.csv').open('w',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    w.writerow(['id','label','source_ids','published_output_kw','arithmetic_units_for_100mw','caveat'])
    for r in industrial:
        if r['scope']=='input_rating':
            continue
        w.writerow([r['id'],r['label'],r['source_ids'],r['power_kw'],math.ceil(100000/r['power_kw']),
                    'Arithmetic only; no redundancy or downstream losses; family ratings need confirmation'])
print(f'Validated {len(rows)} source-linked records; generated three PNG/SVG figure pairs and scaling CSV in {OUT}')

with (ROOT/'high_frequency_sources.csv').open(encoding='utf-8',newline='') as f:
    high=list(csv.DictReader(f))
for r in high:
    for key in ['frequency_hz','average_power_kw','peak_power_kw']:
        r[key]=float(r[key])
    assert 0 < r['average_power_kw'] <= r['peak_power_kw'] and r['source_ids']
assert high[3]['average_power_kw']==high[3]['peak_power_kw']*.002

# Standalone commercial-scale graph requested by the user.
fig,ax=plt.subplots(figsize=(13,7))
fig.subplots_adjust(bottom=.24,top=.84)
fig.suptitle('Commercial source scale: average power matters',fontsize=18,x=.125,ha='left')
fig.text(.125,.89,'Published examples, not a market ceiling | specialist tubes and research shown separately',fontsize=11)
ax.set_xscale('log');ax.set_yscale('log')
ax.set_xlim(100,4e11);ax.set_ylim(1,200000)
ax.set_xticks([1e3,1e5,1e7,1e9,1e11],['1 kHz','100 kHz','10 MHz','1 GHz','100 GHz'])
ax.set_xlabel('Output / carrier frequency (log scale)')
ax.set_ylabel('Output power (kW, log scale)');ax.grid(which='major',alpha=.18)
ax.axhline(100000,color='#777777',ls='--',lw=1)
ax.text(150,115000,'100 MW continuous / average target',fontsize=10)
for r in industrial:
    if r['scope']=='input_rating':
        continue
    x=math.sqrt(r['frequency_min_hz']*r['frequency_max_hz'])
    ax.plot([r['frequency_min_hz'],r['frequency_max_hz']],[r['power_kw']]*2,color='#176d8a',lw=2)
    ax.scatter(x,r['power_kw'],c='#176d8a',s=40,marker='s' if r['scope']=='installation' else 'o')
    ax.annotate(r['id'],(x,r['power_kw']),xytext=(5,8 if r['id']!='G' else -17),textcoords='offset points')
for r in high:
    x,y,p=r['frequency_hz'],r['average_power_kw'],r['peak_power_kw']
    ax.scatter(x,y,marker='D',s=45,c='#7351a1')
    label_offset={'L':(-28,-20),'M':(-32,18),'N':(6,18),'O':(6,8),'P':(6,8)}[r['id']]
    ax.annotate(r['id']+' avg',(x,y),xytext=label_offset,textcoords='offset points',fontsize=9)
    if p>y:
        ax.plot([x,x],[y,p],color='#ba6024',lw=1.2,ls=':')
        ax.scatter(x,p,marker='^',s=60,facecolors='none',edgecolors='#ba6024')
        ax.annotate(f"{r['id']} peak: {p/1000:g} MW",(x,p),xytext=(7,6),textcoords='offset points',fontsize=9)
research=next(r for r in rows if r['id']=='K')
ax.scatter(170e9,1050,marker='x',s=65,c='#555555')
ax.annotate('K: 300 s test',(170e9,1050),xytext=(-8,9),textcoords='offset points',ha='right',fontsize=9)
fig.legend(handles=[Line2D([0],[0],marker='o',color='#176d8a',label='Industrial supply / family'),
                    Line2D([0],[0],marker='D',color='#7351a1',ls='',label='Specialist tube / transmitter average'),
                    Line2D([0],[0],marker='^',markerfacecolor='none',color='#ba6024',ls='',label='Pulsed peak'),
                    Line2D([0],[0],marker='x',color='#555555',ls='',label='Research test')],
           loc='lower center',bbox_to_anchor=(.5,.1),ncol=2,frameon=False)
fig.text(.125,.03,'Source mapping: A:S1 B:S2 C:S3 D:S4 E:S5/S6 F:S7 G/H:S8 I:S9 J:S10 K:S11 L/M/N:S13 O:S14 P:S15.\n'
         'Bands are nominal family ranges. O: 1 MW peak × 0.002 duty = 2 kW average. P: 18–20 kW average (20 plotted).',fontsize=9)
save(fig,'commercial_scale')
print('Added commercial_scale.png/svg with source-linked CW, pulsed, and specialist examples.')

# Output voltage limits: missing output voltages stay missing.
with (ROOT/'voltage_sources.csv').open(encoding='utf-8',newline='') as f:
    volts=list(csv.DictReader(f))
fig,(ax,req)=plt.subplots(2,1,figsize=(12,10))
fig.subplots_adjust(hspace=.5,bottom=.14,top=.9)
fig.suptitle('Voltage connects the power supply to the reactor',fontsize=18)
ax.set_xscale('log');ax.set_yscale('log')
for r in volts:
    if not r['max_output_v_rms']:
        continue
    a,b=float(r['frequency_min_hz']),float(r['frequency_max_hz'])
    v=float(r['max_output_v_rms'])/1000
    assert v>0 and r['source_ids']
    ax.plot([a,b],[v,v],marker='|',color='#176d8a',lw=2,markersize=8)
    # F2/F3 coincide: annotate together once.
    if r['id']=='F3':
        continue
    labels={'D':'D: 240 kW; 1.2 kV RMS max [S4]',
            'F1':'F1: 100 kW; 6.6 kV [S7]',
            'F2':'F2/F3: 30/60 kW; 6.3 kV [S7]',
            'F4':'F4: 10 kW; 5.0 kV [S7]'}
    ax.annotate(labels[r['id']],(b,v),xytext=(10,12 if r['id']=='F1' else -7),textcoords='offset points',fontsize=10)
ax.set_xlim(500,2e8);ax.set_ylim(.8,10)
ax.set_yticks([1,2,5,10],['1','2','5','10'])
ax.set_xlabel('Output frequency (Hz, log scale)');ax.set_ylabel('Published output voltage limit (kV RMS)')
ax.set_title('A. Specific model limits; maximum power and voltage are not necessarily simultaneous',loc='left',fontsize=11)
ax.grid(which='major',alpha=.2)

freq=[10**(3+i*3/150) for i in range(151)]
cap=10e-9;loss_tangent=.1;power=100e3
voltage=[math.sqrt(power/(2*math.pi*f*cap*loss_tangent))/1000 for f in freq]
req.loglog(freq,voltage,color='#ba6024',lw=2)
for f in [1e3,1e4,1e5,1e6]:
    v=math.sqrt(power/(2*math.pi*f*cap*loss_tangent))/1000
    req.scatter(f,v,c='#ba6024')
    req.annotate(f'{v:.1f} kV',(f,v),xytext=(5,10),textcoords='offset points')
req.set_xlim(700,2e6);req.set_ylim(2,250)
req.set_xticks([1e3,1e4,1e5,1e6],['1 kHz','10 kHz','100 kHz','1 MHz'])
req.set_xlabel('Frequency');req.set_ylabel('Required reactor voltage (kV RMS)')
req.set_title('B. Illustrative dielectric load: 100 kW real power, C = 10 nF, loss tangent = 0.1',loc='left',fontsize=11)
req.grid(which='major',alpha=.2)
fig.text(.125,.035,'Panel B is a calculation, not a vendor rating: V = sqrt[P / (2π f C tanδ)]. Properties assumed constant.\n'
         'Generator terminals and reactor electrodes are different boundaries; matching changes voltage/current.\n'
         'Sources: voltage_sources.csv and sources.md. Model assumptions and limits: reactor_matching.md.',fontsize=10)
save(fig,'voltage_and_reactor_matching')
print('Added voltage_and_reactor_matching.png/svg.')
