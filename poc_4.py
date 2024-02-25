import script.movement as mv
import time
from script.calibrationVariables import *

x1 = float(input("x -> "))
y1 = float(input("y -> "))

x2 = float(input("x -> "))
y2 = float(input("y -> "))

x3 = float(input("x -> "))
y3 = float(input("y -> "))

x4 = float(input("x -> "))
y4 = float(input("y -> "))

try:
    mv.navigate(x1, y1)
    input("CONTINUE?")

    mv.navigate(x2, y2)
    input("CONTINUE?")
    
    mv.navigate(x3, y3)
    input("CONTINUE?")
    
    mv.navigate(x4, y4)
    input("CONTINUE?")

except KeyboardInterrupt:
    mv.allStop()