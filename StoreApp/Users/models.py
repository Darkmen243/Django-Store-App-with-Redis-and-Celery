from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(verbose_name="Электронная почта", unique=True, null=False)
    username = models.CharField(verbose_name="Имя пользователя", max_length=40, unique=True, null=False)
    user_info = models.TextField(verbose_name="Дополнительная информация о пользователе", max_length=255, null=True)
    phone_number = models.CharField(verbose_name="Номер телефона пользователя",max_length=12)
    last_login = models.DateTimeField(verbose_name="Время последнего входа", auto_now=True)
    is_active = models.BooleanField(verbose_name="Активен ли пользователь", default=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','phone_number']

    def __str__(self):
        return self.username