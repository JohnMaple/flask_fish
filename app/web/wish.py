from flask import flash, redirect, url_for
from flask_login import login_required, current_user

from app.models.base import db
from app.models.wish import Wish
from . import web

__author__ = '七月'


@web.route('/my/wish')
def my_wish():
    pass


@web.route('/wish/book/<isbn>')
@login_required
def save_to_wish(isbn):
    if current_user.can_save_to_list(isbn):

        with db.auto_commit():
            gift = Wish()
            gift.isbn = isbn
            gift.uid = current_user.id

            db.session.add(gift)
    else:
        flash('这本书已添加至你的赠送清单或已存在于你的心愿清单，请不要重复添加')

    return redirect(url_for('web.book_detail', isbn=isbn))


@web.route('/satisfy/wish/<int:wid>')
def satisfy_wish(wid):
    pass


@web.route('/wish/book/<isbn>/redraw')
def redraw_from_wish(isbn):
    pass