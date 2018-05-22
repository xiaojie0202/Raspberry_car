# -*- coding:utf-8 -*-
from tornado.web import RequestHandler
from tornado.websocket import WebSocketHandler
from lib.car_move import car_move
from lib import ultrasonic
from lib.camera_move import camera_move
from lib.dth22 import dth22
from lib import infrared
import json
import time


class IndexHandler(RequestHandler):

    def get(self, *args, **kwargs):
        self.render('index.html')


# 控制小车，摄像头，超声波，移动
class MoveHandler(RequestHandler):

    def __init__(self, *args, **kwargs):
        print('访问过来了')
        self.car_move = car = car_move.Move(100)  # 实例化控制小车移动的类
        # 小车的控制方法
        self.car_move_dict = {'up': self.car_move.move_up,
                              'left': self.car_move.move_left,
                              'right': self.car_move.move_right,
                              'down': self.car_move.move_down,
                              'stop': self.car_move.move_stop,
                              'add': self.car_move.add_speed,
                              'sub': self.car_move.sub_speed}

        self.camera_move = camera_move
        # 摄像头移动对应的方法
        self.camera_move_dict = {
            'up': self.camera_move.rate_up,
            'left': self.camera_move.rate_left,
            'right': self.camera_move.rate_right,
            'down': self.camera_move.rate_down,
            'stop': self.camera_move.rate_stop}

        self.ultrasonic = ultrasonic.Ulttrasonic()  # 实例化超声波模块
        # 超声波模块转动对应的方法
        self.ultrasonic_dict = {'left': self.ultrasonic.rotate_left, 'middle': self.ultrasonic.rotate_middle, 'right': self.ultrasonic.rotate_right, 'stop': self.ultrasonic.rotate_stop}

        # 对各个模块的功能进行编号
        self.module_fun_dict = {
            1: self.car_move_dict,
            2: self.camera_move_dict,
            3: self.ultrasonic_dict}
        super(MoveHandler, self).__init__(*args, **kwargs)

    def post(self, *args, **kwargs):
        # 要求前端传入的数据是 {'module':1, 'motion':'up'}
        # 1 控制小车移动
        # 2 摄像头移动
        # 3 超声波模块转动
        module = int(self.get_argument('module', 0))
        motion = self.get_argument('motion', None)
        if module in list(self.module_fun_dict.keys()) and motion:
            self.module_fun_dict.get(module).get(motion)()
            self.write(json.dumps({'status': True}))
        else:
            self.write(json.dumps({'status': False}))

# 用于获取红外传感器，超声波传感器，温度湿度
class GetInfo(WebSocketHandler):

    def __init__(self, application, request, **kwargs):
        super(GetInfo, self).__init__(application, request, **kwargs)
        self.ultrasonic = ultrasonic.Ulttrasonic()  # 实例化超声波模块
        self.dth22 = dth22
        self.infrared = infrared.Infrared()

    def open(self, *args, **kwargs):

        print('客户端连接过来了')

    def on_message(self, message):
        # 数据格式 {'ultrasonic':'45, "infrared":[0, 0 ,0, 0], 'temperature':'12', 'humidness':'11'}
        data_dict = self.dth22.get_info() # 温度湿度
        data_dict['ultrasonic'] = self.ultrasonic.ranging() # 超声波距离
        data_dict['hongwai'] = self.infrared.getInfo() # 红外线
        self.write_message(json.dumps(data_dict))

    def check_origin(self, origin):
        # 是否允许跨域请求
        return True

class VideoHandler(RequestHandler):

    def get(self, *args, **kwargs):
        self.redirect('http://192.168.2.109:4455/?action=stream')



'''
websocket
红外
超声波
温度  湿度
'''
