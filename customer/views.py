# author: akash trivedi
# date-created: 1-march-2022
# functionality: handle the incomming requests
# caller: customer\urls.py


from .models import (Customer, CustomerAuth, Feedback)
from .serializers import (
    CustomerSerializer, CustomerAuthSerializer, CustomerOrderSummarySerializer, CustomerFeedbackSerializer)

from rest_framework.decorators import (
    api_view, permission_classes, authentication_classes)
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
@permission_classes([])
@authentication_classes([])
def customerListView(request):
    if request.method == 'GET':
        try:
            publisherInstanceList = Customer.objects.all()
            serializedData = CustomerSerializer(
                publisherInstanceList, many=True)
            print(serializedData.data)
            return Response(data=serializedData.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@permission_classes([])
@authentication_classes([])
def customerFeedbackView(request):
    if request.method == 'GET':
        try:
            feedbackInstanceList = Feedback.objects.all()
            serializedData = CustomerFeedbackSerializer(
                feedbackInstanceList, many=True)
            print(serializedData.data)
            return Response(data=serializedData.data, status=status.HTTP_200_OK)
        except Feedback.DoesNotExists:
            return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@permission_classes([])
@authentication_classes([])
def customerOrderSummaryView(request):
    if request.method == 'GET':
        try:
            feedbackInstanceList = Feedback.objects.all()
            serializedData = CustomerFeedbackSerializer(
                feedbackInstanceList, many=True)
            print(serializedData.data)
            return Response(data=serializedData.data, status=status.HTTP_200_OK)
        except Feedback.DoesNotExists:
            return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
@permission_classes([])
@authentication_classes([])
def customerRegistrationView(request):
    if request.method == 'POST':
        try:
            # checks if the number already exists
            contactNumber = request.data['contactId']
            user = CustomerAuth.objects.filter(contactId=contactNumber).get()
            return Response(status=status.HTTP_409_CONFLICT)

        except CustomerAuth.DoesNotExist:
            instance = CustomerAuthSerializer(data=request.data)
            if instance.is_valid():
                instance.save()
            else:
                return Response(status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            return Response(status=status.HTTP_201_CREATED)

        except Exception:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([])
@authentication_classes([])
def customerUpdateView(request):
    if request.method == 'POST':
        try:
            instance = CustomerAuthSerializer(data=request.data)
            if instance.is_valid():
                instance.save()
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except Exception:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
