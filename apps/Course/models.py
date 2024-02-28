from django.db import models
from apps.Auth.models import User

    
# Профиль Учителя
class ProfileTeacher(models.Model):
    name = models.CharField(max_length=120, verbose_name="Фамилия Имя")
    work_experience = models.CharField(max_length=10, verbose_name="Стаж")
    education = models.CharField(max_length=50, verbose_name="Образование")
    certificate = models.CharField(max_length=50, verbose_name="Сертификат")
    
    def __str__(self) -> str:
        return f'{self.name}'
    
    class Meta:
        verbose_name_plural = "Профиль Учителя"


    
# Курс
class Course(models.Model):
    COURSE_CHOICES = (
        ('Понедельник', 'Понедельник'),
        ('Вторник', 'Вторник'),
        ('Среда', 'Среда'),
        ('Четверг', 'Четверг'),
        ('Пятница', 'Пятница'),
        ('Суббота', 'Суббота'),
        ('Воскресенье', 'Воскресенье')
    )
    
    
    time = models.TimeField(verbose_name="Время")
    week = models.CharField(max_length=15, choices=COURSE_CHOICES, default='Понедельник', verbose_name="Неделя")
    subject = models.CharField(max_length=50, verbose_name="Предмет")
    teacher = models.ForeignKey(ProfileTeacher, on_delete=models.CASCADE, related_name='teacher', verbose_name="Преподаватель")
    text = models.TextField()
    room = models.CharField(max_length=10, verbose_name="Кабинет")
    
    def __str__(self) -> str:
        return f'Предмет {self.subject}'

    class Meta:
        verbose_name_plural = "Курсы"


# Запись курса
class AddCourse(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student', verbose_name="Студент")
    date = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course', verbose_name="Курс")
    
    def __str__(self) -> str:
        return f'Добавлено {self.date}'
    
    class Meta:
        verbose_name_plural = "Добавить курсы"
