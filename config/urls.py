from django.urls import path, include
from django.contrib import admin

urlpatterns = [

    path('admin/', admin.site.urls),

    path('user/',include('Users.urls')),


    path('',include('UnityRankAPI.urls')),
]