from django.db import models
from characters.models import Character


class CharacterSerializer(models.ModelSerializer):
    class Meta:
        model = Character
        fields = "__all__"
