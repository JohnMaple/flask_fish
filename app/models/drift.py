"""
Created by Alex
"""
from app.libs.enums import PendingStatus
from app.models.base import Base
from sqlalchemy import Column, Integer, String, SmallInteger


class Drift(Base):
    """
        一次具体的交易信息
    """
    __tablename__ = 'drift'

    def __init__(self):
        self.pending = PendingStatus.Waiting
        super(Drift, self).__init__()

    id = Column(Integer, primary_key=True)

    # 邮寄信息
    recipient_name = Column(String(20), nullable=False, comment='接收者')
    address = Column(String(100), nullable=False, comment='地址')
    message = Column(String(200), comment='留言')
    mobile = Column(String(20), nullable=False, comment='手机号')

    # 书籍信息
    isbn = Column(String(13), comment='isbn')
    book_title = Column(String(50), comment='书籍名称')
    book_author = Column(String(30), comment='作者')
    book_img = Column(String(50), comment='书籍封面')

    # 请求者信息
    # requester_id = Column(Integer, ForeignKey('user.id'))
    # requester = relationship('User')
    requester_id = Column(Integer, comment='请求者id')
    requester_nickname = Column(String(20), comment='请求者名称')

    # 赠送者信息
    gifter_id = Column(Integer, comment='赠送者id')
    gift_id = Column(Integer, comment='礼物的id')
    gifter_nickname = Column(String(20), comment='赠送者名称')
    _pending = Column('pending', SmallInteger, default=1)
    # gift_id = Column(Integer, ForeignKey('gift.id'))
    # gift = relationship('Gift')

    @property
    def pending(self):
        return PendingStatus(self._pending)

    @pending.setter
    def pending(self, status):
        self._pending = status.value



