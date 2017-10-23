from sqlalchemy import Table, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from pyzza.database import Base

class Topping(Base):
    __tablename__ = 'topping'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    orders = relationship('Order', back_populates='topping')

    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return '<Topping %r>' % (self.name)

class Size(Base):
    __tablename__ = 'size'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    orders = relationship('Order', back_populates='size')

    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return '<Size %r>' % (self.name)

class Order(Base):
    __tablename__ = 'pizza_order'
    id = Column(Integer, primary_key=True)
    size_id = Column('id_size', Integer, ForeignKey('size.id'))
    size = relationship('Size', back_populates='orders')
    topping_id = Column('id_topping', Integer, ForeignKey('topping.id'))
    topping = relationship('Topping', back_populates='orders')

    def __init__(self, size=None):
        self.size = size

    def __repr__(self):
        return '<Order %r, %r>' % (self.size, self.topping)
