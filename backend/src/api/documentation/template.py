from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin

from src.apps.documentation.models import Template
from src.apps.documentation.serializers import TemplateSerializer


class TemplateViewSet(GenericViewSet, ListModelMixin):
    permission_classes = [IsAuthenticated]
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer
