# # date-created: 17-feb-2022
# # usage:
# # calling function:
from publisher.serializers import ShopSerializer
from users.models import LocalUser
from . models import Shop
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from users.serializers import LocalUserSerializer
from rest_framework_simplejwt.tokens import RefreshToken


@api_view(['GET'])
@permission_classes([])
@authentication_classes([])
def publisherOrderListView(request):
    if request.method == 'GET':
        pass
    else:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def registerPublisherView(request):
    if request.method == 'POST':
        try:
            # checks if the number already exists
            user = LocalUser.objects.get(username=request.data['username'])
            return Response(status=status.HTTP_409_CONFLICT)

        except LocalUser.DoesNotExist:
            request.data['isPublisher'] = True
            instance = LocalUserSerializer(data=request.data)
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


@api_view(['GET'])
@permission_classes([])
@authentication_classes([])
def publisherListView(request, pincode='208011'):
    if request.method == 'GET':
        try:
            publisherInstanceList = LocalUser.objects.get(
                pincode=pincode, isPublisher=True)
            serializedData = LocalUserSerializer(
                publisherInstanceList)
            return Response(data=serializedData.data)
        except LocalUser.DoesNotExist:
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
            serializedData = LocalUserSerializer(
                publisherInstanceList, many=True)
            return Response(data=serializedData.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


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
