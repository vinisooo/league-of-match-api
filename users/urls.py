from django.urls import path
from .views import UserView, UserRegisterView, UserDetailView, UserMainDetailView
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path("users/", UserView.as_view()),
    path("users/register/", UserRegisterView.as_view()),
    path("users/login/", TokenObtainPairView.as_view()),
    path("users/<int:pk>/", UserDetailView.as_view()),
    path("users/<int:pk>/main/<int:character_id>/", UserMainDetailView.as_view()),
]
