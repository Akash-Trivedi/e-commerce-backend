from dataclasses import fields
from .models import Customer, CustomerAuth, Feedback, OrderSummary
from rest_framework.serializers import ModelSerializer


class CustomerSerializer(ModelSerializer):
    class Meta():
        model = Customer
        fields = '__all__'


class CustomerOrderSummarySerializer(ModelSerializer):
    class Meta():
        model = OrderSummary
        fields = '__all__'


class CustomerAuthSerializer(ModelSerializer):
    class Meta():
        model = CustomerAuth
        fields = '__all__'


class CustomerFeedbackSerializer(ModelSerializer):
    class Meta():
        model = Feedback
        fields = '__all__'
