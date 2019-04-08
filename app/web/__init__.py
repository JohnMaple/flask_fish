"""
Created by Alex
"""
from flask import Blueprint, render_template

web = Blueprint('web', __name__)

from app.web import book, auth, drift, gift, main, wish


@web.app_errorhandler(404)
def not_found(e):
    """
    可以实现各种业务，如：把e异常里面的错误信息添加到日志里面
    基于aop思想（面向切片编程）
    :param e:
    :return:
    """
    return render_template('404.html'), 404

