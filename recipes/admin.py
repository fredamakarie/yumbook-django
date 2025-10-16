from django.contrib import admin
from .models import Recipe, IngredientsQuantity

# Register your models here.
class IngredientsInline(admin.TabularInline):
    model = IngredientsQuantity
    extra = 1

class RecipeAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "category",)
    list_filter = ("title", "author", "category",)
    search_fields = ("title", "author", "category",)

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(IngredientsQuantity)

