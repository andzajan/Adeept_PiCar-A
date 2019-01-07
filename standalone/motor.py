#!/usr/bin/env python
# File name   : motor.py
# Description : Control Motor
# Author      : Modified version of original Adeept code
# Date        : 2019/01/07

import RPi.GPIO as GPIO
import time
import curses
# motor_pwn_A: Pin7  |  motor_pwn_B: Pin11
# motor_A:  Pin8,Pin10    |  motor_B: Pin13,Pin12

Motor_A_EN    = 7
Motor_B_EN    = 11

Motor_A_Pin1  = 10
Motor_A_Pin2  = 8
Motor_B_Pin1  = 12
Motor_B_Pin2  = 13

Dir_forward   = 1
Dir_backward  = 0

#pwm_A = 0
#pwm_B = 0

def motorStop():#Motor stops
	GPIO.output(Motor_A_Pin1, GPIO.LOW)
	GPIO.output(Motor_A_Pin2, GPIO.LOW)
	GPIO.output(Motor_B_Pin1, GPIO.LOW)
	GPIO.output(Motor_B_Pin2, GPIO.LOW)
	GPIO.output(Motor_A_EN, GPIO.LOW)
	GPIO.output(Motor_B_EN, GPIO.LOW)

def setup():#Motor initialization
	global pwm_A, pwm_B
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(Motor_A_EN, GPIO.OUT)
	GPIO.setup(Motor_B_EN, GPIO.OUT)
	GPIO.setup(Motor_A_Pin1, GPIO.OUT)
	GPIO.setup(Motor_A_Pin2, GPIO.OUT)
	GPIO.setup(Motor_B_Pin1, GPIO.OUT)
	GPIO.setup(Motor_B_Pin2, GPIO.OUT)

	motorStop()
	pwm_A = GPIO.PWM(Motor_A_EN, 5000)
	pwm_B = GPIO.PWM(Motor_B_EN, 5000)

def motorB(direction, speed=100):#Motor 2, forward and reverse rotation

	global  pwm_B
	if direction == Dir_forward:
		GPIO.output(Motor_B_Pin1, GPIO.HIGH)
		GPIO.output(Motor_B_Pin2, GPIO.LOW)
		pwm_B.start(100)
		pwm_B.ChangeDutyCycle(speed)

	elif direction == Dir_backward:
		GPIO.output(Motor_B_Pin1, GPIO.LOW)
		GPIO.output(Motor_B_Pin2, GPIO.HIGH)
		pwm_B.start(0)
		pwm_B.ChangeDutyCycle(speed)

def motorA(direction, speed=100):#Motor 1 forward and reverse rotation
	global pwm_A
	if direction == Dir_forward:#
		GPIO.output(Motor_A_Pin1, GPIO.HIGH)
		GPIO.output(Motor_A_Pin2, GPIO.LOW)
		pwm_A.start(0)
		pwm_A.ChangeDutyCycle(speed)
	elif direction == Dir_backward:
		GPIO.output(Motor_A_Pin1, GPIO.LOW)
		GPIO.output(Motor_A_Pin2, GPIO.HIGH)
		pwm_A.start(0)
		pwm_A.ChangeDutyCycle(speed)

def robot_forward(speed=100):
	motorA (direction=Dir_forward, speed=speed)
	motorB (direction=Dir_forward, speed=speed)


def robot_backward(speed=100):
	motorA (direction=Dir_backward, speed=speed)
	motorB (direction=Dir_backward, speed=speed)


def robot_left(speed=100):
	motorA (direction=Dir_forward, speed=speed)
	motorB (direction=Dir_backward, speed=speed)

def robot_right(speed=100):
	motorA (direction=Dir_backward, speed=speed)
	motorB (direction=Dir_forward, speed=speed)

def destroy():
	motorStop()
	GPIO.cleanup()             # Release resource

try:
#		motorA (direction=Dir_backward, speed=100)
#		motorB (direction=Dir_backward, speed=100)
#		time.sleep(2)
#		motorStop()
#		motorA (direction=Dir_forward, speed=100)
#		time.sleep(2)
#		motorStop()
#		destroy()
	pass
except KeyboardInterrupt:
	destroy()


