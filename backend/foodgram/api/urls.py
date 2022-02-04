from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from users.views import Subscribe, ListSubscriptions
from recipes.views import FavoriteView, ShoppingCardView


router = DefaultRouter()
router.register(r"users/subscriptions", ListSubscriptions, basename="subscriptions")

urlpatterns = [
    path('', include(router.urls)),
    path(f'users/<int:id>/subscribe/', Subscribe.as_view()),
    path(f'recipes/download_shopping_cart/', ShoppingCardView.as_view()),
    path(f'recipes/<int:id>/favorite/', FavoriteView.as_view()),
    path(f'recipes/<int:id>/shopping_cart/', ShoppingCardView.as_view()),

    path(r'', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),

    # path('users/<int:id>/subscribe/', views.profile_follow,
    #      name='profile_follow'),
]
