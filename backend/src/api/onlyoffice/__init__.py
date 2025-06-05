from rest_framework import routers
from django.urls import path, include


from .callback import CallbackViewSet
from .config import ConfigViewSet


router = routers.DefaultRouter()
router.register(r"callback", CallbackViewSet, basename="callback")
router.register(r"config", ConfigViewSet, basename="config")

urlpatterns = [path("", include(router.urls))]
