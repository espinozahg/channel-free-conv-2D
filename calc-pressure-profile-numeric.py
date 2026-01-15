
# EXECUTE USING:
# python3 calc-pressure-profile-numeric.py

# based on 1972-aung-devel
# Developing laminar free convection between vertical flat plates with asymmetric heating


# imports globalDefs.py
#import globalDefs
from globalDefs import *


# 
myFileName = "postProcessing/pressureProfile/" + myStep + "/line.xy"
print("myFileName",myFileName)

myFile = open(myFileName,'r')

# skip first line
next(myFile)

for line in myFile:
   #print(line)
   data = line.strip().split()
   #print(data)
   # y in aung notation is my x
   y = float(data[0])
   p = float(data[1])
   #X = x/(l*Gr)
   Y = y/b
   P = (p - p0)*b*b*b*b/(rho*l*l*nu*nu*Gr*Gr)
   #print(y,p)
   print(Y,"   ",P)


# generates output to stdout, then copy and paste to file

exit()




