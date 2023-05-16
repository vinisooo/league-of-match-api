from django.urls import path
from .views import CharacterView

urlpatterns = [
    path("characters/", CharacterView.as_view()),
]
