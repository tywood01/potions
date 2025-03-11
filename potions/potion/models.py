"""
models.py

Authors: Tytus Woodburn
Email: tytus.woodburn@student.cune.edu
Github: https://github.com/tywood01

Purpose:
    Define the models for the potions app.

"""

from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    bio = models.CharField(max_length=255)
    public = models.BooleanField(default=True)


class Ingredient(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)


class PotionUse(models.Model):
    name = models.CharField(max_length=255, unique=True)


class Potion(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    description = models.TextField(blank=True, null=True)
    uses = models.ManyToManyField(PotionUse, blank=True)  # Multiple uses


class PotionIngredient(models.Model):
    potion = models.ForeignKey(Potion, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=100)
