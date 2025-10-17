from rest_framework import serializers
from .models import Recipe, IngredientsQuantity

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = IngredientsQuantity
        fields = ['item', 'quantity']


class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True)
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Recipe
        fields = '__all__'

    
    def create(self, validated_data):
        # Extract the nested ingredients data
        ingredients_data = validated_data.pop('ingredients', [])
        recipe = Recipe.objects.create(**validated_data)

        # Create the ingredients
        for ingredient in ingredients_data:
            ingredient, _ = IngredientsQuantity.objects.create(recipe=recipe, **ingredient)

        return recipe
    
    
    def update(self, instance, validated_data):
        ingredients_data = validated_data.pop('ingredients', [])
        instance.title = validated_data.get('title', instance.title)
        instance.instructions = validated_data.get('instructions', instance.instructions)
        instance.cook_time = validated_data.get('cook_time', instance.cook_time)
        instance.prep_time = validated_data.get('prep_time', instance.prep_time)
        instance.category = validated_data.get('category', instance.category)
        instance.save()


        # Update recipe fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # Replace all ingredients
        instance.ingredients.all().delete()
        for ingredient in ingredients_data:
            IngredientsQuantity.objects.create(recipe=instance, **ingredient)

        return instance