from flask_restx import Namespace, Resource

Crawl = Namespace(name="Crawl", description="Crawl API")


@Crawl.route('')
class Crawler(Resource):
    def get(self):
        return {}, 200

    def post(self):
        return {}, 201