# # date-created: 17-feb-2022
# # usage:
# # calling function:
from product.models import Product
from product.serializers import ProductSerializer
from publisher.serializers import ShopSerializer
from users.models import LocalUser
from . models import Shop
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from users.serializers import LocalUserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


def publisherOrderListView(request):
    # orderHistory = {}
    # try:
    #     orders=
    pass


@api_view(['POST'])
def publisherSignupView(request):
    if request.method == 'POST':
        try:
            formData = dict(request.data)
            # checks if the number already exists
            user = LocalUser.objects.get(username=formData['username'])
            return Response(status=status.HTTP_409_CONFLICT)

        except LocalUser.DoesNotExist:
            # add value True to isPublisher key of dictionary->formData
            formData['isPublisher'] = True
            instance = LocalUserSerializer(data=formData)
            if instance.is_valid():
                instance.save()
                user = LocalUser.objects.get(
                    username=request.data['username'], isPublisher=True)
                refresh = RefreshToken.for_user(user)
                data = {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }
                return Response(data=data, status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        except Exception:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


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
        try:
            formData = dict(request.data)
            # checks if the number already exists
            shop = Shop.objects.get(name=formData['name'])
            return Response(status=status.HTTP_409_CONFLICT)

        except Shop.DoesNotExist:
            # add value True to isPublisher key of dictionary->formData
            formData['id'] = 2
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


@api_view(['GET'])
def listAllInfoView(request):
    data = {}
    data['shops'] = listShopView()
    data['publisherInfo'] = publisherListView()
    data['products'] = productListView(2)
    return Response(data=data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([])
@authentication_classes([])
def addProductView(request):
    if request.method == 'POST':
        data = {}
        try:
            productData = request.data
            print(f'this is data from request -> {productData}')
            # checks if the number already exists
            shop = Product.objects.get(name=productData['name'])
            return Response(status=status.HTTP_409_CONFLICT)

        except Product.DoesNotExist:
            # add value True to isPublisher key of dictionary->formData
            productData.update({'shopId':1, 'tagId':11})
            print(f'this is data after further adding column data -> {productData}')
            instance = ProductSerializer(data=productData)
            print(f'this is instanceafter Product Serializer -> {instance}')
            if instance.is_valid():
                instance.save()
                productInstance = Product.objects.get(shopId_id=2)
                data1 = ProductSerializer(instance=productInstance, many=True)
                print(f'this is serialized data from instance -> {data1.data}')
                return Response(data=data1.data, status=status.HTTP_201_CREATED)
            else:
                return Response(data=data)

        except Exception:
            return Response(data=data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
