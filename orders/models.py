from django.db import models
import uuid


class Order(models.Model):

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)

    shipping_address = models.ForeignKey('Address', on_delete=models.PROTECT)
    customer = models.ForeignKey('Customer', on_delete=models.PROTECT)
    status = models.CharField(max_length=256, null=True)
    warehouse_origin = models.ForeignKey('Warehouse', on_delete=models.PROTECT, null=True)


class Address(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)

    address1 = models.TextField(default='')
    address2 = models.TextField(default='')
    city = models.CharField(max_length=256)
    state_province = models.CharField(max_length=256, default='')
    post_code = models.CharField(max_length=256, default='')
    country_code = models.CharField(max_length=2, default='')
    lat = models.FloatField(null=True)
    lon = models.FloatField(null=True)


class Customer(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    first_name = models.TextField(default='')
    last_name = models.TextField(default='')
    phone = models.TextField(default='')
    email = models.TextField(default='')


class LineItem(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    sku = models.TextField(default='')
    name = models.TextField(default='')
    quantity = models.IntegerField(default=0)
    price = models.FloatField(default=0.0)
    order = models.ForeignKey('Order', on_delete=models.PROTECT)


class Warehouse(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    address = models.ForeignKey('Address', on_delete=models.CASCADE)
