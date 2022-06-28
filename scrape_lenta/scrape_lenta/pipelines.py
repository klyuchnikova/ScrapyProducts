# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from sqlalchemy.orm import sessionmaker
from models import Items, CostHistory, create_items_table, db_connect

class ScrapePipeline:
    def __init__(self):
        engine = db_connect()
        create_items_table(engine)
        self.Session = sessionmaker(bind = engine)

    def process_item(self, item , spider):
        session = self.Session()
        instance = session.query(Items).filter_by(**item).one_or_none()
        if instance:
            return instance
        product_item = Items(**item)
        try:
            session.add(product_item)
            session.commit()
        except:
            session.rollback()
            raise Exception("couldn't add item to the database")
        finally:
            session.close()
        return item