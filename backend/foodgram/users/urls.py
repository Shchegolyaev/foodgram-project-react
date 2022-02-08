from django.urls import include, path, re_path

from rest_framework.routers import DefaultRouter

from .views import ListSubscriptions, Subscribe

router = DefaultRouter()
router.register(r"", ListSubscriptions, basename="subscriptions")

urlpatterns = [
    path("users/subscriptions/", include(router.urls)),
    path(r"", include("djoser.urls")),
    path("users/<int:id>/subscribe/", Subscribe.as_view(), name="subscribe"),
    re_path(r"^auth/", include("djoser.urls.authtoken")),
]
