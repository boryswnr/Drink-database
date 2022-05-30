from django import forms
# from .fields import GroupedModelChoiceField
from .models import requiredUtensil, ingredientType, Ingredients


class DrinkForm(forms.Form):
    name = forms.CharField(max_length=100)
    utensil = forms.ChoiceField(choices=requiredUtensil)
    ingredients = forms.ModelChoiceField(queryset=Ingredients.objects.all(), widget=forms.Select())


class IngredientForm(forms.Form):
    name = forms.CharField(max_length=100, label="Ingredient name")
    type = forms.ChoiceField(choices=ingredientType)
