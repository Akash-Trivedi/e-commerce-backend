# date-created: 20-feb-2022
# usage:
# calling function: publisher/views.py

from rest_framework import serializers
from .models import Shop


class ShopSerializer(serializers.ModelSerializer):
    '''
    serialize the instance into json and json to istance, for the coressponding model provided in the Meta class
    '''
    class Meta:
        '''
        this class is tells the serializer to return the list of fields equal to fields attribute given and model equal to model provided
        '''
        model = Shop
        fields = '__all__'

