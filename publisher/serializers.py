# date-created: 20-feb-2022
# usage:
# calling function: publisher/views.py

from rest_framework import serializers
from .models import PublisherAuth, Shop, Publisher


class PublishAuthSerializer(serializers.ModelSerializer):
    '''
    serialize the instance into json and json to istance, for the coressponding model provided in the Meta class
    NOTE : this serializer is under discussion becuase it contains the user contact number and their coressponding passwords, so we don't want to send the json response containing the credentials.
    '''
    class Meta:
        '''
        this class is tells the serializer to return the list of fields equal to fields attribute given and model equal to model provided
        '''
        model = PublisherAuth
        fields = '__all__'


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


class PublisherSerializer(serializers.ModelSerializer):
    '''
    serialize the instance into json and json to istance, for the coressponding model provided in the Meta class
    '''
    class Meta:
        '''
        this class is tells the serializer to return the list of fields equal to fields attribute given and model equal to model provided
        '''
        model = Publisher
        fields = '__all__'
