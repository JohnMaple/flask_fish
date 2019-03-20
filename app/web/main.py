from flask import render_template

from app.models.gift import Gift
from . import web


__author__ = '七月'


@web.route('/')
def index():
    recent_gifts = Gift.recent()
    return render_template('index.html', recent=recent_gifts)


@web.route('/personal')
def personal_center():
    pass
