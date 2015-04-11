# Ascent Simulation 0.3 -- Apr 10, 2015

from math import pi, exp, sin, cos, sqrt, log

class Body:
	#Kerbin by default
	radius = 600000.0
	mu = 3531600000000.0 #gravitational parameter
	scale = 5000.0 #atmospheric scale height
	cutoff = 5000.0*log(1e6) #atmospheric cutoff altitude
	rot = 2*pi/21600 #rotation rate in rad/s. Because the 6 h sidereal day is still real.
	k = 0.004 * 1.2230948554874 #magic number to make drag work based on local pressure. Includes the 0.5 factor in the drag equation. (uses data from the actual API)
	def pressure(alt):
		if (alt < cutoff):
			return exp(-alt/scale)
		else:
			return 0.0

class Craft:
	#single stage only, example craft is mk1 pod + mk16 chute + RT-10 SRB
	Thrust = 250
	MassDry = 0.1+0.8+0.5
	MassWet = 1.4 + 433*0.0075
	CdDry = (0.1*0.22+0.8*0.2+0.5*0.3)/1.4
	CdWet = (0.1*0.22+0.8*0.2+3.7475*0.3)/4.6475
	Isp1 = 225
	Isp0 = 240
	def Isp(pressure):
		if pressure > 0:
			return Isp0 - (Isp0 - Isp1)*pressure
		else:
			return Isp0
#class ascentProfile:
#Idea: Profile 0: straight up at full throttle. Profile 1: throttle control. Profile 2: pitch control. Profile 3: 1+2. (-1: do nothing)

#class flightLog:
	def start(logname):
		csv = open('flightlog.csv', 'w') #we can leave this hanging, right?
		csv.write("Time,Mass,R,dR,ddR,Theta,dTheta,ddTheta\r\n")
	def log():
		csv.write("Fuel,Throttle,MaxAlt\r\n")
	def stop():
		csv.close()

class Orbit:
	def semiMajorAxis(R, Spd, GM):
		return 1/(2/R - Spd*Spd/GM)
	def eccentricity(R, Spd, GM, SMA):
		return sqrt(1-R*R*Spd*Spd/(SMA*GM))
	def apoapsis(semiMajorAxis, eccentricity):
		return semiMajorAxis*(1+eccentricity)
	def periapsis(semiMajorAxis, eccentricity):
		return semiMajorAxis*(1-eccentricity) 

fuel = 433.0
Throttle = 1.0
while (Throttle > 0.0):
#default craft: rocket with a Mk1 pod, Mk16 chute, RT-10
	Isp1 = 225
	Isp0 = 240
	Thrust = 250
	MassEmpty = 0.1+0.8+0.5+0.05+1.125
	MassFull = MassEmpty + fuel*0.0075
	Cd = (0.22*0.1 + 0.2*(MassEmpty-0.1) + 0.3*(0.5+0.0075*fuel))/MassFull
	gamma = pi/2 #straight up
	m = MassFull

	#starting situation
	Kerbin = Body
	altitude = 70.0
	r = Kerbin.radius + altitude
	theta = 0.0
	dr = 0.0
	dtheta = 0.0
	ddr = 0.0
	ddtheta = 0.0
	t = 0.0
	dt = 0.1
	tmax = 100.0
	altmax = 0.0
	dv = 0.0
	Kerbin.pressure()

	#~ csv.write(str(t) + "," + str(m) + "," + str(r) + "," + str(dr) + "," + str(ddr) + "," + str(theta) + "," + str(dtheta) + "," + str(ddtheta) + "\r\n")

	#need to account for planet rotation with theta & rot
	while ((t < tmax) and (r >= Kerbin.radius)):
		altitude = r - Kerbin.radius
		Kerbin.pressure(altitude)
		Cd = ((0.182) + 0.3*(m-0.9))/m
		r += dr*dt+0.5*ddr*dt*dt
		theta += dtheta*dt+0.5*ddtheta*dt*dt
		dr += ddr*dt
		dtheta += ddtheta*dt
		# v = sqrt(dr*dr+r*r*dtheta*dtheta) #going to confine drag to seperate r and theta parts.
		ddr = (r*dtheta*dtheta) - (Kerbin.k*Cd*Kerbin.pressure(altitude)*dr*abs(dr)) - (mu/r/r) + (Throttle*Thrust*sin(gamma)/m)
		ddtheta = (-2*dr*dtheta/r) - (Kerbin.k*Cd*Kerbin.pressure(altitude)*r*dtheta*abs(r*dtheta)) + (Throttle*Thrust*cos(gamma)/m)
		if ((Thrust > 0) and (Throttle > 0)):
			dv += dt*Thrust*Throttle/m
		if (m == MassEmpty):
			dm = 0
			Thrust = 0
		if (m > MassEmpty):
			dm = Throttle*Thrust/((Isp0 - (Isp0 - Isp1)*Kerbin.pressure(altitude))*9.82)
		m -= dm*dt
		if (m < MassEmpty): #out of propellant
			m = MassEmpty
			Thrust = dm*(Isp0 - (Isp0 - Isp1)*Kerbin.pressure(altitude))*9.82 #I'm pretty sure KSP doesn't do this.
		t += dt
		if (altmax < altitude):
			altmax = altitude
		
		# Orbital parameters
		
		#~ csv.write(str(t) + "," + str(m) + "," + str(r) + "," + str(dr) + "," + str(ddr) + "," + str(theta) + "," + str(dtheta) + "," + str(ddtheta) + "\r\n")
		#~ print("t:" + str(t) + " m:" +str(m) + " Cd:" +str(Cd))
		#~ print("r:" + str(r) + " dr:" + str(dr) + " ddr:" + str(ddr))
		#~ print("theta:" + str(theta) + " dtheta:" + str(dtheta) + " ddtheta:" + str(ddtheta))
	print("fuel == " + str(fuel) + " Throttle = " + str(Throttle) + " Max Alt = " + str(altmax) + " dV = " + str(dv))
	#~ csv.write(str(fuel) + "," + str(Throttle) + "," + str(altmax) + "\r\n")
	Throttle -= 0.05
#~ csv.close()
