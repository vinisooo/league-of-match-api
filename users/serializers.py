from rest_framework import serializers
from .models import User, RouteChoices, EloChoices


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password", "email", "route", "elo"]
        read_only_fields = ["id", "password"]
        extra_kwargs = {
            "elo": {
                "choices": EloChoices,
            },
            "route": {"choices": RouteChoices},
        }
