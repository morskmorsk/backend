from rest_framework import serializers
from .models import (
    Department,
    Location,
    DeviceDefect,
    Device,
    WorkOrderCart,
    WorkOrderCartItem,
    Order,
    OrderItem
    )


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class DeviceDefectSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceDefect
        fields = '__all__'


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'


class WorkOrderCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkOrderCart
        fields = '__all__'


class WorkOrderCartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkOrderCartItem
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'
