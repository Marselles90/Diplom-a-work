from django.db import models
from apps.Auth.models import User


    # Классный руководитель
class Teacher(models.Model):
    full_name_kr = models.CharField(max_length=100, verbose_name='Имя и Фамилия Клас.рук')
    email_kr = models.EmailField(verbose_name='Email Клас.рук')
    number_kr = models.CharField(max_length=15, verbose_name='Номер Клас.рук')
    
    def __str__(self) -> str:
        return self.full_name_kr
    
    class Meta:
        verbose_name_plural = "Классный рук"


    
    # Профиль родителей
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь', related_name='profile')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='Учитель', related_name='teacher')
    full_name_par = models.CharField(max_length=100, verbose_name='Имя и Фамилия')
    email_par = models.EmailField(verbose_name='Email')
    phone_par = models.CharField(max_length=15, verbose_name='Номер')
    class_num = models.CharField(max_length=5, verbose_name='Класс')
    image = models.ImageField(upload_to='static/images/') 
    about_me = models.TextField()
    
    def __str__(self):
        return self.full_name_par



    
    