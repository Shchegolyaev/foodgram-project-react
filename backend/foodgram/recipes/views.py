import io

from django.db.models import F, Sum
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from rest_framework import filters, permissions, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .permissions import OwnerOrReadOnly

from .models import (Favorite, Ingredient, IngredientInRecipe, Recipe,
                     ShoppingCart, Tag)
from .serializers import (FavoriteSerializer, IngredientSerializer,
                          RecipeCreateSerializer, RecipeSerializer,
                          TagSerializer)


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    http_method_names = ["get"]
    pagination_class = None


class IngredientsViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    http_method_names = ["get"]
    pagination_class = None


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = (OwnerOrReadOnly,)
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_fields = ('tags',)
    ordering_fields = ('id',)

    def get_serializer_class(self):
        if self.request.method in ['POST', 'PATCH']:
            return RecipeCreateSerializer
        elif self.request.method == 'GET':
            return RecipeSerializer


class FavoriteView(APIView):

    def delete(self, request, id):
        user = request.user
        recipe = get_object_or_404(Recipe, id=id)
        favorites = get_object_or_404(Favorite, user=user,
                                      recipe=recipe)
        favorites.delete()
        return Response({"errors": "string"}, status=status.HTTP_204_NO_CONTENT)

    def post(self, request, id):
        user = request.user
        recipe = Recipe.objects.get(id=id)
        if Favorite.objects.filter(user=user, recipe=recipe).exists():
            return Response({"errors": "string"}, status=status.HTTP_400_BAD_REQUEST)
        Favorite.objects.get_or_create(user=user, recipe=recipe)
        serializer = FavoriteSerializer(recipe, context={'request':
                                             request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ShoppingCardView(APIView):

    def get(self, request):
        user = request.user
        string = ''
        shopping_list = IngredientInRecipe.objects.filter(
            recipe__shopping_cart__user=user).values(
            name=F('ingredient__name'),
            unit=F('ingredient__measurement_unit')
        ).annotate(amount=Sum('amount')).order_by()
        font = 'DejaVuSerif'
        pdfmetrics.registerFont(TTFont('DejaVuSerif', 'DejaVuSerif.ttf', 'UTF-8'))
        buffer = io.BytesIO()
        pdf_file = canvas.Canvas(buffer)
        pdf_file.setFont(font, 24)
        pdf_file.drawString(
            150,
            800,
            'Список покупок.'
        )
        pdf_file.setFont(font, 14)
        from_bottom = 750
        for number, ingredient in enumerate(shopping_list, start=1):
            pdf_file.drawString(
                50,
                from_bottom,
                f'{number}.  {ingredient["name"]} - {ingredient["amount"]} '
                f'{ingredient["unit"]}'
            )
            from_bottom -= 20
            if from_bottom <= 50:
                from_bottom = 800
                pdf_file.showPage()
                pdf_file.setFont(font, 14)
        pdf_file.showPage()
        pdf_file.save()
        buffer.seek(0)
        return FileResponse(buffer, as_attachment=True, filename='shopping_list.pdf')

    def delete(self, request, id):
        user = request.user
        recipe = get_object_or_404(Recipe, id=id)
        favorites = get_object_or_404(ShoppingCart, user=user,
                                      recipe=recipe)
        favorites.delete()
        return Response({"errors": "string"}, status=status.HTTP_204_NO_CONTENT)

    def post(self, request, id):
        user = request.user
        recipe = Recipe.objects.get(id=id)
        if ShoppingCart.objects.filter(user=user, recipe=recipe).exists():
            return Response({"errors": "string"}, status=status.HTTP_400_BAD_REQUEST)
        ShoppingCart.objects.get_or_create(user=user, recipe=recipe)
        serializer = FavoriteSerializer(recipe, context={'request':
                                             request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)
