from django.urls import path
from . import views

urlpatterns = [
    path('list-all/', views.CustomerListView.as_view()),
    path('register/', views.CustomerRegistrationView.as_view()),
    path('order-history/', views.CustomerOrderSummaryView.as_view()),
    path('feedback/list-all/', views.CustomerFeedbackView.as_view()),
]
