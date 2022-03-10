# # date-created: 17-feb-2022
# # usage:
# # calling function:

from urllib import response
from publisher.serializers import PublishAuthSerializer, ShopSerializer, PublisherSerializer
from . models import PublisherAuth, Shop, Publisher
from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_500_INTERNAL_SERVER_ERROR


@api_view(['POST'])
def registerPublisher(request):
    try:
        instance = PublishAuthSerializer(request.data)
        if instance.is_valid():
            instance.save()
        return Response(status=HTTP_201_CREATED)
    except:
        return Response(status=HTTP_500_INTERNAL_SERVER_ERROR)

# class PublisherAuthRegistration(APIView):
#     def post(self, request):
#         # Permission checks are always run at the very start of the view,
#         # before any other code is allowed to proceed
#         try:
#             serializedUserData = PublishAuthSerializer()
#             print(serializedUserData)
#             if serializedUserData.is_valid():
#                 serializedUserData.save()
#                 return render(request, 'publisher/success.html')
#             else: return render(request, 'publisher/invalid.html')
#         except:
#             return render(request, 'publisher/error.html')
#         else: return render(request, 'backendroot/test.html')


# class PublisherRegistration(View):
#     def get(self, request):
#         pass

#     def post(self, request):
#         # on signup, get contact for existing user
#         # serialize the request object to PublisherAuth
#         jsonData = JSONParser().parse(request)
#         # assume single json object's first parameter= contact
#         contact = jsonData['contact']
#         if PublisherAuth.objects.get(pk=contact):
#             return JsonResponse(jsonData)
#         else:
#             PublisherAuth(contact=contact)
class PublisherView(ListAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

# class PublisherView(View):
#     def get(self, request):
#         try:
#             if 'publisher-pincode' in request.GET:
#                 publishersList = Publisher.objects.filter(
#                     pincode=request.GET['publisher-pincode'])
#             else:
#                 publishersList = Publisher.objects.all()
#             publishersSerializedData = PublisherSerializer(
#                 publishersList, many=True)
#         except:
#             print('pincode not found')
#             return render(request, 'publisher/error.html', {'error': Exception()})
#         else:
#             return JsonResponse(publishersSerializedData.data, safe=False)


class ShopView(ListAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
# class ShopView(View):
#     def get(self, request):
#         try:
#             shopsList = Shop.objects.all()
#             shopsSerializedData = ShopSerializer(shopsList, many=True)
#         except ValueError:
#             pass
#         else:
#             return JsonResponse(shopsSerializedData.data, safe=False)
