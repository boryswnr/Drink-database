from django import forms
from .models import requiredUtensil, ingredientType, Ingredients


class DrinkForm(forms.Form):
    name = forms.CharField(max_length=100)
    utensil = forms.ChoiceField(choices=requiredUtensil)
    # ingredient1 = forms.ModelChoiceField(queryset=Ingredients.objects.all())
    # ingredient2 = forms.ModelChoiceField(queryset=Ingredients.objects.all())
    # ingredient3 = forms.ModelChoiceField(queryset=Ingredients.objects.all(), required=False)
    # ingredient4 = forms.ModelChoiceField(queryset=Ingredients.objects.all(), required=False)
    # ingredient5 = forms.ModelChoiceField(queryset=Ingredients.objects.all(), required=False)
    # ingredient6 = forms.ModelChoiceField(queryset=Ingredients.objects.all(), required=False)
    # ingredient7 = forms.ModelChoiceField(queryset=Ingredients.objects.all(), required=False)
    # ingredient8 = forms.ModelChoiceField(queryset=Ingredients.objects.all(), required=False)


class IngredientForm(forms.Form):
    name = forms.CharField(max_length=100)
    type = forms.IntegerField(choices=ingredientType)