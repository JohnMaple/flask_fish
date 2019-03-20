"""
Created by Alex
"""
import os

DEBUG = True

SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:root@localhost:3306/fisher'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_COMMIT_TEARDOWN = True

# SCERET_KEY = os.urandom(24)   # 适合开发使用
SECRET_KEY = '\xda\x92b\x83\x17\xb5[!oy1\x08\xc6\xcc+\xba\xbb4\x1b\x9a\xbbr\xea\x80'

# Email 配置
MAIL_SERVER = 'smtp.163.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USE_TSL = False
MAIL_USERNAME = 'feng934879001@163.com'
MAIL_PASSWORD = 'chaqhh3116004048'
MAIL_SUBJECT_PREFIX = '[鱼书]'
MAIL_SENDER = '鱼书 <hello@yushu.im>'



