from sqlalchemy import Column, Integer, String, create_engine, Boolean, Float
from sqlalchemy.engine.base import Engine
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base

import scrape_products.scrape_products.settings as settings

DeclarativeBase = declarative_base()


def db_connect() -> Engine:
    return create_engine(URL(**settings.DATABASE))


def create_items_table(engine: Engine):
    DeclarativeBase.metadata.create_all(engine)


class Items(DeclarativeBase):
    __tablename__ = "items"
    id = Column("id", Integer)
    name = Column(String, primary_key=False)
    name_modified = Column(String, primary_key=True)
    link = Column(String)

    category = Column(String)
    category_id = Column(Integer)

    last_price = Column(Integer)
    last_cost_per_weight = Column(Float)

    weight = Column(Integer)

    producer = Column(String)
    kkal = Column(Integer)
    rating = Column(Integer)
    is_available = Column(Boolean)

class CostHistory(DeclarativeBase):
    __tablename__ = "cost_history"
    product_id = Column("id", Integer)
    date = Column(String, primary_key=False)
    cost = Column(Integer)
