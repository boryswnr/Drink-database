from django.db import models

ingredientType = (
    (1, "Alcohol"),
    (2, "Soft drink"),
    (3, "Fruit"),
    (4, "Spice")
)

requiredUtensil = (
    (1, "Shaker"),
    (2, "Glass")
)


# Create your models here.
class Ingredients(models.Model):
    type = models.IntegerField(choices=ingredientType)
    name = models.CharField(max_length=100)


class DrinkRecipe(models.Model):
    drinkName = models.CharField(max_length=100)
    # ingredient1 = models.ManyToManyField(Ingredients, on_delete=models.CASCADE)
    # ingredient2 = models.ManyToManyField(Ingredients, on_delete=models.CASCADE)
    # ingredient3 = models.ManyToManyField(Ingredients, on_delete=models.CASCADE, null=True)
    # ingredient4 = models.ManyToManyField(Ingredients, on_delete=models.CASCADE, null=True)
    # ingredient5 = models.ManyToManyField(Ingredients, on_delete=models.CASCADE, null=True)
    # ingredient6 = models.ManyToManyField(Ingredients, on_delete=models.CASCADE, null=True)
    # ingredient7 = models.ManyToManyField(Ingredients, on_delete=models.CASCADE, null=True)
    # ingredient8 = models.ManyToManyField(Ingredients, on_delete=models.CASCADE, null=True)
    preparation = models.CharField(max_length=1000)
