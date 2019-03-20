from flask import current_app

from app.models.base import Base, db
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, desc, func
from sqlalchemy.orm import relationship

from app.spider.yushu_book import YuShuBook
from app.view_models.book import BookViewModel


class Gift(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))    # user是relationship返回的对象
    isbn = Column(String(15), nullable=False)
    # book = relationships('Book')
    # bid = Column(Integer, ForeignKey('book.id'))
    launched = Column(Boolean, default=False)

    @property
    def book(self):
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(self.isbn)
        return yushu_book

    @classmethod
    def recent(cls):
        gift_list = Gift.query.filter_by(launched=False).order_by(
            desc(Gift.create_time)).limit(
            current_app.config['RECENT_BOOK_PER_PAGE']).all()

        books = [BookViewModel(gift.book.first) for gift in gift_list]

        return books

    @classmethod
    def get_user_gifts(cls, uid):
        gifts = Gift.query.filter_by(uid=uid, launched=False).order_by(desc(Gift.create_time)).all()
        return gifts

    @classmethod
    def get_wish_counts(cls, isbn_list):
        from app.models.wish import Wish
        # filter 条件表达式，filter_by 关键字参数
        count_list = db.session.query(func.count(Wish.id), Wish.isbn).filter(Wish.launched == False, Wish.isbn.in_(isbn_list), Wish.status == 1).group_by(Wish.isbn).all()
        count_list = [{'count': w[0], 'isbn': w[1]} for w in count_list]

        return count_list

    def is_yourself_gift(self, uid):
        if self.uid == uid:
            return True






