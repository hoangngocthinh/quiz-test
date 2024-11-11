from rest_framework.exceptions import APIException
from rest_framework import status


class ObjectNotFoundException(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = "The requested object does not exist."
    default_code = "object_not_found"
