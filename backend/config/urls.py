"""
URL configuration for onlyoffice_integration project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from django.contrib import admin
from django.conf import settings

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

API_BASE = "api/"
urlpatterns = [path("admin/", admin.site.urls), path(API_BASE, include("src.api"))]


if settings.DEBUG:
    urlpatterns += (
        path(API_BASE + "schema/", SpectacularAPIView.as_view(), name="schema"),
    )
    urlpatterns += (
        path(
            API_BASE + "swagger/",
            SpectacularSwaggerView.as_view(url_name="schema"),
            name="swagger-ui",
        ),
    )
