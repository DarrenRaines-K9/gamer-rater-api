from django.db import models
from django.contrib.auth.models import User


class Game(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="gameuser")
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    designer = models.CharField(max_length=200)
    year_released = models.DateField()
    number_of_players = models.IntegerField()
    time_to_play = models.IntegerField()
    age_restriction = models.IntegerField()
