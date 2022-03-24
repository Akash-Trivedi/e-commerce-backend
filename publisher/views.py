# # date-created: 17-feb-2022
# # usage:
# # calling function:
from rest_framework_simplejwt.backends import TokenBackend
from email.policy import HTTP
from multiprocessing import AuthenticationError
from os import stat
from weakref import ref
from product.models import Product, Tag
from product.serializers import ProductSerializer
from publisher.serializers import ShopSerializer
from customer.serializers import FeedbackSerializer
from customer.models import Feedback
from users.models import LocalUser
from . models import Shop
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import (
    api_view, permission_classes, authentication_classes, APIView)
from users.serializers import LocalUserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import AllowAny


def p():
    print('\n'+'-'*16+'NEW REQUEST'+'-'*16+'\n')


class PublisherOrderListView(APIView):
    pass


class PublisherSignupView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        p()
        if request.data['username'] != '' and request.data['password'] != '':
            try:
                formData = request.data
                user = LocalUser.objects.get(username=formData['username'])
                return Response(data={'status': 409}, status=status.HTTP_409_CONFLICT)
            except LocalUser.DoesNotExist:
                instance = LocalUserSerializer().create(formData)
                newUser = LocalUser.objects.get(
                    username=request.data['username'])
                userSerilazedData = LocalUserSerializer(instance=newUser)
                refresh = RefreshToken.for_user(newUser)
                token = {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token)
                }
                return Response(data={'status': 201, 'data': userSerilazedData.data, 'token': token}, status=status.HTTP_201_CREATED)

            except Exception:
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(data={status: 204}, status=status.HTTP_204_NO_CONTENT)


def publisherListView(id):
    data = []
    try:
        publisherInstanceList = LocalUser.objects.get(isPublisher=True, id=id)
        serializedData = LocalUserSerializer(
            publisherInstanceList)
        data = serializedData.data
    except LocalUser.DoesNotExist:
        print('user does not exists')
    except Exception:
        print('some error occured')
    finally:
        return data


def listShopView(publisherId):
    data = []
    try:
        shopInstance = Shop.objects.filter(id_id=publisherId)
        serializedData = ShopSerializer(
            shopInstance, many=True)
        # many equal to true returns array1?
        data = serializedData.data
    except Shop.DoesNotExist:
        print('Shops does not exists')
    except Exception:
        print('Exception occured')
    finally:
        return data


class PublisherLogin(APIView):
    permission_classes=(IsAuthenticated, )
    authentication_classes = (JWTAuthentication, )

    def post(self, request):
        p()
        print(request.user.id)
        try:
            exists = LocalUser.objects.filter(
                username=request.data['username'], password=request.data['password'])
            # then create cookei and add session id to it
            data = {
                'status': 200,
                'data': publisherInfoView(request.user.id)
            }
            return Response(data=data, status=status.HTTP_200_OK)

        except LocalUser.DoesNotExist:
            return Response(data={'status': 404}, status=status.HTTP_404_NOT_FOUND)

        except Exception:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class AddShopView(APIView):
    def post(self, request):
        print('\n'+'-'*16+'NEW REQUEST'+'-'*16+'\n')
        try:
            formData = request.data
            # checks if the number already exists
            shop = Shop.objects.get(name=formData['name'])
            return Response(status=status.HTTP_409_CONFLICT)

        except Shop.DoesNotExist:
            # add value True to isPublisher key of dictionary->formData
            formData.update({'id': 2})
            instance = ShopSerializer(data=formData)
            if instance.is_valid():
                instance.save()
                shops = Shop.objects.filter(id_id=2)
                data = ShopSerializer(instance=shops, many=True)

                return Response(data=data.data, status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        except Exception:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def productListView(shopid=2):
    data = []
    try:
        shopInstance = Product.objects.filter(shopId_id=shopid)
        serializedData = ProductSerializer(
            shopInstance, many=True)
        # many equal to true returns array1?
        data = dict(serializedData.data)
        print(data)
    except Shop.DoesNotExist:
        print('Shops does not exists')
    except Exception:
        print('Exception occured')
    finally:
        return data


def publisherInfoView(id):
    data = {}
    data['shops'] = listShopView(id)
    data['publisherInfo'] = publisherListView(id)
    data['products'] = productListView(2)
    data['totalSales'] = 0
    for shop in data['shops']:
        data['totalSales'] = shop['sales'] + data['totalSales']
    return data


class AddProductView(APIView):

    def post(self, request):
        print('\n'+'-'*16+'NEW REQUEST'+'-'*16+'\n')
        data = {}
        try:
            productData = request.data
            # checks if the number already exists
            shop = Product.objects.get(name=productData['name'])
            return Response(status=status.HTTP_409_CONFLICT)

        except Product.DoesNotExist:
            shopInstance = Shop.objects.get(shopId=1)
            tagInstance = Tag.objects.get(tagId=11)
            if shopInstance and tagInstance:
                instance = Product.objects.create(
                    name=productData['name'], companyName=productData['companyName'],
                    description=productData['description'], stock=productData['stock'], price=productData['price'], size=productData[
                        'size'], color=productData['color'], discount=productData['discount'], edition=productData['edition'],
                    shopId=shopInstance, tagId=tagInstance
                )
                instance.save()
                productInstance = Product.objects.all().filter(shopId_id=2)
                data1 = ProductSerializer(
                    instance=productInstance, many=True)
                return Response(data=data1.data, status=status.HTTP_201_CREATED)
            else:
                return Response(data={}, status=status.HTTP_208_ALREADY_REPORTED)

        except Exception:
            return Response(data=data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class FeedbackListView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)

    def get(self, request):
        print('\n'+'-'*16+'NEW REQUEST'+'-'*16+'\n')
        try:
            shopInstanceList = Shop.objects.all().filter(id=request.username)
            serializedShopData = ShopSerializer(
                instance=shopInstanceList, many=True).data
            feedbackInstanceList = Feedback.objects.filter(
                shopId__in=[1, 2])
            serializedFeedbackData = FeedbackSerializer(
                instance=feedbackInstanceList, many=True)
            return Response(data=serializedFeedbackData.data, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            # for if the resulting query set is empty
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception:
            print(Exception.__cause__)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class PublisherInfoView(APIView):
    authentication_classes = (JWTAuthentication,)

    def get(self, request):
        data = {
            'status': 200,
            'data': publisherInfoView(request.user.username)
        }
        return Response(data=data, status=status.HTTP_200_OK)
