# date-created: 19-feb-2022
# usage: map the url and views in the app 'product'
# calling function/module: backendroot/urls.py


from django.urls import path
from . import views

# passing the values from url can be handeled and values are passed to views

urlpatterns = [
    path('tags-all/', views.TagView.as_view()),
    path('products-all/', views.ProductView.as_view()),
    path('register/', views.ProductView.as_view()),
]
