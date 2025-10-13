from django.db import models
from django.conf import settings
from django.urls import reverse

class Recipe(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='recipes'
    )
    title = models.CharField(max_length=250)
    instructions = models.TextField(null=True, blank=True)
    cook_time = models.DurationField(null=True, blank=True)
    prep_time = models.DurationField(null=True, blank=True)
    images = models.ImageField(upload_to="recipe_photos/", null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('recipe-detail', kwargs={'pk': self.pk})
