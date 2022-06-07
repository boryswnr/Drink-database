from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from django.http import HttpResponseRedirect

from .forms import IngredientForm, DrinkForm, SearchIngredientsForm, LoginForm, RegistrationForm
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


class AddIngredientView(LoginRequiredMixin, View):

    def get(self, request):
        form_ingredients = IngredientForm()
        ingredients_list = Ingredients.objects.all()
        context = {
            'form_ingredients': form_ingredients,
            'ingredients_list': ingredients_list,
        }
        return render(request, 'shakerApp/add_ingredient.html', context)

    def post(self, request):
        form_ingredients = IngredientForm(request.POST, request.FILES)

        if form_ingredients.is_valid():

            Ingredients.objects.create(
                name=form_ingredients.cleaned_data['name'],
                type=form_ingredients.cleaned_data['type'],
                image=form_ingredients.cleaned_data['image'],

            )
        else:
            messages.error(request, "Ingredient form was invalid.")

        return HttpResponseRedirect(reverse('shakerApp:index'))


class AddDrinkView(LoginRequiredMixin, View):

    def get(self, request):
        form_drinks = DrinkForm()
        drinks_list = DrinkRecipe.objects.all()
        context = {
            'form_drinks': form_drinks,
            'drinks_list': drinks_list,
        }
        return render(request, 'shakerApp/add_drink.html', context)

    def post(self, request):
        form_drinks = DrinkForm(request.POST, request.FILES)

        if form_drinks.is_valid():
            new_drink = DrinkRecipe.objects.create(
                name=form_drinks.cleaned_data['name'],
                utensil=form_drinks.cleaned_data['utensil'],
                preparation=form_drinks.cleaned_data['preparation'],
                image=form_drinks.cleaned_data['image'],
            )
            new_drink.ingredients.set(form_drinks.cleaned_data["ingredients"])
        else:
            messages.error(request, "Drink form is invalid.")
            print('form_drinks:', form_drinks)

        return HttpResponseRedirect(reverse('shakerApp:index'))


class EditDrinkView(LoginRequiredMixin, View):

    def get(self, request, pk):
        drink = get_object_or_404(DrinkRecipe, pk=pk)
        form = DrinkForm(
            initial={
                'image': drink.image,
                'name': drink.name,
                'utensil': drink.utensil,
                'ingredients': drink.ingredients.all(),
                'preparation': drink.preparation,
            }
        )

        context = {
            'drink': drink,
            'form': form
        }

        return render(request, 'shakerApp/edit_drink.html', context)

    def post(self, request, pk):
        drink = get_object_or_404(DrinkRecipe, pk=pk)
        form = DrinkForm(request.POST, request.FILES)
        if form.is_valid():
            drink.image = form.cleaned_data["image"]
            drink.name = form.cleaned_data["name"]
            drink.utensil = form.cleaned_data["utensil"]
            drink.preparation = form.cleaned_data["preparation"]
            drink.ingredients.set(form.cleaned_data["ingredients"])
            drink.save()

        return HttpResponseRedirect(reverse('shakerApp:index'))


class DeleteDrinkView(LoginRequiredMixin, View):

    def get(self, request, pk):
        drink = get_object_or_404(DrinkRecipe, pk=pk)
        drink.delete()
        messages.info(request, "Drink deleted successfully.")

        return HttpResponseRedirect(reverse('shakerApp:index'))


class DetailDrinkView(View):

    def get(self, request, pk):
        drink = get_object_or_404(DrinkRecipe, pk=pk)

        context = {
            'name': drink.name,
            'utensil': drink.utensil,
            'ingredients': drink.ingredients.all(),
            'preparation': drink.preparation,
            'image': drink.image,
            'id': drink.id,
        }

        return render(request, 'shakerApp/drink_details.html', context)


class EditIngredientView(LoginRequiredMixin, View):

    def get(self, request, pk):
        ingredient = get_object_or_404(Ingredients, pk=pk)
        form = IngredientForm(
            initial={
                "type": ingredient.type,
                "name": ingredient.name,
                'image': ingredient.image,
            }
        )

        context = {
            'ingredient': ingredient,
            'form': form,
        }

        return render(request, "shakerApp/edit_ingredient.html", context)

    def post(self, request, pk):
        ingredient = get_object_or_404(Ingredients, pk=pk)
        form = IngredientForm(request.POST, request.FILES)

        if form.is_valid():
            ingredient.type = form.cleaned_data['type']
            ingredient.name = form.cleaned_data['name']
            ingredient.image = form.cleaned_data['image']
            ingredient.save()

        return HttpResponseRedirect(reverse('shakerApp:index'))


class DeleteIngredientView(LoginRequiredMixin, View):

    def get(self, request, pk):
        ingredient = get_object_or_404(Ingredients, pk=pk)
        ingredient.delete()
        messages.info(request, "Ingredient deleted successfully")

        return HttpResponseRedirect(reverse('shakerApp:index'))


class SearchIngredientsView(View):

    def get(self, request):
        form = SearchIngredientsForm()
        drinks = DrinkRecipe
        ingredients_model = Ingredients
        query = self.request.GET.get("q")
        ingredients_list = Ingredients.objects.filter(
            Q(name__icontains=query) | Q(type__icontains=query)
        )

        drinks_list = DrinkRecipe.objects.filter(
            ingredients__name__icontains=query
        )

        print('drinks_list.id:', drinks_list.id)

        context = {
            'form': form,
            'ingredients_model': ingredients_model,
            'drinks': drinks,
            'drinks_list': drinks_list,
            'ingredients_list': ingredients_list
        }
        

        return render(request, 'shakerApp/search_ingredients.html', context)


class LoginView(View):

    def get(self, request):
        form = LoginForm()
        context = {
            'form': form
        }
        return render(request, 'shakerApp/login.html', context)

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                url = request.GET.get('next')
                if url:
                    return redirect(url)

                return HttpResponseRedirect(reverse('shakerApp:index'))

            messages.error(request, "Username or password invalid")
            return HttpResponseRedirect(reverse('shakerApp:login'))

        messages.error(request, "Form was not valid")
        return HttpResponseRedirect(reverse('shakerApp:login'))


class LogoutView(View):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('shakerApp:index'))


class RegistrationView(View):

    def get(self, request):
        form = RegistrationForm()
        context = {
            "form": form
        }
        return render(request, 'shakerApp/register.html', context)

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            if form.cleaned_data["password"] == form.cleaned_data["password_conf"]:
                try:
                    User.objects.get(username=form.cleaned_data["username"])
                    messages.error(request, "User already exists")
                    return HttpResponseRedirect(reverse("shakerApp:registration"))
                except User.DoesNotExist:
                    user = User.objects.create_user(
                        username=form.cleaned_data["username"],
                        password=form.cleaned_data["password"],
                        email=form.cleaned_data["email"]
                    )
                    login(request, user)
                    return HttpResponseRedirect(reverse("shakerApp:index"))
            else:
                messages.error(request, "Passwords are wrong!")
                return HttpResponseRedirect(reverse("shakerApp:registration"))
