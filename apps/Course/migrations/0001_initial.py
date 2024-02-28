# Generated by Django 5.0.2 on 2024-02-28 11:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField(verbose_name='Время')),
                ('week', models.CharField(choices=[('Понедельник', 'Понедельник'), ('Вторник', 'Вторник'), ('Среда', 'Среда'), ('Четверг', 'Четверг'), ('Пятница', 'Пятница'), ('Суббота', 'Суббота'), ('Воскресенье', 'Воскресенье')], default='Понедельник', max_length=15, verbose_name='Неделя')),
                ('subject', models.CharField(max_length=50, verbose_name='Предмет')),
                ('text', models.TextField()),
                ('room', models.CharField(max_length=10, verbose_name='Кабинет')),
            ],
            options={
                'verbose_name_plural': 'Курсы',
            },
        ),
        migrations.CreateModel(
            name='ProfileTeacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Фамилия Имя')),
                ('work_experience', models.CharField(max_length=10, verbose_name='Стаж')),
                ('education', models.CharField(max_length=50, verbose_name='Образование')),
                ('certificate', models.CharField(max_length=50, verbose_name='Сертификат')),
            ],
            options={
                'verbose_name_plural': 'Профиль Учителя',
            },
        ),
        migrations.CreateModel(
            name='AddCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student', to=settings.AUTH_USER_MODEL, verbose_name='Студент')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course', to='Course.course', verbose_name='Курс')),
            ],
            options={
                'verbose_name_plural': 'Добавить курсы',
            },
        ),
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher', to='Course.profileteacher', verbose_name='Преподаватель'),
        ),
    ]