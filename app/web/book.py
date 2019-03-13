"""
Created by Alex
"""
from flask import jsonify, Blueprint
from helper import is_isbn_or_key
from yushu_book import YuShuBook

# 引入蓝图
web = Blueprint('web', __name__)


@web.route('/book/search/<q>/<page>')
def search(q, page):
    """
    搜索isbn或关键词
    :param q:
    :param page:
    :return:
    """
    isbn_or_key = is_isbn_or_key(q)

    result = YuShuBook.search_by_isbn(q) if isbn_or_key == 'isbn' else YuShuBook.search_by_keyword(q)

    return jsonify(result)
    # return json.dumps(result), 200, {'content-type': 'application/json'}
