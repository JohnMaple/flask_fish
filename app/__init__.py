"""
Created by Alex
Desc: 创建核心app对象
"""
from flask import Flask


def create_app():
    app = Flask(__name__)

    # 开启调试模式1
    # app.debug = True

    # 导入配置文件,就可以使用
    app.config.from_object('config')
    register_blueprint(app)

    return app


def register_blueprint(app):
    from app import web
    app.register_blueprint(web)


