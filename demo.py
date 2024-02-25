import script.movement as mv
import time
from script.calibrationVariables import *

dps = float(input("DPS TO CHECK -> "))

try:
    while True:
        mv.lf(dps)
        mv.rf(dps)

except KeyboardInterrupt:
    print("pressed ctrl+c")
    mv.allStop()