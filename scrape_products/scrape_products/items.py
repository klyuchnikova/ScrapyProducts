# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import MapCompose
from w3lib.html import remove_tags


def extract_rating(rating_span_classes):
    rating_classes = rating_span_classes.split()
    for cls in rating_classes:
        if cls.startswith("xf-product-rating__visual--"):
            return cls[-1]
    return "none"


class ScrapeProductsItem(scrapy.Item):
    name = scrapy.Field(input_processor=MapCompose(remove_tags))
    link = scrapy.Field()
    category = scrapy.Field(input_processor=MapCompose(remove_tags))
    category_id = scrapy.Field()
    price = scrapy.Field(input_processor=MapCompose(remove_tags))
    
    kkal = scrapy.Field()
    producer = scrapy.Field()

    rating = scrapy.Field(input_processor=MapCompose(remove_tags, extract_rating))
