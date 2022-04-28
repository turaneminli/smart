from django.shortcuts import render
from rest_framework import serializers
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView

from users.models import Bulb, CustomUser
from .serializers import BulbSerializer, CustomUserSerializer

from .tasks import multiply_by_ten, mul_ten

from .serializers import CelerySerializer

from rest_framework.response import Response

import time

# Create your views here.




class UsersList(ListAPIView):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()

# This is just an example. DELETE it when starting a new project
class MultiTen(APIView):
    serializer_class = CelerySerializer

    def post(self, request):
        serializer = CelerySerializer(data=request.data)
        if serializer.is_valid():
            num = serializer.validated_data.get('number')

            # asynchronous task
            new_num = multiply_by_ten.delay(num) 

            # regular task
            # new_num = mul_ten(num)

            return Response({'response':'Success'})

class BulbList(ListAPIView):
    queryset = Bulb.objects.all()
    serializer_class = BulbSerializer
