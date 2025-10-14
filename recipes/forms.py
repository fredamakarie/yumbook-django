from django import forms
from django.forms import inlineformset_factory
from .models import Recipe, IngredientsQuantity

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'instructions', 'cook_time', 'prep_time', 'images']


class IngredientForm(forms.ModelForm):
    class Meta:
        model = IngredientsQuantity
        fields = ['item', 'quantity']


# Inline formset to link ingredients with recipes
IngredientFormSet = inlineformset_factory(
    Recipe,
    IngredientsQuantity,
    form=IngredientForm,
    extra=1,
    can_delete=True
)
