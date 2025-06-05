from rest_framework.permissions import BasePermission

from src.apps.onlyoffice.utils import OnlyOfficeJWT


class OnlyOfficePermission(BasePermission):
    message = "Invalid or missing ONLYOFFICE JWT token"

    def has_permission(self, request, view):
        auth_header = request.headers.get("Authorization")
        if not auth_header:
            return False

        try:
            token_type, token = auth_header.split()
            if token_type.lower() != "bearer":
                return False
        except ValueError:
            return False

        payload = OnlyOfficeJWT.verify_token(token)
        if not payload:
            return False

        return True
