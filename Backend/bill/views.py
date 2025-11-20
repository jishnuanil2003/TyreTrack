from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .models import BillModel
from inventory.models import InventoryModel
from .serializers import BillSerializers

# Create your views here.
class BillView(APIView):
    permission_classes = [AllowAny]
    def get(self,request):
        objects = BillModel.objects.all()
        serializers  = BillSerializers(objects,many=True)
        return Response(serializers.data,status=status.HTTP_200_OK)
    def post(self,request):
        serializers = BillSerializers(data=request.data)
        if serializers.is_valid():
            service = serializers.validated_data.get("service")
            
            if service == 'Tyre':
                tyre_name = serializers.validated_data.get('tyre_name')
                tyre_size = serializers.validated_data.get('tyre_size')
                qty = int(serializers.validated_data.get('quantity'))

                try:
                    item = InventoryModel.objects.get(
                        item_name = tyre_name,
                        item_size = tyre_size
                    )
                except InventoryModel.DoesNotExist:
                    return Response(
                        {"error": "Tyre not found in inventory"},
                        status=status.HTTP_400_BAD_REQUEST
                    )
                if item.quantity < qty:
                    return Response(
                        {"error": "Not enough stock available"},
                        status=status.HTTP_400_BAD_REQUEST
                    )
                item.quantity -= qty
                item.save()
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

