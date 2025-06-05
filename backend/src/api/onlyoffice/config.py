from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated

from src.apps.documentation.models import Document
from src.apps.onlyoffice.serializers import ConfigSerializer


class ConfigViewSet(GenericViewSet, RetrieveModelMixin):
    permission_classes = [IsAuthenticated]
    queryset = Document.objects.all()
    serializer_class = ConfigSerializer

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
