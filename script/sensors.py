from __future__ import print_function # use python 3 syntax but make it compatible with python 2
from __future__ import division       # 

from script.MPU9250 import MPU9250
import grovepi
import time
import brickpi3
from script.IR_Functions import *

L_US_PORT = 8
R_US_PORT = 3
F_US_PORT = 2

# IMU
grovepi.set_bus("RPI_1")
mpu9250 = MPU9250()

# IR
IR_setup(grovepi)

def queryHeading(): # DEPRECIATED
    data = mpu9250.readGyro()
    print(data)
    return data['x']

def queryLUS():
    try:
        # Read distance value from Ultrasonic
        data = grovepi.ultrasonicRead(L_US_PORT)
        if data == 255:
            raise ValueError
        # print(f"LEFT ultrasonic reading: {data}")
        return data

    except Exception as e:
        print(f"Error:{e}")
        return 0
    
def queryRUS():
    try:
        # Read distance value from Ultrasonic
        data = grovepi.ultrasonicRead(R_US_PORT)
        if data == 255:
            raise ValueError
        # print(f"RIGHT ultrasonic reading: {data}")
        return data

    except Exception as e:
        print(f"Error:{e}")
        return 0
    
def queryFUS():
    try:
        # Read distance value from Ultrasonic
        data = grovepi.ultrasonicRead(F_US_PORT)
        if data == 255:
            raise ValueError
        # print(f"FRONT ultrasonic reading: {data}")
        return data

    except Exception as e:
        print(f"Error:{e}")
        return 0
        
        
def queryAngle():
    BP = brickpi3.BrickPi3()
    BP.set_sensor_type(BP.PORT_1, BP.SENSOR_TYPE.EV3_GYRO_ABS_DPS)

    while True:
        try:
            angle = BP.get_sensor(BP.PORT_1)[0]
            # print(angle)
            return angle
        except Exception as e:
            pass
            # print(f"waiting for angle init w/ error {e}")
        time.sleep(0.08)

def query_IR(mode=0):
    # mode 0: average of both
    # mode 1: left sensor
    # mode 2: right sensor
    try:
        [s1, s2] = IR_Read(grovepi)
        
        if mode == 0:
            return 0.5 * (s1 + s2)
        elif mode == 1:
            return s1
        elif mode == 2:
            return s2
        # print ("One = " + str(s1) + "\tTwo = " + str(s2))
        # time.sleep(.1)

    except IOError:
        print ("Error in IR sensor")
        return -1
    