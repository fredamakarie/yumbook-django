from rest_framework import serializers
from .models import Recipe, IngredientsQuantity
from datetime import timedelta

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
    
    def validate_prep_time(self, value):
        """Ensure prep_time is valid format or return friendly error."""
        return self._validate_duration(value, 'prep_time')

    def validate_cook_time(self, value):
        """Ensure cook_time is valid format or return friendly error."""
        return self._validate_duration(value, 'cook_time')

    def _validate_duration(self, value, field_name):
        if isinstance(value, timedelta) or value is None:
            return value

        # Handle if passed as string
        try:
            if isinstance(value, str):
                parts = value.split(':')
                if len(parts) == 3:
                    h, m, s = map(int, parts)
                    return timedelta(hours=h, minutes=m, seconds=s)
                elif len(parts) == 2:
                    h, m = map(int, parts)
                    return timedelta(hours=h, minutes=m)
                elif len(parts) == 1:
                    m = int(parts[0])
                    return timedelta(minutes=m)
        except ValueError:
            raise serializers.ValidationError(
                f"Invalid format for {field_name}. Use 'HH:MM:SS' or total minutes (e.g. '00:30:00' or '30')."
            )

        raise serializers.ValidationError(
            f"Invalid value for {field_name}. Use 'HH:MM:SS' or 'MM'."
        )