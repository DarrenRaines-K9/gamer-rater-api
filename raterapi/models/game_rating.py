from django.db import models
from django.contrib.auth.models import User


class GameRating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="gamerating")
    game = models.ForeignKey(
        "Game", on_delete=models.CASCADE, related_name="gamerating"
    )
    rating = models.IntegerField()
