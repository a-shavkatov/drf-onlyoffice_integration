import jwt

from django.utils import timezone
from django.conf import settings


class OnlyOfficeJWT:
    jwt_secret = settings.ONLYOFFICE_CONFIG["JWT_SECRET"]
    algorithm = settings.ONLYOFFICE_CONFIG["JWT_ALGORITHM"]

    @classmethod
    def generate_token(cls, payload: dict) -> str:
        expires_at = timezone.localtime() + settings.ONLYOFFICE_CONFIG["JWT_EXPIRE_AT"]
        token_data = {**payload, "exp": expires_at, "iat": timezone.localtime()}

        return jwt.encode(token_data, cls.jwt_secret, algorithm=cls.algorithm)

    @classmethod
    def verify_token(cls, token: str) -> dict | None:
        try:
            return jwt.decode(
                token,
                cls.jwt_secret,
                algorithms=[cls.algorithm],
                options={"verify_iat": False},
            )
        except jwt.InvalidTokenError as e:
            return None
