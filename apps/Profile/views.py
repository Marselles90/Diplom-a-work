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



@login_required
def edit_profile(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        return redirect('create_profile')

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        about_me = request.POST.get('about_me')
        full_name_par = request.POST.get('full_name')
        email_par = request.POST.get('email')
        phone_par = request.POST.get('phone')
        class_num = request.POST.get('class_num')
        image = request.FILES.get('image')
        user_email = request.POST.get('user_email')
        user_number = request.POST.get('user_number')
        
        
        profile.full_name_par = full_name_par
        profile.email_par = email_par
        profile.phone_par = phone_par
        profile.class_num = class_num
        profile.user.email = user_email
        profile.user.number = user_number
        profile.about_me = about_me
        profile.user.first_name = first_name
        profile.user.last_name = last_name
        
        if image:
            profile.image = image
        profile.save()
        profile.user.save()
        return redirect('profile')    
        
    teachers = Teacher.objects.all()
    context ={
        'class_options': teachers,
        'profile': profile
    }
    return render(request, 'edit_profile.html', context)
