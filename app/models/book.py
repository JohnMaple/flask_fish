"""
Created by Alex
"""
from app.models.base import Base
from sqlalchemy import Column, Integer, String


class Book(Base):
    id = Column(Integer, primary_key=True, autoincrement=True, comment='id')
    title = Column(String(50), nullable=False, comment='书名')
    author = Column(String(30), default='未名', comment='作者')
    binding = Column(String(20), comment='装订方式')
    publisher = Column(String(50), comment='出版社')
    price = Column(String(20), comment='价格')
    pages = Column(Integer, comment='页数')
    pubdate = Column(String(20), comment='出版日期')
    isbn = Column(String(15), nullable=False, unique=True, comment='isbn')
    summary = Column(String(1000), comment='简介')
    image = Column(String(50), comment='封面图片')



