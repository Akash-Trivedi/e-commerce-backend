# date-created: 19-feb-2022
# usage: return the json string after querying the database
# calling function/module: product/urls.py

from .serializers import (ProductSerializer, TagSerializer)
from .models import Product, Tag
from rest_framework.generics import ListAPIView, ListCreateAPIView

# below is the alternative to redundant code
# retrieve uses the pk(primary key for retrieval of the data)
class TagView(ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


# class TagView(View):

#     def get(self, request):
#         try:
#             tagList = Tag.objects.all()
#         except ValueError: return HttpResponse("<h1>No Tags !</h1>")
#         except: return HttpResponse("<h1>Server Encountered Some</h1>")

#         # serialize the instance array and return binary output
#         serializedTag = TagSerializer(tagList, many=True)
#         return JsonResponse(serializedTag.data, safe=False, status=status.HTTP_200_OK)

class ProductView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# class ProductView(View):
#     # default pincode=website owner

#     def get(self, request, pincode='208012'):
#         # get the products based on location
#         # pincode to be send by the browser in get request

#         try:
#             if 'pincode' in request.GET:
#                 pincode = request.GET['pincode']
#             productInstanceList = Product.objects.all()
#             productSerializedData = ProductSerializer(
#                 productInstanceList, many=True)

#         except ValueError:
#             return HttpResponse("<h1>content not found</h1>")
#         except:
#             return HttpResponse("<h1>content not found</h1>")
#         else:
#             return JsonResponse(productSerializedData.data, safe=False)

#     def post(self, request):
#         self.put(request)

#     def put(self, request):
#         jsonData = JSONParser().parse(request)
#         productObject = ProductSerializer(data=jsonData)
#         if productObject.is_valid():
#             productObject.save()

#     def delete(self, request):
#         pass


# class ProductRegister(View):

#     def post(self, request):
#         request.data
