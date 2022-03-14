# author: akash trivedi
# date-created: 10-march-2022
# functionality: conatins the views related to utility for the website like sending otp
# caller: api\urls.py

import random
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from publisher.serializers import PublishAuthSerializer
from publisher.models import PublisherAuth
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes


@api_view(['GET'])
@permission_classes([])
@authentication_classes([])
def randomOtp(request, contactNumber):
    try:
        # checks if the number already exists
        user = PublisherAuth.objects.filter(contactId=contactNumber).get()
        return Response(status=status.HTTP_409_CONFLICT)

    except PublisherAuth.DoesNotExist:
        # can be improved
        otp = random.randrange(100000, 999999)
        # below goes in terminal of the server
        print(f'otp for {contactNumber} is {otp}')
        context = {
            "otpFromServer": otp
        }
        return Response(data=context, status=status.HTTP_200_OK)