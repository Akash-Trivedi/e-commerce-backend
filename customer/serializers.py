from customer.models import Customer
from rest_framework import serializers

class CustomerSerializer(serializers.Serializer):
    class Meta():
        model = Customer
        fields = '__all__'

class CustomerOrderSummarySerializer(serializers.Serializer):
    class Meta():
        model = Customer
        fields = '__all__'
