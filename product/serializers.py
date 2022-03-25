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

    def create(self, validated_data):
        product = Product.objects.create(
            name=validated_data['name'],
            companyName=validated_data['companyName'],
            description=validated_data['description'],
            stock=validated_data['stock'],
            price=validated_data['price'],
            size=validated_data['size'],
            color=validated_data['color'],
            discount=validated_data['discount'],
            edition=validated_data['edition'],
            feedBackValue=0,
            totalFeedbacks=0,
            shopId_id=validated_data['shopId_id'],
            tagId_id=validated_data['tagId_id']
        )
        product.save()
        print('new product created!')
        return product
