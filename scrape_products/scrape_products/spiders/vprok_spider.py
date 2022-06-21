import scrapy


class VprokSpider(scrapy.Spider):
    name = "vprok_web"
    start_urls = ["https://www.vprok.ru/"]

    def parse(self, response, **kwargs):
        PROMO_CLASS = '.xf-product.xf-product--promo.js-product'
        CARD_CLASS = "xfnew-semiblocks__carousel-card.tns-item.tns-slide-active"
        PRODUCT_CLASS = '.xf-product'

        ATTRIBUTE_NAME = 'data-owox-product-name'
        for brickset in response.css(PRODUCT_CLASS):
            NAME_SELECTOR = 'h1 ::text'
            PIECES_SELECTOR = './/dl[dt/text() = "Pieces"]/dd/a/text()'
            MINIFIGS_SELECTOR = './/dl[dt/text() = "Minifigs"]/dd[2]/a/text()'
            IMAGE_SELECTOR = 'img ::attr(src)'
            yield {
                'name': brickset.attrib[ATTRIBUTE_NAME]
            }
