from django.contrib import admin

from .models import Recipe, Ingredient, Tag, IngredientInRecipe, ShoppingCart, Favorite


admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(Tag)
admin.site.register(IngredientInRecipe)
admin.site.register(Favorite)
admin.site.register(ShoppingCart)
