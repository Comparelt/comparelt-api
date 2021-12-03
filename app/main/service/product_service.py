from app.main import db
from app.main.model.product import Product


class ProductService:
    def __init__(self):
        return

    @staticmethod
    def findWithTitle(product_title):
        return Product.query.filter_by(title=product_title).all(), 200

    @staticmethod
    def addProduct(title, picture, link, price):
        product = Product(title=title, picture=picture, link=link, price=price)
        db.session.add(product)
        db.session.commit()
        return product

    @staticmethod
    def loadProduct():
        return Product.query.all()

        # if products:
        #     # output = jsonify(Product=[product.serialize() for product in products])
        #     # output = ''
        #     # for product in products:
        #     #     output = output+product
        #
        #     # json_string = json.dumps([product  for product in products])
        #     # data = json.load(json_string)
        #     data = []
        #     for product in products:
        #         data.append(product.serialize())
        #     # jsonify(products.serialize())
        #
        #     # output = json.dumps(products.serialize())
        #     return data
        # return False

    @staticmethod
    def loadProductData(product_title):
        product = Product.query.filter_by(title=product_title).first()

        if product:
            return product.serialize()
        return False
