from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class User(AbstractUser):
    ROLES = [
        (settings.ROLE_GUEST, 'Гость'),
        (settings.ROLE_USER, 'Авторизированный пользователь'),
        (settings.ROLE_ADMIN, 'Администратор'),
    ]
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
    role = models.CharField(
        max_length=300,
        choices=ROLES,
        default='guest',
        verbose_name='роль'
    )

