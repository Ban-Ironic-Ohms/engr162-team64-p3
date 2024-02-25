import script.movement as mv
import time
from script.calibrationVariables import *

turn_dps = 250

target_angle = float(input("What angle would you like to turn to -> "))

try:
    mv.turnInPlace(target_angle, turn_dps)
except KeyboardInterrupt:
    mv.allStop()