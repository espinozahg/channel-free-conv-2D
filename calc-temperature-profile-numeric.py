
# EXECUTE USING:
# python3 calc-temperature-profile-numeric.py

# based on 1972-aung-devel
# Developing laminar free convection between vertical flat plates with asymmetric heating


# imports globalDefs.py
#import globalDefs
from globalDefs import *


# 
myFileName = "postProcessing/temperatureProfile/" + myStep + "/line.xy"
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
   T = float(data[1])
   #X = x/(l*Gr)
   Y = y/b
   theta = (T - T_0)/(T_1 - T_0)
   #print(y,T)
   print(Y,theta)


# generates output to stdout, then copy and paste to file

exit()




