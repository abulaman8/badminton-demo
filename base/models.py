from django.db import models
from django.contrib.auth.models import User


class Player(models.Model):
    class PlayerType(models.TextChoices):
        Professional = 'Professional'
        Grassroot = 'Grassroot'
        Enthusiast = 'Enthusiast'

    class Dominance(models.TextChoices):
        Left = 'Left'
        Right = 'Right'

    class Gender(models.TextChoices):
        Male = 'Male'
        Female = 'Female'
        Other = 'Other'

    class Focus(models.TextChoices):
        Technique = 'Technique'
        Strategy = 'Strategy'
        Speed = 'Speed'
        Fitness = 'Fitness'
        Concentration = 'Concentration'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    player_type = models.CharField(
        max_length=20, choices=PlayerType.choices, default=PlayerType.Enthusiast)
    age = models.PositiveIntegerField()
    dominant_hand = models.CharField(
        max_length=20, choices=Dominance.choices, default=Dominance.Right)
    gender = models.CharField(
        max_length=20, choices=Gender.choices, default=Gender.Male)
    focus = models.CharField(
        max_length=20, choices=Focus.choices, default=Focus.Technique)

    def __str__(self):
        return self.name
