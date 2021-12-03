from functools import wraps
from typing import Callable

from flask import request

from app.main.service.auth_service import AuthService


def token_required(f) -> Callable:
    @wraps(f)
    def decorated(*args, **kwargs):
        data, status = AuthService.get_logged_in_user(request)
        token = data.get('data')

        if not token:
            return data, status

        return f(*args, **kwargs)

    return decorated
