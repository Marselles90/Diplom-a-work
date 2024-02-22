from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Teacher


class PeopleForm(UserCreationForm):
    class Meta:
        model = Profile
        fields = ("full_name", "email", "phone", "class_num", "password1", 'image')


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ("full_name_kr", "email_kr", 'number_kr' )
