from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Recipes(models.Model):
    recipe_id = models.IntegerField()
    title = models.CharField()
