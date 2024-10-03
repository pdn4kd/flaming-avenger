# flaming-avenger various KSP scripts
Raptop Ascent Program

An ascent simulator for testing designs in Kerbal Space Program 0.10.1 - 0.90. This program is explicitly not bug-compatible with the Unity implimentation (for starters this uses spherical coordinates instead of rectangular), but is nonetheless usefully accurate.


Stage split

finding how to distribute tankage between 2 stages, if you know the other parameters (engines, payload, miscellanious bits) of a rocket. Analytic, but finicky. Given actual KSP parts, upper stages will tend towards low TWR. This may be acceptable for larger landers, but is not useful in carrier rockets.

MJ profile
Graphs out example mechjeb ascent profiles in terms of altitude vs angle. These are explicitly using the classic ascent mode, so others can be very different.
In this mode, there's a start altitude, an end altitude, and a shape (goes from 0 to 1). The actual ascent also has a minimum velocity to start the turn. Lower shape numbers result in later/sharper turns, while higher ones in smoother/more gradual turns.
The actual ascent program also has circularization and apoapsis adjustment features that are not considered.

Engines, Early Engines
sketching out performance options (in terms of acceleration vs Δv) for various engine and payload combinations.
