# date-created: 19-feb-2022
# usage: map the url and views in the app 'product'
# calling function/module: backendroot/urls.py


from django.urls import path
from . import views

# passing the values from url can be handeled and values are passed to views

urlpatterns = [
    path('tags/list-all/', views.TagListView.as_view()),
    path('list-all/<slug:pincode>/', views.ProductListView.as_view()),
    path('<int:pk>/', views.SingleProductView.as_view()),
]
