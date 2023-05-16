from rest_framework import serializers
from .models import User, RouteChoices, EloChoices
import re


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password", "email", "route", "elo", "main"]
        read_only_fields = ["id", "password"]
        extra_kwargs = {
            "elo": {
                "choices": EloChoices,
            },
            "route": {"choices": RouteChoices},
            "discord": serializers.CharField(
                validators=[lambda x: re.match(r"^\d{18}$", x)]
            ),
        }

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
