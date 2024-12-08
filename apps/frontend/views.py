import requests
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def register_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Отправляем запрос к API для регистрации
        response = requests.post(
            "http://127.0.0.1:8000/api/v1/auth/register/",
            data={"email": email, "password": password}
        )

        if response.status_code == 201:
            messages.success(request, "Регистрация успешна! Теперь вы можете войти.")
            return redirect('login')
        else:
            errors = response.json()
            messages.error(request, f"Ошибка: {errors}")

    return render(request, 'register.html')


def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Отправляем запрос к API для входа
        response = requests.post(
            "http://127.0.0.1:8000/api/v1/auth/login/",
            data={"email": email, "password": password}
        )

        if response.status_code == 200:
            tokens = response.json()
            request.session['access'] = tokens['access']  # Сохраняем токен в сессии
            request.session['refresh'] = tokens['refresh']
            messages.success(request, "Вы успешно вошли!")
            return redirect('home')
        else:
            messages.error(request, "Неверные учетные данные.")

    return render(request, 'login.html')

@login_required
def home_view(request):
    access_token = request.session.get('access')
    return render(request, 'home.html', {'access_token': access_token})
