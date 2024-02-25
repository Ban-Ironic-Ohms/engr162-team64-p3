from script.MPU9250 import MPU9250
import grovepi
import time

L_US_PORT = 8
R_US_PORT = 3
F_US_PORT = 2

grovepi.set_bus("RPI_1")
mpu9250 = MPU9250()


def queryHeading():
    data = mpu9250.readGyro()
    print(data)
    return data['x']

def queryLUS():
    try:
        # Read distance value from Ultrasonic
        data = grovepi.ultrasonicRead(L_US_PORT)
        # print(f"LEFT ultrasonic reading: {data}")
        return data

    except Exception as e:
        print ("Error:{}".format(e))
    
def queryRUS():
    try:
        # Read distance value from Ultrasonic
        data = grovepi.ultrasonicRead(R_US_PORT)
        # print(f"RIGHT ultrasonic reading: {data}")
        return data

    except Exception as e:
        print ("Error:{}".format(e))
    
def queryFUS():
    try:
        # Read distance value from Ultrasonic
        data = grovepi.ultrasonicRead(F_US_PORT)
        print(f"FRONT ultrasonic reading: {data}")
        return data

    except Exception as e:
        print ("Error:{}".format(e))