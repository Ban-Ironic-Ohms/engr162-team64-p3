# NOTE: This file has been taken and adapted from ENGR161 Team 74 Project 3


# HEADER
# Desc: This file serves as a way for logic to control the rover. It provides 
# simple functions like forward and turn that are highly customizable (speed, 
# power, angles, etc.). It also has a function allStop() that immediatly stops
# all motors. This is most useful in the case of motors running erradically

# ---------- IMPORTS ---------- #
import time
import brickpi3
import grovepi
from script.calibrationVariables import LargeLegoMotor, SmallLegoMotor
import script.sensors as sensors
from math import atan2, degrees, sqrt
# from matplotlib import pyplot as plt

# ---------- INITIALIZATION ---------- #
BP = brickpi3.BrickPi3()

L_MOTOR_PORT = BP.PORT_B
R_MOTOR_PORT = BP.PORT_C

T_MOTOR_PORT = BP.PORT_A

all_motors = [L_MOTOR_PORT, R_MOTOR_PORT, T_MOTOR_PORT]

# ---------- GLOBAL VARIABLES ---------- #
BASE_SPEED = 20
BASE_DPS = 250

turn_state = 0

l_motor_data = []
r_motor_data = []
l_motor_data.append([BP.get_motor_encoder(L_MOTOR_PORT), time.time()])
r_motor_data.append([BP.get_motor_encoder(R_MOTOR_PORT), time.time()])

# ---------- FUNCTIONS ---------- #

# These functions run the left and right motors.      
def lf(dps):
    l_motor_data.append([BP.get_motor_encoder(L_MOTOR_PORT), time.time()])
    BP.set_motor_dps(L_MOTOR_PORT, dps)

def rf(dps):
    r_motor_data.append([BP.get_motor_encoder(R_MOTOR_PORT), time.time()])
    BP.set_motor_dps(R_MOTOR_PORT, dps)
    
# This function can either take a position (cm) for the robot to travel and/or
# a speed (cm/s) for it to travel at. Default speed is 15 cm/s
def forward(dps = BASE_DPS, dir_change = 1):
    dps = dps * dir_change # be able to switch directions

    lf(dps)
    rf(dps)

def fw(dps = BASE_DPS, dir_change = 1):
    forward(dps, dir_change)
  
def turn(dir, speed=BASE_SPEED): # defining dir=direction 0 to be straight, +1 as right and -1 as left
    # keeps a state for current turn direction so we can work relativly across multiple function calls
    global turn_state
    
    # change dir to be relative and update turn state, in place
    dir, turn_state = dir - turn_state, dir
    
def turnInPlace(angle, dps=BASE_DPS):
    # initial_angle = sensors.queryHeading()
    start_time = time.time()
    
    shift_deg_per_deg = 1.25
    angle *= shift_deg_per_deg
    
    while time.time() < start_time + (abs(angle) * (1 / LargeLegoMotor.degrees_per_sec_at_250)):
        if angle > 0:
            lf(dps)
            rf(-dps)
        else:
            lf(-dps)
            rf(dps)
        time.sleep(0.05)
    allStop()

def uncertainTurn(dps, turn_distance):
    start = time.time()
    while sensors.queryFUS() > turn_distance:
        fw(dps * 0.8)
    total_time = time.time() - start
    
    ldist = sensors.queryLUS()
    rdist = sensors.queryRUS()
    
    if rdist > ldist:
        turnInPlace(90)
    else:
        turnInPlace(-90)
    
    fw(dps * 0.8)
    time.sleep(total_time)
    allStop()
    return
    

def followPath(dps=BASE_DPS, sensitivity=1.1, speed_fac=1.1, diff_fac=0.1):
    
    aquire_distance = 40
    turn_distance = 8
    
    
    while True:
        while sensors.queryFUS() > aquire_distance:
            ldist = sensors.queryLUS()
            rdist = sensors.queryRUS()
            
            if ldist > 60000 or rdist > 60000:
                ldist = 0
                rdist = 0
                
            print(f"left: {ldist}, right: {rdist}")
            
            diff = abs(ldist - rdist)
            
            if ldist > rdist * sensitivity:
                # rf(dps * speed_fac * (diff * diff_fac))
                rf(dps * speed_fac)
                lf(dps)
            elif rdist > ldist * sensitivity:
                rf(dps)
                # lf(dps * speed_fac * (diff * diff_fac))
                lf(dps * speed_fac)
            else:
                fw(dps)

            time.sleep(0.05)
            
        uncertainTurn(dps, turn_distance)

def navigate(x, y):
    # takes distance in cm
    # code uses mm
    x *= 10
    y *= 10
    theta = degrees(atan2(x, y))
    turnInPlace(theta)
    
    dist = sqrt(x**2 + y**2)
    
    end = time.time() + dist * (1 / LargeLegoMotor.mm_per_sec_at_250)
    while time.time() < end:
        fw(BASE_DPS)
        time.sleep(0.05)

    turnInPlace(-theta)
    allStop()

# def plot():
#     l_slopes = [[(l_motor_data[ind+1][0] - ele[0]) / (l_motor_data[ind+1][1] - ele[1]), ele[1]] for ind, ele in enumerate(l_motor_data[:-1])]
#     r_slopes = [[(r_motor_data[ind+1][0] - ele[0]) / (r_motor_data[ind+1][1] - ele[1]), ele[1]] for ind, ele in enumerate(r_motor_data[:-1])]
    
#     plt.plot([i[0] for i in l_motor_data], [i[1] for i in l_motor_data])
#     plt.show()

def allStop():
    print("Stopping")    
    for port in all_motors:
        print("setting power 0")
        BP.set_motor_power(port, 0)
    
    BP.reset_all()
    return True
    
    