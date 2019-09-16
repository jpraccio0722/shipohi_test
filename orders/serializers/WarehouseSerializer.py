from orders.serializers.AddressSerializer import AddressSerializer
from rest_framework import serializers
from ..models import Warehouse, Address
from orders.helpers.bing_api import get_lat_lon
import logging


class WarehouseSerializer(serializers.ModelSerializer):

    address = AddressSerializer(many=False)

    class Meta:
        model = Warehouse
        fields = ('address',)

    def create(self, validated_data):
        logger = logging.getLogger(__name__)

        address = Address.objects.update_or_create(**validated_data.pop('address'))

        address_model = address[0]

        lat, lon = get_lat_lon(address=address_model)

        if lat and lon:
            address_model.lat = lat
            address_model.lon = lon
            address_model.save()

        return Warehouse.objects.create(address=address_model)


