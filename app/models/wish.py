
from app.models.base import Base, db
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, func, desc
from sqlalchemy.orm import relationship

from app.spider.yushu_book import YuShuBook


class Wish(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))    # user是relationships返回的对象
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
    def get_user_wishes(cls, uid):
        gifts = Wish.query.filter_by(uid=uid, launched=False).order_by(desc(Wish.create_time)).all()
        return gifts

    @classmethod
    def get_gifts_counts(cls, isbn_list):
        from app.models.gift import Gift
        # filter 条件表达式，filter_by 关键字参数
        count_list = db.session.query(func.count(Gift.id), Gift.isbn).filter(Gift.launched == False,
                                                                             Gift.isbn.in_(isbn_list),
                                                                             Gift.status == 1).group_by(Gift.isbn).all()
        count_list = [{'count': w[0], 'isbn': w[1]} for w in count_list]

        return count_list







