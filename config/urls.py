from django.urls import path, include
from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [

    path('admin/', admin.site.urls),

    path('user/',include('Users.urls')),
    path('api-token-auth/', obtain_auth_token),

    path('',include('UnityRankAPI.urls')),
]