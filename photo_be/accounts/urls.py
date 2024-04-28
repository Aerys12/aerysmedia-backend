from django.urls import path
from .views import home_view, register_view

urlpatterns = [
    path('', home_view.Home.as_view(), name='home'),
    path('register/', register_view.UserRegistrationAPIView.as_view(), name='user_registration'),
    
]