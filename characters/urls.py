from django.urls import path
from .views import CharacterView

urlpatterns = [
    path("create_characters/", CharacterView.as_view()),
]
