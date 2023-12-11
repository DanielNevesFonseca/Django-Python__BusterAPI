from django.db import models
from users.models import User


class RatingChoices(models.TextChoices):
    G = "G"
    PG = "PG"
    PG_13 = "PG-13"
    R = "R"
    NC_17 = "NC-17"


class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, blank=True, default="")
    synopsis = models.TextField(blank=True, null=True, default="")
    rating = models.CharField(
        choices=RatingChoices,
        default=RatingChoices.G,
        max_length=20,
    )

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="movies"
    )

    purchased_by = models.ManyToManyField(
        "users.User",
        through="movies_orders.MovieOrder",
        related_name="purchased_movies"
        )
