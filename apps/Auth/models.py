from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):
    # Создание пользователя
    def create_user(self, email,  password=None, **extra_fields):
        if not email:
            raise ValueError('Поле электронной почты должно быть задано!')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    # Создание суперпользователя
    def create_superuser(self, email,  password=None, **extra_fields):
        user = self.create_user(email, password=password)
        user.is_superuser = True   
        user.is_staff = True
        user.save(using=self._db)
        return user  
    
    # Профиль ученика
class User(AbstractUser):
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    number = models.CharField(max_length=15, verbose_name='Номер телефона', null=True, blank=True)
    email = models.EmailField(unique=True, verbose_name='Email')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    username = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to='static/images/')

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'
    
    
