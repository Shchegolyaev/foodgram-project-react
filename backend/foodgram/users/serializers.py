from django.shortcuts import get_object_or_404
from rest_framework import serializers
from .models import Follow, User
from recipes.models import Recipe


class FollowingRecipeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recipe
        fields = ('id',
                  'name',
                  'image',
                  'cooking_time')


class SubscriptionsSerializer(serializers.ModelSerializer):
    recipe = serializers.SerializerMethodField()
    is_subscribed = serializers.SerializerMethodField()
    recipes_count = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('email',
                  'id',
                  'username',
                  'first_name',
                  'last_name',
                  'is_subscribed',
                  'recipe',
                  'recipes_count',)

    def get_recipe(self, author):
        recipes = author.recipes.all()
        return FollowingRecipeSerializer(recipes, many=True).data

    def get_is_subscribed(self, author):
        if Follow.objects.filter(author=author,
                                 user=self.context['request'].user).exists():
            return True
        return False

    def get_recipes_count(self, author):
        recipes_count = author.recipes.count()
        return recipes_count
