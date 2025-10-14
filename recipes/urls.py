from django.urls import path
from .views import RecipeCreateView

urlpatterns = [
    path('recipes/create/', RecipeCreateView.as_view(), name='recipe-create'),
]
