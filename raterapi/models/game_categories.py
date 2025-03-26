from django.db import models


class GameCategories(models.Model):
    game = models.ForeignKey("Game", on_delete=models.CASCADE, related_name="category")
    category = models.ForeignKey(
        "Category", on_delete=models.CASCADE, related_name="gamecategory"
    )
