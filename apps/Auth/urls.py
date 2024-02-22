from django.urls import path
from . import views


urlpatterns = [
    path('auth/', views.Auth, name='auth'),
    path('', views.home, name='home'),
    path('login/', views.logins, name='login'),
]