#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.nxtdevices import*

# from robot_move import *
# from step_1 import step_1


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor= Motor(Port.D,  Direction.COUNTERCLOCKWISE)
left_arm = Motor(Port.C)
right_arm = Motor(Port.B)

color_1 = LightSensor(Port.S1)
color_2 = LightSensor(Port.S4)

def go_line(speed, degrees):

    # PID 상수 정의
    Kp = 0.5
    Ki = 0.002
    Kd = 2

    # 오차 변수 초기화
    error = 0
    last_error = 0
    integral = 0

    # 메인 루프 정의
    left_motor.reset_angle(0)
    right_motor.reset_angle(0)
    
    while (abs(right_motor.angle()) + abs(left_motor.angle())) / 2 < degrees:
        # 센서 값을 읽기
        left_value = color_1.reflection()
        right_value = color_2.reflection()
        
        # 오차 계산
        error = left_value - right_value
        
        # 비례 항 계산
        proportional = Kp * error
        
        # 적분 항 계산
        integral += Ki * error
        
        # 미분 항 계산
        derivative = Kd * (error - last_error)
        last_error = error
        
        # PID 출력 값 계산
        pid_output = int(proportional + integral + derivative)
        
        # PID 출력 값을 이용하여 모터 속도 설정
        left_speed = speed + pid_output
        right_speed = speed - pid_output
        left_motor.dc(left_speed)
        right_motor.dc(right_speed)