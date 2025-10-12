from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse


# Create your models here.




class Recipe(models.Model):
    recipe_id = models.IntegerField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipes")
    title = models.CharField(max_length=250)
    instructions = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    servings = models.CharField(max_length=250)
    category = models.CharField(max_length=250)
    cook_time = models.DurationField()
    prep_time = models.DurationField()
    images = models.ImageField(upload_to="recipe_photos/", null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('recipe-detail', kwargs={'pk': self.pk})

    class Meta:
        permissions = [
            ("can_add_recipe", "Can add recipes"),
            ("can_change_recipe", "Can change recipes"),
            ("can_delete_recipe", "Can delete recipes"),
        ]


class IngredientsQuantity(models.Model):
    item = models.CharField(max_length=250)
    quantity = models.CharField(max_length=100)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="recipes")

    def __str__(self):
        return f"{self.item} - {self.quantity}"



class UserProfile(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.user
    
  


# 🔔 Signal to auto-create a UserProfile when a User is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:  # Only when a new User is created
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userProfile.save()
