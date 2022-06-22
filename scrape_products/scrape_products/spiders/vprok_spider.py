import scrapy
from scrape_products.scrape_products.items import ScrapeProductsItem


class VprokSpider(scrapy.Spider):
    name = "vprok_web"
    start_urls = ["https://www.vprok.ru/"]

    def parse(self, response, **kwargs):
        CLASS_PRODUCT = '.xf-product'
        CLASS_PROMO = '.xf-product--promo.js-product'
        CLASS_CARD = "xfnew-semiblocks__carousel-card.tns-item.tns-slide-active"

        ATTRIBUTE_NAME = 'data-owox-product-name'
        ATTRIBUTE_LINK = 'data-product-card-url'
        ATTRIBUTE_CATEGORY_ID = 'data-owox-category-id'
        ATTRIBUTE_CATEGORY_NAME = 'data-owox-category-name'
        ATTRIBUTE_AVAILABLE = 'data-owox-is-available'

        item = ScrapeProductsItem()
        for brickset in response.css(CLASS_PRODUCT):
            NAME_SELECTOR = 'h1 ::text'
            PIECES_SELECTOR = './/dl[dt/text() = "Pieces"]/dd/a/text()'
            MINIFIGS_SELECTOR = './/dl[dt/text() = "Minifigs"]/dd[2]/a/text()'
            IMAGE_SELECTOR = 'img ::attr(src)'
            item['name'] = brickset.attrib[ATTRIBUTE_NAME]
            yield item
