from api import db
from api.common.ORMModel import ORMModel


class Product(ORMModel):
    __tablename__ = 'product'

    # declare Product Table Columns
    title = db.Column(db.String())
    picture = db.Column(db.String())
    link = db.Column(db.String())
    price = db.Column(db.String())

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'title': self.title,
            'picture': self.picture,
            'link':  self.link,
            'price': self.price,
        }