# date-created: 19-feb-2022
# usage: return the json string after querying the database
# calling function/module: product/urls.py

from customer.models import Feedback
from customer.serializers import FeedbackSerializer
from publisher.models import Shop
from publisher.serializers import ShopSerializer
from .serializers import (ProductSerializer, TagSerializer)
from .models import Product, Tag

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes, APIView


class SingleProductView(APIView):
    def get(self, request, pk):
        try:
            singleInstance = Product.objects.get(productId=pk)
            serializedData = ProductSerializer(
                singleInstance, many=False)
            return Response(data=serializedData.data)
        except Product.DoesNotExist:
            # for if the resulting query set is empty
            return Response(status=status.HTTP_404_NOT_FOUND)


class TagListView(APIView):
    def get(self, request):
        try:
            tagInstanceList = Tag.objects.all()
            serializedData = TagSerializer(
                tagInstanceList, many=True)
            return Response(data=serializedData.data, status=status.HTTP_200_OK)
        except Tag.DoesNotExist:
            return Response(data={}, status=status.HTTP_404_NOT_FOUND)


class ProductListView(APIView):
    def get(self, request, pincode=208012):
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


class ProductRegisterView(APIView):
    def post(self, request):
        pass


class FeedbackListView(APIView):
    def get(self, request):
        try:
            shopInstanceList = Shop.objects.all().filter(id=2)
            serializedShopData = ShopSerializer(
                instance=shopInstanceList, many=True).data
            print(serializedShopData)
            feedbackInstanceList = Feedback.objects.all().filter(shopId='')
            serializedFeedbackData = FeedbackSerializer(
                feedbackInstanceList, many=True)
            return Response(data=serializedFeedbackData.data)
        except Product.DoesNotExist:
            # for if the resulting query set is empty
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception:
            print(Exception.__cause__)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
