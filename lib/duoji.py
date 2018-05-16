# -*- coding:utf-8 -*-
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup()
GPIO.input()
GPIO.wait_for_edge()
GPIO.add_event_detect()
GPIO.cleanup()
