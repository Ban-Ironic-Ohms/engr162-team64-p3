import script.movement as mv
import time
from script.calibrationVariables import *

run_dps = 250

sens = float(input("Sensitivity -> "))
speed_fac = float(input("Speed different factor -> "))
# diff_fac = float(input("What difference speed factor -> "))

try:
    mv.followPath(run_dps, sens, speed_fac)
except KeyboardInterrupt:
    mv.allStop()
    # mv.plot()