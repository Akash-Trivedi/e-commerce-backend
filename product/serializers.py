# date-created: 19-feb-2022
# usage: convert the json data to object(data=) and vice versa()
# calling function/module: product/views.py

from rest_framework import serializers
from .models import  Product, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


