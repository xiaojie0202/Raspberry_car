# -*- coding:utf-8 -*-
import os
import subprocess
import re
import random

class Humiture():
    def __init__(self,dht_pin=23):
        '''
        :param dht_pin: DHT22 温湿度传感器的BCM编号的针脚
        '''
        self.dht_pin = dht_pin
        self.temperature = None
        self.humidity = None

    def get_info(self):
        # while True:
        #     try:
        #         temp = subprocess.check_output(['sudo', '/home/pi/pycode/DHT22/dht', '22', str(self.dht_pin)]).decode('utf-8')
        #     except:
        #         continue
        #     else:
        #         if temp.find('Hum') == -1:
        #             continue
        #         else:
        #             temp = temp.split('=')
        #             wendu = re.findall(r'\d+.\d+', temp[1])
        #             shidu = re.findall(r'\d+.\d+', temp[2])
        #             self.temperature = float(wendu[0])
        #             self.humidity = float(shidu[0])
        #             break
        # return {'temperature': self.temperature,'humidity': self.humidity}
        return {'temperature': random.randint(0, 100), 'humidity': random.randint(0, 100)}