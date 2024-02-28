from django.shortcuts import render, redirect
from .models import Profile, Teacher
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages



# Профиль ученика
@login_required
def create_profile(request):
    if request.method == 'POST':
        if Profile.objects.filter(user=request.user).exists():
            return redirect('profile')
        
        teacher_id = request.POST.get('teacher')
        full_name_par = request.POST.get('full_name')
        email_par = request.POST.get('email')
        phone_par = request.POST.get('phone')
        class_num = request.POST.get('class_num')
        image = request.FILES.get('image')
        teacher = Teacher.objects.get(pk=teacher_id)
        user = request.user
        
        # print(user, teacher, class_num, phone, email, full_name, teacher_id)
        profile = Profile(
            user=user,
            teacher=teacher,
            full_name_par=full_name_par,
            email_par=email_par,
            phone_par=phone_par,
            class_num=class_num,
            image=image,
            )
        profile.save()
        
        return redirect('profile')    
    teachers = Teacher.objects.all()
    context ={
        'class_options': teachers
    }
    return render(request, 'create_profile.html', context)


@login_required
def profile(request):
    return render(request, 'profile.html')

