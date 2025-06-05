from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from src.apps.documentation.models import Document
from src.apps.documentation.serializers import (
    DocumentCreateSerializer,
    DocumentListSerializer,
)


class DocumentViewSet(GenericViewSet, CreateModelMixin, ListModelMixin):
    permission_classes = [IsAuthenticated]
    queryset = Document.objects.all()

    def get_serializer_class(self):
        serializer_mapping = {
            "create": DocumentCreateSerializer,
            "list": DocumentListSerializer,
        }
        return serializer_mapping[self.action]
