# date-created: 21-feb-2022
# usage: handle the urlconf path by calling respected views
# calling function: backendroot/urls.py

from django.urls import path
from . import views

urlpatterns = [

    path('list-all/', views.PublisherView.as_view()),

    path('shops-list-all/<slug:pincode>', views.ShopView.as_view()),

    path('publisher-registration/', views.registerPublisher),
]
