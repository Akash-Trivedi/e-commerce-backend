from django.urls import path
from . import views

urlpatterns = [
    path('list-all/', views.customerListView),
    path('register/', views.customerRegistrationView),
    path('order-history/', views.customerOrderSummaryView),
    path('feedbacks/', views.customerFeedbackView),
]
