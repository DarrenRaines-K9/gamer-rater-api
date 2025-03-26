from django.db import models
from django.contrib.auth.models import User


class GameReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="gamereview")
    game = models.ForeignKey(
        "Game", on_delete=models.CASCADE, related_name="gamereview"
    )
    review = models.TextField(max_length=400)
