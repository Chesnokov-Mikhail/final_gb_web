from django.urls import path
from . import views

urlpatterns = [
    path('', views.GetIndex.as_view(), name='get_index'),
    path('recipes_all/', views.GetReciepAll.as_view(), name='recipe_all'),
    path('add_recipe/', views.PostRecipe.as_view(), name='add_recipe'),
    path('recipe/<int:recipe_id>/', views.PostRecipe.as_view(), name='get_recipe'),
    path('recipe/<int:recipe_id>/<str:edit>', views.PostRecipe.as_view(), name='edit_recipe'),
]