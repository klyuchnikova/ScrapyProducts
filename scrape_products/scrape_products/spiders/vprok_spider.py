import scrapy
from scrape_products.items import ScrapeProductsItem
from scrapy.loader import ItemLoader


# scrapy crawl vprok_web -O vprok.json


class VprokSpider(scrapy.Spider):
    name = "vprok_web"
    start_urls = ["https://www.vprok.ru/"]

    def parse(self, response, **kwargs):
        CLASS_PRODUCT = '.xf-product'
        CLASS_PROMO = '.xf-product--promo.js-product'
        CLASS_CARD = "xfnew-semiblocks__carousel-card.tns-item.tns-slide-active"

        ATTRIBUTE_NAME = 'data-owox-product-name'
        ATTRIBUTE_LINK = 'data-product-card-url'
        ATTRIBUTE_CATEGORY_NAME = 'data-owox-category-name'
        ATTRIBUTE_CATEGORY_ID = 'data-owox-category-id'
        ATTRIBUTE_PRICE = 'data-owox-product-price'
        ATTRIBUTE_AVAILABLE = 'data-owox-is-available'

        dict_field_attribute = {'name': ATTRIBUTE_NAME,
                                'link': ATTRIBUTE_LINK,
                                'category': ATTRIBUTE_CATEGORY_NAME,
                                'category_id': ATTRIBUTE_CATEGORY_ID,
                                'price': ATTRIBUTE_PRICE}

        for product_card in response.css(CLASS_PRODUCT):
            i_loader = ItemLoader(item=ScrapeProductsItem(), selector=product_card)
            for field_name, attr_name in dict_field_attribute.items():
                i_loader.add_css(field_name, f"::attr({attr_name})")
            i_loader.add_css('rating', "span.xf-product-rating__visual::attr(class)")
            yield i_loader.load_item()
