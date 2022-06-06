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
    image = forms.ImageField(required=False)


class IngredientForm(forms.Form):
    name = forms.CharField(max_length=100, label="Ingredient name")
    type = forms.ChoiceField(choices=ingredientType)
    image = forms.ImageField(required=False)


class SearchIngredientsForm(forms.Form):
    query = forms.CharField(max_length=100, label="SearchBAR...")


class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label="Password", widget=forms.PasswordInput)


class RegistrationForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password_conf = forms.CharField(label="Password confirmation", widget=forms.PasswordInput)
    email = forms.EmailField(label="Email (optional)", required=False)
