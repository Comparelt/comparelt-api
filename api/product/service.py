class ProductService:
    def __init__(self):
        return

    @staticmethod
    def findWithTitle(item):
        from api.product import models
        return models.Product.query.filter_by(title=item).all()
