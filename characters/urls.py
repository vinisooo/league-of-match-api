from django.urls import path
from .views import CharacterView, CreateCharacterView

urlpatterns = [
    path("characters/", CharacterView.as_view()),
    path("create_characters/", CreateCharacterView.as_view()),
]
