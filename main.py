#!/usr/bin/env python

# -*- coding: utf-8 -*-
#用于规定字符编码，想要中文正常最好就加上这句

import tornado.options
from tornado import web,ioloop,httpserver
from tornado.log import app_log
from tornado.options import define, options

from conf.config import SETTING
from router import HANDLERS

define("port", default=8002, type=int)
#定义监听的端口，随便挑个喜欢的数字吧

class Application(web.Application):
    def __init__(self):
        handlers = HANDLERS
        settings = SETTING
        tornado.web.Application.__init__(self, handlers, **settings)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = httpserver.HTTPServer(Application())
    app_log.info('Listen port %s......' % tornado.options.options.port)
    http_server.listen(options.port)
    ioloop.IOLoop.instance().start()