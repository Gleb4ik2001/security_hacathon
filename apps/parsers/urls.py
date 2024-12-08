from django.urls import path
from .views import LatestExploitsView

urlpatterns = [
    path('latest-exploits/', LatestExploitsView.as_view(), name='latest-exploits'),
]