# -*- coding: utf-8 -*-
from dataclasses import dataclass
from typing import List
from datetime import datetime
from passlib.hash import pbkdf2_sha256
from sqlalchemy import (Column, ForeignKey, Integer, Float, String, Text,
                        DateTime, Table)
from sqlalchemy.orm import relationship

from backend.db.database import Base, engine


class TimestampMixin(object):
    create_at: datetime = Column(DateTime,
                                 nullable=False,
                                 default=datetime.utcnow)
    update_at: datetime = Column(DateTime, onupdate=datetime.utcnow)


# mapped classes
class User_icon(Base):
    __tablename__ = "user_icon"

    id: int = Column(Integer, primary_key=True)
    image_url: str = Column(String)
    user_id: int = Column(Integer, ForeignKey("user.id"))


class User(Base, TimestampMixin):
    __tablename__ = 'user'

    id: int = Column(Integer, primary_key=True)
    username: str = Column(String)
    password: str = Column(String)
    email: str = Column(String)
    last_login: str = Column(DateTime)

    icon: User_icon = relationship("User_icon", uselist=False, backref='user')

    items: str = relationship("Item", backref="user", lazy='select')

    def __init__(self, username, password, email, user_icon_id=None):
        self.username = username
        self.set_password(password)
        self.email = email
        self.user_icon_id = user_icon_id

    def set_password(self, password):
        self.password = pbkdf2_sha256.hash(password)

    def check_password(self, value):
        return pbkdf2_sha256.verify(self.password, value)

    def __repr__(self):
        return f"<User(username={ self.username })>"


class Item_info(Base, TimestampMixin):
    __tablename__ = "item_info"

    id: int = Column(Integer, primary_key=True)
    price: float = Column(Float)
    expiration_date: datetime = Column(DateTime)
    purchase_date: datetime = Column(DateTime)

    item_id: int = Column(Integer, ForeignKey("item.id"))
    user_id: int = Column(Integer, ForeignKey("user.id"))
    status_id: int = Column(Integer, ForeignKey('status.id'))
    inventory_location_id = Column(Integer,
                                   ForeignKey('inventory_location.id'))


class Nutrition(Base):
    __tablename__ = "nutrition"

    id: int = Column(Integer, primary_key=True)
    name: str = Column(String(25))
    value: float = Column(Float)
    unit: str = Column(String(10))

    item_id: int = Column(Integer, ForeignKey("item.id"))


class Item_image(Base):
    __tablename__ = "item_image"

    id: int = Column(Integer, primary_key=True)
    image_url: str = Column(String)

    item_id: int = Column(Integer, ForeignKey("item.id"))


class Book_property(Base):
    __tablename__ = "book_property"

    id: int = Column(Integer, primary_key=True)
    author: str = Column(String)
    publisher: str = Column(String)
    notes: str = Column(Text)

    item_id: int = Column(Integer, ForeignKey("item.id"))


class Category(Base):
    __tablename__ = "category"

    id: int = Column(Integer, primary_key=True)
    name: str = Column(String)


class Size(Base):
    __tablename__ = "size"

    id: int = Column(Integer, primary_key=True)
    indicator_name: str = Column(String)
    value: float = Column(Float)
    unit: str = Column(String)

    item_id = Column(Integer, ForeignKey('item.id'))


item_cate_association_table = Table(
    "association", Base.metadata,
    Column("item_id", Integer, ForeignKey("item.id")),
    Column("category_id", Integer, ForeignKey("category.id")))


class Item(Base):
    __tablename__ = 'item'

    id: int = Column(Integer, primary_key=True)
    name: str = Column(String)

    user_id: int = Column(Integer, ForeignKey("user.id"))

    nutritions: List[Nutrition] = relationship("Nutrition",
                                               backref='item',
                                               lazy='select')
    image: List[Item_image] = relationship("Item_image",
                                           backref='item',
                                           lazy='select')

    infos: List[Item_info] = relationship("Item_info",
                                          backref='item',
                                          lazy='select')
    book_property: Book_property = relationship("Book_property",
                                                backref='item',
                                                uselist=False)

    category: Category = relationship("Category",
                                      secondary=item_cate_association_table)
    size: List[Size] = relationship("Size", backref='item')

    def __repr__(self):
        return f"<Item(name= {self.name})>"


class Status(Base):
    """docstring for status"""
    __tablename__ = "status"

    id: int = Column(Integer, primary_key=True)
    name: str = Column(String)

    item_info = relationship('Item_info', backref='status', uselist=False)


class Inventory_location(Base):
    __tablename__ = "inventory_location"

    id: int = Column(Integer, primary_key=True)
    name: str = Column(String)
    description: str = Column(Text)
    image_url: str = Column(String)

    item_info = relationship('Item_info',
                             backref='inventory_location',
                             uselist=False)


Base.metadata.create_all(bind=engine)