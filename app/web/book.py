"""
Created by Alex
"""
import json

from flask import jsonify, request, flash, render_template, url_for
from flask_login import current_user

from app.froms.book import SearchForm
from app.libs.helper import is_isbn_or_key
from app.models.gift import Gift
from app.models.wish import Wish
from app.spider.yushu_book import YuShuBook
from app.view_models.book import BookCollection, BookViewModel
from app.view_models.trade import TradeInfo
from . import web


# 引入蓝图
# web = Blueprint('web', __name__)


# @web.route('/book/search/<q>/<page>')
# def search(q, page):
#     """
#     搜索isbn或关键词
#     :param q:
#     :param page:
#     :return:
#     """
#     isbn_or_key = is_isbn_or_key(q)
#
#     result = YuShuBook.search_by_isbn(q) if isbn_or_key == 'isbn' else YuShuBook.search_by_keyword(q)
#
#     return jsonify(result)
#     # return json.dumps(result), 200, {'content-type': 'application/json'}


@web.route('/book/search')
def search():
    """
    搜索isbn或关键词
    """
    # 使用request获取参数
    # q = request.args['q']
    # page = request.args['page']

    # 验证层，引用验证类
    form = SearchForm(request.args)
    books = BookCollection()

    if form.validate():
        # 从form里面获取参数
        q = form.q.data.strip()
        page = form.page.data

        isbn_or_key = is_isbn_or_key(q)

        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(q) if isbn_or_key == 'isbn' else yushu_book.search_by_keyword(q, page)
        books.fill(yushu_book, q)

    else:
        flash('搜索格式错误，请重新输入')
        # return jsonify(form.errors)

    return render_template('search_result.html', books=books)

    # return json.dumps(books, default=lambda obj: obj.__dict__)
    # return jsonify(result)
    # return json.dumps(result), 200, {'content-type': 'application/json'}


@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    """
            1. 当书籍既不在心愿清单也不在礼物清单时，显示礼物清单
            2. 当书籍在心愿清单时，显示礼物清单
            3. 当书籍在礼物清单时，显示心愿清单
            4. 一本书要防止即在礼物清单，又在赠送清单，这种情况是不符合逻辑的

            这个视图函数不可以直接用cache缓存，因为不同的用户看到的视图不一样
            优化是一个逐步迭代的过程，建议在优化的初期，只缓存那些和用户无关的“公共数据"
    """
    has_in_gifts = False
    has_in_wishes = False

    yushu_book = YuShuBook()
    yushu_book.search_by_isbn(isbn)

    book = BookViewModel(yushu_book.first)

    # 判断是否登录
    if current_user.is_authenticated:
        # 如果未登录，current_user将是一个匿名用户对象
        if Gift.query.filter_by(uid=current_user.id, isbn=isbn,
                                launched=False).first():
            has_in_gifts = True
        if Wish.query.filter_by(uid=current_user.id, isbn=isbn,
                                launched=False).first():
            has_in_wishes = True

    # 取交易的数据
    trade_gifts = Gift.query.filter_by(isbn=isbn, launched=False).all()
    trade_wishes = Wish.query.filter_by(isbn=isbn, launched=False).all()

    trade_gifts_model = TradeInfo(trade_gifts)
    trade_wishes_model = TradeInfo(trade_wishes)

    return render_template('book_detail.html', book=book, wishes=trade_wishes_model, gifts=trade_gifts_model, has_in_wishes=has_in_wishes, has_in_gifts=has_in_gifts)


