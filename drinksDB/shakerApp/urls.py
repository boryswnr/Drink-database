from django.urls import path
from . import views

app_name = "shakerApp"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('add_ingredient/', views.AddIngredientView.as_view(), name='add_ingredient'),
    path('add_drink/', views.AddDrinkView.as_view(), name='add_drink'),
]