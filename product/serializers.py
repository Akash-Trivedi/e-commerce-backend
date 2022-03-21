# date-created: 19-feb-2022
# usage: convert the json data to object(data=) and vice versa()
# calling function/module: product/views.py

from rest_framework import serializers
from .models import Product, Tag
from publisher.models import Shop


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('tagId', 'tagName')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

        extra_kwargs = {
            'timeStamp': {
                'write_only': True
            }
        }
