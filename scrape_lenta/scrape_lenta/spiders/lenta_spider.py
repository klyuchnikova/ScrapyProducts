from scrape_lenta.items import ScrapeProductsItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader

# scrapy crawl vprok_web -O vprok.json


class VprokSpider(CrawlSpider):
    name = "lenta_web"
    allowed_domains = ["lenta.com"]
    start_urls = ["https://lenta.com/"]
    start_urls = ["https://www.vprok.ru/"]
    rules = [
        Rule(LinkExtractor(allow='product', callback='parse_item'))
    ]

    def parse_item(self, response):
        MAIN_UI_ID = '#ui-id-1'

        CLASS_PRODUCT = '.xf-product'
        CLASS_RATING_SCROLL = 'sku-page__commenter-rating-overview-stars js-sku-page-commenter-rating-overview-stars'
        # data-rating = float number
        CLASS_NAME_TAG = "sku-page__title" # h1 with text
        CLASS_PRICE_LABEL = "price-label"  # might be a few instances, like +regular class
        CLASS_PRICE_LABEL_REGUALR = "price-label--regular"
        CLASS_PRICE_LABEL_PRIMARY = "price-label--primary"
        CLASS_PRICE_NUMBERS = ["price-label__integer", "price-label__fraction"]

        CLASS_PARAMETER_TABLE = "sku-card-tab-params__group" #-> sku-card-tab-params__item
        CLASS_PARAMETER_ITEM = "sku-card-tab-params__item"
        CLASS_PARAMETER_NAME = "sku-card-tab-params__label"
        CLASS_PARAMETER_VALUE = "sku-card-tab-params__value"

        ATTRIBUTE_NAME = 'sku-page__title'
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
