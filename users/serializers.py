from rest_framework import serializers
from .models import User, RouteChoices, EloChoices
import re
from characters.models import Character
from characters.serializers import CharacterSerializer
from django.shortcuts import get_object_or_404
from django.core.validators import RegexValidator


class UserSerializer(serializers.ModelSerializer):
    main = CharacterSerializer(read_only=True)

    discord = serializers.CharField(
        allow_null=True,
        allow_blank=True,
        max_length=50,
        validators=[RegexValidator(r"^[a-zA-Z]+\#\d{4}$", "Invalid discord format.")],
    )

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
                "choices": EloChoices.choices,
            },
            "route": {"choices": RouteChoices.choices},
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
