from typing import Dict, Tuple

import bcrypt

from app.main import db
from app.main.model.user import User


class UserService:
    @staticmethod
    def save_new_user(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
        user = User.query.filter_by(email=data['email']).first()
        if not user:
            hashed_password = bcrypt.hashpw(data['password'].encode("utf8"), bcrypt.gensalt())
            new_user = User(
                email=data['email'],
                username=data['username'],
                hashed_password=hashed_password,
            )
            UserService.save_changes(new_user)
            return UserService.generate_token(new_user)
        else:
            response_object = {
                'status': 'fail',
                'message': 'User already exists. Please Log in.',
            }
            return response_object, 409

    @staticmethod
    def get_all_users():
        return User.query.all()

    @staticmethod
    def get_a_user(public_id):
        return User.query.filter_by(public_id=public_id).first()

    @staticmethod
    def generate_token(user: User) -> Tuple[Dict[str, str], int]:
        try:
            # generate the auth token
            auth_token = User.encode_auth_token(user.id)
            response_object = {
                'status': 'success',
                'message': 'Successfully register.',
                'Authorization': auth_token.decode('utf-8')
            }
            return response_object, 201
        except Exception as e:
            print(e)
            response_object = {
                'status': 'fail',
                'message': 'Error occurred. Try again.'
            }
            return response_object, 401

    def save_changes(self: User):
        db.session.add(self)
        db.session.commit()
