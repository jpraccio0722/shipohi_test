from rest_framework import serializers
from ..models import Order, Address


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = ('address1', 'address2', 'city', 'state_province', 'post_code', 'country_code')


