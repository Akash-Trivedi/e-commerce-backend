# date-created: 19-feb-2022
# usage: return the json string after querying the database
# calling function/module: product/urls.py

from .serializers import ProductSerializer, TagSerializer
from .models import Product, Tag
from django.views import View
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.parsers import JSONParser
from publisher.models import Publisher


class TagView(View):

    def get(self, request):
        try:
            tagList = Tag.objects.all()
        except ValueError:
            return HttpResponse("<h1>No Tags !</h1>")
        except:
            return HttpResponse("<h1>Server Encountered Some</h1>")

        # serialize the instance array and return binary output
        serializedTag = TagSerializer(tagList, many=True)
        return JsonResponse(serializedTag.data, safe=False, status=status.HTTP_200_OK)


class ProductView(View):
    # default pincode=website owner
    pincode = '208012'

    def get(self, request, pincode='208012'):
        # get the products based on location
        try:
            if pincode is not None: self.pincode = pincode

            publisherList = Publisher.objects.filter(pincode=self.pincode)
            prodcutList = Product.objects.filter()

        except ValueError:
            return HttpResponse("<h1>content not found</h1>")
        except:
            return HttpResponse("<h1>content not found</h1>")
        else:
            return JsonResponse()

    def post(self, request):
        self.put(request)

    def put(self, request):
        jsonData = JSONParser().parse(request)
        productObject = ProductSerializer(data=jsonData)
        if productObject.is_valid():
            productObject.save()

    def delete(self, request):
        pass


class ProductRegister(View):

    def post(self, request):
        request.data
