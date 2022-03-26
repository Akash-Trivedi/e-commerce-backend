# author: akash trivedi
# date-created: 17-feb-2022
# functionality:
# caller:

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
    authentication_classes = (JWTAuthentication,)

    def get(self, request):
        data = {
            'status': 500,
            'orderHistory': []
        }
        try:
            pass
        except Exception:
            print('some error occured')
        else:
            data['status'] = 200
        finally:
            return Response(data=data, status=status.HTTP_200_OK)


class PublisherSignupView(APIView):

    permission_classes = (AllowAny,)

    def post(self, request):
        p()
        data = {
            'status': 500,
            'data': {
                'token': {},
                'userInfo': {}
            }
        }
        try:
            formData = request.data
            user = LocalUser.objects.get(username=formData['username'])
            data['status'] = 409
            return Response(data=data, status=status.HTTP_409_CONFLICT)

        except LocalUser.DoesNotExist:
            instance = LocalUserSerializer().create(formData, isPublisher=True)
            data['status'] = 201
            data['data']['userInfo'] = LocalUserSerializer(
                instance=instance).data
            refresh = RefreshToken.for_user(instance)
            data['data']['token'] = {
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            }
        except Exception:
            print('some error occured')
        else:
            data['status'] = 201
        finally:
            print(data)
            return Response(data=data, status=status.HTTP_200_OK)


def publisherInfoView(publisherId=1):
    print(f'publisherListView called for id={publisherId}')
    data = {}
    try:
        publisherInstanceList = LocalUser.objects.get(id=publisherId)
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
    print(f'listShopView called for id={publisherId}')
    data = []
    try:
        shopInstance = Shop.objects.filter(id_id=publisherId)
        serializedData = ShopSerializer(
            instance=shopInstance, many=True)
        data = serializedData.data
    except Shop.DoesNotExist:
        print('Shops does not exists')
    except Exception:
        print('Exception occured')
    finally:
        return data


def feedackListView(publisherId):
    print(f'feedbackListView called for shopId={publisherId}')

    data = []
    try:
        shopInstance = Shop.objects.filter(id_id=publisherId)
        serializedData = ShopSerializer(
            instance=shopInstance, many=True)

        data = serializedData.data
    except Shop.DoesNotExist:
        print('Shops does not exists')
    except Exception:
        print('Exception occured')
    finally:
        return data


class PublisherLogin(APIView):
    permission_classes = (IsAuthenticated, )
    authentication_classes = (JWTAuthentication, )

    def post(self, request):
        p()
        print(request.user.id)
        try:
            exists = LocalUser.objects.filter(
                username=request.data['username'], password=request.data['password'])
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
    authentication_classes = (JWTAuthentication,)

    def post(self, request):
        p()
        print(f'AddShopView called for id={request.user.id}')
        data = {
            'status': 500,
            'shops': []
        }
        try:
            formData = request.data
            shop = Shop.objects.get(name=formData['name'])
            data['status'] = 409

        except Shop.DoesNotExist:
            print('shop is new!')
            instance = ShopSerializer().create(
                validated_data=formData, publisherId=request.user.id)
            shopInstance = Shop.objects.filter(id_id=request.user.id)
            data['shops'] = ShopSerializer(
                instance=shopInstance, many=True).data
            data['status'] = 201

        except Exception:
            print('some error in AddShopView')

        finally:
            return Response(data=data, status=status.HTTP_200_OK)


def productListView(shopid=2):
    print('productListView called')
    data = []
    try:
        shopInstance = Product.objects.filter(shopId_id=shopid)
        serializedData = ProductSerializer(
            shopInstance, many=True)
        data = serializedData.data
    except Shop.DoesNotExist:
        print('Shops does not exists')
    except Exception:
        print('Exception occured')
    finally:
        return data


def getAllPublisherInfo(id):
    print(f'publisherInfoView called for id={id}')
    data = {}
    data['shops'] = listShopView(id)
    data['userInfo'] = publisherInfoView(id)
    data['publisherProducts'] = []
    data['feedbacks'] = []
    data['totalSales'] = 0
    for shop in data['shops']:
        data['totalSales'] = shop['sales'] + data['totalSales']
    for shop in data['shops']:
        data['publisherProducts'] = productListView(shop['shopId'])
    return data


class AddProductView(APIView):
    authentication_classes = (JWTAuthentication,)

    def post(self, request):
        p()
        print(f'AddProductView for id={request.user.id}')
        data = {
            'status': 500,
        }
        try:
            formData = request.data
            product = Product.objects.get(name=formData['name'])
            data['status'] = 409
            return Response(data=data, status=status.HTTP_409_CONFLICT)

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


class FeedbackListView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)

    def get(self, request):
        p()
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
        p()
        print(f'PublisherInfoView called for id={request.user.id}')
        data = {
            'status': 200,
            'data': getAllPublisherInfo(request.user.id)
        }
        return Response(data=data, status=status.HTTP_200_OK)


class PublisherProfileUpdateView(APIView):
    authentication_classes = (JWTAuthentication,)

    def put(self, request):
        p()
        formData = request.data
        print(f'PublisherInfoView called for id={request.user.id}')
        data = {'status': 500}
        instance = LocalUser.objects.get(id=request.user.id)
        udpatedInstance = LocalUserSerializer().update(instance=instance,
                                                       validated_data=formData)
        data['userInfo'] = LocalUserSerializer(instance=udpatedInstance).data
        data['status'] = 201

        return Response(data=data, status=status.HTTP_201_CREATED)
