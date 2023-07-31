from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core import validators

from foodgram.settings import (
    LENGTH_EMAIL,
    LENGTH_USERNAME,
    LENGTH_NAME
)


class User(AbstractUser):

    email = models.EmailField(
        max_length=LENGTH_EMAIL,
        verbose_name='Адрес электронной почты',
        unique=True
    )
    username = models.CharField(
        max_length=LENGTH_USERNAME,
        verbose_name='Уникальный юзернейм',
        unique=True,
        validators=[validators.RegexValidator(regex=r'^[\w.@+-]+\z')]
    )
    first_name = models.CharField(
        max_length=LENGTH_NAME,
        verbose_name='Имя'
    )
    last_name = models.CharField(
        max_length=LENGTH_NAME,
        verbose_name='Фамилия'
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.username, self.email}'
