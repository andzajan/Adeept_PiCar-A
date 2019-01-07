#!/usr/bin/env python
# File name   : motor.py
# Description : Motor keyboard controls
# Author      :
# Date        : 2019/01/07

import RPi.GPIO as GPIO
import time
import curses
import motor

actions = {
    curses.KEY_UP:    motor.robot_forward,
    curses.KEY_DOWN:  motor.robot_backward,
    curses.KEY_BACKSPACE: motor.destroy,
    curses.KEY_LEFT:  motor.robot_left,
    curses.KEY_RIGHT: motor.robot_right,
    }

def main(window):
    motor.setup()
    next_key = None
    while True:
        curses.halfdelay(1)
        if next_key is None:
            key = window.getch()
        else:
            key = next_key
            next_key = None
        if key != -1:
            # KEY DOWN
            curses.halfdelay(3)
            action = actions.get(key)
            if action is not None:
                action()
            next_key = key
            while next_key == key:
                next_key = window.getch()
            # KEY UP
            motor.motorStop()

curses.wrapper(main)
