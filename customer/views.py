from pyexpat import model

from django.http import HttpResponse
from .models import Customer
from .serializers import CustomerSerializer, CustomerOrderSummarySerializer
from rest_framework.generics import ListAPIView, ListCreateAPIView


# folowing is the alternative to the redundant things we
# do just to fetch and print the json data
class CustomerView(ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerOrderSummaryView(ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerOrderSummarySerializer

# class CustomerView(APIView):
#     def get(self, request, *args, **kwargs):
#         try:
#             instanceList = Customer.objects.all()
#             serializeData = CustomerSerializer(instanceList, many=True)
#             return JsonResponse(serializeData.data, safe=False)
#         except:
#             return render(request, 'customer/error.html')

#     def post(self, request, *args, **kwargs):
#         pass


class CustomerRegistrationView(ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def create(self, request, *args, **kwargs):
        pass
