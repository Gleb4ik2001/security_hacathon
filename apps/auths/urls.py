from django.urls import path
from .views import RegisterView, LoginView, UserDetailView, HomeAPIView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('user/', UserDetailView.as_view(), name='user-detail'),
    path('home/', HomeAPIView.as_view(), name='home-api'),
]