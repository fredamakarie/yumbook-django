from rest_framework import serializers
from .models import Recipe, IngredientsQuantity

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = IngredientsQuantity
        fields = ['id', 'item', 'quantity']


class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True, read_only=True)
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Recipe
        fields = ['id', 'author', 'title', 'instructions', 'cook_time', 'prep_time', 'images', 'ingredients', 'category']

    
    def create(self, validated_data):
        # Extract the nested ingredients data
        ingredients_data = validated_data.pop('ingredients', [])
        recipe = Recipe.objects.create(**validated_data)

        # Create the ingredients
        for ingredient in ingredients_data:
            IngredientsQuantity.objects.create(recipe=recipe, **ingredient)

        return recipe

    def update(self, instance, validated_data):
        ingredients_data = validated_data.pop('ingredients', [])
        
        # Update recipe fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # Replace all ingredients
        instance.ingredients.all().delete()
        for ingredient in ingredients_data:
            IngredientsQuantity.objects.create(recipe=instance, **ingredient)

        return instance