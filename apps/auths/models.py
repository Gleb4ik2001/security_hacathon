from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone


# Менеджер для кастомной модели пользователя
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """
        Создает и возвращает пользователя с email и паролем.
        """
        if not email:
            raise ValueError("Поле Email обязательно для заполнения.")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Создает и возвращает суперпользователя.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Суперпользователь должен иметь is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Суперпользователь должен иметь is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


# Кастомная модель пользователя
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)  # Email как основное поле для логина
    is_active = models.BooleanField(default=True)  # Активен ли пользователь
    is_staff = models.BooleanField(default=False)  # Доступ в админку
    date_joined = models.DateTimeField(default=timezone.now)  # Дата регистрации

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'  # Поле для логина
    REQUIRED_FIELDS = []  # Поля, которые обязательно нужно указать при создании суперпользователя

    def __str__(self):
        return self.email
