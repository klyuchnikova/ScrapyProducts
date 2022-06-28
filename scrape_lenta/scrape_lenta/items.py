# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from itemloaders.processors import MapCompose
from scrapy import Field, Item
from w3lib.html import remove_tags

class ScrapeProductsItem(Item):
    name = Field(input_processor=MapCompose(remove_tags))
    link = Field()
    category = Field(input_processor=MapCompose(remove_tags))
    category_id = Field()
    price = Field(input_processor=MapCompose(remove_tags))
    kkal = Field()
    weight = Field()
    producer = Field()
    rating = Field(input_processor=MapCompose(remove_tags))
