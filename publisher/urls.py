# date-created: 21-feb-2022
# usage: handle the urlconf path by calling respected views
# calling function: backendroot/urls.py

from django.urls import path
from . import views

urlpatterns = [

    # for listing all the publishers in the area by pincode
    path('list-all/', views.publisherListView),
    
    # list all the shops by pincode
    path('all-info/', views.listAllInfoView),
    path('shop/add/', views.addShopView),
    path('product/add/', views.addProductView),

    # handle the new publisher registration
    path('signup/', views.publisherSignupView),
    path('order-history/', views.publisherOrderListView),
    path('login/', views.publisherLogin),
]
