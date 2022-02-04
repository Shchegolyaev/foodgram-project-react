from django.contrib import admin

from .models import (Favorite, Ingredient, IngredientInRecipe, Recipe,
                     ShoppingCart, Tag)




class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'author', 'recipe_count',
    )
    list_filter = ('name', 'author', 'tags')


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient)
admin.site.register(Tag)
admin.site.register(IngredientInRecipe)
admin.site.register(Favorite)
admin.site.register(ShoppingCart)
