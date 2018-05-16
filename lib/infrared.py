# -*- coding:utf-8 -*-
import random

class Infrared(object):

    def __init__(self):
        pass

    def getInfo(self):
        # [上左， 上右，下左， 下右]
        list = [random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1)]
        return list