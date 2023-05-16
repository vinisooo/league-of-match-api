from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Character
from .serializers import CharacterSerializer
from .data import characters
from rest_framework.response import Response
from .models import Character


class CharacterView(ListAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
