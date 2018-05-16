# -*- coding:utf-8 -*-
import tornado.web
import tornado.ioloop
import tornado.httpserver
from settings import setting
from urls import urls

app = tornado.web.Application(urls, **setting)

if __name__ == '__main__':
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(8888)
    http_server.start()
    tornado.ioloop.IOLoop.current().start()