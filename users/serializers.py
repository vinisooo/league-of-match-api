from rest_framework import serializers
from .models import User, RouteChoices, EloChoices
import re


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
            "discord": serializers.CharField(
                validators=[lambda x: re.match(r"^\d{18}$", x)]
            ),
        }
