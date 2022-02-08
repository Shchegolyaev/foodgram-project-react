from django.shortcuts import get_object_or_404
from rest_framework import filters, status, viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Follow, User
from .serializers import SubscriptionsSerializer


class ListSubscriptions(viewsets.ModelViewSet):
    serializer_class = SubscriptionsSerializer
    filter_backends = (filters.OrderingFilter,)
    pagination_class = LimitOffsetPagination
    ordering_fields = ("recipe.id",)

    def get_queryset(self):
        user = self.request.user
        new_queryset = User.objects.filter(following__user=user)
        return new_queryset


class Subscribe(APIView):
    def delete(self, request, id):
        user = request.user
        author = get_object_or_404(User, id=id)
        if not (
            user == author or Follow.objects.filter(user=user,
                                                    author=author).exists()
        ):
            return Response(
                {"errors": "Ошибка подписки (Например, если не был подписан"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        subscription = get_object_or_404(Follow, user=user, author=author)
        subscription.delete()
        return Response(
            {"errors": "Успешная отписка"}, status=status.HTTP_204_NO_CONTENT
        )

    def post(self, request, id):
        user = request.user
        author = get_object_or_404(User, id=id)
        if user == author or Follow.objects.filter(user=user,
                                                   author=author).exists():
            return Response(
                {
                    "errors": "Ошибка подписки (Например, если уже "
                    "подписан или подписке на самого себя"
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        Follow.objects.get_or_create(user=user, author=author)
        serializer = SubscriptionsSerializer(author,
                                             context={"request": request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)
