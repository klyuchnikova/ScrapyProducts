# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from itemloaders.processors import MapCompose
from scrapy import Field, Item
from w3lib.html import remove_tags


def extract_rating(rating_span_classes):
    rating_classes = rating_span_classes.split()
    for cls in rating_classes:
        if cls.startswith("xf-product-rating__visual--"):
            return cls[-1]
    return "none"


class ScrapeProductsItem(Item):
    name = Field(input_processor=MapCompose(remove_tags))
    link = Field()
    category = Field(input_processor=MapCompose(remove_tags))
    category_id = Field()
    price = Field(input_processor=MapCompose(remove_tags))

    kkal = Field()
    producer = Field()

    rating = Field(input_processor=MapCompose(remove_tags, extract_rating))
