from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics

from django.http import Http404
from django.shortcuts import get_object_or_404
# Create your views here.
from Example2.models import Example2
from Example2.serializer import Example2Serializer

class ExampleList2(APIView):
    def get(self,request, format = None):
        print("Get")
        queryset = Example2.objects.all() 
        serializer = Example2Serializer(queryset, many = True)
        return Response(serializer.data)
    
    def post (self,request, format = None):
        serializer = Example2Serializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
