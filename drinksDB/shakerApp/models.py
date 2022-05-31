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


class Ingredients(models.Model):
    type = models.IntegerField(choices=ingredientType)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class DrinkRecipe(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.ManyToManyField(Ingredients)
    utensil = models.IntegerField(choices=requiredUtensil, default=0)
    preparation = models.CharField(max_length=1000)

    def __str__(self):
        return self.name
