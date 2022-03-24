from rest_framework.serializers import ModelSerializer
from . models import LocalUser


class LocalUserSerializer(ModelSerializer):
    class Meta():
        model = LocalUser
        fields = '__all__'

        option = {'write_only': True}
        extra_kwargs = {
            'username': option,
            'last_login': option,
            'is_superuser': option,
            'is_staff': option,
            'is_active': option,
            'date_joined': option,
            'password': option,
            'ipAddress': option,
            'browser': option,
            'groups': option,
            'user_permissions': option
        }

    def create(self, validated_data):
        user = LocalUser.objects.create(
            isPublisher=True,
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
