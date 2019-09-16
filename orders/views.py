from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from .serializers import OrderCreateSerializer, WarehouseSerializer
from rest_framework import status


class OrderView(ViewSet):

    def create(self, request):
        serial = OrderCreateSerializer(data=request.data)

        if serial.is_valid(raise_exception=True):
            serial.save()
            return Response({serial.data}, status=status.HTTP_201_CREATED)

        return Response(serial.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class WarehouseView(ViewSet):

    def create(self, request):
        serial = WarehouseSerializer(data=request.data)

        if serial.is_valid(raise_exception=True):
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)

        return Response(serial.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



