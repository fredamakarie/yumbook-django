from django.contrib import admin
from .models import Recipe

# Register your models here.
class RecipeAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "category",)
    list_filter = ("title", "author", "category",)
    search_fields = ("title", "author", "category",)
admin.site.register(Recipe, RecipeAdmin)