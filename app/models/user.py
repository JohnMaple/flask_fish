from app.libs.helper import is_isbn_or_key
from app.models.base import Base
from sqlalchemy import Column, Integer, String, Boolean, Float
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login_manager
from app.models.gift import Gift
from app.models.wish import Wish
from app.spider.yushu_book import YuShuBook


class User(UserMixin, Base):
    # __tablename__ = 'user'
    id = Column(Integer, primary_key=True, comment='id')
    nickname = Column(String(24), nullable=False, comment='昵称')
    _password = Column('password', String(128), nullable=False, comment='密码')
    phone_number = Column(String(18), unique=True, comment='手机号')
    email = Column(String(50), unique=True, nullable=False, comment='邮箱')
    confirmed = Column(Boolean, default=False, comment='激活')
    beans = Column(Float, default=0, comment='鱼豆')
    send_counter = Column(Integer, default=0, comment='赠送次数')
    receive_counter = Column(Integer, default=0, comment='索要次数')
    wx_open_id = Column(String(50))
    wx_name = Column(String(32))

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    def check_password(self, raw):
        return check_password_hash(self._password, raw)

    def can_save_to_list(self, isbn):
        if is_isbn_or_key(isbn) != 'isbn':
            return False
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(isbn)

        if not yushu_book.first:
            return False

        # 既不在赠送清单里面，也不在心愿清单里面才能添加
        gifting = Gift.query.filter_by(uid=self.id, isbn=isbn, launched=False).first()
        wishing = Wish.query.filter_by(uid=self.id, isbn=isbn, launched=False).first()

        if not gifting and not wishing:
            return True
        else:
            return False

    # def get_id(self):
    #     """
    #     使用flask_login 必须定义get_id 方法，但是可以使用
    #     :return:
    #     """
    #     return self.id


# 使用flask-login 进行登录权限验证
@login_manager.user_loader
def get_user(uid):
    """
    模块函数
    :return:
    """
    return User.query.get(int(uid))


