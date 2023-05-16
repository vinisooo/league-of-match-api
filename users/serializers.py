from rest_framework import serializers
from .models import User, RouteChoices, EloChoices
import re
from rest_framework_simplejwt.serializers import TokenObtainSerializer
from rest_framework_simplejwt.tokens import RefreshToken


class UserSerializer(serializers.ModelSerializer):
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
        ]
        read_only_fields = ["id"]
        extra_kwargs = {
            "elo": {
                "choices": EloChoices,
            },
            "route": {"choices": RouteChoices},
            "discord": serializers.CharField(
                validators=[lambda x: re.match(r"^\d{18}$", x)]
            ),
            "password": {"required": True, "write_only": True},
        }

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
