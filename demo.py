import script.movement as mv
import time
from script.calibrationVariables import *

# dps = float(input("DPS TO CHECK -> "))
# angle = float(input("ANGLE -> "))

try:
    # mv.turnInPlace(50, 500)
    mv.completeMaze()
    
    
except KeyboardInterrupt:
    print("pressed ctrl+c")
    mv.allStop()