
# EXECUTE USING:
# python3 calc-sym.py

# based on 1972-aung-devel
# Developing laminar free convection between vertical flat plates with asymmetric heating

import sympy as sym

from globalDefs import r_T as r_T_n

#r_T_n = 0.6

r_T = sym.Symbol('r_T')
Y = sym.Symbol('Y')
#U = sym.Symbol('U')

U = (r_T - 1)*(Y**3)/6 - r_T*(Y**2)/2 + (2*r_T + 1)*Y/6
print("U: ",U)

dUdY = sym.diff(U, Y)
print("dUdY: ",dUdY)

#sol = sym.solveset(dUdY, Y)
sol = sym.solve(dUdY, Y)

print("sol: ",sol)

sol1 = sol[0]
#sol2 = sol[1]
print("sol1: ",sol1)
#print("sol2: ",sol2)

#s1 = sym.N(sol.subs(r_T,r_T_n))
sol1_n = sym.N(sol1.subs(r_T,r_T_n))
#sol2_n = sym.N(sol2.subs(r_T,r_T_n))

print("sol1_n: ",sol1_n)
#print("sol2_n: ",sol2_n)

Umax = U.subs(Y,sol1)
Umax = sym.simplify(Umax)

print("Umax: ",Umax)

Umax_n = Umax.subs(r_T,r_T_n)
print("Umax_n: ",Umax_n)


exit




