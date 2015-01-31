from math import pi, exp, sin, cos, sqrt
#~ csv = open('flightlog.csv', 'w')
#~ csv.write("Time,Mass,R,dR,ddR,Theta,dTheta,ddTheta\r\n")
#~ csv.write("Fuel,Throttle,MaxAlt\r\n")

#Kerbin setup
radius = 600000.0
mu = 3531600000000.0 #gravitational parameter
scale = 5000.0 #atmospheric scale height
k = 0.0049 #magic. Also slightly wrong.
rot = 2*pi/21600 #rotation rate in rad/s. Because the 6 h sidereal day is still real.

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
	r = radius + 5000.0
	altitude = 0.0
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
	#~ csv.write(str(t) + "," + str(m) + "," + str(r) + "," + str(dr) + "," + str(ddr) + "," + str(theta) + "," + str(dtheta) + "," + str(ddtheta) + "\r\n")

	#need to account for planet rotation with theta & rot
	while ((t < tmax) and (r > radius)):
		altitude = r - radius
		pressure = exp(-altitude/scale)
		Cd = ((0.182) + 0.3*(m-0.9))/m
		r += dr*dt+0.5*ddr*dt*dt
		theta += dtheta*dt+0.5*ddtheta*dt*dt
		dr += ddr*dt
		dtheta += ddtheta*dt
		# v = sqrt(dr*dr+r*r*dtheta*dtheta) #going to confine drag to seperate r and theta parts.
		ddr = (r*dtheta*dtheta) - (k*Cd*pressure*dr*abs(dr)) - (mu/r/r) + (Throttle*Thrust*sin(gamma)/m)
		ddtheta = (-2*dr*dtheta/r) - (k*Cd*pressure*r*dtheta*abs(r*dtheta)) + (Throttle*Thrust*cos(gamma)/m)
		if ((Thrust > 0) and (Throttle > 0)):
			dv += dt*Thrust*Throttle/m
		if (m == MassEmpty):
			dm = 0
			Thrust = 0
		if (m > MassEmpty):
			dm = Throttle*Thrust/((Isp0 - (Isp0 - Isp1)*pressure)*9.82)
		m -= dm*dt
		if (m < MassEmpty): #out of propellant
			m = MassEmpty
			Thrust = dm*(Isp0 - (Isp0 - Isp1)*pressure)*9.82 #I'm pretty sure KSP doesn't do this.
		t += dt
		if (altmax < altitude):
			altmax = altitude
		#~ csv.write(str(t) + "," + str(m) + "," + str(r) + "," + str(dr) + "," + str(ddr) + "," + str(theta) + "," + str(dtheta) + "," + str(ddtheta) + "\r\n")
		#~ print("t:" + str(t) + " m:" +str(m) + " Cd:" +str(Cd))
		#~ print("r:" + str(r) + " dr:" + str(dr) + " ddr:" + str(ddr))
		#~ print("theta:" + str(theta) + " dtheta:" + str(dtheta) + " ddtheta:" + str(ddtheta))
	print("fuel == " + str(fuel) + " Throttle = " + str(Throttle) + " Max Alt = " + str(altmax) + " dV = " + str(dv))
	#~ csv.write(str(fuel) + "," + str(Throttle) + "," + str(altmax) + "\r\n")
	Throttle -= 0.05
#~ csv.close()
