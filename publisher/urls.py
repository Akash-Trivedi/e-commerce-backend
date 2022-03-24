# date-created: 21-feb-2022
# usage: handle the urlconf path by calling respected views
# calling function: backendroot/urls.py

from django.urls import path
from . import views

urlpatterns = [

    # for listing all the publishers in the area by pincode

    # list all the shops by pincode
    path('shop/add/', views.AddShopView.as_view()),
    path('product/add/', views.AddProductView.as_view()),

    # handle the new publisher registration
    path('signup/', views.PublisherSignupView.as_view()),
    path('order-history/', views.PublisherOrderListView.as_view()),
    path('login/', views.PublisherLogin.as_view()),
    path('feedback/list-all/', views.FeedbackListView.as_view()),
    path('all-info/', views.PublisherInfoView.as_view()),
]
