# author: akash trivedi
# date-created: 1-march-2022
# functionality: handle the incomming requests
# caller: customer\urls.py


from users.models import LocalUser
from .models import Feedback
from .serializers import FeedbackSerializer, CustomerOrderSummarySerializer
from users.serializers import LocalUserSerializer

from rest_framework.decorators import (
    api_view, permission_classes, authentication_classes, APIView)
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken


def p():
    print('\n'+'-'*16+'NEW REQUEST'+'-'*16+'\n')


class CustomerListView(APIView):
    def get(self, request):
        try:
            publisherInstanceList = LocalUser.objects.all()
            serializedData = LocalUserSerializer(
                publisherInstanceList, many=True)
            print(serializedData.data)
            return Response(data=serializedData.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CustomerFeedbackView(APIView):
    def get(self, request):
        try:
            data = {}
            feedbackInstanceList = Feedback.objects.all()
            serializedData = FeedbackSerializer(
                feedbackInstanceList, many=True)
            data['status'] = 200
            data['payload'] = serializedData.data
            return Response(data=data, status=status.HTTP_200_OK)
        except Feedback.DoesNotExists:
            data['status'] = 204
            data['payload'] = []
            return Response(data=data, status=status.HTTP_204_NO_CONTENT)


class CustomerOrderSummaryView(APIView):
    def get(self, request):
        try:
            feedbackInstanceList = Feedback.objects.all()
            serializedData = CustomerOrderSummarySerializer(
                feedbackInstanceList, many=True)
            print(serializedData.data)
            return Response(data=serializedData.data, status=status.HTTP_200_OK)
        except Feedback.DoesNotExists:
            return Response(status=status.HTTP_204_NO_CONTENT)


class CustomerSignupView(APIView):

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
            instance = LocalUserSerializer().create(formData, isPublisher=False)
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


class CustomerProfileUpdateView(APIView):
    
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
