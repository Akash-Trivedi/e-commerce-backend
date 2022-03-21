# # date-created: 17-feb-2022
# # usage:
# # calling function:
from multiprocessing import AuthenticationError
from os import stat
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


def p():
    print('\n'+'-'*16+'NEW REQUEST'+'-'*16+'\n')


def publisherOrderListView(request):
    # orderHistory = {}
    # try:
    #     orders=
    pass


class PublisherSignupView(APIView):
    permission_classes=()
    def post(self, request):
        p()
        try:

            formData = request.data
            print(request.user)
            if(LocalUser.objects.filter(
                    username=formData['username'], isPublisher=True).exists()):
                return Response(data={'status': 409}, status=status.HTTP_409_CONFLICT)

            formData.update({'isPublisher': True})
            instance = LocalUserSerializer(data=formData)

            if instance.is_valid():
                print('1')
                user = LocalUser.objects.filter(
                    username=request.data['username'], isPublisher=True)
                print('2')
                refresh = RefreshToken.for_user(user=user)
                print('3')
                userId = LocalUser.objects.filter(
                    username=request.data['username'], isPublisher=True)
                print('4')
                token = {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }
                print('5')
                response = Response()
                print('6')
                response.set_cookie(key='pjwt', value=token, httponly=True)
                print('7')
                instance.save()
                return response
            else:
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        except Exception:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def publisherListView():
    data = {}
    try:
        publisherInstanceList = LocalUser.objects.get(isPublisher=True, id=2)
        serializedData = LocalUserSerializer(
            publisherInstanceList)
        data = serializedData.data
    except LocalUser.DoesNotExist:
        print('user does not exists')
    except Exception:
        print('some error occured')
    finally:
        return data


def listShopView(publisherId=2):
    data = {}
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


@api_view(['POST'])
def publisherLogin(request):
    if request.method == 'POST':
        try:
            # checks if the number already exists
            if request.data is not None:
                contactNumber = request.data['username']
                user = LocalUser.objects.get(username=contactNumber)
                return Response(status=status.HTTP_200_OK)

        except LocalUser.DoesNotExist:
            instance = LocalUserSerializer(data=request.data)
            if instance.is_valid():
                instance.save()
            return Response(status=status.HTTP_201_CREATED)

        except Exception:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def addShopView(request):
    if request.method == 'POST':
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
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


def productListView(shopid=2):
    data = {}
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


def listAllInfoView():
    data = {}
    data['shops'] = listShopView()
    data['publisherInfo'] = publisherListView()
    data['products'] = productListView(2)
    data['totalSales'] = 0
    for shop in data['shops']:
        print(shop)
        data['totalSales'] = shop['sales'] + data['totalSales']
    return data


@api_view(['POST'])
@permission_classes([])
@authentication_classes([])
def addProductView(request):
    print('\n'+'-'*16+'NEW REQUEST'+'-'*16+'\n')
    if request.method == 'POST':
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
    else:
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
# authentication will be required
def feedbackListView(request):
    print('\n'+'-'*16+'NEW REQUEST'+'-'*16+'\n')
    if request.method == 'GET':
        try:
            shopInstanceList = Shop.objects.all().filter(id=2)
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
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):
    def post(self, request):
        pass
