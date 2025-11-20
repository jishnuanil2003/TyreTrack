from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import InventoryModel
from .serializers import InventorySerializers
from rest_framework.permissions import AllowAny,IsAuthenticatedOrReadOnly
# Create your views here.
class InventoryItemsView(APIView):
    permission_classes = [AllowAny]
    def get(self,request):
        objects = InventoryModel.objects.all()
        serializers = InventorySerializers(objects,many=True)
        return Response(serializers.data,status=status.HTTP_200_OK)
    def post(self,request):
        serializers = InventorySerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
        
class InventoryItemsUpdateView(APIView):
    permission_classes = [AllowAny]

    def get_object(self,pk):
        try:
            return InventoryModel.objects.get(pk=pk)
        except InventoryModel.DoesNotExist:
            return None
    def get(self,request,pk):
        object = self.get_object(pk)
        if not object:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializers = InventorySerializers(object)
        return Response(serializers.data,status=status.HTTP_200_OK)
    def put(self,request,pk):
        object = self.get_object(pk)
        if not object:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = InventorySerializers(object,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        object = self.get_object(pk)
        if not object:
            return Response(status=status.HTTP_404_NOT_FOUND)
        object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
