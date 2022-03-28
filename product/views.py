# date-created: 19-feb-2022
# usage: return the json string after querying the database
# calling function/module: product/urls.py

from itertools import product
from customer.models import Feedback
from customer.serializers import FeedbackSerializer
from publisher.models import Shop
from publisher.serializers import ShopSerializer
from .serializers import (ProductSerializer, TagSerializer)
from .models import Product, Tag

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes, APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import AllowAny


def p():
    print('\n'+'-'*16+'NEW REQUEST'+'-'*16+'\n')


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


class AddProductView(APIView):
    authentication_classes = (JWTAuthentication,)

    def post(self, request):
        p()
        print(f'AddProductView for id={request.user.id}')
        data = {
            'status': 500,
            'products': None
        }
        try:
            formData = request.data
            product = Product.objects.get(name=formData['name'])
            data['status'] = 409

        except Product.DoesNotExist:
            data1 = ProductSerializer().create(validated_data=formData)
            data['status'] = 201
            instances = Product.objects.all()
            data['products'] = ProductSerializer(
                instance=instances, many=True).data

        except Exception:
            print(f'some error occured in AddProductView')

        finally:
            return Response(data=data, status=status.HTTP_200_OK)

    def put(self, request):
        pass


class ProductsByTagView(APIView):
    permission_classes = (AllowAny, )

    def get(self, request, tagId):
        try:
            data = {
                'status': 500,
                'products': []
            }

            productInstances = Product.objects.filter(tagId_id=tagId)
            data['products'] = ProductSerializer(
                instance=productInstances, many=True).data

        except Product.DoesNotExist:
            data['status'] = 404
        except Exception:
            print('some error occured in ProductsByTag view')

        else:
            data['status'] = 200

        finally:
            return Response(data=data, status=status.HTTP_200_OK)


class UpdateProductView(APIView):
    authentication_classes = (JWTAuthentication, )

    def post(self, request):
        p()
        data = {
            'status': 500,
            'product': None
        }
        try:
            formData = request.data
            data1 = ProductSerializer().create(validated_data=formData)
            data['status'] = 201
            instances = Product.objects.all()
            data['products'] = ProductSerializer(
                instance=instances, many=True).data

        except Exception:
            print('some error occured')

        else:
            data['status'] = 201
        finally:
            return Response(data=data, status=status.HTTP_201_CREATED)
