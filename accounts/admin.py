from django.contrib import admin
from .models import CustomUser

# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("username", "id",)
    list_filter = ("username", "id",)
    search_fields = ("username", "id",)
admin.site.register(CustomUser, CustomUserAdmin)