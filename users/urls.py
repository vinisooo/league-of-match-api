from django.urls import path
from .views import UserView, UserRegisterView
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path("register/", UserRegisterView.as_view()),
    path("users/", UserView.as_view()),
    path("users/login/", TokenObtainPairView.as_view()),
]
