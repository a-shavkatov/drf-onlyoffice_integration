from rest_framework import routers
from django.urls import path, include

from .document import DocumentViewSet
from .template import TemplateViewSet

router = routers.DefaultRouter()
router.register(r"document", DocumentViewSet, basename="document")
router.register(r"template", TemplateViewSet, basename="template")

urlpatterns = [path("", include(router.urls))]
