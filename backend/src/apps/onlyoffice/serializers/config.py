from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.apps.documentation.models import Document
    from src.apps.user.models import User

from rest_framework import serializers
from django.conf import settings

from src.apps.onlyoffice.utils import OnlyOfficeJWT
from src.apps.services.minio.utils import get_file_presigned_url


class ConfigSerializer(serializers.Serializer):
    documentType = serializers.CharField(read_only=True)
    document = serializers.DictField(read_only=True)
    editorConfig = serializers.DictField(read_only=True)
    type = serializers.CharField(read_only=True)
    token = serializers.CharField(read_only=True)

    @staticmethod
    def _get_permissions(user: "User", document: "Document"):
        return {
            "delete": user.is_superuser | user.id == document.owner_id,
            "edit": user.is_superuser | user.id == document.owner_id,
            "review": user.is_superuser | user.id == document.owner_id,
        }

    def to_representation(self, instance: "Document"):
        request = self.context["request"]
        user: "User" = request.user

        permissions = self._get_permissions(user, instance)

        callback_url = f"{settings.SITE_URL}/api/callback/"

        payload = {
            "documentType": "word",
            "type": "desktop",
            "document": {
                "fileType": "docx",
                "key": str(instance.key),
                "title": instance.title,
                "url": get_file_presigned_url(instance.file.name),
                "version": instance.version,
            },
            "editorConfig": {
                "callbackUrl": callback_url,
                "mode": "edit" if permissions["edit"] else "view",
                "lang": "ru",
                "user": {
                    "id": user.id,
                    "name": f"{user.firstname} {user.lastname}",
                    "permissions": permissions,
                },
                "customization": {
                    "about": False,  # Показывать кнопку "О программе"
                    "feedback": False,  # Показывать кнопку "Обратная связь"
                    "forcesave": True,  # Принудительное сохранение
                    "goback": True,  # Показывать кнопку "Назад"
                    "chat": False,  # Включить чат
                    "comments": False,  # Включить комментарии
                    "zoom": 100,  # Масштаб по умолчанию
                    "compactHeader": False,  # Компактная шапка
                    "leftMenu": True,  # Показывать левое меню
                    "rightMenu": True,  # Показывать правое меню
                    "toolbar": True,  # Показывать панель инструментов
                    "header": True,  # Показывать заголовок
                    "autosave": True,  # Автосохранение
                    "review": False,  # Включить режим рецензирования
                },
                "recent": {"enable": False},  # Недавние файлы
                "templates": {"enable": False},  # Шаблоны документов
            },
        }

        token = OnlyOfficeJWT.generate_token(payload)
        payload["token"] = token

        return payload
