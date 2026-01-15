
# EXECUTE USING:
# python3 calc-velocity-profile-numeric.py

# based on 1972-aung-devel
# Developing laminar free convection between vertical flat plates with asymmetric heating


# imports globalDefs.py
#import globalDefs
from globalDefs import *


# 
myFileName = "postProcessing/velocityProfile/" + myStep + "/line.xy"
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
   u = float(data[2])
   #X = x/(l*Gr)
   Y = y/b
   U = (b**2)*u/(l*nu*Gr)
   #print(y,u)
   print(Y,"   ",U)


# generates output to stdout, then copy and paste to file

exit()




