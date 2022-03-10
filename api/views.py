import random
from django.http import JsonResponse
from rest_framework.generics import CreateAPIView

from publisher.serializers import PublishAuthSerializer


class RegisterPublisher(CreateAPIView):
    """
    this view will handle the post request for submission of new publisher.
    """
    serializer_class = PublishAuthSerializer


def registerCustomer(request):
    pass


def registerPublisher(request):
    request.auth
    request.user
    if request.method == 'POST':
        result = {
            "response": "ok"
        }
        return JsonResponse(result)


def randomOtp(request, contactNumber):
    try:
        if request.method == "GET":
            otp = random.randrange(100000, 999999)
            print(f'otp for {contactNumber} is {otp}')
            context = {
                "result": otp
            }
            return JsonResponse(context)
        else:
            context = {
                "result": "error"
            }
            return JsonResponse(context)
    except:
        return
#
