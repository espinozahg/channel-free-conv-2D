
# EXECUTE USING:
# python3 calc-velocity-profile-exact.py

# based on 1972-aung-devel
# Developing laminar free convection between vertical flat plates with asymmetric heating

from globalDefs import *

#nelem = 4
#nelem = 80
nelem = 128

for i in range(nelem+1):
   Y = float(i)/float(nelem)
   U = (r_T - 1.0)*(Y**3)/6.0 - r_T*(Y**2)/2.0 + (2.0*r_T + 1)*Y/6.0
   print(Y,"   ",U)

# generates output to stdout, then copy and paste to file

exit




