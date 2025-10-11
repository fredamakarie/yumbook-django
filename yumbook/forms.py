from django import forms
from django.forms import inlineformset_factory
from .models import Recipe, IngredientsQuantity

class RecipeCreationForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'

class IngredientForm(forms.ModelForm):
    class Meta:
        model = IngredientsQuantity
        fields = '__all__'

class RecipeUpdateForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'

IngredientFormSet = inlineformset_factory(
    Recipe,
    IngredientsQuantity,
    form=IngredientForm,
    extra=1,       # how many blank ingredient rows to show
    can_delete=True
)