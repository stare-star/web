# -*- coding: utf-8 -*-
__author__ = '七月'

SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:pass6@ip:port/web?charset=utf8'

SECRET_KEY = '\x88D\xf09\x91\x07\x98\x89\x87\x96\xa0A\xc68\xf9\xecJ:U\x17\xc5V\xbe\x8b\xef\xd7\xd8\xd3\xe6\x98*4'



# Email 配置
MAIL_SERVER = 'smtp.exmail.qq.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USE_TSL = False
MAIL_USERNAME = ''
MAIL_PASSWORD = ''
MAIL_SUBJECT_PREFIX = ''
MAIL_SENDER = ''


# 开启数据库查询性能测试
SQLALCHEMY_RECORD_QUERIES = True

# 性能测试的阀值
DATABASE_QUERY_TIMEOUT = 0.5

SQLALCHEMY_TRACK_MODIFICATIONS = True

WTF_CSRF_CHECK_DEFAULT = False

SQLALCHEMY_ECHO = True

from datetime import timedelta
REMEMBER_COOKIE_DURATION = timedelta(days=30)

PROXY_API = 'http://ip.yushu.im/get'

# PERMANENT_SESSION_LIFETIME = 3600



