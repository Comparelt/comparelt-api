from flask_restx import Resource

from ..service.crawling_service import CrawlingService
from ..util.dto import CrawlingDto

api = CrawlingDto.api
crawled_product = CrawlingDto.crawling


@api.route('/<string:product_title>')
class CrawlProduct(Resource):
    @api.doc('Crawl Product')
    def get(self, product_title):
        return CrawlingService.crawl(product_title)