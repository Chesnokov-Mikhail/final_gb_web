from django.urls import path
from . import views

handler400 = views.ErrorHandlers.as_view(error_code=400)
handler401 = views.ErrorHandlers.as_view(error_code=401)
handler403 = views.ErrorHandlers.as_view(error_code=403)
handler404 = views.ErrorHandlers.as_view(error_code=404)
handler500 = views.ErrorHandlers.as_view(error_code=500)

urlpatterns = [
    path('', views.GetIndex.as_view(), name='get_index'),
    path('recipes_all/', views.GetReciepAll.as_view(), name='recipe_all'),
    path('authors_all/', views.GetAuthorAll.as_view(), name='author_all'),
    path('product_all/', views.GetProductAll.as_view(), name='product_all'),
    path('categorie_all/', views.GetCategorieAll.as_view(), name='categorie_all'),
    path('add_categorie/', views.PostCategorie.as_view(), name='add_categorie'),
    path('categorie/<int:categorie_id>/', views.GetCategorie.as_view(), name='get_categorie'),
    path('categorie/<int:categorie_id>/<str:edit>', views.PostCategorie.as_view(), name='edit_categorie'),
    path('add_recipe/', views.PostRecipe.as_view(), name='add_recipe'),
    path('recipe/<int:recipe_id>/', views.GetRecipe.as_view(), name='get_recipe'),
    path('recipe/<int:recipe_id>/<str:edit>', views.PostRecipe.as_view(), name='edit_recipe'),
    path('add_product/', views.PostProduct.as_view(), name='add_product'),
    path('product/<int:product_id>/', views.GetProduct.as_view(), name='get_product'),
    path('product/<int:product_id>/<str:edit>', views.PostProduct.as_view(), name='edit_product'),
    path('add_author/', views.PostAuthor.as_view(), name='add_author'),
    path('author/<int:author_id>/', views.GetAuthor.as_view(), name='get_author'),
    path('author/<int:author_id>/<str:edit>', views.PostAuthor.as_view(), name='edit_author'),
]