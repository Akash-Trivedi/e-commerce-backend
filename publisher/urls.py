# date-created: 21-feb-2022
# usage: handle the urlconf path by calling respected views
# calling function: backendroot/urls.py

from django.urls import path
from . import views

urlpatterns = [

    # for listing all the publishers in the area by pincode
    path('list-all/<slug:pincode>', views.publisherListView),
    
    # list all the shops by pincode
    path('shop/list-all/<slug:pincode>', views.listShopView),

    # handle the new publisher registration
    path('register/', views.registerPublisherView),
    path('order-history/', views.publisherOrderListView),
    path('login/', views.publisherLogin),
]
