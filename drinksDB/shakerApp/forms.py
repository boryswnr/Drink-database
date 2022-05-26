from django import forms
from .fields import GroupedModelChoiceField
from .models import requiredUtensil, ingredientType, Ingredients, Type


class DrinkForm(forms.Form):
    name = forms.CharField(max_length=100)
    utensil = forms.ChoiceField(choices=requiredUtensil)
    ingredients = forms.ModelChoiceField(queryset=Ingredients.objects.all(), widget=forms.Select())
    # ingredient1 = forms.ModelChoiceField(queryset=Ingredients.objects.all())


class IngredientForm(forms.Form):
    name = forms.CharField(max_length=100, label="Ingredient name")
    type = GroupedModelChoiceField(
        queryset=Type.objects.exclude(parent=None),
        choices_groupby='parent'
    )

    class Meta:
        model = Ingredients
        fields = 'name'
