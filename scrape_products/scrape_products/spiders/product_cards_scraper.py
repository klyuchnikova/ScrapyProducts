import scrapy
from scrape_products.items import ScrapeProductsItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader

# scrapy crawl all_vprok_products -O vprok_products.json

class VprokCatalogSpider(CrawlSpider):
    name = "all_vprok_products"
    start_urls = ["https://www.vprok.ru/"]
    rules = [
        Rule(LinkExtractor(allow = 'product', callback = 'parse_item'))
    ]

    def parse_item(self, response):
        MAIN_UI_ID = '#ui-id-1'

        CLASS_PRODUCT = '.xf-product'
        CLASS_RATING_SCROLL = 'xf-product-new__rating  js-link-scroll'
        # inside <ul> -> number of <li> with class = "xf-product-new__rating__star._active" is the rating
        # right after <a> xf-card-action__text with text which is the number of ratings
        CLASS_NAME_TAG = "xf-product-new__title js-product__title js-product-new-title"
        CLASS_PRICE_ROUBLE = "js-price-rouble" # span with text, might be a few, take first


        ATTRIBUTE_NAME = 'data-owox-product-name'
        ATTRIBUTE_LINK = 'data-product-card-url'
        ATTRIBUTE_CATEGORY_NAME = 'data-owox-category-name'
        ATTRIBUTE_CATEGORY_ID = 'data-owox-category-id'
        ATTRIBUTE_PRICE = 'data-owox-product-price data-owox-price'
        ATTRIBUTE_NUMBER_RATINGS = 'data-owox-points'
        ATTRIBUTE_AVAILABLE = 'data-owox-is-available'

        dict_field_attribute = {'name': ATTRIBUTE_NAME,
                                'link': ATTRIBUTE_LINK,
                                'category': ATTRIBUTE_CATEGORY_NAME,
                                'category_id': ATTRIBUTE_CATEGORY_ID,
                                'price': ATTRIBUTE_PRICE}

        for product_card in response.css(MAIN_UI_ID):
            if product_card.css(f"::attr({ATTRIBUTE_AVAILABLE})") == "1":
                i_loader = ItemLoader(item=ScrapeProductsItem(), selector=product_card)
                for field_name, attr_name in dict_field_attribute.items():
                    i_loader.add_css(field_name, f"::attr({attr_name})")
                i_loader.add_css('rating', "span.xf-product-rating__visual::attr(class)")
                yield i_loader.load_item()
