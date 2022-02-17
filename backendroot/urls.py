# date-created: 17-feb-2022
# usage: root url config, handles the incomming links via routing
# calling function:

from django.contrib import admin
from django.urls import path, include
# rest_framework from installed apps
from restapi.serializers import UserViewSet
from rest_framework import routers, serializers, viewsets

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='restFramework')),
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
]
