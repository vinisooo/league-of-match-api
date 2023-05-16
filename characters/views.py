from django.shortcuts import render
from rest_framework.views import APIView
from .models import Character
from .serializers import CharacterSerializer
from .data import characters
from rest_framework.response import Response
from .models import Character


class CharacterView(APIView):
    def post(self, request):
        serializer = CharacterSerializer(data=characters, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

    def get(self, request):
        characters = Character.objects.all()
        serializer = CharacterSerializer(characters, many=True)

        return Response(serializer.data, status=200)
