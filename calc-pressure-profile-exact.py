
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
   P = 0.7
   print(Y,"   ",P)

# generates output to stdout, then copy and paste to file

exit




