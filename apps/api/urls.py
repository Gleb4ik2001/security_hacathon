from django.urls import path
from .views import VulnerabilitiesListView, ScanInitiateView,ScanIPView
from auths.views import RegisterView, LoginView

urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('v1/scan-ip/', ScanIPView.as_view(), name='scan_ip'),
]
