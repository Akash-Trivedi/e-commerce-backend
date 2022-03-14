# date-created: 17-feb-2022
# usage: root url config, handles the incomming links via routing
# calling function:

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('product/', include('product.urls')),
    path('publisher/', include('publisher.urls')),
    path('customer/', include('customer.urls')),
    path('admin', admin.site.urls),
]
# path('api-auth/', include('rest_framework.urls', namespace='restFramework')),
# path('api-auth/', include('rest_framework.urls')),
