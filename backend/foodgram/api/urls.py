from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter


router = DefaultRouter()


urlpatterns = [
    path(r'', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
