# date-created: 19-feb-2022
# usage: return the json string after querying the database
# calling function/module: product/urls.py

from .serializers import (ProductSerializer, TagSerializer)
from .models import Product, Tag

from rest_framework.response import Response
from rest_framework import status
from rest_framework.request import Request
from rest_framework.decorators import api_view, permission_classes, authentication_classes
# below is the alternative to redundant code
# retrieve uses the pk(primary key for retrieval of the data)


@api_view(['GET'])
@permission_classes([])
@authentication_classes([])
def singleProductView(request, pk):
    # also get the feedback related to this product
    if request.method == 'GET':
        try:
            singleInstance = Product.objects.get(productId=pk)
            serializedData = ProductSerializer(
                singleInstance, many=False)
            return Response(data=serializedData.data)
        except Product.DoesNotExist:
            # for if the resulting query set is empty
            return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
@permission_classes([])
@authentication_classes([])
def tagListView(request):
    if request.method == 'GET':
        try:
            tagInstanceList = Tag.objects.all()
            serializedData = TagSerializer(
                tagInstanceList, many=True)
            return Response(data=serializedData.data)
        except Tag.DoesNotExist:
            # for if the resulting query set is empty
            return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
@permission_classes([])
@authentication_classes([])
def productListView(request, pincode='208012'):
    if request.method == 'GET':
        try:
            productInstanceList = Product.objects.all()
            serializedData = ProductSerializer(
                productInstanceList, many=True)
            return Response(data=serializedData.data)
        except Product.DoesNotExist:
            # for if the resulting query set is empty
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception:
            print(Exception.__cause__)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
@permission_classes([])
@authentication_classes([])
def productRegisterView(request):
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
