from django.urls import path
from . import views

urlpatterns = [
    path('', views.GetIndex.as_view(), name='get_index'),
    path('add_recipe/', views.PostRecipe.as_view(), name='add_recipe'),
]