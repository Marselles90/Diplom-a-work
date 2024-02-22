from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'number', 'email', 'password1', 'password2']
        

class LoginForm(forms.Form):
    username_or_email = forms.CharField(label='Номер или email')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)