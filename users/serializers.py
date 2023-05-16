from django.db import models
from django.contrib.auth.models import AbstractUser


class EloChoices(models.TextChoices):
    FERRO = "Ferro"
    BRONZE = "Bronze"
    PRATA = "Prata"
    OURO = "Ouro"
    PLATINA = "Platina"
    DIAMANTE = "Diamante"
    MESTRE = "Mestre"
    GRAO_MESTRE = "Grão-Mestre"
    DESAFIANTE = "Desafiante"


class RouteChoices(models.TextChoices):
    TOPLANE = "Toplane"
    JUNGLE = "Jungle"
    MIDLANE = "Midlane"
    ADC = "Adc"
    SUPPORT = "Support"


class User(AbstractUser):
    elo = models.TextField(max_length=25, choices=EloChoices.as_choices())
    route = models.TextField(
        max_length=10, choices=RouteChoices.as_choices(), null=True, blank=True
    )
    main = models.ForeignKey(
        "characters.Character",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="users",
    )
    profile_icon = models.URLField(null=True, blank=True)
    bio = models.CharField(blank=True, null=True, max_length=255)
    discord = models.CharField(blank=True, null=True, max_length=50)


from rest_framework import serializers
from .models import User, RouteChoices, EloChoices
import re
from characters.models import Character
from characters.serializers import CharacterSerializer
from django.shortcuts import get_object_or_404


class UserSerializer(serializers.ModelSerializer):
    main = CharacterSerializer(read_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "password",
            "email",
            "route",
            "elo",
            "main",
            "profile_icon",
            "bio",
            "discord",
        ]
        read_only_fields = ["id"]
        extra_kwargs = {
            "elo": {
                "choices": EloChoices.as_choices(),
            },
            "route": {"choices": RouteChoices.as_choices()},
            "discord": serializers.CharField(
                validators=[lambda x: x is None or re.match(r"^\d{18}$", x)]
            ),
            "password": {"required": True, "write_only": True},
        }

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)

        character_id = self.context["view"].kwargs.get("character_id")
        if character_id is not None:
            character = get_object_or_404(Character, id=character_id)
            instance.main = character

        for key, value in validated_data.items():
            setattr(instance, key, value)

        if password is not None:
            instance.set_password(password)

        instance.save()
        return instance
