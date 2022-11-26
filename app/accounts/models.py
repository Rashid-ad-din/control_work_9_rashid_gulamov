from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import TextChoices


class GenderChoices(TextChoices):
    MALE = 'male', 'Мужчина'
    FEMALE = 'female', 'Женщина'


class Account(AbstractUser):
    username = models.CharField(verbose_name='Логин', unique=True, null=False, blank=False, max_length=150)
    favorites = models.ManyToManyField(verbose_name='Избранные',
                                       to='webapp.Photos',
                                       related_name='favorites')

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
