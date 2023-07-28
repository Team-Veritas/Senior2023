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


ev3 = EV3Brick()
left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor= Motor(Port.D,  Direction.COUNTERCLOCKWISE)
left_arm = Motor(Port.C)
right_arm = Motor(Port.B)

color_1 = LightSensor(Port.S1)
color_2 = LightSensor(Port.S4)

def step_1():
    drive = DriveBase(left_motor,right_motor, 56, 162)

    drive.settings(736, 1000, 736,1000) ##전진
    drive.straight(110)
    drive.stop()

    go_line(80,300) ##라인
    robot_stop("brake")

    drive.settings(100, 300, 736,1000) ##배 박치기
    drive.straight(170)
    drive.stop()
    robot_stop("stop")
    wait(300)

    drive.settings(736, 1000, 736,1000) ## 돌아가기
    drive.straight(-168)
    drive.stop()
    robot_stop("brake")
    wait(300)

    left_motor.run_angle(700, 530)## 돌아간다
    robot_stop("brake")
    right_motor.run_angle(700, 528)
    robot_stop("brake")

    drive.settings(736, 1000, 736,1000)## 젼진한다
    drive.straight(260)
    drive.stop()
    robot_stop("brake")

    drive = DriveBase(left_motor,right_motor, 56, 162)
    drive.settings(736, 800, 500,800)
    drive.turn(90)
    drive.stop()
    robot_stop("brake")
    drive.settings(400, 1000, 736,1000)
    drive.straight(-100)
    drive.stop()
    robot_stop("brake")
    right_arm.run_time(-700,550) ##배 먹기
    right_arm.hold()
    wait(400)
    drive.settings(736, 1000, 736,1000)
    drive.straight(-190)
    drive.stop()
    robot_stop("brake")
    wait(200)
    drive.settings(736, 1000, 736,1000)
    drive.straight(400)
    drive.stop()
    robot_stop("brake")
    drive.settings(736, 800, 500, 800)
    drive.turn(90)
    drive.stop()
    robot_stop("brake")
    wait(400)
    drive.settings(736, 1000, 736,1000)
    drive.straight(309)
    drive.stop()
    robot_stop("brake")
    drive.settings(736, 800, 500, 800)
    drive.turn(-90)
    drive.stop()
    robot_stop("brake")
    go_line(80,2800) ##라인
    robot_stop("brake")

    drive.settings(736, 1000, 736,1000) ##전진
    drive.straight(135)
    drive.stop()
    robot_stop("brake")
    wait(400)

    drive.settings(736, 1000, 736, 1000)
    drive.turn(-92)
    drive.stop()
    robot_stop("brake")
    wait(400)
    right_arm.run_time(700,450)
    right_arm.brake()
    wait(400)
    drive.settings(736, 1000, 736,1000) ##전진
    drive.straight(-323)
    drive.stop()
    robot_stop("brake")



    drive.settings(736, 1000, 736,1000) ##전진
    drive.straight(150)
    drive.stop()
    robot_stop("brake")

    