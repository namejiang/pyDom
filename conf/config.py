# -*- coding:utf-8 -*- 
# --------------------
# Author:       
# Description:	各种路径
# Time:         2017/3/16
# --------------------

import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
TEMPLATE_PATH = os.path.join(BASE_DIR, "templates")  # 模板目录
STATIC_PATH = os.path.join(BASE_DIR, "static")  # 静态资源目录

# MYSQL配置
MYSQL_HOST = 'localhost'
MYSQL_PORT = 27017
MYSQL_USER = "admin"
MYSQL_PASSWORD = "admin"
MYSQL_DATABASE = "admin"

# Application
SETTING = dict(
    template_path=TEMPLATE_PATH,
    static_path=STATIC_PATH,
    debug=True,
)