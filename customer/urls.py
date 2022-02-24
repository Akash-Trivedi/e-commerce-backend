from django.urls import path
from . import views

urlpatterns = [
    path('list-all-customers/', views.CustomerView.as_view())
]
