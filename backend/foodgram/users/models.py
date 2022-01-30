from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class User(AbstractUser):

    email = models.EmailField(
        max_length=254,
        unique=True,
        blank=False,
        verbose_name='Адрес электронной почты'
    )
    username = models.CharField(
        max_length=150,
        unique=True,
        blank=False,
        verbose_name='Уникальный юзернейм'
    )
    first_name = models.CharField(
        max_length=150,
        blank=False,
        verbose_name='Имя'
    )
    last_name = models.CharField(
        max_length=150,
        blank=False,
        verbose_name='Фамилия'
    )
    password = models.CharField(
        max_length=150,
        blank=False,
        verbose_name='Пароль'
    )
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

