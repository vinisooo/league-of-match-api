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
