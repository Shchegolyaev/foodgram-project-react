from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import TagViewSet, IngredientsViewSet, RecipeViewSet

router = SimpleRouter()

router.register(r"tags", TagViewSet, basename="tags")
router.register(r"ingredients", IngredientsViewSet, basename="ingredients")
router.register(r"recipes", RecipeViewSet, basename="recipes")

urlpatterns = [
    path("", include(router.urls)),
]