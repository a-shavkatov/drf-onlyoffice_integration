from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from src.apps.user.serializers import UserLoginSerializer


class UserViewSet(GenericViewSet):
    serializer_class = UserLoginSerializer

    @action(detail=False, methods=["post"])
    def login(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.create(serializer.validated_data)

        return Response(data, status=status.HTTP_200_OK)
