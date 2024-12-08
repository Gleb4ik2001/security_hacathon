from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate, logout
from .serializers import UserRegistrationSerializer, UserLoginSerializer
from django.shortcuts import redirect
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser
from django.contrib.auth import authenticate

# Регистрация пользователя
class RegisterView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            return Response({"error": "Email и пароль обязательны"}, status=status.HTTP_400_BAD_REQUEST)

        if CustomUser.objects.filter(email=email).exists():
            return Response({"error": "Пользователь уже существует"}, status=status.HTTP_400_BAD_REQUEST)

        user = CustomUser.objects.create_user(email=email, password=password)
        user.save()

        refresh = RefreshToken.for_user(user)
        return Response({
            "access": str(refresh.access_token),
            "refresh": str(refresh),
            "message": "Регистрация успешна"
        }, status=status.HTTP_201_CREATED)


# Вход пользователя
class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(email=email, password=password)

        if not user:
            return Response({"error": "Неверные учетные данные"}, status=status.HTTP_401_UNAUTHORIZED)

        refresh = RefreshToken.for_user(user)
        return Response({
            "access": str(refresh.access_token),
            "refresh": str(refresh),
            "message": "Вход успешен"
        }, status=status.HTTP_200_OK)


class HomeAPIView(APIView):
    """
    Возвращает данные текущего пользователя, если он авторизован.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            "email": user.email,
            "message": f"Добро пожаловать, {user.email}!"
        })
        
class UserDetailView(APIView):
    """
    Возвращает информацию о текущем авторизованном пользователе.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Текущий авторизованный пользователь доступен через request.user
        user = request.user
        return Response({
            "id": user.id,
            "email": user.email,
            "is_staff": user.is_staff,
            "date_joined": user.date_joined.strftime('%Y-%m-%d %H:%M:%S')
        })