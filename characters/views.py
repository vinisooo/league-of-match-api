from django.shortcuts import render
from rest_framework.views import APIView
from .models import Character
from .serializers import CharacterSerializer
from .data import characters
from rest_framework.response import Response


class CharacterView(APIView):
    def post(self, request):
        serializer = CharacterSerializer(data=characters, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)
