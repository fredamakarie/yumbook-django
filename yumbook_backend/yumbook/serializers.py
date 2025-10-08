from rest_framework import serializers
from .models import Recipe, IngredientsQuantity

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = IngredientsQuantity
        fields = '__all__'


class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True, read_only=True)
    class Meta:
        model = Recipe
        fields = '__all__'