# Finding the amount of propellant to split between 2 stages to maximize dV.
# TWR limits are *not* considered, nor is Isp changing with stage split time.
# Analytic in principle, but the algebra is... bleah.
# May 21, 2015

from math import sqrt

# craft stats
# example craft is a 0.90 Shamash-derived carrier rocket.
# For T = 27 FL-T100s, and P = 0.9, x = 0.37
# For T = 26 FL-T100s, and P = 1.2, x = 0.42
E1 = 0.5
E2 = 1.25
V1 = 9.82*390
V2 = 9.82*360
T = 27*0.0625
S = 0.05
P = 0.9 #11/26 t100s for 1.2, 10/27 t100s for 0.9
R = 9

# a,b,c Yes, it's a glorified quadratic equation.
a = -V2*T*T*R*(R-1)
b = T*(E1+P)*(V1*(R-1)*(R-1)-V2*(R+1)*(R-1))
c = V1*(R-1)*(E1+P)*(E1+E2+T+P+S)-V2*(R-1)*(E1+P)*(E1+P)

# x = ...
print((-b-sqrt(b*b-4*a*c))/(2*a))
print((-b+sqrt(b*b-4*a*c))/(2*a))
