from matplotlib import pyplot as plt
import numpy as np

Engines = np.genfromtxt("KSP engines 1.12.5.csv",dtype=None, delimiter=',', names=True)

#tanks = [0, 0.5625, 1.125, 2.25, 4.5, 9, 18, 20.25, 36, 40.5, 81]
tanks = np.arange(0,562.5,0.5625)
tanks = np.insert(tanks, 1, [0.225, 0.3375])
g0 = 9.80665

payloads = [0,0.1,0.3,1,3]

fig, ax = plt.subplots(ncols=1, nrows=1, figsize=(8,6))

Δv0 = [800*g0*np.log((3.0+t)/(3.0+t/9)) for t in tanks]
TMR0 = [60/(3.0+t) for t in tanks]
ax.plot(Δv0, TMR0, color="gray", linewidth=2.0, linestyle='-', label="LV-N, 0 payload")
Δv0 = [800*g0*np.log((3.0+t+0.1)/(3.0+t/9+0.1)) for t in tanks]
TMR0 = [60/(3.0+t+0.1) for t in tanks]
ax.plot(Δv0, TMR0, color="gray", linewidth=2.0, linestyle='--', label="0.1 tonne payload")
Δv0 = [800*g0*np.log((3.0+t+1.0)/(3.0+t/9+1.0)) for t in tanks]
TMR0 = [60/(3.0+t+1.0) for t in tanks]
ax.plot(Δv0, TMR0, color="gray", linewidth=2.0, linestyle=':', label="1.0 tonne payload")

Δv0 = [345*g0*np.log((0.5+t)/(0.5+t/9)) for t in tanks]
TMR0 = [60/(0.5+t) for t in tanks]
ax.plot(Δv0, TMR0, color="blue", linewidth=2.0, linestyle='-', label="LV-909, 0 payload")
Δv0 = [345*g0*np.log((0.5+t+0.1)/(0.5+t/9+0.1)) for t in tanks]
TMR0 = [60/(0.5+t+0.1) for t in tanks]
ax.plot(Δv0, TMR0, color="blue", linewidth=2.0, linestyle='--', label="0.1 tonne payload")
Δv0 = [345*g0*np.log((0.5+t+1.0)/(0.5+t/9+1.0)) for t in tanks]
TMR0 = [60/(0.5+t+1.0) for t in tanks]
ax.plot(Δv0, TMR0, color="blue", linewidth=2.0, linestyle=':', label="1.0 tonne payload")

Δv0 = [320*g0*np.log((0.13+t)/(0.13+t/9)) for t in tanks]
TMR0 = [20/(0.13+t) for t in tanks]
ax.plot(Δv0, TMR0, color="orange", linewidth=2.0, linestyle='-', label="48-7S, 0 payload")
Δv0 = [320*g0*np.log((0.13+t+0.1)/(0.13+t/9+0.1)) for t in tanks]
TMR0 = [20/(0.13+t+0.1) for t in tanks]
ax.plot(Δv0, TMR0, color="orange", linewidth=2.0, linestyle='--', label="0.1 tonne payload")
Δv0 = [320*g0*np.log((0.3+t+1.0)/(0.3+t/9+1.0)) for t in tanks]
TMR0 = [20/(0.3+t+1.0) for t in tanks]
ax.plot(Δv0, TMR0, color="orange", linewidth=2.0, linestyle=':', label="1.0 tonne payload")

ax.set_xlim(0,8000)
ax.set_ylim(0,160)
ax.set_xlabel("Δv (m/s)")
ax.set_ylabel("TMR (N/kg)")
#ax.set_title("0 payload, vac")
#ax.set_title("0 payload, 1 atm")
#ax.set_title("0.1 tonne, vac")
#ax.set_title("0.1 tonne, 1 atm")
#ax.set_title("1.0 tonne, vac")
#ax.set_title("1.0 tonne, 1 atm")
ax.legend(loc=0)
fig.suptitle("Upper Stage/Lander Engine Performance")
'''
fig, bx = plt.subplots(ncols=2, nrows=3, figsize=(14,12))
for engine in Engines:
	if((engine["Name"] == b'Reliant') or (engine["Name"] == b'Swivel') or (engine["Name"] == b'Terrier')):
		Δv0 = [engine['Isp0']*g0*np.log((engine['Mass']+t)/(engine['Mass']+t/9)) for t in tanks]
		TMR0 = [engine['Thrust0']/(engine['Mass']+t) for t in tanks]
		bx[0,0].plot(Δv0, TMR0, label=engine['Name'])
		Δv1 = [engine['Isp1']*g0*np.log((engine['Mass']+t)/(engine['Mass']+t/9)) for t in tanks]
		TMR1 = [engine['Thrust1']/(engine['Mass']+t) for t in tanks]
		bx[0,1].plot(Δv1, TMR1, label=engine['Name'])
		Δv0 = [engine['Isp0']*g0*np.log((engine['Mass']+t+0.1)/(engine['Mass']+t/9+0.1)) for t in tanks]
		TMR0 = [engine['Thrust0']/(engine['Mass']+t+0.1) for t in tanks]
		bx[1,0].plot(Δv0, TMR0, label=engine['Name'])
		Δv1 = [engine['Isp1']*g0*np.log((engine['Mass']+t+0.1)/(engine['Mass']+t/9+0.1)) for t in tanks]
		TMR1 = [engine['Thrust1']/(engine['Mass']+t+0.1) for t in tanks]
		bx[1,1].plot(Δv1, TMR1, label=engine['Name'])
		Δv0 = [engine['Isp0']*g0*np.log((engine['Mass']+t+1.0)/(engine['Mass']+t/9+1.0)) for t in tanks]
		TMR0 = [engine['Thrust0']/(engine['Mass']+t+1.0) for t in tanks]
		bx[2,0].plot(Δv0, TMR0, label=engine['Name'])
		Δv1 = [engine['Isp1']*g0*np.log((engine['Mass']+t+1.0)/(engine['Mass']+t/9+1.0)) for t in tanks]
		TMR1 = [engine['Thrust1']/(engine['Mass']+t+1.0) for t in tanks]
		bx[2,1].plot(Δv1, TMR1, label=engine['Name'])
bx[0,0].set_xlim(0,8000)
bx[0,0].set_ylim(0,300)
bx[0,1].set_xlim(0,8000)
bx[0,1].set_ylim(0,300)
bx[0,0].set_xlabel("Δv (m/s)")
bx[0,0].set_ylabel("TMR (N/kg)")
bx[0,0].set_title("0 payload, vac")
bx[0,1].set_title("0 payload, 1 atm")
bx[1,0].set_title("0.1 tonne, vac")
bx[1,1].set_title("0.1 tonne, 1 atm")
bx[2,0].set_title("1.0 tonne, vac")
bx[2,1].set_title("1.0 tonne, 1 atm")
bx[0,1].legend(loc=0)
fig.suptitle("LFO Engine Performance")
'''
plt.tight_layout()
plt.show()
