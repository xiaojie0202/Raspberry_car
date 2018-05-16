# -*- coding:utf-8 -*-
# 超声波模块
import random
# import RPi.GPIO as GPIO

class Ulttrasonic(object):

    def __init__(self):
        pass

    def rotate_left(self):
        print('超声波模块选址至左边')
        pass

    def rotate_middle(self):
        print('超声波模块旋转至中间')

    def rotate_right(self):
        print('超声波模块旋转至右方')

    def rotate_stop(self):
        print('超声波模块停止')

    def ranging(self):
        return random.randint(0,100)