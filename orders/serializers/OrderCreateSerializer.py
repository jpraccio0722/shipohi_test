from rest_framework import serializers
from ..models import Order, Address, Customer, LineItem
from orders.serializers.AddressSerializer import AddressSerializer
from orders.serializers.CustomerSerializer import CustomerSerializer
from orders.serializers.LineItemSerializer import LineItemSerializer
from orders.helpers.bing_api import get_lat_lon, find_nearest_warehouse
import logging


class OrderCreateSerializer(serializers.ModelSerializer):

    logger = logging.getLogger(__name__)

    shipping_address = AddressSerializer(many=False)
    line_items = LineItemSerializer(many=True)
    customer = CustomerSerializer(many=False)

    class Meta:
        model = Order
        fields = ('shipping_address', 'customer', 'line_items', 'status')

    def create(self, validated_data):
        address = Address.objects.update_or_create(**validated_data.pop('shipping_address'))

        lat, lon = get_lat_lon(address=address[0])

        customer = Customer.objects.update_or_create(**validated_data.pop('customer'))

        line_items_data = validated_data.pop('line_items')
        status = validated_data.pop('status')
        status = status.replace('\"', '')

        instance = Order.objects.update_or_create(shipping_address=address[0],
                                                  customer=customer[0],
                                                  status=status)

        warehouse = None

        if lat and lon:
            address[0].lat = lat
            address[0].lon = lon

            warehouse = find_nearest_warehouse(address=address[0])

            if warehouse:
                instance.warehouse_origin = warehouse

        for item in line_items_data:
            line_item = LineItem.objects.create(**item)
            line_item.order = instance
            line_item.save()

        return instance




