/*	Raptop General Ascent Simulator. Version 0.2 July 09, 2014 
	Created by Patrick "UmbralRaptor" Newman
	Proposed licence: GPL v3. Any better suggestions? */

import java.lang.Math;
// need better library choices for csv reading/writing.
// import java.io.FileReader;
// import java.io.FileWriter;
// import java.io.FileReader;
// import java.io.IOException;
// import java.io.BufferedWriter;
// import java.io.File;
import java.io.*;

class Body {
	// Kerbin, other bodies are currently being ignored.
	static double GM = 3.5316e12; // m^3/s^2
	static double radius = 6e5; // meters
	static double rotation = 0; // We've spun down the planet. It will be 2.9088820866572159615394846141477e-4 radians per second
	static double rho0 = 1; // atmospheres
	static double scaleHeight = 5000; // meters
	static double cutoffDistance = radius + 13.815510557964274104107948728106*scaleHeight; // At the cutoff height, pressure is 1e-6 datum.
	static double rho(double radialDistance) { // lies. Uses distance from center, not datum.
		if (radialDistance < cutoffDistance) {
			return rho0*Math.exp((radius-radialDistance)/scaleHeight);
		}
		else{
			return 0.0;
		}
	}
}
	
class Craft { // Should be user inputable, and allow multiple stages. Expect an array in the future.
	// Currently a Snatlus 2 at max payload. For future, need a way to load external files and multiple stages.
	static double thrust = 650.0;
	static double massWet = 43.5;
	static double massDry = 11.5;
	static double isp1 = 300.0;
	static double isp0 = 350.0;
	static double Cd = 0.2; // Assumes stock aero. Implies terminal velocity of 
	static double isp(double rho) {
		if (rho > 1) {
			return isp1;
		}
		else {
			return (isp0 - rho*(isp0 -isp1));
		}
	}
}
	
class ascentProfile { // Making this alterable without editing the source code is non-trivial.
	// Idea: Profile 0: straight up at full throttle. Profile 1: throttle control. Profile 2: pitch control. Profile 3: 1+2. (-1: do nothing)
	static double throttle(double Mass) {
		if (Mass > Craft.massDry) {
			return 1; // [REDACTED] terminal velocity.
		} else {
			return 0; // No fuel == no throttle
		}
	}
	static double gamma = 0; // Should be a function. Also, user editable.
}

class OrbitalParameters {
	static double semiMajorAxis;
	static double eccentricity;
	static double apoapsis;
	static double periapsis; 
	static void update(double R, double Spd) {
		semiMajorAxis = 1/(2/R - Spd*Spd/Body.GM);
		eccentricity = Math.sqrt(1-R*R*Spd*Spd/(semiMajorAxis*Body.GM));
		apoapsis = semiMajorAxis*(1+eccentricity);
		periapsis = semiMajorAxis*(1-eccentricity); 
	}
} 

class FlightLog {
	void start() {
		FileWriter flightlog = null;
		try {
		flightlog = new FileWriter("test.txt");
		flightlog.write(buf);
		}
	void end() {
		flightlog.close() throws IOException{}
	}
	void line() {
		// standard loop: convert series of vars to string, then write said string.

		byte buf [] = "\r\n";
		Files.write(outFile, buf);
	}
}

public class AscentSimulation {
	public static void main(java.lang.String[] args) {
		double r0, r1, r2, theta0, theta1, theta2; // variables of polar motion. Spherical will come later.
		double T = 0.0; // Current time.
		double MAX_TIME = 2000; // maximum time, will need user input.
		double dT = 1.0; // timestep size, also will need user input.
		double Mass = Craft.massWet; // Will need to rework for multiple stages.
		double dM, V, thrust, deltaVExpended;
		double surfaceSpeed, orbitalSpeed; // to spinup, will need to replace V with surface and orbital speed.
		
		// Initial conditions. Todo: let it choose a craft.
		r0 = Body.radius + 70; // KSC launch pad, approximately 70 m altitude.
		r1 = 0;
		theta1 = Body.rotation;
		theta2 = 0;
		deltaVExpended = 0;
	
		while ((r0 >= Body.radius) && (T < MAX_TIME)) { // The main ascent. (event?)
			// 0.0049 is a magic number because stock drag is weird like that. The exact value is a best guess from observing falling bodies. Any suggestions from the FAR people and/or those who know how to use the API?
			//9.82 is another magic number. Because stock isp has a g0 like that.
			V = Math.sqrt(r1*r1 + (r0 * theta1) * (r0 * theta1)); // total velocity
			// orbitalSpeed = Math.sqrt(r1*r1 + (r0 * theta1) * (r0 * theta1));
			// surfaceSpeed = Math.sqrt(r1*r1 + r0*r0*(theta1-Body.rotation)*(theta1-Body.rotation));
			thrust = ascentProfile.throttle(Mass)*Craft.thrust;
			dM = dT*thrust/(Craft.isp(Body.rho(r0))*9.82);  // Mass flow per timestep.
			if ((Mass - dM) < Craft.massDry) {
				dM = Mass-Craft.massDry; // Not enough fuel!
				thrust = dM*Craft.isp(Body.rho(r0))*9.82; // thrust reduced to actual fuel use.
			};
			Mass -= dM;
			r2 = r0*theta1*theta1 - Body.GM/r0/r0 - 0.0049*Body.rho(r0)*Craft.Cd*V*r1 + thrust*Math.cos(ascentProfile.gamma)/Mass;
			theta2 = (thrust*Math.sin(ascentProfile.gamma)/Mass - 2*r1*theta1 - 0.0049*Body.rho(r0)*Craft.Cd*V*r0*(theta1-Body.rotation))/r0;
			deltaVExpended += dT*thrust/Mass;
			r0 += dT*r1 + 0.5*dT*dT*r2; // Now less braindead. But its still no 4th order RKN.
			r1 += dT*r2; // RK1 integration, more or less.
			theta1 += dT*theta2; // This seems questionable.
			T += dT; // in principle I could use variable timesteps.
			// Downrange position (theta0, etc) is not currently tracked.
			OrbitalParameters.update(r0, V);
			// Writing to log and outputting display info would go here.
			System.out.println("Time:" + T + "/" + MAX_TIME);
			System.out.println("Altitude:" + r0);
			System.out.println("Spd:" + V);
			System.out.println("Mass:" + Mass);
			System.out.println("r2:" + r2);
			System.out.println("theta2:" + theta2);
			System.out.println("r1:" + r1);
			System.out.println("theta1:" + theta1);
			System.out.println("Vh:" + r0*theta1);
			System.out.println("thrustR:" + thrust*Math.cos(ascentProfile.gamma)/Mass);
			// System.out.println("Press:" + Body.rho(r0));
			// System.out.println("isp:" + Craft.isp(Body.rho(r0)));
		}
		// And in the end...
		System.out.println("dV:" + deltaVExpended);
		System.out.println("SMA:" + OrbitalParameters.semiMajorAxis);
		System.out.println("Ecc:" + OrbitalParameters.eccentricity);
		System.out.println("Ap:" + OrbitalParameters.apoapsis);
		System.out.println("Pe:" + OrbitalParameters.periapsis);
		// cleanup, run another ascent?
	}
}
	
