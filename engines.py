from matplotlib import pyplot as plt
import numpy as np

Engines = np.genfromtxt("KSP engines 1.12.5.csv",dtype=None, delimiter=',', names=True)

tanks = [0, 0.5625, 1.125, 2.25, 4.5, 9, 18, 20.25, 36, 40.5, 81]
tanks = np.arange(0,562.5,0.5625)
g0 = 9.80665

fig, ax = plt.subplots(ncols=2, nrows=5, figsize=(14,12))
for engine in Engines:
	if((engine["Prop"] == b'LFO') and (engine["Size"] == b'0')):
		Δv0 = [engine['Isp0']*g0*np.log((engine['Mass']+t)/(engine['Mass']+t/9)) for t in tanks]
		TMR0 = [engine['Thrust0']/(engine['Mass']+t) for t in tanks]
		ax[0,0].plot(Δv0, TMR0, label=engine['Name'])
		Δv1 = [engine['Isp1']*g0*np.log((engine['Mass']+t)/(engine['Mass']+t/9)) for t in tanks]
		TMR1 = [engine['Thrust1']/(engine['Mass']+t) for t in tanks]
		ax[0,1].plot(Δv1, TMR1, label=engine['Name'])
	if((engine["Prop"] == b'LFO') and (engine["Size"] == b'1')):
		Δv0 = [engine['Isp0']*g0*np.log((engine['Mass']+t)/(engine['Mass']+t/9)) for t in tanks]
		TMR0 = [engine['Thrust0']/(engine['Mass']+t) for t in tanks]
		ax[1,0].plot(Δv0, TMR0, label=engine['Name'])
		Δv1 = [engine['Isp1']*g0*np.log((engine['Mass']+t)/(engine['Mass']+t/9)) for t in tanks]
		TMR1 = [engine['Thrust1']/(engine['Mass']+t) for t in tanks]
		ax[1,1].plot(Δv1, TMR1, label=engine['Name'])
	if(engine["Prop"] == b'LFO' and engine["Size"] == b'1.5'):
		Δv0 = [engine['Isp0']*g0*np.log((engine['Mass']+t)/(engine['Mass']+t/9)) for t in tanks]
		TMR0 = [engine['Thrust0']/(engine['Mass']+t) for t in tanks]
		ax[2,0].plot(Δv0, TMR0, label=engine['Name'])
		Δv1 = [engine['Isp1']*g0*np.log((engine['Mass']+t)/(engine['Mass']+t/9)) for t in tanks]
		TMR1 = [engine['Thrust1']/(engine['Mass']+t) for t in tanks]
		ax[2,1].plot(Δv1, TMR1, label=engine['Name'])
	if(engine["Prop"] == b'LFO' and engine["Size"] == b'2'):
		Δv0 = [engine['Isp0']*g0*np.log((engine['Mass']+t)/(engine['Mass']+t/9)) for t in tanks]
		TMR0 = [engine['Thrust0']/(engine['Mass']+t) for t in tanks]
		ax[3,0].plot(Δv0, TMR0, label=engine['Name'])
		Δv1 = [engine['Isp1']*g0*np.log((engine['Mass']+t)/(engine['Mass']+t/9)) for t in tanks]
		TMR1 = [engine['Thrust1']/(engine['Mass']+t) for t in tanks]
		ax[3,1].plot(Δv1, TMR1, label=engine['Name'])
	if(engine["Prop"] == b'LFO' and engine["Size"] == b'3'):
		Δv0 = [engine['Isp0']*g0*np.log((engine['Mass']+t)/(engine['Mass']+t/9)) for t in tanks]
		TMR0 = [engine['Thrust0']/(engine['Mass']+t) for t in tanks]
		ax[4,0].plot(Δv0, TMR0, label=engine['Name'])
		Δv1 = [engine['Isp1']*g0*np.log((engine['Mass']+t)/(engine['Mass']+t/9)) for t in tanks]
		TMR1 = [engine['Thrust1']/(engine['Mass']+t) for t in tanks]
		ax[4,1].plot(Δv1, TMR1, label=engine['Name'])
ax[0,0].set_xlim(0,8000)
ax[0,0].set_ylim(0,300)
ax[0,1].set_xlim(0,8000)
ax[0,1].set_ylim(0,300)
ax[1,0].set_xlim(0,8000)
ax[1,0].set_ylim(0,300)
ax[1,1].set_xlim(0,8000)
ax[1,1].set_ylim(0,300)
ax[2,0].set_xlim(0,8000)
ax[2,0].set_ylim(0,300)
ax[2,1].set_xlim(0,8000)
ax[2,1].set_ylim(0,300)
ax[3,0].set_xlim(0,8000)
ax[3,0].set_ylim(0,300)
ax[3,1].set_xlim(0,8000)
ax[3,1].set_ylim(0,300)
ax[4,0].set_xlim(0,8000)
ax[4,0].set_ylim(0,400)
ax[4,1].set_xlim(0,8000)
ax[4,1].set_ylim(0,400)
ax[0,0].set_xlabel("Δv (m/s)")
ax[0,0].set_ylabel("TMR (N/kg)")
ax[0,0].set_title("0 payload, vac")
ax[0,1].set_title("0 payload, 1 atm")
ax[0,1].legend(loc=0)
ax[1,1].legend(loc=0)
ax[2,1].legend(loc=0)
ax[3,1].legend(loc=0)
ax[4,1].legend(loc=0)
fig.suptitle("LFO Engine Performance")

#plt.tight_layout()
plt.show()
