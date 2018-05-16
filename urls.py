# -*- coding:utf-8 -*-
from tornado.web import url
from handlers import IndexHandler, MoveHandler, GetInfo, VideoHandler

urls = [
    url(r'^/$', IndexHandler, name='index'),
    url(r'/api/move', MoveHandler, name='move'),
    url(r'/api/getinfo', GetInfo, name='getinfo'),
    url(r'/video', VideoHandler, name='video')
]