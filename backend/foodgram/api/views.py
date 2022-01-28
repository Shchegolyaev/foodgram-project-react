from django.shortcuts import render
from rest_framework import generics
from users.models import User
from .serializers import UserSerializer
from rest_framework import filters, status, viewsets


class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get', 'post']


