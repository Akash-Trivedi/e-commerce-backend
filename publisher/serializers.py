# date-created: 20-feb-2022
# usage:
# calling function: publisher/views.py

from rest_framework import serializers
from .models import PublisherAuth, Shop, Publisher


class PublishAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublisherAuth
        fields = '__all__'


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'
