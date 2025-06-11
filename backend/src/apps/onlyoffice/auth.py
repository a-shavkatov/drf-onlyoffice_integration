from rest_framework import authentication
from rest_framework import exceptions

from src.apps.onlyoffice.utils import OnlyOfficeJWT


class OnlyOfficeAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get("AuthorizationJwt")
        if not auth_header:
            raise exceptions.AuthenticationFailed("Authorization header not found")

        try:
            token_type, token = auth_header.split()
            if token_type.lower() != "bearer":
                raise exceptions.AuthenticationFailed("Invalid token type")
        except ValueError:
            raise exceptions.AuthenticationFailed("Invalid token format")

        payload = OnlyOfficeJWT.verify_token(token)
        if not payload:
            raise exceptions.AuthenticationFailed("Invalid token")

        return (None, payload)

    def authenticate_header(self, request):
        return "Bearer"
