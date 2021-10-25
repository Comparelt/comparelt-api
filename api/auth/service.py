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
            result = bcrypt.checkpw(password, database_user.password.encode())
            if result:
                return AuthService.login(database_user.id), 200
            else:
                return {"message": "UnAuthorized"}, 401
        else:
            return {"message": "User Not Found"}, 404

    @staticmethod
    def login(user_id):
        payload = {'sub': user_id}
        return jwt.encode({"token": payload}, "secret", algorithm="HS256")

    @staticmethod
    def signup(user):
        from api.user.models import User
        (User.username, User.email, User.password) = user
        database_user = User.query.filter_by(email=user.email).first()
        if database_user:
            return {"message": "Duplicated user"}, 409
        hashed_password = bcrypt.hashpw(user.password.encode("utf-8"), bcrypt.gensalt())  # save password
        user = (User.username, User.email, hashed_password)
        User.session.add(user)
        User.session.commit()
        signed_user_id = user.id
        return AuthService.login(signed_user_id), {"message": "Success"}, 200
