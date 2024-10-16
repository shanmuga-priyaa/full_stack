from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework .generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from .models import *
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .forms import UserCreationForm,StudentForm
from rest_framework.viewsets import ModelViewSet
from .serializers import *

from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny,IsAuthenticatedOrReadOnly
from rest_framework.authentication import BasicAuthentication,SessionAuthentication,TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter



class studentsignup(APIView):
    def post(self,request):
        user_data = request.data['user']
        
        std_data =  {
                        'name':request.data['name'],
                        'mobile_name':request.data['mobile_name'],
                        'course':request.data['course'],
                        'fees':request.data['fees'],
                    }
        print(std_data)
        print(user_data)
        user_form = UserCreationForm(user_data)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_data['password'])
            new_user.save()

        new_student = Student(user = new_user,
                              name = std_data['name'],
                              mobile_name = std_data['mobile_name'],
                              course = std_data['course'],
                              fees = std_data['fees'],
                              )
        new_student.save()
        return Response("data save")

class Productdetails(ModelViewSet):
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticatedOrReadOnly]
    permission_classes = [AllowAny]
    queryset = product.objects.all()
    serializer_class = ProductSerializer

    # filter_backends = [SearchFilter,DjangoFilterBackend,OrderingFilter]
    # search_fields = ['brand_name','model_name']
    # filterset_fields = ['price','brand_name']
    # Ordering_fields = ['id','price']

# class Productdetails(ModelViewSet):
#     permision_classes = [AllowAny]
#     queryset = product.objects.all()
#     serializer_class = ProductSerializer

