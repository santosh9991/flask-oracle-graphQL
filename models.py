from sqlalchemy import *
from sqlalchemy.orm import (scoped_session, sessionmaker, relationship,
                            backref)
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('oracle://santosh:oracle@127.0.0.1:1521/xe', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
# We will need this for querying
Base.query = db_session.query_property()
class CustomerModel(Base):
    __tablename__ = 'demo_customers'
    customer_id = Column(Integer,primary_key=True)
    cust_first_name = Column(Unicode)
    cust_last_name = Column(Unicode)
class OrderModel(Base):
    __tablename__ = 'demo_orders'
    order_id = Column('order_id',Integer,primary_key=True)
    order_total = Column('order_total',Float)
    customer_id = Column(Integer, ForeignKey('demo_customers.customer_id'))
    customer = relationship(
        CustomerModel,
        backref = backref('demo_customers',
                    uselist = True,
                    cascade = 'delete,all'))
