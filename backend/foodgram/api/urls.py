from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter

from users.views import ListSubscriptions, Subscribe

router = DefaultRouter()
router.register(r"users/subscriptions", ListSubscriptions, basename="subscriptions")

urlpatterns = [
    path('', include(router.urls)),
    path(f'users/<int:id>/subscribe/', Subscribe.as_view()),
    path(r'', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
