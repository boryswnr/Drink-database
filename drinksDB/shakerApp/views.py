from django.contrib import messages
from django.shortcuts import render
from django.views import View

from .forms import IngredientForm, DrinkForm
from .models import Ingredients, DrinkRecipe


# Create your views here.
class IndexView(View):

    def get(self, request):
        form_ingredients = IngredientForm()
        form_drinks = DrinkForm()
        ingredients_list = Ingredients.objects.all()
        drinks_list = DrinkRecipe.objects.all()
        context = {
            'form_ingredients': form_ingredients,
            'form_drinks': form_drinks,
            'ingredients_list': ingredients_list,
            'drink_list': drinks_list,
        }

    def post(self, request):
        form_drinks = DrinkForm(request.POST)
        form_ingredients = IngredientForm(request.POST)

        if form_ingredients.is_valid():

            Ingredients.objects.create(
                name=form_ingredients.cleaned_data['name'],
                type=form_ingredients.cleaned_data['type']
            )
        else:
            messages.error(request, "Ingredient form was invalid")

        if form_drinks.is_valid():

            DrinkRecipe.objects.create(
                drinkName=form_drinks.cleaned_data['drinkName'],
                ingredient1=form_drinks.cleaned_data['ingredient1']
                # ingredient2=form_drinks.cleaned_data['ingredient2']
                # ingredient3=form_drinks.cleaned_data['ingredient3']
                # ingredient4=form_drinks.cleaned_data['ingredient4']
            )