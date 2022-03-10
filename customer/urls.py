from django.urls import path
from . import views

urlpatterns = [
    path('list-all-customers/', views.CustomerView.as_view()),
    path('customer-registration/', views.CustomerRegistrationView.as_view()),
    path('customer-order-summary/', views.CustomerOrderSummaryView.as_view()),
]
