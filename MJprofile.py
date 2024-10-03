'''Plotting nominal ascent profiles using mechjeb's classic guidance'''
import numpy as np
from matplotlib import pyplot as plt

start_alt = 0
end_alt = 80000
shape = 0.5 #shape should be between 0 and 1
#start_angle = 90
end_angle = 0

altitudes = np.linspace(0,80000,1000)
angles = [90-((alt-start_alt)/(end_alt-start_alt))**shape*(90-end_angle) for alt in altitudes]

fig, ax = plt.subplots()
#ax.plot(altitudes, angles, label="0-80 km; 0-90 deg; shape "+str(shape))
shapes = [1.0, 0.833, 0.667, 0.5, 0.333, 0.167, 0.0]
for shape in shapes:
	revisedangles = [90-((alt-start_alt)/(end_alt-start_alt))**shape*(90-end_angle) for alt in altitudes]
	ax.plot(altitudes, revisedangles, label="0-80 km; 0-90 deg; shape "+str(shape))

ax.set_xlim(0,end_alt)
ax.set_ylim(0,90)
ax.set_xlabel("altitude (m)")
ax.set_ylabel("Flight Path Angle (degrees)")
ax.legend(loc=0)
ax.set_title("MechJeb Classic Ascent Profiles")
fig.set_size_inches(8, 6)
fig.set_dpi(100)
plt.tight_layout()
#plt.savefig("MJ_Ascents.png")
plt.show()

