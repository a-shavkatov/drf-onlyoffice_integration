from . import user, documentation, onlyoffice

urlpatterns = user.urlpatterns + documentation.urlpatterns + onlyoffice.urlpatterns
