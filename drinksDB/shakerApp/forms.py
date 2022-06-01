from django import forms
from .models import requiredUtensil, ingredientType, Ingredients


class DrinkForm(forms.Form):
    name = forms.CharField(max_length=100, label="Name:")
    utensil = forms.ChoiceField(choices=requiredUtensil, label="Required utensil:")
    ingredients = forms.ModelMultipleChoiceField(
        queryset=Ingredients.objects.all(),
        widget=forms.CheckboxSelectMultiple()
    )
    preparation = forms.CharField(widget=forms.Textarea)


class IngredientForm(forms.Form):
    name = forms.CharField(max_length=100, label="Ingredient name")
    type = forms.ChoiceField(choices=ingredientType)
