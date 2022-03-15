from .models import Feedback, OrderSummary
from rest_framework.serializers import ModelSerializer


class CustomerOrderSummarySerializer(ModelSerializer):
    class Meta():
        model = OrderSummary
        fields = '__all__'


class CustomerFeedbackSerializer(ModelSerializer):
    class Meta():
        model = Feedback
        fields = '__all__'
