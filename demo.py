import script.movement as mv
import time
from script.calibrationVariables import *

try:
    while True:
        mv.lf(30)
        mv.rf(-30)

except KeyboardInterrupt:
    print("pressed ctrl+c")
    mv.allStop()