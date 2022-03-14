from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/otp/<slug:contactNumber>/', views.randomOtp, name='random_otp'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api-authorization1/', include('rest_framework.urls')),
    # below api is kept at last because if url is api/otp then it would go to backend.urls and this will slow down the process
    path('api/', include('backendroot.urls')),
]