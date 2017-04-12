# -*- coding:utf-8 -*- 
# --------------------
# Author:       SDN
# Description:	连接数据库
# Time:         2017/3/1
# --------------------

from tornmq import Connection
from config.config import USER, PASSWORD, PORT, HOST, DATABASE

# 连接MySQL数据库
msql = Connection(user=USER, password=PASSWORD, port=PORT, host=HOST, database=DATABASE)
