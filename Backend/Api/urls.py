
from django.contrib import admin
from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import ObtainAuthToken


router = DefaultRouter()

router.register('product',Productdetails,basename='products')

urlpatterns = [
    path('',include(router.urls)),
    path('signup/',studentsignup.as_view()),
    path('api-auth-token/',ObtainAuthToken.as_view())
]