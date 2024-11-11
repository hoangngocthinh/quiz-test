from core.exceptions import ServiceUnavailable


class AuthenticateException(ServiceUnavailable):
    default_code = 0o100

    def __init__(self, message=None):
        self.detail = message or "Email or password incorrect!."
