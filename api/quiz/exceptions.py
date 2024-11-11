from core.exceptions import ServiceUnavailable


class QuizException(ServiceUnavailable):
    default_code = 0o100

    def __init__(self, message=None):
        self.detail = message or "Something went wrong!."
