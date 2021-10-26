import bcrypt
import jwt


class AuthService:
    def __init__(self):
        return

    @staticmethod
    def login_with_email(email, password):
        from api.user.models import User
        database_user: User = User.query.filter_by(email=email).first()
        if database_user :
            result = bcrypt.checkpw(password.encode('utf8'), database_user.password.encode('utf8'))
            if result:
                return AuthService.login(database_user.id), 200
            else:
                return {"message": "UnAuthorized"}, 401
        else:
            return {"message": "User Not Found"}, 404

    @staticmethod
    def login(user_id: int):
        payload = {'sub': user_id}
        return jwt.encode({"token": payload}, "secret", algorithm="HS256")

    @staticmethod
    def signup(user):
        from api.user.models import User
        from api.comparelt import db
        database_user = User.query.filter_by(email=user['email']).first()
        if database_user:
            return {"message": "Duplicated user"}, 409
        hashed_password = bcrypt.hashpw(user['password'].encode("utf8"), bcrypt.gensalt())  # save password
        user = User(user['username'], user['email'], hashed_password.decode('utf8'))
        db.session.add(user)
        db.session.commit()
        return {"message": "Success"}, 200
