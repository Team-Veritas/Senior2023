#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.nxtdevices import*
from module_line import go_line
from module_stop import *
from step_1 import *
from step_2 import *
ev3 = EV3Brick()
left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor= Motor(Port.D,  Direction.COUNTERCLOCKWISE)
left_arm = Motor(Port.C)
right_arm = Motor(Port.B)

color_1 = LightSensor(Port.S1)
color_2 = LightSensor(Port.S4)
# color_3 = ColorSensor(Port.S)


def step_2():
    # go_line(80, 250)
    # robot_stop("brake")
    drive = DriveBase(left_motor,right_motor, 56, 162)

    drive.settings(736, 1000, 736,1000) ##전진
    drive.straight(-250)
    drive.turn(90)
    drive.stop()
    go_line(80, 2600)
    robot_stop("brake")