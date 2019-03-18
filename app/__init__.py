"""
Created by Alex
Desc: 创建核心app对象
"""
from flask import Flask
from app.models.base import db
from flask_login import LoginManager


login_manager = LoginManager()


def register_blueprint(app):
    from app.web import web
    app.register_blueprint(web)


def create_app():
    app = Flask(__name__)

    # 开启调试模式1
    # app.debug = True

    # 导入配置文件,就可以使用
    # app.config.from_object('config')
    app.config.from_object('app.secure')
    app.config.from_object('app.settings')
    register_blueprint(app)

    db.init_app(app)
    db.create_all(app=app)
    login_manager.init_app(app)
    login_manager.login_view = 'web.login'  # 把endpoint赋值给login_view
    login_manager.login_message = '请先登录或注册'

    return app



