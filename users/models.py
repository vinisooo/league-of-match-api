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
    TOPLANE = "toplane"
    JUNGLE = "jungle"
    MIDLANE = "midlane"
    ADC = "adc"
    SUPPORT = "support"


class User(AbstractUser):
    nickname = models.CharField(max_length=75)
    elo = models.TextField(max_length=25, choices=EloChoices.choices)
    route = models.TextField(
        max_length=10, choices=RouteChoices.choices, null=True, blank=True
    )
    main = models.ForeignKey(
        "characters.Character",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="users",
    )
    profile_icon = models.URLField()
    bio = models.CharField(blank=True, null=True, max_length=255)

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="user_groups",
        blank=True,
        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="user_permissions",
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )
