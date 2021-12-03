from .. import db
import datetime

from ..util.ORMModel import ORMModel


class ExpiredToken(ORMModel):
    __tablename__ = 'expired_tokens'

    # declare Token Table Columns
    token = db.Column(db.String(500), unique=True, nullable=False)
    expired_on = db.Column(db.DateTime, nullable=False)

    def __init__(self, token, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.token = token
        self.expired_on = datetime.datetime.now()

    def __repr__(self):
        return '<id: token: {}'.format(self.token)

    @staticmethod
    def check_expire(auth_token: str) -> bool:
        res = ExpiredToken.query.filter_by(token=str(auth_token)).first()
        if res:
            return True
        else:
            return False
