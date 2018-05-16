# -*- coding:utf-8 -*-
# import RPi.GPIO as GPIO
import time
# 马达模块

class Move(object):
    '''
    控制小车移动
    '''
    def __init__(self, speed):
        # self.left_1A = 1
        # self.left_1B = 2
        # self.left_EN = 0  # A通道A
        #
        # self.right_1A = 3
        # self.right_1B = 4
        # self.right_EN = 5  # 通道B
        self.speed = self.get_speed(speed)
        self.set_up()

    def set_up(self):
        # 初始化函数
        # GPIO.setmode(GPIO.BCM)
        # GPIO.setwarnings(False)
        #
        # GPIO.setup(self.left_1A, GPIO.OUT)
        # GPIO.setup(self.left_1B, GPIO.OUT)
        # GPIO.setup(self.left_EN, GPIO.OUT)
        # GPIO.setup(self.right_1A, GPIO.OUT)
        # GPIO.setup(self.right_1B, GPIO.OUT)
        # GPIO.setup(self.right_EN, GPIO.OUT)
        #
        # self.motorR = GPIO.PWM(self.right_EN, 100)
        # self.motorL = GPIO.PWM(self.left_EN, 100)
        # self.move_stop()
        pass


    def get_speed(self, speed):
        # 初始化小车速度，防止发生异常
        if speed < 25:
            return 25
        elif speed > 100:
            return 100
        else:
            return speed

    def initStart(self):
        # self.motorL.start(0)
        # self.motorR.start(0)
        pass

    def move_up(self):
        # 前进
        # self.initStart()
        # self.motorR.ChangeDutyCycle(self.speed)
        # self.motorL.ChangeDutyCycle(self.speed)
        # GPIO.output(self.left_1A, GPIO.HIGH)
        # GPIO.output(self.left_1B, GPIO.LOW)
        # GPIO.output(self.right_1A, GPIO.HIGH)
        # GPIO.output(self.right_1B, GPIO.LOW)
        print('小车前进')

    def move_down(self):
        # 后退
        # self.initStart()
        # self.motorR.ChangeDutyCycle(self.speed)
        # self.motorL.ChangeDutyCycle(self.speed)
        # GPIO.output(self.left_1A, GPIO.LOW)
        # GPIO.output(self.left_1B, GPIO.HIGH)
        # GPIO.output(self.right_1A, GPIO.LOW)
        # GPIO.output(self.right_1B, GPIO.HIGH)
        print('小车后退')

    def move_left(self):
        #左转
        # self.initStart()
        # self.motorR.ChangeDutyCycle(self.speed)
        # self.motorL.ChangeDutyCycle(self.speed)
        # GPIO.output(self.left_1A, GPIO.LOW)
        # GPIO.output(self.left_1B, GPIO.HIGH)
        # GPIO.output(self.right_1A, GPIO.HIGH)
        # GPIO.output(self.right_1B, GPIO.LOW)
        print('小车左转')

    def move_right(self):
        #右转
        # self.initStart()
        # self.motorR.ChangeDutyCycle(self.speed)
        # self.motorL.ChangeDutyCycle(self.speed)
        # GPIO.output(self.left_1A, GPIO.HIGH)
        # GPIO.output(self.left_1B, GPIO.LOW)
        # GPIO.output(self.right_1A, GPIO.LOW)
        # GPIO.output(self.right_1B, GPIO.HIGH)
        print('小车右转')

    def move_stop(self):
        #停止
        # self.motorR.ChangeDutyCycle(0)
        # self.motorL.ChangeDutyCycle(0)
        # GPIO.output(self.left_1A, False)
        # GPIO.output(self.left_1B, False)
        # GPIO.output(self.right_1A, False)
        # GPIO.output(self.right_1B, False)
        print('小车停止')

    def add_speed(self):
        self.speed = self.get_speed(self.speed+25)
        print('增加小车移动速度')

    def sub_speed(self):
        self.speed = self.get_speed(self.speed-25)
        print('降低小车移动速度')


if __name__ == '__main__':
    a = Move(100)
    a.move_up()
    time.sleep(10)
    a.move_stop()
