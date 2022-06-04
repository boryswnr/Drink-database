from django.urls import path
from . import views

app_name = "shakerApp"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('add_ingredient/', views.AddIngredientView.as_view(), name='add_ingredient'),
    path('add_drink/', views.AddDrinkView.as_view(), name='add_drink'),
    path('edit_drink/<int:pk>/', views.EditDrinkView.as_view(), name='edit_drink'),
    path('delete_drink/<int:pk>/', views.DeleteDrinkView.as_view(), name='delete_drink'),
    path('edit_ingredient/<int:pk>/', views.EditIngredientView.as_view(), name='edit_ingredient'),
    path('delete_ingredient/<int:pk>/', views.DeleteIngredientView.as_view(), name="delete_ingredient"),
    path('search_ingredients/', views.SearchIngredientsView.as_view(), name="search_ingredients")
]