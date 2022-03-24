# author: akash trivedi
# date-created: 1-march-2022
# functionality: handle the incomming requests
# caller: customer\urls.py


from users.models import LocalUser
from .models import Feedback
from .serializers import FeedbackSerializer, CustomerOrderSummarySerializer
from users.serializers import LocalUserSerializer

from rest_framework.decorators import (
    api_view, permission_classes, authentication_classes, APIView)
from rest_framework.response import Response
from rest_framework import status


class CustomerListView(APIView):
    def get(self, request):
        try:
            publisherInstanceList = LocalUser.objects.all()
            serializedData = LocalUserSerializer(
                publisherInstanceList, many=True)
            print(serializedData.data)
            return Response(data=serializedData.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CustomerFeedbackView(APIView):
    def get(self, request):
        try:
            data = {}
            feedbackInstanceList = Feedback.objects.all()
            serializedData = FeedbackSerializer(
                feedbackInstanceList, many=True)
            data['status'] = 200
            data['payload'] = serializedData.data
            return Response(data=data, status=status.HTTP_200_OK)
        except Feedback.DoesNotExists:
            data['status'] = 204
            data['payload'] = []
            return Response(data=data, status=status.HTTP_204_NO_CONTENT)


class CustomerOrderSummaryView(APIView):
    def get(self, request):
        try:
            feedbackInstanceList = Feedback.objects.all()
            serializedData = CustomerOrderSummarySerializer(
                feedbackInstanceList, many=True)
            print(serializedData.data)
            return Response(data=serializedData.data, status=status.HTTP_200_OK)
        except Feedback.DoesNotExists:
            return Response(status=status.HTTP_204_NO_CONTENT)


class CustomerRegistrationView(APIView):
    def post(self, request):
        try:
            # checks if the number already exists
            contactNumber = request.data['contactId']
            user = LocalUser.objects.filter(contactId=contactNumber).get()
            return Response(status=status.HTTP_409_CONFLICT)

        except LocalUser.DoesNotExist:
            instance = LocalUserSerializer(data=request.data)
            if instance.is_valid():
                instance.save()
            else:
                return Response(status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            return Response(status=status.HTTP_201_CREATED)

        except Exception:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CustomerUpdateView(APIView):
    def post(self, request):
        try:
            instance = LocalUserSerializer(data=request.data)
            if instance.is_valid():
                instance.save()
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except Exception:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
