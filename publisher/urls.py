# date-created: 21-feb-2022
# usage: handle the urlconf path by calling respected views
# calling function: backendroot/urls.py

from django.urls import path
from . import views

urlpatterns = [

    path('list-all-publishers/', views.PublisherView.as_view()),

    path('list-all-shops/', views.ShopView.as_view()),

    path('registerPublisher/', views.PublisherRegistration.as_view()),

]
