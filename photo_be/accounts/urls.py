from django.urls import path
from .views import home_view, register_view, verify_token_view

urlpatterns = [
    path('', home_view.Home.as_view(), name='home'),
    path('register/', register_view.UserRegistrationAPIView.as_view(), name='user_registration'),
    path('verify-token/', verify_token_view.verify_token, name='verify-token'),
    
]