
# EXECUTE USING:
# python3 globalDefs.py

# based on 1972-aung-devel
# Developing laminar free convection between vertical flat plates with asymmetric heating

import math

#myStep="264" # myNx=2
#myStep="500" # myNx=4
#myStep="1500" # myNx=8
myStep="3000" # myNx=16

b = 0.005
l = 1.5

T_1 = 42.5 + 273.15
T_2 = 37.5 + 273.15
T_0 = 30.0 + 273.15

bar_T = (T_1 + T_2)/2.0

print("bar_T: ",bar_T)

T_prop = (bar_T + T_0)/2.0

print("T_prop: ",T_prop)

# Air at T_0=30 C
rho0 = 1.164

# Air at 35C
mu = 1.895E-5
Pr = 0.7268

k = 0.02625
c_p = 1007.0
nu = 1.655E-5

alpha = 2.277E-5
rho = 1.145
beta = 0.003245

g = 9.8

# Pr = c_p mu / k


Gr = g * beta * (T_1 - T_0) * b**4 / (l * nu**2) 
print("Gr: ",Gr)


r_T = (T_2 - T_0) / (T_1 - T_0)
print("r_T: ",r_T)


bar_Delta_T = (T_1 - T_0) * (1.0 + r_T)/2.0
print("bar_Delta_T: ",bar_Delta_T)


bar_Gr = Gr * (1.0 + r_T)/2.0
print("bar_Gr: ",bar_Gr)

bar_L = 1.0/bar_Gr
print("bar_L: ",bar_L)


bar_Ra = Pr * bar_Gr
print("bar_Ra: ",bar_Ra)


# for fully developed flow:
bar_M = 1.0/12.0

# obtained using calc-sym.py
Umax = (3*r_T - math.sqrt(3*r_T**2 + 3*r_T + 3))*((-6*r_T - math.sqrt(3*r_T**2 + 3*r_T + 3))*(3*r_T - math.sqrt(3*r_T**2 + 3*r_T + 3)) + 9*(r_T - 1)*(2*r_T + 1))/(162*(r_T - 1)**2)
Ymax = (r_T - math.sqrt(3*r_T**2 + 3*r_T + 3)/3)/(r_T - 1)

print("Ymax: ",Ymax)
print("Umax: ",Umax)

# 1972-aung-devel   eq. 4a 
umax = Umax*l*nu*Gr/(b**2)
print("umax: ",umax)






