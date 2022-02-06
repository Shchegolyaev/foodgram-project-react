from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import (FavoriteView, IngredientsViewSet, RecipeViewSet,
                    ShoppingCardView, TagViewSet)

router = SimpleRouter()

router.register(r"tags", TagViewSet, basename="tags")
router.register(r"ingredients", IngredientsViewSet, basename="ingredients")
router.register(r"recipes", RecipeViewSet, basename="recipes")

urlpatterns = [
    path(f'recipes/<int:id>/favorite/', FavoriteView.as_view()),
    path(f'recipes/download_shopping_cart/', ShoppingCardView.as_view()),
    path(f'recipes/<int:id>/shopping_cart/', ShoppingCardView.as_view()),
    path("", include(router.urls)),
]