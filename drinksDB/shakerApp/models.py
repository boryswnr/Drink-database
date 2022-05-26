from django.db import models

ingredientType = (
    (1, "Soft drink"),
    (2, "Alcohol"),
    (3, "Fruit"),
    (4, "Spice")
)

requiredUtensil = (
    (1, "Glass"),
    (2, "Shaker")
)

"""Defining a type as a class will allow to make a group ChoiceField
    despite using ModelChoiceField and not regular ChoiceField at DrinkRecipe model"""


class Type(models.Model):
    name = models.IntegerField(choices=ingredientType)
    parent = models.ForeignKey('Type', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Ingredients(models.Model):
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class DrinkRecipe(models.Model):
    drinkName = models.CharField(max_length=100)
    ingredients = models.ManyToManyField(Ingredients)
    preparation = models.CharField(max_length=1000)
