from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.http import HttpResponseRedirect

from .forms import IngredientForm, DrinkForm
from .models import Ingredients, DrinkRecipe


# Create your views here.
class IndexView(View):

    def get(self, request):
        form_ingredients = IngredientForm()
        form_drinks = DrinkForm()
        ingredients_list = Ingredients.objects.all()
        soft_drinks_list = Ingredients.objects.filter(type=1)
        alcohols_list = Ingredients.objects.filter(type=2)
        fruit_list = Ingredients.objects.filter(type=3)
        spices_list = Ingredients.objects.filter(type=4)
        drinks_list = DrinkRecipe.objects.all()
        context = {
            'form_ingredients': form_ingredients,
            'form_drinks': form_drinks,
            'ingredients_list': ingredients_list,
            'soft_drinks_list': soft_drinks_list,
            'alcohols_list': alcohols_list,
            'fruit_list': fruit_list,
            'spices_list': spices_list,
            'drink_list': drinks_list,
        }
        return render(request, 'shakerApp/index.html', context)

    def post(self, request):
        form_drinks = DrinkForm(request.POST)
        form_ingredients = IngredientForm(request.POST)

        if form_ingredients.is_valid():

            Ingredients.objects.create(
                name=form_ingredients.cleaned_data['name'],
                type=form_ingredients.cleaned_data['type']
            )
        else:
            messages.error(request, "Ingredient form was invalid.")

        if form_drinks.is_valid():

            DrinkRecipe.objects.create(
                drinkName=form_drinks.cleaned_data['drinkName'],
                ingredients=form_drinks.cleaned_data['ingredients']
            )
        else:
            messages.error(request, "Drinks form was invalid.")

        return HttpResponseRedirect(reverse('shakerApp:index'))


class AddIngredientView(View):

    def get(self, request):
        form_ingredients = IngredientForm()
        ingredients_list = Ingredients.objects.all()
        context = {
            'form_ingredients': form_ingredients,
            'ingredients_list': ingredients_list,
        }
        return render(request, 'shakerApp/add_ingredient.html', context)

    def post(self, request):
        form_ingredients = IngredientForm(request.POST)

        if form_ingredients.is_valid():

            Ingredients.objects.create(
                name=form_ingredients.cleaned_data['name'],
                type=form_ingredients.cleaned_data['type']
            )
        else:
            messages.error(request, "Ingredient form was invalid.")

        return HttpResponseRedirect(reverse('shakerApp:index'))

class AddDrinkView(View):

    def get(self, request):
        form_drinks = DrinkForm()
        drinks_list = DrinkRecipe.objects.all()
        context = {
            'form_drinks': form_drinks,
            'drinks_list': drinks_list,
        }
        return render(request, 'shakerApp/add_drink.html', context)

    def post(self, request):
        form_drinks = DrinkForm(request.POST)

        if form_drinks.is_valid():

            DrinkRecipe.objects.create(
                name=form_drinks.cleaned_data('name'),
                utensil=form_drinks.cleaned_data('utensil'),
                ingredients=form_drinks.cleaned_data('ingredients')

            )
        else:
            messages.error(request, "Drink form is invalid.")

        return HttpResponseRedirect(reverse('shakerApp:index'))
