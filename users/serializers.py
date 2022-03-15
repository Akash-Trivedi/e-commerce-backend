from dataclasses import fields
from rest_framework.serializers import ModelSerializer
from . models import LocalUser


class LocalUserSerializer(ModelSerializer):
    class Meta():
        model = LocalUser
        fields = '__all__'
