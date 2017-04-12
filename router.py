# -*- coding:utf-8 -*- 
# --------------------
# Author:		Ken
# Description:	路由
# --------------------

from modules.admin.controller import (MainHandler,BlogHandler)

HANDLERS = [
    (r"/", MainHandler.MainHandler),
    (r"/blog", BlogHandler.BlogHandler),
]

        