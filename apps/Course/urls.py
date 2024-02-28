from django.urls import path
from . import views

urlpatterns = [
    path('course/', views.course, name='course'),
    path('detail/<int:id>', views.detail_course, name='detail'),
    path('success/<int:id>', views.success, name='success'),
    path('exists/<int:id>', views.exists, name='exists'),
    path('table/', views.table, name='table'),
    path('add_course/<int:id>', views.add_course, name='add_course'),

]
