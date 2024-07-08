from django.db import models
from django.contrib.auth.models import User

class FoodType(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.name

class Food(models.Model):
    foodtype = models.ForeignKey(FoodType,on_delete=models.CASCADE)