from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response

from src.apps.onlyoffice.serializers import CallBackSerializer
from src.apps.onlyoffice.auth import OnlyOfficeAuthentication


class CallbackViewSet(GenericViewSet, CreateModelMixin):
    authentication_classes = [OnlyOfficeAuthentication]
    serializer_class = CallBackSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)
