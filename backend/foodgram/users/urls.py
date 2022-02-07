from django.urls import include, path, re_path

from rest_framework.routers import DefaultRouter

from .views import ListSubscriptions, Subscribe

router = DefaultRouter()
router.register(r"subscriptions", ListSubscriptions, basename="subscriptions")

urlpatterns = [
    path(r'', include('djoser.urls')),
    path('users/', include(router.urls)),
    path('users/<int:id>/subscribe/', Subscribe.as_view(),
         name='subscribe'),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
