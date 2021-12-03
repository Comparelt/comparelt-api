from app.main import db

from typing import Dict, Tuple

from app.main.model.expire_token import ExpiredToken


class ExpireService:
    @staticmethod
    def save_token(token: str) -> Tuple[Dict[str, str], int]:
        expired_token = ExpiredToken(token=token)
        try:
            db.session.add(expired_token)
            db.session.commit()
            response_object = {
                'status': 'success',
                'message': 'Successfully logged out.'
            }
            return response_object, 200
        except Exception as e:
            response_object = {
                'status': 'fail',
                'message': e
            }
            return response_object, 200
