
# EXECUTE USING:
# python3 calc-temperature-profile-exact.py

# based on 1972-aung-devel
# Developing laminar free convection between vertical flat plates with asymmetric heating

from globalDefs import *

#nelem = 4
#nelem = 80
nelem = 128

for i in range(nelem+1):
   Y = float(i)/float(nelem)
   theta = (1.0-r_T)*Y +r_T
   print(Y,"   ",theta)

# generates output to stdout, then copy and paste to file

exit




