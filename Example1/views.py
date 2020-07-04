from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics

from django.http import Http404
from django.shortcuts import get_object_or_404
# Create your views here.
from Example1.models import Example1
from Example1.serializer import Example1Serializer

class ExampleList(APIView):
    def get(self,request, format = None):
        print("Get")
        queryset = Example1.objects.all() 
        serializer = Example1Serializer(queryset, many = True)
        return Response(serializer.data)
    
    def post (self,request, format = None):
        serializer = Example1Serializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        else:
            return Response(serializer.errors)

class ExampleDetail(APIView):
    def get_object(self,id):
        try:
            return Example1.objects.get(pk = id)
        except Example1.DoesNotExist :
            return 404

    def get(self,request,id ,format=None):
        example1 = self.get_object(id)
        if example1 == 404:
            return Response(example1)
        else:
            serializer = Example1Serializer(example1)
            return Response(serializer.data)


    def put (self,request,id,format=None):
        otro = self.get_object(id)
        serializer = Example1Serializer(otro,data= request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        else:
            return Response(serializer.errors)