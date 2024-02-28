from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import User




# Регистрация
def Auth(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        number = request.POST['number']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        image = request.FILES.get('image')
        print(first_name, last_name, number, email, password1, password2)    
        
        
        if last_name.isdigit():
            messages.error(request, 'Имя не должно содержать цифр')
            return redirect('auth')
        
        if first_name.isdigit():
            messages.error(request, 'Фамилия не должна содержать цифр')
            return redirect('auth')
        
        if User.objects.filter(number=number).exists():
            messages.error(request, f'{number} уже зарегистрирован!')
            return redirect('auth')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, f'{email} уже зарегистрирован!')
            return  redirect('auth')
        
        if password1 != password2:
            messages.error(request, 'Пароли не совпадают')
            return redirect('auth')
        
        if len(password1) < 8:
            messages.error(request, 'Пароль должен быть не менее 8 символов')
            return redirect('auth')
        
        
        user = User.objects.create_user(
            first_name=first_name, 
            last_name=last_name, 
            number=number, 
            email=email, 
            password=password1,
        )
    
        login(request, user)
        
        return redirect('create_profile')  # Перенаправляет на главную страницу
    return render(request, 'auth.html') 



# Главная страница
def home(request):
    return render(request, 'home.html')
    


# Вход в аккаунт
def logins(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        if email and password:
            try:
                user = authenticate(request, email=email, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Вы успешно вошли!')
                    return redirect('profile')
                else:
                    messages.error(request, 'Неверный логин или пароль!')
            except Exception:
                messages.error(request, 'Произошла ошибка при аутентификации. Пожалуйста, попробуйте снова.')
        else:
            messages.warning(request, 'Заполните все поля!')
    
    return render(request, 'login.html')



def logout_view(request):
    logout(request)
    messages.success(request, 'Вы успешно вышли!')
    return redirect('home')
