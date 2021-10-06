from api import db


class Product(db.Model):
    __tablename__ = 'product'

    # declare Product Table Columns
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    picture = db.Column(db.String())
    link = db.Column(db.String())
    price = db.Column(db.String())

    def __init__(self, title, picture, link, price):
        self.title = title
        self.picture = picture
        self.link = link
        self.picture = picture

    def __repr__(self):
        return '<id {}>'.format(self.name)

    def serialize(self):
        return {
            'title': self.title,
            'picture': self.picture,
            'link':  self.link,
            'price': self.price,
        }