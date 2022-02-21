# date-created: 17-feb-2022
# usage:
# calling function:

from ast import Not
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View

from publisher.serializers import ShopSerializer, PublisherSerializer

from . models import PublisherAuth, Shop, Publisher
from rest_framework.parsers import JSONParser


class PublisherRegistration(View):
    def get(self, request):
        pass

    def post(self, request):
        # on signup, get contact for existing user
        # serialize the request object to PublisherAuth
        jsonData = JSONParser().parse(request)
        # assume single json object's first parameter= contact
        contact = jsonData['contact']
        if PublisherAuth.objects.get(pk=contact):
            return JsonResponse(jsonData)
        else:
            PublisherAuth(contact=contact)


class PublisherView(View):
    def get(self, request):
        try:
            if 'publisher-pincode' in request.GET:
                print(f"printing post request inputs: {request.GET['publisher-pincode']}")
                print(f"printing whole request: {request}")
                publishersList = Publisher.objects.filter(pincode=request.GET['publisher-pincode'])
            else:
                publishersList = Publisher.objects.all()
            publishersSerializedData = PublisherSerializer(
                publishersList, many=True)
        except:
            print('pincode not found')
            return render(request, 'publisher/error.html', {'error':Exception()})
        else:
            return JsonResponse(publishersSerializedData.data, safe=False)


class ShopView(View):
    def get(self, request):
        try:
            shopsList = Shop.objects.all()
            shopsSerializedData = ShopSerializer(shopsList, many=True)
        except ValueError:
            pass
        else:
            return JsonResponse(shopsSerializedData.data, safe=False)
