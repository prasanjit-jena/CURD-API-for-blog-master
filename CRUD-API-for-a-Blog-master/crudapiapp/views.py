from django.shortcuts import render
from .models import BlogData
from .serializers import BlogDataSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import authentication_classes,permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class BlogDataView(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self,request,Format=None):
        queryset=BlogData.objects.all()
        serializer_class=BlogDataSerializer(queryset,many=True)
        return Response(serializer_class.data)
    
    def post(self,request,Format=None):
        serializer_class=BlogDataSerializer(data=request.data,many=True)
        if serializer_class.is_valid():
            serializer_class.save()
            result={'message':'Successfully Saved'}
            return Response(result,status.HTTP_201_CREATED)
        else:
            return Response(serializer_class.errors)

class BlogDataID(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self,request,pk,Format=None): 
        queryset=BlogData.objects.get(pk=pk)
        serializer_class=BlogDataSerializer(queryset)
        return Response(serializer_class.data)

    def put(self,request,pk,Format=None):
        queryset=BlogData.objects.get(pk=pk)
        serializer_class=BlogDataSerializer(queryset,data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            result={'message':'Successfully Updated'}
            return Response(result,status.HTTP_201_CREATED)
        else:
            return Response(serializer_class.errors)
    
    def delete(self,request,pk,Format=None):
        queryset=BlogData.objects.get(pk=pk)
        queryset.delete()
        return Response({'message':'Deleted Successfully'})
    
