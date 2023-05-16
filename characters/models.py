from django.db import models


class Character(models.Model):
    name = models.CharField(max_length=50)
    icon = models.URLField()
    splashart = models.URLField()
    skin_splashart = models.URLField()
    card = models.URLField()
    skin_card = models.URLField()
