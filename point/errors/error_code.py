from fastapi import status

from .base import ErrorCodeBase


class ErrorCode(ErrorCodeBase):
    INVALID_AUTH_SCHEME = "Invalid authentication scheme.", status.HTTP_401_UNAUTHORIZED
    INVALID_TOKEN = "Invalid token or expired token.", status.HTTP_401_UNAUTHORIZED
    INVALID_AUTH_CODE = "Invalid authorization code.", status.HTTP_401_UNAUTHORIZED

    ACCESS_FORBIDDEN = "Access forbidden.", status.HTTP_403_FORBIDDEN
