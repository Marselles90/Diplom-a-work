from django.shortcuts import render, redirect
from .models import Course, AddCourse
from django.contrib.auth.decorators import login_required

# Курсы
@login_required
def course(request):
    courses = Course.objects.all()
    context = {'courses': courses}
    return render(request, 'course.html', context)


# Детали курса
@login_required
def detail_course(request, id):
    cource = Course.objects.get(id=id)
    
    context = {
        'cource': cource,  
    }    
    return render(request, 'detail.html', context)


# Красное сообщение
@login_required
def success(request, id):
    cource = Course.objects.get(id=id)
    context = {'cource': cource,
               }
    return render(request, 'success.html', context)    
    


# Таблица курсов
@login_required
def table(request):
    return render(request, 'table.html')


# Информация о записи
@login_required
def add_course(request, id): 
    course = Course.objects.get(id=id)
    user = request.user
    if AddCourse.objects.filter(student=user, course=course).exists():
        return redirect('exists', id=id)
    add_course = AddCourse(student=user, course=course)
    add_course.save()
    return redirect('success', id=id)


# Страница вы уже записаны
@login_required
def exists(request, id):
    cource = Course.objects.get(id=id)
    context = {'cource': cource,
               }
    return render(request, 'exists.html', context)    
    
    
@login_required
def table(request):
    courses = Course.objects.filter(course__student=request.user).order_by()
    print(course)
    context = {
        'courses': courses
        }
    return render(request, 'table.html', context)