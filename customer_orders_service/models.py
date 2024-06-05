import datetime

from uuid import uuid4
from sqlalchemy import String, DateTime, Integer, Column, ForeignKey
from sqlalchemy.orm import relationship

from customer_orders_service import db


def get_uuid():
    return uuid4().hex


class User(db.Model):
    __tablename__ = 'users'

    id = Column(String(32), primary_key=True, unique=True, nullable=False)
    username = Column(String(150), unique=True, nullable=False)
    registered_on= Column(DateTime, nullable=False, default=datetime.datetime.utcnow)
    orders = relationship('Order', back_populates='customer')

    def __repr__(self):
        return f"User('{self.username}', '{self.registered_on}')"
    

class Order(db.Model):
    __tablename__ = 'orders'

    order_id = Column(String(32), primary_key=True, unique=True, nullable=False)
    item_name = Column(String(150), nullable=False)
    num_of_items = Column(Integer, nullable=False)
    created_at = Column(DateTime, nullable=False)
    user_id = Column(String(32), ForeignKey('users.id'), nullable=False)
    customer = relationship('User', back_populates='orders')

    def __init__(self, item_name, num_of_items):
        self.order_id = get_uuid()
        self.item_name = item_name
        self.num_of_items = num_of_items
        self.created_at = datetime.datetime.utcnow()

    def __repr__(self):
        return f"Order('{self.item_name}', '{self.num_of_items}', '{self.created_at}')"
