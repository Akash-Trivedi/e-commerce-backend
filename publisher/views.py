# # date-created: 17-feb-2022
# # usage:
# # calling function:
import publisher
from publisher.serializers import PublishAuthSerializer, ShopSerializer, PublisherSerializer
from . models import PublisherAuth, Shop, Publisher
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.request import Request
from rest_framework.decorators import api_view, permission_classes, authentication_classes


@api_view(['GET'])
@permission_classes([])
@authentication_classes([])
def publisherOrderListView(request):
    if request.method == 'GET':
        try:
            publisherInstanceList = Publisher.objects.all()
            serializedData = PublisherSerializer(
                publisherInstanceList, many=True)
            return Response(data=serializedData.data)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def registerPublisherView(request):
    if request.method == 'POST':
        try:
            # checks if the number already exists
            contactNumber = request.data['contactId']
            user = PublisherAuth.objects.filter(contactId=contactNumber).get()
            return Response(status=status.HTTP_409_CONFLICT)

        except PublisherAuth.DoesNotExist:
            instance = PublishAuthSerializer(data=request.data)
            if instance.is_valid():
                instance.save()
            return Response(status=status.HTTP_201_CREATED)

        except Exception:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([])
@authentication_classes([])
def publisherListView(request, pincode='208011'):
    if request.method == 'GET':
        try:
            publisherInstanceList = Publisher.objects.get(pincode=pincode)
            serializedData = PublisherSerializer(
                publisherInstanceList)
            return Response(data=serializedData.data)
        except Publisher.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@permission_classes([])
@authentication_classes([])
def listShopView(request, pincode='208011'):
    if request.method == 'GET':
        try:
            publisherInstanceList = Shop.objects.get(pincode=pincode)
            serializedData = PublisherSerializer(
                publisherInstanceList, many=True)
            return Response(data=serializedData.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
